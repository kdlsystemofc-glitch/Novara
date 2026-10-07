import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_JPG = "site/assets/og-image.jpg"
OUTPUT_WEBP = "site/assets/og-image.webp"

def create_og_image():
    W, H = 1200, 630
    
    # 1. Base Paper Canvas #F5EFEB
    canvas = Image.new("RGB", (W, H), "#F5EFEB")
    draw = ImageDraw.Draw(canvas)
    
    # Subtle dot pattern
    dot_color = (20, 20, 20, 15)
    for x in range(0, W, 24):
        for y in range(0, H, 24):
            draw.point((x, y), fill="#E6DDD7")

    # 2. Add hero imagery on the right side (600px width)
    # Use real-pizza-volcano or wood-fired-oven
    photo_path = "site/assets/wood-fired-oven-1600.webp"
    if not os.path.exists(photo_path):
        photo_path = "site/assets/wood-fired-oven-800.webp"
        
    if os.path.exists(photo_path):
        photo = Image.open(photo_path).convert("RGBA")
        # Crop & resize to fit right half: 560x530 with rounded corners and shadow
        pw, ph = 560, 510
        # Resize preserving aspect ratio
        p_ratio = max(pw / photo.width, ph / photo.height)
        photo_resized = photo.resize((int(photo.width * p_ratio), int(photo.height * p_ratio)), Image.Resampling.LANCZOS)
        # Center crop
        left = (photo_resized.width - pw) // 2
        top = (photo_resized.height - ph) // 2
        photo_cropped = photo_resized.crop((left, top, left + pw, top + ph))
        
        # Create mask with rounded corners (16px)
        mask = Image.new("L", (pw, ph), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle([(0, 0), (pw, ph)], radius=16, fill=255)
        
        # Shadow
        shadow = Image.new("RGBA", (pw + 40, ph + 40), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.rounded_rectangle([(16, 20), (pw + 16, ph + 20)], radius=16, fill=(0, 0, 0, 70))
        shadow = shadow.filter(ImageFilter.GaussianBlur(16))
        
        # Paste shadow & photo on right side
        pos_x = 580
        pos_y = 60
        canvas.paste(shadow, (pos_x - 16, pos_y - 16), shadow)
        canvas.paste(photo_cropped, (pos_x, pos_y), mask)

    # 3. Add wax seal badge overlapping the corner
    seal_path = "site/assets/wax-seal-320.webp"
    if os.path.exists(seal_path):
        seal = Image.open(seal_path).convert("RGBA")
        seal = seal.resize((100, 100), Image.Resampling.LANCZOS)
        canvas.paste(seal, (530, 480), seal)

    # 4. Typography & Branding on the Left Side
    # Attempt to load system fonts or bundled TTF
    try:
        font_tag = ImageFont.truetype("arialbd.ttf", 22)
        font_title = ImageFont.truetype("georgiab.ttf", 82)
        font_sub = ImageFont.truetype("arialbd.ttf", 28)
        font_badges = ImageFont.truetype("arialbd.ttf", 20)
        font_meta = ImageFont.truetype("arial.ttf", 20)
    except Exception:
        font_tag = ImageFont.load_default()
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_badges = ImageFont.load_default()
        font_meta = ImageFont.load_default()

    # Category Tag with olive green
    draw.text((70, 75), "PIZZARIA & FORNERIA ARTESANAL", fill="#2E7D32", font=font_tag)
    
    # Monumental Brand Title
    draw.text((68, 120), "NOVARA", fill="#141414", font=font_title)
    
    # Location Subtitle
    draw.text((72, 230), "SÃO BERNARDO DO CAMPO", fill="#A62226", font=font_sub)
    
    # Thin divider rule
    draw.line([(72, 280), (510, 280)], fill="#D8CFCA", width=2)
    
    # Feature Pills / Badges
    badges = [
        "MASSAS FERMENTAÇÃO 48H",
        "FORNO A LENHA ARTESANAL",
        "ESFIHAS E PIZZAS NOBRES"
    ]
    cur_y = 310
    for b in badges:
        # Draw red bullet
        draw.ellipse([(72, cur_y + 4), (82, cur_y + 14)], fill="#D32F2F")
        draw.text((95, cur_y), b, fill="#2C2C2C", font=font_badges)
        cur_y += 38

    # Bottom Address and Phone
    draw.line([(72, 450), (510, 450)], fill="#D8CFCA", width=2)
    draw.text((72, 475), "R. Wadia Jafete Assad, 441 — Dos Casa", fill="#444444", font=font_meta)
    draw.text((72, 510), "Telefone: (11) 4109-0313 / (11) 4171-1234", fill="#141414", font=font_badges)
    draw.text((72, 545), "Delivery Online: novara-cafefilho.wabiz.delivery", fill="#2E7D32", font=font_meta)

    # Save JPG and WebP
    canvas.save(OUTPUT_JPG, "JPEG", quality=88, optimize=True)
    canvas.save(OUTPUT_WEBP, "WEBP", quality=85, method=6)
    
    print(f"OG Image gerada com sucesso:")
    print(f"  - {OUTPUT_JPG}: {os.path.getsize(OUTPUT_JPG) / 1024:.1f} KB (1200x630)")
    print(f"  - {OUTPUT_WEBP}: {os.path.getsize(OUTPUT_WEBP) / 1024:.1f} KB (1200x630)")

if __name__ == "__main__":
    create_og_image()
