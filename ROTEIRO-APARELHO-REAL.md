# ROTEIRO DE TESTES EM APARELHOS REAIS (SMARTPHONES E TABLETS)

Este roteiro fornece o passo a passo prático para validação do site **Novara Pizzas e Esfihas** diretamente na mão de usuários finais em aparelhos físicos **iPhone (iOS / Safari)** e **Android (Chrome / Samsung Internet)**.

---

## 1. Como Subir o Site para Acesso na Rede Local (Wi-Fi)

Para testar no celular sem depender de publicação em servidor externo, compartilhe o servidor local pela sua rede Wi-Fi:

1. **Obtenha o IP local do seu computador:**
   Abra o PowerShell no Windows e execute:
   ```powershell
   ipconfig
   ```
   Localize o endereço **IPv4** do seu adaptador Wi-Fi ou Ethernet (exemplo: `192.168.1.105`).

2. **Inicie o servidor HTTP vinculado a todas as interfaces:**
   No diretório do projeto, execute:
   ```powershell
   python -m http.server 8080 --directory site --bind 0.0.0.0
   ```

3. **No smartphone (conectado ao mesmo Wi-Fi do computador):**
   Abra o navegador (Safari no iPhone ou Chrome no Android) e acesse:
   ```text
   http://192.168.1.105:8080
   ```
   *(Substitua pelo seu IPv4 real).*

---

## 2. Checklist de Validação no iPhone (iOS / Safari & Chrome iOS)

### A. Entalhes, Dynamic Island e Safe Areas
- [ ] **Orientação Retrato (Portrait):** Verifique se o topo do Hero (com o selo social proof de 4.5 estrelas e o badge de 48h) mantém distância confortável da câmera frontal / Dynamic Island, sem cortes.
- [ ] **Orientação Paisagem (Landscape):** Gire o iPhone na horizontal (`844x390`). O conteúdo das seções se acomoda respeitando as margens de toque laterais (`env(safe-area-inset-left)` e `env(safe-area-inset-right)`)?
- [ ] **Rolagem Horizontal:** Tente arrastar a tela para os lados com o polegar. Confirme se há **zero rolagem lateral** indesejada em toda a extensão da página.

### B. Barra de Endereço Dinâmica do Safari
- [ ] **Comportamento 100svh:** Role a página para baixo fazendo a barra de URL do Safari recolher.
- [ ] **Transição sem Saltos:** Confirme se a contração e expansão da barra de navegação do Safari ocorre de forma fluida, sem "pulos" visuais ou reposicionamento abrupto das fotos ou do fio de queijo.

### C. Rolagem Tátil e ProMotion (120Hz)
- [ ] **Inércia e Fluidez:** Nos modelos com tela de 120Hz (iPhone 13 Pro até 16 Pro Max), deslize o dedo com velocidade. A aceleração com a biblioteca Lenis deve parecer amanteigada e natural, sem sensação de arrasto ou delay perceptível.
- [ ] **Navegação Rápida:** Faça um "flick" rápido do topo até o rodapé. Confirme que nenhuma imagem ou elemento fica preso em estado transparente (`opacity: 0`).

### D. Botão Flutuante de Controle de Movimento
- [ ] **Ergonomia do Toque:** O botão circular no canto inferior esquerdo é facilmente alcançável pelo polegar em uso com apenas uma mão?
- [ ] **Ação Imediata:** Dê um toque no botão. O ícone e texto devem alternar para *"Pausar Movimento"* / *"Movimento Pausado"*, congelando instantaneamente as micro-flutuações e os parallaxes.
- [ ] **Feedback Tátil:** O botão reage ao toque com leve compressão visual sem travar a navegação.

### E. Ações de Conversão (Wabiz & Telefone)
- [ ] **Alvos de Toque (Touch Targets):** Toque no botão circular 3D da campainha e no botão vermelho em pílula *"Pedir no Delivery"*. O clique deve ser registrado de primeira sem necessidade de precisão cirúrgica (área superior a 44x44px).
- [ ] **Links Externos:** Ao tocar no botão de delivery, o Safari abre a plataforma Wabiz da Novara em nova aba preservando a navegação original.

### F. Adicionar à Tela de Início (PWA)
- [ ] No Safari, toque no ícone de compartilhamento e selecione **"Adicionar à Tela de Início"**.
- [ ] Verifique se o ícone do Apple Touch Icon (`site/apple-touch-icon.png`, 180x180 com o selo dourado e vinho) é exibido com nitidez impecável e o nome sugerido é *"Novara"*.
- [ ] Ao abrir pelo atalho criado, o site carrega em tela cheia com a cor de fundo `#F5EFEB`.

---

## 3. Checklist de Validação no Android (Chrome & Samsung Internet)

### A. Modos de Desempenho e Economia de Bateria
- [ ] **Modo Economia de Energia:** Ative o modo de economia de bateria do Android e recarregue a página. O navegador aciona nativamente a diretiva `prefers-reduced-motion`? O site substitui as animações complexas por transições de fade sutis (200ms)?
- [ ] **Consistência de FPS:** Em aparelhos intermediários de 60Hz e topos de linha de 120Hz, a rolagem mantém taxa de quadros estável sem quedas bruscas de desempenho.

### B. Renderização Tipográfica e Fontes WOFF2
- [ ] **Nitidez dos Tipos:** Verifique se as fontes `Playfair Display` (serifada rústica dos títulos), `Oswald` (subtítulos condensados) e `Caveat` (anotações manuscritas) aparecem idênticas ao desktop, sem substituir por Roboto ou fontes padrão do Android.
- [ ] **Efeito Letterpress no Hero:** O título monumental `NOVARA` exibe cada letra com a textura e assentamento tipográfico característico.

### C. Instalação e Manifest PWA
- [ ] No Chrome Android, verifique se a opção *"Instalar aplicativo"* ou *"Adicionar à tela inicial"* reconhece o arquivo `site.webmanifest` e gera o ícone adaptativo com fundo `#F5EFEB`.

---

## 4. Testes de Casos Limite e Acessibilidade

### A. Zoom de Acessibilidade do Sistema (200%)
- [ ] Nas configurações de acessibilidade do celular (Tamanho da Fonte / Zoom da Tela), configure o texto no tamanho máximo (+200%).
- [ ] Retorne ao navegador: os textos fluem em novas linhas sem cortar palavras ou sobrepor títulos sobre fotos.

### B. Modo Escuro Nativo do Sistema
- [ ] Alterne o celular para o **Modo Escuro (Dark Mode)**.
- [ ] O site deve manter o papel artesanal `#F5EFEB` e os tons quentes de forneria preservados (declarado formalmente no CSS via `color-scheme: light`), impedindo que o navegador inverta arbitrariamente as cores ou deixe fotos escuras.

### C. Conexão Limitada (Simulação 3G / Offline)
- [ ] No modo avião ou com rede móvel reduzida, verifique se o CSS crítico inline carrega a estrutura e o texto imediatamente antes mesmo do download das imagens completas.
