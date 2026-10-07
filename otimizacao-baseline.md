# BASELINE DE OTIMIZAÇÃO — NOVARA PIZZAS E ESFIHAS

**Data:** 07/10/2026  
**Status Inicial:** Fases de Motion concluídas (Commit: `ca4f5f2` - Tag: `motion-pronto`)

---

## 1. Pontuações do Lighthouse (Mobile Emulado)

| Categoria | Pontuação Inicial | Meta de Otimização |
| :--- | :---: | :---: |
| **Performance** | **65 / 100** | **≥ 90 - 92** |
| **Accessibility** | **100 / 100** | Manter 100 / 100 |
| **Best Practices** | **88 / 100** | Manter ≥ 88 / 100 |
| **SEO** | **91 / 100** | Manter ≥ 91 / 100 |

### Métricas Core Web Vitals Iniciais (Mobile)
- **First Contentful Paint (FCP):** ~3.4 s
- **Largest Contentful Paint (LCP):** ~6.8 s
- **Total Blocking Time (TBT):** 0 ms
- **Cumulative Layout Shift (CLS):** 0.000
- **Speed Index:** ~5.4 s

---

## 2. Diagnóstico dos Gargalos Iniciais

1. **Fontes Externas (Google Fonts CDN):**
   - Requisições bloqueadoras para `fonts.googleapis.com` e download tardio de WOFF2 do `fonts.gstatic.com`.
   - Solução: Baixar e auto-hospedar apenas os pesos usados em WOFF2 localmente (`site/fonts/`), com `font-display: swap` e `preload` das fontes críticas da dobra.
2. **CSS Não Crítico e Arquivos Múltiplos:**
   - 4 arquivos separados (`tokens.css`, `reset.css`, `lenis.css`, `style.css`), somando requisições e bytes não minificados.
   - Solução: CSS crítico inline no `<head>`, CSS complementar minificado e carregado de forma assíncrona/não bloqueante.
3. **Entrega de Imagens e Degraus Menores:**
   - Ícones e miniaturas (selo de cera 60px e botão campainha 3D 80px) carregando assets de 800px.
   - Faltam atributos `fetchpriority="high"` no candidato a LCP e `sizes` ajustados por breakpoint.
   - Solução: Gerar versões 120px e 240px para miniaturas e selos; configurar `sizes` responsivos reais e `loading="lazy"`.
4. **JavaScript Próprio:**
   - `motion.js` sem minificação.
   - Solução: Minificar `motion.min.js`, mantendo zero impacto no FCP.
5. **SEO & Melhores Práticas:**
   - Falta `<meta name="description">` e ícone favicon local para evitar requisições 404 no browser.
