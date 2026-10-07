# EDICAO.md — mapa do projeto (reel Stanley McChrystal)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
**Estado (2026-10-07): RENDERIZADO** — ver "Export final" no fim. Comando único sem parada, numa sessão do Claude Code **na nuvem**
(Linux, 4 núcleos, 16 GB).
Duração **93,39 s** · 25 takes · 1 bipe · 89 legendas · 5 callouts · 4 light-leaks (virada, clímax, CTA + gancho) · 11 SFX fixos + 69 da camada ·
8 slots (2 splits + 6 cenas de tela cheia na camada de motion, `work/mg/gen.py`).

## Bruto e roteiro
`~/Claude/videos-brutos/stanley-mcchrystal-bruto.mov` (iCloud `03bmoRZZJYs86J8Q8tsASiOdw`) — **não alterado**, MD5 `c0c3c7c7406929e053457684f0bc1b3e`.
HEVC 1440x2560 @60, 178,80 s, SDR full-range → mezanino full→limited; cor bruto × mezanino (17,88/89,40/160,92 s): 130,60/130,68 ·
129,81/129,78 · 131,98/132,02, desvio 65,05/65,04 · 65,53/65,52 · 66,76/66,75 — não lavou. Roteiro: ClickUp > Cronograma > "Stanley McChrystal" (v1).
Onde o áudio diverge do roteiro (passe por região e por chunk concordam; vale o áudio): "pra provar que **seu** comercial e **sua** operação" ·
"parar de ser **juiz**" (sem "o") · "Reunião de vendas sem **operação**" (sem "a"). Passes discordantes ou homófono (vale o roteiro): "**Seu** melhor
vendedor" (whisper "Se o") · "Não **o** encostado" (região "Não encostado", chunk "Não um encostado") · "Ele juntou soldado e analista" (região com "o").
Com o roteiro no `--prompt`, o whisper alucinou em 3 de 6 chunks ("Primeiro,", "Segundo,", "A venda foi de trânsito…"): não serve de juiz.
**Os CTAs de palavra-chave não foram gravados** (nem o do meio nem o do fim, "Comenta BRIGA que eu te mando o protocolo completo no direct."):
o bruto vai de "meu querido" (119,91 s) direto para "e a virada" (120,50 s) e termina em "porque você é demais!" (177,44 s) — sem callout de BRIGA.

## Takes descartados (mantido o ÚLTIMO válido)
r02 "Stanley como…" → r03 · r06 fim + r07 "Ele disse que time excelente trabalhando separado." (sem "perde") → r08+r09 ("…separado… perde", pausa
dramática = um take) · r13 "…para de ser…" → r14 · r15 "Seu melhor vendedor passa uma semana na…" → r16 · r19 fim, r20 (completo), r21 "…vê a porra…",
r22 (sem "a porra do" e sem "meu querido"), r23 → **r24** · r26 "…a vida de ma…" → r27 · r28 "Lá, tudo em…" + r29 "Lá." + r30 "E a tudo…" → r31 ·
r31 fim "Ele juntou o soldado e a analista, e a oper…" + r32 + r33 "pra trezentas" (sem "mais de") → r34 · r35 "A venda de ontem…" → r36.

## Bipe
"porra" ("…antes de prometer a porra do prazo, meu querido."): "prometer a" até 118,33 · oclusão /p/ 118,40–118,50 · explosão 118,51 · "o" 118,52–118,63 ·
"rr" 118,64–118,67 · "a" 118,68–118,76 · "do" a partir de 118,77. Whisper em recortes cumulativos (de 115,00): até 118,50 "…antes de prometer a"; até 118,77
"…a porra"; de 118,78: "do prazo, meu querido." (de 118,65 ainda ouve "Porra"). Bipe **118,44–118,77** do source. Legenda `P****` (FIXT 118,44).
Apresentador em tela cheia no bipe (63,01–67,63). Aceite no MP4: ver "Export final".

## J-cut
24 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9 quadros · respiro mediano 0,245 s.

## Olhar
`gaze_pose.py 2.0`: 21 janelas / 4,5 s; `gaze_windows`: 43 / 19,3 s. O apresentador olha para a câmera o tempo todo (folhas `gaze/me/g00-g04`):
**nenhuma leitura nítida** — só piscadas e olhadas sutis para baixo. Cobertas pela camada: 13,34–14,53 · 15,98–16,16 · 32,48–32,66 · 46,00–46,64 ·
50,14–50,44 · 56,82–58,64 · 70,42–70,61 · 76,80–77,13 ("ninguém lia") · 79,29–83,54. Expostas (sutis): 23,97–24,42 (o gesto do apito no "juiz da briga":
lábios em bico, olho baixo — fica no apresentador, com o callout) · 66,46–66,65 ("meu querido", no bipe) · 11,05–11,48 · 38,91–39,09 · 53,80–53,95 ·
65,22–65,50 · 84,70–87,91 · 91,93–92,50. **Leitura exposta: 0 s** (≈1,5 s de desvio sutil/piscada).

## Split
`splitShiftY` **375** (olhos y≈1003 no mezanino em 12 pontos das janelas de split → 1377−1002; `work/olhos_y.py`). Splits: capa 0–5,19 (o gancho
inteiro, sem olhada) · virada 67,63–69,70.

## Marca só depois do nome
"Stanley" em 11,74 s → revelação em 11,81 (retrato de 2003 no Pentágono + "STANLEY McCHRYSTAL · GENERAL · EXÉRCITO DOS EUA" + "FORÇAS ESPECIAIS ·
IRAQUE"). Último quadro limpo 11,78 (apresentador), primeiro com o Stanley 11,86. Pré-revelação: capa gerada (general de costas, sem rosto nem insígnia),
visão noturna (exercício de operações especiais com Chinook; soldado em missão noturna no Iraque) — nada do Stanley.
Capa = **gerada a pedido** no Codex (`gpt-5.6-sol`, conta ChatGPT do Fabio por login de dispositivo — 1 código, login em ~2 min; logout logo depois de gerar):
corredor de concreto em visão noturna verde, soldados de capacete carregando sacos de lona, porta entreaberta para o quartinho com sacos até o teto sob uma
lâmpada, general de costas no primeiro plano (`work/capa/prompt.txt`). Sem texto, rosto, logotipo, bandeira ou insígnia. Assunto entre 5% e 48% da altura.
A mesma capa volta no split da virada ("E a virada foi um quartinho"), com a câmera entrando na porta (Ken Burns 1 → 1,25 com origem na porta).

## Camada de motion (work/mg/gen.py + work/mg/parts.py) — dosagem Deming v2
Chip "PASSO N". Motion só em: PASSO 1/2/3 (chip + título: NA MESMA REUNIÃO · EMPRESTA O MELHOR · ABRE TUDO) · as lanchonetes da base (BURGER KING,
PIZZA HUT, SUBWAY: ABERTO → PROIBIDO; sem logotipo — não há foto livre) · a reunião diária (99 telas de videochamada + 7.000 PESSOAS + 1 REUNIÃO POR DIA) ·
a frase dele sobre o retrato de 4 estrelas ("A META É TODO MUNDO SABER TUDO, O TEMPO TODO." — Stanford GSB) · o quartinho (18 sacos caem e empilham sob a
lâmpada, carimbo NINGUÉM LIA) · o clímax (barras ANTES 18 × DEPOIS 300+, OPERAÇÕES POR MÊS) (≈40% da cobertura). O resto é foto real (Exército/DoD, domínio
público): retrato de 2003, no C-130 com o laptop (4 HORAS DE SONO · 1 REFEIÇÃO POR DIA), dois times separados (sala de operações × incursão noturna) com
carimbo PERDE, um time em roda (OS MELHORES · 6 MESES NO OUTRO TIME), Stanley agachado com um soldado afegão, incursões noturnas no Iraque, Stanley e Flynn
(chefe de inteligência) na mesa (SOLDADO + ANALISTA).
Callouts: 1º digitado "ELES SÓ NÃO / SE CONHECEM." (seg 2) · "JUIZ DA / BRIGA." (5) · "SÓ GENTE / PROMETENDO PRAZO." (9) · "NÃO O / ENCOSTADO." (14) ·
"OU TÁ / NO SACO?" (23).

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
| fotos / cenas da camada | `work/mg/gen.py` (F = foto por papel, OP = enquadramento, CENAS) e `work/mg/parts.py` (CSS, grade, sacos) |
| enquadramento do split | `splitShiftY` (medido: 375 — `work/olhos_y.py`) |
| zoom do apresentador | `presenterZoom` (1,06/1,14, uma troca por aparição; `sceneMax` 4,5) |
| transições | `sections` (após os segs 17, 20, 23) e `leakMinGap` (3,5) no plano |
| bipe | `scripts/bipe.py` (JANELAS 118,44–118,77 s do source) → `bake.py voz` |
| respiro / lead do J-cut | `TA`/`HH` em `scripts/cuts.py`; `jcutLeadFrames` (9) / `jcutCrossfadeFrames` (3) |
| tempos de timeline / palavra | `python3 scripts/tl.py [--words]` |

## Export final

`size_sweep.py`: `--size` **432** (13 partes, sobra mínima 139 quadros) · `render-par.sh 432 … 2` (2 em paralelo, 4 núcleos) · 0 falhas · **1398 s** (~3,6 min por par).
Depois do QC quadro a quadro, refeitas só as partes 1 e 4 (**293 s**): o chicote da pré-revelação mostrava o apresentador por 2–3 quadros (7,86 s; a cena
não tinha mundo escuro) e a grade de telas entrava vazia (o `finalizar.py` acusou "trechos pretos 30,45–30,68", QC COM PROBLEMA). Depois: QC OK.
**Master:** `renders/Stanley-McChrystal-reel-final.mp4` — 1440×2560 · 60 fps · 93,40 s · 5604 quadros (= timeline) · 237 MB (fora do git).
QC (`finalizar.py`): quadros = timeline OK · pico −0,8 dB / média −17,7 dB · trechos pretos 0 · bipe no MP4 98,6% em 950–1050 Hz (65,93–66,19 s;
o resto é a trilha por baixo; na `voz-mix.m4a` 100%) · sincronia boca/voz lag mediano 10 ms (25/25 pontos com r > 0,6; o seg 2, de 1,34 s, deu −140 ms
porque a janela de 1,2 s do `sync-check.mjs` invade o take seguinte — medido dentro do segmento: 10 ms, r 0,97) · bruto intacto (MD5 antes e depois
`c0c3c7c7406929e053457684f0bc1b3e`). Quadro a quadro: 80 quadros do MP4 (um por cena/transição) + 8 dos trechos refeitos; quadro 0 = capa.
**Entregas (a partir do master, `work/entregas.sh`):** `entrega/Stanley-McChrystal-reel-chat.mp4` (x264 dois passes 2,0 Mbps, AAC 160k, 25,6 MB) ·
`entrega/Stanley-McChrystal-reel-final.mp4` (HEVC libx265 dois passes **8 Mbps** — reel de 93,4 s < ~95 s —, `hvc1`, AAC 256k 48 kHz, `+faststart`) ·
`entrega/comparacao-master-x-hevc.jpg` (quadro 780 = 13,00 s, master × HEVC). Final: **95,8 MB**, 7,93 Mbps de vídeo, 5604 quadros, `moov` antes do `mdat`;
SSIM do vídeo inteiro **0,994**. Encode das entregas: 18 min (4 núcleos).

## Correções depois do render

- (nenhuma)

## Lições para o kit

Levadas para `KIT-EDICAO-REEL/docs/05` §30 (+ `work/pesq/wmcat.py` no modelo e a linha dele em `docs/11`):
- Commons no container a ~1 foto/min (429 "robot policy" com qualquer UA): listar por categoria (`wmcat.py`), fila por prioridade em arquivo, sem `pkill -f`.
- Whisper com o roteiro no `--prompt` alucina: o juiz é região + chunk sem prompt.
- Bipe: o vão depois do artigo é a oclusão do /p/.
- Olho baixo num gesto pedido pelo roteiro (o apito) não é leitura.
- Dupla na mesa vai em card paisagem; foto clara leva `.floor`; visão noturna sem `dim`.
- Toda cena de tela cheia com mundo escuro (chicote mostrava o apresentador); peça que nasce invisível sobre o escuro gera "trecho preto" no QC.
- `.cap` colide com as legendas do host; marca sem foto livre vira lista de UI; `sync-check` em take curto mede o take vizinho.
- CTA de palavra-chave não gravado pela 4ª vez seguida.
