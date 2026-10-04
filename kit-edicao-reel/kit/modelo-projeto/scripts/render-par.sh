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
