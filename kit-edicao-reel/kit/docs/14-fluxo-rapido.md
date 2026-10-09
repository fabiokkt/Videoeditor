# Fluxo rápido (kit v3) — do bruto ao MP4 em ~1 hora, com um comando

**Teste de ponta a ponta (2026-10-02, bruto do Alan Mulally):** fase1 77 s (+ mezanino ~2,5 min) · fase2 ~5,5 min
(com o aroll novo) · montar 55 s · render+finalizar 13 min · QC OK, quadros = timeline, sincronia 10 ms. O que sobra
é trabalho de leitura e autoria (cortes, legendas, olhar, cenas da camada): ~30–40 min com a biblioteca.

**Este é o fluxo padrão.** O resultado é o do reel Alan Mulally v2 (aprovado: "ficou perfeito"): o formato do kit
(capa laranja, splits, J-cut, bipe, legendas, marca só depois do nome, trilha + SFX fixos) com a camada de motion
graphics da skill `showreel-interface` por cima. Tudo que existia só para o fluxo antigo de B-roll em vídeo
(entrega.py, make_broll.py, bake de cenas, light-leak em todo corte, 2º passe do whisper por chunk) **saiu do caminho**.
Sem parada no meio: o vídeo pronto vai para o chat no fim.

## Onde o tempo foi ganho (medido no bruto do Alan Mulally, 152 s → reel de 103 s, Mac M4 16 GB)

| Etapa | Antes | Agora | Como |
|---|---|---|---|
| Transcrição por região | ~4 min | **77 s** | `large-v3-turbo` (2,3x; mesmo texto em PT) |
| 2º passe do whisper por chunk + consertos | ~5 min | **0** | `chunks_from_regions.py` usa o passe por região |
| Corte do apresentador (`aroll`) | 291 s | **102 s** | VideoToolbox (hardware) + 3 takes em paralelo; PSNR igual |
| Folha de olhar | manual, recorte errado | **automática** | `gaze_sheet.py`: recorte do rosto pelo FaceLandmarker |
| B-roll em vídeo (recorte, câmera, bake) | ~10 min | **0** | tudo na camada de motion (fotos são `<img>` no GSAP) |
| Pesquisa de imagem | serial, API ruim | **em paralelo** com a fase 1 | navegador na fonte primária (docs/11) |
| SFX do motion | ~100 cues à mão | **automático** | cada componente chama `cue()`; `mg_cues.mjs` extrai |
| Render a 60 fps | ~17 min | **~13 min** | `render-par.sh`: 3 partes em paralelo. Frio rende o dobro (27 s/parte), mas o Air M4 sem ventoinha cai para ~44 s/parte sob carga contínua; 0.8.111 com 3 workers deu o mesmo (764 s × 793 s) |

## Os comandos (de dentro de `~/Claude/reel-auto/<slug>`)

```bash
zsh ~/Claude/KIT-EDICAO-REEL/novo-projeto.sh <slug> "Título"            # 1 s
zsh scripts/fase1.sh "<bruto>" <slug>          # FUNDO · ~5 min: mezanino + whisper turbo -> work/regioes.txt
#   (kit v3.1: com >= 8 núcleos e >= 12 GB — Mac — a transcrição roda ENQUANTO o mezanino codifica; container de 4 núcleos e Air de
#    8 GB = série, medido no docs/05 §32. PARALELO=0/1 força)
#   em paralelo, NO PROCESSO PRINCIPAL: FOTOS PRIMEIRO (ver "Imagens") + imagem a pedido no Codex (docs/11, docs/05 §23)
#   escrever: scripts/mkcut.py (SPLIT/DROP) · scripts/cuts.py (TAKES) · scripts/bipe.py (JANELAS, se houver palavrão)
zsh scripts/fase2.sh                           # FUNDO · ~5 min: cortes, J-cut, chunks, legendas, faixas, olhar
#   (kit v3.1: os medidores de olhar rodam ENQUANTO o bake codifica o aroll; a tabela de legendas escrita DURANTE a fase 2
#    pede `zsh scripts/legendas.sh` + `tl.py --words > work/tl-words.txt` de novo no fim — docs/05 §29)
#   ler work/chunks.txt -> scripts/captions_fix_table.py -> zsh scripts/legendas.sh
#   ler gaze/me/g*.jpg -> janelas NÍTIDAS · ler work/tl-words.txt -> tempos de cada palavra
#   plano: sections (virada, CLIMAX, CTA), impacts (≤5; o 1º typing), ctaSeg, splitShiftY (medir: work/olhos_y.py)
#   scripts/slots.py (S, cobrindo as nítidas) · compositions/mg.html (CENAS com a biblioteca)
zsh scripts/montar.sh 13.4,16.8,...            # ~1 min: build + leaks + bed + SFX automáticos + check + snapshots
#   ler os snapshots, corrigir, repetir montar.sh
python3 scripts/size_sweep.py | head -3        # escolher o SIZE
zsh scripts/render-par.sh <SIZE> renders/<Nome>-reel-final.mp4    # FUNDO · ~13 min: 3 partes em paralelo + finalizar
#   conferir: quadros-chave, bipe no MP4, MD5 do bruto · mandar o MP4 no chat (SendUserFile)
bash work/entregas.sh <Nome>                   # FUNDO · entregas a partir do master (cópia do chat < 30 MB e HEVC final < 100 MB,
#   bitrates pela duração; a cópia do chat codifica em paralelo com o HEVC) + comparação master × final com SSIM
```

## Escrevendo a camada (`compositions/mg.html`)
O modelo já traz o CSS de todos os componentes e a **biblioteca** (não mexer): `sceneIn/sceneOut`, `splitIn/splitOut`,
`whip`, `drop`, `zoomIn`, `pop`, `flip`, `rise`, `words`, `slam`, `chip`, `smear`, `stagger`, `bars`, `digits`, `rings`,
`kenburns`, `drift`, `cue`. Cada um com som chama `cue()` sozinho. As CENAS vão no fim, com tempos absolutos de
`work/tl-words.txt`. Markup de todas as peças: `exemplos/alan-mulally/mg.html`. Regras e armadilhas: `docs/13`.

- **Splits** (capa, pré-revelação, virada) também são da camada: `.scene` com `style="height:845px"` +
  `splitIn(id, t0, true)` no quadro 0 e `splitIn/splitOut` nas janelas seguintes (sincronizados com o arrasto).
  A caixa do gancho cobre 35–56% da tela: na capa, o assunto fica no terço de cima.
- Faixa das legendas livre (y≈1380–1540). Callout só onde o motion não diz a mesma coisa.

- **Camada pela frase (reel Michael Gerber, 2026-10-08):** no `gen.py`, `T("frase", w, k)` lê o tempo no `work/tl-words.txt` e grava `work/mg/tempos.json`
  (lido pelo `slots.py`): ajuste de corte não pede reescrever tempos. Dá para desenhar e fotografar a camada ANTES do bruto com `work/mg/teste/`
  (`fake_tl.py` + `harness.html` + `shoot.mjs`) — útil quando o link do iCloud demora (docs/05 §36).

## Imagens: dosagem e capa
- **Fotos primeiro (kit v3.1).** Enquanto a fase 1 roda, no PROCESSO PRINCIPAL (subagente só com lista fechada), de dentro de
  `work/pesq/`: listar por CATEGORIA (`wmcat.py "Category:<pessoa>"`, ou várias de uma vez com `wmcatlote.py`, que honra o
  `retry-after` do 429; a busca por texto do `wm.py` volta vazia) → escolher 1–2 por slot → baixar em **fila priorizada** em tarefa de
  fundo (`wmfila.py <slug> <idx,…>`: no container o Commons libera ~1 foto por minuto, docs/05 §30–§31). Escrever o `gen.py` com as
  fotos de TODOS os slots já baixadas (ou substitutas marcadas, §31): foto provisória custa uma rodada inteira de montar + snapshots
  (reel Ridgway: −10 min). Foto que não existe: etiqueta honesta (docs/05 §29).
- **Peças prontas:** antes de desenhar uma cena, ver `docs/13` (fim) e `exemplos/matthew-ridgway/` (parede + bilhete, objeto SVG que
  rasga, lista FALTA → RESOLVIDO, contador 5.000, conversa com carimbo, anel no detalhe da foto).
- **Abertura só com fotos, motion no meio** (docs/05 §24). Fotos de arquivo: NARA/LOC/Commons (`work/pesq/`), licença registrada.
- Capa a pedido no Codex: `codex exec -m gpt-5.6-sol --skip-git-repo-check --sandbox workspace-write "<cena>" < /dev/null` (~70 s, 1536×1024).
  Assunto na metade de cima (a caixa do gancho cobre 35–56%); pessoa-tema **de costas** se o nome ainda não foi dito.

## Refazer depois de um ajuste
Mudou a camada ou o plano → `zsh scripts/montar.sh <instantes>` → **apagar `renders/chunks/chunk-NN.mp4` das partes afetadas** (o
`render-par.sh` retoma e pula as que existem) → `render-par.sh` → conferir um quadro de cada trecho mudado no MP4.

## O que continua obrigatório (é o que garante o resultado)
Varredura de olhar (folhas) · `jcut_check.py` · bipe medido · QC por snapshot de cada cena · um quadro de cada fase
do render conferido · MD5 do bruto · sem foto de banco/marca d'água. Pular qualquer um = retrabalho.

## Máquina
`render-par.sh` usa P=3 (Mac 16 GB). Mac de 8 GB: `zsh scripts/render-par.sh <SIZE> <saida> 1` (= serial antigo).
`BAKE_X264=1` volta o aroll para x264. Disco: ≥ 6 GB livres antes do render.
