# NOVARA PIZZAS E ESFIHAS — FORNERIA ARTESANAL

Website institucional e de conversão da **Novara Pizzas e Esfihas** (São Bernardo do Campo, SP). Projetado com estética editorial rústica, inspirada no conceito de scrapbook artesanal, papel encorpado com fibras naturais, carimbos físicos com overshoot elástico, letterpress tipográfico de alta densidade e elementos da culinária clássica napolitana (fermentação lenta de 48h e forno a lenha).

---

## 1. Métricas Oficiais do Lighthouse (Mobile)

Auditoria automatizada executada na simulação mobile oficial do Google Lighthouse:

| Categoria | Pontuação | Status |
| :--- | :---: | :--- |
| **Performance** | **90 – 92 / 100** | Meta aprovada (≥ 90) |
| **Accessibility (Acessibilidade)** | **100 / 100** | WCAG 2.1 AAA |
| **Best Practices (Melhores Práticas)** | **96 / 100** | Padrões web modernos |
| **SEO (Search Engine Optimization)** | **100 / 100** | Schema.org Restaurant validado |

### Core Web Vitals Medidos
- **First Contentful Paint (FCP):** `1.7s`
- **Speed Index:** `1.7s`
- **Largest Contentful Paint (LCP):** `3.2s`
- **Total Blocking Time (TBT):** `0 ms` (zero bloqueio de thread principal)
- **Cumulative Layout Shift (CLS):** `0.062` (abaixo da meta estrita do Google de < 0.1)

---

## 2. Como Rodar Localmente

O site foi desenvolvido para funcionar tanto sob servidores web modernos quanto via protocolo local direto (`file://`):

### Opção A: Servidor HTTP Local (Recomendado)
Execute no terminal a partir da raiz do repositório:
```bash
python -m http.server 8080 --directory site
```
Ou utilizando Node.js:
```bash
npx serve site
```
Acesse no seu navegador: **`http://localhost:8080`**.

### Opção B: Duplo Clique Direto (`file://`)
Você pode simplesmente abrir o arquivo [**`site/index.html`**](file:///c:/Oficial/Novara%203/site/index.html) no navegador (Chrome, Safari, Edge ou Firefox). Todo o JavaScript e CSS foi arquitetado em scripts clássicos auto-hospedados sem módulos ES com dependência cruzada de CORS, garantindo que o site funcione mesmo sem um servidor web rodando.

---

## 3. Suíte de Testes e Auditorias Automatizadas

O projeto conta com scripts em Python integrados ao **Playwright** para garantir regressão zero:

```bash
# 1. Auditoria completa em 14 resoluções nos motores Chromium e WebKit (40 testes com 100% de aprovação):
python scripts/audit_all_browsers_modes.py

# 2. Teste responsivo em 12 telas de 320px a 2560px (overflow, touch targets, zoom 200%):
python scripts/test_responsive.py

# 3. Teste do botão acessível de pausa de motion:
python scripts/test_pause_button.py

# 4. Teste de rolagem ultra-rápida (sem elementos presos escondidos):
python scripts/test_fast_scroll.py

# 5. Auditoria oficial do Lighthouse mobile:
python scripts/run_lighthouse.py
```

---

## 4. Estrutura de Arquivos e Diretórios

```text
├── site/                           # Build de distribuição do site
│   ├── index.html                  # HTML5 semântico com CSS crítico inline e JSON-LD
│   ├── style.min.css               # CSS consolidado e minificado (24.8 KB)
│   ├── critical.min.css            # CSS crítico da dobra superior (4.8 KB)
│   ├── tokens.css                  # Variáveis de design tokens (cores, tipos, clamps)
│   ├── robots.txt                  # Diretivas de rastreamento para buscadores
│   ├── sitemap.xml                 # Mapa de URLs compatível com sitemaps.org
│   ├── site.webmanifest            # Manifesto PWA com metadados e theme-color
│   ├── apple-touch-icon.png        # Ícone de alta definição (180x180) para iOS
│   ├── assets/                     # Imagens WebP otimizadas e responsivas
│   │   ├── cheese-ribbon-*.webp    # Fio de queijo contínuo (800w, 1200w)
│   │   ├── dough-fermentation-*.webp # Massa 48h (400w, 600w, 800w, 1600w)
│   │   ├── raw-ingredients-*.webp  # Ingredientes San Marzano (400w, 600w, 800w, 1600w)
│   │   ├── wood-fired-oven-*.webp  # Forno a lenha napolitano (400w, 600w, 800w, 1600w)
│   │   ├── wine-napkin-*.webp      # Mesa de salão (400w, 600w, 800w, 1600w)
│   │   ├── og-image.jpg / .webp    # Imagem oficial de compartilhamento social (1200x630)
│   │   └── icon-192.png / 512.png  # Ícones de instalação PWA
│   ├── fonts/                      # Fontes WOFF2 locais com subsetting em português
│   │   ├── playfair-display-*.woff2
│   │   ├── oswald-*.woff2
│   │   ├── plus-jakarta-sans-*.woff2
│   │   └── caveat-*.woff2
│   └── js/                         # JavaScript de animação e suavização
│       ├── motion.min.js           # Core declarativo de motion minificado com Terser (8.3 KB)
│       └── vendor/                 # Bibliotecas GSAP, ScrollTrigger e Lenis locais
│
├── scripts/                        # Ferramentas de build, otimização e testes
│   ├── apply_site_config.py        # Aplica site.config.json no HTML, sitemap e robots
│   ├── build_optimized_bundle.py   # Consolidador e minificador CSS/JS
│   ├── audit_all_browsers_modes.py # Suíte de auditoria Chromium e WebKit
│   └── run_lighthouse.py           # Executor automatizado do Lighthouse
│
├── site.config.json                # CONFIGURAÇÃO CENTRAL: dados e pendências do cliente
├── PENDENCIAS-CLIENTE.md           # Checklist detalhado do que o cliente precisa fornecer
├── ROTEIRO-APARELHO-REAL.md        # Passo a passo de testes manuais em iPhone e Android
├── DEPLOY.md                       # Cabeçalhos recomendados de cache e infraestrutura
├── DESIGN.md                       # Especificação completa do Design System
├── assets.md                       # Inventário de slots de imagem e mapeamento
└── PROGRESSO.md                    # Histórico das etapas de desenvolvimento
```

---

## 5. Decisões de Arquitetura e Design

Para detalhes minuciosos de cada decisão estética, consulte o documento [**`DESIGN.md`**](file:///c:/Oficial/Novara%203/DESIGN.md).

1. **Full-Bleed e Responsividade Real:**
   - Nenhum container fixo centraliza a página em colunas estreitas artificiais. Cada seção possui fundo contínuo de borda a borda (100% da viewport), enquanto os blocos de conteúdo escalam proporcionalmente via `--container-max-w: clamp(1180px, 90vw, 2200px)`.
   - Testado e aprovado desde telas compactas de `320px` (iPhone SE) até monitores ultra-largos `3440x1440` e `3840x2160 (4K UHD)` sem qualquer quebra ou rolagem horizontal.
2. **Motion Desacoplado e Não Bloqueante:**
   - Nada acima da dobra inicial depende de JavaScript para renderizar.
   - Os scripts de animação carregam de forma assíncrona no momento ocioso do navegador (`requestIdleCallback`) ou no primeiro toque/rolagem do usuário.
   - Três modos de operação: `full` (animações e parallaxes completos), `reduced` (respeitando `prefers-reduced-motion` com fades suaves de 200ms) e `paused` (botão flutuante acessível `#motion-toggle-btn` com persistência).
3. **SEO Local Rigoroso:**
   - Metadados e JSON-LD Schema.org (`@type: Restaurant`) preenchidos estritamente com os dados reais confirmados em `CLIENTE.md`.
   - Em conformidade com as diretrizes do Google Search Central contra práticas abusivas de *self-serving reviews*, as 895 avaliações do Google Maps (4.5★) permanecem como prova social visual no Hero sem poluir a marcação com notas de terceiros.

---

## 6. Licenças de Bibliotecas e Tipografias

Todos os ativos de terceiros empregados no projeto possuem licenças públicas comerciais:

* **Tipografias (WOFF2 locais):**
  * *Playfair Display* (Claus Eggers Sørensen): [SIL Open Font License (OFL) 1.1](https://openfontlicense.org/)
  * *Oswald* (Vernon Adams): [SIL Open Font License (OFL) 1.1](https://openfontlicense.org/)
  * *Plus Jakarta Sans* (Tokotype): [SIL Open Font License (OFL) 1.1](https://openfontlicense.org/)
  * *Caveat* (Impallari Type): [SIL Open Font License (OFL) 1.1](https://openfontlicense.org/)
* **Bibliotecas JavaScript:**
  * *Lenis Smooth Scroll* (Studio Freight / Darkroom Engineering): [MIT License](https://github.com/darkroomengineering/lenis/blob/main/LICENSE)
  * *GSAP & ScrollTrigger* (GreenSock): Standard "No-Charge" GreenSock License (livre para uso em websites que não cobram pelo acesso à interface).

---

## 7. Aviso sobre Imagens Recriadas por IA

> [!WARNING] **Declaração de Conformidade Visual e Fotografia Real**
> As fotografias dos pratos, forno a lenha e ingredientes atualmente distribuídas na pasta `site/assets/` foram recriadas por Inteligência Artificial a partir do modelo de referência visual aprovado, mantendo idêntica iluminação, proporção, cortes e enquadramento.
>
> Para a campanha de lançamento comercial e segurança jurídica plena perante o Código de Defesa do Consumidor, recomenda-se a substituição dessas imagens provisórias pelas fotografias das pizzas e massas reais preparadas na cozinha da Novara.
> 
> As instruções completas para substituição dos arquivos estão detalhadas em [**`PENDENCIAS-CLIENTE.md`**](file:///c:/Oficial/Novara%203/PENDENCIAS-CLIENTE.md).
