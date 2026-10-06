"""
Script automatizado de capturas de tela com Playwright.
Gera screenshots de seção isolada, página inteira e costura entre seções,
nos viewports 1440x900 (Desktop) e 390x844 (Mobile).
"""

import os
import sys
import argparse
import time
from playwright.sync_api import sync_playwright

def run_screenshot(section_id, prev_section_id=None, viewports=None):
    if viewports is None:
        viewports = [
            ('1440', 1440, 900),
            ('390', 390, 844)
        ]

    os.makedirs('screenshots', exist_ok=True)
    html_path = os.path.abspath('site/index.html')
    file_url = f'file:///{html_path.replace(os.sep, "/")}'

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for vp_name, width, height in viewports:
            context = browser.new_context(
                viewport={'width': width, 'height': height},
                device_scale_factor=2
            )
            page = context.new_page()
            page.goto(file_url, wait_until='networkidle')
            time.sleep(0.5)

            # 1. Página inteira
            full_path = f'screenshots/{section_id}_fullpage_{vp_name}.png'
            page.screenshot(path=full_path, full_page=True)
            print(f'Salvo: {full_path}')

            # 2. Seção isolada
            sec_el = page.query_selector(f'#{section_id}')
            if sec_el:
                iso_path = f'screenshots/{section_id}_isolated_{vp_name}.png'
                sec_el.screenshot(path=iso_path)
                print(f'Salvo: {iso_path}')
            else:
                print(f'Aviso: elemento #{section_id} não encontrado!')

            # 3. Costura com a seção anterior (se houver)
            if prev_section_id:
                prev_el = page.query_selector(f'#{prev_section_id}')
                if prev_el and sec_el:
                    prev_box = prev_el.bounding_box()
                    curr_box = sec_el.bounding_box()
                    if prev_box and curr_box:
                        # Cortar a área de transição: metade inferior do anterior + metade superior do atual
                        seam_y = max(0, prev_box['y'] + prev_box['height'] * 0.5)
                        seam_h = (curr_box['y'] + curr_box['height'] * 0.5) - seam_y
                        seam_path = f'screenshots/seam_{prev_section_id}_{section_id}_{vp_name}.png'
                        page.screenshot(
                            path=seam_path,
                            clip={'x': 0, 'y': seam_y, 'width': width, 'height': max(100, seam_h)}
                        )
                        print(f'Salvo: {seam_path}')

            context.close()
        browser.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--section', required=True, help='ID da seção')
    parser.add_argument('--prev-section', default=None, help='ID da seção anterior para costura')
    parser.add_argument('--all-viewports', action='store_true', help='Capturar 1440, 768 e 390')
    args = parser.parse_args()

    vps = [('1440', 1440, 900), ('768', 768, 1024), ('390', 390, 844)] if args.all_viewports else [('1440', 1440, 900), ('390', 390, 844)]
    run_screenshot(args.section, args.prev_section, vps)
