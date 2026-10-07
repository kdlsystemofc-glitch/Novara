import os
import sys
from playwright.sync_api import sync_playwright

def test_pause_button():
    file_url = "file:///" + os.path.abspath("site/index.html").replace("\\", "/")
    print(f"Testing pause button on: {file_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        page.goto(file_url, wait_until="networkidle")
        page.evaluate("() => { if (window.__loadMotionNow) window.__loadMotionNow(); }")
        page.wait_for_timeout(600)

        btn = page.locator("#motion-toggle-btn")
        assert btn.count() == 1, "Botão #motion-toggle-btn não encontrado!"

        # Estado inicial
        pressed_init = btn.get_attribute("aria-pressed")
        assert pressed_init == "false", f"Estado inicial deveria ser false, obteve {pressed_init}"
        mode_init = page.evaluate("() => window.NovaraMotion.mode")
        assert mode_init in ["full", "reduced"], f"Modo inicial: {mode_init}"

        # Clicar para pausar
        btn.click()
        page.wait_for_timeout(200)

        pressed_after = btn.get_attribute("aria-pressed")
        mode_after = page.evaluate("() => window.NovaraMotion.mode")
        print(f"Após clique 1: pressed={pressed_after}, mode={mode_after}")
        assert pressed_after == "true", "Botão deveria ter aria-pressed='true' após clique!"
        assert mode_after == "paused", f"Modo deveria ser 'paused', obteve {mode_after}"

        # Clicar para retomar
        btn.click()
        page.wait_for_timeout(200)

        pressed_resume = btn.get_attribute("aria-pressed")
        mode_resume = page.evaluate("() => window.NovaraMotion.mode")
        print(f"Após clique 2: pressed={pressed_resume}, mode={mode_resume}")
        assert pressed_resume == "false", "Botão deveria ter aria-pressed='false' após retomar!"
        assert mode_resume in ["full", "reduced"], f"Modo deveria retornar para full/reduced, obteve {mode_resume}"

        browser.close()
        print("TESTE DO BOTÃO DE PAUSA: APROVADO COM 100% DE SUCESSO!")

if __name__ == "__main__":
    test_pause_button()
