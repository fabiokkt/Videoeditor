#!/bin/zsh
# FLUXO RAPIDO (kit v3) · MONTAR — slots (MG) -> build -> leaks + bed -> SFX automaticos da camada de motion -> check
# -> snapshots nos instantes pedidos. ~3 min. uso: zsh scripts/montar.sh 13.4,16.8,26.9,...   (instantes p/ conferir)
set -e; cd "${0:A:h}/.."; export PATH=$HOME/Claude/.venv-reel/bin:$PATH
python3 scripts/slots.py --real | tail -1 && node scripts/build-edit.mjs | tail -1
python3 scripts/bake.py cenas brollfull leaks bed | tail -3
node scripts/mg_cues.mjs && python3 scripts/mg_sfx.py | tail -1
npx --yes hyperframes@0.8.64 check 2>&1 | grep -E "error\(s\)" | head -2
[ -n "$1" ] && { rm -rf snapshots/qc; npx --yes hyperframes@0.8.64 snapshot . -o snapshots/qc --at "$1" --no-end --timeout 20000 >/dev/null 2>&1; ls snapshots/qc/contact-sheet*.jpg; }
echo "MONTAR OK"
