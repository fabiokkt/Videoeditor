#!/bin/zsh
# Fase 1 — mezanino + voz. NOVO no kit v2 (2026-10-01): junta os comandos que eram digitados a cada reel.
# uso: zsh scripts/mezanino.sh "<bruto.MP4>" <slug>
#   -> assets/<slug>-2560-sdr.mp4   mezanino na resolucao e no fps do bruto, BT.709 limited, GOP 30, sem audio
#   -> work/<slug>-voz-limpa.m4a    audio do bruto, sem reencode (SEM bipe)
#   -> assets/<slug>-voz.m4a        voz do projeto (igual a limpa ate o scripts/bipe.py gravar o bipe)
#   -> work/full-clean.wav          mono 44,1 kHz, para a TRANSCRICAO (nunca leva bipe)
#   -> work/full.wav                mono 44,1 kHz, para o cuts.py (o bipe.py regrava com o bipe)
#   -> work/md5-bruto.txt           MD5 do bruto (conferir de novo no fim: o bruto nunca e alterado)
# RODAR SOZINHO: nunca junto com whisper nem com outro encode (o Air de 8 GB derruba o opendirectoryd).
set -e
BRUTO="$1"; SLUG="$2"
[ -f "$BRUTO" ] && [ -n "$SLUG" ] || { echo 'uso: zsh scripts/mezanino.sh "<bruto>" <slug>'; exit 1; }
cd "${0:A:h}/.."; mkdir -p assets work
md5 -q "$BRUTO" | tee work/md5-bruto.txt
P() { ffprobe -v error -select_streams v:0 -show_entries stream=$1 -of csv=p=0 "$BRUTO"; }
TRC=$(P color_transfer); RNG=$(P color_range); PIX=$(P pix_fmt)
echo "bruto: $(P codec_name) $(P width)x$(P height) @$(P r_frame_rate) · pix_fmt $PIX · range $RNG · transfer $TRC"
COMUM=(-c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -g 30 -keyint_min 30 -sc_threshold 0
       -color_range tv -colorspace bt709 -color_trc bt709 -color_primaries bt709 -an -movflags +faststart)
OUT="assets/$SLUG-2560-sdr.mp4"
if [[ "$TRC" == "arib-std-b67" || "$TRC" == "smpte2084" ]]; then
  # HDR do iPhone (HLG / BT.2020 10 bits). O ffmpeg local nao tem zscale: conversao pelo filtro colorspace.
  echo "-> HDR ($TRC): BT.2020 -> BT.709"
  ffmpeg -v error -stats -y -i "$BRUTO" -vf "colorspace=iall=bt2020:itrc=bt2020-10:all=bt709:format=yuv420p:dither=fsb" "${COMUM[@]}" "$OUT"
elif [[ "$RNG" == "pc" || "$PIX" == yuvj* ]]; then
  # SDR FULL-RANGE (o caso de quase todos os brutos): sem converter full->limited a cor lava.
  echo "-> SDR full-range: full -> limited"
  ffmpeg -v error -stats -y -i "$BRUTO" -vf "scale=in_range=full:out_range=tv,format=yuv420p" "${COMUM[@]}" "$OUT"
else
  echo "-> SDR limited: so reencode com GOP 30"
  ffmpeg -v error -stats -y -i "$BRUTO" -vf "format=yuv420p" "${COMUM[@]}" "$OUT"
fi
ffmpeg -v error -y -i "$BRUTO" -vn -c:a copy "work/$SLUG-voz-limpa.m4a"
cp "work/$SLUG-voz-limpa.m4a" "assets/$SLUG-voz.m4a"
ffmpeg -v error -y -i "work/$SLUG-voz-limpa.m4a" -ac 1 -ar 44100 -c:a pcm_s16le work/full-clean.wav
cp work/full-clean.wav work/full.wav
# Conferencia de cor: media e desvio-padrao de luminancia, bruto x mezanino, em 3 pontos.
# A media bate em ~1/255 e o desvio-padrao fica igual; se o desvio cair, a cor lavou.
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT")
for f in 0.1 0.5 0.9; do
  T=$(python3 -c "print(round($DUR*$f,2))")
  for src in "$BRUTO" "$OUT"; do
    ffmpeg -v error -y -ss $T -i "$src" -frames:v 1 -vf "scale=360:-2:out_range=pc,format=gray" -f rawvideo - | python3 -c "
import sys,numpy as np
a=np.frombuffer(sys.stdin.buffer.read(),dtype=np.uint8); print('  t=$T  media %.2f  desvio %.2f  %s'%(a.mean(),a.std(),'$src'.split('/')[-1]))"
  done
done
echo "mezanino: $OUT · $(ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of csv=p=0 "$OUT") quadros"
echo "no edit-plan.json: \"src\": \"$OUT\", \"voiceSrc\": \"assets/$SLUG-voz.m4a\""
