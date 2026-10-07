import os
import sys
import json
import http.server
import socketserver
import threading
from pathlib import Path
from playwright.sync_api import sync_playwright

VIEWPORTS = [
    ('3840x2160_4K', 3840, 2160),
    ('3440x1440_ultrawide', 3440, 1440),
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

MODES = [
    {'name': 'default', 'reduced_motion': 'no-preference', 'color_scheme': 'light'},
    {'name': 'reduced_motion', 'reduced_motion': 'reduce', 'color_scheme': 'light'},
    {'name': 'dark_scheme', 'reduced_motion': 'no-preference', 'color_scheme': 'dark'},
]

def run_full_audit():
    PORT = 8899
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(('127.0.0.1', PORT), Handler)
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    base_url = f"http://127.0.0.1:{PORT}/site/index.html"
    report = {
        'browsers': {},
        'summary': {'total_tests': 0, 'passed': 0, 'failed': 0, 'issues': []}
    }

    try:
        with sync_playwright() as p:
            browsers_to_test = [
                ('chromium', p.chromium.launch()),
                ('webkit', p.webkit.launch()),
            ]

            for b_name, browser in browsers_to_test:
                print(f"\n==========================================")
                print(f"=== TESTING ENGINE: {b_name.upper()} ===")
                print(f"==========================================")
                report['browsers'][b_name] = {'viewports': [], 'modes': []}

                # 1. Test all 14 viewports
                for vp_name, w, h in VIEWPORTS:
                    report['summary']['total_tests'] += 1
                    errors = []
                    context = browser.new_context(viewport={'width': w, 'height': h})
                    page = context.new_page()
                    page.on('console', lambda msg: errors.append(f'Console: {msg.text}') if msg.type == 'error' else None)
                    page.on('pageerror', lambda exc: errors.append(f'PageError: {exc}'))

                    try:
                        page.goto(base_url, wait_until='networkidle')
                        page.wait_for_timeout(300)

                        scroll_w = page.evaluate('document.documentElement.scrollWidth')
                        client_w = page.evaluate('document.documentElement.clientWidth')
                        has_h_scroll = scroll_w > client_w

                        # Touch target >= 44x44
                        small_targets = page.evaluate('''() => {
                            const els = Array.from(document.querySelectorAll('a, button, [role="button"]'));
                            return els.map(el => {
                                const r = el.getBoundingClientRect();
                                return {
                                    text: (el.innerText || el.getAttribute('aria-label') || el.className).trim().slice(0, 30),
                                    w: Math.round(r.width * 10) / 10,
                                    h: Math.round(r.height * 10) / 10,
                                    ok: r.width >= 43.0 && r.height >= 43.0
                                };
                            }).filter(t => !t.ok);
                        }''')

                        # Verify key structural components
                        elements_check = page.evaluate('''() => {
                            const spine = document.querySelector('.cheese-pull-spine');
                            const h1 = document.querySelector('h1.brand-hero-title');
                            const pauseBtn = document.querySelector('#motion-toggle-btn');
                            const sections = document.querySelectorAll('section');
                            return {
                                spineExists: !!spine,
                                h1Exists: !!h1,
                                pauseBtnExists: !!pauseBtn,
                                sectionCount: sections.length
                            };
                        }''')

                        passed = (not has_h_scroll) and (len(errors) == 0) and (len(small_targets) == 0) and elements_check['h1Exists'] and (elements_check['sectionCount'] >= 4)
                        if passed:
                            report['summary']['passed'] += 1
                            status_str = "PASS"
                        else:
                            report['summary']['failed'] += 1
                            status_str = "FAIL"
                            report['summary']['issues'].append({
                                'browser': b_name,
                                'viewport': vp_name,
                                'scroll_w': scroll_w,
                                'client_w': client_w,
                                'has_h_scroll': has_h_scroll,
                                'errors': errors,
                                'small_targets': small_targets
                            })

                        print(f"[{b_name:8}] {vp_name:20} -> {status_str} | Viewport: {client_w}x{h} | ScrollW: {scroll_w} | Errs: {len(errors)}")
                        report['browsers'][b_name]['viewports'].append({
                            'name': vp_name,
                            'w': w,
                            'h': h,
                            'scroll_w': scroll_w,
                            'client_w': client_w,
                            'passed': passed,
                            'errors': errors
                        })
                    except Exception as e:
                        report['summary']['failed'] += 1
                        report['summary']['issues'].append({'browser': b_name, 'viewport': vp_name, 'exception': str(e)})
                        print(f"[{b_name:8}] {vp_name:20} -> EXCEPTION: {e}")
                    finally:
                        context.close()

                # 2. Test Modes (Default, Reduced Motion, Dark Scheme, Motion Paused)
                for mode in MODES:
                    for vp_name, w, h in [('desktop_1440', 1440, 900), ('mobile_390', 390, 844)]:
                        report['summary']['total_tests'] += 1
                        errors = []
                        context = browser.new_context(
                            viewport={'width': w, 'height': h},
                            reduced_motion=mode['reduced_motion'],
                            color_scheme=mode['color_scheme']
                        )
                        page = context.new_page()
                        page.on('console', lambda msg: errors.append(f'Console: {msg.text}') if msg.type == 'error' else None)
                        page.on('pageerror', lambda exc: errors.append(f'PageError: {exc}'))

                        page.goto(base_url, wait_until='networkidle')
                        # Trigger deferred motion loader explicitly
                        page.evaluate('() => { if (window.__loadMotionNow) window.__loadMotionNow(); }')
                        page.wait_for_timeout(350)

                        btn = page.locator('#motion-toggle-btn')
                        btn_count = btn.count()
                        if btn_count > 0:
                            before = btn.get_attribute('aria-pressed')
                            btn.click()
                            page.wait_for_timeout(100)
                            after = btn.get_attribute('aria-pressed')
                            btn.click() # restore
                            page.wait_for_timeout(100)
                            pause_ok = (before != after) and (after == 'true')
                        else:
                            pause_ok = False

                        scroll_w = page.evaluate('document.documentElement.scrollWidth')
                        client_w = page.evaluate('document.documentElement.clientWidth')
                        passed = (scroll_w <= client_w) and (len(errors) == 0) and pause_ok
                        if passed:
                            report['summary']['passed'] += 1
                            status_str = "PASS"
                        else:
                            report['summary']['failed'] += 1
                            status_str = "FAIL"
                            report['summary']['issues'].append({
                                'browser': b_name,
                                'mode': mode['name'],
                                'viewport': vp_name,
                                'errors': errors,
                                'pause_ok': pause_ok
                            })

                        print(f"[{b_name:8}] Mode: {mode['name']:15} ({vp_name}) -> {status_str} | PauseToggle: {pause_ok}")
                        report['browsers'][b_name]['modes'].append({
                            'mode': mode['name'],
                            'viewport': vp_name,
                            'passed': passed,
                            'errors': errors
                        })
                        context.close()

                browser.close()
    finally:
        httpd.shutdown()

    out_file = Path('audit-browsers-modes-result.json')
    out_file.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(f"\n==========================================")
    print(f"AUDIT SUMMARY:")
    print(f"Total Tests Executed: {report['summary']['total_tests']}")
    print(f"Passed: {report['summary']['passed']}")
    print(f"Failed: {report['summary']['failed']}")
    print(f"Issues Count: {len(report['summary']['issues'])}")
    print(f"==========================================")

if __name__ == '__main__':
    run_full_audit()
