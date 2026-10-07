import os
from PIL import Image

ASSETS_DIR = os.path.abspath("site/assets")

def resize_and_save(src_name, target_name, max_w, max_h=None, quality=85):
    src_path = os.path.join(ASSETS_DIR, src_name)
    target_path = os.path.join(ASSETS_DIR, target_name)
    if not os.path.exists(src_path):
        print(f"File not found: {src_path}")
        return

    with Image.open(src_path) as im:
        w, h = im.size
        if max_h:
            ratio = min(max_w / w, max_h / h)
        else:
            ratio = max_w / w

        if ratio >= 1:
            # Não ampliar
            new_w, new_h = w, h
        else:
            new_w, new_h = int(w * ratio), int(h * ratio)

        resized = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
        resized.save(target_path, "WEBP", quality=quality, method=6)
        print(f"Generated {target_name}: {new_w}x{new_h} ({os.path.getsize(target_path) / 1024:.1f} KB)")

# Miniaturas
resize_and_save("wax-seal-800.webp", "wax-seal-160.webp", 160)
resize_and_save("wax-seal-800.webp", "wax-seal-320.webp", 320)
resize_and_save("push-button-3d-800.webp", "push-button-3d-160.webp", 160)
resize_and_save("push-button-3d-800.webp", "push-button-3d-320.webp", 320)

# Degraus mobile (400px) para fotos principais
resize_and_save("dough-fermentation-800.webp", "dough-fermentation-400.webp", 480)
resize_and_save("raw-ingredients-800.webp", "raw-ingredients-400.webp", 480)
resize_and_save("wood-fired-oven-800.webp", "wood-fired-oven-400.webp", 480)
resize_and_save("wine-napkin-800.webp", "wine-napkin-400.webp", 480)
resize_and_save("cheese-ribbon-800.webp", "cheese-ribbon-400.webp", 180)
