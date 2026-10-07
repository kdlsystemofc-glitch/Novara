import os

INDEX_PATH = "site/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Target the head opening down to <style id="critical-css">
target_top = """<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Novara Pizzas e Esfihas — Forneria Artesanal</title>
  
  <meta name="description" content="Novara Pizzas e Esfihas — Forneria artesanal em São Bernardo do Campo com massas de fermentação lenta 48h, forno a lenha e ingredientes nobres selecionados.">

  <!-- Favicons -->
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="alternate icon" href="favicon.ico">

  <!-- Preload de Fontes Críticas da Dobra (WOFF2 local) -->
  <link rel="preload" href="fonts/playfair-display-900-normal-28189.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/oswald-700-normal-54494.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/plus-jakarta-sans-700-normal-33572.woff2" as="font" type="font/woff2" crossorigin>

  <!-- Preload da Imagem LCP Candidata Acima da Dobra (Fio de Queijo Spine) -->
  <link rel="preload" as="image" href="assets/cheese-ribbon-800.webp" fetchpriority="high">"""

replacement_top = """<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Primário & Metadados Específicos (Dados Reais do CLIENTE.md) -->
  <title>Novara Pizzas e Esfihas — Forneria &amp; Pizzaria em São Bernardo do Campo</title>
  <meta name="description" content="Forneria e pizzaria artesanal no bairro Dos Casa, São Bernardo do Campo. Pizzas tradicionais e especiais, massas de fermentação lenta 48h, forno a lenha e esfihas artesanais. Peça pelo delivery ou retire no balcão.">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#F5EFEB">

  <!-- URL Canônica: tag dependente de domínio configurado em seo.config.json (ativar quando o domínio definitivo existir): -->
  <!-- <link rel="canonical" href="https://[DOMINIO_DEFINITIVO]/"> -->

  <!-- Open Graph / Redes Sociais (Tags com URLs absolutas comentadas até configuração de seo.config.json) -->
  <meta property="og:locale" content="pt_BR">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Novara Pizzas e Esfihas">
  <meta property="og:title" content="Novara Pizzas e Esfihas — Forneria &amp; Pizzaria em São Bernardo do Campo">
  <meta property="og:description" content="Forneria e pizzaria artesanal no bairro Dos Casa, São Bernardo do Campo. Massas de fermentação lenta 48h, forno a lenha e esfihas artesanais. Delivery e salão.">
  <!-- <meta property="og:url" content="https://[DOMINIO_DEFINITIVO]/"> -->
  <!-- <meta property="og:image" content="https://[DOMINIO_DEFINITIVO]/assets/og-image.jpg"> -->
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Novara Pizzas e Esfihas — Forneria Artesanal em São Bernardo do Campo">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Novara Pizzas e Esfihas — Forneria &amp; Pizzaria em São Bernardo do Campo">
  <meta name="twitter:description" content="Forneria e pizzaria artesanal no bairro Dos Casa, São Bernardo do Campo. Massas de fermentação lenta 48h, forno a lenha e esfihas artesanais.">
  <!-- <meta name="twitter:image" content="https://[DOMINIO_DEFINITIVO]/assets/og-image.jpg"> -->

  <!-- Favicons, Ícones PWA e Webmanifest -->
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="alternate icon" href="favicon.ico">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">

  <!-- Preload de Fontes Críticas da Dobra (WOFF2 local) -->
  <link rel="preload" href="fonts/playfair-display-900-normal-28189.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/oswald-700-normal-54494.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/plus-jakarta-sans-700-normal-33572.woff2" as="font" type="font/woff2" crossorigin>

  <!-- Preload da Imagem LCP Candidata Acima da Dobra (Fio de Queijo Spine) -->
  <link rel="preload" as="image" href="assets/cheese-ribbon-800.webp" fetchpriority="high">"""

if target_top in html:
    html = html.replace(target_top, replacement_top)
    print("SEO Top block updated.")
else:
    print("Warning: target_top not matched!")

# Target right after <noscript><link rel="stylesheet" href="style.min.css"></noscript>
target_jsonld = """  <!-- CSS Completo Assíncrono Não-Bloqueante -->
  <link rel="preload" as="style" href="style.min.css" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="style.min.css"></noscript>
</head>"""

replacement_jsonld = """  <!-- CSS Completo Assíncrono Não-Bloqueante -->
  <link rel="preload" as="style" href="style.min.css" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="style.min.css"></noscript>

  <!--
    ==============================================================================
    AUDITORIA SCHEMA.ORG / DADOS INCERTOS MANTIDOS COMENTADOS:
    Conforme as diretrizes estritas do Google Search Central e Schema.org:
    1. priceRange: "R$ 20–120" informado por terceiros no Google Maps (121 pessoas),
       não confirmado como definitivo pelo cardápio oficial da forneria.
       Ativar quando validado: "priceRange": "R$ 20-120"
    2. openingHoursSpecification: "Abre às 18:00" confirmado, mas horários de
       fechamento específicos por dia da semana não estão discriminados no CLIENTE.md.
       Ativar quando a grade completa for confirmada.
    3. aggregateRating: As 895 avaliações (4.5★) são do Google Maps (plataforma de terceiros).
       As diretrizes do Google Search Central proíbem expressamente publicar aggregateRating
       no próprio site com notas de terceiros para empresas locais (self-serving reviews).
    ==============================================================================
  -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Restaurant",
    "@id": "https://[DOMINIO_DEFINITIVO]/#restaurant",
    "name": "Novara Pizzas e Esfihas",
    "legalName": "Novara Pizzas e Esfihas",
    "description": "Forneria popular de entregas e retiradas com pizzas diversas e esfihas de sabores tradicionais e especiais, massas com fermentação lenta de 48h e forno a lenha.",
    "telephone": "+55-11-4109-0313",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "R. Wadia Jafete Assad, 441",
      "addressLocality": "São Bernardo do Campo",
      "addressRegion": "SP",
      "postalCode": "09850-090",
      "addressCountry": "BR"
    },
    "servesCuisine": [
      "Pizza",
      "Esfiha",
      "Italiana"
    ],
    "hasMenu": "https://novara-cafefilho.wabiz.delivery",
    "acceptsReservations": true,
    "potentialAction": {
      "@type": "OrderAction",
      "target": {
        "@type": "EntryPoint",
        "urlTemplate": "https://novara-cafefilho.wabiz.delivery",
        "inLanguage": "pt-BR",
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
  </script>
</head>"""

if target_jsonld in html:
    html = html.replace(target_jsonld, replacement_jsonld)
    print("JSON-LD block inserted.")
else:
    print("Warning: target_jsonld not matched!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("SEO metadata applied to site/index.html successfully!")
