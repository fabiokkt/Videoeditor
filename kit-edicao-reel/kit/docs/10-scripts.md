# Catálogo dos scripts (`modelo-projeto/scripts/` e `modelo-projeto/work/`)

Todos rodam de dentro da pasta do projeto. Origem: a cópia mais nova de cada um em 2026-10-01 (projeto
`kazuo-inamori`, que já trazia todas as correções dos reels anteriores), mais três scripts novos escritos para
o kit.

- **MOTOR** — não muda de reel para reel. Correção nele vale para todos: fazer no kit e dar `git commit`.
- **POR VÍDEO** — o código fica, os **dados** são do reel. Vêm com os dados do Kazuo Inamori como exemplo de
  preenchimento e têm que ser reescritos. Não rodar sem trocar.

## Fase 1–2 · mezanino e transcrição

| Script | Tipo | O que faz |
|---|---|---|
| `mezanino.sh` | MOTOR · **novo no kit v2** | mezanino (HDR / SDR full-range / SDR limited), voz limpa, `full.wav`, `full-clean.wav`, MD5, conferência de cor. Testado no caso SDR full-range (o de todos os brutos recentes); o ramo HDR é o comando registrado no kit v1 e não foi exercitado em 2026-10 |
| `_src.py` | MOTOR | resolve o mezanino do projeto (importado pelos scripts de olhar) |
| `regions.py [-35dB] [0.35]` | MOTOR | `silencedetect` → `work/regions.json` |
| `mkreg.py` | MOTOR | um wav por região (± 0,3 s) → `work/reg/` |
| `whisper_regs.sh` | MOTOR | whisper large-v3 por região (`~/.cache/whisper/ggml-large-v3.bin`), serial |
| `regwords.py` | MOTOR | junta em `work/region-words.json` (tempos absolutos) e imprime o texto |

## Fase 3–5 · bipe, cortes, legendas

| Script | Tipo | O que faz |
|---|---|---|
| `bipe.py` | POR VÍDEO (`JANELAS`) | grava o bipe de 1 kHz na voz do projeto e em `work/full.wav`. Lê os nomes de arquivo do plano |
| `se_splice.py` | POR VÍDEO (molde) | cola uma sílaba de outro take na voz (caso David Marquet). Só quando precisar |
| `valleys.py t1 t2 …` | MOTOR | vales de silêncio perto de um instante (para dividir região) |
| `mkcut.py` | POR VÍDEO (`SPLIT`, `DROP`) | divide regiões nos vales e marca descartes → `regions_cut.json`, `region-words-cut.json` |
| `cuts.py` | POR VÍDEO (`TAKES`, `FORCE_IN`, `FORCE_OFF`) + motor | head/tail/aout de cada take → `work/segs.json`. Constantes do formato: `HEAD_PAD`, `TAIL_PAD`, `TA`, `HH` |
| `plan_segments.py` | MOTOR | `work/segs.json` → `segments` do plano (preserva campos postos à mão) |
| `mkchunks.py` | MOTOR | 1 chunk por take do áudio limpo → `assets/chunks/` + `meta.json`. **Sem clamp** |
| `whisper_chunks.sh` | MOTOR | whisper palavra a palavra por chunk |
| `rebuild_chunk.py ch:reg[+reg]` | MOTOR | reconstrói um chunk a partir do passe por região |
| `align.py [chunks]` | MOTOR | reancora os tempos de palavra na energia real; ignora DROP; limita em `aout` |
| `captions_fix_table.py` | POR VÍDEO (`FIX`, `FIXT`) | tabela de correções por chunk e índice de palavra (`DROP` = apagar) |
| `fix_captions.py [chunks]` | MOTOR | aplica a tabela; idempotente (`work/chunks-aligned/`) |
| `tl.py [--words]` | MOTOR | timeline de cada take e de cada palavra |
| `remap_tl.py t…` | MOTOR | converte tempo de timeline de um plano antigo para o atual pelo mesmo quadro do bruto (`REMAP_OLD`) |

## Fase 6 · build e faixas

| Script | Tipo | O que faz |
|---|---|---|
| `build-edit.mjs` | MOTOR | gera a edição inteira no `index.html` a partir do plano; grava `work/mix-plan.json`, `broll-groups.json`, `leaks.json`. `--passes` gera os passes de camada para NLE |
| `bake.py [alvos]` | MOTOR | `aroll`, `voz`, `bed`, `cenas`, `brollfull`, `leaks` (sem argumento = tudo) |
| `jcut_check.py` | MOTOR | valida o J-cut por dados |
| `ritmo.py [4.0]` | MOTOR | lista intervalos sem evento na tela acima do limite |

## Fase 7 · olhar e layout

| Script | Tipo | O que faz |
|---|---|---|
| `gaze_tl.py` | MOTOR | blendshapes quadro a quadro na timeline → `gaze/tl.json` |
| `gaze_windows.py [SIDE] [DOWN]` | MOTOR | janelas de leitura → `gaze/tl-windows.json` |
| `gaze_pose.py [K]` | MOTOR | olhar compensado pela pose da cabeça → `gaze/pose-windows.json` |
| `gaze_review.py [saida]` | MOTOR | folhas grandes das janelas (REF + 5 quadros) |
| `vw_tl.py`, `vw_eyes.py`, `vw_big.py`, `vw_batch.py` | MOTOR* | faixas/zoom dos olhos para conferência. *O recorte dos olhos é do enquadramento: ajustar por bruto |
| `gaze_measure.py`, `gaze_report.py`, `gaze.py`, `grids.py`, `gaze_bounds.py`, `gaze_pairs.py`, `gaze_blend.py`, `gaze_down.py`, `gaze_lids.py` | MOTOR (geração anterior) | medidor de íris e revisões por fronteira de take; úteis em casos específicos |
| `cenas_opt.py` | POR VÍDEO (`SPLIT`, `FORCE`, `ONLYB`, `ONLYP`) + motor | DP do layout de cenas → `work/cenas-opt.json` |
| `work/layout-exemplo.py` | POR VÍDEO (molde) | layout desenhado à mão (S/B/P com tempos) |
| `slots.py [--placeholders] [--real]` | POR VÍDEO (`S`, `NOMES`) + motor | janelas de B-roll em tempo absoluto → `assets/broll-slots.json` e `plan.broll` |

## Fase 8–9 · B-roll

| Script | Tipo | O que faz |
|---|---|---|
| `gimg.mjs "consulta" [n]` | MOTOR | Google Imagens via Serper (chave no `.env`) |
| `fal_img.mjs modelo saida aspect "prompt"` | MOTOR | imagem-conceito no fal.ai — **só a pedido** |
| `work/pesq/*` | MOTOR | pesquisa e download (docs/11) |
| `pesquisa_md.py` | POR VÍDEO (textos) + motor | gera o `PESQUISAS-BROLL-<TEMA>.md` |
| `entrega.py` | POR VÍDEO (`PK`) + motor | foto escolhida por slot → recorte no aspecto do slot + folha |
| `make_broll.py [--only id,…]` | POR VÍDEO (`S`) + motor | anima a foto só com câmera → `assets/broll/` |
| `norm_broll1.py` | POR VÍDEO (molde) | normaliza vídeo entregue pelo Fabio (caso Rolex) |

## Fase 10 · export

| Script | Tipo | O que faz |
|---|---|---|
| `size_sweep.py` | MOTOR · **novo no kit v2** | escolhe o `--size`. Conferido contra o Kazuo: 432 → sobra mínima 92 quadros, como registrado |
| `render-chunks.mjs` | MOTOR | render de uma parte (`--fps --size --only K --split N`); `--join` une |
| `work/render-all.sh <SIZE> [FPS] [SPLIT]` | MOTOR · generalizado no kit v2 | todas as partes, uma por vez, com `TMPDIR` no projeto |
| `finalizar.py <saida.mp4>` | MOTOR · **novo no kit v2** | áudio final + mux + QC. Conferido contra o Kazuo: mesmos 5897 quadros, 98,283 s, 369 MB, pico −1,0 / média −19,1 dB, áudio idêntico byte a byte |
| `sync-check.mjs final16k.wav bruto16k.wav` | MOTOR | lag boca/voz por take |

## Mudanças em relação às cópias dos projetos

Só o que foi necessário para o modelo não depender de pasta ou nome de projeto:
`gimg.mjs` / `fal_img.mjs` (caminho do `.env` por `$REEL_ENV`, padrão `~/Claude/reel-auto/.env`) · `bipe.py` (nomes
de arquivo vindos do plano) · `work/render-all.sh`, `work/pesq/s.sh`, `work/pesq/pick.sh` (caminho relativo ao
script). O resto é byte a byte o que rodou no último reel. O `build-edit.mjs` do modelo, aplicado ao plano do
Kazuo, gera o mesmo `index.html` do projeto (`verificar-instalacao.sh` repete esse teste).

## Dependências

Node ≥ 20 · Python 3.9+ com `numpy`, `opencv-python` (`cv2`), `Pillow`, `mediapipe` · `ffmpeg`/`ffprobe` em
`/opt/homebrew/bin` (o `render-chunks.mjs` usa esse caminho) · `whisper-cli` + `~/.cache/whisper/ggml-large-v3.bin`.

## Scripts antigos

O pipeline `.mjs` dos primeiros reels (Havaianas, Natura, Nubank, Bariloche: `broll-gerar.mjs` com Kling/fal,
`gaze-scan.mjs`, `build-presenter.mjs`…) e variantes pontuais estão em `arquivo-projetos/<slug>/scripts/`.
Não fazem parte do fluxo atual.
