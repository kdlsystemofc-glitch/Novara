# DEPLOY.md — Guia de Cabeçalhos e Diretrizes de Entrega de Produção

Este documento consolida as diretrizes de cache, compressão e segurança para qualquer infraestrutura de hospedagem ou CDN (ex.: Cloudflare, CloudFront, Vercel, Netlify, Nginx, Apache, Caddy), sem acoplamento a um provedor específico.

---

## 1. Estratégia de Cache HTTP (`Cache-Control`)

### A. Documento HTML Raiz (`/index.html`)
O arquivo HTML deve ser revalidado a cada requisição para garantir que qualquer atualização de conteúdo, metadados ou referências de scripts seja recebida imediatamente pelo visitante.
```http
Cache-Control: public, max-age=0, must-revalidate
ETag: W/"novara-v1.0"
```

### B. Fontes Tipográficas Locais (`/fonts/*.woff2`)
Arquivos WOFF2 são estáticos, pesados e imutáveis. Devem ser cacheados pelo navegador e na CDN pelo período máximo permitido (1 ano).
```http
Cache-Control: public, max-age=31536000, immutable
Access-Control-Allow-Origin: *
```

### C. Imagens e Ativos Gráficos (`/assets/*.webp`, `/favicon.svg`, `/favicon.ico`)
Imagens com nomes versionados ou estáticos de alta resolução e miniaturas responsivas:
```http
Cache-Control: public, max-age=31536000, immutable
```

### D. Folhas de Estilo e Scripts Minificados (`/style.min.css`, `/js/*.min.js`, `/js/vendor/*.min.js`)
Arquivos de estilo consolidado e scripts minificados:
```http
Cache-Control: public, max-age=31536000, immutable
```
> *Nota:* Caso o pipeline de CI/CD adicione hashes de conteúdo aos nomes dos arquivos (ex.: `style.[hash].min.css`), o cabeçalho `immutable` garante taxa de acerto de cache de 100% no navegador.

---

## 2. Compressão e Codificação de Conteúdo

Todos os arquivos de texto e vetores devem ser servidos prioritariamente com compressão **Brotli (`br`)**, com fallback automático para **Gzip**:
- Tipos MIME para compressão:
  - `text/html`
  - `text/css`
  - `application/javascript`
  - `image/svg+xml`
  - `application/json`
  - `font/woff2` (já possui compressão interna Brotli na especificação WOFF2; dispensar re-compressão pelo servidor web)

Níveis de compressão recomendados:
- **Brotli estático pré-comprimido:** Nível 11 (máxima taxa de compressão em build time).
- **Brotli dinâmico on-the-fly:** Nível 4 ou 5 (equilíbrio ideal entre latência de CPU e tamanho).
- **Gzip dinâmico:** Nível 6.

---

## 3. Cabeçalhos de Segurança Recomendados

```http
# Prevenção de MIME-sniffing
X-Content-Type-Options: nosniff

# Proteção contra framing / clickjacking
X-Frame-Options: SAMEORIGIN

# Controle de política de referência
Referrer-Policy: strict-origin-when-cross-origin

# Isolamento e permissões do navegador
Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()

# Forçamento de HTTPS estrito (HSTS)
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

### Content Security Policy (CSP) Recomendado:
Para o site Novara sem dependências externas de CDN:
```http
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'self';
```

---

## 4. Otimizações de Rede e Protocolo

1. **HTTP/2 ou HTTP/3 (QUIC):**
   - Essencial para multiplexação paralela de conexões sem bloqueio Head-of-Line (HOL).
   - O carregamento assíncrono do `style.min.css` e o preload das 3 fontes WOFF2 críticas e da imagem LCP beneficiam-se diretamente do stream HTTP/2+.

2. **Early Hints (Status Code 103):**
   - Se o servidor de borda/CDN suportar RFC 8297, enviar cabeçalhos 103 Early Hints antes do corpo do HTML:
   ```http
   Link: </fonts/playfair-display-900-normal-28189.woff2>; rel=preload; as=font; type=font/woff2; crossorigin
   Link: </fonts/oswald-700-normal-54494.woff2>; rel=preload; as=font; type=font/woff2; crossorigin
   Link: </fonts/plus-jakarta-sans-700-normal-33572.woff2>; rel=preload; as=font; type=font/woff2; crossorigin
   Link: </assets/dough-fermentation-400.webp>; rel=preload; as=image; fetchpriority=high
   Link: </style.min.css>; rel=preload; as=style
   ```

3. **Fallback local e file://:**
   - O projeto mantém caminhos relativos em todos os recursos, garantindo total compatibilidade para visualização direta via `file://` sem requisições CORS externas.
