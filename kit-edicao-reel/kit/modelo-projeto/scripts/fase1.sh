#!/bin/zsh
# FLUXO RAPIDO (kit v3) · FASE 1 — bruto -> mezanino + voz + transcricao por regiao (whisper turbo). ~5 min.
# uso: zsh scripts/fase1.sh "<bruto>" <slug>      (rodar como tarefa de fundo; enquanto isso: pesquisa no navegador)
set -e; cd "${0:A:h}/.."; export PATH=$HOME/Claude/.venv-reel/bin:$PATH
[ -f "assets/$2-2560-sdr.mp4" ] && echo "mezanino ja existe (pulado)" || zsh scripts/mezanino.sh "$1" "$2"
python3 scripts/regions.py && python3 scripts/mkreg.py | tail -1 && zsh scripts/whisper_regs.sh | tail -2
python3 scripts/regwords.py > work/regioes.txt; cat work/regioes.txt
echo "FASE 1 OK -> ler work/regioes.txt contra o roteiro; escrever mkcut.py (SPLIT/DROP), cuts.py (TAKES), bipe.py se houver palavrao"
