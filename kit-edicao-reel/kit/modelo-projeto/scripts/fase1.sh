#!/bin/zsh
# FLUXO RAPIDO (kit v3) · FASE 1 — bruto -> mezanino + voz + transcricao por regiao (whisper turbo). ~5 min.
# uso: zsh scripts/fase1.sh "<bruto>" <slug>      (rodar como tarefa de fundo; enquanto isso: pesquisa de fotos, docs/11)
# kit v3.1: com >= 12 GB de RAM e >= 8 nucleos (Mac Apple Silicon: whisper na GPU) a voz sai primeiro e a transcricao roda
# ENQUANTO o mezanino codifica (o whisper so precisa do audio). Container de 4 nucleos: serie — medido no reel Ridgway, em paralelo
# os dois disputam a CPU e a fase 1 foi de ~850 s para 953 s (docs/05 §32). Air de 8 GB: serie (derruba o opendirectoryd, §3).
# PARALELO=0/1 forca.
set -e; cd "${0:A:h}/.."; export PATH=$HOME/Claude/.venv-reel/bin:$PATH
MEM=$( (sysctl -n hw.memsize 2>/dev/null || awk '/MemTotal/{print $2*1024}' /proc/meminfo) | awk '{print int($1/1073741824+0.5)}')
NC=$(sysctl -n hw.ncpu 2>/dev/null || nproc)
PAR=${PARALELO:-$([ "$MEM" -ge 12 ] && [ "$NC" -ge 8 ] && echo 1 || echo 0)}
MEZ="assets/$2-2560-sdr.mp4"; T0=$(date +%s)
if [ -f "$MEZ" ]; then echo "mezanino ja existe (pulado)"; [ -f work/full-clean.wav ] || zsh scripts/mezanino.sh "$1" "$2" audio
elif [ "$PAR" = 1 ]; then
  echo "RAM ${MEM} GB · ${NC} nucleos -> mezanino em paralelo com a transcricao"
  zsh scripts/mezanino.sh "$1" "$2" audio
  zsh scripts/mezanino.sh "$1" "$2" video > work/mezanino.log 2>&1 & MPID=$!
else
  echo "RAM ${MEM} GB · ${NC} nucleos -> serie (mezanino, depois transcricao)"; zsh scripts/mezanino.sh "$1" "$2"
fi
python3 scripts/regions.py | tail -1 && python3 scripts/mkreg.py | tail -1 && zsh scripts/whisper_regs.sh | tail -2
python3 scripts/regwords.py > work/regioes.txt
echo "transcricao em $(( $(date +%s)-T0 ))s"
if [ -n "$MPID" ]; then
  wait $MPID || { echo "MEZANINO FALHOU:"; tail -5 work/mezanino.log; exit 1; }
  grep -E "^ +t=|^-> |mezanino:" work/mezanino.log; echo "mezanino pronto em $(( $(date +%s)-T0 ))s"
fi
cat work/regioes.txt
echo "FASE 1 OK -> ler work/regioes.txt contra o roteiro; escrever mkcut.py (SPLIT/DROP), cuts.py (TAKES), bipe.py se houver palavrao"
