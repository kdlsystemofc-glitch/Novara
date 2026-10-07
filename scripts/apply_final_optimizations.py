import os
import re

INDEX_PATH = "site/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update LCP preload in head: change from dough to cheese ribbon
old_lcp_preload = """  <!-- Preload da Imagem LCP Candidata Acima da Dobra -->
  <link rel="preload" as="image" href="assets/dough-fermentation-400.webp" imagesrcset="assets/dough-fermentation-400.webp 400w, assets/dough-fermentation-800.webp 800w, assets/dough-fermentation-1600.webp 1600w" imagesizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw" fetchpriority="high">"""

new_lcp_preload = """  <!-- Preload da Imagem LCP Candidata Acima da Dobra (Fio de Queijo Spine) -->
  <link rel="preload" as="image" href="assets/cheese-ribbon-800.webp" imagesrcset="assets/cheese-ribbon-400.webp 133w, assets/cheese-ribbon-800.webp 267w, assets/cheese-ribbon-1200.webp 400w, assets/cheese-ribbon-1600.webp 533w" imagesizes="(max-width: 600px) 290px, 42vw" fetchpriority="high">"""

if old_lcp_preload in html:
    html = html.replace(old_lcp_preload, new_lcp_preload)
    print("Preload updated to cheese-ribbon.")
else:
    print("Warning: old_lcp_preload not found!")

# 2. Update cheese ribbon in body with fetchpriority="high" and new srcset
old_spine = """      <picture>
        <source srcset="assets/cheese-ribbon-400.webp 400w, assets/cheese-ribbon-800.webp 800w, assets/cheese-ribbon-1600.webp 1600w" sizes="(max-width: 600px) 290px, 42vw">
        <img src="assets/cheese-ribbon-400.webp" alt="Fio de queijo mozzarella puxado da pizza" width="267" height="800" decoding="async">
      </picture>"""

new_spine = """      <picture>
        <source srcset="assets/cheese-ribbon-400.webp 133w, assets/cheese-ribbon-800.webp 267w, assets/cheese-ribbon-1200.webp 400w, assets/cheese-ribbon-1600.webp 533w" sizes="(max-width: 600px) 290px, 42vw">
        <img src="assets/cheese-ribbon-800.webp" alt="Fio de queijo mozzarella puxado da pizza" width="267" height="800" fetchpriority="high" decoding="async">
      </picture>"""

if old_spine in html:
    html = html.replace(old_spine, new_spine)
    print("Spine updated.")
else:
    print("Warning: old_spine not found!")

# 3. Update dough image with 600w step and loading="lazy"
old_dough = """            <picture>
              <source srcset="assets/dough-fermentation-400.webp 400w, assets/dough-fermentation-800.webp 800w, assets/dough-fermentation-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
              <img src="assets/dough-fermentation-800.webp" alt="Massa de pizza artesanal fermentando sobre pedra com farinha" class="img-dough" width="800" height="533" fetchpriority="high" decoding="async">
            </picture>"""

new_dough = """            <picture>
              <source srcset="assets/dough-fermentation-400.webp 400w, assets/dough-fermentation-600.webp 600w, assets/dough-fermentation-800.webp 800w, assets/dough-fermentation-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
              <img src="assets/dough-fermentation-600.webp" alt="Massa de pizza artesanal fermentando sobre pedra com farinha" class="img-dough" width="800" height="533" loading="lazy" decoding="async">
            </picture>"""

if old_dough in html:
    html = html.replace(old_dough, new_dough)
    print("Dough image updated.")
else:
    print("Warning: old_dough not found!")

# 4. Update raw ingredients with 600w step
old_polaroid = """              <picture>
                <source srcset="assets/raw-ingredients-400.webp 400w, assets/raw-ingredients-800.webp 800w, assets/raw-ingredients-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
                <img src="assets/raw-ingredients-800.webp" alt="Ingredientes frescos selecionados: tomates italianos, burrata e especiarias" class="img-polaroid" width="800" height="800" loading="lazy" decoding="async">
              </picture>"""

new_polaroid = """              <picture>
                <source srcset="assets/raw-ingredients-400.webp 400w, assets/raw-ingredients-600.webp 600w, assets/raw-ingredients-800.webp 800w, assets/raw-ingredients-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
                <img src="assets/raw-ingredients-600.webp" alt="Ingredientes frescos selecionados: tomates italianos, burrata e especiarias" class="img-polaroid" width="800" height="800" loading="lazy" decoding="async">
              </picture>"""

if old_polaroid in html:
    html = html.replace(old_polaroid, new_polaroid)
    print("Polaroid image updated.")
else:
    print("Warning: old_polaroid not found!")

# 5. Update wood-fired oven with 600w step
old_oven = """              <picture>
                <source srcset="assets/wood-fired-oven-400.webp 400w, assets/wood-fired-oven-800.webp 800w, assets/wood-fired-oven-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
                <img src="assets/wood-fired-oven-800.webp" alt="Forno a lenha artesanal com chamas e lenha em brasa" class="img-oven" width="800" height="533" loading="lazy" decoding="async">
              </picture>"""

new_oven = """              <picture>
                <source srcset="assets/wood-fired-oven-400.webp 400w, assets/wood-fired-oven-600.webp 600w, assets/wood-fired-oven-800.webp 800w, assets/wood-fired-oven-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
                <img src="assets/wood-fired-oven-600.webp" alt="Forno a lenha artesanal com chamas e lenha em brasa" class="img-oven" width="800" height="533" loading="lazy" decoding="async">
              </picture>"""

if old_oven in html:
    html = html.replace(old_oven, new_oven)
    print("Oven image updated.")
else:
    print("Warning: old_oven not found!")

# 6. Update buzzer button aspect ratio (height 60 instead of 80)
old_buzzer = """                  <source srcset="assets/push-button-3d-160.webp 160w, assets/push-button-3d-320.webp 320w" sizes="80px">
                  <img src="assets/push-button-3d-160.webp" alt="Botão campainha 3D de pedidos Novara" class="img-buzzer-3d" width="80" height="80" loading="lazy" decoding="async">"""

new_buzzer = """                  <source srcset="assets/push-button-3d-160.webp 160w, assets/push-button-3d-320.webp 320w" sizes="80px">
                  <img src="assets/push-button-3d-160.webp" alt="Botão campainha 3D de pedidos Novara" class="img-buzzer-3d" width="80" height="60" loading="lazy" decoding="async">"""

if old_buzzer in html:
    html = html.replace(old_buzzer, new_buzzer)
    print("Buzzer image updated.")
else:
    print("Warning: old_buzzer not found!")

# 7. Update wine napkin with 600w step
old_wine = """            <picture>
              <source srcset="assets/wine-napkin-400.webp 400w, assets/wine-napkin-800.webp 800w, assets/wine-napkin-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
              <img src="assets/wine-napkin-800.webp" alt="Taça de vinho branco com toalha de mesa xadrez verde artesanal" class="img-wine-napkin" width="800" height="667" loading="lazy" decoding="async">
            </picture>"""

new_wine = """            <picture>
              <source srcset="assets/wine-napkin-400.webp 400w, assets/wine-napkin-600.webp 600w, assets/wine-napkin-800.webp 800w, assets/wine-napkin-1600.webp 1600w" sizes="(max-width: 600px) 92vw, (max-width: 1024px) 50vw, 42vw">
              <img src="assets/wine-napkin-600.webp" alt="Taça de vinho branco com toalha de mesa xadrez verde artesanal" class="img-wine-napkin" width="800" height="667" loading="lazy" decoding="async">
            </picture>"""

if old_wine in html:
    html = html.replace(old_wine, new_wine)
    print("Wine napkin updated.")
else:
    print("Warning: old_wine not found!")

# 8. Update motion-toggle-btn aria-label to match visible label "Pausar Motion"
old_btn = 'aria-label="Pausar animações do site"'
new_btn = 'aria-label="Pausar Motion"'
if old_btn in html:
    html = html.replace(old_btn, new_btn)
    print("Button aria-label updated.")
else:
    print("Warning: old_btn not found!")

# 9. Update idle callback timeout to 3500ms
old_timeout = "requestIdleCallback(loadMotionScripts, { timeout: 1200 });"
new_timeout = """window.__loadMotionNow = loadMotionScripts;
          requestIdleCallback(loadMotionScripts, { timeout: 3500 });"""
if old_timeout in html:
    html = html.replace(old_timeout, new_timeout)
    print("Idle timeout updated.")
else:
    print("Warning: old_timeout not found!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Final optimizations applied to site/index.html!")
