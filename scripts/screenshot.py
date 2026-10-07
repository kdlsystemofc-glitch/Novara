"""
Script automatizado de capturas de tela com Playwright.
Gera screenshots de seção isolada, página inteira e costura entre seções,
com suporte a matriz completa de viewports: 390, 768, 1024, 1440, 1920 e 2560px.
"""

import os
import sys
import argparse
import time
from playwright.sync_api import sync_playwright

VIEWPORT_PRESETS = {
    '390': ('390', 390, 844),
    '768': ('768', 768, 1024),
    '1024': ('1024', 1024, 768),
    '1440': ('1440', 1440, 900),
    '1920': ('1920', 1920, 1080),
    '2560': ('2560', 2560, 1440),
}

def run_screenshot(section_id=None, prev_section_id=None, viewports=None, prefix=''):
    if viewports is None:
        viewports = [
            ('1440', 1440, 900),
            ('1920', 1920, 1080),
            ('2560', 2560, 1440),
            ('390', 390, 844)
        ]

    os.makedirs('screenshots', exist_ok=True)
    html_path = os.path.abspath('site/index.html')
    file_url = f'file:///{html_path.replace(os.sep, "/")}'

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for vp_name, width, height in viewports:
            # Para viewports ultra-largos (2560px), device_scale_factor=1 evita imagens gigantescas de 20MB
            scale = 1 if width >= 2560 else 2
            context = browser.new_context(
                viewport={'width': width, 'height': height},
                device_scale_factor=scale
            )
            page = context.new_page()
            page.goto(file_url, wait_until='networkidle')
            time.sleep(0.5)

            # 1. Página inteira
            if prefix:
                full_path = f'screenshots/{prefix}_fullpage_{vp_name}.png'
            elif section_id:
                full_path = f'screenshots/{section_id}_fullpage_{vp_name}.png'
            else:
                full_path = f'screenshots/fullpage_{vp_name}.png'
            page.screenshot(path=full_path, full_page=True)
            print(f'Salvo: {full_path}')

            # 2. Seção isolada
            if section_id:
                sec_el = page.query_selector(f'#{section_id}')
                if sec_el:
                    iso_path = f'screenshots/{section_id}_isolated_{vp_name}.png'
                    sec_el.screenshot(path=iso_path)
                    print(f'Salvo: {iso_path}')
                else:
                    print(f'Aviso: elemento #{section_id} não encontrado!')

            # 3. Costura com a seção anterior (se houver)
            if prev_section_id and section_id:
                prev_el = page.query_selector(f'#{prev_section_id}')
                sec_el = page.query_selector(f'#{section_id}')
                if prev_el and sec_el:
                    prev_box = prev_el.bounding_box()
                    curr_box = sec_el.bounding_box()
                    if prev_box and curr_box:
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
    parser.add_argument('--section', default=None, help='ID da seção')
    parser.add_argument('--prev-section', default=None, help='ID da seção anterior para costura')
    parser.add_argument('--prefix', default='', help='Prefixo para arquivo de screenshot')
    parser.add_argument('--full-matrix', action='store_true', help='Capturar todos os viewports: 390, 768, 1024, 1440, 1920, 2560')
    parser.add_argument('--vps', default='', help='Lista separada por virgula de viewports (ex: 1440,1920,2560,390)')
    args = parser.parse_args()

    if args.full_matrix:
        vps = [
            VIEWPORT_PRESETS['390'],
            VIEWPORT_PRESETS['768'],
            VIEWPORT_PRESETS['1024'],
            VIEWPORT_PRESETS['1440'],
            VIEWPORT_PRESETS['1920'],
            VIEWPORT_PRESETS['2560']
        ]
    elif args.vps:
        vps = [VIEWPORT_PRESETS[k.strip()] for k in args.vps.split(',') if k.strip() in VIEWPORT_PRESETS]
    else:
        vps = [
            VIEWPORT_PRESETS['1440'],
            VIEWPORT_PRESETS['1920'],
            VIEWPORT_PRESETS['2560'],
            VIEWPORT_PRESETS['390']
        ]

    run_screenshot(args.section, args.prev_section, vps, prefix=args.prefix)
