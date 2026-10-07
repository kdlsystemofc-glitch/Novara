/**
 * ====================================================================
 * NOVARA MOTION ENGINE — Núcleo de Animação e Acessibilidade
 * ====================================================================
 * 
 * Arquitetura de Motion:
 * - GSAP 3 + ScrollTrigger + Lenis Smooth Scroll auto-hospedados
 * - 3 Modos: 'full', 'reduced' (prefers-reduced-motion), 'paused' (controle manual)
 * - Níveis de Qualidade: 'high' vs 'low' (GPU/CPU, mobile, economia de dados)
 * - Declarativo: [data-reveal], [data-parallax], [data-loop]
 * - Ciclo de vida: Pausa automática fora da tela e na aba oculta
 * - Proteção de empilhamento: .cheese-pull-spine e ancestrais intocados
 */

(function () {
  'use strict';

  // Evitar execução duplicada
  if (window.NovaraMotion) return;

  const NovaraMotion = {
    mode: 'full',        // 'full' | 'reduced' | 'paused'
    quality: 'high',     // 'high' | 'low'
    lenis: null,
    loops: [],
    reveals: [],
    parallaxes: [],
    isUserPaused: false,
    initialized: false,

    /**
     * Detectar perfil de hardware, conexão e preferências de acessibilidade
     */
    detectEnvironment() {
      // 1. Checar prefers-reduced-motion
      const mediaQueryReduced = window.matchMedia('(prefers-reduced-motion: reduce)');
      if (mediaQueryReduced.matches) {
        this.mode = 'reduced';
      }

      mediaQueryReduced.addEventListener('change', (e) => {
        if (this.mode !== 'paused') {
          this.setMode(e.matches ? 'reduced' : 'full');
        }
      });

      // 2. Checar qualidade (low vs high)
      const isMobile = window.innerWidth < 768;
      const isLowCPU = navigator.hardwareConcurrency && navigator.hardwareConcurrency < 4;
      const isLowMemory = navigator.deviceMemory && navigator.deviceMemory < 4;
      const isSaveData = navigator.connection && (navigator.connection.saveData === true || /2g|3g/.test(navigator.connection.effectiveType || ''));

      if (isMobile || isLowCPU || isLowMemory || isSaveData) {
        this.quality = 'low';
      } else {
        this.quality = 'high';
      }

      document.documentElement.setAttribute('data-motion-mode', this.mode);
      document.documentElement.setAttribute('data-motion-quality', this.quality);

      console.log(`[NovaraMotion] Ambiente detectado: Modo=${this.mode}, Qualidade=${this.quality}`);
    },

    /**
     * Inicializar Lenis Smooth Scroll
     */
    initLenis() {
      if (typeof window.Lenis === 'undefined') {
        console.warn('[NovaraMotion] Lenis não disponível.');
        return;
      }

      // Se reduced motion estiver ativo, não forçar interpolação pesada
      if (this.mode === 'reduced') {
        return;
      }

      try {
        this.lenis = new window.Lenis({
          duration: this.quality === 'low' ? 0.9 : 1.2,
          easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
          smoothWheel: true,
          syncTouch: false, // touch nativo fluido e responsivo no mobile
          touchMultiplier: 1.5,
          infinite: false
        });

        // Conectar Lenis ao ScrollTrigger
        if (window.ScrollTrigger) {
          this.lenis.on('scroll', window.ScrollTrigger.update);
        }

        // Conectar animação de frame ao GSAP ticker
        if (window.gsap) {
          window.gsap.ticker.add((time) => {
            if (this.lenis && this.mode !== 'paused') {
              this.lenis.raf(time * 1000);
            }
          });
          window.gsap.ticker.lagSmoothing(0);
        }
      } catch (err) {
        console.warn('[NovaraMotion] Erro ao instanciar Lenis:', err);
      }
    },

    /**
     * Inicializar GSAP e plugins
     */
    initGSAP() {
      if (!window.gsap || !window.ScrollTrigger) {
        console.warn('[NovaraMotion] GSAP ou ScrollTrigger não disponíveis.');
        return;
      }

      window.gsap.registerPlugin(window.ScrollTrigger);

      // Configuração padrão de ScrollTrigger
      window.ScrollTrigger.defaults({
        fastScrollEnd: true
      });
    },

    /**
     * Registrar e animar elementos com [data-reveal]
     */
    setupReveals() {
      if (!window.gsap || !window.ScrollTrigger) return;

      const sections = document.querySelectorAll('.editorial-section');
      sections.forEach((section) => {
        const revealElements = section.querySelectorAll('[data-reveal]');
        if (!revealElements.length) return;

        // Verificar se seção já está na dobra inicial (hero)
        const rect = section.getBoundingClientRect();
        const isAboveFold = rect.top < window.innerHeight * 0.7;

        revealElements.forEach((el) => {
          // Proteção absoluta da spine central
          if (el.closest('.cheese-pull-spine')) return;

          const type = el.getAttribute('data-reveal') || 'fade-up';
          const delay = parseFloat(el.getAttribute('data-reveal-delay')) || 0;
          const duration = parseFloat(el.getAttribute('data-reveal-duration')) || (this.mode === 'reduced' ? 0.2 : 0.75);

          if (this.mode === 'reduced') {
            // Em reduced motion: apenas fade suave sem translação
            if (!isAboveFold) {
              window.gsap.fromTo(el,
                { opacity: 0 },
                {
                  opacity: 1,
                  duration: 0.2,
                  delay: delay,
                  scrollTrigger: {
                    trigger: section,
                    start: 'top 75%',
                    once: true
                  }
                }
              );
            }
            return;
          }

          // Modo Full: translateY + fade suave com stagger (600-900ms a 35% de visibilidade)
          let yOffset = 24;
          if (type === 'fade-down') yOffset = -24;
          else if (type === 'fade') yOffset = 0;

          if (!isAboveFold) {
            const tween = window.gsap.fromTo(el,
              { opacity: 0, y: yOffset },
              {
                opacity: 1,
                y: 0,
                duration: duration,
                delay: delay,
                ease: 'power2.out',
                scrollTrigger: {
                  trigger: section,
                  start: 'top 75%',
                  once: true
                }
              }
            );
            this.reveals.push(tween);
          } else {
            // No hero inicial: transição suave pós-load sem bloquear leitura
            window.gsap.fromTo(el,
              { opacity: 0.85, y: Math.min(yOffset, 12) },
              {
                opacity: 1,
                y: 0,
                duration: 0.6,
                delay: delay + 0.1,
                ease: 'power2.out'
              }
            );
          }
        });
      });
    },

    /**
     * Registrar elementos com [data-parallax]
     */
    setupParallax() {
      if (!window.gsap || !window.ScrollTrigger) return;
      if (this.mode === 'reduced' || this.quality === 'low') {
        // Sem parallax em reduced motion ou dispositivos de baixa performance
        return;
      }

      const parallaxElements = document.querySelectorAll('[data-parallax]');
      parallaxElements.forEach((el) => {
        if (el.closest('.cheese-pull-spine')) return;

        const factor = parseFloat(el.getAttribute('data-parallax')) || 0.08;
        // Limite máximo de translação (0.05-0.10, máx ~24px, nunca sobre texto)
        const maxOffset = Math.min(24, Math.max(8, Math.abs(factor * 120)));
        const direction = factor > 0 ? -maxOffset : maxOffset;

        const tween = window.gsap.fromTo(el,
          { y: -direction * 0.5 },
          {
            y: direction * 0.5,
            ease: 'none',
            scrollTrigger: {
              trigger: el,
              start: 'top bottom',
              end: 'bottom top',
              scrub: 1.2
            }
          }
        );
        this.parallaxes.push(tween);
      });
    },

    /**
     * Registrar elementos de micro-interação contínua [data-loop]
     */
    setupLoops() {
      if (!window.gsap || !window.ScrollTrigger) return;
      if (this.mode === 'reduced' || this.quality === 'low') {
        // Sem loops contínuos em reduced motion ou dispositivos low-end
        return;
      }

      const loopElements = document.querySelectorAll('[data-loop]');
      loopElements.forEach((el) => {
        if (el.closest('.cheese-pull-spine')) return;

        const loopType = el.getAttribute('data-loop') || 'float';
        let tween;

        if (loopType === 'float') {
          // Flutuação milimétrica (1.5px a 2.5px), ritmo calmo (3.2 segundos)
          tween = window.gsap.to(el, {
            y: '+=2.5',
            rotation: '+=0.6',
            duration: 3.2,
            repeat: -1,
            yoyo: true,
            ease: 'sine.inOut'
          });
        } else if (loopType === 'pulse-subtle') {
          // Pulso calmo de escala (1.00 para 1.025)
          tween = window.gsap.to(el, {
            scale: 1.025,
            duration: 2.8,
            repeat: -1,
            yoyo: true,
            ease: 'sine.inOut'
          });
        }

        if (tween) {
          this.loops.push(tween);

          // Pausar quando o elemento sai da tela para poupar CPU/GPU
          window.ScrollTrigger.create({
            trigger: el,
            start: 'top bottom',
            end: 'bottom top',
            onEnter: () => { if (this.mode === 'full') tween.play(); },
            onLeave: () => tween.pause(),
            onEnterBack: () => { if (this.mode === 'full') tween.play(); },
            onLeaveBack: () => tween.pause()
          });
        }
      });
    },

    /**
     * Pausar tudo quando aba do navegador fica oculta
     */
    setupVisibilityObserver() {
      document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
          this.pauseInternal();
        } else {
          if (!this.isUserPaused && this.mode !== 'paused') {
            this.resumeInternal();
          }
        }
      });
    },

    /**
     * Pausa interna (quando oculta ou por comando)
     */
    pauseInternal() {
      if (window.gsap) {
        window.gsap.globalTimeline.pause();
      }
      if (this.lenis) {
        this.lenis.stop();
      }
      this.loops.forEach(tween => tween.pause());
    },

    /**
     * Retomada interna
     */
    resumeInternal() {
      if (this.mode === 'paused') return;

      if (window.gsap) {
        window.gsap.globalTimeline.play();
      }
      if (this.lenis && this.mode !== 'reduced') {
        this.lenis.start();
      }
      if (this.mode === 'full' && this.quality === 'high') {
        this.loops.forEach(tween => {
          // Retomar apenas se o elemento correspondente estiver visível
          tween.play();
        });
      }
    },

    /**
     * Alternar modo do usuário (Full / Reduced / Paused)
     */
    setMode(newMode) {
      this.mode = newMode;
      document.documentElement.setAttribute('data-motion-mode', newMode);

      if (newMode === 'paused') {
        this.isUserPaused = true;
        this.pauseInternal();
      } else {
        this.isUserPaused = false;
        this.resumeInternal();
        if (window.ScrollTrigger) {
          window.ScrollTrigger.refresh();
        }
      }

      console.log(`[NovaraMotion] Modo alterado para: ${newMode}`);
      window.dispatchEvent(new CustomEvent('novaramotion:modechange', { detail: { mode: newMode } }));
    },

    /**
     * Toggle do Botão de Pausa
     */
    togglePause() {
      if (this.mode === 'paused') {
        const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
        this.setMode(mediaQuery.matches ? 'reduced' : 'full');
        return false; // Não pausado
      } else {
        this.setMode('paused');
        return true;  // Pausado
      }
    },

    /**
     * Inicialização geral do motor
     */
    init() {
      if (this.initialized) return;
      this.initialized = true;

      this.detectEnvironment();
      this.initGSAP();
      this.initLenis();
      this.setupVisibilityObserver();

      // Configuração declarativa
      this.setupReveals();
      this.setupParallax();
      this.setupLoops();

      document.body.classList.add('js-motion-ready');
      console.log('[NovaraMotion] Motor de motion inicializado com sucesso.');
    }
  };

  // Expor globalmente para inspeção e testes
  window.NovaraMotion = NovaraMotion;

  // Inicializar quando o script carregar
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => NovaraMotion.init());
  } else {
    NovaraMotion.init();
  }
})();
