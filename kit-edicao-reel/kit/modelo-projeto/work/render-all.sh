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
