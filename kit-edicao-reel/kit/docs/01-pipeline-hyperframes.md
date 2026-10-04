# Pipeline — do bruto ao MP4 (estado de 2026-10-01)

O fluxo como ele é feito hoje, fase a fase, com os comandos. Os números e os porquês estão em `docs/05`; o
catálogo dos scripts em `docs/10`. Tudo roda de dentro da pasta do projeto (`~/Claude/reel-auto/<slug>`).

```
bruto ─► mezanino + voz ─► transcrição por região ─► bipe ─► takes/cortes ─► chunks + legendas
      ─► plano + build + bake ─► varredura de olhar ─► layout + placeholders ─► pesquisa de B-roll
      ─► ■ PARADA ÚNICA ■ ─► B-rolls reais ─► 2ª varredura + QC ─► render em partes ─► finalizar ─► entrega
```

Três regras que atravessam tudo: **nunca editar `index.html` à mão** · **uma tarefa pesada por vez** (Air de
8 GB) · **o bruto nunca é alterado**.

---

## Fase 0 — Projeto

```bash
zsh ~/Claude/KIT-EDICAO-REEL/novo-projeto.sh <slug> "Título"
cd ~/Claude/reel-auto/<slug>
```
Cria o projeto a partir de `modelo-projeto/` + `assets-fixos/` (scripts, template, fontes, SFX, trilha,
light-leak, modelo do FaceLandmarker). Os scripts **POR VÍDEO** vêm com os dados do reel Kazuo Inamori como
exemplo e são reescritos ao longo das fases (lista em `docs/10`).

## Fase 1 — Mezanino e voz  *(sozinho, sem nada pesado em paralelo)*

```bash
zsh scripts/mezanino.sh "$HOME/Claude/videos-brutos/<Bruto>.MP4" <slug>
```
Gera `assets/<slug>-2560-sdr.mp4`, `assets/<slug>-voz.m4a`, `work/<slug>-voz-limpa.m4a`, `work/full.wav`,
`work/full-clean.wav`, `work/md5-bruto.txt` e imprime a conferência de cor (média/desvio bruto × mezanino).

## Fase 2 — Transcrição por região  *(só depois que o mezanino terminou)*

```bash
python3 scripts/regions.py            # silencedetect -35dB / 0.35 -> work/regions.json
python3 scripts/mkreg.py              # um wav por região -> work/reg/
zsh scripts/whisper_regs.sh           # whisper large-v3 por região; imprime json/wav no fim: os números têm que bater
python3 scripts/regwords.py           # work/region-words.json + o texto de cada região
```
Ler o texto das regiões contra o roteiro: takes repetidos, falsos inícios, palavrões.

## Fase 3 — Bipe  *(se houver palavrão; antes dos cortes)*

Mapear a palavra (whisper em recortes cumulativos + envelope/espectro), preencher `JANELAS` em
`scripts/bipe.py` e rodar. Ele grava o bipe em `assets/<slug>-voz.m4a` e em `work/full.wav`. Aceite por medição
depois do `bake.py voz` (docs/05 §9).

## Fase 4 — Takes e cortes

```bash
python3 scripts/valleys.py 8.2 15.5 …   # vales de silêncio perto dos pontos onde uma região deve ser dividida
python3 scripts/mkcut.py                # SPLIT/DROP  -> work/regions_cut.json + region-words-cut.json
python3 scripts/cuts.py                 # TAKES       -> work/segs.json (in, out, aout de cada take)
python3 scripts/plan_segments.py        # copia os takes para `segments` do edit-plan.json
```
`cuts.py` lê `rate` e `jcutLeadFrames` do plano (o esqueleto já vem com 1,1 / 9 / 3).

## Fase 5 — Chunks e legendas

```bash
python3 scripts/mkchunks.py             # 1 chunk por take -> assets/chunks/chNN.wav + meta.json
zsh scripts/whisper_chunks.sh           # palavra a palavra por chunk
mkdir -p work/chunks-raw && cp assets/chunks/ch*-words.json work/chunks-raw/
python3 scripts/rebuild_chunk.py 3:5 7:9+10 …   # chunk:região_cut — onde o passe por chunk vazou/alucinou/colapsou
python3 scripts/align.py                # reancora os tempos na energia real
python3 scripts/fix_captions.py         # aplica scripts/captions_fix_table.py (FIX / DROP / FIXT)
```

## Fase 6 — Plano, build e faixas

Preencher no `assets/edit-plan.json`: `sections` (cortes de seção; a do clímax com "CLIMAX" no nome), `impacts`
(callouts; o 1º `style: typing`), `ctaSeg`, `hookSeg`.

```bash
node scripts/build-edit.mjs             # index.html + work/mix-plan.json + work/broll-groups.json + work/leaks.json
python3 scripts/bake.py voz bed aroll   # faixas prontas
python3 scripts/jcut_check.py           # 0 buracos · nenhum crossfade sobre fala · lead de fala ~5 quadros
python3 scripts/tl.py --words           # timeline de cada take e de cada palavra (acha a 1ª menção do nome)
```

## Fase 7 — Varredura de olhar (1ª passada) e layout

```bash
python3 scripts/gaze_tl.py && python3 scripts/gaze_windows.py     # janelas de leitura na timeline
python3 scripts/gaze_pose.py 2.0                                  # se ele mexe muito a cabeça: resíduo olho × pose
python3 scripts/gaze_review.py                                    # folhas de conferência -> gaze/rev/
python3 scripts/vw_eyes.py gaze/duvida.jpg 8.27 27.72 …           # zoom nos pontos em dúvida
python3 scripts/cenas_opt.py                                      # ponto de partida do layout (ou à mão)
python3 scripts/slots.py --placeholders                           # S/NOMES -> plan.broll com cartões rotulados
node scripts/build-edit.mjs && python3 scripts/bake.py cenas brollfull leaks bed
```
Depois: medir o `splitShiftY`, conferir a capa em t=0 e o ritmo (`python3 scripts/ritmo.py`), `npm run check`.

## Fase 8 — Pesquisa de B-roll

Ferramentas em `work/pesq/` (docs/11). Saída: candidatas em `work/pesq/cand/`, `candidates.json`,
`picks.json` e o arquivo `PESQUISAS-BROLL-<TEMA>.md` (`scripts/pesquisa_md.py`).

## ■ PARADA ÚNICA

Preview no ar (`npx hyperframes preview --background`), **link no topo da mensagem**, e a lista do que trava o
tempo: duração · cortes · velocidade · J-cuts · palavrões e bipe · varredura de olhar · primeira cena ·
B-rolls por slot. Não gerar B-roll antes da resposta.

## Fase 9 — B-rolls reais

```bash
python3 scripts/entrega.py              # PK: foto por slot + recorte -> assets/broll-src/entrega/
python3 scripts/make_broll.py           # S: movimento de câmera por slot -> assets/broll/   (--only sNN regera um)
python3 scripts/slots.py --real
node scripts/build-edit.mjs && python3 scripts/bake.py cenas brollfull leaks bed
npm run check
```
Com os snapshots: definir `capLowSegs` e `impacts[].top`, conferir a revelação quadro a quadro (último limpo /
primeiro com marca), a capa, o ritmo, e fazer a **2ª varredura de olhar** nos quadros da composição.

## Fase 10 — Export

```bash
python3 scripts/size_sweep.py                         # escolhe o --size (sobra mínima de clipe por pedaço)
npx hyperframes preview --stop                        # libera RAM
zsh work/render-all.sh <SIZE>                         # COMO TAREFA DE FUNDO do harness; retoma de onde parou
python3 scripts/finalizar.py renders/<Nome>-reel-final.mp4
```
`finalizar.py` monta o áudio (limiter a −1 dBTP), faz o mux e o QC básico. À parte: bipe no MP4, quadros-chave
× preview, `sync-check.mjs`, MD5 do bruto.

## Fase 11 — Entrega e fechamento

Mensagem com o link do preview e o resumo (arquivo, duração, resolução, fps, validação, áudio, B-roll por slot,
callouts, decisões). Preencher o `EDICAO.md` do projeto e levar as **"Lições para o kit"** para `docs/05` e para
`modelo-projeto/scripts/` (com `git commit` no kit).

## Correção depois do render

- **Não muda o tempo** (B-roll, texto, cor, volume): corrigir → build → bake dos alvos → apagar só as partes
  afetadas em `renders/chunks/` → `zsh work/render-all.sh <SIZE>` (mesmo SIZE) → `finalizar.py`.
- **Muda o tempo** (corte, velocidade, J-cut, ordem): avisar que é render inteiro; guardar o plano antigo em
  `work/vN/`, remapear os slots com `remap_tl.py`, refazer chunks/legendas, apagar todas as partes.

---

## O contrato: `assets/edit-plan.json`

| Campo | O que faz |
|---|---|
| `fps` | fps da **timeline** (30). O arquivo final sai a 60 |
| `rate` | velocidade global: vídeo por `setpts`, voz por `atempo` (tom preservado) |
| `jcutLeadFrames` / `jcutCrossfadeFrames` | 9 / 3 (docs/05 §7) |
| `src` / `voiceSrc` | mezanino / voz dedicada (com bipe) |
| `segments[]` | `in`, `out`, `aout`, `label`, `chunk` (vêm do `plan_segments.py`); `videoTail` opcional (L-cut) |
| `sections[]` | `afterSegment`, `name` — light-leak no corte; "CLIMAX" no nome dispara riser + impact-hit |
| `broll[]` | `mode` (`split`/`full`), `fromSeg`, `toSeg`, `span` [f0,f1], `file`; opcionais `preStart`, `objectPosition`. Escrito por `slots.py` |
| `impacts[]` | `phrase` (como está na legenda, sem acento/pontuação), `seg`, `lines`, `hold`, `style` (`typing` no 1º), `top` (%) |
| `presenterZoom` | `scales`, `mode: scene`, `sceneMax`, `maxHold`, `origin` |
| `leakMinGap` | intervalo mínimo entre transições (3,5) |
| `hookSeg` | segmento do gancho/capa (0; `null` desliga) |
| `capLowSegs` | segmentos com legenda a 76% sobre B-roll de tela cheia |
| `splitShiftY` | deslocamento vertical do apresentador no split — medir |
| `ctaSeg` | 1º segmento do encerramento (push-in) |
| `trilhaVol`, `trilhaLoop` | volume da trilha (0,079); emenda quando o reel passa de 164 s (`at`, `back`, `xfade`) |
| `bakedAroll`, `bakedAudio`, `bakedBroll`, `bakedLeaks` | faixas pré-renderizadas (sempre `true`) |
| `brollKenBurns` | `false` (o `make_broll.py` já grava a câmera) |
| `yellowCapSegs` | LEGADO — caixa amarela no gancho (só com `hookSeg: null`) |

`build-edit.mjs` lê também `assets/chunks/meta.json` e `assets/chunks/chNN-words.json` — sem eles quebra — e
termina com `OK: N segs, Xs, N cenas de broll (N tomadas), N sfx, N legendas, N callouts, N leaks, J-cut 9f/3f.`
