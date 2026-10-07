# PROGRESSO DO PROJETO — NOVARA PIZZAS E ESFIHAS

**Status Geral:** Construção do layout estático 100% concluída com alta fidelidade e acessibilidade WCAG 2.1 AAA.

---

## 1. Etapas Executadas

- [x] **Etapa 0: Inicialização e Controle de Versão**
  - Git inicializado, `.gitignore` configurado (ignorando `node_modules/` e `screenshots/`).
  - Commit inicial: `design pronto` (hash: `a8c0160`).
- [x] **Etapa 1: Inventário e Conversão de Assets**
  - Mapeamento de todos os slots de imagem do `DESIGN.md` para arquivos reais e plates idênticos à referência gerados pelo usuário (`novara img/`).
  - Conversão em lote para WebP nos tamanhos 800px e 1600px na pasta `site/assets/`.
  - Geração do documento [`assets.md`](file:///c:/Oficial/Novara%203/assets.md). Nenhum slot sem arquivo.
- [x] **Etapa 2: Fundação**
  - Criação do [`tokens.css`](file:///c:/Oficial/Novara%203/site/tokens.css) baseado no `DESIGN.md` com paleta validada e tipografia fluida.
  - Criação do [`reset.css`](file:///c:/Oficial/Novara%203/site/reset.css) com suporte obrigatório a `prefers-reduced-motion: reduce`.
  - Configuração da suíte de testes visuais automatizados com Playwright em [`scripts/screenshot.py`](file:///c:/Oficial/Novara%203/scripts/screenshot.py).
- [x] **Etapa 3: Construção Seção por Seção (Layout Estático)**
  - **Seção 1: Hero & Crust Alchemy (`#hero-crust-alchemy`)**
    - Construída com H1 Novara monumental, social proof real do Google Maps (4.5 ★ / 895 avaliações), stickers e card de massa fermentando.
    - Testada em 1440px e 390px, refinada e validada.
    - Commit: `seção hero-crust-alchemy pronta` (hash: `ababe32`).
  - **Seção 2: Matéria-Prima Pura (`#materia-prima-pura`)**
    - Construída com polaroid de ingredientes, tag washi tape, título monumental e selo com retalho verde.
    - Testada isolada e costura com a Seção 1 em 1440px e 390px.
    - Commit: `seção materia-prima-pura pronta` (hash: `f083103`).
  - **Seção 3: Forno & Tempo (`#forno-e-tempo`)**
    - Construída com foto do forno rústico com base rasgada, título editorial e doodles SVG manuscritos.
    - Testada isolada e costura com a Seção 2 em 1440px e 390px.
    - Commit: `seção forno-e-tempo pronta` (hash: `9973113`).
  - **Seção 4: Table & Reservations (`#table-reservations`)**
    - Construída com título editorial, buzzer button 3D interativo, taça de vinho com guardanapo xadrez, botão em pílula para delivery Wabiz/telefone e rodapé rasgado.
    - Testada isolada e costura com a Seção 3 em 1440px e 390px.
    - Commit: `seção table-reservations pronta` (hash: `454a303`).
- [x] **Etapa 5: Correção da Arquitetura de Layout (Full-Bleed e Responsividade Real)**
  - **Problema corrigido:** Remoção do container fixo `.editorial-canvas` (`max-width: 680px`), do box-shadow lateral e do background pontilhado de `.page-wrapper`.
  - **Nova arquitetura:** Fundo de papel artesanal contínuo e full-bleed de ponta a ponta (100% da tela) em todas as seções.
  - **Containers fluidos:** Utilização de `.editorial-container` com `--container-max-w: clamp(1180px, 90vw, 2200px)`, mantendo leitura confortável para parágrafos e imponência visual proporcional para títulos e imagens.
  - **Fio de queijo contínuo:** Escalando fluidamente via `clamp(150px, 18vw, 360px)`, perfeitamente ancorado na costura central entre as duas colunas do grid sem distorção.
  - **Regra de Ouro documentada:** Incluída formalmente em `CLAUDE.md` e `DESIGN.md` (*"A largura do mockup NUNCA vira um max-width fixo do site inteiro — ela é só a proporção de referência, extrapolada para a largura real de cada tela"*).
  - **Auditoria Playwright Completa:** Capturas geradas e verificadas sem nenhum overflow em **390px**, **768px**, **1024px**, **1440px**, **1920px** e **2560px**.

- [x] **FASE A: Base Global de Motion (Concluída)**
  - Criação do baseline [`motion-baseline.md`](file:///c:/Oficial/Novara%203/motion-baseline.md) com métricas de Lighthouse e requisitos de preservação visual.
  - Hospedagem local dos scripts vendor GSAP 3.14, ScrollTrigger e Lenis Smooth Scroll em `site/js/vendor/`.
  - Construção do núcleo declarativo em [`site/js/motion.js`](file:///c:/Oficial/Novara%203/site/js/motion.js):
    - 3 Modos: `full`, `reduced` (respeitando `prefers-reduced-motion`) e `paused` (suporte a congelamento manual).
    - Qualidade dinâmica: `high` vs `low` baseado em hardware, memória, conexão e tamanho de tela.
    - Suporte a atributos declarativos: `[data-reveal]`, `[data-parallax]`, `[data-loop]`.
    - Ciclo de vida: pausa de animações e loops fora da tela via ScrollTrigger e em aba oculta via `visibilitychange`.
    - Proteção estrutural: `.cheese-pull-spine` e seus ancestrais sem transformações ou filtros que criem novo contexto de empilhamento.
  - Suíte de regressão automatizada [`scripts/test_motion_base.py`](file:///c:/Oficial/Novara%203/scripts/test_motion_base.py) executada com sucesso (0 erros, carregamento após load/interação, sem dependência de JS na dobra inicial).
  - Lighthouse Mobile pós-Fase A: Performance 66/100 (variação de apenas 2 pontos em relação ao baseline de 68), Acessibilidade 100/100, Melhores Práticas 88/100, SEO 91/100.
  - Tag registrada: `motion-base`.

---

## 2. Próximos Passos (Fases B e C de Motion)
1. **FASE B:** Implementar animações declarativas seção por seção (Hero, Matéria-Prima, Forno & Tempo, Reservas).
2. **FASE C:** Botão de pausa acessível, inventário de motion, avaliação de ritmo e tag `motion-pronto`.

