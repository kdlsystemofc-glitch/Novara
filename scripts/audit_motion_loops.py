import os
import json
from playwright.sync_api import sync_playwright

def audit_loops():
    file_url = "file:///" + os.path.abspath("site/index.html").replace("\\", "/")
    print(f"Auditing motion loops on: {file_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        page.goto(file_url, wait_until="networkidle")
        page.wait_for_timeout(600)

        # Obter lista de todos os elementos com data-loop
        loops_info = page.evaluate("""() => {
            const loopEls = Array.from(document.querySelectorAll('[data-loop]'));
            return loopEls.map((el, idx) => {
                const rect = el.getBoundingClientRect();
                return {
                    id: idx + 1,
                    selector: el.className || el.tagName,
                    type: el.getAttribute('data-loop'),
                    parentSection: el.closest('.editorial-section') ? el.closest('.editorial-section').id : 'none',
                    offsetTop: window.scrollY + rect.top,
                    height: rect.height
                };
            });
        }""")

        print(f"Total loop elements found: {len(loops_info)}")
        for l in loops_info:
            print(f"  #{l['id']} [{l['parentSection']}] {l['selector']} ({l['type']}) at Y={l['offsetTop']:.0f}px")

        # Testar contagem de loops visíveis na viewport em diferentes posições de scroll
        max_scroll = page.evaluate("() => document.body.scrollHeight - window.innerHeight")
        step = 400
        scroll_positions = list(range(0, int(max_scroll) + step, step))

        results_by_scroll = []

        for scroll_y in scroll_positions:
            page.evaluate(f"() => window.scrollTo(0, {scroll_y})")
            page.wait_for_timeout(200)

            active_in_viewport = page.evaluate("""() => {
                const winH = window.innerHeight;
                const loopEls = Array.from(document.querySelectorAll('[data-loop]'));
                const active = [];
                loopEls.forEach(el => {
                    const rect = el.getBoundingClientRect();
                    // Elemento dentro da viewport
                    const isVisible = rect.bottom > 0 && rect.top < winH;
                    if (isVisible) {
                        active.push({
                            selector: el.className,
                            type: el.getAttribute('data-loop')
                        });
                    }
                });
                return active;
            }""")

            results_by_scroll.append({
                "scrollY": scroll_y,
                "count": len(active_in_viewport),
                "elements": active_in_viewport
            })
            print(f"Scroll Y={scroll_y}px -> {len(active_in_viewport)} loops ativos: {[e['selector'].split()[0] for e in active_in_viewport]}")
            assert len(active_in_viewport) <= 3, f"Excesso de loops simultâneos em Y={scroll_y}: {len(active_in_viewport)} (máx permitido: 3)"

        browser.close()
        print("AUDITORIA DE LOOPS CONCLUÍDA: Todos os pontos de rolagem têm <= 3 loops simultâneos!")
        return loops_info, results_by_scroll

if __name__ == "__main__":
    audit_loops()
