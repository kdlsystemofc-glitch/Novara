# PENDÊNCIAS DO CLIENTE — NOVARA PIZZAS E ESFIHAS

Este documento consolida com precisão tudo o que ainda depende de dados ou ativos fornecidos pela diretoria da **Novara Pizzas e Esfihas**, acompanhado do impacto técnico e mercadológico de cada resolução.

Toda a infraestrutura do site foi construída em arquitetura desacoplada: **o site já funciona perfeitamente sem esses dados**, operando com fallbacks seguros e placeholders documentados. Ao receber os dados do cliente, basta atualizar o arquivo [**`site.config.json`**](file:///c:/Oficial/Novara%203/site.config.json) e rodar o script de reconstrução automática.

---

## 1. Tabela Resumo de Pendências e Impactos

| Prioridade | Item Pendente | Dado Atual (Fallback) | O Que Falta do Cliente | Impacto Quando Resolvido |
| :---: | :--- | :--- | :--- | :--- |
| **Alta** | **Domínio Oficial e SSL** | URLs relativas locais | Endereço do domínio registrado (ex: `novarapizzas.com.br`) | Ativa `canonical` em todas as páginas, sitemap no Google Search Console e prévia rica com imagem no WhatsApp/Instagram/Twitter. |
| **Alta** | **Horários de Fechamento** | Abre às 18:00 (confirmado) | Horário exato de encerramento de cada dia (ex: 23:30 ou 00:00) | Google exibe o selo em tempo real **"Aberto agora"** / **"Fecha às 23:30"** na busca local e no Maps. |
| **Alta** | **WhatsApp de Atendimento** | Telefones fixos (11) 4109-0313 e 4171-1234 | Número de WhatsApp com DDD (se houver atendimento direto) | Converte o botão de reservas e contato em link direto 1-clique (`wa.me`) para conversa imediata. |
| **Média** | **Fotos Reais dos Pratos** | Fotos recriadas por IA idênticas à referência | Fotos de alta resolução da bancada, forno em chamas e pratos reais | Elimina risco de divergência visual com o cliente e garante autenticidade jurídica para campanhas. |
| **Média** | **Faixa de Preço / Ticket Médio** | Comentada no código (estimativa informal R$ 20–120) | Ticket médio oficial por pessoa (ex: `$$` ou `R$ 40–80`) | Habilita o rich snippet de preço oficial no Google (`priceRange`), qualificando o tráfego orgânico. |
| **Média** | **CNPJ da Unidade Dos Casa** | Omitido do rodapé | Número do CNPJ e Razão Social oficial | Cumprimento do Decreto Federal 7.962/2013 (Lei do E-commerce) para lojas virtuais e canais de delivery. |
| **Baixa** | **Perfis Sociais Oficiais** | Links neutros / Wabiz | URLs oficiais do Instagram e Facebook | Marcação `sameAs` no Schema.org unificando a entidade nos motores de IA e no Knowledge Graph do Google. |
| **Baixa** | **ID do Google Analytics 4 (GA4)** | Sem rastreamento externo | ID de métricas (ex: `G-XXXXXXXXXX`) | Monitoramento de volume de visitantes, tempo de sessão e taxa de cliques para o sistema Wabiz. |

---

## 2. Detalhamento de Cada Pendência

### 1. Domínio Oficial e Hospedagem
* **Situação Atual:** O site está preparado para qualquer hospedagem estática moderna (Cloudflare Pages, Vercel, Netlify, Apache, Nginx). As tags `<link rel="canonical">`, `<meta property="og:url">` e `sitemap.xml` estão documentadas em formato de placeholder comentado para evitar apontamentos para domínios inexistentes.
* **Efeito ao Resolver:** 
  - Robôs do Google indexam imediatamente o site através do [**`site/sitemap.xml`**](file:///c:/Oficial/Novara%203/site/sitemap.xml).
  - Links compartilhados no WhatsApp, Telegram, Facebook e Twitter passam a exibir automaticamente a imagem editorial de alta resolução ([`site/assets/og-image.jpg`](file:///c:/Oficial/Novara%203/site/assets/og-image.jpg)), o título e a descrição da forneria.

### 2. Grade de Horários de Funcionamento (Segunda a Domingo)
* **Situação Atual:** O dado real confirmado do Google Maps indica abertura diária às 18:00 (inclusive às segundas-feiras, testado por cliente). No entanto, os horários exatos de fechamento (especialmente sextas, sábados e domingos) não constam de forma inequívoca em `CLIENTE.md`.
* **Efeito ao Resolver:**
  - Inclusão do nó `OpeningHoursSpecification` no JSON-LD do Schema.org.
  - O robô do Google e do assistente Gemini passa a informar aos usuários que buscarem "pizzaria aberta agora em São Bernardo" que a Novara está em pleno funcionamento, aumentando os pedidos de impulso.

### 3. Canal WhatsApp Oficial
* **Situação Atual:** Os contatos cadastrados e ativos são os telefones fixos `(11) 4109-0313` e `(11) 4171-1234`, e o link de delivery direto na plataforma Wabiz (`https://novara-cafefilho.wabiz.delivery`).
* **Efeito ao Resolver:**
  - O cliente mobile ganha a opção de iniciar um chat imediato no WhatsApp com mensagem pré-preenchida (ex: *"Olá! Gostaria de consultar os sabores do dia e fazer uma reserva/pedido."*).

### 4. Fotografias Reais de Culinária
* **Situação Atual:** Conforme instrução e regra de governança (`CLAUDE.md`), as 4 fotografias principais foram recriadas por Inteligência Artificial mantendo 100% da fidelidade estética e proporções da referência aprovada.
* **Efeito ao Resolver:**
  - A troca das imagens em `site/assets/` pelas fotos autênticas dos ingredientes, fornos e massas da Novara garante segurança jurídica plena contra alegações de publicidade ilustrativa e fortalece a conexão emocional com os frequentadores do bairro Dos Casa.
  - Veja a lista dos arquivos a substituir na seção 3 abaixo.

### 5. Faixa de Preço / Ticket Médio Oficial
* **Situação Atual:** No Google Maps, 121 usuários votaram na faixa de R$ 20 a R$ 120 por pessoa. Para evitar penalidades do Google Search Central por dados inverídicos não oficiais, esse campo foi mantido fora do Schema.org até validação da administração.
* **Efeito ao Resolver:**
  - Publicação do símbolo de precificação correto nos resultados do Google, atraindo o perfil ideal de consumidor para a pizza artesanal de 48h.

### 6. CNPJ no Rodapé
* **Situação Atual:** O rodapé exibe os dados de endereço físico, telefones, copyright e link para o sistema Wabiz.
* **Efeito ao Resolver:**
  - Conformidade plena com a legislação de comércio eletrônico no Brasil (exigência de CNPJ visível no rodapé de sites que realizam pedidos/compras online).

---

## 3. Inventário de Imagens para Substituição Futura

Quando o cliente fornecer o acervo fotográfico real, basta salvar os arquivos nos seguintes caminhos de `site/assets/`:

1. **Massa Fermentando (48h):**
   - Arquivo: `site/assets/dough-fermentation-1600.webp`
   - Especificação: Foto de close-up da massa crua com bolhas de ar e farinha rústica sobre madeira.
2. **Matéria-Prima Pura (Ingredientes):**
   - Arquivo: `site/assets/raw-ingredients-1600.webp`
   - Especificação: Composição de tomates frescos, manjericão e fatias de queijo.
3. **Forno a Lenha:**
   - Arquivo: `site/assets/wood-fired-oven-1600.webp`
   - Especificação: Boca do forno refratário da Novara com chamas vivas e labaredas ao fundo.
4. **Taça de Vinho & Salão:**
   - Arquivo: `site/assets/wine-napkin-1600.webp`
   - Especificação: Mesa posta com taça de vinho tinto, guardanapo xadrez e fatias servidas.

---

## 4. Como Preencher e Reconstruir em 2 Passos

1. Abra o arquivo [**`site.config.json`**](file:///c:/Oficial/Novara%203/site.config.json) na raiz do projeto.
2. Preencha os campos recebidos do cliente (ex: `domain: "novarapizzas.com.br"`, horários, WhatsApp, etc.).
3. No terminal, execute:
   ```bash
   python scripts/apply_site_config.py
   ```
4. O script aplicará automaticamente todas as URLs, ativará as diretivas do `robots.txt`, sincronizará o `sitemap.xml`, atualizará o Schema.org JSON-LD e o HTML final.
