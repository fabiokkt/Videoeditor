# Código do motor — `modelo-projeto/` na íntegra

O esqueleto que todo reel novo copia: template da composição, biblioteca da camada de motion, plano-esqueleto e todos os scripts. Catálogo (MOTOR × POR VÍDEO) em `docs/10-scripts.md`. Os scripts POR VÍDEO trazem dados de outro reel como exemplo.

_kit em 47e642e · v3.1: dosagem foto x motion (reel Deming), exemplo Deming, instalador e guia para outro computador, showreel-interface no kit · gerado em 2026-10-04_

## Índice

- `novo-projeto.sh`
- `instalar.sh`
- `verificar-instalacao.sh`
- `modelo-projeto/CLAUDE.md`
- `modelo-projeto/package.json`
- `modelo-projeto/hyperframes.json`
- `modelo-projeto/meta.json`
- `modelo-projeto/assets/edit-plan.json`
- `modelo-projeto/index.html`
- `modelo-projeto/compositions/mg.html`
- `modelo-projeto/scripts/fase1.sh`
- `modelo-projeto/scripts/fase2.sh`
- `modelo-projeto/scripts/legendas.sh`
- `modelo-projeto/scripts/montar.sh`
- `modelo-projeto/scripts/render-par.sh`
- `modelo-projeto/scripts/build-edit.mjs`
- `modelo-projeto/scripts/bake.py`
- `modelo-projeto/scripts/render-chunks.mjs`
- `modelo-projeto/scripts/finalizar.py`
- `modelo-projeto/scripts/_src.py`
- `modelo-projeto/scripts/align.py`
- `modelo-projeto/scripts/bipe.py`
- `modelo-projeto/scripts/captions_fix_table.py`
- `modelo-projeto/scripts/cenas_opt.py`
- `modelo-projeto/scripts/chunks_from_regions.py`
- `modelo-projeto/scripts/cuts.py`
- `modelo-projeto/scripts/entrega.py`
- `modelo-projeto/scripts/fal_img.mjs`
- `modelo-projeto/scripts/fix_captions.py`
- `modelo-projeto/scripts/gaze.py`
- `modelo-projeto/scripts/gaze_blend.py`
- `modelo-projeto/scripts/gaze_bounds.py`
- `modelo-projeto/scripts/gaze_down.py`
- `modelo-projeto/scripts/gaze_lids.py`
- `modelo-projeto/scripts/gaze_measure.py`
- `modelo-projeto/scripts/gaze_pairs.py`
- `modelo-projeto/scripts/gaze_pose.py`
- `modelo-projeto/scripts/gaze_report.py`
- `modelo-projeto/scripts/gaze_review.py`
- `modelo-projeto/scripts/gaze_sheet.py`
- `modelo-projeto/scripts/gaze_tl.py`
- `modelo-projeto/scripts/gaze_windows.py`
- `modelo-projeto/scripts/gimg.mjs`
- `modelo-projeto/scripts/grids.py`
- `modelo-projeto/scripts/jcut_check.py`
- `modelo-projeto/scripts/make_broll.py`
- `modelo-projeto/scripts/mezanino.sh`
- `modelo-projeto/scripts/mg_cues.mjs`
- `modelo-projeto/scripts/mg_sfx.py`
- `modelo-projeto/scripts/mkchunks.py`
- `modelo-projeto/scripts/mkcut.py`
- `modelo-projeto/scripts/mkreg.py`
- `modelo-projeto/scripts/norm_broll1.py`
- `modelo-projeto/scripts/pesquisa_md.py`
- `modelo-projeto/scripts/plan_segments.py`
- `modelo-projeto/scripts/rebuild_chunk.py`
- `modelo-projeto/scripts/regions.py`
- `modelo-projeto/scripts/regwords.py`
- `modelo-projeto/scripts/remap_tl.py`
- `modelo-projeto/scripts/ritmo.py`
- `modelo-projeto/scripts/se_splice.py`
- `modelo-projeto/scripts/size_sweep.py`
- `modelo-projeto/scripts/slots.py`
- `modelo-projeto/scripts/sync-check.mjs`
- `modelo-projeto/scripts/tl.py`
- `modelo-projeto/scripts/valleys.py`
- `modelo-projeto/scripts/vw_batch.py`
- `modelo-projeto/scripts/vw_big.py`
- `modelo-projeto/scripts/vw_eyes.py`
- `modelo-projeto/scripts/vw_tl.py`
- `modelo-projeto/scripts/whisper_chunks.sh`
- `modelo-projeto/scripts/whisper_regs.sh`
- `modelo-projeto/work/layout-exemplo.py`
- `modelo-projeto/work/mg-cues-auto.json`
- `modelo-projeto/work/render-all.sh`
- `modelo-projeto/work/pesq/crawl.py`
- `modelo-projeto/work/pesq/dl.py`
- `modelo-projeto/work/pesq/filt.py`
- `modelo-projeto/work/pesq/pick.sh`
- `modelo-projeto/work/pesq/s.sh`
- `modelo-projeto/work/pesq/sheet.py`
- `modelo-projeto/work/pesq/wm.py`
- `modelo-projeto/work/pesq/wmpick.py`


---

# ARQUIVO: `novo-projeto.sh`

```bash
#!/bin/zsh
# Cria um projeto de reel a partir do kit — sem depender de nenhum projeto antigo.
# uso: zsh novo-projeto.sh <slug> ["Título do reel"]
#   ex.: zsh ~/Claude/KIT-EDICAO-REEL/novo-projeto.sh kazuo-inamori "Kazuo Inamori"
# Destino: ~/Claude/reel-auto/<slug>  (outra pasta: REEL_DIR=/caminho zsh novo-projeto.sh ...)
set -e
KIT="${0:A:h}"
SLUG="$1"; TITULO="${2:-$1}"
[[ "$SLUG" =~ ^[a-z0-9][a-z0-9-]*$ ]] || { echo 'uso: zsh novo-projeto.sh <slug-em-minusculas-com-hifen> ["Título"]'; exit 1; }
DEST="${REEL_DIR:-$HOME/Claude/reel-auto}/$SLUG"
[ -e "$DEST" ] && { echo "já existe: $DEST"; exit 1; }
mkdir -p "$DEST"
cp -R "$KIT/modelo-projeto/." "$DEST/"
A="$KIT/assets-fixos"
mkdir -p "$DEST/assets/fonts" "$DEST/assets/sfx" "$DEST/.models"
cp "$A"/fonts/*.woff2 "$DEST/assets/fonts/"
cp "$A"/sfx/* "$DEST/assets/sfx/"
cp "$A/fx/transicao-light-leak.mp4" "$A/trilha/trilha-epic-cinematic-corporate.mp3" "$DEST/assets/"
cp "$A/models/face_landmarker.task" "$DEST/.models/"
mkdir -p "$DEST"/{assets/chunks,assets/broll,assets/broll-src/entrega,work/reg,work/pesq/raw,work/pesq/q,work/pesq/cand,gaze,renders/chunks,snapshots}
HOJE=$(date +%Y-%m-%d)
for f in package.json meta.json index.html assets/edit-plan.json EDICAO.md; do
  sed -i '' -e "s|__SLUG__|$SLUG|g" -e "s|__TITULO__|$TITULO|g" -e "s|__DATA__|$HOJE|g" "$DEST/$f"
done
chmod +x "$DEST"/scripts/*.sh "$DEST"/work/*.sh "$DEST"/work/pesq/*.sh 2>/dev/null || true
V=$(cd "$KIT" && git log -1 --format='%h %cs' 2>/dev/null || echo 'sem git')
echo "kit: $V" > "$DEST/work/kit-versao.txt"
cat <<EOF
Projeto criado: $DEST   (kit $V)

Scripts POR VÍDEO — vêm com os dados do reel Kazuo Inamori como exemplo e têm que ser REESCRITOS neste reel:
  mkcut.py (SPLIT/DROP) · cuts.py (TAKES, FORCE_IN/FORCE_OFF) · captions_fix_table.py (FIX/FIXT) · bipe.py (JANELAS)
  slots.py (S/NOMES) · cenas_opt.py (SPLIT/FORCE/ONLYB/ONLYP) · entrega.py (PK) · make_broll.py (S) · pesquisa_md.py
  (só se usar: se_splice.py, norm_broll1.py, work/layout-exemplo.py)

Próximos passos (docs/06-checklist-execucao.md):
  1. bruto em ~/Claude/videos-brutos/  ->  zsh scripts/mezanino.sh "<bruto>" $SLUG      (sozinho, sem whisper junto)
  2. python3 scripts/regions.py && python3 scripts/mkreg.py && zsh scripts/whisper_regs.sh && python3 scripts/regwords.py
  3. mkcut.py -> cuts.py -> plan_segments.py -> mkchunks.py -> whisper_chunks.sh -> align.py -> fix_captions.py
EOF
```


---

# ARQUIVO: `instalar.sh`

```bash
#!/bin/zsh
# Instala o kit de edição de reel num Mac novo (Apple Silicon). Rodar no Terminal:
#   zsh /caminho/do/KIT-EDICAO-REEL/instalar.sh
# Pode rodar de novo quantas vezes quiser: o que já existe é pulado.
set -e
KIT_SRC="${0:A:h}"; KIT="$HOME/Claude/KIT-EDICAO-REEL"
echo "== 1/7 Homebrew =="
command -v brew >/dev/null || { echo "Falta o Homebrew. Instale com o comando de https://brew.sh (pede a senha do Mac) e rode este script de novo."; exit 1; }
echo "== 2/7 Ferramentas (ffmpeg, whisper-cpp, node, python 3.12) =="
for p in ffmpeg whisper-cpp node python@3.12; do brew list $p >/dev/null 2>&1 || brew install $p; done
echo "== 3/7 Kit em $KIT =="
mkdir -p "$HOME/Claude" "$HOME/Claude/reel-auto" "$HOME/Claude/videos-brutos"
if [ "$KIT_SRC" != "$KIT" ]; then
  [ -e "$KIT" ] && { echo "Já existe $KIT — renomeando o antigo para KIT-EDICAO-REEL.antigo-$(date +%Y%m%d%H%M)"; mv "$KIT" "$KIT.antigo-$(date +%Y%m%d%H%M)"; }
  cp -R "$KIT_SRC" "$KIT"
fi
echo "== 4/7 Python do kit (~/Claude/.venv-reel: numpy, opencv, Pillow, mediapipe 0.10.14) =="
PY=$(brew --prefix python@3.12)/bin/python3.12
[ -x "$HOME/Claude/.venv-reel/bin/python" ] || "$PY" -m venv "$HOME/Claude/.venv-reel"
"$HOME/Claude/.venv-reel/bin/pip" install -q --upgrade pip
"$HOME/Claude/.venv-reel/bin/pip" install -q numpy opencv-python Pillow mediapipe==0.10.14
echo "== 5/7 Modelo do Whisper (large-v3-turbo, 1,6 GB) =="
mkdir -p "$HOME/.cache/whisper"
M="$HOME/.cache/whisper/ggml-large-v3-turbo.bin"
[ -s "$M" ] || curl -L --fail -o "$M" https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin
echo "== 6/7 Skills do Claude Code =="
mkdir -p "$HOME/.claude/skills"
cp -R "$KIT/skill/edicao-reel-viral" "$KIT/skill/showreel-interface" "$HOME/.claude/skills/"
npx --yes hyperframes@0.8.64 skills update || echo "(skills do HyperFrames: rodar depois 'npx hyperframes skills update')"
echo "== 7/7 Conferência =="
bash "$KIT/verificar-instalacao.sh"
cat <<FIM

Pronto. Opcional:
  - Codex (para gerar a capa): instalar o Codex CLI e fazer login (ver COMECE-AQUI.md).
  - ~/Claude/reel-auto/.env com SERPER_API_KEY= / FAL_KEY= (só para a pesquisa por API e imagem no fal; o fluxo padrão não precisa).
Uso: abrir o Claude Code na pasta ~/Claude e mandar o prompt de docs/04-prompt-comando-unico.md.
FIM
```


---

# ARQUIVO: `verificar-instalacao.sh`

```bash
#!/usr/bin/env bash
# Teste de fumaça do kit (v3). Confere o ambiente e reconstrói o reel de referência (só o HTML).
# Uso: bash verificar-instalacao.sh
set -uo pipefail
KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ok=0; fail=0; aviso=0
# grep -q + pipefail = SIGPIPE no ffmpeg; ler a saída inteira evita o falso negativo
hasfilter() { ffmpeg -hide_banner -filters 2>/dev/null | grep -w "$1" >/dev/null; }
chk() { if eval "$2" >/dev/null 2>&1; then printf "  ✓ %s\n" "$1"; ok=$((ok+1)); else printf "  ✗ %s  → %s\n" "$1" "$3"; fail=$((fail+1)); fi; }
opc() { if eval "$2" >/dev/null 2>&1; then printf "  ✓ %s\n" "$1"; ok=$((ok+1)); else printf "  ! %s  → %s\n" "$1" "$3"; aviso=$((aviso+1)); fi; }

echo "== Ferramentas =="
chk "node >= 20"        '[ "$(node -p "process.versions.node.split(\".\")[0]")" -ge 20 ]' "instale Node 20+"
chk "ffmpeg em /opt/homebrew/bin" '[ -x /opt/homebrew/bin/ffmpeg ] && [ -x /opt/homebrew/bin/ffprobe ]' "brew install ffmpeg (o render-chunks.mjs usa esse caminho)"
for f in colorspace scale setpts silencedetect volumedetect blackdetect alimiter atempo zoompan; do
  chk "filtro $f" "hasfilter $f" "ffmpeg sem o filtro $f"
done
chk "whisper-cli"       "command -v whisper-cli" "brew install whisper-cpp"
chk "modelo whisper (large-v3-turbo ou large-v3)" '[ -f "$HOME/.cache/whisper/ggml-large-v3-turbo.bin" ] || [ -f "$HOME/.cache/whisper/ggml-large-v3.bin" ]' "zsh instalar.sh (baixa o ggml-large-v3-turbo.bin)"
chk "python do kit (~/Claude/.venv-reel) + numpy, cv2, PIL, mediapipe" '"$HOME/Claude/.venv-reel/bin/python" -c "import numpy, cv2, PIL, mediapipe"' "zsh instalar.sh (cria o venv com python 3.12 + mediapipe 0.10.14)"
chk "zsh"               "command -v zsh" "os scripts .sh do kit são zsh"

echo "== Kit =="
chk "scripts do modelo (>= 53)" '[ "$(ls "$KIT"/modelo-projeto/scripts | wc -l)" -ge 53 ]' "modelo-projeto/scripts incompleto"
chk "fontes (Montserrat 600/800 + Oswald 700)" '[ "$(ls "$KIT"/assets-fixos/fonts/*.woff2 | wc -l)" -ge 6 ]' "faltam fontes em assets-fixos/fonts/"
chk "trilha + 9 SFX + light-leak" '[ -f "$KIT/assets-fixos/trilha/trilha-epic-cinematic-corporate.mp3" ] && [ "$(ls "$KIT"/assets-fixos/sfx/ | wc -l)" -ge 9 ] && [ -f "$KIT/assets-fixos/fx/transicao-light-leak.mp4" ]' "assets-fixos incompleto"
chk "modelo FaceLandmarker" '[ -f "$KIT/assets-fixos/models/face_landmarker.task" ]' "falta assets-fixos/models/face_landmarker.task"
chk "sintaxe dos scripts .py" 'for f in "$KIT"/modelo-projeto/scripts/*.py; do python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" "$f" || exit 1; done' "erro de sintaxe em modelo-projeto/scripts"
chk "sintaxe dos scripts .mjs" 'for f in "$KIT"/modelo-projeto/scripts/*.mjs; do node --check "$f" || exit 1; done' "erro de sintaxe em modelo-projeto/scripts"

echo "== Ambiente (opcional) =="
chk "skill showreel-interface (sfx.py da camada)" '[ -f "$HOME/.claude/skills/showreel-interface/scripts/sfx.py" ]' "cp -R skill/showreel-interface ~/.claude/skills/"
opc "skill edicao-reel-viral" '[ -f "$HOME/.claude/skills/edicao-reel-viral/SKILL.md" ]' "cp -R skill/edicao-reel-viral ~/.claude/skills/"
opc "codex (capa a pedido)" "command -v codex" "opcional: instalar o Codex CLI e fazer login"
opc "skills do HyperFrames" '[ -d "$HOME/.claude/skills/hyperframes-core" ]' "npx hyperframes skills update"
opc "chaves de API (.env)" '[ -f "${REEL_ENV:-$HOME/Claude/reel-auto/.env}" ]' "sem ~/Claude/reel-auto/.env a pesquisa no Google Imagens e a imagem-conceito não rodam"
opc "kit em ~/Claude/KIT-EDICAO-REEL" '[ "$KIT" = "$HOME/Claude/KIT-EDICAO-REEL" ]' "docs e CLAUDE.md dos projetos apontam para ~/Claude/KIT-EDICAO-REEL"
opc "servidor montado" '[ -d "/Volumes/Company/Equipe/FABIO KENJI" ]' "share Company não montado (só para backup e brutos)"

echo "== novo-projeto.sh + build de referência (reel Kazuo Inamori) =="
TMP="$(mktemp -d)"
if REEL_DIR="$TMP" zsh "$KIT/novo-projeto.sh" teste-fumaca "Kazuo Inamori" >/dev/null 2>&1 && [ -f "$TMP/teste-fumaca/scripts/build-edit.mjs" ]; then
  printf "  ✓ novo-projeto.sh criou o projeto\n"; ok=$((ok+1))
  P="$TMP/teste-fumaca"; E="$KIT/exemplos/kazuo-inamori"
  cp "$E/assets/edit-plan.json" "$P/assets/"; cp "$E"/assets/chunks/*.json "$P/assets/chunks/"
  OUT="$(cd "$P" && node scripts/build-edit.mjs 2>&1)"
  ESP="OK: 41 segs, 98.275s, 4 cenas de broll (21 tomadas), 25 sfx, 101 legendas, 9 callouts, 18 leaks, J-cut 9f/3f."
  if [ "$OUT" = "$ESP" ]; then printf "  ✓ gerador: %s\n" "$OUT"; ok=$((ok+1)); else printf "  ✗ build divergiu\n    esperado: %s\n    obtido:   %s\n" "$ESP" "$OUT"; fail=$((fail+1)); fi
  # o Studio reescreve o index.html do projeto ao salvar (data-hf-id, <br>, &#160;): normaliza os dois lados antes de comparar
  norm() { sed -E -e 's/ data-hf-id="[^"]*"//g' -e 's#<br/>#<br>#g' -e 's/&#160;/\&nbsp;/g' "$1"; }
  if diff <(norm "$P/index.html") <(norm "$E/index.html") >/dev/null; then printf "  ✓ index.html igual ao de referência\n"; ok=$((ok+1)); else printf "  ✗ index.html difere do de referência (exemplos/kazuo-inamori/index.html)\n"; fail=$((fail+1)); fi
else
  printf "  ✗ novo-projeto.sh falhou\n"; fail=$((fail+1))
fi
rm -rf "$TMP"

echo
echo "== $ok ok · $aviso aviso(s) · $fail falha(s) =="
[ "$fail" -eq 0 ]
```


---

# ARQUIVO: `modelo-projeto/CLAUDE.md`

# Reel no formato do Fabio — LEIA ANTES DE QUALQUER COISA

Este projeto foi criado pelo kit `~/Claude/KIT-EDICAO-REEL` (versão em `work/kit-versao.txt`).
**O kit é a fonte única do formato. Não consultar projetos antigos de `reel-auto/` para saber como se faz.**

- Fluxo fase a fase, com comandos: `~/Claude/KIT-EDICAO-REEL/docs/01-pipeline-hyperframes.md`
- Números travados e armadilhas já pagas: `~/Claude/KIT-EDICAO-REEL/docs/05-calibracoes-e-armadilhas.md`
- Checklist: `~/Claude/KIT-EDICAO-REEL/docs/06-checklist-execucao.md` · scripts: `docs/10-scripts.md`
- Mapa deste projeto: `EDICAO.md` (preencher durante a edição)

Regras que não se negociam:
1. **Nunca editar `index.html` à mão**: plano (`assets/edit-plan.json`) → `node scripts/build-edit.mjs` → `python3 scripts/bake.py` → `npm run check`.
2. **Uma tarefa pesada por vez** (MacBook Air 8 GB): nunca whisper junto com encode; render em partes, como tarefa de fundo.
3. **O bruto nunca é alterado** (MD5 antes e depois).
4. **Kit v3: sem parada** — fluxo rápido (`docs/14`) até o MP4, mandado no chat. Parada só se o usuário pedir ou houver decisão que só ele pode tomar.
5. Scripts marcados `POR VIDEO` trazem dados de outro reel como exemplo: reescrever os dados antes de rodar.
6. **Dosagem (docs/05 §24): abertura só com fotos; no corpo, foto real é o padrão e motion só onde conta a história.**
7. Lição nova deste reel vai para o kit (`docs/05` / `modelo-projeto/scripts/` + `git commit`), não só para o `EDICAO.md`.

O restante deste arquivo é o texto padrão do HyperFrames.

---

# HyperFrames Composition Project

## Skills — USE THESE FIRST

**Always invoke the relevant skill before writing or modifying compositions.** Skills encode framework-specific patterns (e.g., `window.__timelines` registration, `data-*` attribute semantics, shader-compatible CSS rules) that are NOT in generic web docs. Skipping them produces broken compositions.

**Doing anything with HyperFrames?** Start at `/hyperframes` — it tells you what HyperFrames can do and which skill or workflow handles your intent (make a video, TTS / BGM, prep footage, author / animate, render, install blocks), confirms your brief up front (the intent layer), and routes every "make me a…" request (a video, a deck, a composition port) to the right workflow. Read it first, especially when there's no project context to orient you. The workflows it routes to:

- `/product-launch-video` — any **website** URL or brief / script → a product launch / SaaS / promo video, or a site tour / showcase featuring the site's own captured visuals.
- `/faceless-explainer` — arbitrary text (topic / article / notes), **no URL, no website capture** → 60-90s faceless explainer.
- `/embedded-captions` — an existing talking-head video (MP4) → the same footage with captions / subtitles added (rail + embed, or pure-cinematic embed); the footage itself is untouched.
- `/talking-head-recut` — an existing talking-head / interview / podcast video (MP4) → the same footage **packaged with designed graphic overlays** (kinetic titles, lower-thirds, data callouts, pull-quotes, side panels, pip) synced to the transcript; the clip plays unchanged underneath. (Plain captions/subtitles → `/embedded-captions`.)
- `/pr-to-video` — a GitHub PR (URL / `owner/repo#N` / "this PR") → 30-90s code-change explainer (changelog / feature reveal / fix / refactor).
- `/motion-graphics` — a short (typically under 10s) design-led **motion graphic**, motion-is-the-message, no narration: kinetic type, a stat / number count-up, a chart, a logo sting, a lower-third / overlay, or an animated tweet / headline / captured-page highlight; rendered to MP4 or a transparent overlay. Longer / narrated / custom → `/general-video`.
- `/music-to-video` — a **music track** (audio file, video to pull audio from, or one generated from a mood brief) → beat-synced video (lyric / slideshow / kinetic promo). Music drives pacing; user-supplied images / videos are cut onto the same beat grid.
- `/slideshow` — a **presentation / pitch deck / interactive deck** — discrete slides, fragment reveals, branching, hotspot navigation, presenter mode. Output is a navigable deck, not a rendered video.
- `/general-video` — fallback for any other video (title card, longer brand / sizzle reel, multi-scene montage, static loop, custom composition) and the home of **companion mode** — co-create with the full HyperFrames toolbox; the original hyperframes authoring flow, any length.

**Porting an existing composition?** `/remotion-to-hyperframes` translates a Remotion (React) composition into HyperFrames HTML — a source migration, separate from the creation workflows above.

The domain skills (`/hyperframes-core`, `/hyperframes-animation`, `/hyperframes-keyframes`, `/hyperframes-creative`, `/hyperframes-cli`, `/media-use`, `/hyperframes-audio`, `/hyperframes-registry`, `/figma`) and the full capability map live inside `/hyperframes` — it is the single source of truth for which skill handles which intent.

**Changing how real footage or images look or reveal?** Load `/media-use` and read its `references/media-treatments.md` before editing, even when the request only says dark, flat, boring, retro, private, or “make the reveal cooler.” It governs how footage is treated, never whether media may be used. Use canonical media treatments and seek-safe motion; do not improvise equivalent CSS/SVG filters or overlays.

> **Tailwind v4 projects** (`hyperframes init --tailwind`): see `/hyperframes-core` → `references/tailwind.md`.

> **Skill missing or stale?** Run `npx hyperframes skills update <name>` to install/refresh
> the specific skill you need (the `/hyperframes` router does this automatically before
> entering a workflow), or bare `npx hyperframes skills update` to refresh the core set plus
> everything already installed — neither pulls the full set. Restart the agent session so
> newly installed skills load.

## Commands

```bash
npm run dev          # human-operated foreground preview (blocks until stopped)
npx hyperframes preview --background  # agent-safe persistent Studio preview
npx hyperframes preview --status      # verify the persistent preview is listening
npx hyperframes preview --stop        # stop it when review is finished
npm run check        # lint + runtime + layout + motion + contrast (one command)
npm run render       # render to MP4
npm run publish      # publish and get a shareable link
npx hyperframes lint --verbose  # include info-level findings
npx hyperframes lint --json     # machine-readable output for CI
npx hyperframes docs <topic> # reference docs in terminal
```

> **Agents must use `npx hyperframes preview --background` for Studio handoff.** Do not rely
> on a shell/tool `run_in_background` wrapper around `npm run dev`: that foreground process
> remains owned by the invoking session and can disappear while the browser stays open,
> leaving refreshes at `ERR_CONNECTION_TIMED_OUT`. Verify with `preview --status`, keep it
> alive through review, and stop it explicitly with `preview --stop` afterward.

> **Pinned CLI version.** These scripts pin an exact `hyperframes@X.Y.Z` so this project re-renders identically over time. Weeks later that pin lags fixes shipped since. To move up: `npx hyperframes@latest upgrade --project . --check` (shows the delta), then `npx hyperframes@latest upgrade --project .` to rewrite the pins. Always unpinned — the pinned script re-runs the old version against itself.

## Documentation

**For quick reference**, use the local CLI docs command (no network required):

```bash
npx hyperframes docs <topic>
```

Topics: `data-attributes`, `gsap`, `compositions`, `rendering`, `examples`, `troubleshooting`

**For full documentation**, discover pages via the machine-readable index — do NOT guess URLs:

```
https://hyperframes.heygen.com/llms.txt
```

## Project Structure

- `index.html` — main composition (root timeline)
- `compositions/` — sub-compositions referenced via `data-composition-src`
- `meta.json` — project metadata (id, name)
- `transcript.json` — whisper word-level transcript (if generated)

## Linting — ALWAYS RUN AFTER CHANGES

After creating or editing any `.html` composition, **always** run the full check before considering the task complete:

```bash
npm run check
```

Fix all errors before presenting the result. Warnings should be reviewed before rendering.

## Key Rules

1. Every timed element needs `data-start` and a duration. `data-start` is what marks it as timed; `data-track-index` is an optional Studio display lane the render never reads
2. Give timed visual elements `class="clip"`. The framework keys visibility off `data-start`, not the class, but the shared `.clip` CSS is what gives a scene its full-frame box, and `lint` warns without it
3. Register one paused root timeline per composition on `window.__timelines`:
   ```js
   window.__timelines = window.__timelines || {};
   window.__timelines["composition-id"] = gsap.timeline({ paused: true });
   ```
   Scene timelines manually added to this root must not be paused. A paused
   child does not advance when the root is seeked. The runtime activates
   registered composition siblings, not arbitrary nested scene timelines.
4. Videos use `muted` with a separate `<audio>` element for the audio track
5. Sub-compositions use `data-composition-src="compositions/file.html"` to reference other HTML files
6. Only deterministic logic — no `Date.now()`, no `Math.random()`, no network fetches


---

# ARQUIVO: `modelo-projeto/package.json`

```json
{
  "name": "__SLUG__",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "npx --yes hyperframes@0.8.64 preview",
    "check": "npx --yes hyperframes@0.8.64 check",
    "render": "npx --yes hyperframes@0.8.64 render",
    "publish": "npx --yes hyperframes@0.8.64 publish"
  }
}
```


---

# ARQUIVO: `modelo-projeto/hyperframes.json`

```json
{
  "$schema": "https://hyperframes.heygen.com/schema/hyperframes.json",
  "registry": "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry",
  "paths": {
    "blocks": "compositions",
    "components": "compositions/components",
    "assets": "assets"
  },
  "media": {
    "autoProxy": true
  }
}
```


---

# ARQUIVO: `modelo-projeto/meta.json`

```json
{
 "id": "__SLUG__",
 "name": "__SLUG__",
 "createdAt": "__DATA__T00:00:00.000Z"
}
```


---

# ARQUIVO: `modelo-projeto/assets/edit-plan.json`

```json
{
 "_nota": "Reel __TITULO__ — formato viral do Fabio. NUNCA editar index.html a mao: mexer aqui e rodar `node scripts/build-edit.mjs && python3 scripts/bake.py && npm run check`.",
 "fps": 30,
 "rate": 1.1,
 "jcutLeadFrames": 9,
 "jcutCrossfadeFrames": 3,
 "src": "assets/__SLUG__-2560-sdr.mp4",
 "voiceSrc": "assets/__SLUG__-voz.m4a",
 "segments": [],
 "sections": [],
 "broll": [],
 "impacts": [],
 "presenterZoom": {
  "scales": [
   1.06,
   1.14
  ],
  "maxHold": 3.5,
  "origin": "50% 53%",
  "mode": "scene",
  "sceneMax": 4.5
 },
 "leakMinGap": 3.5,
 "brollKenBurns": false,
 "bakedAroll": true,
 "bakedAudio": true,
 "bakedBroll": true,
 "bakedLeaks": true,
 "hookSeg": 0,
 "capLowSegs": [],
 "splitShiftY": 400,
 "ctaSeg": 0,
 "_splitShiftY": "400 e so o valor inicial: MEDIR pelos olhos (docs/05, secao Split-screen). Nunca copiar de outro reel.",
 "_ctaSeg": "indice do 1o segmento do encerramento (push-in 1->1.05). Trocar depois do plan_segments.py.",
 "_impacts": "phrase casa com as palavras da legenda normalizadas (sem acento/pontuacao). O 1o leva style typing + drum-fill.",
 "mg": {
  "src": "compositions/mg.html",
  "id": "mg"
 },
 "_mg": "kit v3: camada de motion graphics (docs/13, docs/14). Splits e tela cheia desenhados em compositions/mg.html; sections so nas trocas grandes (virada, CLIMAX, CTA)."
}
```


---

# ARQUIVO: `modelo-projeto/index.html`

```html
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1440, height=2560">
    <title>Reel __TITULO__</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      html,
      body {
        margin: 0;
        width: 1440px;
        height: 2560px;
        overflow: hidden;
        background: #000;
      }
      #root {
        position: relative;
        width: 1440px;
        height: 2560px;
        overflow: hidden;
        background: #000;
      }
      /* Palco na geometria calibrada (1080x1920) escalado para a saida 2K.
         Assim fonte, caixa do gancho, splitShiftY e recortes continuam com os
         mesmos numeros validados — muda so a resolucao de rasterizacao. */
      #stage {
        position: absolute;
        top: 0; left: 0;
        width: 1080px;
        height: 1920px;
        transform: scale(1.3333333333);
        transform-origin: 0 0;
      }
      @font-face {
        font-family: "Montserrat";
        font-weight: 600;
        src: url("assets/fonts/Montserrat-600.woff2") format("woff2"), url("assets/fonts/Montserrat-600-ext.woff2") format("woff2");
      }
      /* Gancho (capa): fonte condensada pesada, estilo da referência do reel Natura */
      @font-face {
        font-family: "Oswald";
        font-weight: 700;
        src: url("assets/fonts/Oswald-700.woff2") format("woff2"), url("assets/fonts/Oswald-700-ext.woff2") format("woff2");
      }
      @font-face {
        font-family: "Montserrat";
        font-weight: 800;
        src: url("assets/fonts/Montserrat-800.woff2") format("woff2"), url("assets/fonts/Montserrat-800-ext.woff2") format("woff2");
      }
      /* Corte com zoom: wrapper interno que muda de escala nos cortes (sem duplicar <video>) */
      #presenter-zoom {
        position: absolute;
        inset: 0;
      }
      /* Apresentador em wrapper não-temporizado (desce durante os splits) */
      #presenter-wrap {
        position: absolute;
        inset: 0;
        z-index: 1;
      }
      #presenter-zoom > video {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
      /* B-roll tela cheia (cutaway) — wrapper não-temporizado anima o Ken Burns */
      .broll-full-wrap {
        position: absolute;
        inset: 0;
        z-index: 20;
        overflow: hidden;
      }
      .broll-full-wrap > video {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
      /* bakedBroll: faixa unica com todas as cenas de tela cheia; comeca escondida e o gerador
         liga/desliga por tl.set nas janelas de cada cena */
      #bfw-all {
        visibility: hidden;
        opacity: 0;
      }
      /* B-roll do split: 44% de cima (tela de baixo maior); wrapper desliza na transição */
      .broll-split-wrap {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 44%;
        z-index: 20;
        overflow: hidden;
      }
      .broll-split-wrap > video {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
      /* Light-leak por cima de tudo, blend screen (flash quente) */
      video.leak {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        mix-blend-mode: screen;
        opacity: 0.85;
        z-index: 40;
      }
      /* Legenda padrão: Montserrat 600, branca sem contorno, centro a 44% */
      .cap {
        position: absolute;
        left: 50%;
        top: 44%;
        transform: translate(-50%, -50%);
        z-index: 60;
        font-family: "Montserrat", sans-serif;
        font-weight: 600;
        font-size: 47px;
        line-height: 1.2;
        color: #fff;
        text-align: center;
        white-space: nowrap;
        text-shadow:
          0 0 7px rgba(0, 0, 0, 0.9),
          0 0 20px rgba(0, 0, 0, 0.75),
          0 3px 16px rgba(0, 0, 0, 0.65);
      }
      /* LEGADO (formato antigo, antes do reel O Boticário): caixa amarela nas legendas do gancho.
         Só usada se o plano tiver "hookSeg": null + "yellowCapSegs". */
      .cap.cap-yellow {
        color: #000;
        background: #ffdd00;
        padding: 8px 26px;
        border-radius: 14px;
        text-shadow: none;
        box-shadow: 0 4px 18px rgba(0, 0, 0, 0.35);
      }
      /* Gancho (hookSeg): a frase INTEIRA desde o frame 0 — serve de capa do reel.
         Caixa laranja vivo com brilho; letras brancas com contorno escuro e sombra dura. */
      .cap.cap-hook {
        top: 44%;
        width: 1016px;
        white-space: normal;
        text-shadow: none;
      }
      .cap-hook .hook-box {
        position: relative;
        display: block;
        overflow: hidden;
        padding: 14px 14px 20px;
        border-radius: 22px;
        background: linear-gradient(180deg, #ff6a2b 0%, #ff4a1c 55%, #f23a0e 100%);
        border: 6px solid #ffffff;
        box-shadow:
          0 0 0 4px rgba(0, 0, 0, 0.55),
          0 0 44px 10px rgba(255, 74, 28, 0.85),
          0 12px 34px rgba(0, 0, 0, 0.5);
      }
      /* Caixa alta, grande, condensada: letras brancas com contorno escuro e sombra dura */
      .cap-hook .hook-text {
        position: relative;
        z-index: 2;
        display: block;
        font-family: "Oswald", "Montserrat", sans-serif;
        font-weight: 700;
        font-size: 90px;
        line-height: 1.03;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        color: #ffffff;
        paint-order: stroke fill;
        -webkit-text-stroke: 12px #141414;
        text-shadow:
          0 7px 0 #141414,
          0 10px 18px rgba(0, 0, 0, 0.5);
      }
      .cap-hook .hook-shine {
        position: absolute;
        top: -20%;
        left: 0;
        width: 38%;
        height: 140%;
        z-index: 1;
        transform: translateX(-160%) skewX(-18deg);
        background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.55) 50%, rgba(255, 255, 255, 0) 100%);
      }
      /* Apresentador sozinho em tela cheia: legenda desce pra não cobrir o rosto */
      .cap.cap-low {
        top: 76%;
      }
      /* Legenda de impacto: maior, caixa alta, centro a 30% */
      .cap-big {
        position: absolute;
        left: 50%;
        top: 30%;
        width: 100%;
        transform: translate(-50%, -50%);
        z-index: 62;
        font-family: "Montserrat", sans-serif;
        font-weight: 800;
        font-size: 76px;
        line-height: 1.14;
        color: #fff;
        text-align: center;
        text-transform: uppercase;
        paint-order: stroke fill;
        -webkit-text-stroke: 10px #000;
        text-shadow: 0 4px 18px rgba(0, 0, 0, 0.6);
      }
      .cap-big .inner {
        display: inline-block;
      }
      /* Caracteres do efeito de digitação começam invisíveis */
      .cap-big .tc {
        opacity: 0;
        visibility: hidden;
      }
      /* ---- Toggle de camadas (pacote conformável para NLE) ----
         Aplicado via classe no <html> nos arquivos pass-*.html gerados pelo
         build-edit.mjs. O index.html fica sempre com tudo visível.
           layers-clean → picture (apresentador + B-roll), sem grafismo
           layers-gfx   → só legendas e callouts, fundo transparente
           layers-leaks → só light-leaks, fundo transparente (blend screen no NLE) */
      html.layers-clean .cap,
      html.layers-clean .cap-big,
      html.layers-clean video.leak {
        display: none !important;
      }
      html.layers-gfx #presenter-wrap,
      html.layers-gfx .broll-full-wrap,
      html.layers-gfx .broll-split-wrap,
      html.layers-gfx video.leak {
        display: none !important;
      }
      html.layers-leaks #presenter-wrap,
      html.layers-leaks .broll-full-wrap,
      html.layers-leaks .broll-split-wrap,
      html.layers-leaks .cap,
      html.layers-leaks .cap-big {
        display: none !important;
      }
      html.layers-gfx video.leak,
      html.layers-leaks video.leak {
        mix-blend-mode: normal;
      }
      html.layers-gfx,
      html.layers-gfx body,
      html.layers-gfx #root,
      html.layers-leaks,
      html.layers-leaks body,
      html.layers-leaks #root {
        background: transparent !important;
      }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="1" data-width="1440" data-height="2560">
    <div id="stage">
    <!-- EDIT:BEGIN (gerado por scripts/build-edit.mjs — não editar à mão) -->
    <!-- EDIT:END -->
    </div>
    </div>

    <script>
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      // EDIT-TWEENS:BEGIN (gerado — crossfades, splits, callouts, trilha)
      // EDIT-TWEENS:END
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
```


---

# ARQUIVO: `modelo-projeto/compositions/mg.html`

```html
<!doctype html>
<html>
  <head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>
        /* Camada de motion graphics (skill showreel-interface) — kit v3.
           Geometria 1080x1920 (dentro do #stage do host). Transparente fora das cenas.
           Faixa das legendas (76% = y~1460) fica livre: o conteúdo mora entre y 140 e 1340. */
        #mg { position: absolute; inset: 0; overflow: hidden; pointer-events: none; font-family: "Montserrat", sans-serif; }
        #mg .scene { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; visibility: hidden; opacity: 0; overflow: hidden; }
        #mg .world { position: absolute; inset: 0; }
        #mg .dark { background: radial-gradient(130% 80% at 50% 28%, #1B2130 0%, #0C0F15 68%); }
        /* mundo claro com "chao" escuro abaixo de 64%: a legenda branca (76%) precisa de fundo escuro (reel Deming) */
        #mg .light { background: linear-gradient(180deg, rgba(17,20,26,0) 0%, rgba(17,20,26,0) 64%, #11141A 73%), radial-gradient(130% 80% at 50% 28%, #FFFFFF 0%, #E8E6E1 78%); }
        #mg .band { position: absolute; left: -400px; top: 520px; width: 1900px; height: 520px; border-radius: 260px; transform: rotate(-14deg); }
        #mg .dark .band { background: rgba(255,255,255,.035); }
        #mg .light .band { background: rgba(0,0,0,.03); }
        #mg .card { position: absolute; border-radius: 44px; overflow: hidden; box-shadow: 0 34px 90px rgba(0,0,0,.45), 0 6px 18px rgba(0,0,0,.25); background: #222; }
        #mg .card img { width: 100%; height: 100%; object-fit: cover; display: block; }
        #mg .full { position: absolute; inset: 0; overflow: hidden; }
        #mg .full img { width: 100%; height: 100%; object-fit: cover; display: block; }
        /* chip de capítulo (status do BPR) */
        #mg .chip { position: absolute; left: 270px; width: 540px; height: 104px; border-radius: 999px; background: #11141A; color: #fff;
                    display: flex; align-items: center; justify-content: center; gap: 24px; box-shadow: 0 18px 44px rgba(0,0,0,.28); }
        #mg .light .chip, #mg .chip.on-light { background: #11141A; }
        #mg .chip .dot { width: 34px; height: 34px; border-radius: 50%; flex: none; }
        #mg .chip .win { height: 104px; overflow: hidden; }
        #mg .chip .roll span { display: block; height: 104px; line-height: 104px; font-weight: 800; font-size: 44px; letter-spacing: .06em; }
        #mg .chip .plus { position: absolute; left: 50%; top: 50%; width: 104px; height: 104px; margin: -52px 0 0 -52px; border-radius: 50%;
                          background: #11141A; color: #fff; font-weight: 600; font-size: 78px; line-height: 98px; text-align: center; }
        /* etiqueta de nome */
        #mg .name { position: absolute; left: 90px; width: 900px; padding: 26px 40px; border-radius: 34px; background: rgba(255,255,255,.96);
                    color: #11141A; box-shadow: 0 20px 50px rgba(0,0,0,.3); }
        #mg .name b { display: block; font-weight: 800; font-size: 58px; letter-spacing: .01em; }
        #mg .name i { display: block; font-style: normal; font-weight: 600; font-size: 30px; letter-spacing: .08em; color: #5A606B; margin-top: 6px; }
        #mg .tag { white-space: nowrap; position: absolute; padding: 18px 34px; border-radius: 999px; font-weight: 800; font-size: 38px; letter-spacing: .06em; color: #fff; }
        /* carimbo */
        #mg .stamp { position: absolute; padding: 8px 40px; border: 12px solid #E5322D; border-radius: 26px; color: #E5322D; background: rgba(255,255,255,.9);
                     font-weight: 800; font-size: 112px; letter-spacing: .04em; }
        /* título palavra a palavra */
        #mg .title { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; font-size: 112px; line-height: 1.04; color: #11141A; }
        #mg .title span { display: inline-block; }
        #mg .sel { position: relative; display: inline-block; padding: 6px 30px 14px; border: 6px solid #F2B705; background: rgba(242,183,5,.16); }
        #mg .sel .h { position: absolute; width: 26px; height: 26px; background: #fff; border: 4px solid #F2B705; border-radius: 5px; }
        #mg .sel .tl { left: -17px; top: -17px; } #mg .sel .tr { right: -17px; top: -17px; } #mg .sel .bl { left: -17px; bottom: -17px; } #mg .sel .br { right: -17px; bottom: -17px; }
        /* toast */
        #mg .toast { position: absolute; left: 90px; width: 900px; padding: 30px 36px; border-radius: 38px; background: #fff; color: #11141A;
                     box-shadow: 0 26px 70px rgba(0,0,0,.35); display: flex; gap: 28px; align-items: center; }
        #mg .toast .ic { width: 92px; height: 92px; border-radius: 26px; background: #F2B705; color: #11141A; font-weight: 800; font-size: 64px; line-height: 92px; text-align: center; flex: none; }
        #mg .toast b { display: block; font-weight: 800; font-size: 34px; letter-spacing: .06em; color: #5A606B; }
        #mg .toast p { margin: 6px 0 0; font-weight: 600; font-size: 46px; }
        /* semáforo */
        #mg .tlight { position: absolute; left: 400px; width: 280px; height: 760px; border-radius: 64px; background: #050608; border: 6px solid #2A303C;
                      box-shadow: 0 40px 90px rgba(0,0,0,.6); }
        #mg .tlight .lamp { position: absolute; left: 40px; width: 188px; height: 188px; border-radius: 50%; background: #1C2029; }
        #mg .tlight .glow { position: absolute; inset: 0; border-radius: 50%; opacity: 0; }
        #mg .week { position: absolute; left: 60px; width: 960px; display: flex; justify-content: space-between; }
        #mg .week span { width: 120px; height: 120px; border-radius: 30px; background: #1C2029; color: #8C93A1; font-weight: 800; font-size: 46px; line-height: 120px; text-align: center; }
        /* quadro de status (BPR) */
        #mg .board { position: absolute; left: 60px; width: 960px; border-radius: 44px; padding: 40px 44px 30px; box-shadow: 0 34px 90px rgba(0,0,0,.28); }
        #mg .board.b-light { background: #fff; }
        #mg .board.b-dark { background: #151A23; border: 2px solid #252C39; }
        #mg .board .hd { display: flex; justify-content: space-between; font-weight: 800; font-size: 34px; letter-spacing: .08em; margin-bottom: 18px; }
        #mg .b-light .hd { color: #11141A; } #mg .b-dark .hd { color: #E9ECF2; }
        #mg .board .hd i { font-style: normal; font-weight: 600; color: #8C93A1; }
        #mg .row { position: relative; height: 112px; display: flex; align-items: center; justify-content: space-between; border-top: 2px solid rgba(128,136,150,.18); }
        #mg .row .g { display: flex; gap: 14px; }
        #mg .row .g i { display: block; height: 22px; border-radius: 11px; }
        #mg .b-light .row .g i { background: #D9DCE2; } #mg .b-dark .row .g i { background: #303746; }
        #mg .pill { position: relative; width: 330px; height: 74px; border-radius: 999px; }
        #mg .pill span { position: absolute; inset: 0; border-radius: 999px; color: #fff; font-weight: 800; font-size: 30px; letter-spacing: .05em;
                         display: flex; align-items: center; justify-content: center; gap: 14px; }
        #mg .pill span::before { content: ""; width: 20px; height: 20px; border-radius: 50%; background: rgba(255,255,255,.9); }
        #mg .p0 { background: #C9CCD2; } #mg .b-dark .p0 { background: #343B49; }
        #mg .pg { background: #1FB45A; } #mg .py { background: #F2B705; color: #11141A !important; } #mg .pr { background: #E5322D; }
        #mg .bars { position: absolute; left: 60px; width: 960px; height: 300px; display: flex; align-items: flex-end; gap: 22px; padding: 0 30px; }
        #mg .bars i { flex: 1; border-radius: 18px 18px 6px 6px; transform-origin: 50% 100%; }
        #mg .rainbow { position: absolute; left: 60px; width: 960px; height: 14px; border-radius: 7px;
                       background: linear-gradient(90deg, #E5322D, #F28C05, #F2B705, #1FB45A, #1E8BE5, #7B3FE4); }
        /* balões */
        #mg .bubble { position: absolute; padding: 22px 38px; border-radius: 40px; background: #fff; color: #11141A; font-weight: 800; font-size: 58px;
                      box-shadow: 0 18px 44px rgba(0,0,0,.3); }
        #mg .bubble.me { background: #1FB45A; color: #fff; }
        #mg .strike { position: absolute; height: 14px; border-radius: 7px; background: #E5322D; transform-origin: 0 50%; }
        #mg .ring { position: absolute; width: 300px; height: 300px; margin: -150px 0 0 -150px; border-radius: 50%; border: 10px solid #fff; opacity: 0; }
        /* split: prejuízo */
        #mg .panel { position: absolute; left: 0; top: 0; width: 1080px; height: 845px; background: radial-gradient(120% 90% at 50% 20%, #2A1416 0%, #0E0B0D 70%); overflow: hidden; }
        #mg .lbl { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; font-size: 36px; letter-spacing: .1em; color: #F3B4B0; }
        #mg .money { position: absolute; left: 0; width: 1080px; display: flex; justify-content: center; align-items: center; gap: 10px; color: #FF4A3D; font-weight: 800; }
        #mg .money .cur { font-size: 96px; margin-right: 16px; }
        #mg .money .col { height: 210px; overflow: hidden; }
        #mg .money .col div span { display: block; height: 210px; line-height: 210px; font-size: 220px; text-align: center; width: 140px; }
        #mg .money .suf { font-size: 96px; margin-left: 18px; }
        #mg .dots { position: absolute; display: flex; gap: 18px; padding: 30px 40px; border-radius: 40px; background: #fff; box-shadow: 0 18px 44px rgba(0,0,0,.3); }
        #mg .dots i { width: 26px; height: 26px; border-radius: 50%; background: #8C93A1; display: block; }
            </style>

      <div id="mg" data-composition-id="mg" data-width="1080" data-height="1920">
        <!-- CENAS (por video). Uma .scene por janela de motion (tela cheia) e uma .scene com style="height:845px" por
             split. Modelo de todas as pecas (card, nome, chip, carimbo, toast, semaforo, quadro de status, baloes,
             contador, barras, aneis, arco-iris): ~/Claude/KIT-EDICAO-REEL/exemplos/alan-mulally/mg.html -->
      </div>

      <script>
        (function () {
          // ================= BIBLIOTECA (kit v3) — nao mexer; as CENAS vao no fim =================
          // Todo componente que tem som chama cue(): scripts/mg_cues.mjs le esta lista sem navegador e o
          // scripts/mg_sfx.py sintetiza e mistura no bed. Ganhos calibrados no reel Alan Mulally (voz >= 6 dB acima).
          var tl = gsap.timeline({ paused: true });
          var q = 1 / 30;
          window.__mgCues = [];
          function Q(t) { return Math.round(t * 30) / 30; }
          function cue(t, som, g, args) { window.__mgCues.push({ t: Math.round(t * 1000) / 1000, som: som, ganho: g, args: args || {} }); }
          function hide(sel) { gsap.set(sel, { autoAlpha: 0 }); }
          // cena de tela cheia: cresce de card -> cheia; sai encolhendo para card + chicote p/ cima (revela o apresentador)
          function sceneIn(id, t) {
            tl.set(id, { autoAlpha: 1 }, Q(t));
            tl.fromTo(id, { clipPath: "inset(14% 9% 14% 9% round 72px)", scale: 0.92 },
              { clipPath: "inset(0% 0% 0% 0% round 0px)", scale: 1, duration: 13 * q, ease: "expo.out" }, Q(t));
            cue(t, "whoosh", -17);
          }
          function sceneOut(id, t) {
            tl.to(id, { clipPath: "inset(9% 7% 9% 7% round 72px)", scale: 0.9, duration: 8 * q, ease: "power3.in" }, Q(t) - 12 * q);
            tl.to(id, { y: -2300, duration: 4 * q, ease: "power4.in" }, Q(t) - 4 * q);
            tl.set(id, { autoAlpha: 0 }, Q(t));
            cue(t - 0.2, "swish", -18);
          }
          // faixa de cima do split (44% = 845 px), sincronizada com o arrasto do apresentador (0,55 s power3.inOut)
          function splitIn(id, t, imediato) {
            tl.set(id, { autoAlpha: 1 }, Q(t));
            if (!imediato) { tl.fromTo(id, { y: -845 }, { y: 0, immediateRender: false, duration: 0.55, ease: "power3.inOut" }, Q(t)); cue(t + 0.3, "whoosh", -18); }
          }
          function splitOut(id, t) { tl.to(id, { y: -845, duration: 0.55, ease: "power3.inOut" }, Q(t - 0.55)); tl.set(id, { autoAlpha: 0 }, Q(t)); }
          // corte dentro do split / da cena: o novo entra pelo lado (chicote), o velho sai no mesmo vetor
          function whip(saem, entra, t, dir) {
            var d = dir === "dir" ? -1 : 1;
            if (saem) tl.to(saem, { x: -1400 * d, filter: "blur(18px)", duration: 5 * q, ease: "power4.in" }, Q(t) - 5 * q);
            tl.fromTo(entra, { x: 1300 * d, autoAlpha: 1, filter: "blur(18px)" }, { x: 0, autoAlpha: 1, filter: "blur(0px)", immediateRender: false, duration: 13 * q, ease: "expo.out" }, Q(t) - q);
            cue(t - 0.05, "whoosh", -14);
          }
          // troca vertical: o velho cai, o novo entra de cima (ou o contrario com dir "sobe")
          function drop(saem, entra, t, dir) {
            var d = dir === "sobe" ? -1 : 1;
            if (saem) tl.to(saem, { y: 1900 * d, duration: 5 * q, ease: "power4.in" }, Q(t) - 5 * q);
            tl.fromTo(entra, { y: -1500 * d, autoAlpha: 1 }, { y: 0, autoAlpha: 1, immediateRender: false, duration: 13 * q, ease: "expo.out" }, Q(t) - q);
            cue(t - 0.05, "whoosh", -15);
          }
          // zoom-through de um card/foto para o proximo (T1 curto)
          function zoomIn(id, t) { tl.fromTo(id, { scale: 0.55, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, immediateRender: false, duration: 13 * q, ease: "expo.out" }, Q(t) - q); cue(t - 0.05, "whoosh", -14); }
          function drift(id, t0, t1) { tl.fromTo(id, { x: -60 }, { x: 60, duration: t1 - t0, ease: "none" }, t0); }
          function kenburns(id, t0, t1, z0, z1) { tl.fromTo(id, { scale: z0 || 1.1 }, { scale: z1 || 1, duration: t1 - t0, ease: "power2.out" }, t0); }
          // entradas pequenas
          function pop(id, t, from, som) {
            tl.fromTo(id, from || { scale: 0.6, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, x: 0, y: 0, duration: 9 * q, ease: "back.out(2.2)" }, Q(t));
            if (som !== false) cue(t + 0.02, som || "pop", -20);
          }
          function flip(id, t) { pop(id, t, { scale: 0.5, autoAlpha: 0 }, "clique"); }            // pilula de status muda de cor
          function rise(id, t) { tl.fromTo(id, { y: 70, autoAlpha: 0, filter: "blur(10px)" }, { y: 0, autoAlpha: 1, filter: "blur(0px)", duration: 9 * q, ease: "expo.out" }, Q(t)); }
          function words(ids, ts) { ids.forEach(function (id, k) { rise(id, ts[k]); cue(ts[k], "tique", -24); }); }   // titulo palavra a palavra
          function slam(id, t, rot) {                                                              // carimbo
            tl.fromTo(id, { scale: 2.4, autoAlpha: 0, rotation: rot }, { scale: 1, autoAlpha: 1, rotation: rot, duration: 4 * q, ease: "power4.in" }, Q(t) - 4 * q);
            tl.fromTo(id, { scale: 1 }, { scale: 1.04, duration: 3 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(t));
            cue(t, "impacto", -18, { dur: 0.9 }); cue(t, "clique", -18);
          }
          // chip de capitulo (T2): "+" aparece em tAp, abre em pilula e o rolo trava no capitulo em t
          function chip(base, t, tAp) {
            var R = (540 - 104) / 2, t0 = tAp != null ? tAp : t - 14 * q;
            tl.set("#" + base + "-chip", { clipPath: "inset(0px " + R + "px 0px " + R + "px round 999px)" }, 0);
            tl.fromTo("#" + base + "-chip", { scale: 0.4, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 7 * q, ease: "back.out(2)" }, Q(t0));
            tl.to("#" + base + "-chip", { clipPath: "inset(0px 0px 0px 0px round 999px)", duration: 8 * q, ease: "power3.out" }, Q(t) - 6 * q);
            tl.to("#" + base + "-plus", { rotation: 45, autoAlpha: 0, duration: 6 * q, ease: "power2.in" }, Q(t) - 6 * q);
            tl.fromTo("#" + base + "-roll", { y: 0, filter: "blur(6px)" }, { y: -208, filter: "blur(0px)", duration: 14 * q, ease: "power4.out" }, Q(t) - 6 * q);
            cue(t0 + 0.02, "pop", -21); cue(t, "cacaniquel", -20);
          }
          function smear(id, t) {                                                                  // chip vira risco -> corte (T7)
            tl.to(id, { scaleX: 1.3, duration: q, ease: "power2.in" }, Q(t) - 5 * q);
            tl.to(id, { scaleX: 9, scaleY: 0.5, filter: "blur(14px)", autoAlpha: 0, duration: 4 * q, ease: "power4.in" }, Q(t) - 4 * q);
          }
          function stagger(sel, t, n, passo) {                                                    // linhas/barras entrando
            tl.to(sel, { autoAlpha: 1, x: 0, duration: 9 * q, ease: "expo.out", stagger: (passo || 2) * q }, Q(t));
            for (var k = 0; k < n; k++) cue(t + k * (passo || 2) * q, "tique", -27);
          }
          function bars(sel, t, n) { tl.to(sel, { scaleY: 1, duration: 10 * q, ease: "expo.out", stagger: 2 * q }, Q(t)); for (var k = 0; k < n; k++) cue(t + k * 2 * q, "pop", -24, { f0: 700 + 120 * k }); }
          function digits(id, t, casas, dur) {                                                    // rolo de digitos (caca-niquel, seek-safe)
            tl.fromTo(id, { y: 0, filter: "blur(4px)" }, { y: -casas * 210, filter: "blur(0px)", duration: dur || 26 * q, ease: "power4.out" }, Q(t));
          }
          function rings(a, b, t) {                                                               // palma / impacto
            tl.fromTo(a, { scale: 0.2, opacity: 0.9 }, { scale: 3.2, opacity: 0, immediateRender: false, duration: 14 * q, ease: "expo.out" }, Q(t));
            tl.fromTo(b, { scale: 0.2, opacity: 0.7 }, { scale: 2.4, opacity: 0, immediateRender: false, duration: 14 * q, ease: "expo.out" }, Q(t) + 3 * q);
            cue(t, "impacto", -19, { dur: 0.6 }); cue(t, "swish", -20);
          }
          // ================= CENAS (por video) — tempos absolutos de `python3 scripts/tl.py --words` =================

          // (vazio = camada transparente)

          window.__timelines["mg"] = tl;
        })();
      </script>
    </template>
  </body>
</html>
```


---

# ARQUIVO: `modelo-projeto/scripts/fase1.sh`

```bash
#!/bin/zsh
# FLUXO RAPIDO (kit v3) · FASE 1 — bruto -> mezanino + voz + transcricao por regiao (whisper turbo). ~5 min.
# uso: zsh scripts/fase1.sh "<bruto>" <slug>      (rodar como tarefa de fundo; enquanto isso: pesquisa no navegador)
set -e; cd "${0:A:h}/.."; export PATH=$HOME/Claude/.venv-reel/bin:$PATH
[ -f "assets/$2-2560-sdr.mp4" ] && echo "mezanino ja existe (pulado)" || zsh scripts/mezanino.sh "$1" "$2"
python3 scripts/regions.py && python3 scripts/mkreg.py | tail -1 && zsh scripts/whisper_regs.sh | tail -2
python3 scripts/regwords.py > work/regioes.txt; cat work/regioes.txt
echo "FASE 1 OK -> ler work/regioes.txt contra o roteiro; escrever mkcut.py (SPLIT/DROP), cuts.py (TAKES), bipe.py se houver palavrao"
```


---

# ARQUIVO: `modelo-projeto/scripts/fase2.sh`

```bash
#!/bin/zsh
# FLUXO RAPIDO (kit v3) · FASE 2 — cortes -> J-cut -> chunks (do passe por regiao, sem 2o whisper) -> legendas ->
# faixas -> timeline por palavra -> olhar (medidores + folhas de rosto inteiro). ~6 min.
# uso: zsh scripts/fase2.sh      (depois de mkcut.py/cuts.py/bipe.py escritos; bipe.py roda aqui se tiver JANELAS)
set -e; cd "${0:A:h}/.."; export PATH=$HOME/Claude/.venv-reel/bin:$PATH
grep -q "^JANELAS=\[(" scripts/bipe.py && python3 scripts/bipe.py
python3 scripts/mkcut.py > work/mkcut.txt && python3 scripts/cuts.py | tail -4 && python3 scripts/plan_segments.py | tail -1
python3 scripts/mkchunks.py && python3 scripts/chunks_from_regions.py > work/chunks.txt
zsh scripts/legendas.sh
python3 scripts/bake.py voz bed aroll leaks | tail -4 && python3 scripts/jcut_check.py | tail -3
python3 scripts/tl.py --words > work/tl-words.txt
python3 scripts/gaze_tl.py 2>/dev/null | tail -1 && python3 scripts/gaze_windows.py | tail -1 && python3 scripts/gaze_pose.py 2.0 2>/dev/null | tail -1
python3 scripts/gaze_sheet.py 2>/dev/null | tail -2
echo "FASE 2 OK -> work/chunks.txt (indices p/ captions_fix_table.py) · work/tl-words.txt (tempos) · gaze/me/*.jpg (olhar)"
```


---

# ARQUIVO: `modelo-projeto/scripts/legendas.sh`

```bash
#!/bin/zsh
# Refaz as legendas do zero a partir do passe por regiao + scripts/captions_fix_table.py (idempotente) e regenera o index.
# uso: zsh scripts/legendas.sh      (depois de mexer na captions_fix_table.py)
set -e; cd "${0:A:h}/.."; export PATH=$HOME/Claude/.venv-reel/bin:$PATH
cp work/chunks-raw/ch*-words.json assets/chunks/ && rm -rf work/chunks-aligned
python3 scripts/align.py > work/align.txt 2>&1 && python3 scripts/fix_captions.py | tail -3
node scripts/build-edit.mjs | tail -1
```


---

# ARQUIVO: `modelo-projeto/scripts/montar.sh`

```bash
#!/bin/zsh
# FLUXO RAPIDO (kit v3) · MONTAR — slots (MG) -> build -> leaks + bed -> SFX automaticos da camada de motion -> check
# -> snapshots nos instantes pedidos. ~3 min. uso: zsh scripts/montar.sh 13.4,16.8,26.9,...   (instantes p/ conferir)
set -e; cd "${0:A:h}/.."; export PATH=$HOME/Claude/.venv-reel/bin:$PATH
python3 scripts/slots.py --real | tail -1 && node scripts/build-edit.mjs | tail -1
python3 scripts/bake.py cenas brollfull leaks bed | tail -3
node scripts/mg_cues.mjs && python3 scripts/mg_sfx.py | head -1
npx --yes hyperframes@0.8.64 check 2>&1 | grep -E "error\(s\)" | head -2
[ -n "$1" ] && { rm -rf snapshots/qc; npx --yes hyperframes@0.8.64 snapshot . -o snapshots/qc --at "$1" --no-end --timeout 20000 >/dev/null 2>&1; ls snapshots/qc/contact-sheet*.jpg; }
echo "MONTAR OK"
```


---

# ARQUIVO: `modelo-projeto/scripts/render-par.sh`

```bash
#!/bin/zsh
# MOTOR (kit v3). Render em partes, P de cada vez em PARALELO (cada uma com seu TMPDIR), depois finalizar.py.
# Medido no Mac de 16 GB (reel Alan Mulally, 1440x2560 @60): serial ~55 s/parte; 3 em paralelo ~27 s/parte (o dobro);
# 4 e 6 em paralelo saturam (~34 s/parte). Resultado identico ao serial (PSNR 53 dB = so ruido de codificacao).
# Em maquina de 8 GB: P=1 (o render-all.sh antigo). RODAR COMO TAREFA DE FUNDO DO HARNESS (run_in_background).
# uso: zsh scripts/render-par.sh <SIZE> <saida.mp4> [P=3] [FPS=60] [SPLIT=3]
cd "${0:A:h}/.."
SIZE=${1:?uso: zsh scripts/render-par.sh <SIZE> <saida.mp4> [P] [FPS] [SPLIT]}; OUT=${2:?saida}; P=${3:-3}; FPS=${4:-60}; SPLIT=${5:-3}
# HF_VERSION / HF_WORKERS (render-chunks.mjs): padrao 0.8.48 / 1 (validado, identico ao serial). Testado 0.8.111 x3 workers x2 partes:
# 764 s contra 793 s — o Air M4 sem ventoinha limita a ~8 q/s no total sob carga continua; nao compensa trocar a versao.
mkdir -p renders/chunks
N=$(python3 -c "import json,math;print(math.ceil(math.ceil(json.load(open('work/mix-plan.json'))['total']*$FPS-1e-6)/$SIZE))")
echo "$N partes de $SIZE quadros @$FPS, $P em paralelo, --split $SPLIT"
T0=$(date +%s); FALHA=0
roda() {  # $1 = parte
  local k=$1 c=renders/chunks/chunk-$(printf %02d $1).mp4
  [ -f $c ] && return 0
  mkdir -p renders/tmp$k
  TMPDIR=$PWD/renders/tmp$k/ node scripts/render-chunks.mjs --fps $FPS --size $SIZE --split $SPLIT --only $k > renders/chunks/log-$k.txt 2>&1 \
    || { echo "PARTE $k FALHOU"; tail -3 renders/chunks/log-$k.txt; rm -f $c; rm -rf renders/tmp$k; return 1; }
  find renders/chunks -name "sub-$(printf %02d $k)-*" -delete; rm -rf renders/tmp$k
  echo "parte $k pronta · $(( $(date +%s)-T0 ))s"
}
for ((k=0; k<N; k+=P)); do
  for ((j=k; j<k+P && j<N; j++)); do roda $j & done
  wait
  free=$(df -m /System/Volumes/Data | tail -1 | awk '{print $4}')
  [ $free -lt 700 ] && { echo "DISCO CRITICO (${free} MB) — parando"; exit 2; }
done
rm -f compositions/_chunk-*.html; find . -maxdepth 1 -name "render-chunk-*.html" -delete
miss=$(for ((k=0;k<N;k++)); do [ -f renders/chunks/chunk-$(printf %02d $k).mp4 ] || echo $k; done)
[ -n "$miss" ] && { echo "FALTAM PARTES: $miss — rodar de novo (retoma)"; exit 1; }
echo "partes em $(( $(date +%s)-T0 ))s"
python3 scripts/finalizar.py "$OUT" --fps $FPS
```


---

# ARQUIVO: `modelo-projeto/scripts/build-edit.mjs`

```javascript
#!/usr/bin/env node
// Gera a edição completa (vídeo + voz J-cut + B-rolls + legendas + callouts +
// light-leaks + SFX + trilha) a partir de assets/edit-plan.json e injeta em
// index.html entre <!-- EDIT:BEGIN -->...<!-- EDIT:END --> e // EDIT-TWEENS:BEGIN...END.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const plan = JSON.parse(fs.readFileSync(path.join(ROOT, 'assets/edit-plan.json'), 'utf8'));
const FPS = plan.fps || 30;
const F = n => n / FPS;
const r3 = x => Math.round(x * 1000) / 1000;

const LEAD_FRAMES = plan.jcutLeadFrames ?? 5;
const XFADE_FRAMES = plan.jcutCrossfadeFrames ?? LEAD_FRAMES;
const LEAD = F(LEAD_FRAMES);   // J-cut: voz entra antes do corte (timeline)
const XFADE = F(XFADE_FRAMES); // crossfade entre as duas faixas de voz
const LEAK_DUR = 0.7;   // light-leak 21 frames
const LEAK_PRE = F(10); // leak começa 10 frames antes do corte
const RATE = plan.rate || 1;

// ---- segmentos → linha do tempo ----
let t = 0;
const segs = plan.segments.map((s, i) => {
  const sourceDur = r3((s.out - s.in) / RATE);
  const lead = i === 0 ? 0 : Math.min(LEAD, sourceDur - F(10));
  // O conteúdo falado do take começa `lead` antes do corte visual. Para manter
  // lip-sync, os primeiros `lead` segundos do VÍDEO ficam cobertos pelo take
  // anterior e a janela visual deste segmento fica menor na mesma medida.
  const dur = r3(sourceDur - lead);
  if (dur <= F(10)) throw new Error(`Segmento ${i} (${s.label}) curto demais`);
  const tStart = r3(t);
  const seg = {
    ...s,
    i,
    lead,
    sourceDur,
    dur,
    tStart,
    audioStart: r3(tStart - lead),
    tEnd: r3(tStart + dur),
  };
  t = r3(t + dur);
  return seg;
});
const TOTAL = r3(t);
const rateAttr = RATE !== 1 ? ` data-playback-rate="${RATE}"` : '';
const volTweens = [];

// ---- vídeo do apresentador (track 0, mudo, dentro do wrapper) ----
// videoTail (source sec): o VÍDEO deste take corta antes do fim (desvio de olhar);
// o vídeo do PRÓXIMO take entra adiantado com pré-rolo (L-cut) enquanto a voz termina.
// Lip-sync preservado: quando a imagem do take entra em tStart, ela já avançou
// o mesmo `lead` que o áudio avançou durante o J-cut.
const earlyDelta = segs.map(s => s.videoTail ? r3((s.out - s.videoTail) / RATE) : 0);
// Janela de um B-roll na timeline. preStart antecipa a janela inteira; span [f0, f1] recorta
// uma fração dela (vários B-rolls seguidos dentro do mesmo trecho de fala, um a cada ~4 s).
const brollWin = b => {
  const w0 = r3(segs[b.fromSeg].tStart - (b.preStart || 0));
  const w1 = segs[b.toSeg].tEnd;
  const [f0, f1] = b.span || [0, 1];
  return [r3(w0 + (w1 - w0) * f0), r3(w0 + (w1 - w0) * f1)];
};
const fullWins = (plan.broll || []).filter(b => b.mode !== 'split').map(brollWin);
const coveredFull = (a, b) => fullWins.some(([w0, w1]) => w0 <= a + 0.02 && b <= w1 + 0.02);
// presenterZoom: "corte seco com zoom" no apresentador — a escala alterna a cada corte de take e,
// dentro de takes longos, a cada `maxHold` s no máximo (ritmo: algo muda na tela a cada <= 4 s).
// Não mexe no lip-sync: cada pedaço é o mesmo vídeo, só com outro enquadramento.
const PZ = plan.presenterZoom || null;
// O corte com zoom NÃO duplica elementos <video> (o Chrome só carrega ~75 players por aba e a
// composição ficava com a tela preta no preview): a escala é aplicada por tl.set no wrapper
// #presenter-zoom, nos mesmos instantes em que o enquadramento deveria trocar.
const zoomCuts = [];
const videoCutTimes = [];
let zoomIdx = 0;
const videoClips = segs.map(s => {
  const dPrev = s.i > 0 ? earlyDelta[s.i - 1] : 0;
  const vStart = r3(s.tStart - dPrev);
  const vEnd = r3(s.tEnd - earlyDelta[s.i]);
  const vDur = r3(vEnd - vStart);
  const vMedia = r3(s.in + (s.lead - dPrev) * RATE);
  if (vMedia < 0) throw new Error(`seg${s.i}: pré-rolo estoura o início do source`);
  if (PZ) {
    const n = coveredFull(vStart, vEnd) ? 1 : Math.max(1, Math.ceil(vDur / PZ.maxHold - 1e-6));
    for (let p = 0; p < n; p++) {
      zoomCuts.push({ t: r3(vStart + (vDur * p) / n), scale: PZ.scales[zoomIdx++ % PZ.scales.length] });
    }
  }
  videoCutTimes.push(vStart);
  return `      <video id="v${s.i}" class="clip" src="${plan.src}" data-start="${vStart}" data-duration="${vDur}" data-media-start="${vMedia}"${rateAttr} data-track-index="0" muted playsinline preload="auto"></video> <!-- ${s.label} -->`;
}).join('\n');
const presenterClips = plan.bakedAroll === false ? videoClips
  : `      <video id="aroll" class="clip" src="assets/aroll.mp4" data-start="0" data-duration="${TOTAL}" data-media-start="0" data-track-index="0" muted playsinline preload="auto"></video> <!-- corte do apresentador (${segs.length} takes + L-cuts + ${RATE}x) gerado por scripts/bake.py -->`;
// presenterZoom.mode "scene" (ritmo de ~4 s): em vez de trocar o zoom em TODO corte de take (a cada ~2 s),
// troca uma vez em cada aparicao do apresentador (janela entre B-rolls de tela cheia) e, se a aparicao
// passar de `sceneMax` s, mais uma vez no corte de take mais proximo do meio dela.
if (PZ && PZ.mode === 'scene') {
  zoomCuts.length = 0; zoomIdx = 0;
  const fw = [...fullWins].sort((a, b) => a[0] - b[0]);
  const vis = []; let c0 = 0;
  for (const [a, b] of fw) { if (a > c0 + 0.05) vis.push([c0, a]); c0 = Math.max(c0, b); }
  if (TOTAL > c0 + 0.05) vis.push([c0, TOTAL]);
  const cuts = videoCutTimes;
  for (const [a, b] of vis) {
    zoomCuts.push({ t: r3(a), scale: PZ.scales[zoomIdx++ % PZ.scales.length] });
    // no split a troca de imagem do topo ja e o evento: sem zoom extra no meio
    const inSplit = (plan.broll || []).some(x => x.mode === 'split' && (() => { const [w0, w1] = brollWin(x); return w0 < b && w1 > a; })());
    if (!inSplit && b - a > (PZ.sceneMax ?? 4.6)) {
      const mid = (a + b) / 2;
      const cand = cuts.filter(t => t > a + 1.8 && t < b - 1.8).sort((x, y) => Math.abs(x - mid) - Math.abs(y - mid))[0];
      zoomCuts.push({ t: r3(cand ?? mid), scale: PZ.scales[zoomIdx++ % PZ.scales.length] });
    }
  }
}
volTweens.push(`tl.set("#presenter-zoom", { transformOrigin: "${PZ ? PZ.origin || '50% 42%' : '50% 42%'}" }, 0);`);
zoomCuts.forEach(z => volTweens.push(`tl.set("#presenter-zoom", { scale: ${z.scale} }, ${z.t});`));

// ---- voz ----
// BAKED (padrão): o J-cut inteiro (42 clipes + crossfades) é renderizado OFFLINE por
// scripts/mixaudio.py em assets/voz-mix.m4a e entra como UM elemento <audio>. Motivo: o Chrome
// carrega ~75 players de mídia por aba; com um clipe por take a composição passava de 160
// elementos e o preview ficava preto. O mix vem do mesmo edit-plan.json (work/mix-plan.json).
// Emenda ponta a ponta (reel Atul Gawande): a voz de cada take vai ate o inicio da voz do take seguinte
// (+ XFADE de crossfade, que cai no silencio do tail `aout`); nada de duas vozes somadas durante o lead.
// O video do take continua os 5 quadros de lead depois disso (out = aout + lead*rate): J-cut.
const mixVoice = segs.map((s, i) => {
  const next = segs[i + 1];
  const dur = next ? r3(next.audioStart - s.audioStart + XFADE) : s.sourceDur;
  return { label: s.label, start: s.audioStart, dur, in: s.in, out: r3(s.in + dur * RATE), first: s.i === 0, xfade: XFADE };
});
const voiceClips = plan.bakedAudio === false
  ? segs.map(s => {
      const start = s.audioStart, dur = s.sourceDur, end = r3(start + dur), track = 10 + (s.i % 2);
      if (s.i === 0) volTweens.push(`tl.fromTo("#voz${s.i}", { volume: 1 }, { volume: 1, duration: ${r3(dur - XFADE)}, ease: "none" }, 0);`);
      else volTweens.push(`tl.fromTo("#voz${s.i}", { volume: 0 }, { volume: 1, duration: ${r3(XFADE)}, ease: "none" }, ${start});`);
      volTweens.push(`tl.to("#voz${s.i}", { volume: 0, duration: ${r3(XFADE)}, ease: "none" }, ${r3(end - XFADE)});`);
      return `    <audio id="voz${s.i}" src="${plan.voiceSrc || plan.src}" data-start="${start}" data-duration="${dur}" data-media-start="${r3(s.in)}"${rateAttr} data-track-index="${track}"></audio> <!-- ${s.label} -->`;
    }).join('\n')
  : `    <audio id="voz-mix" src="assets/voz-mix.m4a" data-start="0" data-duration="${TOTAL}" data-media-start="0" data-track-index="10"></audio> <!-- voz com J-cut ${LEAD_FRAMES}f/${XFADE_FRAMES}f (gerada por scripts/mixaudio.py) -->`;

// ---- B-rolls ----
// mode "full": cobre a tela toda; mode "split": faixa de 44% do topo.
// Tomadas SEGUIDAS da mesma cena (janelas contíguas e mesmo modo) entram como UM elemento
// <video>, apontando para o arquivo concatenado por scripts/concat_broll.py — o movimento de
// câmera de cada tomada já vem gravado pelo make_broll.py. Isso derruba o número de players.
const shots = (plan.broll || []).map((b, k) => { const [t0, t1] = brollWin(b); return { ...b, k, t0, t1, dur: r3(t1 - t0) }; });
const groups = [];
shots.forEach(sh => {
  const last = groups[groups.length - 1];
  if (last && last.mode === sh.mode && Math.abs(last.t1 - sh.t0) < 0.02 && !sh.objectPosition && !last.objectPosition) {
    last.shots.push(sh); last.t1 = sh.t1;
  } else groups.push({ mode: sh.mode, t0: sh.t0, t1: sh.t1, shots: [sh] });
});
const brollClips = [];
const splitWindows = [];
groups.forEach((g, gi) => {
  const dur = r3(g.t1 - g.t0);
  const file = !g.shots[0].file ? '' : g.shots.length === 1 ? g.shots[0].file : `assets/broll/_cena${String(gi).padStart(2, '0')}.mp4`;
  g.file = file;
  const op = g.shots[0].objectPosition ? ` style="object-position: ${g.shots[0].objectPosition}"` : '';
  const nomes = g.shots.map(x => x.file.split('/').pop()).join(' + ');
  if (g.mode === 'split') {
    // kit v3: split com file "" = a faixa de cima e desenhada pela camada de motion (compositions/mg.html, splitIn/splitOut);
    // aqui fica so o wrapper (o apresentador continua sendo arrastado pelo split). Sem <video>: render mais leve.
    if (!g.shots[0].file) brollClips.push(`    <div class="broll-split-wrap" id="bsw${gi}"></div> <!-- split desenhado pela camada de motion -->`);
    else brollClips.push(`    <div class="broll-split-wrap" id="bsw${gi}"><video id="broll${gi}" class="clip" src="${file}" data-start="${g.t0}" data-duration="${dur}" data-media-start="0" data-track-index="${2 + (gi % 2)}"${op} muted playsinline preload="auto"></video></div> <!-- ${nomes} -->`);
    const last = splitWindows[splitWindows.length - 1];
    if (last && Math.abs(last.end - g.t0) < 0.02) { last.end = g.t1; last.lastK = gi; }
    else splitWindows.push({ start: g.t0, end: g.t1, firstK: gi, lastK: gi });
  } else if (plan.bakedBroll) {
    // bakedBroll: todas as cenas de tela cheia estao gravadas em assets/broll-full.mp4 (scripts/bake.py
    // brollfull), no tempo exato da timeline. Aqui so liga/desliga a camada na janela da cena.
    // Motivo: com um <video> por cena (27) + um por light-leak (29) o Chrome do Fabio esgotava os
    // decoders e os B-rolls sumiam no preview (a timeline mostrava os clipes, a imagem nao).
    volTweens.push(`tl.set("#bfw-all", { autoAlpha: 1 }, ${g.t0});`);
    volTweens.push(`tl.set("#bfw-all", { autoAlpha: 0 }, ${g.t1});`);
  } else {
    brollClips.push(`    <div class="broll-full-wrap" id="bfw${gi}"><video id="broll${gi}" class="clip" src="${file}" data-start="${g.t0}" data-duration="${dur}" data-media-start="0" data-track-index="${2 + (gi % 2)}"${op} muted playsinline preload="auto"></video></div> <!-- ${nomes} -->`);
    // Ken Burns só quando o arquivo não tem movimento próprio (make_broll já grava a câmera)
    if (plan.brollKenBurns) volTweens.push(`tl.fromTo("#bfw${gi}", { scale: 1 }, { scale: 1.07, duration: ${dur}, ease: "none" }, ${g.t0});`);
  }
});
if (plan.bakedBroll && groups.some(g => g.mode !== 'split')) {
  const nFull = groups.filter(g => g.mode !== 'split').length;
  brollClips.unshift(`    <div class="broll-full-wrap" id="bfw-all"><video id="broll-full" class="clip" src="assets/broll-full.mp4" data-start="0" data-duration="${TOTAL}" data-media-start="0" data-track-index="2" muted playsinline preload="auto"></video></div> <!-- ${nFull} cenas de tela cheia (gerada por scripts/bake.py brollfull) -->`);
}
fs.writeFileSync(path.join(ROOT, 'work/broll-groups.json'), JSON.stringify(groups.map(g => ({
  file: g.file, mode: g.mode, t0: g.t0, t1: g.t1,
  shots: g.shots.map(x => ({ file: x.file, dur: x.dur })),
})), null, 1));

// Transição tela cheia ⇄ split: apresentador é "arrastado" pra baixo enquanto o
// B-roll do topo desce junto revelando o split; na saída, ambos sobem de volta.
const SPLIT_Y = plan.splitShiftY ?? 710;
const TRANS = 0.55;
volTweens.push(`tl.set("#presenter-wrap", { transformOrigin: "50% 38%" }, 0);`);
splitWindows.forEach(w => {
  if (w.start === 0) {
    volTweens.push(`tl.set("#presenter-wrap", { y: ${SPLIT_Y} }, 0);`);
  } else {
    volTweens.push(`tl.fromTo("#presenter-wrap", { y: 0 }, { y: ${SPLIT_Y}, duration: ${TRANS}, ease: "power3.inOut" }, ${w.start});`);
    volTweens.push(`tl.fromTo("#bsw${w.firstK}", { yPercent: -100 }, { yPercent: 0, duration: ${TRANS}, ease: "power3.inOut" }, ${w.start});`);
  }
  volTweens.push(`tl.to("#presenter-wrap", { y: 0, duration: ${TRANS}, ease: "power3.inOut" }, ${r3(w.end - TRANS)});`);
  volTweens.push(`tl.to("#bsw${w.lastK}", { yPercent: -100, duration: ${TRANS}, ease: "power3.inOut" }, ${r3(w.end - TRANS)});`);
});
// Push-in lento no encerramento (CTA)
const ctaSegIdx = plan.ctaSeg ?? 12;
const ctaStart = segs[ctaSegIdx] ? segs[ctaSegIdx].tStart : null;
if (ctaStart != null) volTweens.push(`tl.fromTo("#presenter-wrap", { scale: 1 }, { scale: 1.05, duration: ${r3(TOTAL - ctaStart)}, ease: "none" }, ${ctaStart});`);

// ---- legendas (palavra-a-palavra → chunks de até 3 palavras) ----
const meta = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(ROOT, 'assets/chunks/meta.json'), 'utf8')).map(m => [m.i, m]));
const norm = w => w.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]/g, '');
function segWords(seg) {
  const ch = seg.chunk;
  const off = meta[ch].off;
  const j = JSON.parse(fs.readFileSync(path.join(ROOT, `assets/chunks/ch${String(ch).padStart(2, '0')}-words.json`), 'utf8'));
  const words = [];
  for (const e of j.transcription) {
    const text = e.text.trim();
    if (!text || /^\[.*\]$/.test(text)) continue;
    const src = off + e.offsets.from / 1000;
    const srcEnd = off + e.offsets.to / 1000;
    // legenda so ate o fim da VOZ do take (aout): o video segura o lead e pode conter o comeco do take seguinte
    if (srcEnd < seg.in - 0.05 || src > (seg.aout ?? seg.out) + 0.05) continue;
    words.push({ text, t: r3(Math.max(seg.audioStart, seg.audioStart + (src - seg.in) / RATE)) });
  }
  return words;
}
const capDivs = [];
const typingSfx = [];
const bigDivs = [];
let capId = 0, bigId = 0, typingDone = false;
const impacts = plan.impacts || [];
// janelas com B-roll na tela (split ou full): legenda fica no centro (44%);
// apresentador sozinho em tela cheia: legenda desce (cap-low) pra não cobrir o rosto
const brollWindows = (plan.broll || []).map(brollWin);
const overBroll = (a, b) => brollWindows.some(([w0, w1]) => (a + b) / 2 >= w0 && (a + b) / 2 < w1);
segs.forEach(seg => {
  if (seg.chunk === undefined) return;
  const words = segWords(seg);
  if (!words.length) return;
  // hookSeg: o gancho aparece INTEIRO desde o frame 0 (capa do reel), numa caixa só.
  // Padrão do formato: hookSeg = 0. Para desligar (voltar às legendas de 3 palavras no gancho),
  // usar "hookSeg": null no plano.
  if ((plan.hookSeg === undefined ? 0 : plan.hookSeg) === seg.i) {
    const hookEnd = segs[seg.i + 1]?.audioStart ?? seg.tEnd;
    const hookStart = seg.i === 0 ? 0 : seg.audioStart;
    const hookDur = r3(hookEnd - hookStart);
    capDivs.push(`    <div id="cap${capId++}" class="clip cap cap-hook" data-start="${hookStart}" data-duration="${hookDur}" data-track-index="5"><span id="hook-box" class="hook-box"><span class="hook-shine" id="hook-shine"></span><span class="hook-text">${words.map(w => w.text).join(' ')}</span></span></div>`);
    // Efeitos do gancho (seek-safe, no timeline): caixa completa já no frame 0 (capa);
    // pulso suave de escala + brilho atravessando a caixa duas vezes.
    const half = r3(hookDur / 4);
    volTweens.push(`tl.fromTo("#hook-box", { scale: 1 }, { scale: 1.018, duration: ${half}, ease: "sine.inOut", repeat: 3, yoyo: true }, ${hookStart});`);
    volTweens.push(`tl.fromTo("#hook-shine", { xPercent: -160 }, { xPercent: 260, duration: 0.9, ease: "power2.inOut" }, ${r3(hookStart + 0.5)});`);
    volTweens.push(`tl.fromTo("#hook-shine", { xPercent: -160 }, { xPercent: 260, duration: 0.9, ease: "power2.inOut", immediateRender: false }, ${r3(hookStart + Math.max(1.6, hookDur - 1.6))});`);
    return;
  }
  // Durante o J-cut há duas falas em crossfade. A legenda nova ganha prioridade:
  // a legenda do take anterior encerra assim que a próxima voz começa.
  const segTextEnd = segs[seg.i + 1]?.audioStart ?? seg.tEnd;
  // localizar frases de impacto neste segmento
  const wnorm = words.map(w => norm(w.text));
  const zones = [];
  for (const imp of impacts) {
    if (imp.seg !== undefined && imp.seg !== seg.i) continue; // callout preso a um segmento
    const pw = imp.phrase.split(/\s+/).map(norm);
    for (let i = 0; i + pw.length <= wnorm.length; i++) {
      if (pw.every((p, k) => wnorm[i + k] === p)) {
        const start = words[i].t;
        const endW = words[i + pw.length]; // início da palavra seguinte (ou fim do seg)
        const supEnd = r3(endW ? Math.min(endW.t, segTextEnd) : segTextEnd); // supressão só durante a frase
        const end = r3(Math.min(segTextEnd, supEnd + (imp.hold ?? 0.7))); // callout segura o hold
        zones.push({ start, supEnd, end, imp });
        break;
      }
    }
  }
  // chunks normais (até 3 palavras, quebra em pontuação), pulando as zonas de impacto
  const inZone = tt => zones.some(z => tt >= z.start - 0.001 && tt < z.supEnd);
  let group = [];
  const flush = nextT => {
    if (!group.length) return;
    const start = group[0].t;
    const end = r3(Math.min(segTextEnd, nextT));
    if (end - start < 0.1) { group = []; return; }
    const text = group.map(w => w.text).join(' ');
    const yellow = (plan.yellowCapSegs || []).includes(seg.i) ? ' cap-yellow' : '';
    // capLowSegs: força a legenda baixa mesmo sobre B-roll — usado quando o B-roll
    // tem informação importante na faixa dos 44% (ex.: logotipo no meio do quadro).
    const forceLow = (plan.capLowSegs || []).includes(seg.i);
    // reel HERB KELLEHER: dentro do SPLIT a legenda fica sempre na divisa (44%) — a 76% ela cai na boca do
    // apresentador (a faixa de baixo e o rosto). capLowSegs so vale sobre B-roll de TELA CHEIA.
    const mid = (start + end) / 2;
    const inSplitWin = splitWindows.some(w => Math.min(end, w.end) - Math.max(start, w.start) > 0.08);
    const overFull = fullWins.some(([w0, w1]) => mid >= w0 && mid < w1);
    const low = inSplitWin ? '' : (overFull ? (forceLow ? ' cap-low' : '') : (overBroll(start, end) ? '' : ' cap-low'));
    const capTrack = 5 + 2 * (seg.i % 2); // 5/7 pingue-pongue para captions sobrepostos pelo J-cut
    capDivs.push(`    <div id="cap${capId++}" class="clip cap${yellow}${low}" data-start="${start}" data-duration="${r3(end - start)}" data-track-index="${capTrack}">${text}</div>`);
    group = [];
  };
  words.forEach((w, i) => {
    if (inZone(w.t)) { flush(w.t); return; }
    group.push(w);
    const punct = /[.,!?;:]$/.test(w.text);
    const next = words[i + 1];
    const nextT = next ? next.t : segTextEnd;
    if (group.length >= 3 || punct || !next || inZone(nextT)) flush(nextT);
  });
  // callouts grandes
  for (const z of zones) {
    const lines = (z.imp.lines || [z.imp.phrase.toUpperCase()]).map(l => l.toUpperCase());
    const html = lines.join('<br/>');
    const dur = r3(z.end - z.start);
    if (z.imp.style === 'typing' && !typingDone) {
      typingDone = true;
      // spans por caractere para o efeito de digitação
      const chars = [];
      let ci = 0;
      for (const line of lines) {
        for (const c of line) chars.push(`<span class="tc" id="tc${ci++}">${c === ' ' ? '&nbsp;' : c}</span>`);
        chars.push('<br/>');
      }
      chars.pop();
      // impacts[].top tambem no callout de digitacao (o B-roll pode ter rosto na faixa dos 30%)
      const topT = z.imp.top != null ? ` style="top: ${z.imp.top}%"` : '';
      bigDivs.push(`    <div id="big${bigId}" class="clip cap-big"${topT} data-start="${z.start}" data-duration="${dur}" data-track-index="6"><span class="inner">${chars.join('')}</span></div>`);
      // reel KAZUO INAMORI: callout de digitacao curto (1,1 s, fecha o take) — a digitacao tem que acabar a tempo do pulso (0,14 s) fechar antes da saida
      const typeDur = Math.min(1.35, dur * 0.7, Math.max(0.3, dur - 0.2 - 0.14 - F(2)));
      const per = r3(typeDur / ci);
      volTweens.push(`for (let i = 0; i < ${ci}; i++) tl.set("#tc" + i, { autoAlpha: 1 }, ${z.start} + ${per} * i);`);
      // settle: pulso de escala quando a digitação completa + saída suave
      const tEndType = r3(z.start + typeDur);
      volTweens.push(`tl.fromTo("#big${bigId} .inner", { scale: 1 }, { scale: 1.06, duration: 0.14, ease: "power2.out" }, ${tEndType});`);
      // o settle tem que FECHAR antes da saída começar (1 quadro de folga): com duração fixa
      // de 0,21 s ele invadia a saída em callout curto e o linter acusava tweens concorrentes
      const tExit = r3(z.start + dur - 0.2);
      // callout curto (a frase fecha o take e a voz seguinte entra logo): sem espaco para o settle,
      // a saida parte direto da escala 1.06 (reel Atul Gawande, "NAO ERRA POR BURRICE": 1,27 s)
      const settleRoom = r3(Math.min(0.21, tExit - (tEndType + 0.15) - F(1)));
      if (settleRoom >= 0.06) volTweens.push(`tl.to("#big${bigId} .inner", { scale: 1, duration: ${settleRoom}, ease: "power2.inOut" }, ${r3(tEndType + 0.15)});`);
      volTweens.push(`tl.to("#big${bigId} .inner", { autoAlpha: 0, scale: 1.1, duration: 0.2, ease: "power2.in" }, ${tExit});`);
      volTweens.push(`tl.set("#big${bigId} .inner", { autoAlpha: 0 }, ${r3(z.start + dur)});`);
      // drum-fill simulando a digitação
      typingSfx.push({ file: 'assets/sfx/drum-fill.m4a', start: z.start, dur: 1.43, vol: 0.3, nome: 'drum-fill do callout de digitação' });
    } else {
      // impacts[].top: altura do callout em % (padrao 30%) — quando o B-roll tem o rosto na faixa dos 30%
      const topSt = z.imp.top != null ? ` style="top: ${z.imp.top}%"` : '';
      bigDivs.push(`    <div id="big${bigId}" class="clip cap-big"${topSt} data-start="${z.start}" data-duration="${dur}" data-track-index="6"><span class="inner">${html}</span></div>`);
      // pop fluido: entra com back-ease + leve rotação, cresce devagar, sai limpo
      // deixa 1 frame de folga antes da saída para evitar tweens concorrentes
      const grow = Math.max(0.12, r3(dur - 0.42 - 0.24));
      volTweens.push(`tl.fromTo("#big${bigId} .inner", { scale: 0.5, rotation: -5, y: 44, autoAlpha: 0 }, { scale: 1, rotation: 0, y: 0, autoAlpha: 1, duration: 0.42, ease: "back.out(2.4)" }, ${z.start});`);
      volTweens.push(`tl.to("#big${bigId} .inner", { scale: 1.07, duration: ${grow}, ease: "power1.inOut" }, ${r3(z.start + 0.43)});`);
      volTweens.push(`tl.to("#big${bigId} .inner", { autoAlpha: 0, scale: 1.14, duration: 0.22, ease: "power2.in" }, ${r3(z.start + dur - 0.22)});`);
      volTweens.push(`tl.set("#big${bigId} .inner", { autoAlpha: 0 }, ${r3(z.start + dur)});`);
      // punch-in no apresentador quando o callout estoura em tela cheia (sem B-roll)
      if (!overBroll(z.start, z.start)) {
        volTweens.push(`tl.to("#presenter-wrap", { scale: 1.07, duration: 0.18, ease: "power3.out" }, ${z.start});`);
        volTweens.push(`tl.to("#presenter-wrap", { scale: 1, duration: 0.45, ease: "power2.inOut" }, ${r3(z.start + 0.2)});`);
      }
    }
    bigId++;
  }
});

// ---- light-leaks + whoosh nas transições de cena ----
// Pontos de transição: cortes de seção (plan.sections) + entradas e saídas de cada cena de
// B-roll. Cada um leva um light-leak (0,7 s, começando 10f antes) e um one-shot de whoosh /
// swoosh / whoosh-transition alternados. Espaçamento mínimo `leakMinGap` para não virar
// cama rítmica sobre a fala (regra de ouro do mix).
const LEAK_MIN_GAP = plan.leakMinGap ?? 2.4;
const pontos = [];
plan.sections.forEach(sec => pontos.push({ t: segs[sec.afterSegment].tEnd, nome: sec.name }));
groups.forEach(g => {
  pontos.push({ t: g.t0, nome: `entra ${g.file.split('/').pop()}` });
  // cortes DENTRO da cena concatenada também levam transição (sem isso o trecho lia como
  // "um B-roll só, sem nada" — reclamação real do usuário no trecho 42-56 s)
  let t = g.t0;
  g.shots.slice(0, -1).forEach(sh => { t = r3(t + sh.dur); pontos.push({ t, nome: `corte ${sh.file.split('/').pop()}` }); });
  pontos.push({ t: g.t1, nome: `sai ${g.file.split('/').pop()}` });
});
const trans = [];
pontos.sort((x, y) => x.t - y.t).forEach(p => {
  if (p.t < 0.5 || p.t > TOTAL - 0.4) return;
  const last = trans[trans.length - 1];
  if (last && p.t - last.t < LEAK_MIN_GAP) return;
  trans.push(p);
});
const leaks = [], leakTimes = [], sfxEvents = [...typingSfx];
trans.forEach((p, k) => {
  const start = r3(Math.max(0, p.t - LEAK_PRE));
  leakTimes.push({ start, nome: p.nome });
  if (!plan.bakedLeaks) leaks.push(`    <video id="leak${k}" class="clip leak" src="assets/transicao-light-leak.mp4" data-start="${start}" data-duration="${LEAK_DUR}" data-track-index="4" muted playsinline preload="auto"></video> <!-- ${p.nome} @${r3(p.t)}s -->`);
  const pick = [['whoosh', 1.2], ['swoosh', 0.98], ['whoosh-transition', 2.1]][k % 3];
  sfxEvents.push({ file: `assets/sfx/${pick[0]}.mp3`, start, dur: pick[1], vol: 0.18, nome: p.nome });
});

if (plan.bakedLeaks) leaks.push(`    <video id="leaks" class="clip leak" src="assets/leaks.mp4" data-start="0" data-duration="${TOTAL}" data-media-start="0" data-track-index="4" muted playsinline preload="auto"></video> <!-- ${leakTimes.length} light-leaks (gerada por scripts/bake.py leaks) -->`);
fs.writeFileSync(path.join(ROOT, 'work/leaks.json'), JSON.stringify({ total: TOTAL, dur: LEAK_DUR, file: 'assets/transicao-light-leak.mp4', leaks: leakTimes }, null, 1));

// ---- SFX fixos (todos vão para a faixa pronta assets/bed.m4a) ----
const climaxSec = plan.sections.find(s => /cl[ií]max/i.test(s.name));
const climaxT = climaxSec ? segs[climaxSec.afterSegment].tEnd : null;
sfxEvents.push({ file: 'assets/sfx/intro-cinematic-opening.mp3', start: 0, dur: 3.2, vol: 0.25, nome: 'intro opening' });
sfxEvents.push({ file: 'assets/sfx/intro-when-emphasizing-riser.mp3', start: 0, dur: 3.2, vol: 0.22, nome: 'intro riser' });
sfxEvents.push({ file: 'assets/sfx/boom-cinematic.mp3', start: 4.8, dur: 4, vol: 0.12, nome: 'boom' });
// reel SUN TZU: o callout de digitacao caiu em 7,7 s — dois drum-fills sobrepostos embolam; o da digitacao fecha a intro sozinho
if (!typingSfx.some(e => e.start > 5.5 && e.start < 9.5))
  sfxEvents.push({ file: 'assets/sfx/drum-fill.m4a', start: 7.0, dur: 1.43, vol: 0.166, nome: 'drum-fill da intro' });
if (climaxT != null) {
  sfxEvents.push({ file: 'assets/sfx/riser.mp3', start: r3(Math.max(0, climaxT - 3)), dur: 3, vol: 0.2, nome: 'riser do clímax' });
  sfxEvents.push({ file: 'assets/sfx/impact-hit.mp3', start: climaxT, dur: 2.5, vol: 0.3, nome: 'impact do clímax' });
}

// ---- trilha + bed ----
// trilhaLoop: quando o reel é mais longo que a trilha (164 s), a 2ª cópia entra em `at` recuada
// `back` s (nº inteiro de compassos: batida em fase), com crossfade `xfade`.
// A trilha e todos os SFX são renderizados OFFLINE em assets/bed.m4a (scripts/mixaudio.py):
// um elemento <audio> em vez de ~20 (limite de players do Chrome).
const TRILHA_VOL = plan.trilhaVol ?? 0.079;
const loop = plan.trilhaLoop && TOTAL > plan.trilhaLoop.at ? plan.trilhaLoop : null;
const trilhaMix = { file: 'assets/trilha-epic-cinematic-corporate.mp3', vol: TRILHA_VOL, loop, fadeLow: 0.045, lowAt: r3(Math.max((loop ? loop.at : 0) + 3, TOTAL - 9)), endFade: 0.7 };
const trilha = `    <audio id="bed" src="assets/bed.m4a" data-start="0" data-duration="${TOTAL}" data-media-start="0" data-track-index="17"></audio> <!-- trilha + ${sfxEvents.length} SFX (gerada por scripts/mixaudio.py) -->`;
fs.writeFileSync(path.join(ROOT, 'work/mix-plan.json'), JSON.stringify({
  total: TOTAL, fps: FPS, rate: RATE, voiceSrc: plan.voiceSrc || plan.src,
  voice: mixVoice, sfx: sfxEvents.sort((x, y) => x.start - y.start), trilha: trilhaMix,
}, null, 1));

const block = [
  `    <!-- EDIT:BEGIN (gerado por scripts/build-edit.mjs — não editar à mão) -->`,
  `    <!-- Duração total: ${TOTAL}s (${Math.round(TOTAL * FPS)} frames @${FPS}fps) · rate ${RATE}x -->`,
  `    <div id="presenter-wrap"><div id="presenter-zoom">`,
  presenterClips,
  `    </div></div>`,
  `    <!-- Voz independente com J-cut (lead ${LEAD_FRAMES}f) + crossfade ${XFADE_FRAMES}f -->`,
  voiceClips,
  `    <!-- B-rolls -->`,
  ...brollClips,
  ...(plan.mg ? [`    <!-- Motion graphics (sub-composição ${plan.mg.src}, skill showreel-interface): por cima do apresentador e do B-roll, abaixo dos light-leaks e das legendas -->`,
    `    <div id="mg-host" data-composition-id="${plan.mg.id}" data-composition-src="${plan.mg.src}" data-start="0" data-duration="${TOTAL}" data-track-index="8" data-width="1080" data-height="1920" style="position:absolute;left:0;top:0;width:1080px;height:1920px;z-index:30"></div>`] : []),
  `    <!-- Legendas -->`,
  ...capDivs,
  ...bigDivs,
  `    <!-- Transições light-leak -->`,
  ...leaks,
  `    <!-- Trilha + SFX (faixa pronta) -->`,
  trilha,
  `    <!-- EDIT:END -->`,
].join('\n');

const idx = path.join(ROOT, 'index.html');
let html = fs.readFileSync(idx, 'utf8');
html = html.replace(/ {4}<!-- EDIT:BEGIN[\s\S]*?<!-- EDIT:END -->/, block);
const jsBlock = [`      // EDIT-TWEENS:BEGIN (gerado — crossfades, splits, callouts, trilha)`, ...volTweens.map(l => `      ${l}`), `      // EDIT-TWEENS:END`].join('\n');
html = html.replace(/ {6}\/\/ EDIT-TWEENS:BEGIN[\s\S]*?\/\/ EDIT-TWEENS:END/, jsBlock);
html = html.replace(/(id="root"[^>]*data-duration=")[^"]*(")/, `$1${TOTAL}$2`);
fs.writeFileSync(idx, html);

// ---- passes de camada para o pacote conformável (NLE) ----
// Mesma composição, com uma classe no <html> que liga/desliga camadas via CSS.
// Deterministas: nenhum estado de runtime, só o seletor muda.
// OPT-IN (`--passes`): na raiz eles contam como composições-raiz duplicadas e o
// `hyperframes check` reprova. Gerar só na hora do export e apagar depois.
const PASSES = process.argv.includes('--passes');
for (const layer of PASSES ? ['clean', 'gfx', 'leaks'] : []) {
  const passHtml = html.replace(/<html\b([^>]*)>/, (m, attrs) =>
    /class="/.test(attrs)
      ? `<html${attrs.replace(/class="([^"]*)"/, `class="$1 layers-${layer}"`)}>`
      : `<html${attrs} class="layers-${layer}">`);
  fs.writeFileSync(path.join(ROOT, `pass-${layer}.html`), passHtml);
}

if (PASSES) console.log('passes de camada: pass-clean.html, pass-gfx.html, pass-leaks.html');
console.log(`OK: ${segs.length} segs, ${TOTAL}s, ${brollClips.length} cenas de broll (${shots.length} tomadas), ${sfxEvents.length} sfx, ${capId} legendas, ${bigId} callouts, ${leakTimes.length} leaks, J-cut ${LEAD_FRAMES}f/${XFADE_FRAMES}f.`);
```


---

# ARQUIVO: `modelo-projeto/scripts/bake.py`

```python
"""Renderiza offline as faixas pesadas da composição, a partir do edit-plan.json:
  aroll  -> assets/aroll.mp4      (corte do apresentador: takes + L-cuts + velocidade)
  voz    -> assets/voz-mix.m4a    (J-cut: clipes + crossfades no silêncio)
  bed    -> assets/bed.m4a        (trilha com emenda/automação + todos os SFX)
  cenas  -> assets/broll/_cenaNN.mp4 (tomadas seguidas da mesma cena num arquivo)
  brollfull -> assets/broll-full.mp4 (todas as cenas de tela cheia numa faixa, no tempo da timeline)
  leaks  -> assets/leaks.mp4       (todos os light-leaks numa faixa)
Motivo: o Chrome cria um player (e uma sessão de decodificação) por <video>/<audio>; com um
elemento por take a composição passava de 160 elementos e a imagem sumia no preview.
Uso: python3 scripts/bake.py [aroll|voz|bed|cenas ...]   (sem argumento = tudo)
"""
import json, math, os, shutil, subprocess, sys, tempfile
FPS=60                      # quadros do ARQUIVO de saida (2K/60)
P=json.load(open('assets/edit-plan.json'))
# A matematica da TIMELINE (lead do J-cut, duracao minima de take) tem que usar o MESMO fps
# do gerador (plan.fps, 30) — com 60 aqui o lead virava 5/60 e cada take saia 0,083 s mais
# longo: o aroll fechou 3671 quadros contra 3555 da timeline (1,9 s de dessincronia).
TLFPS=P.get('fps',30)
M=json.load(open('work/mix-plan.json'))
RATE=P.get('rate',1.1); TOTAL=M['total']
def run(cmd): subprocess.run(cmd,check=True)
import platform
ENC_AROLL=(['-c:v','libx264','-crf','16','-preset','medium'] if os.environ.get('BAKE_X264') or platform.system()!='Darwin'
           else ['-c:v','h264_videotoolbox','-b:v','45M','-maxrate','60M','-profile:v','high'])
def nf(d): return int(round(d*FPS))

def bake_aroll():
    """Concatena os takes do mezanino já na velocidade final (vídeo mudo)."""
    F=1/TLFPS; LEAD=P.get('jcutLeadFrames',5)*F
    segs=[];t=0
    for i,s in enumerate(P['segments']):
        sd=round((s['out']-s['in'])/RATE,3); lead=0 if i==0 else min(LEAD,sd-10*F); d=round(sd-lead,3)
        segs.append(dict(i=i,**s,lead=lead,dur=d,t0=round(t,3))); t=round(t+d,3)
    ed=[round((s['out']-s['videoTail'])/RATE,3) if s.get('videoTail') else 0 for s in segs]
    tmp=tempfile.mkdtemp(prefix='aroll'); parts=[]
    # fronteiras de quadro ACUMULADAS: cada take começa no quadro em que a timeline o coloca
    # (arredondar take por take somava erro e o arquivo saía 3 quadros curto, tirando o lip-sync)
    jobs=[]
    for k,s in enumerate(segs):
        dPrev=ed[k-1] if k>0 else 0
        vStart=round(s['t0']-dPrev,3); vEnd=round(s['t0']+s['dur']-ed[k],3)
        frames=nf(vEnd)-nf(vStart); vMedia=round(s['in']+(s['lead']-dPrev)*RATE,3)
        out=f'{tmp}/p{k:03d}.mp4'
        jobs.append(['ffmpeg','-v','error','-y','-ss',f'{vMedia:.3f}','-i',P['src'],
             # setpts + fps nesta ordem: com '-r' no lugar do filtro fps o conteúdo saía
             # 2 quadros atrasado dentro de cada take (medido quadro a quadro)
             '-vf',f'setpts=PTS/{RATE},fps={FPS}','-frames:v',str(frames),
             # -g 30: sem GOP denso o renderizador avisa "sparse keyframes ... causes seek
             # failures and frame freezing" e a captura TRAVA num quadro (reel Costco: parou
             # em 572/600, duas vezes no mesmo quadro).
             # crf 16 (era 18): o aroll e' a imagem principal do reel — pedido "sem perder nada de qualidade"
             # kit v3: no Mac, codificador de HARDWARE (VideoToolbox) a 45 Mb/s: 4,3x mais rapido e PSNR igual ou melhor
             # que x264 crf 16 medium (43,9 x 43,7 dB, reel Alan Mulally); GOP 30 respeitado. BAKE_X264=1 volta ao x264.
             *ENC_AROLL,'-pix_fmt','yuv420p',
             '-g','30','-keyint_min','30','-sc_threshold','0','-an',out])
        parts.append(out)
    from concurrent.futures import ThreadPoolExecutor   # kit v3: 3 takes de cada vez
    with ThreadPoolExecutor(3) as ex: list(ex.map(run, jobs))
    lst=f'{tmp}/list.txt'; open(lst,'w').write('\n'.join(f"file '{p}'" for p in parts))
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-c','copy','-movflags','+faststart','assets/aroll.mp4'])
    n=subprocess.run(['ffprobe','-v','error','-select_streams','v','-count_frames','-show_entries','stream=nb_read_frames','-of','csv=p=0','assets/aroll.mp4'],capture_output=True,text=True).stdout.strip().rstrip(',')
    shutil.rmtree(tmp,ignore_errors=True)
    print(f'  aroll.mp4  {int(n)} quadros (timeline {nf(TOTAL)}) · {len(parts)} takes')

def bake_voz():
    """Mix do J-cut: cada take na velocidade final, com fade de crossfade dentro do silêncio."""
    ins=[];fc=[];n=0
    for v in M['voice']:
        ins+=['-ss',f"{v['in']:.3f}",'-t',f"{(v['out']-v['in']):.3f}",'-i',M['voiceSrc']]
        xf=v['xfade']
        f=f"[{n}:a]atempo={RATE},asetpts=N/SR/TB"
        if not v['first']: f+=f",afade=t=in:st=0:d={xf:.3f}"
        f+=f",afade=t=out:st={max(0,v['dur']-xf):.3f}:d={xf:.3f}"
        f+=f",adelay={int(v['start']*1000)}|{int(v['start']*1000)}[a{n}]"
        fc.append(f); n+=1
    fc.append(''.join(f'[a{i}]' for i in range(n))+f'amix=inputs={n}:normalize=0:dropout_transition=0[out]')
    run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[out]',
         '-t',f'{TOTAL:.3f}','-c:a','aac','-b:a','256k','-ar','48000','-ac','2','assets/voz-mix.m4a'])
    print(f'  voz-mix.m4a  {n} takes')

def bake_bed():
    """Trilha (com emenda e automação de volume) + todos os SFX one-shot."""
    T=M['trilha']; V=T['vol']; low=T['lowAt']; loop=T['loop']
    # automação: V até lowAt, 1 s para 0.045, e fade final de 0,7 s
    aut=(f"volume=eval=frame:volume='({V}+({T['fadeLow']}-{V})*max(0,min(1,(t-{low})/1)))"
         f"*(1-max(0,min(1,(t-{TOTAL-T['endFade']})/{T['endFade']})))'")
    ins=[];fc=[];n=0
    if loop:
        at,back,xf=loop['at'],loop['back'],loop.get('xfade',2.5)
        ins+=['-i',T['file']]; fc.append(f"[{n}:a]atrim=0:{at+xf},asetpts=N/SR/TB,afade=t=out:st={at}:d={xf},{aut}[t0]"); n+=1
        ins+=['-ss',f'{at-back:.3f}','-i',T['file']]
        fc.append(f"[{n}:a]atrim=0:{TOTAL-at},asetpts=N/SR/TB,afade=t=in:st=0:d={xf},adelay={int(at*1000)}|{int(at*1000)},{aut}[t1]"); n+=1
        beds=['[t0]','[t1]']
    else:
        ins+=['-i',T['file']]; fc.append(f"[{n}:a]atrim=0:{TOTAL},asetpts=N/SR/TB,{aut}[t0]"); n+=1; beds=['[t0]']
    for s in M['sfx']:
        ins+=['-i',s['file']]
        fc.append(f"[{n}:a]atrim=0:{s['dur']},asetpts=N/SR/TB,volume={s['vol']},adelay={int(s['start']*1000)}|{int(s['start']*1000)}[s{n}]")
        beds.append(f'[s{n}]'); n+=1
    fc.append(''.join(beds)+f'amix=inputs={len(beds)}:normalize=0:dropout_transition=0[out]')
    run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[out]',
         '-t',f'{TOTAL:.3f}','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','assets/bed.m4a'])
    print(f"  bed.m4a  trilha{' + emenda' if loop else ''} + {len(M['sfx'])} SFX")

def bake_cenas():
    """Tomadas seguidas da mesma cena num arquivo só, cada uma cortada no quadro exato."""
    G=json.load(open('work/broll-groups.json')); n=0
    for g in G:
        if len(g['shots'])<2 or not g['file']: continue  # kit v3: split da camada de motion nao tem arquivo
        ins=[];fc=[]
        # fronteiras por quadro ACUMULADO da janela: arredondar tomada a tomada perdia ate um
        # quadro no fim da cena (o arquivo ficava mais curto que a janela do index.html)
        acc=g['t0']; prev=nf(g['t0'])
        for k,sh in enumerate(g['shots']):
            acc=round(acc+sh['dur'],6); cur=nf(acc); nfr=cur-prev; prev=cur
            if k==len(g['shots'])-1: nfr+=3   # folga (como no make_broll): a janela pede ate
            # ceil((start+dur)*30)-1, que cai alguns milissegundos depois do ultimo quadro exato
            ins+=['-i',sh['file']]
            fc.append(f"[{k}:v]trim=end_frame={nfr},setpts=N/{FPS}/TB,setsar=1[v{k}]")
        fc.append(''.join(f'[v{k}]' for k in range(len(g['shots'])))+f"concat=n={len(g['shots'])}:v=1:a=0[out]")
        run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[out]','-r',str(FPS),
             '-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p',
             '-g','30','-keyint_min','30','-sc_threshold','0','-an','-movflags','+faststart',g['file']])
        d=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',g['file']],capture_output=True,text=True).stdout.strip()
        print(f"  {g['file'].split('/')[-1]}  {float(d):.2f}s (janela {g['t1']-g['t0']:.2f}s) · {len(g['shots'])} tomadas"); n+=1
    print(f'  {n} cenas concatenadas')

def _enc(args,out):
    run(['ffmpeg','-v','error','-y',*args,'-c:v','libx264','-crf','18','-preset','medium','-pix_fmt','yuv420p',
         '-g','30','-keyint_min','30','-sc_threshold','0','-an',out])
def _black(n,out):
    _enc(['-f','lavfi','-i',f'color=c=black:s=1440x2560:r={FPS}','-frames:v',str(n)],out)
def _concat(parts,out):
    lst=out+'.txt'; open(lst,'w').write('\n'.join(f"file '{os.path.abspath(p)}'" for p in parts))
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-c','copy','-movflags','+faststart',out]); os.remove(lst)
def _nframes(f):
    return int(subprocess.run(['ffprobe','-v','error','-select_streams','v','-count_frames','-show_entries','stream=nb_read_frames','-of','csv=p=0',f],capture_output=True,text=True).stdout.strip().rstrip(','))

def bake_brollfull():
    """Todas as cenas de B-roll de TELA CHEIA numa faixa so, no tempo exato da timeline (preto entre elas;
    a composicao so mostra a camada dentro das janelas). Um <video> no lugar de ~27: com um player por
    cena + um por light-leak o Chrome esgotava os decoders e o B-roll sumia no preview."""
    G=sorted([g for g in json.load(open('work/broll-groups.json')) if g['mode']!='split'],key=lambda g:g['t0'])
    if not G: print('  broll-full: nenhuma cena de tela cheia em video (camada de motion) — pulado'); return
    tmp=tempfile.mkdtemp(prefix='bfull'); parts=[]; c=0; END=nf(TOTAL)
    for k,g in enumerate(G):
        # conteudo cobre floor(t0) .. ceil(t1): a camada liga em t0 e desliga em t1, entao a imagem
        # tem que existir no quadro inteiro que contem cada borda (senao pisca 1 quadro preto)
        s0=max(c,math.floor(g['t0']*FPS)); e0=min(END,math.ceil(g['t1']*FPS))
        if s0>c: b=f'{tmp}/b{k:03d}.mp4'; _black(s0-c,b); parts.append(b)
        n=e0-s0; o=f'{tmp}/g{k:03d}.mp4'
        _enc(['-i',g['file'],'-vf',f'fps={FPS},scale=1440:2560,setsar=1','-frames:v',str(n)],o)
        got=_nframes(o)
        if got<n: raise SystemExit(f"{g['file']} tem {got} quadros, precisa de {n}")
        parts.append(o); c=e0
    if END>c: b=f'{tmp}/bfim.mp4'; _black(END-c,b); parts.append(b)
    _concat(parts,'assets/broll-full.mp4'); shutil.rmtree(tmp,ignore_errors=True)
    print(f"  broll-full.mp4  {_nframes('assets/broll-full.mp4')} quadros (timeline {END}) · {len(G)} cenas")

def bake_leaks():
    """Todos os light-leaks numa faixa so (preto no resto: com blend screen, preto nao altera a imagem)."""
    L=json.load(open('work/leaks.json')); tmp=tempfile.mkdtemp(prefix='leaks'); END=nf(TOTAL)
    one=f'{tmp}/leak.mp4'; _enc(['-i',L['file'],'-vf',f'fps={FPS},scale=1440:2560,setsar=1'],one); nl=_nframes(one)
    parts=[]; c=0
    for k,x in enumerate(L['leaks']):
        s0=max(c,nf(x['start'])); n=min(nl,END-s0)
        if s0>c: b=f'{tmp}/b{k:03d}.mp4'; _black(s0-c,b); parts.append(b)
        if n<nl: o=f'{tmp}/l{k:03d}.mp4'; _enc(['-i',one,'-frames:v',str(n)],o); parts.append(o)
        else: parts.append(one)
        c=s0+n
    if END>c: b=f'{tmp}/bfim.mp4'; _black(END-c,b); parts.append(b)
    _concat(parts,'assets/leaks.mp4'); shutil.rmtree(tmp,ignore_errors=True)
    print(f"  leaks.mp4  {_nframes('assets/leaks.mp4')} quadros (timeline {END}) · {len(L['leaks'])} leaks")

alvos=sys.argv[1:] or ['cenas','brollfull','leaks','voz','bed','aroll']
for a in alvos: globals()['bake_'+a]()
```


---

# ARQUIVO: `modelo-projeto/scripts/render-chunks.mjs`

```javascript
#!/usr/bin/env node
// Render em PARTES para máquinas com pouca memória (MacBook Air 8 GB): o renderizador local trava
// ("Sequential screenshot capture stalled") depois de ~800 quadros numa mesma sessão do Chrome.
// Cada parte é uma cópia do index.html com os tempos deslocados:
//   - elementos temporizados: data-start -= A (o que começa antes vira 0 e avança data-media-start)
//   - vídeos fora da janela são removidos (o wrapper fica, as animações seguem válidas); áudio removido
//   - animações: a timeline original é tocada de A a B por um tween (tl.tweenFromTo), então todo
//     estado anterior (splits, sets, Ken Burns) chega correto ao 1º quadro da parte
// Cada parte vira renders/chunks/chunk-NN.mp4 (só vídeo). Depois: node scripts/render-chunks.mjs --join
// uso: node scripts/render-chunks.mjs [--size 600] [--only N,M] [--join]
import fs from 'node:fs';
import { execFileSync, spawnSync } from 'node:child_process';
const FPS = +(process.argv[process.argv.indexOf('--fps') + 1] || 30) || 30;
const args = process.argv.slice(2);
const SIZE = +(args[args.indexOf('--size') + 1] || 600) || 600;
const only = args.includes('--only') ? args[args.indexOf('--only') + 1].split(',').map(Number) : null;
const html = fs.readFileSync('index.html', 'utf8');
const attr = (t, k) => (t.match(new RegExp(`(?<![\\w-])${k}="([^"]*)"`)) || [])[1];
const TOTAL = +attr(html.match(/<div[^>]*id="root"[^>]*>/)[0], 'data-duration');
const TOTAL_F = Math.ceil(TOTAL * FPS - 1e-6);
const r4 = x => Math.round(x * 10000) / 10000;
// kit v3: versao do HyperFrames e workers por variavel (render-par.sh). Padrao = a combinacao antiga validada no Air de 8 GB.
// No Air M4 de 16 GB: HF_VERSION=0.8.111 HF_WORKERS=3 com 2 partes em paralelo = ~26 s/parte (x ~40 s sustentado no modo antigo).
const HFV = process.env.HF_VERSION || '0.8.48', HFW = process.env.HF_WORKERS || '1';
const N = Math.ceil(TOTAL_F / SIZE);

function chunkHtml(k, R) {
  const F0 = R ? R[0] : k * SIZE, F1 = R ? R[1] : Math.min(TOTAL_F, F0 + SIZE);
  const A = F0 / FPS, B = F1 / FPS, D = r4(B - A);
  let h = html;
  // áudio fora (o áudio final vem do render completo)
  h = h.replace(/\n?[ \t]*<audio\b[^>]*><\/audio>[^\n]*/g, '');
  // vídeos: remover fora da janela, deslocar os de dentro
  h = h.replace(/<video\b[^>]*data-start="[^"]*"[^>]*><\/video>/g, tag => {
    const s = +attr(tag, 'data-start'), d = +attr(tag, 'data-duration'), ms = +(attr(tag, 'data-media-start') || 0);
    const e = s + d;
    if (e <= A + 1e-4 || s >= B - 1e-4) return '';
    let ns = s - A, nd = d, nms = ms;
    if (ns < 0) { nd = d + ns; nms = ms + (-ns); ns = 0; }
    nd = Math.min(nd, D - ns);
    return tag.replace(/data-start="[^"]*"/, `data-start="${r4(ns)}"`).replace(/data-duration="[^"]*"/, `data-duration="${r4(nd)}"`)
      .replace(/data-media-start="[^"]*"/, `data-media-start="${r4(nms)}"`);
  });
  // divs temporizados (legendas, callouts, grafismos): deslocar; fora da janela → escondidos para sempre
  h = h.replace(/<div\b(?![^>]*id="root")[^>]*data-start="[^"]*"[^>]*>/g, tag => {
    const s = +attr(tag, 'data-start'), d = +attr(tag, 'data-duration');
    const e = s + d;
    if (e <= A + 1e-4 || s >= B - 1e-4) return tag.replace(/data-start="[^"]*"/, `data-start="${r4(D + 5)}"`).replace(/data-duration="[^"]*"/, 'data-duration="0.1"');
    let ns = s - A, nd = d;
    if (ns < 0) { nd = d + ns; ns = 0; }
    nd = Math.min(nd, D - ns);
    return tag.replace(/data-start="[^"]*"/, `data-start="${r4(ns)}"`).replace(/data-duration="[^"]*"/, `data-duration="${r4(nd)}"`);
  });
  h = h.replace(/(id="root"[^>]*data-duration=")[^"]*(")/, `$1${D}$2`);
  // sub-composicoes (data-composition-src, ex.: compositions/mg.html — nasceu no reel ALAN MULALLY): a timeline delas comeca no
  // 0 local; sem isto, numa parte que comeca em A a camada mostrava o estado de (t - A). Cada parte ganha uma copia da
  // sub-composicao cuja timeline toca de A a B, como a principal.
  h = h.replace(/data-composition-src="([^"]+)"/g, (m, src) => {
    const sub = fs.readFileSync(src, 'utf8');
    const reg = sub.match(/window\.__timelines\["([^"]+)"\] = tl;/);
    if (!reg) throw new Error(`registro da timeline nao encontrado em ${src}`);
    const dst = src.replace(/([^/]+)\.html$/, `_chunk-${F0}-$1.html`);
    fs.writeFileSync(dst, sub.replace(reg[0], `var __sc = gsap.timeline({ paused: true }); __sc.add(tl.tweenFromTo(${r4(A)}, ${r4(B)}, { ease: "none" }), 0); window.__timelines["${reg[1]}"] = __sc;`));
    return `data-composition-src="${dst}"`;
  });
  // timeline: toca a original de A a B
  const reg = 'window.__timelines["main"] = tl;';
  if (!h.includes(reg)) throw new Error('registro da timeline não encontrado');
  h = h.replace(reg, `const __chunk = gsap.timeline({ paused: true });\n      __chunk.add(tl.tweenFromTo(${r4(A)}, ${r4(B)}, { ease: "none" }), 0);\n      window.__timelines["main"] = __chunk;`);
  return { h, F0, F1, A, B };
}

if (!args.includes('--join')) {
  for (let k = 0; k < N; k++) {
    if (only && !only.includes(k)) continue;
    const out = `renders/chunks/chunk-${String(k).padStart(2, '0')}.mp4`;
    if (fs.existsSync(out) && !only) { console.log(`parte ${k}: já existe`); continue; }
    const SPLIT = args.includes('--split') ? +args[args.indexOf('--split') + 1] : 1;
    if (SPLIT > 1) {
      // parte que trava sempre no mesmo quadro: renderiza em pedacos menores (sessoes novas) e une
      const k0 = k * SIZE, k1 = Math.min(TOTAL_F, k0 + SIZE), step = Math.ceil((k1 - k0) / SPLIT), subs = [];
      for (let j = 0; j < SPLIT; j++) {
        const R = [k0 + j * step, Math.min(k1, k0 + (j + 1) * step)];
        const { h } = chunkHtml(k, R); const file = `render-chunk-${k}-${j}.html`; fs.writeFileSync(file, h);
        const so = `renders/chunks/sub-${String(k).padStart(2, '0')}-${j}.mp4`;
        console.log(`parte ${k + 1} pedaco ${j + 1}/${SPLIT}: quadros ${R[0]}–${R[1] - 1}`);
        const r = spawnSync('npx', ['--yes', `hyperframes@${HFV}`, 'render', '-c', file, '--sdr', '-f', String(FPS), '-q', 'delivery',
          '-o', so, '--workers', HFW, '--video-frame-format', 'jpg', '--no-best-effort', '--browser-timeout', '300',
          ...(process.env.RENDER_EXTRA ? process.env.RENDER_EXTRA.split(' ') : [])], { encoding: 'utf8', maxBuffer: 1 << 28 });
        fs.writeFileSync(so.replace('.mp4', '.log'), (r.stdout || '') + (r.stderr || '')); fs.rmSync(file, { force: true });
        const ok = fs.existsSync(so) && /Render complete/.test((r.stdout || '') + (r.stderr || ''));
        console.log(`  ${ok ? 'OK' : 'FALHOU'}`); if (!ok) process.exit(1);
        // cada pedaco sai com +1 quadro (copia do ultimo) — corta no numero exato antes de unir
        // (reel Andy Grove: sem isso a parte unida deu 357/354 e o script abortava)
        const st = so.replace('.mp4', '-t.mp4');
        execFileSync('/opt/homebrew/bin/ffmpeg', ['-v', 'error', '-y', '-i', so, '-frames:v', String(R[1] - R[0]), '-c', 'copy', st]);
        subs.push(st);
      }
      fs.writeFileSync(`renders/chunks/sub-${k}.txt`, subs.map(p => `file '${process.cwd()}/${p}'`).join('\n'));
      execFileSync('/opt/homebrew/bin/ffmpeg', ['-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', `renders/chunks/sub-${k}.txt`, '-c', 'copy', out]);
      const fr = +execFileSync('/opt/homebrew/bin/ffprobe', ['-v', 'error', '-count_frames', '-select_streams', 'v', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', out], { encoding: 'utf8' }).trim();
      console.log(`  parte ${k + 1} unida: ${fr}/${k1 - k0} quadros`); if (fr !== k1 - k0) process.exit(1);
      continue;
    }
    const { h, F0, F1 } = chunkHtml(k);
    const file = `render-chunk-${String(k).padStart(2, '0')}.html`;
    fs.writeFileSync(file, h);
    console.log(`parte ${k + 1}/${N}: quadros ${F0}–${F1 - 1} (${F1 - F0})`);
    const t0 = Date.now();
    const r = spawnSync('npx', ['--yes', `hyperframes@${HFV}`, 'render', '-c', file, '--sdr', '-f', String(FPS), '-q', 'delivery',
      '-o', out, '--workers', HFW, '--video-frame-format', 'jpg', '--no-best-effort', '--browser-timeout', '300', ...(process.env.RENDER_EXTRA ? process.env.RENDER_EXTRA.split(' ') : [])],
      { encoding: 'utf8', maxBuffer: 1 << 28 });
    fs.writeFileSync(`renders/chunks/chunk-${String(k).padStart(2, '0')}.log`, (r.stdout || '') + (r.stderr || ''));
    fs.rmSync(file, { force: true });
    const ok = fs.existsSync(out) && /Render complete/.test((r.stdout || '') + (r.stderr || ''));
    const frames = ok ? +execFileSync('/opt/homebrew/bin/ffprobe', ['-v', 'error', '-count_frames', '-select_streams', 'v', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', out], { encoding: 'utf8' }).trim() : 0;
    console.log(`  ${ok ? 'OK' : 'FALHOU'} em ${((Date.now() - t0) / 60000).toFixed(1)} min · ${frames}/${F1 - F0} quadros`);
    if (!ok || frames !== F1 - F0) process.exit(1);
  }
} else {
  const parts = Array.from({ length: N }, (_, k) => `renders/chunks/chunk-${String(k).padStart(2, '0')}.mp4`);
  for (const p of parts) if (!fs.existsSync(p)) throw new Error(`falta ${p}`);
  fs.writeFileSync('renders/chunks/lista.txt', parts.map(p => `file '${process.cwd()}/${p}'`).join('\n'));
  execFileSync('/opt/homebrew/bin/ffmpeg', ['-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', 'renders/chunks/lista.txt', '-c', 'copy', '-an', 'renders/chunks/_video.mp4']);
  console.log('vídeo unido: renders/chunks/_video.mp4');
}
```


---

# ARQUIVO: `modelo-projeto/scripts/finalizar.py`

```python
"""Fecha o export: audio final + mux das partes + QC. NOVO no kit v2 (2026-10-01): junta os comandos que eram digitados a cada reel.
Uso: python3 scripts/finalizar.py renders/<Nome>-reel-final.mp4 [--fps 60] [--sem-preto]
Pre-requisito: todas as partes em renders/chunks/chunk-NN.mp4 (work/render-all.sh) e assets/voz-mix.m4a + assets/bed.m4a (bake.py).
 1. renders/_audio.m4a = amix(voz-mix, bed, normalize=0) + alimiter a -1 dBTP.
    `level=disabled` e obrigatorio: com o auto-level (padrao) o limiter normaliza de volta para 0 dB.
 2. mux direto da lista de partes + _audio.m4a, video COPIADO, SEM -shortest (ele decepa o ultimo quadro),
    com -frames:v = quadros da timeline (a ultima parte pode vir com +1 quadro).
 3. QC: quadros = timeline · duracoes A/V · pico e media (volumedetect) · trechos pretos (blackdetect).
Nao confere sincronia boca/voz (scripts/sync-check.mjs) nem compara quadros-chave com o preview — fazer a parte."""
import json, glob, math, os, re, subprocess, sys
out=sys.argv[1]; FPS=int(sys.argv[sys.argv.index('--fps')+1]) if '--fps' in sys.argv else 60
TOTAL=json.load(open('work/mix-plan.json'))['total']; NF=math.ceil(TOTAL*FPS-1e-6)
def sh(c): return subprocess.run(c,capture_output=True,text=True)
def nq(f): return int(sh(['ffprobe','-v','error','-select_streams','v:0','-count_packets','-show_entries','stream=nb_read_packets','-of','csv=p=0',f]).stdout.strip().rstrip(','))
parts=sorted(glob.glob('renders/chunks/chunk-[0-9][0-9].mp4'))
q=[nq(p) for p in parts]; soma=sum(q)
print(f"timeline {TOTAL}s = {NF} quadros @{FPS} · {len(parts)} partes · soma {soma}")
if not (NF<=soma<=NF+1): raise SystemExit(f"PARTES NAO FECHAM: soma {soma}, timeline {NF} — {list(zip([os.path.basename(p) for p in parts],q))}")
os.makedirs('renders',exist_ok=True)
subprocess.run(['ffmpeg','-v','error','-y','-i','assets/voz-mix.m4a','-i','assets/bed.m4a','-filter_complex',
  '[0:a][1:a]amix=inputs=2:normalize=0:dropout_transition=0,alimiter=limit=0.891:level=disabled[a]','-map','[a]',
  '-t',f'{TOTAL:.3f}','-c:a','aac','-b:a','256k','-ar','48000','-ac','2','renders/_audio.m4a'],check=True)
open('renders/parts.txt','w').write('\n'.join(f"file '{os.path.abspath(p)}'" for p in parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','renders/parts.txt','-i','renders/_audio.m4a',
  '-map','0:v','-map','1:a','-c','copy','-frames:v',str(NF),'-movflags','+faststart',out],check=True)
# ---- QC ----
pr=lambda s,e: sh(['ffprobe','-v','error','-select_streams',s,'-show_entries',e,'-of','csv=p=0',out]).stdout.strip().rstrip(',')
w,hh,fr=pr('v:0','stream=width,height,r_frame_rate').split(','); dv=float(pr('v:0','stream=duration')); da=float(pr('a:0','stream=duration'))
fq=nq(out); ok=fq==NF
vd=sh(['ffmpeg','-v','info','-i',out,'-vn','-af','volumedetect','-f','null','-']).stderr
pico=float(re.search(r'max_volume: ([-\d.]+)',vd)[1]); media=float(re.search(r'mean_volume: ([-\d.]+)',vd)[1])
print(f"{out}: {w}x{hh} @{fr} · {fq} quadros ({'= timeline' if ok else 'DIFERENTE da timeline '+str(NF)}) · video {dv:.3f}s / audio {da:.3f}s · {os.path.getsize(out)/1e6:.0f} MB")
print(f"audio: pico {pico} dB (alvo -1; nunca 0) · media {media} dB")
if pico>-0.3: ok=False; print("  PICO ALTO — o limiter nao atuou")
if abs(dv-da)>2/FPS: ok=False; print("  A/V com mais de 2 quadros de diferenca")
if '--sem-preto' not in sys.argv:
    bd=sh(['ffmpeg','-v','info','-i',out,'-an','-vf','scale=180:-2,blackdetect=d=0.05:pic_th=0.98','-f','null','-']).stderr
    pretos=re.findall(r'black_start:([\d.]+) black_end:([\d.]+)',bd)
    print(f"trechos pretos: {len(pretos)} {pretos or ''}")
    if pretos: ok=False
print("QC OK" if ok else "QC COM PROBLEMA"); sys.exit(0 if ok else 1)
```


---

# ARQUIVO: `modelo-projeto/scripts/_src.py`

```python
"""Resolve o mezanino do projeto: `src` do edit-plan.json, senão o único assets/*-sdr.mp4."""
import json, glob, os
def mezanino():
    if os.path.exists('assets/edit-plan.json'):
        s = json.load(open('assets/edit-plan.json')).get('src')
        if s: return s
    c = glob.glob('assets/*-sdr.mp4')
    if len(c) != 1: raise SystemExit(f'mezanino ambíguo/ausente em assets/: {c}')
    return c[0]
SRC = mezanino()
```


---

# ARQUIVO: `modelo-projeto/scripts/align.py`

```python
"""Reancora os timestamps de palavra do whisper na energia real do chunk.
O whisper deriva ate ~1s dentro de um chunk; aqui cada grupo de palavras e
encaixado sobre o grupo de fala correspondente detectado por RMS."""
import numpy as np, wave, json, glob, os, shutil, sys
SOMENTE={int(x) for x in sys.argv[1:]}  # sem argumento = todos os chunks
META={m['i']:m for m in json.load(open('assets/chunks/meta.json'))}
PLAN=json.load(open('assets/edit-plan.json'))
sys.path.insert(0, os.path.dirname(__file__))
from captions_fix_table import FIX  # palavras DROP (vazamento do take vizinho) ficam fora do encaixe
NOISE=-45.0
def envelope(path):
    w=wave.open(path); n=w.getnframes(); sr=w.getframerate()
    a=np.frombuffer(w.readframes(n),dtype=np.int16).astype(np.float32)/32768.0
    W=int(0.020*sr); nw=len(a)//W
    return 20*np.log10(np.sqrt(np.maximum((a[:nw*W].reshape(nw,W)**2).mean(1),1e-12))), nw
def runs(db,nw,merge=0.16,minrun=0.07):
    on=db>=NOISE; out=[];i=0
    while i<nw:
        if on[i]:
            j=i
            while j<nw and on[j]: j+=1
            out.append([i*0.02,j*0.02]); i=j
        else: i+=1
    m=[]
    for r in out:
        if m and r[0]-m[-1][1]<merge: m[-1][1]=r[1]
        else: m.append(r)
    return [r for r in m if r[1]-r[0]>=minrun]
def groups(ws,gap=0.22):
    g=[[ws[0]]]
    for p,c in zip(ws,ws[1:]):
        if c[0]-p[1]>gap: g.append([c])
        else: g[-1].append(c)
    return g
def warp(ws,src,dst):
    s0,s1=src; d0,d1=dst
    k=(d1-d0)/(s1-s0) if s1-s0>1e-6 else 1.0
    return [(round(d0+(a-s0)*k,3), round(d0+(b-s0)*k,3), t) for a,b,t in ws]
report=[]
for p in sorted(glob.glob('assets/chunks/ch*-words.json')):
    if SOMENTE and int(os.path.basename(p)[2:4]) not in SOMENTE: continue
    ci=int(os.path.basename(p)[2:4]); wav=f'assets/chunks/ch{ci:02d}.wav'
    d=json.load(open(p))
    ents=[e for e in d['transcription'] if e['text'].strip() and not e['text'].strip().startswith('[')]
    keep=[k for k in range(len(ents)) if not (k in FIX.get(ci,{}) and FIX[ci][k] is None)]
    ents=[ents[k] for k in keep]
    ws=[(e['offsets']['from']/1000,e['offsets']['to']/1000,e['text'].strip()) for e in ents]
    if not ws: continue
    db,nw=envelope(wav); R=runs(db,nw)
    # o chunk tem +-0.3s de folga e pode conter o fim do take anterior / inicio do
    # proximo: so valem os trechos de fala dentro do corpo do proprio take.
    off=META[ci]['off']; seg=PLAN['segments'][ci]
    b0,b1=seg['in']-off-0.06, seg.get('aout',seg['out'])-off+0.06  # so a VOZ do take (o out inclui o lead do J-cut)
    R=[r for r in R if r[1]>b0 and r[0]<b1]
    R=[[max(r[0],b0),min(r[1],b1)] for r in R]
    if not R: continue
    G=groups(ws)
    if len(G)==len(R):                      # alinhamento grupo-a-grupo
        new=[]
        for g,r in zip(G,R): new+=warp(g,(g[0][0],g[-1][1]),(r[0],r[1]))
        mode=f"grupos {len(G)}"
    else:                                   # fallback: ancora so os extremos
        new=warp(ws,(ws[0][0],ws[-1][1]),(R[0][0],R[-1][1]))
        mode=f"extremos (w{len(G)}/r{len(R)})"
    shift=max(abs(n[0]-o[0]) for n,o in zip(new,ws))
    report.append(f"ch{ci:02d}: {mode:<18} corr.max {shift*1000:4.0f}ms  '{' '.join(t for _,_,t in ws)[:52]}'")
    for e,(a,b,_) in zip(ents,new):
        e['offsets']['from']=int(round(a*1000)); e['offsets']['to']=int(round(b*1000))
    json.dump(d,open(p,'w'),ensure_ascii=False)
print("\n".join(report))
```


---

# ARQUIVO: `modelo-projeto/scripts/bipe.py`

```python
"""POR VIDEO — reel KAZUO INAMORI. Bipe de censura gravado na voz, na palavra INTEIRA
(roteiro: "Sobrou verba em dezembro e o time torrou em qualquer merda... piiii? Voce ensinou, meu amiguinho.").
Entrada: work/kazuo-inamori-voz-limpa.m4a (audio do bruto) -> assets/kazuo-inamori-voz.m4a (voz do projeto)
e work/full.wav (mono, o que o cuts.py le). Transcricao continua usando work/full-clean.wav (sem bipe).
Mapa (envelope 10 ms + bandas de espectro 30 ms, source): "em" nasal 75,15-75,41 · oclusao /k/ 75,43-75,47 · "qual" 75,48-75,70 ·
oclusao /k/ 75,71-75,73 · "quer" 75,74-75,90 · nasal /m/ 75,91-76,08 (energia < 400 Hz, -25 dB) · "er" 76,09-76,23 · tap /r/ 76,24-76,26 ·
oclusao /d/ 76,27-76,34 · "a" 76,35-76,47 · decaimento ate 76,50.
Varredura da transcricao INTEIRA (40 regioes, inclusive as descartadas): so este palavrao."""
import numpy as np, subprocess, wave, json, os
VOZ=json.load(open('assets/edit-plan.json'))['voiceSrc']                      # assets/<slug>-voz.m4a (voz do projeto, COM bipe)
LIMPA='work/'+os.path.basename(VOZ).replace('.m4a','-limpa.m4a')             # work/<slug>-voz-limpa.m4a (audio do bruto, SEM bipe)
JANELAS=[]  # POR VIDEO: [(ini, fim)] em s do source, palavra INTEIRA. Ex. (reel Kazuo): [(75.905,76.505)]. Vazio = sem bipe (fase2.sh pula)
GAIN=10**(-18/20)*1.75    # bipe ~1 dB acima da frase (Dan Martell: -17,2 contra -18,4)
subprocess.run(['ffmpeg','-v','error','-y','-i',LIMPA,'-ar','48000','-ac','2','-c:a','pcm_s16le','work/voz-limpa48.wav'],check=True)
w=wave.open('work/voz-limpa48.wav'); sr=w.getframerate(); ch=w.getnchannels()
x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32).reshape(-1,ch)/32768
for A,B in JANELAS:
    i0,i1=int(A*sr),int(B*sr); n=i1-i0; t=np.arange(n)/sr
    f=int(0.006*sr); env=np.ones(n); env[:f]=np.linspace(0,1,f); env[-f:]=np.linspace(1,0,f)
    x[i0:i1]=0; x[i0:i1]+= (GAIN*np.sin(2*np.pi*1000*t)*env)[:,None]
y=(np.clip(x,-1,1)*32767).astype(np.int16)
o=wave.open('work/voz-bipe48.wav','wb'); o.setnchannels(ch); o.setsampwidth(2); o.setframerate(sr); o.writeframes(y.tobytes()); o.close()
subprocess.run(['ffmpeg','-v','error','-y','-i','work/voz-bipe48.wav','-c:a','aac','-b:a','192k',VOZ],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i','work/voz-bipe48.wav','-ac','1','-ar','44100','-c:a','pcm_s16le','work/full.wav'],check=True)
print(f'bipes {JANELAS} gravados em {VOZ} e work/full.wav')
```


---

# ARQUIVO: `modelo-projeto/scripts/captions_fix_table.py`

```python
"""POR VIDEO — reel KAZUO INAMORI. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Regra do formato: onde o whisper erra so GRAFIA/PONTUACAO, vale a grafia do roteiro ("pra", "pro", "setenta e oito", "um bilhao", "MONGE");
onde o AUDIO diz outra coisa (passe por regiao, passe por chunk e passe com --prompt do roteiro concordam), vale o audio:
"virou UM monge budista" (roteiro: "virou monge"), "sem olhar numero" (roteiro: "o numero"), "uma reuniao COM O diretor QUE ia gastar"
(roteiro: "uma reuniao. Um diretor ia gastar"), "pra voce nao confio" (roteiro: "eu nao confio"), "ja ESTA aprovado" (roteiro: "ja ta").
Todos os chunks foram reconstruidos do passe por REGIAO (rebuild_chunk.py: o passe por chunk vazava/alucinava nas bordas — "Caso",
"monstro", "Sensacional!", "equilibrio", "importancia"), menos o ch28, que fica com o passe por chunk (o por regiao punha o "com" no take anterior).
Copia do passe por chunk cru: work/chunks-raw/. ch24: "merda" -> M**** (bipe de censura na palavra inteira, scripts/bipe.py)."""
DROP=None
FIX={
 2:{0:"pra"},
 4:{4:"e,",6:"setenta e oito",7:"anos,",12:"falida."},
 5:{0:"Sem"},
 6:{5:"pra",14:"pro",15:DROP},
 8:{0:"quebra"},
 9:{5:"empresinha,"},
 14:{0:"mostra",5:"equipe,"},
 17:{1:"diz"},
 19:{4:"gafanhoto."},
 22:{0:"Ele",4:"plano,"},
 23:{0:"porque"},
 24:{1:DROP,11:"M****?"},
 26:{1:"MONGE"},
 27:{6:DROP},
 28:{6:"um",10:DROP,11:DROP},
 29:{1:"cortou:"},
 30:{0:"“Pra",6:"centavo.”"},
 31:{1:"diretor:"},
 32:{0:"“Mas",6:"orçamento.”"},
 33:{1:"explodiu:"},
 34:{0:"“De"},
 36:{9:"chão.”"},
 39:{1:"escondido."},
 40:{0:"Se",7:"pro",8:DROP,14:"segue,",17:"é",18:"demais."},
}
FIXT={24:{11:75.905}}  # legenda M**** entra junto com o bipe (75,905 s do source)
```


---

# ARQUIVO: `modelo-projeto/scripts/cenas_opt.py`

```python
"""Otimizador do ritmo de cenas (pedido do Fabio: troca de cena/efeito a cada ~4 s, nao 1-2 s).
Particiona a timeline em cenas de LMIN..LMAX s. Tipos: P (apresentador), B (B-roll tela cheia),
S (split, so nas janelas de split). Custo = segundos de leitura de roteiro EXPOSTA (P/S) * 1
+ segundos de B-roll * WB (preferir o apresentador quando o olhar esta limpo).
Cortes obrigatorios: FORCE. Trechos so-B: ONLYB. Saida: work/cenas-opt.json"""
import json, math
TOTAL=json.load(open('work/mix-plan.json'))['total']
# leituras de roteiro (timeline) — gaze/tl-windows.json (scripts/gaze_tl.py + gaze_windows.py), revisadas nas folhas
# gaze/rev/*.jpg. Reel MIKE MICHALOWICZ (rate 1.1, timeline 100,87 s): as 59 janelas tratadas como desvio
# (conservador: o pedido e aparecer 100% olhando para a camera) -> gaze/tl-windows-conf-uniao.json.
G=[(w['t0']-0.03,w['t1']+0.03) for w in json.load(open(__import__('os').environ.get('GW','gaze/tl-windows-conf.json')))]
SPLIT=[(0.0,12.31),(66.98,76.72)]  # intro (pre-revelacao, segs 0-3) e split 2 (a virada: "foi um cofrinho... cada centavo", segs 23-26)
FORCE=[12.31,66.98,82.75]          # revelacao ("Mike" em 12,19 s) · entrada do split 2 · climax ("Papai, a gente vai conseguir")
ONLYB=[(12.31,13.40),(82.75,84.30)] # revelacao (Mike) · climax
ONLYP=[(48.35,48.72),(98.50,100.87)] # bipe no rosto (a boca sob o bipe le como censura) · "me segue, porque voce e demais"
FIRST=('S',0.0)                    # a CAPA (quadro 0) e sempre split
WBS=0.5                           # custo extra por s de tela cheia DENTRO de split (preserva o formato)
LMIN,LMAX,WB,STEP=2.5,5.0,0.05,0.05
def expo(a,b): return sum(max(0,min(b,g1)-max(a,g0)) for g0,g1 in G)
N=int(round(TOTAL/STEP)); T=lambda i: min(TOTAL,i*STEP)
F={int(round(f/STEP)) for f in FORCE}
def allowed(a,b,k):
    ta,tb=T(a),T(b)
    if any(ta<f*STEP<tb for f in F if 0<f<N): return False
    insp=any(s0-1e-6<=ta and tb<=s1+1e-6 for s0,s1 in SPLIT)
    inb=any(ta<b1 and tb>b0 for b0,b1 in ONLYB)
    if k!='P' and any(ta<p1 and tb>p0 for p0,p1 in ONLYP): return False
    if k=='S': return insp
    ovs=any(ta<s1-1e-6 and tb>s0+1e-6 for s0,s1 in SPLIT)
    if k=='P': return not inb and not ovs
    return True
INF=1e9; best=[{} for _ in range(N+1)]; best[0]={None:(0,None)}
for i in range(N+1):
    for last,(c,_) in list(best[i].items()):
        for L in range(int(LMIN/STEP),int(LMAX/STEP)+1):
            j=i+L
            if j>N:
                j=N
                if (j-i)*STEP<1.2: continue
            for k in 'PBS':
                if i==0 and FIRST and k!=FIRST[0]: continue
                if not allowed(i,j,k): continue
                if k=='P' and last=='P': continue      # P->P sem troca nao conta como cena nova
                cost=c+(expo(T(i),T(j)) if k in 'PS' else WB*(T(j)-T(i))+WBS*sum(max(0,min(T(j),s1)-max(T(i),s0)) for s0,s1 in SPLIT))
                if cost<best[j].get(k,(INF,))[0]: best[j][k]=(cost,(i,last))
            if j==N: break
k=min(best[N],key=lambda x:best[N][x][0]); cost=best[N][k][0]; out=[]; j=N
while j>0:
    c,(i,prev)=best[j][k]; out.append((round(T(i),2),round(T(j),2),k)); j,k=i,prev
out.reverse()
json.dump([{"t0":a,"t1":b,"tipo":k,"exposto":round(expo(a,b),2) if k!='B' else 0} for a,b,k in out],open('work/cenas-opt.json','w'),indent=1)
tot=sum(expo(a,b) for a,b,k in out if k!='B'); allg=sum(g1-g0 for g0,g1 in G)
for a,b,k in out: print(f"{k} {a:6.2f}-{b:6.2f} ({b-a:4.2f})"+(f"  expoe {expo(a,b):.2f}s" if k!='B' and expo(a,b)>0 else ''))
print(f"{len(out)} cenas · B-roll {sum(1 for x in out if x[2]=='B')} · leitura exposta {tot:.2f}s de {allg:.2f}s")
```


---

# ARQUIVO: `modelo-projeto/scripts/chunks_from_regions.py`

```python
"""MOTOR (kit v3, fluxo rapido). Gera assets/chunks/chNN-words.json de TODOS os takes a partir do passe por REGIAO
(work/region-words-cut.json), sem rodar o whisper de novo por chunk. Substitui whisper_chunks.sh + rebuild_chunk.py:
nos reels Sun Tzu, Kazuo e Alan Mulally quase todo chunk acabava reconstruido do passe por regiao (o passe por chunk
vaza palavra do take vizinho, alucina e colapsa tempos). Depois: align.py -> fix_captions.py, como sempre.
uso: python3 scripts/chunks_from_regions.py      (depois de mkchunks.py)"""
import json, os
M = {m['i']: m for m in json.load(open('assets/chunks/meta.json'))}
RW = json.load(open('work/region-words-cut.json'))
RC = {r['i']: r for r in json.load(open('work/regions_cut.json'))}
segs = json.load(open('work/segs.json'))
os.makedirs('work/chunks-raw', exist_ok=True)
for s in segs:
    ci = s['i']; a, b = s['region']; off = M[ci]['off']
    ws = [w for r in range(a, b + 1) if not RC[r]['drop'] for w in RW.get(str(r), [])]
    tr = [{"text": " " + w[0].strip(), "offsets": {"from": int(round((w[1] - off) * 1000)), "to": int(round((w[2] - off) * 1000))}} for w in ws]
    d = {"transcription": tr}
    json.dump(d, open(f'assets/chunks/ch{ci:02d}-words.json', 'w'), ensure_ascii=False)
    json.dump(d, open(f'work/chunks-raw/ch{ci:02d}-words.json', 'w'), ensure_ascii=False)
    print(f"ch{ci:02d} {s['label']:<20} " + ' '.join(t['text'].strip() for t in tr))
print(f"{len(segs)} chunks a partir do passe por regiao (indices de palavra = os desta lista, para a captions_fix_table.py)")
```


---

# ARQUIVO: `modelo-projeto/scripts/cuts.py`

```python
"""Detecta head e tail de cada take mantido -> work/segs.json.
Head: onset por RMS (20 ms, -27 dB, 4 de 8 janelas), recuando ate o piso de ruido, - HEAD_PAD.
Tail: ultima janela acima do piso de ruido (-45 dB) + TAIL_PAD — garante a palavra inteira."""
import numpy as np, wave, json
w=wave.open('work/full.wav'); n=w.getnframes(); sr=w.getframerate()
a=np.frombuffer(w.readframes(n),dtype=np.int16).astype(np.float32)/32768.0
W=int(0.020*sr); nw=len(a)//W
db=20*np.log10(np.sqrt(np.maximum((a[:nw*W].reshape(nw,W)**2).mean(1),1e-12)))
t2w=lambda t:max(0,min(nw-1,int(t/0.020))); w2t=lambda i:round(i*0.020,3)
NOISE=-45.0
# folgas: o crossfade do J-cut (3f) cai inteiro no silêncio e sobra ~0,1 s de respiro entre as falas
# (com 0,12/0,10 e crossfade 5f o fade comia até 76 ms da palavra final — reel André Esteves)
HEAD_PAD=0.20; TAIL_PAD=0.13
# J-cut sem soma de vozes (reel Atul Gawande, 2026-09-27: "as J-cuts nao ficaram tao boas"): a voz de cada
# take termina em `aout` = fim da fala + TA e a do take seguinte comeca em `in` = inicio da fala - HH, emendadas
# ponta a ponta (crossfade de 3 quadros dentro do silencio). O VIDEO do take segura mais LEAD_SRC depois do
# `aout` (out = aout + lead*rate): a voz nova entra 5 quadros ANTES do corte de imagem. Respiro = (TA+HH)/rate.
import json as _j
_P=_j.load(open('assets/edit-plan.json')); RATE=_P.get('rate',1.1); LEAD_SRC=round(_P.get('jcutLeadFrames',5)/30*RATE,3)
TA=0.12; HH=0.15
R={r['i']:r for r in json.load(open('work/regions_cut.json'))}
# Fim da ULTIMA PALAVRA de cada regiao (whisper -ml 1 -sow). Serve de ancora para o tail:
# o piso de -45 dB sozinho entra no decaimento da respiracao e deixa ~1 s de ar morto
# (medido no IKEA: CAMADAS +0,57 s, PROVA +0,86 s).
WEND={int(k):v[-1][2] for k,v in json.load(open('work/region-words-cut.json')).items()}
# POR VIDEO: (label, 1a regiao, ultima regiao) em work/regions_cut.json — reel KAZUO INAMORI
# (regions_cut.json vem de scripts/mkcut.py). TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido):
#   c12 (r09 "Pela empresa inteira.") -> c13 · c27+c28+c29 (r22-r24 "E se voce quiser o protocolo completo / Comenta Monge. / Que eu te mando.") -> c30
#   c42 (r34 parte 2 "Seu time gasta...") e c43 (r35 "Se o time gasta como se o dinheiro...") -> c44
# c46+c47+c48 = "Se voce e o unico... me segue, porque voce... e demais" (pausa dramatica, NAO e repeticao: um take so)
TAKES=[
 ("GANCHO",0,0),
 ("PROTOCOLO-POLEMICO",1,1),
 ("ESCONDE-NUMERO",2,2),
 ("KAZUO-GIGANTES",3,3),
 ("MONGE-AEREA",4,4),
 ("SEM-SALARIO",5,5),
 ("PROTOCOLO-DINHEIRO",6,6),
 ("P1-PRIMEIRO",7,7),
 ("P1-PEDACINHOS",8,8),
 ("P1-EMPRESINHA",9,9),
 ("P1-LIDER-DONO",10,10),
 ("P1-BRIGA-LUCRO",11,11),
 ("P1-NINGUEM-BRIGA",13,13),
 ("P2-SEGUNDO",14,14),
 ("P2-MOSTRA-NUMERO",15,15),
 ("P2-TODO-DIA",16,16),
 ("P2-CONTA-DE-CASA",17,17),
 ("P2-PAINEL",18,18),
 ("P2-SO-VOCE-VE",19,19),
 ("P2-GAFANHOTO",20,20),
 ("P3-TERCEIRO",21,21),
 ("P3-ORCAMENTO",22,22),
 ("P3-PLANO",23,23),
 ("P3-GASTAR-TUDO",24,24),
 ("P3-TORROU-BIPE",25,25),
 ("P3-AMIGUINHO",26,26),
 ("CTA-COMENTA-MONGE",30,30),
 ("VIRADA-REUNIAO",31,31),
 ("VIRADA-BILHAO",32,32),
 ("VIRADA-CORTOU",33,33),
 ("VIRADA-CENTAVO",34,34),
 ("VIRADA-O-DIRETOR",35,35),
 ("VIRADA-APROVADO",36,36),
 ("VIRADA-EXPLODIU",37,37),
 ("CLIMAX-DE-QUEM",38,38),
 ("CLIMAX-NAO",39,39),
 ("CLIMAX-RASTEJANDO",40,40),
 ("FECHO-RECORDE",41,41),
 ("FECHO-TIME-GASTA",44,44),
 ("FECHO-NUM-ESCONDIDO",45,45),
 ("CTA-ME-SEGUE",46,48),
]
AP=[(lab,R[a]['s'],R[b]['e']) for lab,a,b in TAKES]
res=[];tot=0
print(f"{'i':>2} {'label':<15} {'IN':>7} {'OUT':>7} {'dur':>5}   onset/offset")
for k,(lab,s0,s1) in enumerate(AP):
    # vizinhos no SOURCE (um take descartado pode ficar entre dois mantidos)
    pe=max([r['e'] for r in R.values() if r['e']<=s0+1e-6], default=-1e9)
    ns=min([r['s'] for r in R.values() if r['s']>=s1-1e-6], default=1e9)
    lo,hi=t2w(max(s0-0.8,pe+0.12)),t2w(min(s0+1.2,ns-0.2)); on=None
    for j in range(lo,max(lo+1,hi)):
        if (db[j:j+8]>=-27.0).sum()>=4: on=j; break
    if on is None: on=t2w(s0)
    j=on
    while j>lo and db[j-1]>=NOISE: j-=1
    onset=w2t(j); IN=round(max(0,onset-HEAD_PAD),3)
    # POR VIDEO: head fixo onde a deteccao nao serve (reel KAZUO INAMORI: nenhum)
    # (nenhum ate agora)
    FORCE_IN={}
    if lab in FORCE_IN: onset=round(FORCE_IN[lab]+HEAD_PAD,3); IN=FORCE_IN[lab]
    hi2=t2w(min(s1+0.8,ns-0.15)); lo2=t2w(max(s1-0.8,pe))
    # Tail: ultima janela acima do piso. Mas um respiro/estalo DESTACADO (separado do corpo da
    # fala por >= GAP_MIN de silencio) nao e palavra — e o take ficaria com ~1 s de ar morto
    # (medido no IKEA: CAMADAS +1,2 s e PROVA +0,9 s). Nesses casos recua para o bloco anterior.
    # Nunca corta DENTRO de um bloco contiguo, entao a palavra inteira fica sempre preservada.
    off=None
    for j in range(hi2,lo2,-1):
        if db[j]>=NOISE: off=j+1; break
    if off is None: off=t2w(s1)
    # O whisper as vezes estoura alem do audio (GANCHO: 7,59 contra 7,28 real) e o RMS as vezes
    # entra no respiro (PROVA: 67,00 contra 66,14). Pega o MENOR dos dois...
    we=WEND.get(TAKES[k][2])
    if we is not None:
        cand=min(off,t2w(we)+1)
        # ...e TRAVA: nunca cortar dentro de fala energetica. Se o corpo acima de -35 dB
        # continua depois do candidato, o tail vai ate o fim desse bloco (palavra inteira).
        body=cand
        while body<hi2 and db[body]>=-35.0: body+=1
        cand=max(cand,body)
        if cand<off: print(f"     [{lab}] tail {w2t(off):.2f} -> {w2t(cand):.2f} (fim da palavra {we:.2f}s; -{(off-cand)*0.02:.2f}s de ar morto)")
        off=cand
    # POR VIDEO: fim de fala fixo onde a respiracao seguinte fica acima do piso (reel REED HASTINGS:
    # "fim." termina em 105,42; o piso de -45 dB entrava no respiro ate o "Em" do take seguinte)
    FORCE_OFF={}
    if lab in FORCE_OFF: off=t2w(FORCE_OFF[lab])
    offset=w2t(off); OUT=round(offset+TAIL_PAD,3); d=round(OUT-IN,3); tot+=d
    print(f"{k:>2} {lab:<15} {IN:7.2f} {OUT:7.2f} {d:5.2f}   {onset:.2f}/{offset:.2f}")
    res.append({"i":k,"label":lab,"in":IN,"out":OUT,"region":[TAKES[k][1],TAKES[k][2]],"_on":onset,"_off":offset})
print(f"\nsource {tot:.2f}s -> /1.1 = {tot/1.1:.2f}s ; menos {len(AP)-1} leads(5f) = {tot/1.1-(len(AP)-1)*5/30:.2f}s")
for r in res: r['on'],r['off']=r.pop('_on'),r.pop('_off')
for k,r in enumerate(res):
    r['in']=round(max(0,r['on']-(HEAD_PAD if k==0 else HH)),3); r['aout']=round(r['off']+TA,3)
# Pausa curta (fala a fala < TA+HH no source): a emenda vai no silencio real, 45% para o tail e 55% para a cabeca.
print(f"\nrate {RATE} · lead {LEAD_SRC}s de source · respiro alvo {(TA+HH)/RATE:.3f}s de timeline")
for k in range(len(res)-1):
    a,b=res[k],res[k+1]; g=round(b['on']-a['off'],3)
    if b['in']<a['aout']:
        a['aout']=round(a['off']+g*0.45,3); b['in']=round(b['on']-g*0.55,3)
        # reel HERB KELLEHER: com 45/55 o crossfade (3 f) invadia o inicio da palavra seguinte ("piloto|foi grosso",
        # pausa 0,14 s). Se o crossfade cabe na pausa, a emenda vai logo antes da fala nova e o fade termina no silencio.
        XF=_P.get('jcutCrossfadeFrames',3)/30*RATE
        if g*0.55<XF+0.005 and g>=XF+0.01: b['in']=round(b['on']-XF-0.005,3); a['aout']=b['in']
        print(f"  pausa curta {a['label']} | {b['label']}: fala a fala {g:.2f}s -> emenda em {a['aout']} (respiro {g/RATE:.3f}s)")
for k,r in enumerate(res):
    last=k==len(res)-1
    r['out']=round(r['aout'] if last else r['aout']+LEAD_SRC,3)
    if last: r['out']=r['aout']=round(r['off']+TAIL_PAD,3)
tot=sum(r['out']-r['in'] for r in res)
print(f"source {tot:.2f}s -> /{RATE} menos {len(res)-1} leads = {tot/RATE-(len(res)-1)*5/30:.2f}s")
json.dump(res,open('work/segs.json','w'),indent=1)
```


---

# ARQUIVO: `modelo-projeto/scripts/entrega.py`

```python
"""POR VIDEO — reel KAZUO INAMORI. Foto escolhida por slot (work/pesq/slot-picks.json) -> assets/broll-src/<slot>.jpg (original)
e o recorte de ENTREGA no aspecto do slot: assets/broll-src/entrega/<slot>-9x16.jpg (tela cheia) ou <slot>-16x9.jpg (split).
ax/ay = ancora do recorte (0 = esquerda/topo, 1 = direita/base). fill = foto inteira sobre fundo borrado (foto pequena ou
assunto largo demais para o 9:16). Folha de conferencia: work/pesq/sheet_entrega.jpg"""
import json, shutil
from PIL import Image, ImageFilter, ImageDraw, ImageFont
PK={ # slot: (candidata, ax, ay, fill[, box]) — box = pre-recorte (x0,y0,x1,y1 em fracao) antes do aspecto
 "s01":("C1",.5,.2,0), "s02":("c04a_7",.5,.5,0), "s03":("C2",.5,.3,0), "s04":("d02a_11",.5,.35,0),
 "s05":("b03a_9",.5,.5,0), "s06":("b03a_2",.5,.2,0), "s07":("b05a_7",.6,.5,0),
 "s08":("b07a_0",.5,.5,1,(.1,.0,.9,1.0)), "s09":("b08b_10",.5,.5,1,(.15,.0,.85,1.0)), "s10":("b03c_19",.5,.5,0), "s11":("c09b_6",.5,.5,1),
 "s12":("b10b_11",.5,.5,0), "s13":("po-1",.65,.5,0), "s14":("d12a_3",.5,.5,0), "s15":("b13a_0",.5,.5,0),
 "s16":("b12a_11",.5,.5,0), "s17":("b15a_18",.5,.5,0), "s18":("b18c_6",.5,.5,1,(.15,.0,1.0,1.0)), "s19":("c18a_15",.5,.5,1,(.2,.0,.8,1.0)),
 "s20":("b19c_16",.5,.5,1,(.1,.0,.9,1.0)), "s21":("d20a_4",.5,.5,0)}
S={s['id']:s for s in json.load(open('assets/broll-slots.json'))['slots']}
json.dump({k:v[0] for k,v in PK.items()},open('work/pesq/slot-picks.json','w'),indent=1)
th=[]; fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',26)
for sid,(cid,ax,ay,fill,*bx) in PK.items():
    im=Image.open(f'work/pesq/cand/{cid}.jpg').convert('RGB')
    if bx: W0,H0=im.size; x0,y0,x1,y1=bx[0]; im=im.crop((int(W0*x0),int(H0*y0),int(W0*x1),int(H0*y1)))
    shutil.copy(f'work/pesq/cand/{cid}.jpg',f'assets/broll-src/{sid}.jpg')
    split=S[sid]['mode']=='split'; A=16/9 if split else 9/16; W,H=im.size
    if fill:  # foto inteira na largura do quadro, sobre a propria foto ampliada e borrada
        cw,ch=(2560,1440) if split else (1440,2560)   # canvas na resolucao de saida (antes: altura da foto -> 487x866)
        bg=im.resize((int(ch*W/H),ch)) if W/H<A else im.resize((cw,int(cw*H/W)))
        bg=bg.resize((cw,ch)).filter(ImageFilter.GaussianBlur(45))
        if fill==2:  # fundo liso (foto de estudio com fundo de cor unica: o borrado mostrava o produto borrado)
            import numpy as np; a=np.asarray(im); bd=np.concatenate([a[:8].reshape(-1,3),a[-8:].reshape(-1,3),a[:,:8].reshape(-1,3),a[:,-8:].reshape(-1,3)])
            bg=Image.new('RGB',(cw,ch),tuple(int(x) for x in np.median(bd,0)))
        fg=im.resize((cw,int(cw*H/W))); out=bg.copy(); out.paste(fg,(0,(ch-fg.size[1])//2))
    else:
        if W/H>A: cw,ch=int(H*A),H
        else: cw,ch=W,int(W/A)
        x0=int((W-cw)*ax); y0=int((H-ch)*ay); out=im.crop((x0,y0,x0+cw,y0+ch))
    p=f"assets/broll-src/entrega/{sid}-{'16x9' if split else '9x16'}.jpg"; out.save(p,quality=93)
    t=out.copy(); t.thumbnail((360,360)); c=Image.new('RGB',(360,380),(20,20,20)); c.paste(t,((360-t.size[0])//2,0))
    ImageDraw.Draw(c).text((6,352),f"{sid} {cid} {out.size[0]}x{out.size[1]}",font=fnt,fill=(255,255,0)); th.append(c)
    print(sid,cid,out.size)
sh=Image.new('RGB',(360*7,380*((len(th)+6)//7)),(40,40,40))
for i,c in enumerate(th): sh.paste(c,(360*(i%7),380*(i//7)))
sh.save('work/pesq/sheet_entrega.jpg',quality=85)
```


---

# ARQUIVO: `modelo-projeto/scripts/fal_img.mjs`

```javascript
#!/usr/bin/env node
// Gera UMA imagem-conceito no fal.ai (so quando o Fabio pede uma imagem encenada — ex.: capa do reel).
// Uso: node scripts/fal_img.mjs <modelo> <saida.jpg> <aspect> "<prompt>"
import fs from 'node:fs';
const env = Object.fromEntries(fs.readFileSync(process.env.REEL_ENV || `${process.env.HOME}/Claude/reel-auto/.env`, 'utf8').split('\n').filter(l => l.includes('=')).map(l => [l.slice(0, l.indexOf('=')).trim(), l.slice(l.indexOf('=') + 1).trim()]));
const [model, out, aspect, prompt] = process.argv.slice(2);
const H = { Authorization: `Key ${env.FAL_KEY}`, 'Content-Type': 'application/json' };
const body = model.includes('flux') ? { prompt, aspect_ratio: aspect, raw: true, output_format: 'jpeg', safety_tolerance: '5' }
  : { prompt, aspect_ratio: aspect, num_images: 1, output_format: 'jpeg', resolution: '2K' };
const sub = await (await fetch(`https://queue.fal.run/${model}`, { method: 'POST', headers: H, body: JSON.stringify(body) })).json();
if (!sub.status_url) { console.error(JSON.stringify(sub)); process.exit(1); }
for (let i = 0; i < 120; i++) {
  await new Promise(r => setTimeout(r, 3000));
  const st = await (await fetch(sub.status_url, { headers: H })).json();
  if (st.status === 'COMPLETED') break;
  if (st.status && !['IN_QUEUE', 'IN_PROGRESS'].includes(st.status)) { console.error(JSON.stringify(st)); process.exit(1); }
}
const res = await (await fetch(sub.response_url, { headers: H })).json();
const url = res.images?.[0]?.url; if (!url) { console.error(JSON.stringify(res).slice(0, 500)); process.exit(1); }
fs.writeFileSync(out, Buffer.from(await (await fetch(url)).arrayBuffer()));
console.log(out, res.images[0].width, res.images[0].height);
```


---

# ARQUIVO: `modelo-projeto/scripts/fix_captions.py`

```python
"""Correcoes de texto das legendas (o whisper erra grafia, pontuacao e maiuscula quando o chunk
comeca no meio da frase). Roda depois de align.py. Nao muda timing — so o texto de cada palavra.
A tabela POR VIDEO fica em scripts/captions_fix_table.py (o align.py tambem a le para ignorar as palavras DROP).
IDEMPOTENTE: na 1a execucao guarda a saida do align.py em work/chunks-aligned/ e sempre parte dela.
Para regerar do zero depois de um novo align.py: apagar work/chunks-aligned/chNN-words.json."""
import json, os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from captions_fix_table import FIX, FIXT
SOMENTE={int(x) for x in sys.argv[1:]}  # sem argumento = todos
META={m['i']:m for m in json.load(open('assets/chunks/meta.json'))}
os.makedirs('work/chunks-aligned',exist_ok=True)
for ci in range(len(json.load(open('assets/chunks/meta.json')))):
    if SOMENTE and ci not in SOMENTE: continue
    p=f'assets/chunks/ch{ci:02d}-words.json'; b=f'work/chunks-aligned/ch{ci:02d}-words.json'
    if not os.path.exists(b): shutil.copy(p,b)
    d=json.load(open(b)); n=0
    words=[e for e in d['transcription'] if e['text'].strip() and not e['text'].strip().startswith('[')]
    for k,new in FIX.get(ci,{}).items():
        e=words[k]
        e['text']='' if new is None else ' '+new; n+=1
    for k,src in FIXT.get(ci,{}).items():
        e=words[k]; d0=e['offsets']['to']-e['offsets']['from']; e['offsets']['from']=int(round((src-META[ci]['off'])*1000))
        e['offsets']['to']=max(e['offsets']['to'],e['offsets']['from']+1); n+=1
    json.dump(d,open(p,'w'),ensure_ascii=False)
    if n: print(f"  ch{ci:02d}: {n} correcao(oes) -> "+' '.join(e['text'].strip() for e in words if e['text'].strip()))
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze.py`

```python
"""Varredura de olhar: amostra frames do mezanino nos tempos de TIMELINE em que o
apresentador esta visivel e monta grades para revisao visual."""
import re,subprocess,os,sys,json,math
def win(w0,w1,b):
    f0,f1=b.get('span',[0,1]); return (round(w0+(w1-w0)*f0,3), round(w0+(w1-w0)*f1,3))
from _src import SRC
plan=json.load(open('assets/edit-plan.json')); RATE=plan.get("rate",1.1)
# janelas cobertas por B-roll full (apresentador invisivel)
# timeline -> source pelo plano (o vídeo do apresentador virou um arquivo só: assets/aroll.mp4)
segT=[]; t=0; LEAD=plan.get("jcutLeadFrames",5)/30
for i,s in enumerate(plan["segments"]):
    sd=(s["out"]-s["in"])/RATE; lead=0 if i==0 else min(LEAD,sd-10/30); d=sd-lead
    segT.append({"i":i,"label":s["label"],"t0":round(t,3),"t1":round(t+d,3),
                 "vMedia":round(s["in"]+lead*RATE,3)}); t+=d
cov=[]
for b in (plan.get("broll") or json.load(open("assets/broll-slots.json"))["slots"]):
    if b.get("mode")=="full":
        cov.append(win(segT[b["fromSeg"]]["t0"]-b.get("preStart",0), segT[b["toSeg"]]["t1"], b))
covered=lambda x: any(a<=x<bb for a,bb in cov)
times=[]
x=0.0
while x < segT[-1]["t1"] and '--bordas' not in sys.argv:
    times.append(round(x,2)); x+=0.65
for s in segT:  # densidade extra nas bordas do take (onde ele le o roteiro)
    for off in (0.03,0.12,0.22,0.33):
        times.append(round(s["t0"]+off,2))
    for off in (0.08,0.2,0.32,0.45,0.6,0.8):
        times.append(round(s["t1"]-off,2))
times=sorted({t for t in times if 0<=t<segT[-1]["t1"] and not covered(t)})
args=[a for a in sys.argv[1:] if not a.startswith('--')]
out=args[0] if args else 'gaze/pass1'
os.makedirs(out,exist_ok=True)
for f in os.listdir(out):
    if f.endswith('.jpg') or f.endswith('.png'): os.remove(os.path.join(out,f))
rows=[]
for k,tt in enumerate(times):
    seg=[s for s in segT if s["t0"]-1e-6<=tt<s["t1"]]
    if not seg: continue
    src=round(seg[0]["vMedia"]+(tt-seg[0]["t0"])*RATE,3)
    lab=seg[0]["label"]
    rel_end=round((seg[0]["t1"]-tt),2)
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(src),'-i',SRC,
      '-frames:v','1','-vf','crop=720:280:250:1100,scale=300:-1',f'{out}/f{k:03d}.jpg'],check=True)
    rows.append({"k":k,"t":tt,"src":src,"seg":seg[0]["i"],"label":lab,"toEnd":rel_end})
json.dump(rows,open(f'{out}/index.json','w'),indent=1)
print(f"{len(rows)} frames -> {out}")
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze_blend.py`

```python
"""Olhar para baixo/lado por blendshapes do FaceLandmarker (.models/face_landmarker.task),
quadro a quadro nas bordas de cada take (últimos 1,6 s e primeiros 0,6 s) + meio do take.
Saída gaze/blend.json: {seg: [{t, down, out, inn, blink}]}; down = média eyeLookDown L/R,
side = max(eyeLookOut/In) com sinal (+ = direita da tela)."""
import json, cv2, mediapipe as mp, numpy as np, sys
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
from _src import SRC
P=json.load(open('assets/edit-plan.json'))
opt=vision.FaceLandmarkerOptions(base_options=mpt.BaseOptions(model_asset_path='.models/face_landmarker.task'),
    output_face_blendshapes=True,num_faces=1,running_mode=vision.RunningMode.IMAGE)
lmk=vision.FaceLandmarker.create_from_options(opt)
cap=cv2.VideoCapture(SRC); FPS=30
segs=[int(x) for x in sys.argv[1:]] or range(len(P['segments']))
out={}
for i in segs:
    s=P['segments'][i]; mid=(s['in']+s['out'])/2
    wins=[(s['in']-0.5,s['in']+0.6),(mid-0.5,mid+0.5),(s['out']-1.6,s['out']+0.3)]
    rows=[]
    for a,b in wins:
        f0=int(round(max(0,a)*FPS)); cap.set(cv2.CAP_PROP_POS_FRAMES,f0)
        for f in range(f0,int(round(b*FPS))+1):
            ok,fr=cap.read()
            if not ok: break
            img=mp.Image(image_format=mp.ImageFormat.SRGB,data=cv2.cvtColor(cv2.resize(fr,(540,960)),cv2.COLOR_BGR2RGB))
            r=lmk.detect(img)
            if not r.face_blendshapes: continue
            d={c.category_name:c.score for c in r.face_blendshapes[0]}
            rows.append({"t":round(f/FPS,3),"down":round((d['eyeLookDownLeft']+d['eyeLookDownRight'])/2,3),
              "up":round((d['eyeLookUpLeft']+d['eyeLookUpRight'])/2,3),
              "blink":round((d['eyeBlinkLeft']+d['eyeBlinkRight'])/2,3),
              "side":round(((d['eyeLookOutLeft']+d['eyeLookInRight'])-(d['eyeLookInLeft']+d['eyeLookOutRight']))/2,3)})
    out[i]=rows; print(i, len(rows), flush=True)
json.dump(out,open('gaze/blend.json','w'))
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze_bounds.py`

```python
"""Varredura das FRONTEIRAS de take: últimos ~0,8 s e primeiros ~0,3 s de cada take,
onde o apresentador lê o roteiro. Monta uma folha de olhos por lote, com o gx medido."""
import subprocess,sys,os,json
from _src import SRC
M={round(o['t'],3):o for o in json.load(open('gaze/measure.json')) if o.get('ok')}
P=json.load(open('assets/edit-plan.json'))
os.makedirs('work/gb',exist_ok=True)
CROP='crop=680:320:220:1080,scale=340:160'
subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=c=#101014:s=340x160:d=1','-frames:v','1','work/gb/pad.jpg'],check=True)
def gx(t):
    n=min(M,key=lambda k:abs(k-t)); return M[n]['gx']
def folha(nome,itens,cols=6):
    files=[]
    for k,(lab,t) in enumerate(itens):
        f=f'work/gb/{nome}_{k:03d}.jpg'
        subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{t:.3f}','-i',SRC,'-frames:v','1',
            '-vf',CROP,f],check=True)
        files.append(f)
    while len(files)%cols: files.append('work/gb/pad.jpg')
    args=[];  [args.extend(['-i',f]) for f in files]
    rows=[files[i:i+cols] for i in range(0,len(files),cols)]
    fc='';ro=[];idx=0
    for ri,r in enumerate(rows):
        fc+=''.join(f'[{idx+j}:v]' for j in range(len(r)))+f'hstack=inputs={len(r)}[r{ri}];'; idx+=len(r); ro.append(f'[r{ri}]')
    fc+=''.join(ro)+f'vstack=inputs={len(rows)}[out]'
    subprocess.run(['ffmpeg','-v','error','-y']+args+['-filter_complex',fc,'-map','[out]',f'work/gb/{nome}.jpg'],check=True)
    print(f'work/gb/{nome}.jpg  ({len(itens)} quadros, {cols} col)')
    for r in range(0,len(itens),cols):
        print('   '+'  '.join(f'{lab}@{t:.2f}:{gx(t):+.3f}' for lab,t in itens[r:r+cols]))
segs=P['segments']
tails=[];heads=[]
for i,s in enumerate(segs):
    for d in (0.55,0.38,0.22,0.07):
        tails.append((f'{i}T', s['out']-d))
    if i: 
        for d in (0.04,0.16,0.30):
            heads.append((f'{i}H', s['in']+d))
lote=sys.argv[1] if len(sys.argv)>1 else 'todos'
if lote in ('todos','tails'):
    for b in range(0,len(tails),36): folha(f'tails{b//36}',tails[b:b+36])
if lote in ('todos','heads'):
    for b in range(0,len(heads),36): folha(f'heads{b//36}',heads[b:b+36])
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze_down.py`

```python
"""Olhar PARA BAIXO (leitura do roteiro) nas bordas de cada take — o gx do gaze_report só vê
desvio lateral. Usa a abertura do olho (op) de gaze/measure.json: olhar para baixo baixa a
pálpebra por vários quadros seguidos; piscada dura < 0,2 s.
Imprime, por take, a faixa do source em que op < LIM x mediana do próprio take (>= 0,24 s)."""
import json, numpy as np, sys
M=[o for o in json.load(open('gaze/measure.json')) if o.get('ok')]
plan=json.load(open('assets/edit-plan.json'))
LIM=float(sys.argv[1]) if len(sys.argv)>1 else 0.8
for i,s in enumerate(plan['segments']):
    xs=[o for o in M if s['in']-0.05<=o['t']<=s['out']+0.05]
    if not xs: continue
    med=np.median([o['op'] for o in xs])
    runs=[];cur=None
    for o in xs:
        low=o['op']<LIM*med
        if low: cur=[o['t'],o['t']] if cur is None else [cur[0],o['t']]
        else:
            if cur and cur[1]-cur[0]>=0.24: runs.append(cur)
            cur=None
    if cur and cur[1]-cur[0]>=0.24: runs.append(cur)
    tags=[]
    for a,b in runs:
        pos='INICIO' if a-s['in']<0.5 else ('FIM' if s['out']-b<1.0 else 'meio')
        tags.append(f"{a:.2f}-{b:.2f}({pos})")
    if tags: print(f"{i:2} {s['label']:<12} in {s['in']:.2f} out {s['out']:.2f} | "+'  '.join(tags))
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze_lids.py`

```python
"""Leitura do roteiro para BAIXO (padrão do reel André Esteves): cabeça abaixa e a pálpebra
cobre a íris. Métrica: op (abertura do olho) relativa ao começo do PRÓPRIO take (0,15–0,7 s,
quando ele está de olhos abertos na câmera). Sustentado >= 0,24 s abaixo de LIM = desvio
(piscada dura menos). Imprime início do desvio (source) e quanto antes do out ele começa."""
import json, numpy as np, sys
M=[o for o in json.load(open('gaze/measure.json')) if o.get('ok')]
P=json.load(open('assets/edit-plan.json')); LIM=float(sys.argv[1]) if len(sys.argv)>1 else 0.72
res=[]
for i,s in enumerate(P['segments']):
    st=[o['op'] for o in M if s['in']+0.15<=o['t']<=s['in']+0.7]
    ref=np.percentile(st,70)
    xs=[o for o in M if s['in']<=o['t']<=s['out']]
    runs=[];cur=None
    for o in xs:
        if o['op']<LIM*ref: cur=[o['t'],o['t']] if cur is None else [cur[0],o['t']]
        else:
            if cur and cur[1]-cur[0]>=0.24: runs.append(cur)
            cur=None
    if cur and cur[1]-cur[0]>=0.16: runs.append(cur)
    res.append({"seg":i,"label":s['label'],"runs":[[round(a,2),round(b,2)] for a,b in runs]})
    print(f"{i:2} {s['label']:<12} {s['in']:6.2f}-{s['out']:6.2f} "+'  '.join(f"{a:.2f}-{b:.2f}(fim-{s['out']-a:.2f})" for a,b in runs))
json.dump(res,open('gaze/lids.json','w'),indent=1)
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze_measure.py`

```python
"""Mede desvio de olhar quadro a quadro no mezanino (FaceMesh + iris refinada).
gx > 0 => iris deslocada para a DIREITA DA TELA ; yaw > 0 => cabeca virada p/ direita da tela."""
import cv2, json, numpy as np, mediapipe as mp
from _src import SRC
STEP=0.08
fm=mp.solutions.face_mesh.FaceMesh(static_image_mode=False,max_num_faces=1,
    refine_landmarks=True,min_detection_confidence=0.5,min_tracking_confidence=0.5)
R_OUT,R_IN=33,133; L_IN,L_OUT=362,263
RIRIS=[469,470,471,472]; LIRIS=[474,475,476,477]
cap=cv2.VideoCapture(SRC); fps=cap.get(cv2.CAP_PROP_FPS)
out=[]; nxt=0.0; i=0
while True:
    ok,frame=cap.read()
    if not ok: break
    t=i/fps; i+=1
    if t+1e-9<nxt: continue
    nxt+=STEP
    small=cv2.resize(frame,(540,960))
    res=fm.process(cv2.cvtColor(small,cv2.COLOR_BGR2RGB))
    if not res.multi_face_landmarks:
        out.append({"t":round(t,3),"ok":0}); continue
    lm=res.multi_face_landmarks[0].landmark
    def ratio(inn,outr,iris):
        xi,xo=lm[inn].x,lm[outr].x
        cx=sum(lm[k].x for k in iris)/len(iris); w=xo-xi
        return (cx-xi)/w if abs(w)>1e-6 else 0.5
    rr=ratio(R_IN,R_OUT,RIRIS); lr=ratio(L_IN,L_OUT,LIRIS)
    gx=((0.5-rr)+(lr-0.5))/2
    x33,x263,xn=lm[33].x,lm[263].x,lm[1].x
    yaw=(xn-(x33+x263)/2)/abs(x263-x33) if abs(x263-x33)>1e-6 else 0
    op=((lm[145].y-lm[159].y)+(lm[374].y-lm[386].y))/2
    # gy: altura da íris em relação à linha dos cantos do olho, normalizada pela largura do olho
    # (gy maior => olhar para BAIXO — leitura do roteiro abaixo da câmera, reel André Esteves)
    def vy(a,b,iris):
        cy=sum(lm[k].y for k in iris)/len(iris); return (cy-(lm[a].y+lm[b].y)/2)/max(1e-6,abs(lm[b].x-lm[a].x))
    gy=(vy(33,133,RIRIS)+vy(362,263,LIRIS))/2
    out.append({"t":round(t,3),"ok":1,"gx":round(gx,4),"yaw":round(yaw,4),"op":round(op,5),"gy":round(gy,4)})
cap.release()
json.dump(out,open('gaze/measure.json','w'))
g=[o for o in out if o.get("ok")]
print(f"{len(out)} amostras, {len(g)} com rosto")
for k in ("gx","yaw","op","gy"):
    v=np.array([o[k] for o in g])
    print(f"  {k}: mediana {np.median(v):+.4f}  p2 {np.percentile(v,2):+.4f}  p98 {np.percentile(v,98):+.4f}  sd {v.std():.4f}")
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze_pairs.py`

```python
"""Revisão visual por take: [meio do take = referência] | início +0.03/+0.25 | fim -0.9/-0.6/-0.35/-0.12.
Cada linha = 1 take (tempos de SOURCE, já descontando videoTail). Uso: gaze_pairs.py <saida> [seg ...]"""
import json,subprocess,os,sys
from _src import SRC
plan=json.load(open('assets/edit-plan.json')); out=sys.argv[1]; only=[int(x) for x in sys.argv[2:]]
os.makedirs(out,exist_ok=True)
rows=[]
for i,s in enumerate(plan['segments']):
    if only and i not in only: continue
    a=s['in']+ (0.17*1.1 if i else 0); b=s.get('videoTail') or s['out']
    ts=[(a+b)/2, a+0.03, a+0.25, b-0.9, b-0.6, b-0.35, b-0.12]
    files=[]
    for k,t in enumerate(ts):
        f=f'{out}/s{i:02d}_{k}.jpg'
        subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{t:.3f}','-i',SRC,'-frames:v','1','-vf',
          'crop=640:400:230:1040,scale=320:-1',f],check=True); files.append(f)
    subprocess.run(['ffmpeg','-v','error','-y',*sum([['-i',f] for f in files],[]),'-filter_complex',
      f"{''.join(f'[{k}]' for k in range(7))}hstack=7",f'{out}/row{i:02d}.jpg'],check=True)
    for f in files: os.remove(f)
    rows.append(i)
for g in range(0,len(rows),8):
    rr=rows[g:g+8]
    subprocess.run(['ffmpeg','-v','error','-y',*sum([['-i',f'{out}/row{i:02d}.jpg'] for i in rr],[]),'-filter_complex',
      (f"{''.join(f'[{k}]' for k in range(len(rr)))}vstack={len(rr)}" if len(rr)>1 else '[0]copy'),f'{out}/P{g//8}.jpg'],check=True)
    print(f'P{g//8}: segs {rr}')
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze_pose.py`

```python
"""Varredura de olhar COMPENSADA pela pose da cabeca (reel KAZUO INAMORI).
Motivo: os blendshapes eyeLook* medem o olho DENTRO da cabeca. Este apresentador grava de perto e mexe muito a cabeca
sem tirar o olho da lente — o gaze_windows.py marcava 40 janelas / 19,5 s que eram quase todas giro de cabeca.
Aqui: yaw/pitch da cabeca (matriz de transformacao facial) + centro do rosto no quadro; regressao robusta
side ~ yaw + cx e vert(down-up) ~ pitch + cy (quem olha para a lente compensa o giro com o olho). O RESIDUO e o desvio real.
Saida: gaze/pose.json (amostras com rs, rv) e gaze/pose-windows.json (janelas |residuo| > K sigma, >= 0,15 s, sem piscada).
Uso: gaze_pose.py [K=3.0]"""
import json, sys, cv2, numpy as np, mediapipe as mp, os
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
from _src import SRC
K=float(sys.argv[1]) if len(sys.argv)>1 else 3.0
if not os.path.exists('gaze/pose-raw.json') or '--remeasure' in sys.argv:
    T=json.load(open('gaze/tl.json'))
    bysrc={}
    for o in T: bysrc.setdefault(round(o['src'],3),[]).append(o)
    opt=vision.FaceLandmarkerOptions(base_options=mpt.BaseOptions(model_asset_path='.models/face_landmarker.task'),
        output_face_blendshapes=True,output_facial_transformation_matrixes=True,num_faces=1,running_mode=vision.RunningMode.IMAGE)
    lmk=vision.FaceLandmarker.create_from_options(opt)
    cap=cv2.VideoCapture(SRC); fps=cap.get(cv2.CAP_PROP_FPS); n=0; out=[]
    while True:
        if not cap.grab(): break
        src=round(n/fps,3); n+=1
        if src not in bysrc: continue
        ok,fr=cap.retrieve()
        r=lmk.detect(mp.Image(image_format=mp.ImageFormat.SRGB,data=cv2.cvtColor(cv2.resize(fr,(540,960)),cv2.COLOR_BGR2RGB)))
        if not r.face_blendshapes: continue
        d={c.category_name:c.score for c in r.face_blendshapes[0]}
        M=np.array(r.facial_transformation_matrixes[0])[:3,:3]
        yaw=float(np.degrees(np.arctan2(M[0,2],M[2,2]))); pitch=float(np.degrees(np.arcsin(-M[1,2])))
        L=r.face_landmarks[0]; cx=float(np.mean([L[i].x for i in (33,133,362,263)])); cy=float(np.mean([L[i].y for i in (33,133,362,263)]))
        side=((d['eyeLookOutLeft']+d['eyeLookInRight'])-(d['eyeLookInLeft']+d['eyeLookOutRight']))/2
        vert=((d['eyeLookDownLeft']+d['eyeLookDownRight'])-(d['eyeLookUpLeft']+d['eyeLookUpRight']))/2
        blink=(d['eyeBlinkLeft']+d['eyeBlinkRight'])/2
        for o in bysrc[src]: out.append(dict(t=o['t'],seg=o['seg'],src=src,yaw=round(yaw,2),pitch=round(pitch,2),cx=round(cx,4),cy=round(cy,4),side=round(side,3),vert=round(vert,3),blink=round(blink,3)))
    out.sort(key=lambda o:o['t']); json.dump(out,open('gaze/pose-raw.json','w'))
S=json.load(open('gaze/pose-raw.json'))
def fit(y,X):
    w=np.ones(len(y))
    for _ in range(8):
        A=np.c_[X,np.ones(len(y))]*w[:,None]; c=np.linalg.lstsq(A,y*w,rcond=None)[0]
        r=y-np.c_[X,np.ones(len(y))]@c; s=1.4826*np.median(np.abs(r-np.median(r)))
        w=(np.abs(r)<2.5*s).astype(float)
    return c,r,s
nb=np.array([o['blink']<0.4 for o in S])
side=np.array([o['side'] for o in S]); vert=np.array([o['vert'] for o in S])
Xs=np.array([[o['yaw'],o['cx']] for o in S]); Xv=np.array([[o['pitch'],o['cy']] for o in S])
cs,_,ss=fit(side[nb],Xs[nb]); cv_,_,sv=fit(vert[nb],Xv[nb])
rs=side-np.c_[Xs,np.ones(len(S))]@cs; rv=vert-np.c_[Xv,np.ones(len(S))]@cv_
print(f"side ~ {cs[0]:+.4f}*yaw {cs[1]:+.3f}*cx  sigma {ss:.3f} | vert ~ {cv_[0]:+.4f}*pitch {cv_[1]:+.3f}*cy  sigma {sv:.3f}  ({len(S)} amostras)")
for o,a,b in zip(S,rs,rv): o['rs']=round(float(a/ss),2); o['rv']=round(float(b/sv),2)
json.dump(S,open('gaze/pose.json','w'))
W=[];cur=None
for o in S:
    f=o['blink']<0.4 and (abs(o['rs'])>K or o['rv']>K)
    if f:
        if cur and o['t']-cur[1]<=0.1: cur[1]=o['t']; cur[2].append(o)
        else:
            if cur: W.append(cur)
            cur=[o['t'],o['t'],[o]]
if cur: W.append(cur)
res=[]
for a,b,os_ in W:
    if b-a+0.033<0.15: continue
    m=max(os_,key=lambda o:max(abs(o['rs']),o['rv']))
    res.append(dict(t0=round(a,2),t1=round(b+0.033,2),seg=os_[0]['seg'],rs=float(np.mean([o['rs'] for o in os_])),rv=float(np.mean([o['rv'] for o in os_])),pico=max(abs(m['rs']),m['rv'])))
    print(f"{a:6.2f}-{b+0.033:6.2f} ({b-a+0.033:.2f}s) seg{os_[0]['seg']:>2}  lado {res[-1]['rs']:+.1f}σ  baixo {res[-1]['rv']:+.1f}σ  pico {res[-1]['pico']:.1f}σ")
json.dump(res,open('gaze/pose-windows.json','w'),indent=1)
print(f"{len(res)} janelas, {sum(r['t1']-r['t0'] for r in res):.1f}s (K={K})")
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze_report.py`

```python
import json, numpy as np, sys
def win(w0,w1,b):
    f0,f1=b.get('span',[0,1]); return (round(w0+(w1-w0)*f0,3), round(w0+(w1-w0)*f1,3))
M=json.load(open('gaze/measure.json'))
plan=json.load(open('assets/edit-plan.json')); RATE=plan.get('rate',1.1); F=lambda n:n/30
LEAD=F(plan.get('jcutLeadFrames',5))
segs=[];t=0
for i,s in enumerate(plan['segments']):
    sd=(s['out']-s['in'])/RATE; lead=0 if i==0 else min(LEAD,sd-F(10)); d=sd-lead
    segs.append({"i":i,"label":s["label"],"in":s["in"],"out":s["out"],"tail":s.get("videoTail"),
                 "t0":round(t,3),"t1":round(t+d,3),"lead":lead}); t+=d
ed=[ (s['out']-s['tail'])/RATE if s['tail'] else 0 for s in segs]
for i,s in enumerate(segs):
    dPrev=ed[i-1] if i>0 else 0
    s['vStart']=round(s['t0']-dPrev,3); s['vEnd']=round(s['t1']-ed[i],3)
    s['vMedia']=round(s['in']+(s['lead']-dPrev)*RATE,3)
def src2tl(i,x):
    s=segs[i]; return round(s['vStart']+(x-s['vMedia'])/RATE,3)
# janelas em que o apresentador aparece
# cobertura por JANELA de timeline (inclui preStart), nao por segmento:
# um cutaway antecipado cobre o fim do take anterior.
fullW=[]; splitW=[]
for b in (plan.get('broll') or json.load(open('assets/broll-slots.json'))['slots']):
    w=win(segs[b['fromSeg']]['t0']-b.get('preStart',0), segs[b['toSeg']]['t1'], b)
    (fullW if b['mode']=='full' else splitW).append(w)
def merge(ws):
    # tomadas seguidas da mesma cena sao janelas contiguas: sem unir, um desvio em cima da
    # emenda (ex. 18,57 s) era reportado como descoberto so por cair entre duas tomadas.
    out=[]
    for w0,w1 in sorted(ws):
        if out and w0<=out[-1][1]+0.03: out[-1][1]=max(out[-1][1],w1)
        else: out.append([w0,w1])
    return out
fullW=merge(fullW); splitW=merge(splitW)
def cover(a,b):
    if any(w0<=a+0.02 and b<=w1+0.02 for w0,w1 in fullW): return "B-ROLL"
    if any(w0<=a+0.02 and b<=w1+0.02 for w0,w1 in splitW): return "split"
    return "CHEIA"
ok=[o for o in M if o.get('ok')]
med=np.median([o['gx'] for o in ok]); opmed=np.median([o['op'] for o in ok])
byt={round(o['t'],3):o for o in ok}; ts=sorted(byt)
THR=float(sys.argv[1]) if len(sys.argv)>1 else 0.028
rows=[]
for s in segs:
    i=s['i']
    lo,hi=s['vMedia'], s['vMedia']+(s['vEnd']-s['vStart'])*RATE
    flags=[(x,(byt[x]['op']>=opmed*0.55) and abs(byt[x]['gx']-med)>THR,byt[x]['gx'])
           for x in ts if lo-0.02<=x<=hi+0.02]
    wins=[];cur=None
    for x,f,g in flags:
        if f: cur=[x,x,[g]] if cur is None else [cur[0],x,cur[2]+[g]]
        else:
            if cur and cur[1]-cur[0]>=0.15: wins.append(cur)
            cur=None
    if cur and cur[1]-cur[0]>=0.15: wins.append(cur)
    for a,b,gv in wins:
        pos="INICIO" if a-lo<0.5 else ("FIM" if hi-b<1.0 else "MEIO")
        rows.append({"seg":i,"label":s['label'],"vis":cover(src2tl(i,a),src2tl(i,b)),"a":round(a,2),"b":round(b,2),
                     "dur":round(b-a+0.08,2),"gx":round(float(np.mean(gv)),4),"pos":pos,
                     "tl0":src2tl(i,a),"tl1":src2tl(i,b)})
print(f"limiar |gx-{med:+.4f}| > {THR}\n")
print(f"{'seg':<5}{'label':<12}{'visivel':<8}{'src':<16}{'dur':>5} {'gx':>8} {'pos':<7}{'timeline':<15}{'acao'}")
for r in rows:
    need = r['vis']!='B-ROLL'
    print(f"{r['seg']:<5}{r['label']:<12}{r['vis']:<8}{r['a']:.2f}-{r['b']:.2f}   {r['dur']:>4.2f} {r['gx']:+8.4f} {r['pos']:<7}{r['tl0']:.2f}-{r['tl1']:.2f}   {'<< VERIFICAR' if need else 'coberto'}")
json.dump(rows,open('gaze/windows.json','w'),indent=1)
print(f"\n{len(rows)} janelas | {sum(1 for r in rows if r['vis']!='B-ROLL')} com apresentador visivel")
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze_review.py`

```python
"""Folhas de conferencia MAIORES das janelas de leitura (gaze/tl-windows.json).
Por janela: [REF = quadro do mesmo take com olhar mais proximo da mediana] | 5 quadros de t0-0,1 a t1+0,1.
Recorte acompanha o rosto (centro dos olhos pelo FaceLandmarker), 640x250 px do mezanino -> 384x150.
Uso: gaze_review.py [saida=gaze/rev]"""
import json, cv2, sys, os, numpy as np, mediapipe as mp
from PIL import Image, ImageDraw, ImageFont
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
from _src import SRC
W=json.load(open('gaze/tl-windows.json')); T=[o for o in json.load(open('gaze/tl.json')) if o['ok']]
out=sys.argv[1] if len(sys.argv)>1 else 'gaze/rev'; os.makedirs(out,exist_ok=True)
ms=np.median([o['side'] for o in T]); md=np.median([o['down'] for o in T])
lmk=vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=mpt.BaseOptions(model_asset_path='.models/face_landmarker.task'),num_faces=1))
cap=cv2.VideoCapture(SRC); fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',24)
TW,TH=384,150
def frame(o,lab):
    cap.set(cv2.CAP_PROP_POS_MSEC,o['src']*1000); ok,f=cap.read()
    r=lmk.detect(mp.Image(image_format=mp.ImageFormat.SRGB,data=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)))
    if r.face_landmarks:
        L=r.face_landmarks[0]; cx=int(np.mean([L[i].x for i in (33,263)])*f.shape[1]); cy=int(np.mean([L[i].y for i in (33,133,362,263)])*f.shape[0])
    else: cx,cy=720,1330
    x0=max(0,min(f.shape[1]-640,cx-320)); y0=max(0,min(f.shape[0]-250,cy-125))
    c=cv2.resize(f[y0:y0+250,x0:x0+640],(TW,TH)); im=Image.fromarray(cv2.cvtColor(c,cv2.COLOR_BGR2RGB))
    d=ImageDraw.Draw(im); d.rectangle([0,0,len(lab)*14+6,28],fill=(0,0,0)); d.text((3,1),lab,font=fnt,fill=(255,255,0)); return im
rows=[]
for k,w in enumerate(W):
    seg=[o for o in T if o['seg']==w['seg'] and not (w['t0']-0.3<=o['t']<=w['t1']+0.3) and o['blink']<0.3]
    ref=min(seg or T,key=lambda o:abs(o['side']-ms)+abs(o['down']-md))
    ts=np.linspace(w['t0']-0.1,w['t1']+0.1,5)
    row=Image.new('RGB',(80+TW*6+10,TH),(16,16,20)); d=ImageDraw.Draw(row); d.text((4,55),f"w{k}",font=fnt,fill=(255,255,255))
    row.paste(frame(ref,f"REF {ref['t']:.2f}"),(80,0))
    for j,t in enumerate(ts):
        o=min(T,key=lambda x:abs(x['t']-t)); row.paste(frame(o,f"{o['t']:.2f}"),(80+TW*(j+1)+10,0))
    rows.append(row)
for g in range(0,len(rows),8):
    B=rows[g:g+8]; sh=Image.new('RGB',(B[0].width,(TH+4)*len(B)),(60,60,60))
    for j,r in enumerate(B): sh.paste(r,(0,j*(TH+4)))
    p=f"{out}/r{g//8:02d}.jpg"; sh.save(p,quality=88); print(p,f"w{g}-w{g+len(B)-1}")
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze_sheet.py`

```python
"""MOTOR (kit v3). Folhas de conferencia do olhar com o ROSTO INTEIRO (o recorte do gaze_review.py corta a testa e
precisava ser medido por bruto). O recorte sai sozinho: FaceLandmarker em 9 quadros do aroll -> caixa mediana do rosto.
Junta as janelas de gaze/pose-windows.json (P) e gaze/tl-windows.json (T, so as que nao cruzam uma P); 4 quadros por
janela (antes, 1/3, 2/3, depois), 12 janelas por folha -> gaze/me/gNN.jpg. Ler as folhas e listar as NITIDAS.
uso: python3 scripts/gaze_sheet.py      (depois de gaze_tl.py, gaze_windows.py e gaze_pose.py)"""
import json, subprocess, os, cv2, numpy as np, mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
from PIL import Image, ImageDraw, ImageFont
V = 'assets/aroll.mp4'
lm = vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=BaseOptions(model_asset_path='.models/face_landmarker.task')))
cap = cv2.VideoCapture(V); n = int(cap.get(7)); W = int(cap.get(3)); H = int(cap.get(4)); boxes = []
for f in np.linspace(n * 0.05, n * 0.95, 9).astype(int):
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(f)); ok, im = cap.read()
    if not ok: continue
    r = lm.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(im, cv2.COLOR_BGR2RGB)))
    if r.face_landmarks:
        xs = [p.x for p in r.face_landmarks[0]]; ys = [p.y for p in r.face_landmarks[0]]
        boxes.append((min(xs) * W, min(ys) * H, max(xs) * W, max(ys) * H))
x0, y0, x1, y1 = np.median(np.array(boxes), 0)
fw = (x1 - x0) * 1.25; fh = fw * 0.72                       # testa ate a boca, com folga
cx, cy = (x0 + x1) / 2, y0 + (y1 - y0) * 0.30
cw, ch = int(fw) // 2 * 2, int(fh) // 2 * 2
cx0 = int(max(0, min(W - cw, cx - cw / 2))); cy0 = int(max(0, min(H - ch, cy - ch / 2)))
print(f'recorte do rosto: {cw}x{ch} em ({cx0},{cy0}) de {W}x{H}')
P = json.load(open('gaze/pose-windows.json')) if os.path.exists('gaze/pose-windows.json') else []
T = json.load(open('gaze/tl-windows.json'))
Wn = [(w['t0'], w['t1'], 'P') for w in P]
for w in T:
    a, b = w['t0'], w['t1']
    if not any(min(b, x[1]) - max(a, x[0]) > 0 for x in Wn): Wn.append((a, b, 'T'))
Wn.sort()
TW, TH = 300, int(300 * ch / cw)
F = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 22)
os.makedirs('gaze/me', exist_ok=True)
def frame(t):
    d = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{max(0,t):.3f}', '-i', V, '-frames:v', '1', '-vf', f'crop={cw}:{ch}:{cx0}:{cy0},scale={TW}:{TH}',
                        '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
    return Image.frombytes('RGB', (TW, TH), d) if len(d) == TW * TH * 3 else Image.new('RGB', (TW, TH))
rows = [(k, a, b, s, [a - 0.15, a + (b - a) / 3, a + 2 * (b - a) / 3, b + 0.1]) for k, (a, b, s) in enumerate(Wn)]
per = 12
for p in range(0, len(rows), per):
    S = Image.new('RGB', (160 + 4 * (TW + 2), per * (TH + 2)), 'black'); d = ImageDraw.Draw(S)
    for r, (k, a, b, s, ts) in enumerate(rows[p:p + per]):
        y = r * (TH + 2); d.text((4, y + TH // 3), f'#{k} {s}\n{a:.2f}\n{b:.2f}', fill='yellow', font=F)
        for j, t in enumerate(ts):
            S.paste(frame(t), (160 + j * (TW + 2), y)); d.text((164 + j * (TW + 2), y + 2), f'{t:.2f}', fill='yellow', font=F)
    S.save(f'gaze/me/g{p // per:02d}.jpg', quality=85)
print(f'{len(rows)} janelas -> gaze/me/g00..g{(len(rows) - 1) // per:02d}.jpg')
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze_tl.py`

```python
"""Olhar quadro a quadro NA TIMELINE (30 amostras/s), so onde o apresentador aparece em algum take.
FaceLandmarker (.models/face_landmarker.task) com blendshapes: down/up (eyeLookDown/Up), side (+ = direita
da tela), blink. Le o mezanino em sequencia (rapido) e converte source->timeline pela mesma conta do
build-edit.mjs (lead do J-cut, videoTail). Saida: gaze/tl.json [{t, seg, src, down, up, side, blink}].
Depois: scripts/gaze_windows.py transforma em janelas de leitura."""
import json, cv2, mediapipe as mp
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
from _src import SRC
P=json.load(open('assets/edit-plan.json')); RATE=P.get('rate',1.1); F=1/30; LEAD=P.get('jcutLeadFrames',5)*F
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/RATE,3); lead=0 if i==0 else min(LEAD,sd-10*F); d=round(sd-lead,3)
    segs.append(dict(i=i,t0=round(t,3),t1=round(t+d,3),lead=lead,**s)); t=round(t+d,3)
ed=[round((s['out']-s['videoTail'])/RATE,3) if s.get('videoTail') else 0 for s in segs]
R=[]  # (src0, src1, vStart, seg)
for k,s in enumerate(segs):
    dPrev=ed[k-1] if k>0 else 0
    vS=round(s['t0']-dPrev,3); vE=round(s['t1']-ed[k],3); vM=round(s['in']+(s['lead']-dPrev)*RATE,3)
    R.append((vM, vM+(vE-vS)*RATE, vS, k))
opt=vision.FaceLandmarkerOptions(base_options=mpt.BaseOptions(model_asset_path='.models/face_landmarker.task'),
    output_face_blendshapes=True,num_faces=1,running_mode=vision.RunningMode.IMAGE)
lmk=vision.FaceLandmarker.create_from_options(opt)
cap=cv2.VideoCapture(SRC); fps=cap.get(cv2.CAP_PROP_FPS); n=0; out=[]
while True:
    ok=cap.grab()
    if not ok: break
    src=n/fps; n+=1
    hit=[r for r in R if r[0]-1e-6<=src<r[1]]
    if not hit: continue
    # 30 amostras por segundo de TIMELINE ~ 33 por segundo de source: pega 1 quadro a cada 2 (60 fps)
    if (n-1)%2: continue
    ok,fr=cap.retrieve()
    img=mp.Image(image_format=mp.ImageFormat.SRGB,data=cv2.cvtColor(cv2.resize(fr,(540,960)),cv2.COLOR_BGR2RGB))
    r=lmk.detect(img)
    for s0,s1,vS,k in hit:
        tl=round(vS+(src-s0)/RATE,3)
        if not r.face_blendshapes: out.append({"t":tl,"seg":k,"src":round(src,3),"ok":0}); continue
        d={c.category_name:c.score for c in r.face_blendshapes[0]}
        out.append({"t":tl,"seg":k,"src":round(src,3),"ok":1,
            "down":round((d['eyeLookDownLeft']+d['eyeLookDownRight'])/2,3),
            "up":round((d['eyeLookUpLeft']+d['eyeLookUpRight'])/2,3),
            "blink":round((d['eyeBlinkLeft']+d['eyeBlinkRight'])/2,3),
            "side":round(((d['eyeLookOutLeft']+d['eyeLookInRight'])-(d['eyeLookInLeft']+d['eyeLookOutRight']))/2,3)})
out.sort(key=lambda o:o['t'])
json.dump(out,open('gaze/tl.json','w'))
print(f"{len(out)} amostras na timeline ({sum(o['ok'] for o in out)} com rosto)")
```


---

# ARQUIVO: `modelo-projeto/scripts/gaze_windows.py`

```python
"""Janelas de leitura de roteiro na timeline a partir de gaze/tl.json (gaze_tl.py).
Suspeito = |side - mediana| > SIDE ou down - mediana > DOWN, sem piscada, sustentado >= MIN s.
Imprime as janelas (timeline) e grava gaze/tl-windows.json. E pista: confirmar nas faixas (vw_tl.py)."""
import json, numpy as np, sys
M=[o for o in json.load(open('gaze/tl.json')) if o['ok']]
SIDE=float(sys.argv[1]) if len(sys.argv)>1 else 0.17
DOWN=float(sys.argv[2]) if len(sys.argv)>2 else 0.11
MIN=0.15
ms=np.median([o['side'] for o in M]); md=np.median([o['down'] for o in M])
def flag(o): return o['blink']<0.4 and (abs(o['side']-ms)>SIDE or o['down']-md>DOWN)
W=[];cur=None
for o in M:
    if flag(o):
        if cur and o['t']-cur[1]<=0.1: cur[1]=o['t']; cur[2].append(o)
        else:
            if cur: W.append(cur)
            cur=[o['t'],o['t'],[o]]
if cur: W.append(cur)
W=[w for w in W if w[1]-w[0]>=MIN]
res=[]
for a,b,os_ in W:
    sd=np.mean([o['side'] for o in os_])-ms; dn=np.mean([o['down'] for o in os_])-md
    res.append({"t0":round(a,2),"t1":round(b+0.033,2),"seg":os_[0]['seg'],"side":round(float(sd),3),"down":round(float(dn),3)})
    print(f"{a:6.2f}-{b+0.033:6.2f} ({b-a+0.033:.2f}s) seg{os_[0]['seg']:>2}  side{sd:+.2f} down{dn:+.2f}")
json.dump(res,open('gaze/tl-windows.json','w'),indent=1)
print(f"{len(res)} janelas, {sum(r['t1']-r['t0'] for r in res):.1f}s (mediana side {ms:+.3f} down {md:.3f})")
```


---

# ARQUIVO: `modelo-projeto/scripts/gimg.mjs`

```javascript
#!/usr/bin/env node
// Busca no Google Imagens (Serper /images, chave em ~/Claude/reel-auto/.env, ou no arquivo apontado por $REEL_ENV) — imprime os resultados
// com tamanho, dominio e links. Uso: node scripts/gimg.mjs "consulta" [n=20]   (filtro de tamanho grande: tbs=isz:l)
import fs from 'node:fs';
const env = Object.fromEntries(fs.readFileSync(process.env.REEL_ENV || `${process.env.HOME}/Claude/reel-auto/.env`, 'utf8').split('\n').filter(l => l.includes('=')).map(l => [l.slice(0, l.indexOf('=')).trim(), l.slice(l.indexOf('=') + 1).trim()]));
const q = process.argv[2]; const n = +(process.argv[3] || 20);
const r = await fetch('https://google.serper.dev/images', { method: 'POST', headers: { 'X-API-KEY': env.SERPER_API_KEY, 'Content-Type': 'application/json' }, body: JSON.stringify({ q, num: n, tbs: 'isz:l' }) });
if (!r.ok) { console.error('serper', r.status, await r.text()); process.exit(1); }
const j = await r.json();
for (const [i, x] of (j.images || []).entries()) console.log(JSON.stringify({ i, w: x.imageWidth, h: x.imageHeight, dom: x.domain, title: x.title, img: x.imageUrl, page: x.link }));
```


---

# ARQUIVO: `modelo-projeto/scripts/grids.py`

```python
import json,subprocess,os,sys
d=sys.argv[1]; COLS=int(sys.argv[2]) if len(sys.argv)>2 else 6; ROWS=int(sys.argv[3]) if len(sys.argv)>3 else 5
rows=json.load(open(f'{d}/index.json')); per=COLS*ROWS
os.makedirs(f'{d}/grids',exist_ok=True)
for f in os.listdir(f'{d}/grids'): os.remove(f'{d}/grids/{f}')
w,h=subprocess.run(['ffprobe','-v','error','-show_entries','stream=width,height','-of','csv=p=0',f"{d}/f{rows[0]['k']:03d}.jpg"],capture_output=True,text=True).stdout.strip().split(',')
subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'color=c=#101014:s={w}x{h}:d=1','-frames:v','1',f'{d}/pad.jpg'],check=True)
for g in range(0,len(rows),per):
    batch=rows[g:g+per]; gi=g//per
    files=[f"{d}/f{r['k']:03d}.jpg" for r in batch]
    while len(files)%COLS: files.append(f'{d}/pad.jpg')
    lines=[files[i:i+COLS] for i in range(0,len(files),COLS)]
    args=[];
    for f in files: args+=['-i',f]
    fc="";idx=0;ro=[]
    for ri,l in enumerate(lines):
        fc+="".join(f"[{idx+j}:v]" for j in range(COLS))+f"hstack=inputs={COLS}[r{ri}];";idx+=COLS;ro.append(f"[r{ri}]")
    fc+="".join(ro)+f"vstack=inputs={len(ro)}[out]" if len(ro)>1 else f"{ro[0]}copy[out]"
    subprocess.run(['ffmpeg','-v','error','-y']+args+['-filter_complex',fc,'-map','[out]',f'{d}/grids/g{gi}.jpg'],check=True)
    print(f"g{gi}: k{batch[0]['k']}-{batch[-1]['k']} t={batch[0]['t']}-{batch[-1]['t']}s  segs {sorted({r['seg'] for r in batch})}")
```


---

# ARQUIVO: `modelo-projeto/scripts/jcut_check.py`

```python
"""Validacao do J-cut por dados (work/mix-plan.json + work/segs.json + plano):
 - cobertura da voz sem buracos; crossfade inteiro no silencio (nem sobre a ultima palavra nem sobre a primeira);
 - LEAD DE FALA = corte de imagem - inicio da 1a palavra do take seguinte (quadros a 30 fps). Alvo: 5 f.
 - respiro = silencio entre a ultima palavra de um take e a primeira do seguinte (timeline)."""
import json, statistics as st
P=json.load(open('assets/edit-plan.json')); M=json.load(open('work/mix-plan.json')); S=json.load(open('work/segs.json'))
R=P['rate']; F=1/30; LEAD=P.get('jcutLeadFrames',5)*F; V=M['voice']; t=0; T=[]
for i,s in enumerate(P['segments']):
    sd=(s['out']-s['in'])/R; lead=0 if i==0 else min(LEAD,sd-10*F); T.append((t,t-lead)); t+=sd-lead
holes=0; bad=[]; sl=[]; resp=[]
for k in range(len(V)-1):
    a,b=V[k],V[k+1]
    if b['start']>a['start']+a['dur']+1e-3: holes+=1
    if a['in']+a['dur']*R-a['xfade']*R < S[k]['off']-1e-3: bad.append((k,'fim'))
    if b['in']+b['xfade']*R > S[k+1]['on']+1e-3: bad.append((k+1,'inicio'))
    tcut,astart=T[k+1]; on=astart+(S[k+1]['on']-S[k+1]['in'])/R
    sl.append(round((tcut-on)*30,1))
    resp.append((S[k+1]['on']-S[k+1]['in'])/R+(S[k]['aout']-S[k]['off'])/R)
print(f"emendas {len(V)-1} · buracos {holes} · crossfade sobre fala: {bad or 'nenhum'}")
print(f"lead de FALA (quadros): mediana {st.median(sl)} · min {min(sl)} · max {max(sl)} -> {sorted(set(sl))}")
print(f"respiro entre falas: mediana {st.median(resp):.3f}s · min {min(resp):.3f} · max {max(resp):.3f}")
```


---

# ARQUIVO: `modelo-projeto/scripts/make_broll.py`

```python
"""Renderiza os B-rolls a partir das fotos reais em assets/broll-src/ (padrão do formato, sem fal.ai).
POR VÍDEO: editar a lista S (um slot por foto; dur = data-duration da janela no index.html).
Fotos com lado menor < ~900 px em tela cheia: usar fill=1 (foto inteira sobre fundo borrado).
Move APENAS a camera sobre a foto (push-in / pan / crane) — como nada e' gerado por
modelo, texto, logotipo e marca ficam matematicamente identicos ao original: zero
morphing, zero deformacao. Saida em assets/broll/."""
import json, math, subprocess, os
FPS=60
# out: 1080x846 nos splits (a faixa de 44%), 1080x1920 nos cutaways de tela cheia
# ax/ay: ancora do recorte (0=esq/topo, .5=centro, 1=dir/base)
# z0,z1: zoom no inicio/fim · dx,dy: deriva em fracao da janela · fill: fundo borrado
# dim: escurece a foto (produto sobre fundo branco) para a legenda branca SEM contorno ter
#      contraste. A legenda do formato so tem sombra-halo; sobre estudio branco ela some.
S=[
 # reel KAZUO INAMORI — 21 tomadas (scripts/slots.py), fotos recortadas em assets/broll-src/entrega/ (PESQUISAS-BROLL-KAZUO-INAMORI.md)
 # movimento = o do prompt de cada slot. Splits: 1440x1128 (faixa de 44%); tela cheia: 1440x2560
 dict(id="s01-split-capa-monge-pista", src="s01", w=1440,h=1128, ax=0.50,ay=0.50, z0=1.00,z1=1.04, dx= 0.00,dy= 0.00, dim=0.00),  # CAPA: conceito do monge na pista (4:3 inteira: monge e aviao acima da caixa do gancho)
 dict(id="s02-monge-temido", src="entrega/s02-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy=-0.02, dim=0.00),  # monge de costas no templo
 dict(id="s03-split-protocolo-polemico", src="s03", w=1440,h=1128, ax=0.50,ay=0.50, z0=1.03,z1=1.05, dx= 0.04,dy= 0.00, dim=0.00),  # conceito da reuniao (capa B)
 dict(id="s04-split-esconde-numero", src="entrega/s04-16x9", w=1440,h=1128, ax=0.80,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy= 0.00, dim=0.00),  # homem escondendo o papel (callout de digitacao)
 dict(id="s05-kazuo-revelacao", src="entrega/s05-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.06, dx= 0.00,dy=-0.01, dim=0.00),  # REVELACAO: retrato
 dict(id="s06-virou-monge", src="entrega/s06-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.03,z1=1.06, dx= 0.00,dy=-0.05, dim=0.00),  # Inamori de monge (tilt para cima)
 dict(id="s07-jal-sem-salario", src="entrega/s07-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.05,z1=1.05, dx= 0.00,dy= 0.05, dim=0.00),  # pulpito sob o logo JAL (tilt para baixo)
 dict(id="s08-quebra-em-pedacinhos", src="entrega/s08-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.05,z1=1.05, dx= 0.04,dy= 0.00, dim=0.00),  # equipe Kyocera (travelling esq->dir)
 dict(id="s09-briga-pelo-lucro", src="entrega/s09-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy= 0.00, dim=0.00),  # equipe de punho erguido
 dict(id="s10-empresa-inteira", src="entrega/s10-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.04,z1=1.06, dx= 0.00,dy=-0.06, dim=0.00),  # sede da Kyocera (tilt para cima)
 dict(id="s11-conta-de-casa", src="entrega/s11-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy= 0.00, dim=0.00),  # kakeibo + calculadora
 dict(id="s12-painel-do-aviao", src="entrega/s12-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.06, dx= 0.00,dy= 0.00, dim=0.00),  # cockpit 787
 dict(id="s13-pequeno-gafanhoto", src="entrega/s13-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.06, dx= 0.00,dy=-0.01, dim=0.00),  # Mestre Po
 dict(id="s14-orcamento-gastar-tudo", src="entrega/s14-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.05,z1=1.05, dx= 0.00,dy= 0.05, dim=0.00),  # pilha de papeis ACCEPTED (tilt para baixo)
 dict(id="s15-verba-de-dezembro", src="entrega/s15-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy= 0.00, dim=0.00),  # nota em chamas
 dict(id="s16-split-reuniao", src="entrega/s16-16x9", w=1440,h=1128, ax=0.50,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy= 0.00, dim=0.00),  # Inamori entre dois executivos
 dict(id="s17-split-bilhao-de-ienes", src="entrega/s17-16x9", w=1440,h=1128, ax=0.40,ay=0.50, z0=1.05,z1=1.05, dx= 0.05,dy= 0.00, dim=0.00),  # macos de ienes (travelling esq->dir)
 dict(id="s18-aprovado-no-orcamento", src="entrega/s18-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.05,z1=1.05, dx=-0.04,dy= 0.00, dim=0.00),  # diretores da JAL (travelling dir->esq)
 dict(id="s19-climax-rastejando", src="entrega/s19-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.06, dx= 0.00,dy= 0.00, dim=0.00),  # CLIMAX: reverencia na pista
 dict(id="s20-recorde-de-lucro", src="entrega/s20-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.04,z1=1.04, dx= 0.04,dy=-0.02, dim=0.00),  # 787 da JAL decolando
 dict(id="s21-unico-que-liga", src="entrega/s21-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy= 0.00, dim=0.00),  # sozinho com as contas
]
import sys
def _janelas():
    """Duracao de cada tomada = janela do slot (assets/broll-slots.json), casada pelo nome do arquivo."""
    return {x['file'].split('/')[-1][:-4]: x['dur'] for x in json.load(open('assets/broll-slots.json'))['slots']}
W=_janelas()
for _s in S:
    _s['dur']=W[_s['id']]   # janela do slot na timeline; o script soma 0,1 s
ONLY=sys.argv[sys.argv.index('--only')+1].split(',') if '--only' in sys.argv else None
os.makedirs('assets/broll',exist_ok=True)
for s in S:
    if ONLY and not any(s['id'].startswith(o) for o in ONLY): continue
    import glob as _g
    src=_g.glob(f"assets/broll-src/{s['src']}.*")[0]
    W,H=s['w'],s['h']; A=W/H
    sw,sh=[int(x) for x in subprocess.run(['ffprobe','-v','error','-show_entries',
        'stream=width,height','-of','csv=p=0',src],capture_output=True,text=True).stdout.strip().split(',')]
    N=int(math.ceil((s['dur']+0.10)*FPS))
    # 1,5x nos splits; 1,25x em tela cheia. A 1,5x o buffer do zoompan fica 2160x3840 e o
    # ffmpeg leva SIGKILL no Air de 8 GB (aconteceu em 3 tomadas). 1,25x = 1800x3200 passa.
    K=1.5 if H<2000 else 1.15
    UW,UH=int(W*K)//2*2,int(H*K)//2*2
    if s.get('pan'):
        # travelling puro em tela cheia: crop movel numa copia 2x, depois reduz
        x0,x1=s['pan']; K=1.5; CW,CH=int(W*K),int(H*K); ph=s.get('ph',1.0)
        vf=(f"[0:v]scale=-2:{int(CH/ph)}:flags=lanczos,"
            f"crop={CW}:{CH}:x='(iw-ow)*({x0}+({x1}-{x0})*min(1,n/{N-1}))':y='(ih-oh)*{s['ay']}',"
            f"scale={W}:{H}:flags=lanczos,unsharp=5:5:0.55:5:5:0.0"
            +(f",eq=brightness={-s['dim']}:contrast=1.04:saturation=1.06" if s.get('dim') else "")
            +f",format=yuv420p[v]")
        out=f"assets/broll/{s['id']}.mp4"
        subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-i',src,'-filter_complex',vf,
            '-map','[v]','-frames:v',str(N),'-r',str(FPS),'-c:v','libx264','-crf','17',
            '-preset','slow','-pix_fmt','yuv420p','-g','30','-keyint_min','30','-sc_threshold','0',
            '-an','-movflags','+faststart',out],check=True)
        dd=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out],
            capture_output=True,text=True).stdout.strip()
        print(f"  {s['id']:<20} {W}x{H} {N:>4}f  {float(dd):.2f}s  (janela {s['dur']:.2f}s) [travelling]")
        continue
    if s.get('fill'):
        # foto ajustada a largura + fundo borrado dela mesma (preserva a cena inteira).
        # ANTES disso, `far` (fit aspect ratio) recorta a foto para um formato mais ALTO:
        # sem ele uma foto 16:9 ocupa so ~32% da altura do 9:16 e a tarja borrada domina a tela.
        # far e' escolhido por foto pelo maior recorte que nao passa de ~1,8x de ampliacao.
        far=s.get('far')
        if far:
            if sw/sh > far: fw,fh=int(round(sh*far)),sh; fx,fy=int(round((sw-fw)*s.get('ax',.5))),0
            else:           fw,fh=sw,int(round(sw/far)); fx,fy=0,int(round((sh-fh)*s.get('ay',.5)))
            src_chain=f"[0:v]crop={fw}:{fh}:{fx}:{fy},split=2[c0][c1];"
            a,b="[c0]","[c1]"
        else:
            src_chain=""; a,b="[0:v]","[0:v]"
        pre=(src_chain+
             f"{a}scale={UW}:{UH}:force_original_aspect_ratio=increase:flags=lanczos,"
             f"crop={UW}:{UH},gblur=sigma=54,eq=brightness=-0.16:saturation=0.75[bg];"
             f"{b}scale={UW}:-2:flags=lanczos[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2[base];")
    else:
        if sw/sh > A: cw,ch=int(round(sh*A)),sh; cx,cy=int(round((sw-cw)*s['ax'])),0
        else:         cw,ch=sw,int(round(sw/A)); cx,cy=0,int(round((sh-ch)*s['ay']))
        pre=(f"[0:v]crop={cw}:{ch}:{cx}:{cy},scale={UW}:{UH}:flags=lanczos[base];")
    # DOIS PASSOS quando ha fundo borrado: o composite (crop + gblur sigma 54 + overlay) e o
    # zoompan no mesmo processo estouram a RAM do Air de 8 GB (SIGKILL). O passo 1 grava o
    # quadro-base em PNG; o passo 2 so faz a camera em cima dele.
    # DOIS PASSOS SEMPRE (nao so no fill): com foto de 12 MP o crop+scale junto com o zoompan
    # no mesmo processo leva SIGKILL no Air de 8 GB (aconteceu na 02f, 3024x4032). O passo 1
    # grava o quadro-base ja no tamanho final em PNG; o passo 2 so faz a camera em cima dele.
    base_png=f"work/base_{s['id']}.png"
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-filter_complex',
        pre[:-1].replace('[base]','[out]'),'-map','[out]','-frames:v','1',base_png],check=True)
    src=base_png; pre="[0:v]null[base];"
    # easing (skill showreel-interface, lei 1 "antecipacao -> rajada -> assentamento"): ease='out' faz a camera chegar com
    # velocidade logo depois da transicao e ASSENTAR devagar (1-(1-p)^2.2); sem 'ease' = linear. Nasceu no reel ALAN MULALLY.
    p=f"(on/{N-1})" if s.get('ease')!='out' else f"(1-pow(1-on/{N-1},2.2))"
    z=f"({s['z0']}+({s['z1']}-{s['z0']})*{p})"
    xc=f"(iw-iw/zoom)/2"; yc=f"(ih-ih/zoom)/2"
    xe=f"max(0,min(iw-iw/zoom,{xc}+(iw/zoom)*{s['dx']}*({p}-0.5)))"
    ye=f"max(0,min(ih-ih/zoom,{yc}+(ih/zoom)*{s['dy']}*({p}-0.5)))"
    dim=f",eq=brightness={-s['dim']}:contrast=1.04:saturation=1.06" if s.get('dim') else ""
    vf=(pre+f"[base]zoompan=z='{z}':x='{xe}':y='{ye}':d={N}:s={W}x{H}:fps={FPS},"
        f"unsharp=5:5:0.55:5:5:0.0{dim},format=yuv420p[v]")
    out=f"assets/broll/{s['id']}.mp4"
    subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-i',src,'-filter_complex',vf,
        '-map','[v]','-frames:v',str(N),'-r',str(FPS),'-c:v','libx264','-crf','17',
        '-preset','slow','-pix_fmt','yuv420p','-g','30','-keyint_min','30','-sc_threshold','0',
        '-an','-movflags','+faststart',out],check=True)
    d=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out],
        capture_output=True,text=True).stdout.strip()
    print(f"  {s['id']:<20} {W}x{H} {N:>4}f  {float(d):.2f}s  (janela {s['dur']:.2f}s)")
```


---

# ARQUIVO: `modelo-projeto/scripts/mezanino.sh`

```bash
#!/bin/zsh
# Fase 1 — mezanino + voz. NOVO no kit v2 (2026-10-01): junta os comandos que eram digitados a cada reel.
# uso: zsh scripts/mezanino.sh "<bruto.MP4>" <slug>
#   -> assets/<slug>-2560-sdr.mp4   mezanino na resolucao e no fps do bruto, BT.709 limited, GOP 30, sem audio
#   -> work/<slug>-voz-limpa.m4a    audio do bruto, sem reencode (SEM bipe)
#   -> assets/<slug>-voz.m4a        voz do projeto (igual a limpa ate o scripts/bipe.py gravar o bipe)
#   -> work/full-clean.wav          mono 44,1 kHz, para a TRANSCRICAO (nunca leva bipe)
#   -> work/full.wav                mono 44,1 kHz, para o cuts.py (o bipe.py regrava com o bipe)
#   -> work/md5-bruto.txt           MD5 do bruto (conferir de novo no fim: o bruto nunca e alterado)
# RODAR SOZINHO: nunca junto com whisper nem com outro encode (o Air de 8 GB derruba o opendirectoryd).
set -e
BRUTO="$1"; SLUG="$2"
[ -f "$BRUTO" ] && [ -n "$SLUG" ] || { echo 'uso: zsh scripts/mezanino.sh "<bruto>" <slug>'; exit 1; }
cd "${0:A:h}/.."; mkdir -p assets work
md5 -q "$BRUTO" | tee work/md5-bruto.txt
P() { ffprobe -v error -select_streams v:0 -show_entries stream=$1 -of csv=p=0 "$BRUTO"; }
TRC=$(P color_transfer); RNG=$(P color_range); PIX=$(P pix_fmt)
echo "bruto: $(P codec_name) $(P width)x$(P height) @$(P r_frame_rate) · pix_fmt $PIX · range $RNG · transfer $TRC"
COMUM=(-c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -g 30 -keyint_min 30 -sc_threshold 0
       -color_range tv -colorspace bt709 -color_trc bt709 -color_primaries bt709 -an -movflags +faststart)
OUT="assets/$SLUG-2560-sdr.mp4"
if [[ "$TRC" == "arib-std-b67" || "$TRC" == "smpte2084" ]]; then
  # HDR do iPhone (HLG / BT.2020 10 bits). O ffmpeg local nao tem zscale: conversao pelo filtro colorspace.
  echo "-> HDR ($TRC): BT.2020 -> BT.709"
  ffmpeg -v error -stats -y -i "$BRUTO" -vf "colorspace=iall=bt2020:itrc=bt2020-10:all=bt709:format=yuv420p:dither=fsb" "${COMUM[@]}" "$OUT"
elif [[ "$RNG" == "pc" || "$PIX" == yuvj* ]]; then
  # SDR FULL-RANGE (o caso de quase todos os brutos): sem converter full->limited a cor lava.
  echo "-> SDR full-range: full -> limited"
  ffmpeg -v error -stats -y -i "$BRUTO" -vf "scale=in_range=full:out_range=tv,format=yuv420p" "${COMUM[@]}" "$OUT"
else
  echo "-> SDR limited: so reencode com GOP 30"
  ffmpeg -v error -stats -y -i "$BRUTO" -vf "format=yuv420p" "${COMUM[@]}" "$OUT"
fi
ffmpeg -v error -y -i "$BRUTO" -vn -c:a copy "work/$SLUG-voz-limpa.m4a"
cp "work/$SLUG-voz-limpa.m4a" "assets/$SLUG-voz.m4a"
ffmpeg -v error -y -i "work/$SLUG-voz-limpa.m4a" -ac 1 -ar 44100 -c:a pcm_s16le work/full-clean.wav
cp work/full-clean.wav work/full.wav
# Conferencia de cor: media e desvio-padrao de luminancia, bruto x mezanino, em 3 pontos.
# A media bate em ~1/255 e o desvio-padrao fica igual; se o desvio cair, a cor lavou.
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT")
for f in 0.1 0.5 0.9; do
  T=$(python3 -c "print(round($DUR*$f,2))")
  for src in "$BRUTO" "$OUT"; do
    ffmpeg -v error -y -ss $T -i "$src" -frames:v 1 -vf "scale=360:-2:out_range=pc,format=gray" -f rawvideo - | python3 -c "
import sys,numpy as np
a=np.frombuffer(sys.stdin.buffer.read(),dtype=np.uint8); print('  t=$T  media %.2f  desvio %.2f  %s'%(a.mean(),a.std(),'$src'.split('/')[-1]))"
  done
done
echo "mezanino: $OUT · $(ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of csv=p=0 "$OUT") quadros"
echo "no edit-plan.json: \"src\": \"$OUT\", \"voiceSrc\": \"assets/$SLUG-voz.m4a\""
```


---

# ARQUIVO: `modelo-projeto/scripts/mg_cues.mjs`

```javascript
#!/usr/bin/env node
// MOTOR (kit v3). Le compositions/mg.html e devolve os cues de SFX que os componentes registraram com cue()
// (window.__mgCues), SEM navegador: roda o <script> da camada num vm com um gsap de mentira.
// Saida: work/mg-cues-auto.json (lido pelo scripts/mg_sfx.py).   uso: node scripts/mg_cues.mjs
import fs from 'node:fs';
import vm from 'node:vm';
const html = fs.readFileSync('compositions/mg.html', 'utf8');
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
if (!scripts.length) throw new Error('compositions/mg.html sem <script>');
const nada = new Proxy(function () {}, { get: (t, k) => (k === Symbol.toPrimitive ? () => 0 : nada), apply: () => nada });
const gsap = { timeline: () => nada, set: () => nada, to: () => nada, fromTo: () => nada, from: () => nada, registerPlugin: () => {} };
const window = { __timelines: {} };
vm.runInNewContext(scripts.join('\n'), { window, gsap, Math, console, document: nada });
const cues = (window.__mgCues || []).sort((a, b) => a.t - b.t);
fs.mkdirSync('work', { recursive: true });
fs.writeFileSync('work/mg-cues-auto.json', JSON.stringify(cues, null, 0));
const cont = cues.reduce((m, c) => ((m[c.som] = (m[c.som] || 0) + 1), m), {});
console.log(`${cues.length} cues da camada de motion -> work/mg-cues-auto.json`, JSON.stringify(cont));
```


---

# ARQUIVO: `modelo-projeto/scripts/mg_sfx.py`

```python
"""MOTOR (kit v3) + lista EXTRA por video. SFX da camada de motion graphics, com o kit sintetizado da skill
showreel-interface (~/.claude/skills/showreel-interface/scripts/sfx.py). Cada cue marca o PICO do som no quadro do evento.
Os cues vem SOZINHOS dos componentes do compositions/mg.html (cue() -> scripts/mg_cues.mjs -> work/mg-cues-auto.json);
EXTRA abaixo e so para som que nenhum componente dispara (ex.: ding no arco-iris).
Mistura POR CIMA do bed do formato (trilha + SFX fixos, que continuam todos): rodar SEMPRE depois de `bake.py bed`.
uso: node scripts/mg_cues.mjs && python3 scripts/mg_sfx.py"""
import sys, os, json, subprocess
import numpy as np
sys.path.insert(0, os.path.expanduser('~/.claude/skills/showreel-interface/scripts'))
import sfx as K

# POR VIDEO: (t_pico, som, ganho_dB, args). Sons: whoosh swish impacto subdrop clique tique cacaniquel pop riser ding reverso digitar
EXTRA = [
]

SR = K.SR
TOTAL = json.load(open('work/mix-plan.json'))['total']
auto = json.load(open('work/mg-cues-auto.json')) if os.path.exists('work/mg-cues-auto.json') else []
C = [(c['t'], c['som'], c['ganho'], c.get('args', {})) for c in auto] + list(EXTRA)

N = int((TOTAL + 1) * SR)
bus = np.zeros((N, 2))
for t, som, g, args in C:
    s, pico = K.SONS[som](**args)
    if s.ndim == 1: s = np.stack([s, s], 1)
    k = int(round(t * SR)) - pico
    i0, j0 = max(0, k), max(0, -k); m = min(len(s) - j0, N - i0)
    if m > 0: bus[i0:i0 + m] += s[j0:j0 + m] * K.db(g)
bus = bus[:int(TOTAL * SR)]

base = 'work/bed-base.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'assets/bed.m4a', '-ar', str(SR), '-ac', '2', base], check=True)
b = K.le_audio(base)
n = min(len(b), len(bus)); out = b[:n] + bus[:n]
print(f'{len(C)} cues ({len(auto)} automaticos + {len(EXTRA)} extras) · pico do bed+mg {20*np.log10(np.abs(out).max()):.1f} dBFS')
K.grava('work/bed-mg.wav', out)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'work/bed-mg.wav', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', 'assets/bed.m4a'], check=True)
json.dump([dict(t=t, som=s, ganho=g, args=a) for t, s, g, a in C], open('work/mg-cues.json', 'w'), indent=0)
print('assets/bed.m4a = bed do formato + SFX do motion')
```


---

# ARQUIVO: `modelo-projeto/scripts/mkchunks.py`

```python
import json, subprocess, os
segs=json.load(open('work/segs.json'))
# SEM clamp do out no in do take seguinte (reel REED HASTINGS): out = aout + lead (cuts.py) e o video do take
# segura o lead de 5 quadros depois da voz. Em takes CONTIGUOS no source (frase dividida num vale), o clamp
# cortava o lead e a voz perdia os ultimos 14-75 ms da palavra final ("familia", "porta", "Africa").
# O cuts.py ja garante aout <= in do seguinte, entao out <= in_seguinte + lead: nenhum quadro repetido.
# Os chunks de TRANSCRIÇÃO saem do áudio LIMPO (sem o bipe de censura): o bipe está só na
# voz final (assets/ikea-voz.m4a) e em work/full.wav, usado pelo cuts.py para o tail.
SRC='work/full-clean.wav'
meta=[]
for s in segs:
    i=s['i']; off=round(max(0.0,s['in']-0.3),3); end=round(s['out']+0.3,3)
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(off),'-t',str(round(end-off,3)),
        '-i',SRC,'-ac','1','-ar','16000','-c:a','pcm_s16le',
        f'assets/chunks/ch{i:02d}.wav'],check=True)
    meta.append({"i":i,"off":off,"end":end})
json.dump(meta,open('assets/chunks/meta.json','w'),indent=1)
json.dump(segs,open('work/segs.json','w'),indent=1)
print(f"{len(meta)} chunks")
```


---

# ARQUIVO: `modelo-projeto/scripts/mkcut.py`

```python
"""POR VIDEO — reel KAZUO INAMORI. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 1:([8.25],set()),                # "E ele criou um protocolo polemico" | "pra provar que seu funcionario nao pensa como dono porque voce esconde o numero."
 2:([15.495,21.095],set()),       # "Kazuo fundou duas gigantes," | "virou monge budista e com 78 anos assumiu uma companhia aerea falida," | "sem salario."
 16:([60.955],set()),             # "Na sua, so voce ve o numero." | "E olhe la, pequeno gafanhoto."
 17:([64.115],set()),             # "E terceiro," | "proibe a palavra orcamento."
 26:([92.715,95.73],set()),       # "E a virada foi uma reuniao." | "Um diretor ia gastar um bilhao de ienes." | "Ele cortou:"
 34:([116.10],{1}),               # "No primeiro ano, a empresa falida bateu recorde de lucro." | DROP "Seu time gasta..." (falso inicio, refeito em r36)
 37:([126.645],set()),            # "Numero escondido." | "Se voce e o unico que liga pro dinheiro da sua empresa, me segue,"
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel KAZUO INAMORI:
#  r09 "Pela empresa inteira." (falso inicio) -> refeito em r10 "Pela empresa inteira, ninguem briga."
#  r22+r23+r24 "E se voce quiser o protocolo completo / Comenta Monge. / Que eu te mando." -> refeito em r25
#     "Comenta MONGE, que eu te mando o protocolo completo." (a frase do roteiro)
#  r34 parte 2 "Seu time gasta..." (falso inicio) e r35 "Se o time gasta como se o dinheiro..." (falso inicio) -> refeito em r36
DROP={9,22,23,24,35}
out=[];ww={}
for k in sorted(R):
    r=R[k]; pts,dr=SPLIT.get(k,([],set()))
    b=[r['s']]+pts+[r['e']]
    for p in range(len(b)-1):
        s,e=round(b[p],3),round(b[p+1],3)
        n=len(out)
        out.append({"i":n,"s":s,"e":e,"parent":k,"drop":(k in DROP) or (p in dr)})
        # bordas EXTERNAS da regiao: tolerancia de 0,35 s (o whisper poe palavras fracas como "E", "tudo,"
        # alem da borda do silencedetect); divisoes internas: estritas no ponto de corte
        lo=0.35 if p==0 else 0.0; hi=0.35 if p==len(b)-2 else 0.0
        ws=[x for x in W.get(k,[]) if s-lo<=(x[1]+x[2])/2<e+hi]
        if ws: ww[str(n)]=ws
json.dump(out,open('work/regions_cut.json','w'),indent=1)
json.dump(ww,open('work/region-words-cut.json','w'),ensure_ascii=False,indent=1)
for r in out:
    t=''.join(x[0] for x in ww.get(str(r['i']),[])).strip()
    print(f"c{r['i']:02d} (r{r['parent']:02d}) {r['s']:7.2f}-{r['e']:7.2f} {'DROP ' if r['drop'] else '     '}{t}")
```


---

# ARQUIVO: `modelo-projeto/scripts/mkreg.py`

```python
"""Extrai um wav por regiao de fala (+-0.3s) -> work/reg/rNN.wav + work/reg/meta.json"""
import json, subprocess
regs=json.load(open('work/regions.json'))
meta=[]
for r in regs:
    off=round(max(0.0,r['s']-0.3),3); end=round(r['e']+0.3,3)
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(off),'-t',str(round(end-off,3)),
        '-i','work/full-clean.wav','-ac','1','-ar','16000','-c:a','pcm_s16le',
        f"work/reg/r{r['i']:02d}.wav"],check=True)
    meta.append({"i":r['i'],"off":off,"end":end})
json.dump(meta,open('work/reg/meta.json','w'),indent=1)
print(f"{len(meta)} regioes extraidas")
```


---

# ARQUIVO: `modelo-projeto/scripts/norm_broll1.py`

```python
"""Normaliza o broll1.mp4 entregue pelo Fabio para os 3 usos do INTRO SPLIT.
Velocidade NORMAL (os cortes internos dele dao o ritmo) e MUDO.
 01a split  broll1[0.000-3.350]  1440x1128  (fachada + vitrine + inicio do close)
 01c full   broll1[3.350-4.300]  1440x2560  (miolo do close do relogio) -> cobre H01+H02
 01b split  broll1[4.300-5.950]  1440x1128  (fim do close + entrada da boutique)
O 'full' usa CROP 9:16 direto ancorado na coroa (x=190): com FILL o relogio virava uma
faixa pequena entre duas tarjas borradas (conferido lado a lado). O texto do mostrador desta
peca de estoque tem uma linha de letra miuda DEFORMADA: o recorte em x=190 deixa ela fora do quadro.
"""
import subprocess
SRC='assets/broll/broll1.mp4'; MARGEM=0.15
CUTS=[("01a","split",0.000,3.350),("01c","full",3.350,4.300),("01b","split",4.300,5.950)]
COM=['-c:v','libx264','-crf','17','-preset','slow','-pix_fmt','yuv420p',
     '-g','30','-keyint_min','30','-sc_threshold','0','-an','-movflags','+faststart',
     '-colorspace','bt709','-color_trc','bt709','-color_primaries','bt709','-color_range','tv']
for sid,modo,a,b in CUTS:
    dur=round(b-a+MARGEM,3)
    out=f'assets/broll/{sid}.mp4'
    if modo=='split':
        W,H=1440,1128
        vf=(f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,"
            f"crop={W}:{H},fps=60,setsar=1,format=yuv420p")
    else:
        W,H=1440,2560
        vf=(f"[0:v]crop=405:720:190:0,scale={W}:{H}:flags=lanczos,"
            f"unsharp=5:5:0.6:5:5:0,fps=60,setsar=1,format=yuv420p[v]")
    cmd=['ffmpeg','-v','error','-y','-ss',f'{a:.3f}','-t',f'{dur:.3f}','-i',SRC]
    cmd += (['-filter_complex',vf,'-map','[v]'] if modo=='full' else ['-vf',vf])
    subprocess.run(cmd+COM+[out],check=True)
    d=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out],
                     capture_output=True,text=True).stdout.strip()
    n=subprocess.run(['ffprobe','-v','error','-select_streams','v','-count_frames',
                      '-show_entries','stream=nb_read_frames,width,height','-of','csv=p=0',out],
                     capture_output=True,text=True).stdout.strip()
    print(f"  {sid}.mp4  {modo:<5} {n}  {float(d):.2f}s  (janela {b-a:.2f}s)")
```


---

# ARQUIVO: `modelo-projeto/scripts/pesquisa_md.py`

````python
"""POR VIDEO — reel KAZUO INAMORI. Gera PESQUISAS-BROLL-KAZUO-INAMORI.md a partir de assets/broll-slots.json (scripts/slots.py),
work/pesq/candidates.json (pesquisa) e work/pesq/slot-picks.json (foto escolhida por slot, scripts/entrega.py).
Grava tambem img/link/fonte/prompt de cada slot em assets/broll-slots.json. Uso: python3 scripts/pesquisa_md.py"""
import json
S=json.load(open('assets/broll-slots.json'))['slots']
C={c['id']:c for c in json.load(open('work/pesq/candidates.json'))}
PK=json.load(open('work/pesq/slot-picks.json'))
ALT={k:v.get('alt') for k,v in json.load(open('work/pesq/picks.json')).items()}
LOCK=("Os textos, logotipos e elementos de marca da imagem (o logo JAL e o grou vermelho, o letreiro KYOCERA, a caligrafia 敬天愛人, "
"as notas de 10.000 ienes, os números do caderno e da calculadora, as telas do painel do avião, a palavra ACCEPTED) precisam ficar PARADOS, "
"legíveis e nítidos exatamente como na imagem de referência: sem morphing, sem deformar, sem redesenhar, sem inventar letras novas e sem mudar cor. "
"Rostos e mãos não podem mudar de feição, de forma nem de identidade. Nada na cena se move por conta própria — ninguém anda, fala, gesticula ou pisca, "
"nenhum objeto desliza, nenhuma chama ou luz pisca, nenhuma pessoa ou objeto novo aparece. O ÚNICO movimento é o da câmera. Movimento constante e suave, "
"sem aceleração, sem corte, sem tremor.")
DESC={k:C[PK[k]]['desc'] for k in PK}
CAM={
"s01":"Aproximação lenta (~4%) em direção ao monge de costas no centro da pista.",
"s02":"Aproximação lenta (~5%) seguindo o monge de costas, com leve deriva para cima (~2% da altura).",
"s03":"Travelling lateral lento da esquerda para a direita (~4% da largura) com leve aproximação em direção à mão sobre a mesa.",
"s04":"Aproximação lenta (~5%) em direção ao papel que o homem segura contra o peito.",
"s05":"Aproximação muito lenta (~6%) centrada no rosto.",
"s06":"Tilt lento de baixo para cima (~5% da altura), do rosário nas mãos até o rosto, com leve aproximação (~3%).",
"s07":"Tilt lento de cima para baixo (~5% da altura), do logotipo no avião até o homem no púlpito.",
"s08":"Travelling lateral lento da esquerda para a direita (~4% da largura) ao longo do grupo.",
"s09":"Aproximação lenta (~5%) em direção ao centro do grupo.",
"s10":"Tilt lento de baixo para cima (~6% da altura) ao longo da fachada do prédio.",
"s11":"Aproximação lenta (~5%) em direção ao visor da calculadora.",
"s12":"Aproximação lenta (~6%) em direção às telas do painel de instrumentos.",
"s13":"Aproximação muito lenta (~6%) em direção aos olhos do Mestre Po.",
"s14":"Tilt lento de cima para baixo (~5% da altura) ao longo da pilha de papéis até a bandeja.",
"s15":"Aproximação lenta (~5%) em direção à nota em chamas.",
"s16":"Aproximação lenta (~5%) em direção ao homem do centro.",
"s17":"Travelling lateral lento da esquerda para a direita (~5% da largura) sobre os maços de notas.",
"s18":"Travelling lateral lento da direita para a esquerda (~4% da largura) ao longo da fila de diretores.",
"s19":"Aproximação muito lenta (~6%) em direção aos dois funcionários curvados.",
"s20":"Travelling lento acompanhando o avião para a direita e para cima (~4% da largura, ~2% da altura).",
"s21":"Aproximação lenta (~5%) em direção à pessoa sozinha na mesa.",
}
NOTA={
"s01":"CAPA do reel (quadro 0, atrás da caixa laranja do gancho) e PRÉ-REVELAÇÃO. Gerada a seu pedido (fal.ai, nano-banana-pro, 4:3): bateu com a descrição de primeira (monge de costas, avião sem logotipo, luz vermelha no alto, preto/vermelho/âmbar). O split sai da foto 4:3 inteira para o monge e o avião ficarem acima da caixa do gancho.",
"s02":"PRÉ-REVELAÇÃO e cobre a olhada do gancho (1,72–2,24 s). Foto de matéria da revista Chichi (templo zen japonês), 1920x1280: o recorte vertical fica com 720 px de largura — é o slot de menor resolução. Alternativa nítida (3000x4498, Pexels): `d02f_2`, monge de túnica laranja num corredor de templo (não é zen japonês).",
"s03":"PRÉ-REVELAÇÃO. É a sua alternativa de capa (ação × curiosidade), gerada a pedido — fica aqui e disponível como capa B do teste (`work/conceito/c2-reuniao-nb.jpg`). Nenhum texto legível nas folhas.",
"s04":"PRÉ-REVELAÇÃO: callout de digitação \"VOCÊ ESCONDE O NÚMERO.\" + drum-fill sobre esta tomada (9,90 s). Pexels, licença livre.",
"s05":"REVELAÇÃO: entra em 11,25 s, 2 quadros depois de \"Kazuo\" (11,18 s). Retrato publicado pelo jornal Minami-Nippon Shimbun (373news.com), licença não informada — uso editorial.",
"s06":"Foto do jornal Sankei (1997, ordenação no templo Enpuku-ji), 1084x1701 — uso editorial. Alternativa em preto e branco de corpo inteiro: `b04a_0`.",
"s07":"Callout \"SEM SALÁRIO.\" nesta tomada (18,6 s). Foto do Sankei, 1200x1552 — uso editorial. O logo JAL ocupa o terço de cima: `capLowSegs` para a legenda não cobrir.",
"s08":"Foto institucional da Kyocera (kyocera.co.jp). Horizontal: entra inteira (recorte lateral leve) sobre o próprio fundo borrado.",
"s09":"Callout \"BRIGA PELO LUCRO.\" nesta tomada. Evento na Biblioteca Inamori (industry-co-creation.com), 1920x1080, sobre fundo borrado.",
"s10":"Sede da Kyocera em Kyoto (bigcompany.jp), vertical nativa.",
"s11":"Foto de divulgação da Casio (calculadora + kakeibo), 1600x1200, sobre fundo borrado. As alternativas com dinheiro eram em dólar.",
"s12":"Callout \"PILOTAR AVIÃO SEM OLHAR O PAINEL.\" nesta tomada. Foto de usuário (reddit), vertical 2268x4032 — uso editorial. É um 787; a JAL opera o modelo, mas a foto não identifica a companhia.",
"s13":"Mesma foto de divulgação da série Kung Fu (IMDb) usada no reel Sun Tzu — uso editorial. Alternativa: pôster da série (`b11b_12`).",
"s14":"Pexels, licença livre. A palavra ACCEPTED está em inglês.",
"s15":"Pexels, licença livre. É uma nota de dólar (não achei iene queimando em resolução útil). Logo depois o apresentador volta para o bipe (61,61–62,15 s).",
"s16":"Split com a transição de arrastar. Foto da Diamond Online (coletiva da JAL), 4096x2152 — uso editorial.",
"s17":"Split com a transição de arrastar. Foto de site japonês de numismática (kosen-kantei.jp), 5184x3456 — licença não informada.",
"s18":"Foto do JBpress (coletiva da JAL, 2010), 1600x1066, sobre fundo borrado — uso editorial. Riser do clímax começa em 79,28 s, já no apresentador.",
"s19":"CLÍMAX (impact-hit em 82,28 s + callout \"RASTEJANDO NO CHÃO.\"). Foto do site oficial da JAL (trico.jal.com), 1920x1280, sobre fundo borrado. Alternativa mais literal: carregadores agachados na esteira (`c18e_3`).",
"s20":"Unsplash, licença livre. Não achei a foto da relistagem na bolsa (2012) em resolução útil.",
"s21":"Pexels, licença livre. Cobre as duas olhadas do CTA (94,71–95,04 e 95,65–96,11 s); o apresentador volta em 96,15 s para \"me segue, porque você é demais\".",
}
L=[]
L.append("# PESQUISAS-BROLL-KAZUO-INAMORI.md\n")
L.append("Pesquisa de B-roll do reel **Kazuo Inamori** — formato viral, projeto HyperFrames `reel-auto/kazuo-inamori`.\n")
L.append("**21 tomadas em 4 slots.** Prioridade aplicada: (1) **sites oficiais** — Kyocera (`s08`) e Japan Airlines (`s19`); as salas de imprensa não têm o Inamori "
"de monge nem as coletivas de 2010 em tamanho útil; (2) **Google Imagens em tamanho grande**: imprensa japonesa (Sankei, Diamond, JBpress, Minami-Nippon) para o "
"retrato, o monge e a JAL; Pexels/Unsplash (licença livre) para as falas genéricas (esconder o número, orçamento, verba torrada, dono sozinho, decolagem). "
"Nada com marca d'água de banco de imagens. **Duas imagens são conceito gerado por IA a seu pedido** (`s01`, a capa, e `s03`, a alternativa de capa). "
"Todas as outras são fotos reais.\n")
L.append("As fotos originais estão em `assets/broll-src/<slot>.jpg`. **Já recortadas no formato de entrega**: `assets/broll-src/entrega/<slot>-9x16.jpg` "
"(tela cheia) e `<slot>-16x9.jpg` (split). As candidatas escolhidas e as alternativas: `work/pesq/cand/` (metadados em `work/pesq/candidates.json`, escolha e alternativa por slot em "
"`work/pesq/picks.json`); as 331 fotos baixadas na busca estão em `work/pesq/raw/` (índice `work/pesq/g_index.json`, folhas por trecho em `work/pesq/sheets2/`). "
"Mapa técnico: `assets/broll-slots.json`. Folha das escolhidas: `work/pesq/sheet_entrega.jpg`.\n")
L.append("**Geração:** depois do \"pode gerar as brolls\", as tomadas são geradas **localmente** por `scripts/make_broll.py`, que executa exatamente o "
"movimento de câmera de cada prompt sobre a foto (nada de IA generativa na animação): texto, logotipo e rosto ficam idênticos ao original. Os prompts abaixo "
"servem também para Kling/Seedance/Veo, se preferir gerar lá.\n")
L.append("## Regra que vale para TODOS os prompts\n\nO modelo recebe a imagem como referência, então **o prompt não redescreve a imagem**: só o movimento de câmera, e trava os textos e marcas:\n\n> "+LOCK+"\n")
L.append("## Por que as durações importam\n\nTempos a 1,1x. Vários cutaways cobrem um **desvio de olhar** medido no bruto. "
"**Se a tomada encurtar, o desvio reaparece**: a duração pedida é mínima. Gerar **5 s** em todas (a maior janela é 4,02 s); o corte é no quadro exato.\n")
L.append("## Como entregar (se for gerar fora)\n\n- **Split-screen** (`s01`, `s03`, `s04`, `s16`, `s17`): **16:9 horizontal**. No reel aparece a faixa central de ~72% da largura (topo de 44% da tela).\n"
"- **Tela cheia** (os demais): **9:16 vertical**.\n- Nome final de cada tomada na tabela do fim, em `reel-auto/kazuo-inamori/assets/broll/`. O áudio dos vídeos é zerado (só voz tratada + trilha + SFX).\n")
L.append("## Pontos de atenção (decisões e limitações)\n\n"
"- **Nome só depois do áudio:** \"Kazuo\" é dito em 11,18 s. `s01`–`s04` não mostram o Inamori, a Kyocera, a KDDI nem a JAL (o avião da capa não tem logotipo); a revelação (`s05`) entra em 11,25 s.\n"
"- **A capa é o split** (`s01`, quadro 0) com a sua imagem do monge na pista. A alternativa (mão batendo na mesa) está no `s03` e em `work/conceito/c2-reuniao-nb.jpg` para o teste de capa.\n"
"- **Fotos pequenas:** `s02` (720 px de largura no recorte), `s06` (956 px) e `s07` (873 px) são ampliadas para 1440 px — as únicas fotos reais do monge e da posse na JAL que achei em vertical. Seis fotos horizontais entram inteiras sobre fundo borrado (`s08`, `s09`, `s11`, `s18`, `s19`, `s20`).\n"
"- **Não achei em resolução útil:** a relistagem da JAL na bolsa em 2012 (`s20` usa a decolagem), o Inamori pedindo esmola de monge na rua (só miniaturas), iene queimando (`s15` é dólar).\n"
"- **Slots com texto/logo (maior risco se gerar com IA):** `s07`, `s18`, `s19`, `s20` (JAL), `s08`, `s10` (Kyocera), `s09` (caligrafia), `s11`, `s12` (números e telas), `s14` (ACCEPTED), `s17` (cédulas).\n"
"- **Licenças:** Pexels/Unsplash = licença livre (`s04`, `s14`, `s15`, `s20`, `s21`); Kyocera e JAL = material institucional (`s08`, `s19`); imprensa e sites japoneses, IMDb e reddit = "
"licença não informada, uso editorial (`s02`, `s05`, `s06`, `s07`, `s09`, `s10`, `s11`, `s12`, `s13`, `s16`, `s17`, `s18`); `s01`/`s03` gerados a pedido.\n"
"- A pesquisa foi feita com User-Agent genérico de Chrome, sem nenhum dado seu nas requisições.\n\n---\n")
SLOTS=[("SLOT 1 — INTRO EM SPLIT-SCREEN (PRÉ-REVELAÇÃO)","0,00 → 11,25 s. Capa em split no quadro 0 (`s01`), cutaway cobrindo a olhada do gancho (`s02`), e o split voltando com a transição de arrastar (`s03`, `s04` com o callout de digitação). **Nada de Inamori, Kyocera ou JAL** antes de 11,18 s, quando o áudio diz \"Kazuo\".",["s01","s02","s03","s04"]),
("SLOT 2 — CUTAWAYS DURANTE O CORPO DO VÍDEO","11,25 → 61,40 s. Revelação, o monge, a JAL e os três passos do protocolo. Entre os cutaways o apresentador aparece em tela cheia olhando para a câmera (inclusive no bipe, 61,61–62,15 s, e no \"Comenta MONGE\").",["s05","s06","s07","s08","s09","s10","s11","s12","s13","s14","s15"]),
("SLOT 3 — SEGUNDO SPLIT-SCREEN (A VIRADA: A REUNIÃO)","67,30 → 78,28 s. Split com a transição de arrastar (67,30–71,89), \"Ele cortou: pra você não confio nem um centavo\" no seu rosto, e os diretores (`s18`). \"Ele explodiu: de quem é esse dinheiro? Da empresa? Não.\" fica no seu rosto, com o riser subindo.",["s16","s17","s18"]),
("SLOT 4 — CLÍMAX EMOCIONAL","82,28 → 96,15 s. \"É o lucro que o funcionário tirou rastejando no chão\" (riser 3 s antes + impact-hit em 82,28 s), o recorde de lucro e, depois de \"Número escondido.\" no seu rosto, o dono sozinho com as contas. O CTA fecha no seu rosto.",["s19","s20","s21"])]
Sd={s['id']:s for s in S}
fmt=lambda x: f"{x:.2f}".replace('.',',')
for tit,desc,ids in SLOTS:
    L.append(f"## {tit}\n\n{desc}\n")
    for sid in ids:
        s=Sd[sid]; c=C[PK[sid]]; tag='16x9' if s['mode']=='split' else '9x16'
        enq="Split-screen (faixa de 44% do topo) — entregar em **16:9 horizontal**." if s['mode']=='split' else "Tela cheia — entregar em **9:16 vertical**."
        L.append(f"### `{sid}` — {fmt(s['t0'])} → {fmt(s['t1'])} s\n")
        L.append("| | |\n|---|---|")
        L.append(f"| **Trecho da fala** | \"{s['fala']}\" |")
        L.append(f"| **Tipo de enquadramento** | {enq} |")
        L.append(f"| **Imagem recomendada** | {s['tema']} — {DESC[sid]} |")
        L.append(f"| **Arquivo para subir** | `assets/broll-src/entrega/{sid}-{tag}.jpg` (original: `assets/broll-src/{sid}.jpg`, {c['w']}x{c['h']} px) |")
        L.append(f"| **Link da imagem** | {c['img']} |")
        L.append(f"| **Fonte** | {c['dom']} — {c['fonte']} — {c['page']} ({c['licenca']}) |")
        L.append(f"| **Duração necessária** | **{fmt(s['dur'])} s** (gerar 5 s) |")
        L.append(f"| **Nome do arquivo final** | `{s['file'].split('/')[-1]}` |")
        L.append(f"| **Cobre desvio de olhar** | {s['cobre']} |")
        L.append(f"| **Alternativa** | `{ALT.get(sid)}` — {C[ALT[sid]]['desc']} ({C[ALT[sid]]['dom']}, {C[ALT[sid]]['w']}x{C[ALT[sid]]['h']}) — `work/pesq/cand/{ALT[sid]}.jpg` |" if ALT.get(sid) else "| **Alternativa** | — |")
        L.append(f"| **Atenção** | {NOTA[sid]} |\n")
        L.append("**Prompt de animação (Kling / Seedance / Veo):**\n\n```\n"+CAM[sid]+" "+LOCK+"\n```\n")
        s.update(img=c['img'],link=c['page'],fonte=c['dom'],prompt=CAM[sid]+" "+LOCK,foto=PK[sid])
L.append("---\n\n## Resumo — arquivos que eu preciso receber em `assets/broll/`\n\n| Slot | Janela (s) | Duração | Formato | Nome do arquivo |\n|---|---|---|---|---|")
for s in S:
    L.append(f"| `{s['id']}` | {fmt(s['t0'])}–{fmt(s['t1'])} | {fmt(s['dur'])} s | {'16:9 (split)' if s['mode']=='split' else '9:16'} | `{s['file'].split('/')[-1]}` |")
open('PESQUISAS-BROLL-KAZUO-INAMORI.md','w').write('\n'.join(L)+'\n')
d=json.load(open('assets/broll-slots.json')); d['slots']=S; json.dump(d,open('assets/broll-slots.json','w'),ensure_ascii=False,indent=1)
print(f"PESQUISAS-BROLL-KAZUO-INAMORI.md: {len(S)} tomadas")
````


---

# ARQUIVO: `modelo-projeto/scripts/plan_segments.py`

```python
"""Copia work/segs.json (scripts/cuts.py) para `segments` do assets/edit-plan.json (in, out, aout, label, chunk).
Preserva campos extras ja postos a mao num segmento (videoTail etc.) quando o label bate."""
import json
P=json.load(open('assets/edit-plan.json')); S=json.load(open('work/segs.json'))
old={s['label']:s for s in P.get('segments',[])}
P['segments']=[{**{k:v for k,v in old.get(s['label'],{}).items() if k not in ('in','out','aout','label','chunk')},
                "in":s['in'],"out":s['out'],"label":s['label'],"chunk":s['i'],"aout":s['aout']} for s in S]
json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1)
print(len(P['segments']),'segments')
```


---

# ARQUIVO: `modelo-projeto/scripts/rebuild_chunk.py`

```python
"""Reconstroi ch<NN>-words.json a partir do passe por REGIAO (work/region-words-cut.json)
quando o passe por chunk colapsa/alucina. Uso: rebuild_chunk.py ch:regiao_cut[+regiao_cut...] ..."""
import json, sys
M={m['i']:m for m in json.load(open('assets/chunks/meta.json'))}
RW=json.load(open('work/region-words-cut.json'))
for spec in sys.argv[1:]:
    ci,rc=spec.split(':'); ci=int(ci); off=M[ci]['off']; ws=[w for r in rc.split('+') for w in RW[r]]
    tr=[{"text":" "+w[0].strip(),"offsets":{"from":int(round((w[1]-off)*1000)),"to":int(round((w[2]-off)*1000))}} for w in ws]
    json.dump({"transcription":tr},open(f'assets/chunks/ch{ci:02d}-words.json','w'),ensure_ascii=False)
    print(f"ch{ci:02d} <- c{rc}:",' '.join(f"{t['text'].strip()}[{t['offsets']['from']}-{t['offsets']['to']}]" for t in tr))
```


---

# ARQUIVO: `modelo-projeto/scripts/regions.py`

```python
"""silencedetect -> regioes de fala -> work/regions.json"""
import subprocess, re, json, sys
SRC='work/full.wav'
NOISE=sys.argv[1] if len(sys.argv)>1 else '-35dB'
D=sys.argv[2] if len(sys.argv)>2 else '0.35'
out=subprocess.run(['ffmpeg','-v','info','-i',SRC,'-af',f'silencedetect=noise={NOISE}:d={D}','-f','null','-'],
                   capture_output=True,text=True).stderr
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',SRC],
                         capture_output=True,text=True).stdout.strip())
sil=[]
cur=None
for m in re.finditer(r'silence_(start|end): ([\d.\-]+)', out):
    k,v=m.group(1),float(m.group(2))
    if k=='start': cur=v
    elif cur is not None: sil.append((cur,v)); cur=None
if cur is not None: sil.append((cur,dur))
regs=[];prev=0.0
for s,e in sil:
    if s-prev>0.25: regs.append((prev,s))
    prev=e
if dur-prev>0.25: regs.append((prev,dur))
res=[{"i":i,"s":round(s,3),"e":round(e,3),"d":round(e-s,3)} for i,(s,e) in enumerate(regs)]
json.dump(res,open('work/regions.json','w'),indent=1)
for r in res: print(f"r{r['i']:02d}  {r['s']:7.2f} -> {r['e']:7.2f}  ({r['d']:.2f}s)")
print(f"\n{len(res)} regioes de fala")
```


---

# ARQUIVO: `modelo-projeto/scripts/regwords.py`

```python
"""Junta as transcricoes por regiao -> work/region-words.json (tempos ABSOLUTOS do source)
e imprime o texto de cada regiao para a selecao de takes."""
import json, glob, os
meta={m['i']:m for m in json.load(open('work/reg/meta.json'))}
R={r['i']:r for r in json.load(open('work/regions.json'))}
out={}
for p in sorted(glob.glob('work/reg/r*.json')):
    i=int(os.path.basename(p)[1:3]); off=meta[i]['off']
    d=json.load(open(p))
    ws=[[e['text'], round(off+e['offsets']['from']/1000,3), round(off+e['offsets']['to']/1000,3)]
        for e in d['transcription'] if e['text'].strip() and not e['text'].strip().startswith('[')]
    if not ws: continue
    out[i]=ws
json.dump({str(k):v for k,v in sorted(out.items())},open('work/region-words.json','w'),ensure_ascii=False,indent=1)
for i in sorted(out):
    txt=''.join(w[0] for w in out[i]).strip()
    print(f"r{i:02d} [{R[i]['s']:6.2f} -> {R[i]['e']:6.2f}]  {txt}")
print(f"\n{len(out)} regioes transcritas")
```


---

# ARQUIVO: `modelo-projeto/scripts/remap_tl.py`

```python
"""Converte tempos de timeline de uma versao antiga do plano para a atual, passando pelo tempo de SOURCE
(o mesmo quadro do bruto). Uso como modulo: from remap_tl import remap; remap(t). Planos: $REMAP_OLD (padrao work/v1/edit-plan.json) -> assets/edit-plan.json"""
import json, os
def _segs(P):
    R=P['rate']; F=1/30; LEAD=P.get('jcutLeadFrames',5)*F; t=0; out=[]
    for i,s in enumerate(P['segments']):
        sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(LEAD,sd-10*F); d=round(sd-lead,3)
        out.append(dict(t0=round(t,3),t1=round(t+d,3),m0=round(s['in']+lead*R,3),R=R)); t=round(t+d,3)
    return out
OLD=_segs(json.load(open(os.environ.get('REMAP_OLD','work/v1/edit-plan.json')))); NEW=_segs(json.load(open('assets/edit-plan.json')))
def src_of(t,S=OLD):
    for s in S:
        if s['t0']-1e-6<=t<s['t1']+1e-6: return s['m0']+(t-s['t0'])*s['R']
    s=S[-1]; return s['m0']+(t-s['t0'])*s['R']
def tl_of(src,S=NEW):
    best=None
    for s in S:
        m1=s['m0']+(s['t1']-s['t0'])*s['R']
        if s['m0']-1e-6<=src<=m1+1e-6: return round(s['t0']+(src-s['m0'])/s['R'],3)
        d=min(abs(src-s['m0']),abs(src-m1))
        if best is None or d<best[0]: best=(d,s)
    s=best[1]; return round(min(max(s['t0']+(src-s['m0'])/s['R'],s['t0']),s['t1']),3)
def remap(t): return tl_of(src_of(t))
if __name__=='__main__':
    import sys
    for x in sys.argv[1:]: print(x,'->',remap(float(x)))
```


---

# ARQUIVO: `modelo-projeto/scripts/ritmo.py`

```python
"""Ritmo visual: nenhum trecho pode passar de MAX s sem algo mudar na tela.
Conta como evento: entrada/saída de B-roll, corte do apresentador com troca de zoom,
callout, light-leak e transição de split. Lê o index.html gerado."""
import re, sys, json, os
MAX=float(sys.argv[1]) if len(sys.argv)>1 else 4.0
h=open('index.html').read()
T=float(re.search(r'id="root"[^>]*data-duration="([\d.]+)"',h)[1])
attr=lambda tag,k: (re.search(k+r'="([^"]*)"',tag) or [None,None])[1]
ev=[(0.0,'inicio')]
full=[(g['t0'],g['t1']) for g in json.load(open('work/broll-groups.json')) if g['mode']!='split']
hidden=lambda x: any(a-0.01<=x<b-0.01 for a,b in full)
prev=None
# corte com zoom: tl.set("#presenter-zoom", { scale: X }, T)
for m in re.finditer(r'tl\.set\("#presenter-zoom", \{ scale: ([\d.]+) \}, ([\d.]+)\)',h):
    sc=float(m[1]); t=float(m[2])
    if (prev is None or sc!=prev) and not hidden(t): ev.append((t,f'zoom {sc}'))
    prev=sc
# entradas/saidas de B-roll pelas cenas (com bakedBroll as cenas de tela cheia sao uma faixa so)
for g in json.load(open('work/broll-groups.json')):
    ev+= [(g['t0'],'broll in '+g['file'].split('/')[-1][:22]),(g['t1'],'broll out')]
full=[(g['t0'],g['t1']) for g in json.load(open('work/broll-groups.json')) if g['mode']!='split']
# cortes DENTRO de uma cena concatenada (várias tomadas num arquivo só)
if os.path.exists('work/broll-groups.json'):
    for g in json.load(open('work/broll-groups.json')):
        t=g['t0']
        for sh in g['shots'][:-1]:
            t+=sh['dur']; ev.append((round(t,2),'tomada '+sh['file'].split('/')[-1][:18]))
for tag in re.findall(r'<div[^>]*class="clip cap-big"[^>]*>',h): ev.append((float(attr(tag,'data-start')),'callout'))
for x in json.load(open('work/leaks.json'))['leaks']: ev.append((x['start'],'leak'))
ev=sorted(set((round(t,2),n) for t,n in ev if t<=T)); ev.append((T,'fim'))
gaps=[(a[0],b[0],b[0]-a[0],a[1]) for a,b in zip(ev,ev[1:]) if b[0]-a[0]>MAX]
print(f"duração {T:.2f}s · {len(ev)} eventos · maior intervalo {max(b[0]-a[0] for a,b in zip(ev,ev[1:])):.2f}s")
for a,b,d,n in gaps: print(f"  SEM EVENTO {a:7.2f} -> {b:7.2f} ({d:.2f}s) depois de: {n}")
print("OK" if not gaps else f"{len(gaps)} trechos acima de {MAX}s")
```


---

# ARQUIVO: `modelo-projeto/scripts/se_splice.py`

```python
"""POR VIDEO — reel DAVID MARQUET. Recupera o "Se voce" de "Se voce e a unica pessoa que pensa na sua empresa".
O take valido (r30) diz "(ce) e a unica..." com o "voce" quase engolido (whisper ouve so "E a unica"); o
"Se voce" claro so existe no tropeco r29 ("Se voce...", com o "e" final arrastado).
Envelope 10 ms de r29: /s/ 108,61-108,69 · "e" 108,70-108,76 · "vo" 108,78-108,84 · /s/ 108,85-108,94 · "e" 108,95-109,12.
Copia "Se voce" (108,59-109,06: corta o "e" arrastado, fade de 20 ms) e encosta no "e a unica" de r30 (109,49).
Antes, SILENCIA 108,55-109,49 na voz (o resto do tropeco nao pode vazar: o take CTA-UNICA agora comeca em 108,87).
O trecho fica sob o B-roll s18 (sem lip-sync a respeitar).
Entrada: work/marquet-voz-limpa.m4a (audio do bruto) -> work/voz-limpa-se.wav (48k estereo, base do bipe.py)
e work/full-clean.wav (mono 44,1k, transcricao). Depois: bipe.py -> assets/marquet-voz.m4a + work/full.wav."""
import numpy as np, subprocess, wave
A,B=108.59,109.06     # "Se voce" no tropeco r29
DST_END=109.49        # onset do "e a unica" de r30
MUTE=(108.55,109.49)  # resto do tropeco, silenciado
subprocess.run(['ffmpeg','-v','error','-y','-i','work/marquet-voz-limpa.m4a','-ar','48000','-ac','2','-c:a','pcm_s16le','work/_limpa48.wav'],check=True)
w=wave.open('work/_limpa48.wav'); sr=w.getframerate(); ch=w.getnchannels()
x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32).reshape(-1,ch)/32768
seg=x[int(A*sr):int(B*sr)].copy(); n=len(seg)
fi,fo=int(0.005*sr),int(0.020*sr)
env=np.ones(n); env[:fi]=np.linspace(0,1,fi); env[-fo:]=np.linspace(1,0,fo); seg*=env[:,None]
m0,m1=int(MUTE[0]*sr),int(MUTE[1]*sr); g=int(0.005*sr)
x[m0:m0+g]*=np.linspace(1,0,g)[:,None]; x[m0+g:m1]=0
d1=int(DST_END*sr); d0=d1-n; x[d0:d1]+=seg
y=(np.clip(x,-1,1)*32767).astype(np.int16)
o=wave.open('work/voz-limpa-se.wav','wb'); o.setnchannels(ch); o.setsampwidth(2); o.setframerate(sr); o.writeframes(y.tobytes()); o.close()
subprocess.run(['ffmpeg','-v','error','-y','-i','work/voz-limpa-se.wav','-ac','1','-ar','44100','-c:a','pcm_s16le','work/full-clean.wav'],check=True)
print(f'"Se voce" {A}-{B}s colado em {d0/sr:.3f}-{DST_END}s (tropeco silenciado {MUTE[0]}-{MUTE[1]}) -> work/voz-limpa-se.wav + work/full-clean.wav')
```


---

# ARQUIVO: `modelo-projeto/scripts/size_sweep.py`

```python
"""Escolhe o --size do render em partes (scripts/render-chunks.mjs). NOVO no kit v2 (2026-10-01): era uma conta refeita a mao a cada reel.
O render aborta no gate de cobertura quando uma parte fica com poucos quadros de um clipe ("captured 2 of expected 3 frames").
Para cada tamanho candidato, mede a MENOR sobra de <video> dentro de qualquer pedaco (parte dividida em --split) e lista os melhores.
Regras ja pagas:
 - varrer SO os <video> (as legendas sempre ficam fatiadas e nao passam pelo gate);
 - a varredura tem que incluir os pedacos do --split (354 era bom sem split e deixava 8 quadros com --split 3);
 - sobra minima >= ~15 quadros; quanto maior, melhor;
 - a 60 fps nao passar de ~460 quadros por parte (o Chrome travou em ~530 e ~570 em sessoes longas); nao desligar o gate.
Uso: python3 scripts/size_sweep.py [--fps 60] [--split 3] [--min 300] [--max 460] [--top 8]"""
import re, sys, math
def arg(k, d): return type(d)(sys.argv[sys.argv.index(k)+1]) if k in sys.argv else d
FPS=arg('--fps',60); SPLIT=arg('--split',3); LO=arg('--min',300); HI=arg('--max',460); TOP=arg('--top',8)
h=open('index.html').read()
TOTAL=float(re.search(r'id="root"[^>]*data-duration="([\d.]+)"',h)[1]); TF=math.ceil(TOTAL*FPS-1e-6)
at=lambda t,k: float(re.search(r'(?<![\w-])'+k+r'="([^"]*)"',t)[1])
V=[(at(t,'data-start')*FPS,(at(t,'data-start')+at(t,'data-duration'))*FPS,re.search(r' id="([^"]*)"',t)[1])
   for t in re.findall(r'<video\b[^>]*data-start="[^"]*"[^>]*>',h)]
def pedacos(S):
    out=[]
    for k0 in range(0,TF,S):
        k1=min(TF,k0+S); step=math.ceil((k1-k0)/SPLIT)
        out+=[(k0+j*step,min(k1,k0+(j+1)*step)) for j in range(SPLIT) if k0+j*step<k1]
    return out
def pior(S):
    w=(1e9,None,None)
    for a,b in pedacos(S):
        for s,e,i in V:
            o=min(b,e)-max(a,s)
            if o>1e-6 and o<w[0]: w=(o,i,(a,b))
    return w
res=sorted(((pior(S),S) for S in range(LO,HI+1)),key=lambda x:(-x[0][0],-x[1]))
print(f"timeline {TOTAL}s = {TF} quadros @{FPS} · {len(V)} <video> · --split {SPLIT} · tamanhos {LO}-{HI}")
for (o,i,p),S in res[:TOP]:
    print(f"  --size {S}: {math.ceil(TF/S)} partes · sobra minima {o:.0f} quadros ({i} no pedaco {p[0]}-{p[1]})")
```


---

# ARQUIVO: `modelo-projeto/scripts/slots.py`

```python
"""POR VIDEO — reel KAZUO INAMORI. Mapa dos slots de B-roll em tempo ABSOLUTO de timeline (rate 1.1, timeline 98,275 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava
assets/broll-slots.json. Com --placeholders, gera cartoes rotulados em assets/broll/_ph/ e
escreve o plan.broll apontando para eles (so para ver a estrutura no preview).
Com --real, escreve o plan.broll apontando para assets/broll/<arquivo final>.
Layout desenhado a mao sobre as janelas de gaze/pose-windows.json (scripts/gaze_pose.py, olhar compensado pela pose da cabeca):
capa em split 0-1,65; cutaway 1,65-5,05 (olhada 1,72-2,24 do gancho); split 5,05-11,25 (pre-revelacao); revelacao em 11,25
("Kazuo" em 11,18 s); split 2 (a virada) 67,30-71,89 com a transicao de arrastar; climax 82,28 s ("E o lucro que o funcionario
tirou rastejando no chao"); apresentador no bipe (61,40-67,30) e no fim do CTA (96,15-fim)."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- SLOT 1: INTRO EM SPLIT (PRE-REVELACAO: nada de Inamori, Kyocera, KDDI ou JAL antes de "Kazuo", 11,18 s) ---
 ("s01","split", 0.00,  1.65,"Esse cara é um dos monges…","CAPA (ideia do Fabio): pista de aeroporto à noite, monge de costas diante de um avião sem logotipo, luz vermelha no alto","— (quadro 0 = capa)"),
 ("s02","full",  1.65,  5.05,"…mais temidos e mais lucrativos do planeta Terra.","PRÉ-REVELAÇÃO: monge zen japonês de costas / templo (sem rosto identificável)","olhada 1,72–2,24 s"),
 ("s03","split", 5.05,  8.00,"E ele criou um protocolo polêmico pra provar","PRÉ-REVELAÇÃO: sala de reunião com a mão batendo na mesa e planilhas voando (capa B, ideia do Fabio)","—"),
 ("s04","split", 8.00, 11.25,"que seu funcionário não pensa como dono porque você esconde o número.","PRÉ-REVELAÇÃO: dono escondendo a planilha / número fechado (callout de digitação)","—"),
 # --- SLOT 2: CUTAWAYS DO CORPO ---
 ("s05","full", 11.25, 13.60,"Kazuo fundou duas gigantes,","REVELAÇÃO: Kazuo Inamori + Kyocera","—"),
 ("s06","full", 13.60, 16.25,"virou um monge budista e, com setenta e oito anos,","Inamori de monge (1997)","—"),
 ("s07","full", 16.25, 19.60,"assumiu uma companhia aérea falida. Sem salário.","Inamori na Japan Airlines, 2010","olhadas 16,30–16,67 · 17,18–17,61 s"),
 ("s08","full", 22.40, 26.42,"…liga pro dinheiro da sua empresa. Primeiro, quebra a empresa em pedacinhos.","Gestão Ameba: equipes pequenas no chão de fábrica da Kyocera","olhadas 22,59–22,92 · 24,69–24,98 s"),
 ("s09","full", 31.00, 34.00,"Ele diz que quem vê o próprio resultado briga pelo lucro.","funcionários da Kyocera / equipe reunida","—"),
 ("s10","full", 34.00, 36.75,"Pela empresa inteira, ninguém briga.","a empresa inteira: sede/fábrica vista de fora","olhada 34,60–35,05 s"),
 ("s11","full", 40.30, 43.60,"Simples, igual conta de casa. Ele diz que tocar empresa","caderno de contas de casa (kakeibo)","olhada 41,58–41,86 s"),
 ("s12","full", 43.60, 47.30,"sem olhar número é pilotar avião sem olhar o painel.","cockpit: painel de instrumentos do avião","olhada 45,18–45,37 s"),
 ("s13","full", 47.30, 51.06,"Na sua, só você vê o número. E olhe lá, pequeno gafanhoto.","“pequeno gafanhoto”: série Kung Fu (Mestre Po)","olhada 48,65–49,11 s"),
 ("s14","full", 55.54, 58.82,"porque quem tem orçamento acha que o certo é gastar tudo.","orçamento aprovado / gastar tudo","—"),
 ("s15","full", 58.82, 61.40,"Sobrou verba em dezembro e o time torrou","verba torrada no fim do ano","—"),
 # --- SLOT 3: SEGUNDO SPLIT (A VIRADA) ---
 ("s16","split",67.30, 69.16,"E a virada foi uma reunião","reunião de diretoria da JAL com Inamori","—"),
 ("s17","split",69.16, 71.89,"com o diretor que ia gastar um bilhão de ienes.","maços de notas de 10.000 ienes","—"),
 ("s18","full", 74.94, 78.28,"O diretor: “Mas senhor, já está aprovado no orçamento.”","diretores da JAL","—"),
 # --- SLOT 4: CLIMAX EMOCIONAL ---
 ("s19","full", 82.28, 85.69,"“É o lucro que o funcionário tirou rastejando no chão.”","CLÍMAX: equipe de solo / manutenção da JAL — riser + impact","olhada 85,33–85,48 s"),
 ("s20","full", 85.69, 89.20,"No primeiro ano, a empresa falida bateu recorde de lucro.","JAL decolando / relistagem na bolsa em 2012","olhada 88,90–89,09 s"),
 ("s21","full", 93.45, 96.15,"Se você é o único que liga pro dinheiro da sua empresa,","dono sozinho olhando as contas","olhadas 94,71–95,04 · 95,65–96,11 s"),
]
NOMES={"s01":"s01-split-capa-monge-pista","s02":"s02-monge-temido","s03":"s03-split-protocolo-polemico","s04":"s04-split-esconde-numero",
 "s05":"s05-kazuo-revelacao","s06":"s06-virou-monge","s07":"s07-jal-sem-salario","s08":"s08-quebra-em-pedacinhos",
 "s09":"s09-briga-pelo-lucro","s10":"s10-empresa-inteira","s11":"s11-conta-de-casa","s12":"s12-painel-do-aviao",
 "s13":"s13-pequeno-gafanhoto","s14":"s14-orcamento-gastar-tudo","s15":"s15-verba-de-dezembro","s16":"s16-split-reuniao",
 "s17":"s17-split-bilhao-de-ienes","s18":"s18-aprovado-no-orcamento","s19":"s19-climax-rastejando","s20":"s20-recorde-de-lucro",
 "s21":"s21-unico-que-liga"}
def seg_of(x, end=False):
    for i,(a,b) in enumerate(segs):
        if (a<=x<b) if not end else (a<x<=b+1e-6): return i
    return len(segs)-1
slots=[]
for sid,mode,t0,t1,fala,tema,cobre in S:
    f=seg_of(t0); g=seg_of(t1,end=True); w0,w1=segs[f][0],segs[g][1]
    sp=[round((t0-w0)/(w1-w0),5),round((t1-w0)/(w1-w0),5)]
    slots.append(dict(id=sid,file=f"assets/broll/{NOMES[sid]}.mp4",mode=mode,fromSeg=f,toSeg=g,span=sp,
                      t0=t0,t1=t1,dur=round(t1-t0,2),fala=fala,tema=tema,cobre=cobre))
old={x['id']:x for x in json.load(open('assets/broll-slots.json')).get('slots',[])} if os.path.exists('assets/broll-slots.json') else {}
for s in slots:  # preserva campos da pesquisa (img, link, fonte, prompt...) ja gravados
    for k,v in old.get(s['id'],{}).items():
        if k not in s: s[k]=v
json.dump({"total":TOTAL,"slots":slots},open('assets/broll-slots.json','w'),ensure_ascii=False,indent=1)
print(f"{len(slots)} slots · timeline {TOTAL}s")
# POR VIDEO: slots que viraram motion graphics (compositions/mg.html, docs/13): ficam no broll-slots.json (tempos de
# referencia) e saem do plan.broll. Vazio = todo slot vira video de B-roll (fluxo antigo).
MG={"*"}  # "*" = TODO slot vira camada de motion (kit v3, padrao). set() = fluxo antigo (todo slot vira video)
def plan_broll(path_of):
    # kit v3: slot MG em split continua no plano com file "" (o split arrasta o apresentador; a faixa de cima e da camada)
    return [{k:s[k] for k in ('mode','fromSeg','toSeg','span')}|{"file":("" if ('*' in MG or s['id'] in MG) else path_of(s))} for s in slots
            if not ('*' in MG or s['id'] in MG) or s['mode']=='split']
if '--placeholders' in sys.argv:
    from PIL import Image, ImageDraw, ImageFont
    os.makedirs('assets/broll/_ph',exist_ok=True)
    try: fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',46); fs=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',30)
    except Exception: fnt=fs=ImageFont.load_default()
    for k,s in enumerate(slots):
        W,H=(720,1280) if s["mode"]=="full" else (720,564)
        im=Image.new('RGB',(W,H),[(38,52,86),(70,44,86),(40,78,70),(86,62,36)][k%4]); d=ImageDraw.Draw(im)
        y=H*0.30 if s['mode']=='full' else 60
        for line in [f"B-ROLL {s['id']}", "aguardando arquivo", NOMES[s['id']]+".mp4", f"{s['dur']:.2f}s"]:
            d.text((W/2,y),line,font=fnt if line.startswith('B-') else fs,fill=(255,255,255),anchor='mm'); y+=70
        png=f"assets/broll/_ph/{s['id']}.png"; im.save(png)
        subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-i',png,'-t',f"{s['dur']+0.2:.2f}",'-r','60','-c:v','libx264','-pix_fmt','yuv420p','-g','30','-crf','30',f"assets/broll/_ph/{s['id']}.mp4"],check=True)
    P['broll']=plan_broll(lambda s:f"assets/broll/_ph/{s['id']}.mp4"); P['_broll']="PLACEHOLDERS (cartoes rotulados) — slots aguardando os B-rolls do usuario. Ver PESQUISAS-BROLL-KAZUO-INAMORI.md."
    json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1); print("plan.broll -> placeholders")
if '--real' in sys.argv:
    P['broll']=plan_broll(lambda s:s['file']); json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1); print("plan.broll -> arquivos finais")
```


---

# ARQUIVO: `modelo-projeto/scripts/sync-check.mjs`

```javascript
#!/usr/bin/env node
// Sincronia A/V por dados. Para cada take, compara o envelope de energia do ÁUDIO DO MP4 FINAL
// com o áudio do bruto no instante de source que o VÍDEO do apresentador mostra naquele ponto.
// lag ≈ 0 ms => boca e voz alinhadas.  uso: node scripts/sync-check.mjs <final16k.wav> <bruto16k.wav>
import fs from 'node:fs';
const plan = JSON.parse(fs.readFileSync('assets/edit-plan.json', 'utf8'));
const RATE = plan.rate || 1, FPS = plan.fps || 30, F = n => n / FPS;
const LEAD = F(plan.jcutLeadFrames ?? 5);
const r3 = x => Math.round(x * 1000) / 1000;
let t = 0; const segs = plan.segments.map((s, i) => {
  const sd = r3((s.out - s.in) / RATE); const lead = i === 0 ? 0 : Math.min(LEAD, sd - F(10));
  const d = r3(sd - lead); const o = { i, in: s.in, lead, tStart: r3(t), dur: d }; t = r3(t + d); return o;
});
const early = segs.map(s => (plan.segments[s.i].videoTail ? r3((plan.segments[s.i].out - plan.segments[s.i].videoTail) / RATE) : 0));
segs.forEach(s => { const dPrev = s.i > 0 ? early[s.i - 1] : 0; s.vStart = r3(s.tStart - dPrev); s.vMedia = r3(s.in + (s.lead - dPrev) * RATE); });
const rd = f => fs.readFileSync(f);
const A = rd(process.argv[2]), S = rd(process.argv[3]), SR = 16000, W = 160;
const env = (b, t0, secs, speed = 1) => { const o = []; for (let k = 0; k < secs * 100; k++) { const off = Math.round((t0 + k * 0.01 * speed) * SR); let s = 0; for (let i = 0; i < W; i++) { const j = 44 + 2 * (off + i); if (j + 1 < b.length && j >= 44) { const v = b.readInt16LE(j) / 32768; s += v * v; } } o.push(Math.sqrt(s / W)); } return o; };
const corr = (a, b) => { const ma = a.reduce((x, y) => x + y, 0) / a.length, mb = b.reduce((x, y) => x + y, 0) / b.length; let n = 0, da = 0, db = 0; for (let i = 0; i < a.length; i++) { n += (a[i] - ma) * (b[i] - mb); da += (a[i] - ma) ** 2; db += (b[i] - mb) ** 2; } return n / Math.sqrt(da * db + 1e-12); };
const rows = [];
for (const s of segs) {
  if (s.dur < 1.0) continue;
  const tt = r3(s.tStart + Math.min(1.2, s.dur * 0.4));
  const src = r3(s.vMedia + (tt - s.vStart) * RATE);
  const ref = env(S, src, 1.2, RATE);
  let best = { lag: 0, r: -1 };
  for (let lag = -15; lag <= 15; lag++) { const r = corr(ref, env(A, tt + lag * 0.01, 1.2)); if (r > best.r) best = { lag, r }; }
  rows.push({ i: s.i, t: tt, lagMs: best.lag * 10, r: +best.r.toFixed(2) });
}
console.log(rows.map(r => `  seg${String(r.i).padStart(2)}@${String(r.t).padStart(6)}s  lag ${String(r.lagMs).padStart(4)} ms  (r=${r.r})`).join('\n'));
const good = rows.filter(r => r.r > 0.6).map(r => r.lagMs).sort((a, b) => a - b);
console.log(`\n${good.length}/${rows.length} pontos com correlação > 0.6 · lag mediano ${good[good.length >> 1]} ms · faixa ${good[0]}..${good.at(-1)} ms (1 quadro = 33 ms)`);
```


---

# ARQUIVO: `modelo-projeto/scripts/tl.py`

```python
"""Timeline dos takes (mesma conta do build-edit.mjs) + palavras em tempo de timeline. Uso: tl.py [--words]"""
import json, sys
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
M={m['i']:m for m in json.load(open('assets/chunks/meta.json'))}
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3),lead)); t=round(t+d,3)
def src2tl(i,x):  # voz do take i: comeca lead antes de t0
    s=P['segments'][i]; return round(segs[i][0]-segs[i][2]+(x-s['in'])/R,3)
if __name__=='__main__':
    for i,s in enumerate(P['segments']):
        d=json.load(open(f"assets/chunks/ch{i:02d}-words.json"))
        ws=[(e['text'].strip(),src2tl(i,M[i]['off']+e['offsets']['from']/1000)) for e in d['transcription'] if e['text'].strip()]
        txt=' '.join(f"{w}@{x:.2f}" for w,x in ws) if '--words' in sys.argv else ' '.join(w for w,_ in ws)
        print(f"{i:2d} {s['label']:<20} {segs[i][0]:6.2f}-{segs[i][1]:6.2f} ({segs[i][1]-segs[i][0]:.2f})  {txt}")
    print('TOTAL',t)
```


---

# ARQUIVO: `modelo-projeto/scripts/valleys.py`

```python
"""Lista os vales de silencio (envelope RMS 10 ms) perto de um instante do source.
Uso: valleys.py t1 t2 ...  -> para cada t, runs abaixo de -38 dB em [t-0.7, t+0.7]"""
import numpy as np, wave, sys
w=wave.open('work/full-clean.wav'); sr=w.getframerate()
a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768.0
W=int(0.010*sr); nw=len(a)//W
db=20*np.log10(np.sqrt(np.maximum((a[:nw*W].reshape(nw,W)**2).mean(1),1e-12)))
THR=float(__import__('os').environ.get('THR','-38'))
for t in map(float,sys.argv[1:]):
    lo,hi=int((t-0.7)/0.01),int((t+0.7)/0.01); runs=[];i=lo
    while i<hi:
        if db[i]<THR:
            j=i
            while j<hi and db[j]<THR: j+=1
            runs.append((i*0.01,j*0.01,db[i:j].min())); i=j
        else: i+=1
    print(f"t={t:.2f}: "+"  ".join(f"[{s:.2f}-{e:.2f} {e-s:.2f}s {m:.0f}dB]" for s,e,m in runs if e-s>=0.04))
```


---

# ARQUIVO: `modelo-projeto/scripts/vw_batch.py`

```python
"""Varredura de olhar em lote: para cada janela (source a-b), monta uma faixa quadro a
quadro so da regiao dos olhos, com o gx medido. Uso: vw_batch.py nome:a:b[:passo] ..."""
import subprocess,sys,os,json
from _src import SRC
M={round(o['t'],3):o for o in json.load(open('gaze/measure.json')) if o.get('ok')}
os.makedirs('work/vb',exist_ok=True)
pad='work/vb/pad.jpg'
subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=c=#101014:s=420x163:d=1','-frames:v','1',pad],check=True)
for spec in sys.argv[1:]:
    p=spec.split(':'); name=p[0]; a=float(p[1]); b=float(p[2]); step=float(p[3]) if len(p)>3 else 0.1
    ts=[];x=a
    while x<=b+1e-6: ts.append(round(x,2)); x+=step
    files=[];line=[]
    for i,t in enumerate(ts):
        f=f"work/vb/{name}_{i:02d}.jpg"
        subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',SRC,'-frames:v','1',
          '-vf','crop=720:280:250:1100,scale=420:163',f],check=True)
        files.append(f); n=min(M,key=lambda k:abs(k-t)); line.append(f"{t:.2f}:{M[n]['gx']:+.3f}")
    COLS=6
    while len(files)%COLS: files.append(pad)
    args=[]
    for f in files: args+=['-i',f]
    rows=[files[i:i+COLS] for i in range(0,len(files),COLS)]
    fc="";idx=0;ro=[]
    for ri,r in enumerate(rows):
        fc+="".join(f"[{idx+j}:v]" for j in range(COLS))+f"hstack=inputs={COLS}[r{ri}];";idx+=COLS;ro.append(f"[r{ri}]")
    fc+="".join(ro)+f"vstack=inputs={len(ro)}[out]" if len(ro)>1 else f"{ro[0]}copy[out]"
    subprocess.run(['ffmpeg','-v','error','-y']+args+['-filter_complex',fc,'-map','[out]',f'work/vb/{name}.jpg'],check=True)
    for f in files:
        if f!=pad: os.remove(f)
    print(name, '  '.join(line))
```


---

# ARQUIVO: `modelo-projeto/scripts/vw_big.py`

```python
"""Quadros grandes (rosto) em tempos de TIMELINE, rotulados. Uso: vw_big.py saida.jpg t1 t2 ..."""
import json, cv2, sys
from PIL import Image, ImageDraw, ImageFont
from _src import SRC
T=[o for o in json.load(open('gaze/tl.json')) if o['ok']]
cap=cv2.VideoCapture(SRC); fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',26)
ts=[float(x) for x in sys.argv[2:]]; ims=[]
for t in ts:
    o=min(T,key=lambda x:abs(x['t']-t)); cap.set(cv2.CAP_PROP_POS_MSEC,o['src']*1000); ok,f=cap.read()
    c=cv2.resize(f[1000:1700,300:1200],(360,280)); im=Image.fromarray(cv2.cvtColor(c,cv2.COLOR_BGR2RGB))
    d=ImageDraw.Draw(im); d.rectangle([0,0,86,30],fill=(0,0,0)); d.text((4,1),f"{t:.2f}",font=fnt,fill=(255,255,0)); ims.append(im)
C=6; R=(len(ims)+C-1)//C; sh=Image.new('RGB',(360*C,280*R),(20,20,20))
for k,im in enumerate(ims): sh.paste(im,(360*(k%C),280*(k//C)))
sh.save(sys.argv[1],quality=88); print(sys.argv[1])
```


---

# ARQUIVO: `modelo-projeto/scripts/vw_eyes.py`

```python
"""Olhos em ZOOM (tempos de TIMELINE, rotulados) para tirar duvida de leitura x movimento de cabeca. Uso: vw_eyes.py saida.jpg t1 t2 ..."""
import json, cv2, sys
from PIL import Image, ImageDraw, ImageFont
from _src import SRC
T=[o for o in json.load(open('gaze/tl.json')) if o['ok']]
cap=cv2.VideoCapture(SRC); fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',24)
ims=[]
for t in [float(x) for x in sys.argv[2:]]:
    o=min(T,key=lambda x:abs(x['t']-t)); cap.set(cv2.CAP_PROP_POS_MSEC,o['src']*1000); ok,f=cap.read()
    c=cv2.resize(f[1060:1420,340:1140],(500,225)); im=Image.fromarray(cv2.cvtColor(c,cv2.COLOR_BGR2RGB))
    d=ImageDraw.Draw(im); d.rectangle([0,0,150,28],fill=(0,0,0)); d.text((4,1),f"{t:.2f} s{o['side']:+.2f} d{o['down']:.2f}",font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',15),fill=(255,255,0)); ims.append(im)
C=4; R=(len(ims)+C-1)//C; sh=Image.new('RGB',(500*C,225*R),(20,20,20))
for k,im in enumerate(ims): sh.paste(im,(500*(k%C),225*(k//C)))
sh.save(sys.argv[1],quality=90); print(sys.argv[1])
```


---

# ARQUIVO: `modelo-projeto/scripts/vw_tl.py`

```python
"""Folhas de conferencia das janelas de leitura (gaze/tl-windows.json): 1 linha por janela, quadros
da faixa dos olhos de t0-0.2 a t1+0.2 (tempos de TIMELINE, rotulados). Uso: vw_tl.py [saida] [i0 i1]"""
import json, cv2, sys, os, numpy as np
from PIL import Image, ImageDraw, ImageFont
from _src import SRC  # recorte dos olhos: reel KAZUO INAMORI, olhos em y~1220-1260, x~580-900 do 1440x2560
W=json.load(open('gaze/tl-windows.json')); T=[o for o in json.load(open('gaze/tl.json')) if o['ok']]
out=sys.argv[1] if len(sys.argv)>1 else 'gaze/tlw'; os.makedirs(out,exist_ok=True)
i0,i1=(int(sys.argv[2]),int(sys.argv[3])) if len(sys.argv)>3 else (0,len(W))
cap=cv2.VideoCapture(SRC); fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',22)
def frame(t):
    o=min(T,key=lambda x:abs(x['t']-t)); cap.set(cv2.CAP_PROP_POS_MSEC,o['src']*1000); ok,f=cap.read()
    c=f[1100:1380,380:1100]; c=cv2.resize(c,(300,117)); im=Image.fromarray(cv2.cvtColor(c,cv2.COLOR_BGR2RGB))
    d=ImageDraw.Draw(im); lab=f"{t:.2f}"; d.rectangle([0,0,70,24],fill=(0,0,0)); d.text((3,0),lab,font=fnt,fill=(255,255,0)); return im
COLS=8; rows=[]
for k in range(i0,min(i1,len(W))):
    w=W[k]; a,b=w['t0']-0.2,w['t1']+0.2; ts=list(np.linspace(a,b,COLS))
    row=Image.new('RGB',(300*COLS+90,117),(16,16,20)); d=ImageDraw.Draw(row); d.text((4,40),f"w{k}",font=fnt,fill=(255,255,255))
    for j,t in enumerate(ts): row.paste(frame(t),(90+300*j,0))
    rows.append(row)
for g in range(0,len(rows),9):
    B=rows[g:g+9]; sh=Image.new('RGB',(B[0].width,117*len(B)+4*(len(B)-1)),(60,60,60))
    for j,r in enumerate(B): sh.paste(r,(0,j*121))
    p=f"{out}/s{(i0+g)//9:02d}.jpg"; sh.save(p,quality=88); print(p, f"w{i0+g}-w{i0+g+len(B)-1}")
```


---

# ARQUIVO: `modelo-projeto/scripts/whisper_chunks.sh`

```bash
#!/bin/zsh
M=$HOME/.cache/whisper/ggml-large-v3.bin
for w in assets/chunks/ch*.wav; do
  b=${w%.wav}
  whisper-cli -m $M -l pt --max-context 0 -ml 1 -sow -oj -of ${b}-words -f $w > work/whc-${b:t}.log 2>&1 || echo "FALHOU $b"
done
echo "json: $(ls assets/chunks/ch*-words.json | wc -l) / wav: $(ls assets/chunks/ch*.wav | wc -l)"
```


---

# ARQUIVO: `modelo-projeto/scripts/whisper_regs.sh`

```bash
#!/bin/zsh
# Transcricao por REGIAO, palavra a palavra. Kit v3: large-v3-TURBO por padrao (2,3x mais rapido, mesmo texto em PT
# medido no reel Alan Mulally: 11 s x 26 s em 5 regioes). WHISPER_MODEL=<caminho> troca o modelo; sem o turbo cai no large-v3.
# Serial: nunca junto com encode pesado.
M=${WHISPER_MODEL:-$HOME/.cache/whisper/ggml-large-v3-turbo.bin}
[ -f "$M" ] || M=$HOME/.cache/whisper/ggml-large-v3.bin
echo "whisper: ${M:t}"
for w in work/reg/r*.wav; do
  b=${w%.wav}; n=${b:t}
  whisper-cli -m $M -l pt --max-context 0 -ml 1 -sow -oj -of $b -f $w > work/wh-$n.log 2>&1 || echo "FALHOU $n"
done
echo "json: $(ls work/reg/r*.json | wc -l) / wav: $(ls work/reg/r*.wav | wc -l)"
```


---

# ARQUIVO: `modelo-projeto/work/layout-exemplo.py`

```python
# Layout desenhado a mao (reel SUN TZU) sobre as leituras nitidas de gaze/tl-windows-conf.json. S=split, B=B-roll tela cheia, P=apresentador
L=[('S',0.00,2.60),('S',2.60,4.95),('B',4.95,7.40),('S',7.40,9.87),('B',9.87,13.40),('B',13.40,17.09),('P',17.09,20.48),
('B',20.48,24.20),('P',24.20,27.60),('B',27.60,31.70),('P',31.70,32.70),('B',32.70,36.95),('B',36.95,39.44),('P',39.44,42.32),
('B',42.32,45.30),('P',45.30,47.34),('B',47.34,50.90),('B',50.90,55.30),('P',55.30,57.24),('B',57.24,60.30),('S',60.30,63.00),
('B',63.00,66.62),('S',66.62,69.73),('P',69.73,72.40),('B',72.40,74.70),('P',74.70,77.61),('B',77.61,81.00),('B',81.00,83.59),
('B',83.59,85.82),('P',85.82,91.509)]
```


---

# ARQUIVO: `modelo-projeto/work/mg-cues-auto.json`

```json
[]
```


---

# ARQUIVO: `modelo-projeto/work/render-all.sh`

```bash
#!/bin/zsh
# Render em partes, uma por vez, cada parte dividida em pedacos (sessao nova do Chrome por pedaco).
# uso: zsh work/render-all.sh <SIZE> [FPS=60] [SPLIT=3]      SIZE = o melhor de `python3 scripts/size_sweep.py`
# RODAR COMO TAREFA DE FUNDO DO HARNESS (run_in_background). Com `nohup ... &` dentro de uma chamada de shell o render
# morre com "render_cancelled_parent_exited" quando a chamada termina.
# Antes: parar o preview deste projeto (libera RAM) e conferir o disco (>= 7 GB livres e o confortavel; com menos,
# este script ja mantem o TMPDIR do render DENTRO do projeto e limpa a cada parte).
# Retoma de onde parou: parte que ja existe e pulada. Correcao sem mudar o tempo: apagar so as partes afetadas e rodar de novo.
cd "${0:A:h}/.."
SIZE=${1:?uso: zsh work/render-all.sh <SIZE> [FPS=60] [SPLIT=3]}; FPS=${2:-60}; SPLIT=${3:-3}
export TMPDIR="$PWD/renders/tmp/"
mkdir -p renders/chunks renders/tmp
N=$(python3 -c "import json,math;print(math.ceil(math.ceil(json.load(open('work/mix-plan.json'))['total']*$FPS-1e-6)/$SIZE))")
echo "$N partes de $SIZE quadros @$FPS, --split $SPLIT"
for k in $(seq 0 $((N-1))); do
  t0=$(date +%s)
  mkdir -p renders/tmp
  if [ -f renders/chunks/chunk-$(printf %02d $k).mp4 ]; then echo "parte $k ja existe"; continue; fi
  node scripts/render-chunks.mjs --fps $FPS --size $SIZE --split $SPLIT --only $k > renders/chunks/log-$k.txt 2>&1 || { echo "PARTE $k FALHOU"; tail -5 renders/chunks/log-$k.txt; rm -f renders/chunks/chunk-$(printf %02d $k).mp4; exit 1; }
  find renders/chunks -name "sub-$(printf %02d $k)-*" -delete
  rm -rf renders/tmp/*
  free=$(df -m /System/Volumes/Data | tail -1 | awk '{print $4}')
  echo "parte $k pronta em $(( $(date +%s)-t0 ))s · livre ${free} MB"
  if [ $free -lt 600 ]; then echo "DISCO CRITICO (${free} MB) — parando"; exit 2; fi
done
echo "TODAS AS PARTES OK — agora: python3 scripts/finalizar.py renders/<Nome>-reel-final.mp4 --fps $FPS"
```


---

# ARQUIVO: `modelo-projeto/work/pesq/crawl.py`

```python
#!/usr/bin/env python3
# BFS serial em www.kyocera.co.jp/inamori (limite de paginas); grava crawl.json {img_url: [page, alt]}
import urllib.request, re, json, sys, time, urllib.parse
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
base=sys.argv[1]; pref=sys.argv[2]; lim=int(sys.argv[3]); out=sys.argv[4]
seen=set([base]); q=[base]; imgs={}
n=0
while q and n<lim:
    u=q.pop(0); n+=1
    try: h=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=25).read().decode('utf-8','ignore')
    except Exception as e: print('ERR',u,e); continue
    for m in re.finditer(r'<img[^>]+>',h):
        t=m.group(0); s=re.search(r'src="([^"]+)"',t); a=re.search(r'alt="([^"]*)"',t)
        if not s: continue
        iu=urllib.parse.urljoin(u,s.group(1))
        if re.search(r'assets/img|\.svg|\.gif',iu): continue
        imgs.setdefault(iu,[u,a.group(1) if a else ''])
    for m in re.finditer(r'href="([^"#]+)"',h):
        l=urllib.parse.urljoin(u,m.group(1)).split('#')[0]
        if re.search(r'\.(jpg|jpeg|png)$',l,re.I) and pref in l: imgs.setdefault(l,[u,'link'])
        if l.startswith(pref) and l not in seen and not re.search(r'\.(css|js|png|jpg|jpeg|pdf|ico|svg|mp4)$',l):
            seen.add(l); q.append(l)
    time.sleep(0.3)
json.dump(imgs,open(out,'w'),ensure_ascii=False,indent=0); print(n,'pages',len(imgs),'imgs', len(q),'left')
```


---

# ARQUIVO: `modelo-projeto/work/pesq/dl.py`

```python
#!/usr/bin/env python3
# uso: dl.py <tag> <img_url> <page_url> <dom>  -> raw/<tag>.jpg (converte com Pillow), registra em g_index.json
import sys, json, os, io, urllib.request
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
tag, img, page, dom = sys.argv[1:5]
if 'images.pexels.com' in img: img=img.split('?')[0]+'?auto=compress&cs=tinysrgb&w=3000'
req = urllib.request.Request(img, headers={'User-Agent': UA, 'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8', 'Referer': page})
try: data = urllib.request.urlopen(req, timeout=40).read()
except Exception as e: print(tag, 'FAIL', e); sys.exit(1)
out = f'raw/{tag}.jpg'
try:
    im = Image.open(io.BytesIO(data)); w, h = im.size
    if data[:3] == b'\xff\xd8\xff': open(out, 'wb').write(data)
    else:
        if im.mode in ('RGBA','LA','P'):
            im = im.convert('RGBA'); bg = Image.new('RGB', im.size, 'white'); bg.paste(im, mask=im.split()[3]); im = bg
        im.convert('RGB').save(out, quality=95)
except Exception as e: print(tag, 'CONVFAIL', e); sys.exit(1)
idx = json.load(open('g_index.json')) if os.path.exists('g_index.json') else {}
idx[tag] = dict(file=out, w=w, h=h, img=img, page=page, dom=dom)
json.dump(idx, open('g_index.json', 'w'), indent=1)
print(tag, w, h)
```


---

# ARQUIVO: `modelo-projeto/work/pesq/filt.py`

```python
import sys,json
bad=("shutterstock","getty","alamy","istock","dreamstime","123rf","depositphotos","vecteezy","freepik","pinterest","pinimg","stock.adobe","agefotostock","bigstock","canstock","superstock","pond5","megapixl","masterfile","lookandlearn","bridgeman","artstation","lovepik","pngtree","gettyimages","westend61","stockcake")
for l in sys.stdin:
  x=json.loads(l)
  w,h=x.get("w") or 0,x.get("h") or 0
  if min(w,h)<900: continue
  if any(b in (x["dom"]+x["img"]).lower() for b in bad): continue
  print(x["i"], "%dx%d"%(w,h), x["dom"], "|", x["title"][:60], "|", x["img"], "|", x["page"])
```


---

# ARQUIVO: `modelo-projeto/work/pesq/pick.sh`

```bash
#!/bin/zsh
# uso: pick.sh <qid> <idx> [<idx>...]  -> baixa em raw/<qid>_<idx>.jpg
cd "${0:A:h}"; mkdir -p raw
q=$1; shift
for i in "$@"; do python3 - "$q" "$i" <<'PY'
import sys,subprocess
q,i=sys.argv[1:3]
for l in open(f'q/{q}.txt'):
    if l.split(' ',1)[0]==i:
        f=l.rstrip('\n').split(' | '); dom=l.split(' ')[2]
        subprocess.run(['python3','dl.py',f'{q}_{i}',f[-2],f[-1],dom]); break
PY
done
```


---

# ARQUIVO: `modelo-projeto/work/pesq/s.sh`

```bash
#!/bin/zsh
# uso: s.sh <qid> "consulta" [n]  -> q/<qid>.txt   (Google Imagens via scripts/gimg.mjs, filtrado por filt.py)
P="${0:A:h}"; mkdir -p "$P/q"
cd "$P/../.." && node scripts/gimg.mjs "$2" ${3:-20} | python3 work/pesq/filt.py > work/pesq/q/$1.txt; echo "== $1 $2: $(wc -l < work/pesq/q/$1.txt)"
```


---

# ARQUIVO: `modelo-projeto/work/pesq/sheet.py`

```python
#!/usr/bin/env python3
# uso: sheet.py <out.jpg> <glob...>  -> grade de miniaturas rotuladas
import sys,glob,os
from PIL import Image,ImageDraw,ImageFont
out=sys.argv[1]; files=[]
def key(p):
    b=os.path.basename(p)[:-4]; a,_,n=b.rpartition('-')
    return (a,int(n) if n.isdigit() else 0)
for g in sys.argv[2:]: files+=glob.glob(g)
files=sorted(set(files),key=key)
C=4; TW,TH=420,420
rows=(len(files)+C-1)//C
S=Image.new('RGB',(C*TW,rows*(TH+30)),'white'); d=ImageDraw.Draw(S)
try: F=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',22)
except: F=None
for k,f in enumerate(files):
    try: im=Image.open(f); w,h=im.size; im=im.convert('RGB'); im.thumbnail((TW-8,TH-8))
    except Exception as e: continue
    x=(k%C)*TW; y=(k//C)*(TH+30)
    S.paste(im,(x+(TW-im.width)//2,y+(TH-im.height)//2))
    d.text((x+6,y+TH+2),f"{os.path.basename(f)[:-4]}  {w}x{h}",fill='black',font=F)
S.save(out,quality=85); print(out,len(files))
```


---

# ARQUIVO: `modelo-projeto/work/pesq/wm.py`

```python
#!/usr/bin/env python3
# uso: wm.py "consulta" [n]  -> busca arquivos no Commons; imprime idx WxH titulo licenca ; salva q/wm_<slug>.json
import sys, json, urllib.request, urllib.parse, re, os
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
q=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 30
p=dict(action='query',format='json',generator='search',gsrsearch=q+' filetype:bitmap',gsrnamespace=6,gsrlimit=n,prop='imageinfo',iiprop='url|size|extmetadata',iiurlwidth=1920)
u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(p)
import time
for k in range(4):
    try: j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}))); break
    except Exception as e: print('retry',e); time.sleep(15*(k+1))
pages=sorted(j.get('query',{}).get('pages',{}).values(), key=lambda x:x.get('index',0))
out=[]
for i,pg in enumerate(pages):
  ii=pg['imageinfo'][0]; em=ii.get('extmetadata',{})
  lic=em.get('LicenseShortName',{}).get('value','')
  w,h=ii['width'],ii['height']
  rec=dict(i=i,title=pg['title'],w=w,h=h,lic=lic,url=ii['url'],thumb=ii.get('thumburl',ii['url']),page=ii['descriptionurl'])
  out.append(rec)
  if min(w,h)>=800: print(i,f'{w}x{h}',pg['title'][5:90],'|',lic)
slug=re.sub(r'\W+','_',q)[:40]
json.dump(out,open(f'q/wm_{slug}.json','w'),indent=0)
print('->',f'q/wm_{slug}.json')
```


---

# ARQUIVO: `modelo-projeto/work/pesq/wmpick.py`

```python
#!/usr/bin/env python3
# uso: wmpick.py <slug> <idx...> -> raw/wm_<slug>_<i>.jpg (original; tif/png convertidos), registra em g_index.json com lic
import sys,json,subprocess,time
slug=sys.argv[1]; j=json.load(open(f'q/wm_{slug}.json'))
lic=json.load(open('wm_lic.json')) if __import__('os').path.exists('wm_lic.json') else {}
for i in sys.argv[2:]:
    r=j[int(i)]; tag=f'wm_{slug}_{i}'
    u=r['url'] if r['url'].lower().endswith(('.jpg','.jpeg','.png')) and r['w']*r['h']<40e6 else r['thumb']
    subprocess.run(['python3','dl.py',tag,u,r['page'],'commons.wikimedia.org'])
    lic[tag]=dict(lic=r['lic'],title=r['title']); time.sleep(3)
json.dump(lic,open('wm_lic.json','w'),ensure_ascii=False,indent=0)
```
