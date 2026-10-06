# DESIGN.md — Especificação Visual e Arquitetura de Design
**Projeto:** Novara Pizzas e Esfihas (São Bernardo do Campo - SP)  
**Referência Visual:** `design/mockup-full.png` (corte fatiado em `design/secoes/`)  
**Base de Conteúdo:** `CLIENTE.MD` e acervo fotográfico em `imagens/`  
**Data:** Outubro de 2026  

---

## 1. Leitura Honesta: O Mockup vs. A Realidade Concreta

O mockup em `design/mockup-full.png` é uma peça gráfica conceitual de altíssimo padrão estético, inspirada no design editorial italiano contemporâneo (estilo revista gastronômica avant-garde, scrapbook de chef, premiações Awwwards). No entanto, um confronto transparente com os dados factuais do cliente (`CLIENTE.MD`) e com as fotos reais (`imagens/`) revela profundos abismos que precisam ser conciliados com honestidade profissional:

| Aspecto | O que o Mockup Apresenta (Fantasia / Placeholder) | A Realidade Concreta do Cliente (`CLIENTE.MD` + `imagens/`) | Solução Adotada no Projeto |
| :--- | :--- | :--- | :--- |
| **Identidade do Negócio** | *"Avant-garde contemporary pizzeria"* — pizzaria napolitana de alta gastronomia, foco em degustação gourmet. | **"Novara Pizzas e Esfihas"** — Forneria popular e familiar de bairro (Dos Casa, SBC), com salão descontraído, forte delivery e retiradas no balcão. | Preservar a **elegância editorial e o impacto visual** do mockup, mas comunicar a verdadeira alma da casa: fartura, tradição, massas saborosas e o diferencial das esfihas abertas artesanais. |
| **Logotipo da Marca** | Tipografia serifada em caixa alta preta (`NOVARA`), minimalista, estilo revista de moda europeia. | Logotipo popular consolidado (`imgi_2`, `imgi_19`): contorno de skyline urbano em traço amarelo/dourado, tipografia vermelha com borda branca e o descritivo *"Pizzas e Esfihas"* em itálico branco sobre fundo verde-escuro floresta. | Manter a tipografia serifada de alto impacto no editorial principal, mas integrar o **símbolo do skyline e as cores identitárias reais (verde, vermelho, dourado)** para respeitar o patrimônio visual da marca. |
| **Ingredientes & Pratos** | Burrata derramando leite, anchovas inteiras marinadas com sal marinho, tomates heirloom europeus frescos (*"MATÉRIA-PRIMA PURA"*). | Pizzas tradicionais paulistas bem recheadas (Carne Seca com Catupiry e Pimenta Biquinho `imgi_33`, Borda Vulcão com Bacon e Mussarela Gratinada `imgi_19`, Mussarela com Tomate `imgi_28`), Esfihas Abertas de Queijo e Carne `imgi_17`, e Pizzas Doces generosas `imgi_18`. | Trocar as fotos genéricas de banco de imagens (burrata/anchovas) pelas **fotos reais dos produtos mais cobiçados da Novara**, mantendo a moldura de polaroid e selos artesanais. |
| **Forno e Cocção** | Forno a lenha rústico napolitano com chamas vivas e cúpula de alvenaria antiga (*"FORNO & TEMPO"*). | Não há fotos do forno no acervo do cliente. A menção no Google Maps cita "Forneria popular de entregas". | Usar o conceito de forno em alta temperatura e tempo de forno de forma elegante, com plate neutro ou foco no calor da forneria, sem inventar mentiras estruturais. |
| **Ambiente & Salão** | Toalha de linho xadrez verde com taça de vinho branco seco (*"TABLE & RESERVATIONS"* / *"PRENOTA UN TAVOLO"*). | Salão de bairro com mesas pretas e cadeiras vermelhas, varanda externa na calçada com gradil branco, drinks tropicais (ex: coquetel de morango `imgi_31`), refrigerantes e porções de batata frita com cheddar e bacon. | Adaptar a seção para reservas/visita ao salão acolhedor e familiar na varanda de SBC, substituindo a ideia de enoteca de luxo pela vibração autêntica do encontro entre amigos e família. |
| **Placeholder / Distintivos** | Selo de mentira: *"Awwwards Site of the Year GRAND PRIX"*. | O cliente possui **nota 4,5 com 895 avaliações reais no Google Maps**. | Substituir o badge fictício de festival internacional pela **prova social concreta e incontestável do Google Maps (4,5 ★ / +890 clientes)**. |
| **Ação Principal (CTA)** | *"[ PRENOTA UN TAVOLO // BOOK YOUR TABLE ]"* (Reserva de mesa em italiano/inglês). | Foco comercial imediato é o **Cardápio Online / Delivery Wabiz** (`novara-cafefilho.wabiz.delivery`) e pedidos via WhatsApp/Telefone. | O CTA principal deve direcionar para o **Cardápio & Delivery Online**, com CTA secundário para reservas/salão. |

---

## 2. Elementos Decorativos de Assinatura e Viabilidade Técnica

### 2.1. O "Cheese Pull" Central Contínuo (Fio de Queijo Derretido)
- **Descrição no Mockup:** Uma fatia de pizza apetitosa no topo (Hero) de onde se estica um longo fio elástico de queijo derretido, sinuoso em curva "S", com gotas âmbar translúcidas caindo, atravessando 4 blocos de conteúdo e finalizando próximo ao CTA inferior com uma dobra crocante de massa.
- **Avaliação Honesta de Viabilidade:**
  - *Tentar recriar em CSS puro / SVG de vetor simples:* **INVIÁVEL E ARTIFICIAL**. Queijo derretido com bolhas de queijo tostado, elasticidade orgânica e gotas líquidas ficaria com aparência de borracha ou plástico vetorizado amarelo.
  - *Abordagem Viável e Robusta:* Tratar o fio de queijo como um **Plate Gráfico de Alta Resolução (PNG-24 com canal alpha transparente)** ou um conjunto de 2 a 3 segmentos otimizados (topo com fatia, extensão intermediária em "S", gota final).
  - *Desafio de Responsividade:* Em telas móveis (360px a 430px), o fio desce pelo centro enquanto o conteúdo se alinha de forma compacta. Em desktops amplos (1024px+), o fio central precisa permanecer dentro de uma coluna de proporção controlada (`max-width: 600px` centrada) para não distorcer nem desconectar o layout.
  - *Regra CLAUDE.md:* O elemento contínuo **NÃO** receberá animações de scroll contínuo pesado, nem `transform`/`filter` nos contêineres ancestrais, garantindo 60fps constantes e compatibilidade total.

### 2.2. Bordas Rasgadas de Papel (*Torn Paper Edges*)
- **Descrição:** Transições entre seções com aspecto de papel rasgado à mão, exibindo fibras e desníveis orgânicos.
- **Viabilidade:** **TOTALMENTE VIÁVEL**. Implementado com divisores `<svg>` inline de alta fidelidade com `preserveAspectRatio="none"` ou `mask-image` com máscara SVG. Leve, sem impacto em tempo de carregamento.

### 2.3. Estética Scrapbook (Selos de Cera, Fitas Adesivas, Adesivos Smile e Carimbos)
- **Descrição:** Selos de cera vermelhos com relevo, tiras de fita crepe (*washi tape*) translúcida fosca, carimbo circular de fermentação 48h e adesivos smile amarelos.
- **Viabilidade:** **TOTALMENTE VIÁVEL**.
  - Fitas adesivas: Feitas 100% em CSS (`background: rgba(255,255,255,0.75)`, `backdrop-filter: blur(1px)`, `transform: rotate(-2deg)`, bordas denteadas ou sutilmente desiguais).
  - Selos e carimbos: SVGs vetorizados e estilizáveis com filtros CSS sutis (`drop-shadow`).

### 2.4. Anotações Manuscritas (*Handwritten Scribbles & Arrows*)
- **Descrição:** Textos editoriais explicativos que parecem rabiscados à mão com caneta/lápis (ex: *"editorial paper"*, *"Wood-fired"*, setinhas pontilhadas e corações).
- **Viabilidade:** **TOTALMENTE VIÁVEL** em HTML real utilizando uma fonte do Google Fonts especializada (`Caveat`) combinada com setas desenhadas em SVG inline responsivo.

---

## 3. Paleta de Cores e Matriz de Acessibilidade WCAG 2.1

As cores foram rigorosamente amostradas do mockup `design/mockup-full.png` e calibradas para garantir máxima vivacidade editorial sem abrir mão da conformidade com a norma **WCAG 2.1 nível AA e AAA**.

### 3.1. Variáveis de Cores (CSS Tokens)

```css
:root {
  /* Fundo e Papel */
  --color-paper: #F3F2EC;          /* Off-white quente de papel editorial artesanal */
  --color-paper-card: #FFFFFF;     /* Branco puro para polaroids e cartões */
  --color-paper-muted: #E6E4DC;    /* Papel kraft / dobras e sombras de papel */

  /* Tipografia e Tinta */
  --color-ink: #141414;            /* Preto carvão editorial profundo */
  --color-ink-muted: #4A4944;      /* Cinza grafite para notas e legendas */
  --color-ink-faint: #78766E;      /* Tinta cinza suave para anotações manuscritas */

  /* Identidade Novara & Destaques do Mockup */
  --color-brand-red: #9A1E1A;      /* Vermelho escarlate do botão CTA e molho */
  --color-wax-red: #822225;        /* Bordô fechado do selo de cera clássico */
  --color-brand-green: #1E4231;    /* Verde escuro floresta da marca Novara */
  --color-tag-green: #244233;      /* Verde oliva escuro da fita "No Compromise" */

  /* Acentos Gastronômicos */
  --color-cheese-gold: #DEA01B;    /* Âmbar do queijo dourado derretido */
  --color-cheese-light: #F8DA76;   /* Amarelo suave da massa do queijo */
  --color-sticker-yellow: #FFC001; /* Amarelo vibrante dos adesivos smile */
  --color-postit-blue: #B7CAC9;    /* Azul sálvia pastel da etiqueta de fermentação */
}
```

### 3.2. Matriz de Contraste WCAG 2.1

| Elemento Testado | Cor de Primeiro Plano | Cor de Fundo | Razão de Contraste | Nível WCAG | Status & Correção |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Títulos & Textos Editoriais** | `#141414` (Preto Tinta) | `#F3F2EC` (Papel Off-White) | **16.43 : 1** | **AAA** | **Aprovado com folga**. Legibilidade absoluta. |
| **Notas & Legendas Secundárias** | `#4A4944` (Grafite) | `#F3F2EC` (Papel Off-White) | **8.52 : 1** | **AAA** | **Aprovado com folga**. Perfeito para notas. |
| **Botão Principal (CTA)** | `#FFFFFF` (Branco) | `#9A1E1A` (Vermelho CTA) | **8.16 : 1** | **AAA** | **Aprovado com folga**. Botão de ação seguro. |
| **Fita / Tag "No Compromise"** | `#FFFFFF` (Branco) | `#244233` (Verde Escuro) | **11.04 : 1** | **AAA** | **Aprovado com folga**. |
| **Selo de Cera Relevo** | `#FFFFFF` (Branco) | `#822225` (Bordô Cera) | **9.53 : 1** | **AAA** | **Aprovado com folga**. |
| **Etiqueta Post-it 48h** | `#141414` (Preto Tinta) | `#B7CAC9` (Azul Pastel) | **10.79 : 1** | **AAA** | **Aprovado com folga**. Texto escuro obrigatório. |
| **Adesivo Smile** | `#141414` (Preto Tinta) | `#FFC001` (Amarelo) | **11.22 : 1** | **AAA** | **Aprovado com folga**. |
| **Texto Vermelho no Papel** | `#9A1E1A` (Vermelho) | `#F3F2EC` (Papel Off-White) | **7.27 : 1** | **AAA** | **Aprovado com folga** para badges e títulos. |
| **Texto sobre Queijo Dourado** | `#FFFFFF` (Branco) | `#DEA01B` (Queijo Ouro) | **2.30 : 1** | **REPROVADO** | **CORREÇÃO WCAG:** Jamais utilizar texto branco sobre o queijo. Se houver sobreposição, utilizar texto `#141414` (**8.03:1 AAA**) ou pílula com fundo sólido. |

---

## 4. Tipografia: Proposta de Fontes (Google Fonts)

Seguindo as restrições explícitas do `CLAUDE.md` (*proibido Inter, Roboto, Arial*), propomos duas candidatas do Google Fonts para cada papel estilístico:

### 4.1. Papel 1: Display / Títulos de Impacto Editorial
Usada em: *"NOVARA"*, *"CRUST ALCHEMY"*, *"MATÉRIA-PRIMA PURA"*, *"FORNO & TEMPO"*, *"TABLE & RESERVATIONS"*.
1. **Candidata 1 (Recomendada): `Playfair Display`** (Pesos: 700 Bold, 900 Black)
   - *Justificativa:* Possui serifas clássicas de altíssimo contraste, curvas nobres e proporções elegantes. Com peso 900, atinge exatamente a densidade visual e o ritmo das letras do mockup, sem comprometer a acentuação brasileira em palavras como *"MATÉRIA-PRIMA"*.
2. **Candidata 2: `Bodoni Moda`** (Pesos: 700, 900)
   - *Justificativa:* Ícone do design editorial gastronômico e de moda italiana. Geometria rigorosa com serifas retas e hastes contrastantes que evocam revistas italianas clássicas.

### 4.2. Papel 2: Apoio, Badges, Botões e Dados Técnicos
Usada em: Etiquetas (*"NO COMPROMISE"*), cardápio, horários, endereço, botão de pedido.
1. **Candidata 1 (Recomendada): `Plus Jakarta Sans`** (Pesos: 600 Semi-Bold, 700 Bold, 800 Extra-Bold)
   - *Justificativa:* Tipografia geométrica contemporânea, com formas abertas e acabamento moderno de alta definição. Escala perfeitamente em caixas altas com `letter-spacing` espaçado sem parecer fria ou genérica.
2. **Candidata 2: `Syne`** (Pesos: 600, 700, 800)
   - *Justificativa:* Fonte com personalidade artística arrojada e cortes geométricos únicos, ideal para reforçar o apelo avant-garde e descolado.

### 4.3. Papel 3: Anotações Manuscritas (*Editorial Scribbles & Notes*)
Usada em: Notas de caderno de chef, setas e detalhes explicativos (*"editorial paper"*, *"slow fermented"*, *"friendly service"*).
1. **Candidata 1 (Recomendada): `Caveat`** (Pesos: 500, 700)
   - *Justificativa:* Traço de caneta hidrográfica fluida e descontraída. É humanizada, dinâmica, legível em tamanhos reduzidos e casa perfeitamente com os grafismos de setas do mockup.
2. **Candidata 2: `Reenie Beanie`** (Peso: 400 Regular)
   - *Justificativa:* Traço fino de caneta esferográfica, transmitindo autenticidade de rabisco rápido e anotação imediata de cozinha.

---

## 5. Tabela de Camadas por Seção

O corte fatiado em `design/secoes/` dividiu a página em 4 blocos conceituais. Cada bloco é decomposto nas seguintes camadas ordenadas (do fundo para o topo):

| Seção (Fatia em `design/secoes/`) | Camada 1: CSS (Fundo / Textura) | Camada 2: SVG (Vetores / Bordas) | Camada 3: Imagem (FOTO Real ou PLATE) | Camada 4: HTML (Conteúdo / Tipografia) | Camada 5: Anotações & Stickers |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01. Hero & Crust Alchemy**<br>`01-hero-crust-alchemy.png`<br>*(Y: 0 – 400)* | Fundo `#F3F2EC` com micro-textura de ruído de papel CSS (`mix-blend-mode: multiply`). | SVG de rasgo de papel no topo e badge minimalista; carimbo circular de 48h. | **FOTO REAL:** Fatia de pizza da casa recortada (`imgi_28`) **OU** **PLATE GERADO:** Fatia no topo com queijo esticando.<br>**PLATE GERADO:** Massa crua na bancada enfarinhada. | Header com nota Google Maps (4,5 ★ / 895 avaliações); H1 gigante `NOVARA`; H2 `CRUST ALCHEMY`. | Stickers CSS/SVG: Tomate, folha de manjericão, smile amarelo, etiqueta azul de fermentação com texto real. |
| **02. Matéria-Prima Pura**<br>`02-materia-prima-pura.png`<br>*(Y: 400 – 608)* | Fundo contínuo de papel `#F3F2EC` com fita adesiva CSS translúcida. | Retalho de papel verde em SVG no canto direito; SVG de fita adesiva washi. | **FOTO REAL:** Prancha Polaroid com esfiha artesanal aberta de queijo (`imgi_17`) ou pizza vulcão artesanal (`imgi_19`).<br>**PLATE:** Continuação da fita de queijo central (canal alpha). | H2 `MATÉRIA-PRIMA PURA`; Badge inclinado `NO COMPROMISE`; Descritivo da fartura dos recheios artesanais. | Selo de cera vermelho bordô no canto direito; sticker smile no canto inferior do polaroid; anotação a mão *"Wood-fired door"*. |
| **03. Forno & Tempo**<br>`03-forno-e-tempo.png`<br>*(Y: 608 – 765)* | Fundo de papel `#F3F2EC` com transição de papel rasgado superior. | Máscara de arco do forno em SVG ou moldura de pedra; setinhas curvas e coraçãozinho em SVG. | **PLATE GERADO:** Forno a lenha rústico em arco com lenha incandescente e chamas douradas.<br>**PLATE:** Curva inferior da fita de queijo central. | H2 `FORNO & TEMPO`; Micro-copy sobre a temperatura e crocância da massa assada na hora. | Rabiscos manuais e setas apontando para a textura e calor da massa. |
| **04. Salão, Mesa & CTA**<br>`04-table-reservations.png`<br>*(Y: 765 – 1024)* | Fundo de papel com rodapé rasgado revelando base escura `#141414`. | Divisor SVG de papel rasgado inferior; botão pulsador 3D em puro CSS. | **FOTO REAL:** Mesa da varanda com drinks e porções (`imgi_31`) **OU** **PLATE GERADO:** Toalha xadrez verde com taça de vinho e queijo final.<br>**FOTO REAL:** Fachada acolhedora (`imgi_15` / `imgi_34`). | H2 `MESA & SALÃO` (ou `TABLE & RESERVATIONS`); Botão CTA principal: `[ PEDIR DELIVERY / CARDÁPIO ]` + link WhatsApp/Telefone. | Sticker smile com espátula de pizza; anotação *"friendly service"*; botão vermelho táctil 3D. |

---

## 6. Reinterpretação de Elementos Decorativos Complexos em CSS/SVG Real

Para garantir carregamento instantâneo, total responsividade e acessibilidade, os elementos do mockup que parecem "gráficos estáticos colados" serão recriados com código limpo:

1. **Fitas Adesivas (*Washi Tape*):**
   - Feitas em CSS puro:
   ```css
   .washi-tape {
     background: rgba(255, 255, 255, 0.72);
     box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
     backdrop-filter: blur(1.5px);
     transform: rotate(-3deg);
     border-left: 2px dashed rgba(200, 200, 200, 0.4);
     border-right: 2px dashed rgba(200, 200, 200, 0.4);
   }
   ```
2. **Selo de Cera Vermelho (*Wax Seal*):**
   - Elemento SVG com bordas orgânicas irregulares de cera derretida, gradiente radial sutil (`#A62226` para `#6B1719`) e sombra projetada realista via `filter: drop-shadow(0 4px 6px rgba(0,0,0,0.25))`.
3. **Divisores de Papel Rasgado (*Torn Paper Divider*):**
   - Vetor SVG responsivo com `d="M0,10 Q20,2 40,9 T80,5 T120,11 T160,3 ... L160,50 L0,50 Z"`, escalável em qualquer largura de tela sem pixelar.
4. **Botão de Campainha Vermelho 3D (*Push Button*):**
   - Criado 100% em CSS sem imagens externas:
   ```css
   .btn-buzzer-3d {
     width: 52px;
     height: 52px;
     border-radius: 50%;
     background: radial-gradient(circle at 35% 35%, #E53935, #9A1E1A 60%, #5C0E0B);
     box-shadow: 
       0 6px 12px rgba(154, 30, 26, 0.4),
       inset 0 2px 4px rgba(255, 255, 255, 0.6),
       inset 0 -3px 6px rgba(0, 0, 0, 0.4);
     cursor: pointer;
     transition: transform 0.15s ease, box-shadow 0.15s ease;
   }
   .btn-buzzer-3d:active {
     transform: scale(0.94) translateY(2px);
     box-shadow: 0 2px 4px rgba(154, 30, 26, 0.4);
   }
   ```
5. **Adesivos Smile e Tomate (*Stickers*):**
   - Construídos em SVG com borda branca destacada (`stroke: #FFFFFF; stroke-width: 4px;`) e sombra suave, idênticos aos stickers de vinil reais.

---

## 7. Especificação de Animação e Motion por Seção

Em estrita consonância com o `CLAUDE.md`:
> *"Qualquer elemento decorativo contínuo/caro (ex. uma faixa, textura ou filtro pesado que atravessa várias seções): ele NÃO se move na fase de motion, e nada nele pode ganhar transform/filter/opacity<1 em nenhum ancestral. Só transform/opacity nas camadas-folha. Nada acima da dobra depende de JS para aparecer — motion carrega depois do load."*

### 7.1. Seção 1 (Hero & Crust Alchemy)
- **Carga Inicial (Above the Fold):** Conteúdo 100% legível e visível sem JS (sem `opacity: 0` inicial travando a tela).
- **Motion (Pós-Load / Entrada Suave):**
  - Título `NOVARA`: Efeito de desdobramento sutil em Y (`translateY(16px) -> translateY(0)` em 0.6s).
  - Adesivos (Tomate, Smile, 48h): Efeito de "carimbada física" escalonada (*stagger* de 150ms): `scale: 1.15 -> 1.0` com leve rotação elástica.
  - Gotículas do queijo: Oscilação pendular milimétrica e suave de gota em repouso (`transform: translateY(0) -> translateY(3px)` em loop suave de 3s com `will-change: transform`).

### 7.2. Seção 2 (Matéria-Prima Pura)
- **Scroll Trigger:** Ao atingir a viewport:
  - Prancha Polaroid: Transição com leve desvio angular (`rotate(-3deg) -> rotate(-1.5deg)`) simulando foto afixada em mural.
  - Tag *"NO COMPROMISE"*: Entrada tipo fita colada com leve fade e escala.

### 7.3. Seção 3 (Forno & Tempo)
- **Efeito Visual:**
  - Chamas do Forno: Leve pulso de luminosidade quente no SVG de sobreposição (`opacity: 0.85 <-> 1.0` em ciclo calmo de 4s).
  - Setas desenhadas a mão: Animação de traçado SVG (`stroke-dashoffset` revelando a linha como se estivesse sendo riscada com giz/caneta).

### 7.4. Seção 4 (Mesa, Salão & CTA)
- **Interação:**
  - Botão CTA Vermelho: Efeito de pulso de atenção discreto a cada 5 segundos; hover magnético suave.
  - Botão 3D Redondo: Feedback táctil no clique com compressão (`scale(0.92)`) e som/vibração sutil se compatível.

---

## 8. PLANO DE IMAGENS (Estratégia Detalhada)

Esta é a espinha dorsal de todo o projeto. Cada espaço visual é mapeado entre **FOTO REAL** (do acervo de `imagens/`) ou **PLATE GERADO** (elementos conceituais neutros), acompanhado dos **prompts prontos para uso imediato**.

### 8.1. Mapeamento de Slots de Imagem

| Slot de Imagem | Tipo | Origem Exata / Destino | Tratamento Necessário |
| :--- | :--- | :--- | :--- |
| **Slot 1: Fatia Hero & Fio de Queijo** (Topo) | **FOTO REAL** (Fatia) + **PLATE** (Fio contínuo) | FOTO: `imagens/imgi_28_...jpg`<br>PLATE: `design/plates/cheese-ribbon.png` | A fatia de mussarela da Novara tem puxada real de queijo (`imgi_28`). O fio de queijo que percorre a página inteira precisa de plate de alta definição com fundo transparente. |
| **Slot 2: Massa Crua na Bancada** (Crust Alchemy) | **PLATE GERADO** | `design/plates/dough-fermentation.png` | O cliente não possui foto de massa crua fermentando na farinha. Gerar plate fotorealista de massa madre. |
| **Slot 3: Polaroid Ingredientes** (Matéria-Prima) | **FOTO REAL** | `imagens/imgi_17_...jpg` (Esfiha aberta) ou `imagens/imgi_19_...jpg` (Pizza generosa) | Substituir burrata/anchovas do mockup pelas fotos reais das esfihas e pizzas artesanais da Novara. |
| **Slot 4: Forno a Lenha Incandescente** (Forno & Tempo) | **PLATE GERADO** | `design/plates/wood-fired-oven.png` | Não há foto do forno no acervo. Gerar plate neutro em arco com lenha em brasa viva. |
| **Slot 5: Mesa / Salão / Drinks** (Mesa & Reservas) | **FOTO REAL** | `imagens/imgi_31_...jpg` (Mesa na varanda com drink) | A foto real da varanda mostra a mesa completa servida, drink da casa e pizzas. |
| **Slot 6: Logotipo Oficial da Casa** (Header / Footer) | **FOTO REAL (Ajustada)** | `imagens/imgi_2_...jpg` ou vetorizado a partir de `imagens/imgi_19_...jpg` | O arquivo original tem apenas 150x150px. Precisa de ampliação e vetorização SVG cristalina. |
| **Slot 7: Fachada Noturna Iluminada** (Sobre / Localização) | **FOTO REAL (Ajustada)** | `imagens/imgi_15_...jpg` e `imagens/imgi_34_...jpg` | Fotos reais do letreiro de neon noturno da Novara em SBC. |

---

### 8.2. Prompts PRONTOS para Geração de PLATES (Decorativos / Conceituais)

> **Nota:** Priorizou-se código CSS/SVG em todos os elementos possíveis (fitas, selos, adesivos, divisores). Os plates abaixo são estritamente restritos àquilo que exige textura fotorealista inacessível por vetor.

#### PLATE 01: Fio de Queijo Derretido Contínuo (*Cheese Pull Ribbon*)
* **Uso:** Elemento de assinatura que corta o layout central de ponta a ponta com canal alfa transparente.
* **Arquivo de Saída:** `design/plates/cheese-ribbon.png`
* **Prompt Pronto para Copiar e Colar:**
```text
An ultra-realistic, continuous gourmet mozzarella cheese pull ribbon, stretching vertically downwards in a gentle organic S-curve against a pure transparent isolated background (PNG with alpha channel). The melted cheese exhibits realistic stringy textures, golden toasted blisters, warm molten gradients (#DEA01B, #F9D874), creamy elasticity, and tiny dangling honey-golden melted droplets. Commercial food photography, sharp studio lighting, 8k resolution, macro food details, appetizing, no background, pure cheese pull only.
```

#### PLATE 02: Massa Artesanal Fermentando na Bancada (*Slow Fermented Dough*)
* **Uso:** Bloco 1 (Crust Alchemy / Fermentação).
* **Arquivo de Saída:** `design/plates/dough-fermentation.png`
* **Prompt Pronto para Copiar e Colar:**
```text
Close-up of a raw rustic artisanal pizza dough ball naturally rising and resting on a dark slate baking stone, generously dusted with fine white flour. Evident gas fermentation bubbles under the smooth gluten surface, artisanal bakery atmosphere, dramatic soft low-key studio lighting, editorial culinary magazine photography, high texture detail, 8k, photorealistic, cinematic food still life.
```

#### PLATE 03: Interior de Forno a Lenha com Chamas (*Wood-Fired Oven Arch*)
* **Uso:** Bloco 3 (Forno & Tempo).
* **Arquivo de Saída:** `design/plates/wood-fired-oven.png`
* **Prompt Pronto para Copiar e Colar:**
```text
Front view of an authentic artisanal wood-fired pizza oven chamber through a curved rustic brick archway. Glowing hardwood logs burning with vibrant golden-orange flames, glowing hot embers, intense radiant heat, cinematic dark oven interior with soft ambient ember glow on stone hearth, 8k resolution, professional food documentary photography, hyper-realistic.
```

---

### 8.3. Prompts PRONTOS para AJUSTE de FOTOS REAIS do Cliente

> **Regra Obrigatória:** Seguir à risca a diretriz *"mantenha tudo idêntico, só corrija X"*, referenciando o arquivo exato de `imagens/`.

#### AJUSTE 01: Logotipo Oficial em Alta Resolução / Vetor
* **Arquivo de Origem:** `imagens/imgi_2_704766711_18400416724157431_4882130753143776944_n.jpg`
* **Problema:** Resolução extremamente baixa (150x150 pixels), imprópria para telas retina.
* **Prompt Pronto de Ajuste:**
```text
Based on the logo image imgi_2_704766711_18400416724157431_4882130753143776944_n.jpg: keep everything strictly identical in shape, typography, proportions and colors. Only enhance and upscale the resolution to ultra-sharp vector-grade definition (4000x4000). Keep the dark forest green background (#1E4231), the extruded gold architectural skyline outline at the top, the bold red serif typography "Novara" with clean white border bevel, and the white italic subtitle "Pizzas e Esfihas" at the bottom. Crystal-clear edges, zero compression artifacts, perfect fidelity to the original.
```

#### AJUSTE 02: Limpeza do Fundo da Varanda e Rua
* **Arquivo de Origem:** `imagens/imgi_31_713983671_981539201330623_1659608048361987037_n.jpg`
* **Problema:** A cena da mesa e do garçom é autêntica e rica, mas o letreiro iluminado da farmácia ("Drogasil") e os carros na rua ao fundo poluem a atmosfera gastronômica.
* **Prompt Pronto de Ajuste:**
```text
Based on image imgi_31_713983671_981539201330623_1659608048361987037_n.jpg: keep everything identical in the foreground and midground — maintain the waiter serving, the vibrant red strawberry cocktail glass with sugar rim, the plate of golden french fries with cheddar and bacon, the savory pizza, the sweet dessert pizza, the black tables, red chairs and the white balcony railing. Only correct the deep background street across the railing: remove the commercial pharmacy neon signs ("Drogasil") and parked cars, replacing them with a soft, warm, out-of-focus nighttime urban bokeh with subtle ambient streetlights.
```

#### AJUSTE 03: Fachada Noturna Externa sem Carros
* **Arquivo de Origem:** `imagens/imgi_15_788104628_18628694836021901_9116897497193504579_n.jpg`
* **Problema:** Carros estacionados bloqueiam a visão térrea da varanda e a placa lateral da drogaria compete com o restaurante.
* **Prompt Pronto de Ajuste:**
```text
Based on image imgi_15_788104628_18628694836021901_9116897497193504579_n.jpg: keep the entire restaurant building, architecture, glowing neon sign "Novara" with green skyline, "Pizzas e Esfihas" neon sign, fairy lights, warm indoor lighting, and the white terrace railing completely identical. Only correct the street foreground: remove the parked silver SUV and vehicles on the asphalt, clean the street pavement with subtle warm reflections, and soften or remove the adjacent pharmacy sign on the left edge. Keep authentic night atmosphere.
```

#### AJUSTE 04: Isolamento da Pizza com Borda Vulcão e Bacon
* **Arquivo de Origem:** `imagens/imgi_19_805485575_18417622879157431_1435122697872442889_n.jpg`
* **Problema:** A pizza é espetacular, mas a borda de papelão ondulado da caixa delivery limita o uso como prato editorial solto.
* **Prompt Pronto de Ajuste:**
```text
Based on image imgi_19_805485575_18417622879157431_1435122697872442889_n.jpg: keep the pizza completely identical with 100% fidelity — the braided golden volcano crust, melted cheese, crisp diced bacon, black olives, and herbs. Only remove the brown cardboard delivery box edges, isolating the entire round pizza with a clean transparent background (PNG alpha channel) or placing it seamlessly on a rustic dark granite pizza serving board with soft natural drop shadow.
```

---

## 9. Perguntas para o Usuário (Decisões Puramente Subjetivas)

*(Decisões de engenharia de software, contraste WCAG, responsividade mobile e arquitetura de código foram decididas de forma autônoma conforme as regras do projeto. Restam apenas as seguintes decisões de alinhamento subjetivo):*

1. **Posicionamento Editorial do Texto:** Prefere que o tom dos títulos do site mantenha a elegância poética em português clássico (ex: *"A Alquimia da Massa"*, *"Matéria-Prima Pura"*, *"O Forno & O Tempo"*) ou que adote uma linguagem mais direta e comercial de pizzaria tradicional paulista (ex: *"Tradição em Massas"*, *"Ingredientes Selecionados"*, *"Assadas no Ponto Certo"* )?
2. **Foco do Botão Principal (CTA):** O botão de maior destaque no topo e no rodapé deve levar prioritariamente para o **Cardápio Online Wabiz** (`novara-cafefilho.wabiz.delivery`) ou para o **WhatsApp direto** para pedidos e reservas?
3. **Tratamento das Esfihas no Layout:** Como as esfihas abertas são um pilar de vendas central da Novara (conforme o próprio nome *"Novara Pizzas e Esfihas"*), deseja que uma das seções do layout seja dedicada com destaque exclusivo às esfihas artesanais (usando a foto real `imgi_17`), adaptando o bloco que no mockup mostrava peixe e burrata?
4. **Substituição da Taça de Vinho no Bloco Final:** No mockup há uma taça de vinho branco sobre toalha xadrez. Na vida real, a Novara oferece drinks tropicais (como o coquetel de morango da foto `imgi_31`), cervejas e refrigerantes. Prefere exibir a foto real da varanda com o drink e as porções da casa ou manter a ilustração estilizada da toalha com taça para manter o ar clássico do mockup?

---

## 10. Pendências com o Cliente e Mensagem Pronta

### 10.1. Lista de Itens a Coletar com o Estabelecimento
- **WhatsApp Oficial para Vendas:** No Google Maps constam apenas telefones fixos ((11) 4109-0313 e os números de fachada 4171-1234 / 4172-1234). Necessário o número celular/WhatsApp direto com link para pedidos.
- **Arquivo Vetorial do Logotipo:** Solicitar o arquivo em vetor (.AI, .EPS, .CDR ou .SVG) ou PNG com fundo transparente em alta resolução do logo original da Novara.
- **Horário Semanal Completo:** Confirmar horários de abertura e fechamento de terça a domingo (e se abre às segundas-feiras).
- **Especificações de Cozinha:** Confirmar se o forno da unidade é a lenha ou a gás/esteira, e o tempo real de descanso/fermentação da massa.
- **Autorização de Uso de Imagem:** Validação formal para veiculação das fotos com clientes/atendentes no salão.

---

### 10.2. Mensagem Pronta para o Cliente (WhatsApp / E-mail)

```text
Olá, equipe da Novara Pizzas e Esfihas! Tudo bem? 🍕✨

Estamos desenvolvendo o novo site oficial da Novara para destacar a tradição, o sabor e a qualidade impecável das pizzas e esfihas de vocês na internet, com foco em facilitar os pedidos de delivery e atrair ainda mais clientes para a casa!

O projeto visual está ficando incrível, no padrão das melhores casas de gastronomia, e para finalizarmos os últimos detalhes com total fidelidade ao negócio de vocês, precisamos apenas confirmar 4 informações rápidas:

1. WhatsApp oficial de pedidos: Qual é o número de WhatsApp principal que os clientes usam para pedir ou tirar dúvidas? (vamos colocar um botão direto para o cliente clicar e já abrir a conversa com vocês).
2. Horários de funcionamento: Vocês abrem de que horas até que horas em cada dia da semana? Abrem às segundas ou apenas de terça a domingo?
3. Logotipo da Novara: Vocês teriam o arquivo do logo em alta definição (em PDF, vetor ou PNG sem fundo)?
4. Forno e massa: As pizzas e esfihas de vocês são assadas em forno a lenha? A massa tem algum segredo especial (como fermentação artesanal) que vocês gostariam que a gente destacasse no texto?

Muito obrigado pela parceria! Estamos ansiosos para colocar no ar uma presença digital à altura do sucesso da Novara! 🚀
```
