import os
from PIL import Image

ASSETS_DIR = os.path.abspath("site/assets")
PLATES_DIR = os.path.abspath("design/plates")

def get_best_source(base_name):
    # Check if original PNG exists in design/plates
    plate_path = os.path.join(PLATES_DIR, f"{base_name}.png")
    if os.path.exists(plate_path):
        return plate_path
    # Otherwise check 1600.webp
    w1600 = os.path.join(ASSETS_DIR, f"{base_name}-1600.webp")
    if os.path.exists(w1600):
        return w1600
    # Otherwise 800.webp
    w800 = os.path.join(ASSETS_DIR, f"{base_name}-800.webp")
    if os.path.exists(w800):
        return w800
    return None

def optimize():
    print("Iniciando otimizacao e recompressao inteligente de imagens...")
    
    # 1. Cheese Ribbon
    plate_cheese = get_best_source("cheese-ribbon")
    if plate_cheese:
        im = Image.open(plate_cheese)
        w, h = im.size
        # Ratio is h/w ~ 3.0
        # Steps: 400h (w133), 800h (w267), 1200h (w400), 1600h (w533)
        targets = [
            (int(400 * w / h), 400, "cheese-ribbon-400.webp", 78),
            (int(800 * w / h), 800, "cheese-ribbon-800.webp", 78),
            (int(1200 * w / h), 1200, "cheese-ribbon-1200.webp", 78),
            (int(1600 * w / h), 1600, "cheese-ribbon-1600.webp", 78)
        ]
        for tw, th, fname, q in targets:
            resized = im.resize((tw, th), Image.Resampling.LANCZOS)
            out_path = os.path.join(ASSETS_DIR, fname)
            resized.save(out_path, "WEBP", quality=q, method=6)
            print(f"  - {fname}: {tw}x{th} -> {os.path.getsize(out_path)/1024:.1f} KB")

    # 2. Main content photos: dough-fermentation, raw-ingredients, wood-fired-oven, wine-napkin
    content_photos = ["dough-fermentation", "raw-ingredients", "wood-fired-oven", "wine-napkin"]
    for base in content_photos:
        src = get_best_source(base)
        if not src:
            continue
        im = Image.open(src)
        w, h = im.size
        ratio = h / w
        # Generate 400w, 600w, 800w, 1600w
        steps = [
            (400, int(400 * ratio), f"{base}-400.webp", 78),
            (600, int(600 * ratio), f"{base}-600.webp", 78),
            (800, int(800 * ratio), f"{base}-800.webp", 78),
            (1600, int(1600 * ratio), f"{base}-1600.webp", 78),
        ]
        for tw, th, fname, q in steps:
            # If resizing up, don't exceed source
            tw_final = min(tw, w)
            th_final = int(tw_final * ratio)
            resized = im.resize((tw_final, th_final), Image.Resampling.LANCZOS)
            out_path = os.path.join(ASSETS_DIR, fname)
            resized.save(out_path, "WEBP", quality=q, method=6)
            print(f"  - {fname}: {tw_final}x{th_final} -> {os.path.getsize(out_path)/1024:.1f} KB")

    # 3. Small badge assets: wax-seal, push-button-3d
    small_assets = [
        ("wax-seal", [(160, 160, "wax-seal-160.webp", 78), (320, 320, "wax-seal-320.webp", 78)]),
        ("push-button-3d", [(160, 120, "push-button-3d-160.webp", 78), (320, 240, "push-button-3d-320.webp", 78)])
    ]
    for base, steps in small_assets:
        src = get_best_source(base)
        if not src:
            continue
        im = Image.open(src)
        for tw, th, fname, q in steps:
            resized = im.resize((tw, th), Image.Resampling.LANCZOS)
            out_path = os.path.join(ASSETS_DIR, fname)
            resized.save(out_path, "WEBP", quality=q, method=6)
            print(f"  - {fname}: {tw}x{th} -> {os.path.getsize(out_path)/1024:.1f} KB")

    # Also optimize remaining 800 and 1600 images in site/assets
    for fname in os.listdir(ASSETS_DIR):
        if not fname.endswith(".webp") or fname.startswith("test-"):
            continue
        fpath = os.path.join(ASSETS_DIR, fname)
        size_kb = os.path.getsize(fpath) / 1024
        # If it's already one of our newly created ones, skip
        if any(f"{b}-" in fname for b in ["cheese-ribbon", "dough-fermentation", "raw-ingredients", "wood-fired-oven", "wine-napkin", "wax-seal", "push-button-3d"]):
            continue
        if size_kb > 100:
            im = Image.open(fpath)
            im.save(fpath, "WEBP", quality=78, method=6)
            print(f"  - Recompressed {fname}: {size_kb:.1f} KB -> {os.path.getsize(fpath)/1024:.1f} KB")

    # Remove temporary test file if exists
    test_path = os.path.join(ASSETS_DIR, "test-raw-800.webp")
    if os.path.exists(test_path):
        os.remove(test_path)

if __name__ == "__main__":
    optimize()
