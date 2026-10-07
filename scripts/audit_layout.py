import os
from pathlib import Path
from playwright.sync_api import sync_playwright

def audit():
    file_url = Path('site/index.html').resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for w in [390, 768, 1024, 1440, 1920, 2560]:
            page = browser.new_page(viewport={'width': w, 'height': 900})
            page.goto(file_url, wait_until='networkidle')
            
            scroll_w = page.evaluate('document.documentElement.scrollWidth')
            client_w = page.evaluate('document.documentElement.clientWidth')
            has_h_overflow = scroll_w > client_w
            
            title_box = page.query_selector('.brand-hero-title').bounding_box()
            cheese_box = page.query_selector('.cheese-pull-spine').bounding_box()
            container_box = page.query_selector('.editorial-container').bounding_box()
            
            print(f"Viewport {w}px:")
            print(f"  Overflow: {has_h_overflow} (client={client_w}, scroll={scroll_w})")
            print(f"  Container width: {container_box['width']:.1f}px (left margin: {container_box['x']:.1f}px)")
            print(f"  Title width: {title_box['width']:.1f}px, height: {title_box['height']:.1f}px")
            print(f"  Cheese pull: width={cheese_box['width']:.1f}px, x={cheese_box['x']:.1f}px (center offset: {(cheese_box['x'] + cheese_box['width']/2) - w/2:.1f}px)")
            print()
            page.close()
        browser.close()

if __name__ == '__main__':
    audit()
