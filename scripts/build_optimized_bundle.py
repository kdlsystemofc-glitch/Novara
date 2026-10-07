import os
import re

SITE_DIR = os.path.abspath("site")

def minify_css(css_text):
    # Remove comments
    css_text = re.sub(r"/\*[\s\S]*?\*/", "", css_text)
    # Remove extra whitespace
    css_text = re.sub(r"\s+", " ", css_text)
    # Remove space around punctuation
    css_text = re.sub(r"\s*([\{\};:,>])\s*", r"\1", css_text)
    # Remove trailing semicolon
    css_text = re.sub(r";\}", "}", css_text)
    return css_text.strip()

def minify_js(js_text):
    # Remove single line comments (but not inside quotes)
    lines = []
    for line in js_text.splitlines():
        line = re.sub(r"^\s*//.*$", "", line)
        lines.append(line)
    js_text = "\n".join(lines)
    # Remove multi-line comments
    js_text = re.sub(r"/\*[\s\S]*?\*/", "", js_text)
    # Collapse multiple blank lines
    js_text = re.sub(r"\n\s*\n", "\n", js_text)
    return js_text.strip()

def build():
    # 1. Juntar todos os CSS
    css_files = ["fonts.css", "tokens.css", "reset.css", "lenis.css", "style.css"]
    full_css = []
    for fname in css_files:
        fpath = os.path.join(SITE_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                full_css.append(f.read())

    combined_css = "\n".join(full_css)
    minified_css = minify_css(combined_css)

    min_css_path = os.path.join(SITE_DIR, "style.min.css")
    with open(min_css_path, "w", encoding="utf-8") as f:
        f.write(minified_css)

    print(f"CSS combinando {len(css_files)} arquivos:")
    print(f"  - Original: {len(combined_css) / 1024:.1f} KB")
    print(f"  - Minificado: {len(minified_css) / 1024:.1f} KB (Salvo em site/style.min.css)")

    # 2. Minificar motion.js
    motion_js_path = os.path.join(SITE_DIR, "js", "motion.js")
    with open(motion_js_path, "r", encoding="utf-8") as f:
        motion_code = f.read()

    minified_motion = minify_js(motion_code)
    min_motion_path = os.path.join(SITE_DIR, "js", "motion.min.js")
    with open(min_motion_path, "w", encoding="utf-8") as f:
        f.write(minified_motion)

    print(f"JavaScript próprio (motion.js):")
    print(f"  - Original: {len(motion_code) / 1024:.1f} KB")
    print(f"  - Minificado: {len(minified_motion) / 1024:.1f} KB (Salvo em site/js/motion.min.js)")

    # 3. Criar favicon SVG artesanal e favicon.ico para zerar erro 404
    favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <circle cx="16" cy="16" r="15" fill="#A62226" stroke="#DEA01B" stroke-width="2"/>
  <text x="16" y="22" font-family="serif" font-weight="bold" font-size="18" fill="#FFF8F0" text-anchor="middle">N</text>
</svg>'''
    with open(os.path.join(SITE_DIR, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(favicon_svg)
    with open(os.path.join(SITE_DIR, "favicon.ico"), "wb") as f:
        # Mini binary valid ico file
        f.write(b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00 \x00h\x00\x00\x00\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' + b'\x00' * 80)
    print("Favicon local criado em site/favicon.svg e site/favicon.ico")

if __name__ == "__main__":
    build()
