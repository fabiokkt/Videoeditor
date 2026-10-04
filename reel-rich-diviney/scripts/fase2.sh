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
