# MOTION BASELINE — AUDITORIA INICIAL (ESTÁTICO)

**Data:** 07/10/2026  
**Status:** Layout Estático 100% responsivo aprovado (Commit: `responsivo pronto` - hash `83a5e36`)

---

## 1. Pontuações do Lighthouse (Mobile)

| Categoria | Pontuação | Meta de Regressão |
| :--- | :---: | :---: |
| **Performance** | **68 / 100** | Não cair mais de 3 pontos durante as fases de motion (mínimo 65) |
| **Accessibility** | **100 / 100** | Manter 100 / 100 |
| **Best Practices** | **88 / 100** | Manter ≥ 88 / 100 |
| **SEO** | **91 / 100** | Manter ≥ 91 / 100 |

### Métricas Core Web Vitals (Mobile Emulado)
- **First Contentful Paint (FCP):** 3.2 s
- **Largest Contentful Paint (LCP):** 6.4 s
- **Total Blocking Time (TBT):** 0 ms (Zero impacto de scripts no estático)
- **Cumulative Layout Shift (CLS):** 0.000 (Perfeito, sem deslocamentos bruscos)
- **Speed Index:** 5.2 s

---

## 2. Auditoria de Elementos e Restrições de Motion

1. **Elemento Contínuo de Assinatura (`.cheese-pull-spine`):**
   - **Regra:** NÃO se move em nenhuma animação.
   - **Contexto de Empilhamento:** Nenhum elemento ancestral ganha `transform`, `filter` ou `opacity < 1`. Mantido com fluxo natural ou `position: absolute/sticky` isolado.
2. **Above-the-Fold (Dobra Superior):**
   - Todo o conteúdo de `.sec-hero` e `.hero-top-bar` permanece 100% visível sem dependência de JavaScript (`opacity: 1`).
   - Carregamento assíncrono e diferido dos scripts de motion após evento `load` ou primeira interação do usuário.
3. **Hardware & Qualidade Dinâmica:**
   - Detecção de dispositivos com economia de dados (`saveData`), CPU reduzida (`hardwareConcurrency < 4`) ou memória baixa (`deviceMemory < 4`).
   - Adaptação automática entre modos `full` e `low` (reduzindo loops contínuos e desativando parallax complexo em mobile/hardware modesto).
4. **Respeito à Preferência do Usuário:**
   - Suporte nativo a `prefers-reduced-motion: reduce`: desativação completa de parallax e loops; transição restrita a fade suave de 200ms.
   - Botão de Pausa global: controle sob demanda para congelar e retomar qualquer animação.
