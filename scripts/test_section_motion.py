import os
import sys
import time
from playwright.sync_api import sync_playwright

def test_section(section_id, screenshot_name):
    file_url = "file:///" + os.path.abspath("site/index.html").replace("\\", "/")
    print(f"Testing section {section_id} on: {file_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: console_errors.append(str(err)))

        page.goto(file_url, wait_until="networkidle")

        # 1. Checar estado imediato (above fold não bloqueado)
        sec = page.locator(f"#{section_id}")
        assert sec.count() == 1, f"Seção {section_id} não encontrada!"

        # Scroll rápido para a seção
        sec.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)

        # 2. Verificar que todos os elementos com data-reveal estão com opacity == 1 e visíveis após settle
        reveals_status = page.evaluate(f"""() => {{
            const sec = document.querySelector('#{section_id}');
            const reveals = sec.querySelectorAll('[data-reveal]');
            const results = [];
            reveals.forEach(el => {{
                const style = window.getComputedStyle(el);
                results.push({{
                    tag: el.tagName,
                    classes: el.className,
                    opacity: parseFloat(style.opacity),
                    visibility: style.visibility,
                    transform: style.transform
                }});
            }});
            return results;
        }}""")

        print(f"Elements in #{section_id}:", len(reveals_status))
        for item in reveals_status:
            print(f"  - {item['classes']}: opacity={item['opacity']}, visibility={item['visibility']}, transform={item['transform']}")
            assert item["opacity"] >= 0.95, f"Elemento {item['classes']} ficou preso com opacity < 0.95 ({item['opacity']})!"
            assert item["visibility"] != "hidden", f"Elemento {item['classes']} está oculto!"

        # 3. Teste de empilhamento da spine contínua
        spine_status = page.evaluate("""() => {
            const spine = document.querySelector('.cheese-pull-spine');
            const style = window.getComputedStyle(spine);
            return {
                transform: style.transform,
                opacity: parseFloat(style.opacity),
                zIndex: style.zIndex
            };
        }""")
        print("Spine status:", spine_status)
        assert spine_status["transform"] == "none", "Spine contínua ganhou transform indevido!"
        assert spine_status["opacity"] >= 0.8, "Spine contínua perdeu opacidade!"

        # 4. Captura de tela para confirmação visual
        os.makedirs("screenshots", exist_ok=True)
        sec.screenshot(path=f"screenshots/{screenshot_name}")
        print(f"Screenshot salvo em screenshots/{screenshot_name}")

        browser.close()

        assert len(console_errors) == 0, f"Erros no console: {console_errors}"
        print(f"Seção {section_id} validada com sucesso!")

if __name__ == "__main__":
    sec_id = sys.argv[1] if len(sys.argv) > 1 else "hero-crust-alchemy"
    shot_name = sys.argv[2] if len(sys.argv) > 2 else "phase_b_hero.png"
    test_section(sec_id, shot_name)
