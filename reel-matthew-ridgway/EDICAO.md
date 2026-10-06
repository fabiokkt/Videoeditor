# EDICAO.md — mapa do projeto (reel Matthew Ridgway)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
**Estado (2026-10-06): RENDERIZADO** — ver "Export final" no fim. Comando único sem parada, numa sessão do Claude Code **na nuvem**
(Linux, 4 núcleos, 16 GB).
Duração **96,189 s** · 28 takes · 1 bipe · 103 legendas · 5 callouts · 5 light-leaks (virada, clímax, CTA + gancho) · 11 SFX fixos + 61 da camada ·
9 slots (2 splits + 7 cenas de tela cheia na camada de motion, `work/mg/gen.py`).

## Bruto e roteiro
`~/Claude/videos-brutos/matthew-ridgway-bruto.mov` (iCloud `0capzl6CmWE1nFDYnBQXUKsyg`) — **não alterado**, MD5 `f2d11c26a63ef102c02469c41d17672f`.
HEVC 1440x2560 @60, 145,52 s, SDR full-range → mezanino full→limited; cor bruto × mezanino (14,55/72,76/130,97 s): 128,74/128,87 ·
128,01/128,02 · 128,72/128,74, desvio 58,15/58,10 · 57,90/57,88 · 57,88/57,87 — não lavou. Roteiro: ClickUp > Cronograma > "Matthew Ridgway" (v1 curto).
Onde o áudio diverge do roteiro (vale o áudio): "três dias **na** linha de frente" · "**E** você não sabe nem o nome…" · "mostrou pra ele **um** plano
de recuar" · "Ele perguntou: **o** plano de ataque?" (sem o "e"; 3 passes) · "o exército que fugia" (sem "mesmo"). Passes discordantes (vale o roteiro):
"Ele **diz** que teve que arrancar" · "passando **o mesmo** frio". "Primeiro," existe (35,16 s; o passe por região fundiu com "Resolve" → FIX + FIXT).
**O CTA "E comenta GENERAL que eu te mando o PDF." não foi gravado**: o bruto termina em "porque você é demais" (144,35 s) — sem callout de GENERAL.

## Takes descartados (mantido o ÚLTIMO válido)
r01 "Matthew andava com uma granada no peito e pregou na parede." (parou) + r02 "O primeiro é…" → r03 · r07 "resolveu antes de falar" → r08 ·
r09 "Seu vendedor tá sem computador que presta e você manda" → r10 · r14 "chefe que só aparece na festa" → r15 · r18 "…do filho do seu vendedor…"
(sem "melhor") + r19 "E você não sabe nem o…" → r20 · r22 parte 2 "O cara gaguejou sem…" → r23 · r25 "Em menos de três meses, o exército que…" → r26.

## Bipe
"porra" ("…e você manda a porra do vídeo motivacional, meu querido"): "manda a" até 64,01 · oclusão /p/ 64,02–64,07 · "o" 64,08–64,20 · "rr" 64,21–64,35 ·
"a" 64,36–64,52 · "do" a partir de 64,54. Whisper em recortes cumulativos (de 61,00): até 64,40 "…manda a aposta"; até 64,53 "…manda a porra."; de 64,54:
"do vídeo motivacional". Bipe **64,03–64,53** do source. Legenda `P****`. Apresentador em tela cheia no bipe (37,52–42,64), com o callout "SEM COMPUTADOR
QUE PRESTA.". Aceite no MP4: ver "Export final".

## J-cut
27 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9 quadros (4,9–5,4) · respiro mediano 0,245 s (3 pausas curtas emendadas no silêncio).

## Olhar
`gaze_pose.py 2.0`: 13 janelas / 3,7 s; `gaze_windows`: 13 / 5,2 s. O apresentador olha para a câmera quase o tempo todo (folhas `gaze/me/g00-g01`).
Nítidas, ambas cobertas: **2,90–3,32** (dentro do gancho: o split da capa encurta para 0–2,75 e a mesma capa abre em tela cheia com a caixa por cima) ·
**90,10–90,60** ("Cadê o plano de ataque?": retrato oficial do Ridgway em tela cheia). Pré-revelação estendida até 9,70 para cobrir a sutil 9,01–9,62.
Expostas (sutis, olho no lugar): capa 1,05–1,29 e 2,32–2,54 (dentro do split) · 22,10–22,25 · 54,77–54,99 · 70,32–70,50 · 93,71–94,02.
**Leitura exposta: 0 s** (≈1,1 s de desvio sutil). 2ª passada nos quadros da composição (16 bordas de aparição do apresentador): todas olhando a câmera.

## Split
`splitShiftY` **370** (olhos y≈1007 no mezanino em 13 pontos das janelas de split → 1377−1007; `work/olhos_y.py`). Splits: capa 0–2,75 · virada 72,29–76,51.

## Marca só depois do nome
"Matthew" em 10,86 s → revelação em 10,93 (Ridgway com a granada no suspensório, trem-hospital 1951 + "MATTHEW RIDGWAY · GENERAL · EXÉRCITO DOS EUA").
Pré-revelação: capa gerada (general de costas, sem rosto), fuzileiros na neve em Funchilin (dez/1950) e feridos de congelamento — nada do Ridgway.
Capa = **gerada a pedido** no Codex (`gpt-5.6-sol`, conta ChatGPT do Fabio por login de dispositivo; 3 códigos até o login; logout logo depois de gerar):
estrada de terra na nevasca à noite, jipe aberto com o farol âmbar, general estritamente de costas com a granada no cinto contra a luz, soldados ao
fundo (`work/capa/prompt.txt`). Sem texto, rosto, logotipo, bandeira ou insígnia. Assunto entre 6% e 48% da altura (acima da caixa do gancho).

## Camada de motion (work/mg/gen.py + work/mg/parts.py) — dosagem Deming v2
Chip "PASSO N". Motion só em: PASSO 1/2/3 (chip + título) · a parede com o bilhete ("AO COMANDANTE DAS FORÇAS INIMIGAS, COM OS CUMPRIMENTOS DO
COMANDANTE DO 8º EXÉRCITO.") e a calça de pijama listrada que cai, é pregada e rasga no fundilho · a lista do que faltava (LUVA, COMIDA QUENTE,
ENVELOPE: FALTA → RESOLVIDO; ATACAR: DEPOIS) · 5.000 SOLDADOS RECONHECIDOS DE CARA · a conversa da virada (PLANO DE RECUO, "O PLANO DE ATAQUE?",
"SENHOR, A GENTE TÁ RECUANDO.", DIAS DEPOIS, carimbo FORA) (≈40% da cobertura). O resto é foto real (Exército/USMC/NARA, domínio público).
Clímax: a coluna na neve da abertura volta em "o exército que fugia" (+ MENOS DE 3 MESES) → tanque no rio Han, fev/1951 ("1951 · A CONTRAOFENSIVA":
não existe no Commons foto da retomada de Seul; etiqueta honesta).
Callouts: 1º digitado "TÁ / ABANDONADO." (seg 1) · "PALESTRA / MOTIVACIONAL." (3) · "SEM COMPUTADOR / QUE PRESTA." (9) · "É CONVIDADO." (13) ·
"NEM O NOME / DO FILHO." (18).

> **Regra de ouro: nunca editar `index.html` à mão.**
```
editar assets/edit-plan.json (ou scripts/slots.py) -> python3 work/mg/gen.py -> zsh scripts/montar.sh <instantes>
(cortes: scripts/mkcut.py / cuts.py -> zsh scripts/fase2.sh · legendas: scripts/captions_fix_table.py -> zsh scripts/legendas.sh)
```

## Onde mexer em cada coisa

| Quero mudar… | Arquivo |
|---|---|
| cortes / takes (in/out) | `scripts/mkcut.py` (divisões/descartes) → `scripts/cuts.py` (lista TAKES, FORCE_IN/FORCE_OFF) → `work/segs.json` → `python3 scripts/plan_segments.py` |
| texto de legenda | `scripts/captions_fix_table.py` (FIX/FIXT por chunk e índice de palavra) → `zsh scripts/legendas.sh` |
| callouts | `impacts` no plano (frase, seg, linhas, hold, `top` opcional; o 1º com `style: typing`) |
| janelas de cobertura | `scripts/slots.py` (lista S, tempos absolutos; MG="*") → `zsh scripts/montar.sh` |
| fotos / cenas da camada | `work/mg/gen.py` (F = foto por papel, OP = enquadramento, CENAS) e `work/mg/parts.py` (CSS, calça SVG) |
| enquadramento do split | `splitShiftY` (medido: 370 — `work/olhos_y.py`) |
| zoom do apresentador | `presenterZoom` (1,06/1,14, uma troca por aparição; `sceneMax` 4,5) |
| transições | `sections` (após os segs 18, 23, 26) e `leakMinGap` (3,5) no plano |
| bipe | `scripts/bipe.py` (JANELAS 64,03–64,53 s do source) → `bake.py voz` |
| respiro / lead do J-cut | `TA`/`HH` em `scripts/cuts.py`; `jcutLeadFrames` (9) / `jcutCrossfadeFrames` (3) |
| tempos de timeline / palavra | `python3 scripts/tl.py [--words]` |

## Export final

`size_sweep.py`: `--size` **444** (13 partes, sobra mínima 147 quadros) · `render-par.sh 444 … 2` (2 em paralelo, 4 núcleos) · 0 falhas · **1417 s** (~3,7 min por par).
**Master:** `renders/Matthew-Ridgway-reel-final.mp4` — 1440×2560 · 60 fps · 96,20 s · 5772 quadros (= timeline) · 250 MB (fora do git).
QC (`finalizar.py`): quadros = timeline OK · pico −0,8 dB / média −19,6 dB · trechos pretos 0 · bipe no MP4 98,7% em 950–1050 Hz (39,94–40,41 s;
o resto é a trilha por baixo; na `voz-mix.m4a` 100%) · sincronia boca/voz lag mediano 10 ms (27/28 pontos com r > 0,6; faixa 0–20 ms) · bruto intacto
(MD5 antes e depois `f2d11c26a63ef102c02469c41d17672f`). Quadro a quadro: 64 quadros do MP4 (um por cena/transição) conferidos; quadro 0 = capa.
**Entregas (a partir do master, `work/entregas.sh`):** `entrega/Matthew-Ridgway-reel-chat.mp4` (x264 dois passes 2,0 Mbps, AAC 160k) ·
`entrega/Matthew-Ridgway-reel-final.mp4` (HEVC libx265 dois passes **7,6 Mbps** — reel de 96,2 s > ~95 s —, `hvc1`, AAC 256k, `+faststart`) ·
`entrega/comparacao-master-x-hevc.jpg` (quadro 768 = 12,80 s, master × HEVC). Final: **95,3 MB**, 7,65 Mbps de vídeo, 5772 quadros, `moov` antes do `mdat`; SSIM do vídeo inteiro **0,994**. Cópia do chat: 26,6 MB.

## Correções depois do render

- (nenhuma)

## Lições para o kit

Levadas para `KIT-EDICAO-REEL/docs/05` §29 (+ `work/olhos_y.py` no modelo):
- Olhada no gancho: split curto + a mesma capa abrindo em tela cheia com a caixa por cima (leitura exposta 0).
- `work/olhos_y.py` mede o `splitShiftY`.
- Commons no container: listar categoria (não buscar texto) e baixar miniatura só em largura padrão (960/1280/1920); subagente com escopo fechado.
- Foto que não existe (Seul, mar/1951): etiqueta honesta; a foto da revelação tem que provar a fala (a granada), anel com Ken Burns no container.
- CTA de palavra-chave não gravado pelo 2º reel seguido.
- `legendas.sh` roda dentro da fase 2: rodar de novo se a tabela for escrita durante ela.
