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
