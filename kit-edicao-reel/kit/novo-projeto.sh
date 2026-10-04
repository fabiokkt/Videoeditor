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
