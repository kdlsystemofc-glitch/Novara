import os

# CSS crítico essencial para first paint e Hero above-the-fold
CRITICAL_CSS = """
@font-face {
  font-family: 'Oswald';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url('fonts/oswald-700-normal-54494.woff2') format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
@font-face {
  font-family: 'Playfair Display';
  font-style: normal;
  font-weight: 900;
  font-display: swap;
  src: url('fonts/playfair-display-900-normal-28189.woff2') format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
@font-face {
  font-family: 'Plus Jakarta Sans';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url('fonts/plus-jakarta-sans-700-normal-33572.woff2') format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

:root {
  --color-ink: #141414;
  --color-paper: #F5EFEB;
  --color-paper-alt: #EFE8E1;
  --color-accent-tomato: #D32F2F;
  --color-accent-gold: #DEA01B;
  --color-accent-olive: #2E7D32;
  --color-accent-wax: #A62226;
  --font-display: 'Playfair Display', Georgia, serif;
  --font-secondary: 'Oswald', Arial Narrow, sans-serif;
  --font-primary: 'Plus Jakarta Sans', -apple-system, sans-serif;
  --font-accent: 'Caveat', cursive;
  --space-2xs: clamp(0.5rem, 1vw, 0.75rem);
  --space-xs: clamp(0.75rem, 1.5vw, 1.125rem);
  --space-sm: clamp(1rem, 2vw, 1.5rem);
  --space-md: clamp(1.5rem, 3vw, 2.25rem);
  --space-lg: clamp(2rem, 4.5vw, 3.5rem);
  --space-xl: clamp(3rem, 6vw, 4.75rem);
  color-scheme: light;
}

*, *::before, *::after {
  box-sizing: border-box;
}

html {
  background-color: var(--color-paper);
  color: var(--color-ink);
  font-family: var(--font-primary);
  font-size: 16px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

body {
  margin: 0;
  padding: 0;
  background-color: var(--color-paper);
  min-height: 100vh;
  min-height: 100svh;
  overflow-x: hidden;
}

.site-main {
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background-color: var(--color-paper);
  background-image: radial-gradient(var(--color-ink) 0.6px, transparent 0.6px);
  background-size: 24px 24px;
}

.cheese-pull-spine {
  position: absolute;
  top: clamp(60px, 5.8vw, 100px);
  left: 0;
  right: 0;
  margin-inline: auto;
  width: clamp(300px, 42vw, 660px);
  z-index: 10;
  pointer-events: none;
  filter: drop-shadow(0 10px 24px rgba(0, 0, 0, 0.18));
}

.cheese-pull-spine img {
  width: 100%;
  height: auto;
  display: block;
}

.editorial-section {
  position: relative;
  width: 100%;
  padding-left: clamp(1rem, 4vw, 3.5rem);
  padding-right: clamp(1rem, 4vw, 3.5rem);
}

.sec-hero {
  padding-top: var(--space-2xs);
  padding-bottom: var(--space-lg);
  min-height: auto;
}

.hero-header-wrap {
  position: relative;
  width: 100%;
  max-width: 1600px;
  margin-inline: auto;
  z-index: 5;
}

.hero-top-bar {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: var(--space-xs);
  margin-bottom: var(--space-2xs);
}

.badge-social-proof {
  display: inline-flex;
  flex-direction: column;
  background: var(--color-ink);
  color: #FFF8F0;
  padding: 4px 10px;
  border-radius: 3px;
  font-family: var(--font-secondary);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  line-height: 1.15;
}

.proof-star { color: var(--color-accent-gold); font-size: 0.85rem; }
.proof-count { color: #BBB; font-size: 0.6rem; }

.hero-wax-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
}

.wax-seal-badge {
  width: 60px;
  height: 60px;
  object-fit: contain;
  filter: drop-shadow(0 4px 10px rgba(166, 34, 38, 0.35));
}

.stamp-fermentation {
  font-family: var(--font-secondary);
  font-size: 0.55rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: var(--color-accent-wax);
  border: 1px dashed var(--color-accent-wax);
  padding: 2px 4px;
  margin-top: -6px;
  background: rgba(245, 239, 235, 0.85);
}

.brand-hero-title-wrap {
  text-align: center;
  position: relative;
  z-index: 8;
  width: 100%;
}

.brand-hero-title {
  font-family: var(--font-display);
  font-size: clamp(4.4rem, 15.6vw, 16.5rem);
  font-weight: 900;
  letter-spacing: clamp(0.02em, 0.25vw, 0.06em);
  line-height: 0.84;
  color: var(--color-ink);
  text-transform: uppercase;
  margin: 0;
  padding: 0;
}

.hero-letter {
  display: inline-block;
  will-change: transform, opacity;
}

.editorial-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: clamp(1.5rem, 5vw, 5rem);
  width: 100%;
  max-width: clamp(1180px, 90vw, 2200px);
  margin-inline: auto;
  align-items: start;
}

.hero-content-grid {
  margin-top: clamp(1rem, 2vw, 2.5rem);
  position: relative;
  z-index: 6;
}

.title-crust-alchemy {
  font-family: var(--font-display);
  font-size: clamp(2.2rem, 5.2vw, 4.6rem);
  font-weight: 900;
  line-height: 0.92;
  text-transform: uppercase;
  margin: 0;
}

.sub-crust {
  display: block;
  font-size: 0.52em;
  letter-spacing: 0.08em;
  color: var(--color-ink);
  opacity: 0.9;
}

.dough-card {
  position: relative;
  width: 100%;
  border-radius: 12px;
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.15);
  overflow: visible;
}

.img-dough {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 12px;
}

@media (max-width: 720px) {
  .editorial-grid {
    grid-template-columns: 1fr;
    gap: var(--space-md);
  }
  .cheese-pull-spine {
    width: clamp(200px, 60vw, 290px);
    top: 50px;
    right: clamp(-15px, 2vw, 15px);
    left: auto;
    z-index: 2;
    opacity: 0.85;
  }
}
"""

def extract():
    import re
    # Minify critical CSS
    css_text = re.sub(r"/\*[\s\S]*?\*/", "", CRITICAL_CSS)
    css_text = re.sub(r"\s+", " ", css_text)
    css_text = re.sub(r"\s*([\{\};:,>])\s*", r"\1", css_text)
    css_text = re.sub(r";\}", "}", css_text).strip()
    
    with open("site/critical.min.css", "w", encoding="utf-8") as f:
        f.write(css_text)
    print(f"Critical CSS gerado: {len(css_text) / 1024:.1f} KB (site/critical.min.css)")

if __name__ == "__main__":
    extract()
