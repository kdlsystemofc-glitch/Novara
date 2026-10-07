import os
from fontTools import subset

FONTS_DIR = os.path.abspath("site/fonts")

# Comprehensive text coverage: all printable ASCII, numbers, punctuation,
# and all Portuguese accented characters, arrows, stars, etc.
CHARACTERS = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "áàâãéèêíïóôõöúüçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÜÇÑ"
    " .,;:!?'\"-–—/()[]{}<>«»★➔//%&+=*@#$"
)

def subset_all():
    options = subset.Options()
    options.flavor = "woff2"
    
    total_orig = 0
    total_sub = 0

    for fname in os.listdir(FONTS_DIR):
        if not fname.endswith(".woff2"):
            continue
        fpath = os.path.join(FONTS_DIR, fname)
        orig_size = os.path.getsize(fpath)
        total_orig += orig_size

        try:
            font = subset.load_font(fpath, options)
            subsetter = subset.Subsetter(options=options)
            subsetter.populate(text=CHARACTERS)
            subsetter.subset(font)
            subset.save_font(font, fpath, options)
            new_size = os.path.getsize(fpath)
            total_sub += new_size
            print(f"  - {fname}: {orig_size/1024:.1f} KB -> {new_size/1024:.1f} KB (saved {(orig_size-new_size)/1024:.1f} KB)")
        except Exception as e:
            print(f"  - Erro em {fname}: {e}")
            total_sub += orig_size

    print(f"\nEconomia total em fontes: {total_orig/1024:.1f} KB -> {total_sub/1024:.1f} KB (Redução de {(total_orig-total_sub)/1024:.1f} KB)")

if __name__ == "__main__":
    subset_all()
