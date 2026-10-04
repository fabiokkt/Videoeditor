#!/bin/zsh
# Refaz as legendas do zero a partir do passe por regiao + scripts/captions_fix_table.py (idempotente) e regenera o index.
# uso: zsh scripts/legendas.sh      (depois de mexer na captions_fix_table.py)
set -e; cd "${0:A:h}/.."; export PATH=$HOME/Claude/.venv-reel/bin:$PATH
cp work/chunks-raw/ch*-words.json assets/chunks/ && rm -rf work/chunks-aligned
python3 scripts/align.py > work/align.txt 2>&1 && python3 scripts/fix_captions.py | tail -3
node scripts/build-edit.mjs | tail -1
