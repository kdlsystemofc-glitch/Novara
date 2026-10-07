import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

VIEWPORTS = [
    ('2560x1440', 2560, 1440),
    ('1920x1080', 1920, 1080),
    ('1440x900', 1440, 900),
    ('1366x768', 1366, 768),
    ('1280x720', 1280, 720),
    ('1024x768', 1024, 768),
    ('768x1024', 768, 1024),
    ('430x932', 430, 932),
    ('390x844', 390, 844),
    ('360x740', 360, 740),
    ('320x568', 320, 568),
    ('844x390_landscape', 844, 390),
]

def run_tests():
    file_url = Path('site/index.html').resolve().as_uri()
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--allow-file-access-from-files"])
        for name, w, h in VIEWPORTS:
            errors = []
            page = browser.new_page(viewport={'width': w, 'height': h})
            page.on('console', lambda msg: errors.append(f'Console: {msg.text}') if msg.type == 'error' else None)
            page.on('pageerror', lambda exc: errors.append(f'PageError: {exc}'))
            
            page.goto(file_url, wait_until='networkidle')
            
            # 1. Horizontal scroll check
            scroll_w = page.evaluate('document.documentElement.scrollWidth')
            client_w = page.evaluate('document.documentElement.clientWidth')
            has_h_scroll = scroll_w > client_w
            
            # 2. Touch targets check (>= 44x44px for actionable elements)
            targets = page.evaluate('''() => {
                const els = Array.from(document.querySelectorAll('a, button, [role="button"]'));
                return els.map(el => {
                    const r = el.getBoundingClientRect();
                    return {
                        text: (el.innerText || el.getAttribute('aria-label') || el.className).trim().slice(0, 35),
                        w: Math.round(r.width * 10) / 10,
                        h: Math.round(r.height * 10) / 10,
                        ok: r.width >= 43.5 && r.height >= 43.5
                    };
                });
            }''')
            
            small_targets = [t for t in targets if not t['ok']]

            # 3. Check text zoom 200%
            page_zoom = browser.new_page(viewport={'width': w, 'height': h})
            page_zoom.goto(file_url, wait_until='networkidle')
            page_zoom.evaluate('document.body.style.fontSize = "200%"')
            zoom_scroll_w = page_zoom.evaluate('document.documentElement.scrollWidth')
            zoom_client_w = page_zoom.evaluate('document.documentElement.clientWidth')
            zoom_h_scroll = zoom_scroll_w > zoom_client_w
            page_zoom.close()

            # 4. Check prefers-reduced-motion
            page_prm = browser.new_page(viewport={'width': w, 'height': h}, reduced_motion='reduce')
            page_prm.goto(file_url, wait_until='networkidle')
            prm_errors = []
            page_prm.on('pageerror', lambda exc: prm_errors.append(str(exc)))
            page_prm.close()

            # 5. Check prefers-color-scheme dark
            page_dark = browser.new_page(viewport={'width': w, 'height': h}, color_scheme='dark')
            page_dark.goto(file_url, wait_until='networkidle')
            dark_bg = page_dark.evaluate('window.getComputedStyle(document.body).backgroundColor')
            page_dark.close()

            # Capture screenshot
            screenshot_path = f'screenshots/responsive_{name}.png'
            page.screenshot(path=screenshot_path, full_page=True)

            status = 'PASS' if not has_h_scroll and not errors and not small_targets else 'FAIL'
            res = {
                'name': name,
                'width': w,
                'height': h,
                'status': status,
                'h_scroll': has_h_scroll,
                'scroll_w': scroll_w,
                'client_w': client_w,
                'zoom_h_scroll': zoom_h_scroll,
                'errors': errors,
                'small_targets': small_targets,
                'dark_bg': dark_bg,
                'screenshot': screenshot_path
            }
            results.append(res)
            print(f"[{status}] {name} ({w}x{h}): scrollW={scroll_w}, clientW={client_w}, h_scroll={has_h_scroll}, zoom_h_scroll={zoom_h_scroll}, errors={len(errors)}, small_targets={len(small_targets)}")
            if small_targets:
                for st in small_targets:
                    print(f"    Target < 44px: '{st['text']}' ({st['w']}x{st['h']}px)")
            if errors:
                for err in errors:
                    print(f"    Error: {err}")
            
            page.close()
        browser.close()
    return results

if __name__ == '__main__':
    run_tests()
