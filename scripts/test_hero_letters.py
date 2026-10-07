import os
import sys
from playwright.sync_api import sync_playwright

def test_hero():
    file_url = "file:///" + os.path.abspath("site/index.html").replace("\\", "/")
    print(f"Testing enhanced hero choreography on: {file_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        page.goto(file_url, wait_until="networkidle")

        # 1. Checar atributos acessíveis
        title = page.locator(".brand-hero-title")
        assert title.get_attribute("aria-label") == "NOVARA", "aria-label no título não está presente!"

        letters = page.locator(".hero-letter")
        assert letters.count() == 6, f"Deveria ter 6 letras, encontrou {letters.count()}"

        # 2. Capturar quadro intermediário (durante a carimbada / letterpress)
        page.wait_for_timeout(350)
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(path="screenshots/hero_keyframes_stamp.png")
        print("Quadro intermediário salvo: screenshots/hero_keyframes_stamp.png")

        # 3. Aguardar assentamento completo
        page.wait_for_timeout(1500)
        page.screenshot(path="screenshots/hero_settled.png")
        print("Quadro final assentado salvo: screenshots/hero_settled.png")

        # 4. Verificar que todas as letras estão 100% visíveis
        letters_state = page.evaluate("""() => {
            const letters = Array.from(document.querySelectorAll('.hero-letter'));
            return letters.map(el => {
                const s = window.getComputedStyle(el);
                return {
                    text: el.textContent,
                    opacity: parseFloat(s.opacity),
                    transform: s.transform
                };
            });
        }""")
        print("Letras de NOVARA:", letters_state)
        for l in letters_state:
            assert l["opacity"] >= 0.98, f"Letra {l['text']} não assentou com opacidade completa!"

        # 5. Testar interação de mousemove (Parallax do Hero)
        hero = page.locator("#hero-crust-alchemy")
        hero_box = hero.bounding_box()
        # Mover mouse no hero
        page.mouse.move(hero_box["x"] + 200, hero_box["y"] + 200)
        page.wait_for_timeout(300)
        page.mouse.move(hero_box["x"] + 800, hero_box["y"] + 400)
        page.wait_for_timeout(300)

        # 6. Testar hover em stickers (com force=True pois o elemento possui loop flutuante)
        basil = page.locator(".sticker-basil-wrap")
        basil.hover(force=True)
        page.wait_for_timeout(200)
        page.screenshot(path="screenshots/hero_basil_hover.png")
        print("Hover no manjericão salvo: screenshots/hero_basil_hover.png")

        browser.close()
        print("TESTE DE COREOGRAFIA DO HERO APROVADO COM 100% DE SUCESSO!")

if __name__ == "__main__":
    test_hero()
