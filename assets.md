# Inventário de Assets: Novara Pizzas e Esfihas

Todos os assets visuais utilizados no projeto estão hospedados localmente em `site/assets/` no formato WebP de alta performance, gerados a partir de imagens reais do cliente (`imagens/`) e plates gerados conforme a referência (`novara img/` e `design/plates/`).

---

## 1. Mapeamento de Slots e Arquivos

| Nome do Asset | Tipo | Origem | Versão 800px | Versão 1600px | Papel no Site | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `cheese-ribbon` | **PLATE GERADO** | `novara img/Fatia margherita com fio de mozzarella-1.png` | `site/assets/cheese-ribbon-800.webp` | `site/assets/cheese-ribbon-1600.webp` | Fatia de pizza superior com fio contínuo de mozzarella em curva "S" descendo pelo centro da página | Pronto (canal alpha transparente) |
| `dough-fermentation` | **PLATE GERADO** | `novara img/Três bolas de massa sobre pedra-2.png` | `site/assets/dough-fermentation-800.webp` | `site/assets/dough-fermentation-1600.webp` | Bloco 1: Massa madre artesanal em fermentação sobre pedra com farinha | Pronto |
| `raw-ingredients` | **PLATE GERADO** | `novara img/Tomate, burrata, anchovas e manjericão-4.png` | `site/assets/raw-ingredients-800.webp` | `site/assets/raw-ingredients-1600.webp` | Bloco 2: Prancha polaroid com ingredientes puros (tomates, burrata, anchovas) | Pronto |
| `wood-fired-oven` | **PLATE GERADO** | `novara img/Forno a lenha em chamas-3.png` | `site/assets/wood-fired-oven-800.webp` | `site/assets/wood-fired-oven-1600.webp` | Bloco 3: Forno a lenha rústico em arco com lenha incandescente ardendo | Pronto |
| `wine-napkin` | **PLATE GERADO** | `novara img/Copo de vinho branco e guardanapo axadrezado-5.png` | `site/assets/wine-napkin-800.webp` | `site/assets/wine-napkin-1600.webp` | Bloco 4: Taça de vinho branco com guardanapo xadrez vichy verde | Pronto (canal alpha transparente) |
| `wax-seal` | **PLATE GERADO** | `novara img/Selo de cera bordô com relevo botânico-6.png` | `site/assets/wax-seal-800.webp` | `site/assets/wax-seal-1600.webp` | Selo de cera clássico com relevo para detalhes de scrapbook | Pronto (canal alpha transparente) |
| `push-button-3d` | **PLATE GERADO** | `novara img/Botão de pressão vermelho brilhante-7.png` | `site/assets/push-button-3d-800.webp` | `site/assets/push-button-3d-1600.webp` | Botão 3D tátil tipo campainha vermelha brilhante | Pronto (canal alpha transparente) |
| `basil-sprig` | **PLATE GERADO** | `novara img/Raminho de manjericão fresco-8.png` | `site/assets/basil-sprig-800.webp` | `site/assets/basil-sprig-1600.webp` | Ramo de manjericão fresco para decoração flutuante | Pronto (canal alpha transparente) |
| `real-pizza-volcano` | **FOTO REAL** | `imagens/imgi_19_805485575_18417622879157431_1435122697872442889_n.jpg` | `site/assets/real-pizza-volcano-800.webp` | `site/assets/real-pizza-volcano-1600.webp` | Pizza Novara com borda vulcão recheada, bacon crocante e queijo gratinado | Foto Real do Cliente |
| `real-cheese-pull` | **FOTO REAL** | `imagens/imgi_28_726270071_18404682256157431_5942686219652501334_n.jpg` | `site/assets/real-cheese-pull-800.webp` | `site/assets/real-cheese-pull-1600.webp` | Fatia de pizza da Novara sendo erguida com fio real de queijo derretido | Foto Real do Cliente |
| `real-esfiha-open` | **FOTO REAL** | `imagens/imgi_17_824815052_18419714503157431_6515126437674167090_n.jpg` | `site/assets/real-esfiha-open-800.webp` | `site/assets/real-esfiha-open-1600.webp` | Esfiha aberta artesanal de queijo com ervas servida no prato | Foto Real do Cliente |
| `real-sweet-pizza` | **FOTO REAL** | `imagens/imgi_18_813428838_18418544182157431_1850512890744409572_n.jpg` | `site/assets/real-sweet-pizza-800.webp` | `site/assets/real-sweet-pizza-1600.webp` | Pizza doce de chocolate generosa na caixa delivery | Foto Real do Cliente |
| `real-balcony-table` | **FOTO REAL** | `imagens/imgi_31_713983671_981539201330623_1659608048361987037_n.jpg` | `site/assets/real-balcony-table-800.webp` | `site/assets/real-balcony-table-1600.webp` | Mesa servida na varanda da Novara com coquetel de morango e pizzas | Foto Real do Cliente |
| `real-facade-night` | **FOTO REAL** | `imagens/imgi_15_788104628_18628694836021901_9116897497193504579_n.jpg` | `site/assets/real-facade-night-800.webp` | `site/assets/real-facade-night-1600.webp` | Fachada noturna ampla com letreiro iluminado da Novara | Foto Real do Cliente |
| `real-facade-neon` | **FOTO REAL** | `imagens/imgi_34_705306261_26081475971529282_1635168780417373060_n.jpg` | `site/assets/real-facade-neon-800.webp` | `site/assets/real-facade-neon-1600.webp` | Detalhe em ângulo do letreiro de neon Novara | Foto Real do Cliente |
| `real-logo-novara` | **FOTO REAL** | `imagens/imgi_2_704766711_18400416724157431_4882130753143776944_n.jpg` | `site/assets/real-logo-novara-800.webp` | `site/assets/real-logo-novara-1600.webp` | Logotipo oficial (150x150) | Foto Real do Cliente (Recomenda-se confirmação do vetor com cliente) |

---

## 2. Notas de Governança
- **Nenhum arquivo em `/design` é referenciado no código do site:** Todos os caminhos de imagem apontam exclusivamente para `site/assets/*.webp`.
- **Todos os slots possuem imagens disponíveis:** Não houve necessidade de travar ou criar fallbacks de emergência, pois o conjunto de imagens geradas cobre 100% dos slots conceituais e o acervo real cobre a comida e salão autênticos.
