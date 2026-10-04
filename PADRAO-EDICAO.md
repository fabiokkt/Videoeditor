# Padrão de edição — reels falados (talking head + B-roll)

Medido quadro a quadro no vídeo de referência (reel "capitão da Marinha / submarino", 1:30, 9:16,
link iCloud `07f1AD6emvO3QFiTR0mzjMACQ`). Medidas em pixels de um quadro 1080×1920.
Aplicar em todo bruto gravado no mesmo formato (Fabio falando para a câmera, fundo de tijolo com flores).

## Estrutura do roteiro (o bruto já vem assim)
1. **Gancho** (0–5 s): "Esse cara é um dos ___ mais ___ e mais ___ de ___."
2. **Promessa**: "Ele criou um protocolo polêmico para provar que ___."
3. **História curta** do personagem.
4. **"E esse é o protocolo para você parar de ___."**
5. **Primeiro / Segundo / Terceiro** + "ele diz que…" + aplicação ("meu querido", "pequeno gafanhoto").
6. **A virada**.
7. **Pergunta + CTA**: "Se você ___, me segue, porque você é demais."

## Corte
- Retake: fica a **última tomada**. Silêncio > 0,30 s sai (0,09 s de respiro). Microfades de 12–15 ms.
- **Palavrão**: o som é cortado no meio da palavra (fica "po…"), entra o som curto de censura da referência
  e a legenda mostra `po---`.

## Gancho (0 até o fim da primeira frase)
- **Tela dividida**: imagem em cima (0–840 px), apresentador embaixo (840–1920) em **close (zoom 1,25)**,
  olhos em y≈1357.
- Imagem do topo em **duotone vermelho-escuro** (preto profundo, altas-luzes vermelhas). Na metade do gancho
  ela troca por outra imagem do assunto, com **light leak**.
- **Caixa**: x 33→1047, y 594→1097, cantos de 12 px, **borda branca 5 px**, sombra escura por baixo,
  **degradê vertical #FB672A → #F1390D**. Fica parada na tela do 1º quadro até o fim da frase.
- **Texto**: **Oswald Bold**, CAIXA ALTA, 5 linhas centralizadas, branco, **contorno preto 4,5**, sombra 3.
  Tamanho: a linha mais longa (~19 letras) ocupa ~890 px (libass 156). Centros das linhas: y 664 / 757 / 850 / 943 / 1036.
- Sem legenda pequena durante o gancho.

## Resto do vídeo
| Elemento | Especificação |
|---|---|
| **Legenda pequena** | Montserrat SemiBold, minúsculas normais, branca com sombra suave; ~378 px de largura para "A pessoa chega" (libass 74). 1–3 palavras, quebra na pontuação. y=845 em B-roll e tela dividida, y=1458 no talking head. |
| **Frase de impacto** | Montserrat ExtraBold, CAIXA ALTA, branca com contorno cinza-escuro e sombra; ~811 px para 15 letras (libass 127). **Digitada letra a letra (~28 letras/s)** em sincronia com a fala; y=1190. A legenda pequena some enquanto ela está na tela. Usa as mesmas palavras faladas. |
| **Talking head** | Punch-in alternado **1,30 ↔ 1,50** a cada corte (1,60 numa frase curta de impacto); olhos a 43 % da altura. |
| **B-roll** | Tela cheia com zoom lento 1,00↔1,08. Foto muito larga: **faixa nítida de 1190 px** no centro + a mesma foto desfocada atrás. |
| **Light leak** | Laranja/amarelo descendo do topo (~0,3 s antes do corte) e um bloco laranja-avermelhado à esquerda que some ~0,2 s depois. Em quase toda entrada de B-roll. |
| Ritmo | Troca de plano a cada 2–5 s. |

## Som
- **Trilha da referência** (separada da voz com demucs/htdemucs): impacto grave de 0,5–3,4 s no gancho,
  silêncio até ~4,4 s, depois a cama de música até o CTA; a **subida (clímax)** vai na virada da história.
- A música fica **~20 dB abaixo da voz** (mesma proporção da referência).
- **Whoosh** da referência em cada light leak (pico no corte), exceto no do gancho.
- Mix final normalizada em −14 LUFS (pico −1,5 dBTP), AAC 192 kbps.

## Como rodar (ver `reel-stockdale/edicao/`)
1. `ic.py <id-do-link-icloud> bruto.mov`: baixa vídeo de `share.icloud.com/photos/<id>` (bruto e referência).
2. `tr.py bruto.wav`: transcrição palavra a palavra (faster-whisper small, pt).
3. `edl.py`: tomadas + remoção de silêncio → `segs.json` → corte do A-roll.
4. `python3 -m demucs --two-stems=vocals -n htdemucs referencia.wav`: separa a trilha da referência.
5. `mix2.py`: remapeia a trilha, whooshes, censura e proporção voz/música → `mix2.wav`.
6. `build2.py`: planos (`SHOTS`), leaks (`LEAKS`), frases (`EMPH`), gancho (`HOOK_LINES`) → `shots2/`;
   `build2.py final` → caixa do gancho + leaks + legendas + mix → vídeo final.
