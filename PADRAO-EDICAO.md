# Padrão de edição — reels falados (talking head + B-roll)

Medido no vídeo de referência (reel "capitão da Marinha / submarino", 1:30, 9:16) em 04/10/2026.
Aplicar em todo vídeo bruto gravado no mesmo formato (Fabio falando para a câmera, fundo de tijolo com flores).

## Estrutura do roteiro (o bruto já vem assim)
1. **Gancho** (0–5 s): "Esse cara é um dos ___ mais ___ e mais ___ de ___."
2. **Promessa**: "Ele criou um protocolo polêmico para provar que ___."
3. **História curta** do personagem (2–3 frases).
4. **"E esse é o protocolo para você parar de ___."**
5. **Primeiro / Segundo / Terceiro**: cada regra + "ele diz que…" + aplicação ("meu querido", "pequeno gafanhoto").
6. **A virada**: a cena decisiva da história.
7. **Pergunta ao espectador + CTA**: "Se você ___, me segue, porque você é demais."

## Corte
- Escolher sempre a **última tomada** quando a frase é repetida (retake), a não ser que ela esteja pior.
- Cortar todo silêncio > 0,30 s (deixar ~0,09 s de respiro de cada lado). Ritmo final ≈ 1:30 para ~2:20 de bruto.
- Microfades de 12–15 ms em cada emenda de áudio (sem clique).

## Visual (1080×1920, 30 fps)
| Momento | Tratamento |
|---|---|
| Gancho | **Tela dividida**: imagem do personagem em cima (0–880 px), apresentador embaixo. **Caixa laranja** (#E4471C, contorno branco fino) com o texto do gancho em **CAIXA ALTA, fonte condensada (Anton)**, branco com contorno preto. Sem legenda pequena. |
| Promessa / dados | Tela dividida com imagem do assunto em cima; legenda pequena na linha da divisão. |
| História / "ele diz que…" | **B-roll em tela cheia** com movimento lento (zoom 1,00↔1,10, alternando entrada e saída). |
| Aplicação para o espectador | **Talking head** com **punch-in** alternado a cada corte (1,00 → 1,15–1,20 → 1,30–1,38 na frase de impacto). |
| Cada "Primeiro/Segundo/Terceiro", frase-tese, número forte | **Frase de impacto**: CAIXA ALTA, Montserrat Black ~90 px, branca com sombra; no peito (talking head) ou no centro (B-roll). Entra com pop rápido (80 %→100 % em 90 ms). A legenda pequena some enquanto ela está na tela. |
| Viradas de bloco | **Flash laranja** (#FF6A1A, 0,45 s, some em fade) no primeiro quadro do novo bloco. |

- Troca de plano a cada **2–5 s**; nunca mais de ~6 s no mesmo enquadramento.
- **Legenda pequena** o tempo todo: Montserrat SemiBold 44 px, branca, contorno fino e sombra suave, 1–3 palavras por vez, quebrando na pontuação. Posição: y≈1440 (talking head/B-roll) ou na linha da divisão (tela dividida).
- B-roll: primeiro fotos reais do personagem e do lugar (Wikimedia, domínio público); depois banco de imagens (Unsplash) para os trechos sobre a empresa e o espectador. Créditos em `broll/CREDITOS.txt`.

## Áudio
- Só a voz, normalizada em −14 LUFS (pico −1,5 dBTP), AAC 192 kbps.

## Como rodar (exemplo: `reel-stockdale/edicao/`)
1. `ic.py <id-do-link-icloud> bruto.mov`: baixa o vídeo de um link `share.icloud.com/photos/<id>`.
2. `tr.py bruto.wav`: transcrição com tempo por palavra (faster-whisper, modelo small, pt).
3. `edl.py`: tomadas a manter + remoção de silêncios → `segs.json` → corte do A-roll.
4. `build.py`: planos (`SHOTS`), frases de impacto (`EMPH`), gancho (`HOOK`) → `shots/*.mp4` + `subs.ass`.
5. Montagem final: concat dos planos + `ass=subs.ass:fontsdir=fonts` + loudnorm.
