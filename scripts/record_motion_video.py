import os
import time
from playwright.sync_api import sync_playwright

def record_walkthrough():
    os.makedirs("screenshots/videos", exist_ok=True)
    file_url = "file:///" + os.path.abspath("site/index.html").replace("\\", "/")
    print(f"Recording motion walkthrough on: {file_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            record_video_dir="screenshots/videos",
            record_video_size={"width": 1280, "height": 720}
        )
        page = context.new_page()

        page.goto(file_url, wait_until="networkidle")
        page.wait_for_timeout(1000)

        # 1. Contemplar Hero pós-load (2s)
        page.wait_for_timeout(2000)

        # 2. Scroll suave para Seção 2: Matéria-Prima Pura
        page.locator("#materia-prima-pura").scroll_into_view_if_needed()
        page.wait_for_timeout(2200)

        # 3. Scroll suave para Seção 3: Forno & Tempo
        page.locator("#forno-e-tempo").scroll_into_view_if_needed()
        page.wait_for_timeout(2200)

        # 4. Scroll suave para Seção 4: Table & Reservations
        page.locator("#table-reservations").scroll_into_view_if_needed()
        page.wait_for_timeout(2200)

        # 5. Testar botão de pausa em tempo real
        pause_btn = page.locator("#motion-toggle-btn")
        if pause_btn.count() > 0:
            pause_btn.click()
            print("Motion pausado no vídeo.")
            page.wait_for_timeout(1500)
            pause_btn.click()
            print("Motion retomado no vídeo.")
            page.wait_for_timeout(1500)

        # 6. Retorno suave ao topo
        page.locator("#hero-crust-alchemy").scroll_into_view_if_needed()
        page.wait_for_timeout(1800)

        # Finalizar gravação
        page.close()
        context.close()
        browser.close()

    # Listar vídeos gerados
    video_files = os.listdir("screenshots/videos")
    print("Vídeos gravados com sucesso:", video_files)

if __name__ == "__main__":
    record_walkthrough()
