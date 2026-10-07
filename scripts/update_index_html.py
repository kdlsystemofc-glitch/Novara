import os

INDEX_PATH = "site/index.html"
CRITICAL_PATH = "site/critical.min.css"

with open(CRITICAL_PATH, "r", encoding="utf-8") as f:
    critical_css = f.read().strip()

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update <head>
old_head_block = """  <!-- Google Fonts: Playfair Display, Oswald, Plus Jakarta Sans, Caveat -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&family=Oswald:wght@600;700&family=Playfair+Display:ital,wght@0,600..900;1,600..900&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="tokens.css">
  <link rel="stylesheet" href="reset.css">
  <link rel="stylesheet" href="lenis.css">
  <link rel="stylesheet" href="style.css">"""

new_head_block = f"""  <meta name="description" content="Novara Pizzas e Esfihas — Forneria artesanal em São Bernardo do Campo com massas de fermentação lenta 48h, forno a lenha e ingredientes nobres selecionados.">

  <!-- Favicons -->
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="alternate icon" href="favicon.ico">

  <!-- Preload de Fontes Críticas da Dobra (WOFF2 local) -->
  <link rel="preload" href="fonts/playfair-display-900-normal-28189.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/oswald-700-normal-54494.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/plus-jakarta-sans-700-normal-33572.woff2" as="font" type="font/woff2" crossorigin>

  <!-- Preload da Imagem LCP Candidata Acima da Dobra -->
  <link rel="preload" as="image" href="assets/dough-fermentation-400.webp" imagesrcset="assets/dough-fermentation-400.webp 400w, assets/dough-fermentation-800.webp 800w, assets/dough-fermentation-1600.webp 1600w" imagesizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw" fetchpriority="high">

  <!-- CSS Crítico Inline (Zero Render-Blocking no FCP) -->
  <style id="critical-css">{critical_css}</style>

  <!-- CSS Completo Assíncrono Não-Bloqueante -->
  <link rel="preload" as="style" href="style.min.css" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="style.min.css"></noscript>"""

if old_head_block in html:
    html = html.replace(old_head_block, new_head_block)
    print("Head block updated successfully.")
else:
    print("Warning: old_head_block not found exactly!")

# 2. Update Cheese Ribbon Spine
old_spine = """      <picture>
        <source srcset="assets/cheese-ribbon-1600.webp" media="(min-width: 600px)">
        <img src="assets/cheese-ribbon-800.webp" alt="Fio de queijo mozzarella puxado da pizza" width="267" height="800">
      </picture>"""

new_spine = """      <picture>
        <source srcset="assets/cheese-ribbon-400.webp 400w, assets/cheese-ribbon-800.webp 800w, assets/cheese-ribbon-1600.webp 1600w" sizes="(max-width: 600px) 290px, 42vw">
        <img src="assets/cheese-ribbon-400.webp" alt="Fio de queijo mozzarella puxado da pizza" width="267" height="800" decoding="async">
      </picture>"""

if old_spine in html:
    html = html.replace(old_spine, new_spine)
    print("Cheese ribbon spine updated.")
else:
    print("Warning: old_spine not found!")

# 3. Update Hero wax seal
old_hero_seal = """            <img src="assets/wax-seal-800.webp" alt="Selo de cera de qualidade Novara" class="wax-seal-badge hero-seal" width="60" height="60">"""
new_hero_seal = """            <picture>
              <source srcset="assets/wax-seal-160.webp 160w, assets/wax-seal-320.webp 320w" sizes="(max-width: 600px) 48px, 60px">
              <img src="assets/wax-seal-160.webp" alt="Selo de cera de qualidade Novara" class="wax-seal-badge hero-seal" width="60" height="60" decoding="async">
            </picture>"""

if old_hero_seal in html:
    html = html.replace(old_hero_seal, new_hero_seal)
    print("Hero wax seal updated.")
else:
    print("Warning: old_hero_seal not found!")

# 4. Update Dough LCP image
old_dough = """            <picture>
              <source srcset="assets/dough-fermentation-1600.webp" media="(min-width: 600px)">
              <img src="assets/dough-fermentation-800.webp" alt="Massa de pizza artesanal fermentando sobre pedra com farinha" class="img-dough" width="800" height="533">
            </picture>"""

new_dough = """            <picture>
              <source srcset="assets/dough-fermentation-400.webp 400w, assets/dough-fermentation-800.webp 800w, assets/dough-fermentation-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
              <img src="assets/dough-fermentation-800.webp" alt="Massa de pizza artesanal fermentando sobre pedra com farinha" class="img-dough" width="800" height="533" fetchpriority="high" decoding="async">
            </picture>"""

if old_dough in html:
    html = html.replace(old_dough, new_dough)
    print("Hero dough image updated.")
else:
    print("Warning: old_dough not found!")

# 5. Update Polaroid ingredients
old_polaroid = """              <picture>
                <source srcset="assets/raw-ingredients-1600.webp" media="(min-width: 600px)">
                <img src="assets/raw-ingredients-800.webp" alt="Ingredientes frescos selecionados: tomates italianos, burrata e especiarias" class="img-polaroid" width="800" height="800">
              </picture>"""

new_polaroid = """              <picture>
                <source srcset="assets/raw-ingredients-400.webp 400w, assets/raw-ingredients-800.webp 800w, assets/raw-ingredients-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
                <img src="assets/raw-ingredients-800.webp" alt="Ingredientes frescos selecionados: tomates italianos, burrata e especiarias" class="img-polaroid" width="800" height="800" loading="lazy" decoding="async">
              </picture>"""

if old_polaroid in html:
    html = html.replace(old_polaroid, new_polaroid)
    print("Polaroid ingredients updated.")
else:
    print("Warning: old_polaroid not found!")

# 6. Update Section 2 scrap wax seal
old_scrap_seal = """              <img src="assets/wax-seal-800.webp" alt="Selo de autenticidade Novara" class="wax-seal-badge scrap-seal" width="60" height="60">"""
new_scrap_seal = """              <picture>
                <source srcset="assets/wax-seal-160.webp 160w, assets/wax-seal-320.webp 320w" sizes="(max-width: 600px) 48px, 60px">
                <img src="assets/wax-seal-160.webp" alt="Selo de autenticidade Novara" class="wax-seal-badge scrap-seal" width="60" height="60" loading="lazy" decoding="async">
              </picture>"""

if old_scrap_seal in html:
    html = html.replace(old_scrap_seal, new_scrap_seal)
    print("Section 2 scrap seal updated.")
else:
    print("Warning: old_scrap_seal not found!")

# 7. Update Wood-fired oven
old_oven = """              <picture>
                <source srcset="assets/wood-fired-oven-1600.webp" media="(min-width: 600px)">
                <img src="assets/wood-fired-oven-800.webp" alt="Forno a lenha artesanal com chamas e lenha em brasa" class="img-oven" width="800" height="533">
              </picture>"""

new_oven = """              <picture>
                <source srcset="assets/wood-fired-oven-400.webp 400w, assets/wood-fired-oven-800.webp 800w, assets/wood-fired-oven-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
                <img src="assets/wood-fired-oven-800.webp" alt="Forno a lenha artesanal com chamas e lenha em brasa" class="img-oven" width="800" height="533" loading="lazy" decoding="async">
              </picture>"""

if old_oven in html:
    html = html.replace(old_oven, new_oven)
    print("Wood-fired oven image updated.")
else:
    print("Warning: old_oven not found!")

# 8. Update Buzzer button 3d
old_buzzer = """                <picture>
                  <source srcset="assets/push-button-3d-1600.webp" media="(min-width: 600px)">
                  <img src="assets/push-button-3d-800.webp" alt="Botão campainha 3D de pedidos Novara" class="img-buzzer-3d" width="80" height="80">
                </picture>"""

new_buzzer = """                <picture>
                  <source srcset="assets/push-button-3d-160.webp 160w, assets/push-button-3d-320.webp 320w" sizes="80px">
                  <img src="assets/push-button-3d-160.webp" alt="Botão campainha 3D de pedidos Novara" class="img-buzzer-3d" width="80" height="80" loading="lazy" decoding="async">
                </picture>"""

if old_buzzer in html:
    html = html.replace(old_buzzer, new_buzzer)
    print("Buzzer 3D image updated.")
else:
    print("Warning: old_buzzer not found!")

# 9. Update Wine Napkin
old_wine = """            <picture>
              <source srcset="assets/wine-napkin-1600.webp" media="(min-width: 600px)">
              <img src="assets/wine-napkin-800.webp" alt="Taça de vinho branco com toalha de mesa xadrez verde artesanal" class="img-wine-napkin" width="800" height="667">
            </picture>"""

new_wine = """            <picture>
              <source srcset="assets/wine-napkin-400.webp 400w, assets/wine-napkin-800.webp 800w, assets/wine-napkin-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
              <img src="assets/wine-napkin-800.webp" alt="Taça de vinho branco com toalha de mesa xadrez verde artesanal" class="img-wine-napkin" width="800" height="667" loading="lazy" decoding="async">
            </picture>"""

if old_wine in html:
    html = html.replace(old_wine, new_wine)
    print("Wine napkin image updated.")
else:
    print("Warning: old_wine not found!")

# 10. Update motion script to motion.min.js
old_script = "'js/motion.js'"
new_script = "'js/motion.min.js'"
if old_script in html:
    html = html.replace(old_script, new_script)
    print("Motion script updated to motion.min.js.")
else:
    print("Warning: old_script not found!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("site/index.html updated successfully!")
