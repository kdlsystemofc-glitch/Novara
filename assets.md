# Inventário de Assets: Novara Pizzas e Esfihas

Todos os assets visuais utilizados no projeto estão hospedados localmente em `site/assets/` no formato WebP de alta performance, gerados a partir de imagens reais do cliente (`imagens/`) e plates gerados conforme a referência (`novara img/` e `design/plates/`).

---

## 1. Mapeamento de Slots, Arquivos e Degraus Responsivos

| Nome do Asset | Tipo | Origem | Degraus Disponíveis | Papel no Site | Status & Otimização |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `cheese-ribbon` | **PLATE GERADO** | `design/plates/cheese-ribbon.png` | `400.webp` (18 KB)<br>`800.webp` (45 KB)<br>`1200.webp` (86 KB)<br>`1600.webp` (153 KB) | Spine Central: Fio contínuo de mozzarella em curva "S" descendo pelo centro da página (LCP principal) | Pronto (canal alpha transparente, fetchpriority="high", preloaded) |
| `dough-fermentation` | **PLATE GERADO** | `novara img/Três bolas de massa sobre pedra-2.png` | `400.webp` (24 KB)<br>`600.webp` (50 KB)<br>`800.webp` (82 KB)<br>`1600.webp` (218 KB) | Bloco 1: Massa madre artesanal em fermentação sobre pedra com farinha | Pronto |
| `raw-ingredients` | **PLATE GERADO** | `novara img/Tomate, burrata, anchovas e manjericão-4.png` | `400.webp` (33 KB)<br>`600.webp` (64 KB)<br>`800.webp` (100 KB)<br>`1600.webp` (191 KB) | Bloco 2: Prancha polaroid com ingredientes puros (tomates, burrata, anchovas) | Pronto |
| `wood-fired-oven` | **PLATE GERADO** | `novara img/Forno a lenha em chamas-3.png` | `400.webp` (22 KB)<br>`600.webp` (42 KB)<br>`800.webp` (65 KB)<br>`1600.webp` (166 KB) | Bloco 3: Forno a lenha rústico em arco com lenha incandescente ardendo | Pronto |
| `wine-napkin` | **PLATE GERADO** | `novara img/Copo de vinho branco e guardanapo axadrezado-5.png` | `400.webp` (22 KB)<br>`600.webp` (39 KB)<br>`800.webp` (70 KB)<br>`1600.webp` (193 KB) | Bloco 4: Taça de vinho branco com guardanapo xadrez vichy verde | Pronto (canal alpha transparente) |
| `wax-seal` | **PLATE GERADO** | `novara img/Selo de cera bordô com relevo botânico-6.png` | `160.webp` (7.8 KB)<br>`320.webp` (21 KB)<br>`800.webp`<br>`1600.webp` | Selo de cera clássico com relevo para detalhes de scrapbook e hero | Pronto (canal alpha transparente) |
| `push-button-3d` | **PLATE GERADO** | `novara img/Botão de pressão vermelho brilhante-7.png` | `160.webp` (3.5 KB)<br>`320.webp` (8.1 KB)<br>`800.webp`<br>`1600.webp` | Botão 3D tátil tipo campainha vermelha brilhante (proporção 4:3 corrigida) | Pronto (canal alpha transparente) |
| `basil-sprig` | **PLATE GERADO** | `novara img/Raminho de manjericão fresco-8.png` | `800.webp`<br>`1600.webp` (154 KB) | Ramo de manjericão fresco para decoração flutuante | Pronto (canal alpha transparente) |
| `real-pizza-volcano` | **FOTO REAL** | `imagens/imgi_19_*.jpg` | `800.webp` (90 KB)<br>`1600.webp` (232 KB) | Pizza Novara com borda vulcão recheada, bacon crocante e queijo gratinado | Foto Real do Cliente |
| `real-cheese-pull` | **FOTO REAL** | `imagens/imgi_28_*.jpg` | `800.webp`<br>`1600.webp` (110 KB) | Fatia de pizza da Novara sendo erguida com fio real de queijo derretido | Foto Real do Cliente |
| `real-esfiha-open` | **FOTO REAL** | `imagens/imgi_17_*.jpg` | `800.webp`<br>`1600.webp` (126 KB) | Esfiha aberta artesanal de queijo com ervas servida no prato | Foto Real do Cliente |
| `real-sweet-pizza` | **FOTO REAL** | `imagens/imgi_18_*.jpg` | `800.webp` (73 KB)<br>`1600.webp` (197 KB) | Pizza doce de chocolate generosa na caixa delivery | Foto Real do Cliente |
| `real-balcony-table` | **FOTO REAL** | `imagens/imgi_31_*.jpg` | `800.webp`<br>`1600.webp` | Mesa servida na varanda da Novara com coquetel de morango e pizzas | Foto Real do Cliente |
| `real-facade-night` | **FOTO REAL** | `imagens/imgi_15_*.jpg` | `800.webp`<br>`1600.webp` | Fachada noturna ampla com letreiro iluminado da Novara | Foto Real do Cliente |
| `real-facade-neon` | **FOTO REAL** | `imagens/imgi_34_*.jpg` | `800.webp`<br>`1600.webp` (71 KB) | Detalhe em ângulo do letreiro de neon Novara | Foto Real do Cliente |
| `real-logo-novara` | **FOTO REAL** | `imagens/imgi_2_*.jpg` | `800.webp`<br>`1600.webp` | Logotipo oficial (150x150) | Foto Real do Cliente |

---

## 2. Notas de Governança
- **Nenhum arquivo em `/design` é referenciado no código do site:** Todos os caminhos de imagem apontam exclusivamente para `site/assets/*.webp`.
- **Economia de Payload Total:** Imagens reprocessadas em WebP Q68–Q78 economizaram mais de **1.2 MB** em relação às exportações brutas, com degraus de 160px para ícones e 400px/600px para celulares e tablets.
