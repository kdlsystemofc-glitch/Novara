import os
import re
import urllib.request

FONTS_DIR = os.path.abspath("site/fonts")
os.makedirs(FONTS_DIR, exist_ok=True)

# Google Fonts URL para os pesos necessários com subset latin
url = "https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Oswald:wght@600;700&family=Playfair+Display:ital,wght@0,900;1,700&family=Plus+Jakarta+Sans:wght@700;800&display=swap"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    css_content = resp.read().decode("utf-8")

# Parse @font-face blocks
# Apenas latin e latin-ext para manter o bundle ultra leve
blocks = re.findall(r"(/\* (?:latin|latin-ext) \*/\s*@font-face\s*\{[^}]+\})", css_content)

font_files = {}
local_css_rules = []

for block in blocks:
    # Extract font-family, weight, style, url
    family_match = re.search(r"font-family:\s*'([^']+)'", block)
    weight_match = re.search(r"font-weight:\s*(\d+)", block)
    style_match = re.search(r"font-style:\s*(\w+)", block)
    url_match = re.search(r"src:\s*url\((https://[^)]+\.woff2)\)", block)
    unicode_match = re.search(r"unicode-range:\s*([^;]+);", block)

    if family_match and weight_match and style_match and url_match:
        family = family_match.group(1)
        weight = weight_match.group(1)
        style = style_match.group(1)
        font_url = url_match.group(1)
        unicode_range = unicode_match.group(1) if unicode_match else "U+0000-00FF"

        # Safe filename
        safe_name = f"{family.lower().replace(' ', '-')}-{weight}-{style}-{hash(font_url) & 0xffff}.woff2"
        file_path = os.path.join(FONTS_DIR, safe_name)

        if not os.path.exists(file_path):
            print(f"Downloading {safe_name} from {font_url}...")
            font_req = urllib.request.Request(font_url, headers=headers)
            with urllib.request.urlopen(font_req) as f_resp:
                with open(file_path, "wb") as out:
                    out.write(f_resp.read())

        local_rule = f"""@font-face {{
  font-family: '{family}';
  font-style: {style};
  font-weight: {weight};
  font-display: swap;
  src: url('fonts/{safe_name}') format('woff2');
  unicode-range: {unicode_range};
}}"""
        local_css_rules.append(local_rule)

fonts_css_path = os.path.abspath("site/fonts.css")
with open(fonts_css_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(local_css_rules) + "\n")

print(f"Fontes salvas em {FONTS_DIR} e {fonts_css_path}")
