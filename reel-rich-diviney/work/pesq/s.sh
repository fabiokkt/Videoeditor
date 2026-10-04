#!/bin/zsh
# uso: s.sh <qid> "consulta" [n]  -> q/<qid>.txt   (Google Imagens via scripts/gimg.mjs, filtrado por filt.py)
P="${0:A:h}"; mkdir -p "$P/q"
cd "$P/../.." && node scripts/gimg.mjs "$2" ${3:-20} | python3 work/pesq/filt.py > work/pesq/q/$1.txt; echo "== $1 $2: $(wc -l < work/pesq/q/$1.txt)"
