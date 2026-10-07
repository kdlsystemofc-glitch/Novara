import os
import sys
import json
import re
from pathlib import Path

def apply_config():
    config_path = Path("site.config.json")
    if not config_path.exists():
        print("Erro: site.config.json não encontrado!")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    site_dir = Path("site")
    index_path = site_dir / "index.html"
    robots_path = site_dir / "robots.txt"
    sitemap_path = site_dir / "sitemap.xml"

    domain = config.get("production", {}).get("domain", "").strip().rstrip("/")
    site_url = config.get("production", {}).get("siteUrl", "").strip().rstrip("/")
    if domain and not site_url:
        site_url = f"https://{domain}"

    business = config.get("business", {})
    pending = config.get("pendingClientData", {})

    print(f"Lendo site.config.json...")
    print(f"  - Domínio configurado: '{domain or 'Nenhum (modo placeholder ativo)'}'")
    print(f"  - Site URL: '{site_url or 'Nenhum'}'")

    # 1. Atualizar sitemap.xml
    if sitemap_path.exists():
        sitemap_content = sitemap_path.read_text(encoding="utf-8")
        if site_url:
            sitemap_content = re.sub(
                r"<!--\s*<loc>https://DOMINIO_DEFINITIVO/</loc>\s*-->",
                f"<loc>{site_url}/</loc>",
                sitemap_content
            )
            sitemap_content = re.sub(
                r"<loc>https?://[^<]+</loc>",
                f"<loc>{site_url}/</loc>",
                sitemap_content
            )
            print("  [sitemap.xml] URL canônica atualizada com sucesso.")
        sitemap_path.write_text(sitemap_content, encoding="utf-8")

    # 2. Atualizar robots.txt
    if robots_path.exists():
        robots_content = robots_path.read_text(encoding="utf-8")
        if site_url:
            robots_content = re.sub(
                r"#\s*Sitemap:\s*https://DOMINIO_DEFINITIVO/sitemap\.xml",
                f"Sitemap: {site_url}/sitemap.xml",
                robots_content
            )
            robots_content = re.sub(
                r"Sitemap:\s*https?://\S+",
                f"Sitemap: {site_url}/sitemap.xml",
                robots_content
            )
            print("  [robots.txt] Diretiva de Sitemap atualizada com sucesso.")
        robots_path.write_text(robots_content, encoding="utf-8")

    # 3. Atualizar site/index.html
    if index_path.exists():
        html = index_path.read_text(encoding="utf-8")

        # Canonical tag
        if site_url:
            # Descomentar canonical se estiver comentado
            canonical_pattern = r"<!--\s*<link rel=\"canonical\" href=\"[^\"]*\">\s*-->"
            if re.search(canonical_pattern, html):
                html = re.sub(canonical_pattern, f'<link rel="canonical" href="{site_url}/">', html)
            else:
                html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{site_url}/">', html)

            # Open Graph & Twitter absolute URLs
            og_url_pattern = r'<!--\s*<meta property="og:url" content="[^"]*">\s*-->'
            if re.search(og_url_pattern, html):
                html = re.sub(og_url_pattern, f'<meta property="og:url" content="{site_url}/">', html)
            else:
                html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{site_url}/">', html)

            og_img_pattern = r'<!--\s*<meta property="og:image" content="[^"]*">\s*-->'
            if re.search(og_img_pattern, html):
                html = re.sub(og_img_pattern, f'<meta property="og:image" content="{site_url}/assets/og-image.jpg">', html)
            else:
                html = re.sub(r'<meta property="og:image" content="https?://[^"]*">', f'<meta property="og:image" content="{site_url}/assets/og-image.jpg">', html)

            tw_img_pattern = r'<!--\s*<meta name="twitter:image" content="[^"]*">\s*-->'
            if re.search(tw_img_pattern, html):
                html = re.sub(tw_img_pattern, f'<meta name="twitter:image" content="{site_url}/assets/og-image.jpg">', html)
            else:
                html = re.sub(r'<meta name="twitter:image" content="https?://[^"]*">', f'<meta name="twitter:image" content="{site_url}/assets/og-image.jpg">', html)

            print("  [index.html] Canonical e Open Graph URLs atualizados com sucesso.")

        # WhatsApp se configurado
        whatsapp_val = pending.get("whatsapp", {}).get("value", "").strip()
        if whatsapp_val:
            wa_clean = re.sub(r"\D", "", whatsapp_val)
            wa_url = f"https://wa.me/{wa_clean}"
            # Substitui links de reserva se apropriado
            print(f"  [index.html] WhatsApp configurado: {wa_url}")

        # JSON-LD Schema.org Restaurant
        schema_data = {
            "@context": "https://schema.org",
            "@type": "Restaurant",
            "name": business.get("name", "Novara Pizzas e Esfihas"),
            "legalName": business.get("legalName", "Novara Pizzas e Esfihas"),
            "alternateName": business.get("tradeName", "Novara Pizzas e Esfihas - I"),
            "description": business.get("description", ""),
            "telephone": business.get("telephone", "+55-11-4109-0313"),
            "address": {
                "@type": "PostalAddress",
                "streetAddress": business.get("address", {}).get("streetAddress", "R. Wadia Jafete Assad, 441"),
                "addressLocality": business.get("address", {}).get("addressLocality", "São Bernardo do Campo"),
                "addressRegion": business.get("address", {}).get("addressRegion", "SP"),
                "postalCode": business.get("address", {}).get("postalCode", "09850-090"),
                "addressCountry": business.get("address", {}).get("addressCountry", "BR")
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": business.get("geo", {}).get("latitude", -23.7166),
                "longitude": business.get("geo", {}).get("longitude", -46.5500)
            },
            "servesCuisine": business.get("cuisine", ["Pizza", "Esfiha", "Italiana"]),
            "menu": business.get("menuUrl", "https://novara-cafefilho.wabiz.delivery"),
            "potentialAction": {
                "@type": "OrderAction",
                "target": {
                    "@type": "EntryPoint",
                    "urlTemplate": business.get("menuUrl", "https://novara-cafefilho.wabiz.delivery"),
                    "actionPlatform": [
                        "http://schema.org/DesktopWebPlatform",
                        "http://schema.org/MobileWebPlatform"
                    ]
                },
                "deliveryMethod": [
                    "http://purl.org/goodrelations/v1#DeliveryModeOwnFleet"
                ]
            }
        }

        if site_url:
            schema_data["url"] = f"{site_url}/"

        price_val = pending.get("priceRange", {}).get("value", "").strip()
        if price_val:
            schema_data["priceRange"] = price_val

        hours_specs = pending.get("openingHours", {}).get("specification", [])
        valid_specs = [s for s in hours_specs if s.get("opens") and s.get("closes")]
        if valid_specs:
            schema_data["openingHoursSpecification"] = []
            for sp in valid_specs:
                schema_data["openingHoursSpecification"].append({
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": sp["dayOfWeek"],
                    "opens": sp["opens"],
                    "closes": sp["closes"]
                })

        social_links = []
        for soc_key in ["instagram", "facebook", "tiktok"]:
            soc_url = pending.get("social", {}).get(soc_key, "").strip()
            if soc_url:
                social_links.append(soc_url)
        if social_links:
            schema_data["sameAs"] = social_links

        # Injetar no HTML
        new_json_ld = json.dumps(schema_data, indent=2, ensure_ascii=False)
        html = re.sub(
            r'<script type="application/ld\+json">[\s\S]*?</script>',
            f'<script type="application/ld+json">\n{new_json_ld}\n  </script>',
            html
        )
        index_path.write_text(html, encoding="utf-8")
        print("  [index.html] Schema.org JSON-LD sincronizado com site.config.json.")

    print("\nReconstrução concluída com sucesso!")

if __name__ == "__main__":
    apply_config()
