import os
import sys
import time
from playwright.sync_api import sync_playwright

def test_fast_scroll():
    file_url = "file:///" + os.path.abspath("site/index.html").replace("\\", "/")
    print(f"Testing fast scroll on: {file_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--allow-file-access-from-files"])
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        page.goto(file_url, wait_until="networkidle")
        page.evaluate("() => { if (window.__loadMotionNow) window.__loadMotionNow(); }")
        page.wait_for_timeout(600)

        # 1. Rolagem rápida para o fundo
        page.evaluate("() => window.scrollTo({ top: document.body.scrollHeight, behavior: 'auto' })")
        page.wait_for_timeout(800)

        # 2. Rolagem rápida de volta para o topo
        page.evaluate("() => window.scrollTo({ top: 0, behavior: 'auto' })")
        page.wait_for_timeout(800)

        # 3. Rolagem intermediária
        page.evaluate("() => window.scrollTo({ top: 1200, behavior: 'auto' })")
        # Aguardar tempo de animação (duration 0.75s + delay 0.3s)
        page.wait_for_timeout(1400)

        # Verificar se algum elemento com data-reveal ficou preso com opacity < 0.95
        stuck_elements = page.evaluate("""() => {
            const reveals = document.querySelectorAll('[data-reveal]');
            const stuck = [];
            reveals.forEach(el => {
                const style = window.getComputedStyle(el);
                const op = parseFloat(style.opacity);
                if (op < 0.95 || style.visibility === 'hidden') {
                    stuck.push({
                        selector: el.className || el.tagName,
                        opacity: op,
                        visibility: style.visibility
                    });
                }
            });
            return stuck;
        }""")

        print("Stuck elements check:", stuck_elements)
        assert len(stuck_elements) == 0, f"Elementos ficaram presos escondidos após navegação rápida: {stuck_elements}"

        # Captura de tela da página inteira após navegação rápida
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(path="screenshots/phase_b_fast_scroll.png", full_page=True)
        print("Página inteira capturada com sucesso em screenshots/phase_b_fast_scroll.png")

        browser.close()
        print("TESTE DE NAVEGAÇÃO RÁPIDA: APROVADO COM 100% DE SUCESSO!")

if __name__ == "__main__":
    test_fast_scroll()
