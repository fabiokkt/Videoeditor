# Blueprint numérico — vídeo original "Casas Bahia"

Mapa completo do vídeo de referência, extraído frame a frame do projeto CapCut do usuário. Use como gabarito de **proporções e ritmo** ao montar vídeos novos. Timeline-mestre: **2040 frames @ 30 fps (68s) a 1.0x** → 1.087x → **1877 frames (62.6s)**.

> ⚠️ **Documento histórico.** Os números aqui são os do vídeo-referência original (era CapCut/Palmier, 1.087x, legenda 46pt com contorno). Os valores **em vigor** — 1.1x, legenda 47px sem contorno com sombra-halo, split 44/56, etc. — estão em `calibracoes-e-armadilhas.md` e mandam sobre qualquer coisa deste arquivo.

## Mapa de B-rolls

| Janela (frames) | Conteúdo | Layout |
|---|---|---|
| 0–107 | Fachada de loja atual (tema apresentado) | SPLIT topo |
| 107–236 | Segundo B-roll do tema | SPLIT topo |
| 284–590 | Cena narrativa longa (escritório/burocracia) | TELA CHEIA |
| 686–744 | Continuação da cena narrativa (outro trim do mesmo vídeo) | TELA CHEIA |
| 922–1020 | Imagem estática histórica (screenshot/foto P&B) | TELA CHEIA |
| 1128–1271 | B-roll tema (vendedor) | SPLIT topo (2ª janela) |
| 1271–1441 | B-roll tema (banco) | SPLIT topo (2ª janela) |
| 1602–1864 | B-roll emocional (família feliz em casa) | TELA CHEIA (clímax) |

Fora dessas janelas: apresentador em tela cheia.

- SPLIT: no HyperFrames é `mode: "split"` no `edit-plan.json` — B-roll ocupa os 44% de cima, apresentador os 56% de baixo (`splitShiftY` enquadra o rosto)
- TELA CHEIA: `mode: "full"` — o cover-crop 9:16 é automático; `objectPosition` reenquadra quando o assunto sai da faixa visível
- No CapCut original os B-rolls de split tinham velocidade 0.5–0.8x para preencher a janela; no HyperFrames use `rate` (= duração_source / janela). **Atenção:** `rate < 1` reprova no gate de frames do `hyperframes render` — gerar a câmera lenta no próprio arquivo (`setpts`+`minterpolate`) e usar rate 1.0

## Transições light-leak (7)

Frames de início: **217, 363, 572, 724, 1000, 1422, 1844** — cada uma 21 frames, começando ~10 frames antes do ponto de corte que ela cobre. `blendMode screen`, áudio vinculado volume 0. Ficam em faixa própria acima do B-roll.

## Legendas (85 chunks no original)

Estilo (todos iguais):
```json
{"fontName": "Montserrat", "fontSize": 46, "color": "#FFFFFF",
 "borderColor": "#000000", "alignment": "center", "animation": "fadeIn",
 "transform": {"centerX": 0.5, "centerY": 0.44}}
```
Chunks de 1–4 palavras, sentence case, duração = janela da fala (5–64 frames). Exemplos reais: "O Carnê" / "que enxergou o" / "A Casas Bahia" / "pagava," / "não enxergava."

## Callouts (do original)

| Frame | Dur | Texto | Estilo |
|---|---|---|---|
| 594 | 46 | "MILHÕES\nDE BRASILEIROS" | 68pt bold, centerY 0.3, popIn |
| 712 | 29 | "CASA\nPRÓPRIA" | 68pt bold, centerY 0.3, popIn |

Colocados quando a voz fala o número/frase de impacto. Sempre na faixa MAIS ALTA.

## Mix de áudio (volumes exatos do original)

| Elemento | Janela (frames) | Volume |
|---|---|---|
| Trilha épica | 0–2040 contínua | automação -22 dB (→ -27 dB no final) |
| Intro: cinematic-opening | 0–95 | 0.25 → 0.19 |
| Intro: when-emphasizing-riser | 0–95 | 0.25 → 0.19 |
| Boom cinematic | 0–76 | 0.06 → 0.16 |
| Whoosh (pós-intro) | 90–121 | 0.35 |
| Drum-fill (virada da intro) | 187–221 | 0.166 |
| Swoosh (corte) | 217–237 | 0.095 |
| Whoosh (corte seção) | 414–427 | 0.35 |
| Swoosh | 560–589 | 0.092 |
| Whoosh (dupla) | 731–763 | 0.143 |
| Impact hit (virada) | 792–842 | 0.5 |
| Swoosh | 926–955 | 0.117 |
| Whoosh (dupla) | 1020–1051 | 0.35 |
| Swoosh | 1257–1286 | 0.056 |
| Whoosh+Swoosh | 1436–1463 | 0.083–0.085 |
| Impact (dupla, clímax) | 1555–1600 | 0.221 |
| Riser (build-up clímax) | 1637–1703 | 0.198 |
| Whoosh (CTA) | 1844–1861 | 0.149 |
| Voz | 0–2040 | 1.0 (com crossfades do J-cut) |
| Áudio original do bruto | — | 0 (mudo) |
| Áudio dos B-rolls | — | 0 (mudo) |

**Removido do formato:** percussion-ticks 0.6 sobre a fala densa (frames 427–506) — causava sensação de "áudio quebrado". Não repetir.

## J-cut (números do original)

- 43 clipes de voz (após remover 6 fillers de 1 frame) em 2 faixas: A=22, B=21
- Leads: 2–5 frames (média 4.8)
- Crossfades: 5 frames lineares em todos (fade-in e fade-out)
- Cobertura da voz: contínua 0→2040, zero buracos

## Export

- Bake mestre: H.264 1080p, 2040 frames
- Projeto final: baked a speed **1.087** → 1877 frames = 00:01:02:17 (bateu exatamente com o CapCut do usuário)
- No CapCut original o usuário usa 1.1x nos clipes; 1.087x no baked produz a mesma duração final
