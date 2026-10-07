import os
import sys
import time
from playwright.sync_api import sync_playwright

def test_motion_base():
    file_url = "file:///" + os.path.abspath("site/index.html").replace("\\", "/")
    print(f"Testing motion base on: {file_url}")

    errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        page.on("console", lambda msg: print(f"[BROWSER CONSOLE {msg.type}] {msg.text}") if msg.type in ["error", "warning"] else None)
        page.on("pageerror", lambda err: errors.append(f"PageError: {err}"))

        page.goto(file_url, wait_until="networkidle")

        # Aguardar um momento para os scripts carregarem após load
        page.wait_for_timeout(500)

        # 1. Verificar se NovaraMotion, gsap, ScrollTrigger, Lenis existem
        motion_status = page.evaluate("""() => {
            return {
                hasGsap: typeof window.gsap !== 'undefined',
                hasScrollTrigger: typeof window.ScrollTrigger !== 'undefined',
                hasLenis: typeof window.Lenis !== 'undefined',
                hasNovaraMotion: typeof window.NovaraMotion !== 'undefined',
                mode: window.NovaraMotion ? window.NovaraMotion.mode : null,
                quality: window.NovaraMotion ? window.NovaraMotion.quality : null,
                hasLenisInstance: !!(window.NovaraMotion && window.NovaraMotion.lenis)
            };
        }""")

        print("Motion status:", motion_status)
        assert motion_status["hasGsap"], "GSAP não foi carregado!"
        assert motion_status["hasScrollTrigger"], "ScrollTrigger não foi carregado!"
        assert motion_status["hasLenis"], "Lenis não foi carregado!"
        assert motion_status["hasNovaraMotion"], "NovaraMotion não foi inicializado!"
        assert motion_status["mode"] in ["full", "reduced"], f"Modo inválido: {motion_status['mode']}"
        assert motion_status["quality"] in ["high", "low"], f"Qualidade inválida: {motion_status['quality']}"

        # 2. Testar toggle de pausa
        pause_result = page.evaluate("""() => {
            const paused = window.NovaraMotion.togglePause();
            const modeAfterPause = window.NovaraMotion.mode;
            window.NovaraMotion.togglePause(); // retomar
            const modeAfterResume = window.NovaraMotion.mode;
            return { paused, modeAfterPause, modeAfterResume };
        }""")
        print("Pause toggle test:", pause_result)
        assert pause_result["modeAfterPause"] == "paused", "Falha ao pausar motor de motion!"
        assert pause_result["modeAfterResume"] in ["full", "reduced"], "Falha ao retomar motor de motion!"

        # 3. Verificar que .cheese-pull-spine e ancestrais NÃO possuem transform/filter/opacity < 1
        spine_check = page.evaluate("""() => {
            const spine = document.querySelector('.cheese-pull-spine');
            if (!spine) return { found: false };

            const checkEl = (el) => {
                const style = window.getComputedStyle(el);
                return {
                    transform: style.transform !== 'none' ? style.transform : null,
                    filter: style.filter !== 'none' ? style.filter : null,
                    opacity: parseFloat(style.opacity)
                };
            };

            const spineStyle = checkEl(spine);
            let ancestor = spine.parentElement;
            const ancestors = [];
            while (ancestor && ancestor !== document.documentElement) {
                ancestors.push({ tag: ancestor.tagName, ...checkEl(ancestor) });
                ancestor = ancestor.parentElement;
            }

            return { found: true, spine: spineStyle, ancestors };
        }""")

        print("Spine check:", spine_check)
        assert spine_check["found"], "Elemento .cheese-pull-spine não encontrado!"
        assert spine_check["spine"]["transform"] is None or spine_check["spine"]["transform"] == 'none', "Spine tem transform ativo!"
        for anc in spine_check["ancestors"]:
            assert anc["transform"] is None or anc["transform"] == 'none', f"Ancestral {anc['tag']} tem transform ativo!"
            assert anc["filter"] is None or anc["filter"] == 'none', f"Ancestral {anc['tag']} tem filter ativo!"
            assert anc["opacity"] >= 1, f"Ancestral {anc['tag']} tem opacity < 1!"

        # 4. Verificar overflow horizontal
        scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
        client_width = page.evaluate("() => document.documentElement.clientWidth")
        print(f"Scroll width: {scroll_width}, Client width: {client_width}")
        assert scroll_width <= client_width, "Detectado overflow horizontal!"

        # 5. Captura de tela para confirmação visual
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(path="screenshots/phase_a_motion_base.png", full_page=True)
        print("Screenshot salvo em screenshots/phase_a_motion_base.png")

        browser.close()

    if errors:
        print("Erros detectados:", errors)
        sys.exit(1)
    else:
        print("FASE A: TODOS OS TESTES PASSARAM COM SUCESSO!")

if __name__ == "__main__":
    test_motion_base()
