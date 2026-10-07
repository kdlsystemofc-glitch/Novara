# INVENTÁRIO DE MOTION E RITMO EDITORIAL — NOVARA

**Data:** 07/10/2026  
**Status:** FASE C Concluída — Tag: `motion-pronto`  
**Vídeo do Walkthrough:** [`screenshots/videos/novara_motion_walkthrough.webm`](file:///c:/Oficial/Novara%203/screenshots/videos/novara_motion_walkthrough.webm)

---

## 1. Arquitetura do Motor de Motion (`site/js/motion.js`)

- **Bibliotecas:** GSAP 3.14.2, ScrollTrigger 3.14.2 e Lenis 1.3.26 (100% auto-hospedados em `site/js/vendor/`, zero CDN, compatível com `file://`).
- **Estratégia de Carregamento:** Diferido após evento `load` via `requestIdleCallback` (fallback 800ms) ou acionado imediatamente na primeira interação (`scroll`, `pointerdown`, `touchstart`).
- **Above-the-Fold:** Nada na dobra inicial depende de JavaScript para renderizar. Textos e imagens têm `opacity: 1` intrínseco.
- **Proteção do Fio de Queijo Contínuo (`.cheese-pull-spine`):** Mantido fixo e estático. Nenhum ancestral recebe `transform`, `filter` ou `opacity < 1`.

---

## 2. Inventário Completo de Animações por Seção

### Seção 1: Hero & Crust Alchemy (`#hero-crust-alchemy`)
| Elemento | Seletor | Tipo de Motion | Easing / Duração / Delay | Comportamento Visual |
| :--- | :--- | :---: | :---: | :--- |
| Badge Google | `.badge-social-proof` | `reveal (fade-down)` | `power2.out` / 600ms / 0s | Assentamento sutil de topo |
| Selo Cera Topo | `.hero-wax-container` | `reveal (fade-down)` | `power2.out` / 600ms / 0.1s | Entrada defasada do selo artesanal |
| Título Monumental | `.brand-hero-title` | `reveal (fade-up)` | `power2.out` / 600ms / 0.05s | Desdobramento vertical calmo |
| Folha Manjericão | `.sticker-basil-wrap` | `loop (float)` | `sine.inOut` / 3.2s / y: +2.5px | Flutuação orgânica sutil (só high quality) |
| Sticker Smile | `.sticker-smile-hero` | `loop (float)` | `sine.inOut` / 3.2s / rot: +0.6° | Micro-oscilação pendular de adesivo |
| Molho Tomate | `.tomato-badge-flow` | `reveal (fade-up)` | `power2.out` / 600ms / 0.15s | Entrada defasada |
| Título Crust | `.title-crust-alchemy` | `reveal (fade-up)` | `power2.out` / 600ms / 0.2s | Entrada tipográfica elegante |
| Foto da Massa | `.dough-card` | `reveal + parallax` | Parallax 0.06 (máx 14px) | Profundidade com rolagem |
| Post-it 48h | `.postit-dough` | `reveal (fade-up)` | `power2.out` / 600ms / 0.3s | Fixação física inclinada |
| Nota Manuscrita | `.hand-note-dough` | `reveal (fade)` | `power2.out` / 600ms / 0.35s | Aparecimento suave de tinta |

### Seção 2: Matéria-Prima Pura (`#materia-prima-pura`)
| Elemento | Seletor | Tipo de Motion | Easing / Duração / Delay | Comportamento Visual |
| :--- | :--- | :---: | :---: | :--- |
| Card Polaroid | `.polaroid-wrapper` | `reveal + parallax` | Parallax 0.07 / 750ms / 0s | Pouso de foto polaroid em mural |
| Etiqueta Fita | `.tape-tag-polaroid` | `reveal (fade)` | `power2.out` / 750ms / 0.1s | Fade de fita adesiva colada |
| Smile Polaroid | `.sticker-smile-polaroid`| `loop (float)` | `sine.inOut` / 3.2s / y: +2.5px | Flutuação milimétrica |
| Washi Tape | `.washi-note-wrap` | `reveal (fade-up)` | `power2.out` / 750ms / 0.1s | Entrada suave |
| Título Matéria | `.title-materia-prima` | `reveal (fade-up)` | `power2.out` / 750ms / 0.2s | Entrada hierárquica editorial |
| Badge No Compromise| `.badge-no-compromise` | `reveal (fade-up)` | `power2.out` / 750ms / 0.3s | Assentamento de carimbo |
| Selo Papel Verde | `.seal-green-scrap-wrap`| `reveal + loop` | `sine.inOut` / 3.2s / y: +2.5px | Respiração sutil de cera sobre papel |

### Seção 3: Forno & Tempo (`#forno-e-tempo`)
| Elemento | Seletor | Tipo de Motion | Easing / Duração / Delay | Comportamento Visual |
| :--- | :--- | :---: | :---: | :--- |
| Foto Forno Lenha | `.oven-card` | `reveal + parallax` | Parallax 0.06 (máx 14px) | Suave deslocamento sob a base rasgada |
| Título Forno | `.title-forno-tempo` | `reveal (fade-up)` | `power2.out` / 750ms / 0.15s | Entrada defasada |
| Doodles SVG | `.oven-doodles-wrap` | `reveal + loop` | `sine.inOut` / 2.8s / scale 1.025 | Pulso calmo de calor artesanal |

### Seção 4: Table & Reservations (`#table-reservations`)
| Elemento | Seletor | Tipo de Motion | Easing / Duração / Delay | Comportamento Visual |
| :--- | :--- | :---: | :---: | :--- |
| Título Table | `.title-reservations` | `reveal (fade-up)` | `power2.out` / 750ms / 0s | Imposição editorial |
| Nota Ambiente | `.reservations-doodle-note`| `reveal (fade-up)`| `power2.out` / 750ms / 0.1s | Fade de nota manuscrita |
| Smile Pizzaiolo | `.sticker-smile-table` | `loop (float)` | `sine.inOut` / 3.2s / y: +2.5px | Flutuação calmo |
| Campainha 3D | `.buzzer-btn-link` | `loop (pulse) + active`| `scale: 1.025` + `:active` 0.92 | Pulso sutil e resposta tátil imediata |
| Botão CTA Pílula | `.btn-cta-pill` | `reveal (fade-up)` | `power2.out` / 750ms / 0.25s | Destaque suave |
| Telefones / Endereço | `.delivery-meta-info` | `reveal (fade-up)` | `power2.out` / 750ms / 0.3s | Finalização |
| Taça e Guardanapo | `.wine-napkin-card` | `reveal + parallax` | Parallax 0.08 (máx 18px) | Profundidade da toalha xadrez |

---

## 3. Auditoria de Loops Simultâneos por Posição de Rolagem

A regra de ouro de performance e ergonomia visual estipula um **máximo de 3 micro-loops simultâneos** visíveis na viewport ao mesmo tempo. Loops fora da viewport são automaticamente pausados via `ScrollTrigger.create({ onLeave: pause, onEnter: play })`.

| Posição de Rolagem (Scroll Y) | Loops Ativos Simultâneos | Elementos em Execução | Status de Carga |
| :---: | :---: | :--- | :---: |
| **0 px (Hero)** | **2 loops** | Manjericão (`sticker-basil-wrap`), Smile Hero | ✅ Perfeito |
| **400 px (Transição Hero-Ingredientes)** | **1 loop** | Selo Verde (`seal-green-scrap-wrap`) | ✅ Leve |
| **800 px (Matéria-Prima Pura)** | **3 loops** | Smile Polaroid, Selo Verde, Doodles Forno | ✅ Dentro do limite |
| **1200 px (Transição Ingredientes-Forno)**| **3 loops** | Smile Polaroid, Selo Verde, Doodles Forno | ✅ Dentro do limite |
| **1600 px (Forno & Tempo)** | **3 loops** | Doodles Forno, Smile Table, Campainha 3D | ✅ Dentro do limite |
| **2000+ px (Table & Reservations)** | **2 loops** | Smile Table, Campainha 3D | ✅ Perfeito |

> **Resultado:** Zero sobrecarga de GPU/CPU. Em nenhum instante há mais de 3 loops em execução simultânea. Dispositivos `low` e modo `reduced` têm 100% dos loops desativados.

---

## 4. Avaliação de Ritmo Editorial

1. **Entradas Suaves e Defasadas:** O stagger de 100ms a 150ms entre o título, anotações manuscritas e as fotos cria a sensação de uma revista de culinária artesanal sendo folheada, sem movimentos mecânicos bruscos.
2. **Harmonia com o Papel Artesanal:** As translações curtas (24px máximo) e rotações milimétricas (0.6° a 1.2°) mantêm a sensação tangível de colagem física, scrapbook e fitas adesivas.
3. **Rolagem Inercial com Lenis:** O scroll suave desacelera com a curva de inércia $1 - 2^{-10t}$, integrando perfeitamente a leitura das anotações manuscritas com a descida da página.
