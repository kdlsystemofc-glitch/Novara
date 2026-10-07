import os
from pathlib import Path
from playwright.sync_api import sync_playwright

def audit():
    file_url = Path('site/index.html').resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for w in [1440, 390]:
            page = browser.new_page(viewport={'width': w, 'height': 900})
            page.goto(file_url, wait_until='networkidle')
            
            total_h = page.evaluate('document.documentElement.scrollHeight')
            print(f"=== VIEWPORT {w}px (Total Height: {total_h:.1f}px) ===")
            
            sections = ['hero-crust-alchemy', 'materia-prima-pura', 'forno-e-tempo', 'table-reservations']
            for s in sections:
                box = page.query_selector(f'#{s}').bounding_box()
                print(f"Section #{s}: y={box['y']:.1f}, h={box['height']:.1f} ({box['height']/total_h*100:.1f}%)")
            
            # Key images
            elements = [
                ('Dough Card', '.dough-card'),
                ('Polaroid Card', '.polaroid-wrapper'),
                ('Oven Card', '.oven-card-wrap'),
                ('Wine Napkin Card', '.wine-napkin-card'),
                ('Cheese Ribbon', '.cheese-pull-spine')
            ]
            print("\nImage Elements:")
            for name, sel in elements:
                el = page.query_selector(sel)
                if el:
                    box = el.bounding_box()
                    print(f"  {name}: x={box['x']:.1f}, y={box['y']:.1f}, w={box['width']:.1f}px ({box['width']/w*100:.1f}% of screen), h={box['height']:.1f}px")
            print("\n" + "="*50 + "\n")
            page.close()
        browser.close()

if __name__ == '__main__':
    audit()
