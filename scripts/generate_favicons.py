import os
from PIL import Image

ASSETS_DIR = "site/assets"
SEAL_SRC = "site/assets/wax-seal-320.webp"

def generate_icons():
    if not os.path.exists(SEAL_SRC):
        print(f"Erro: {SEAL_SRC} não encontrado.")
        return

    seal = Image.open(SEAL_SRC).convert("RGBA")
    
    sizes = [
        (180, "site/apple-touch-icon.png"),
        (192, os.path.join(ASSETS_DIR, "icon-192.png")),
        (512, os.path.join(ASSETS_DIR, "icon-512.png")),
        (96, os.path.join(ASSETS_DIR, "favicon-96x96.png")),
    ]

    for size, out_path in sizes:
        # Create square canvas with brand background #F5EFEB
        canvas = Image.new("RGBA", (size, size), "#F5EFEB")
        # Scale seal to occupy ~80% of canvas
        seal_size = int(size * 0.82)
        seal_resized = seal.resize((seal_size, seal_size), Image.Resampling.LANCZOS)
        # Center seal
        offset = (size - seal_size) // 2
        canvas.paste(seal_resized, (offset, offset), seal_resized)
        
        # Save as PNG
        canvas.save(out_path, "PNG", optimize=True)
        print(f"  - {out_path} ({size}x{size}): {os.path.getsize(out_path)/1024:.1f} KB")

if __name__ == "__main__":
    generate_icons()
