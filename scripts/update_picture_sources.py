import os
from PIL import Image

INDEX_PATH = "site/index.html"
ASSETS_DIR = "site/assets"

# First ensure cheese-ribbon-1200.webp is saved with quality 68
plate_cheese = "design/plates/cheese-ribbon.png"
if os.path.exists(plate_cheese):
    im = Image.open(plate_cheese)
    im_1200 = im.resize((400, 1200), Image.Resampling.LANCZOS)
    im_1200.save(os.path.join(ASSETS_DIR, "cheese-ribbon-1200.webp"), "WEBP", quality=68, method=6)
    print("cheese-ribbon-1200.webp re-saved at Q68:", os.path.getsize(os.path.join(ASSETS_DIR, "cheese-ribbon-1200.webp")) / 1024, "KB")

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update <head> preloads: single critical font + direct cheese-ribbon-1200.webp preload
old_preloads = """  <!-- Preload de Fontes Críticas da Dobra (WOFF2 local) -->
  <link rel="preload" href="fonts/playfair-display-900-normal-28189.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/oswald-700-normal-54494.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/plus-jakarta-sans-700-normal-33572.woff2" as="font" type="font/woff2" crossorigin>

  <!-- Preload da Imagem LCP Candidata Acima da Dobra (Fio de Queijo Spine) -->
  <link rel="preload" as="image" href="assets/cheese-ribbon-800.webp" imagesrcset="assets/cheese-ribbon-400.webp 133w, assets/cheese-ribbon-800.webp 267w, assets/cheese-ribbon-1200.webp 400w, assets/cheese-ribbon-1600.webp 533w" imagesizes="(max-width: 600px) 290px, 42vw" fetchpriority="high">"""

new_preloads = """  <!-- Preload da Fonte Display Monumental do Título Hero -->
  <link rel="preload" href="fonts/playfair-display-900-normal-28189.woff2" as="font" type="font/woff2" crossorigin>

  <!-- Preload da Imagem LCP Candidata Acima da Dobra (Fio de Queijo Spine) -->
  <link rel="preload" as="image" href="assets/cheese-ribbon-1200.webp" fetchpriority="high">"""

if old_preloads in html:
    html = html.replace(old_preloads, new_preloads)
    print("Head preloads updated.")
else:
    print("Warning: old_preloads not matched exactly!")

# 2. Update Cheese Ribbon Spine
old_spine = """      <picture>
        <source srcset="assets/cheese-ribbon-400.webp 133w, assets/cheese-ribbon-800.webp 267w, assets/cheese-ribbon-1200.webp 400w, assets/cheese-ribbon-1600.webp 533w" sizes="(max-width: 600px) 290px, 42vw">
        <img src="assets/cheese-ribbon-800.webp" alt="Fio de queijo mozzarella puxado da pizza" width="267" height="800" fetchpriority="high" decoding="async">
      </picture>"""

new_spine = """      <picture>
        <source media="(max-width: 600px)" srcset="assets/cheese-ribbon-800.webp 1x, assets/cheese-ribbon-1200.webp 2x">
        <source media="(min-width: 601px)" srcset="assets/cheese-ribbon-800.webp 800w, assets/cheese-ribbon-1200.webp 1200w, assets/cheese-ribbon-1600.webp 1600w" sizes="42vw">
        <img src="assets/cheese-ribbon-1200.webp" alt="Fio de queijo mozzarella puxado da pizza" width="267" height="800" fetchpriority="high" decoding="async">
      </picture>"""

if old_spine in html:
    html = html.replace(old_spine, new_spine)
    print("Spine picture updated.")
else:
    print("Warning: old_spine not matched!")

# 3. Update Dough picture
old_dough = """            <picture>
              <source srcset="assets/dough-fermentation-400.webp 400w, assets/dough-fermentation-600.webp 600w, assets/dough-fermentation-800.webp 800w, assets/dough-fermentation-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
              <img src="assets/dough-fermentation-600.webp" alt="Massa de pizza artesanal fermentando sobre pedra com farinha" class="img-dough" width="800" height="533" loading="lazy" decoding="async">
            </picture>"""

new_dough = """            <picture>
              <source media="(max-width: 600px)" srcset="assets/dough-fermentation-400.webp 1x, assets/dough-fermentation-600.webp 2x">
              <source media="(min-width: 601px)" srcset="assets/dough-fermentation-600.webp 600w, assets/dough-fermentation-800.webp 800w, assets/dough-fermentation-1600.webp 1600w" sizes="42vw">
              <img src="assets/dough-fermentation-600.webp" alt="Massa de pizza artesanal fermentando sobre pedra com farinha" class="img-dough" width="800" height="533" loading="lazy" decoding="async">
            </picture>"""

if old_dough in html:
    html = html.replace(old_dough, new_dough)
    print("Dough picture updated.")
else:
    print("Warning: old_dough not matched!")

# 4. Update Raw ingredients picture
old_raw = """              <picture>
                <source srcset="assets/raw-ingredients-400.webp 400w, assets/raw-ingredients-600.webp 600w, assets/raw-ingredients-800.webp 800w, assets/raw-ingredients-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
                <img src="assets/raw-ingredients-600.webp" alt="Ingredientes frescos selecionados: tomates italianos, burrata e especiarias" class="img-polaroid" width="800" height="800" loading="lazy" decoding="async">
              </picture>"""

new_raw = """              <picture>
                <source media="(max-width: 600px)" srcset="assets/raw-ingredients-400.webp 1x, assets/raw-ingredients-600.webp 2x">
                <source media="(min-width: 601px)" srcset="assets/raw-ingredients-600.webp 600w, assets/raw-ingredients-800.webp 800w, assets/raw-ingredients-1600.webp 1600w" sizes="42vw">
                <img src="assets/raw-ingredients-600.webp" alt="Ingredientes frescos selecionados: tomates italianos, burrata e especiarias" class="img-polaroid" width="800" height="800" loading="lazy" decoding="async">
              </picture>"""

if old_raw in html:
    html = html.replace(old_raw, new_raw)
    print("Raw ingredients picture updated.")
else:
    print("Warning: old_raw not matched!")

# 5. Update Wood-fired oven picture
old_oven = """              <picture>
                <source srcset="assets/wood-fired-oven-400.webp 400w, assets/wood-fired-oven-600.webp 600w, assets/wood-fired-oven-800.webp 800w, assets/wood-fired-oven-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
                <img src="assets/wood-fired-oven-600.webp" alt="Forno a lenha artesanal com chamas e lenha em brasa" class="img-oven" width="800" height="533" loading="lazy" decoding="async">
              </picture>"""

new_oven = """              <picture>
                <source media="(max-width: 600px)" srcset="assets/wood-fired-oven-400.webp 1x, assets/wood-fired-oven-600.webp 2x">
                <source media="(min-width: 601px)" srcset="assets/wood-fired-oven-600.webp 600w, assets/wood-fired-oven-800.webp 800w, assets/wood-fired-oven-1600.webp 1600w" sizes="42vw">
                <img src="assets/wood-fired-oven-600.webp" alt="Forno a lenha artesanal com chamas e lenha em brasa" class="img-oven" width="800" height="533" loading="lazy" decoding="async">
              </picture>"""

if old_oven in html:
    html = html.replace(old_oven, new_oven)
    print("Oven picture updated.")
else:
    print("Warning: old_oven not matched!")

# 6. Update Wine napkin picture
old_wine = """            <picture>
              <source srcset="assets/wine-napkin-400.webp 400w, assets/wine-napkin-600.webp 600w, assets/wine-napkin-800.webp 800w, assets/wine-napkin-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
              <img src="assets/wine-napkin-600.webp" alt="Taça de vinho branco com toalha de mesa xadrez verde artesanal" class="img-wine-napkin" width="800" height="667" loading="lazy" decoding="async">
            </picture>"""

new_wine = """            <picture>
              <source media="(max-width: 600px)" srcset="assets/wine-napkin-400.webp 1x, assets/wine-napkin-600.webp 2x">
              <source media="(min-width: 601px)" srcset="assets/wine-napkin-600.webp 600w, assets/wine-napkin-800.webp 800w, assets/wine-napkin-1600.webp 1600w" sizes="42vw">
              <img src="assets/wine-napkin-600.webp" alt="Taça de vinho branco com toalha de mesa xadrez verde artesanal" class="img-wine-napkin" width="800" height="667" loading="lazy" decoding="async">
            </picture>"""

if old_wine in html:
    html = html.replace(old_wine, new_wine)
    print("Wine picture updated.")
else:
    print("Warning: old_wine not matched!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("site/index.html picture sources updated successfully!")
