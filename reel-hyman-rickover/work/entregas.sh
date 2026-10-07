#!/bin/bash
# Entregas pedidas pelo usuario a partir do master (renders/Hyman-Rickover-reel-final.mp4):
#  1) copia para o chat: 1440x2560 @60, x264 dois passes, < 30 MB
#  2) versao final: 1440x2560 @60, HEVC libx265 dois passes ~8 Mbps de video, tag hvc1, AAC 256k, +faststart, < 100 MB
#  3) comparacao: um quadro do master x o mesmo quadro da versao final, lado a lado
set -e; cd "$(dirname "$0")/.."
M=renders/Hyman-Rickover-reel-final.mp4; mkdir -p entrega; T=work/2pass; mkdir -p $T
VB=${VB:-8000k}; CB=${CB:-2200k}
# 1) chat
ffmpeg -v error -y -i $M -c:v libx264 -preset slow -b:v $CB -pass 1 -passlogfile $T/x264 -pix_fmt yuv420p -g 120 -an -f mp4 /dev/null
ffmpeg -v error -y -i $M -c:v libx264 -preset slow -b:v $CB -pass 2 -passlogfile $T/x264 -pix_fmt yuv420p -g 120 \
  -color_range tv -colorspace bt709 -color_trc bt709 -color_primaries bt709 -c:a aac -b:a 160k -movflags +faststart entrega/Hyman-Rickover-reel-chat.mp4
# 2) HEVC final
ffmpeg -v error -y -i $M -c:v libx265 -preset medium -b:v $VB -x265-params "pass=1:stats=$T/x265.log:log-level=error" -pix_fmt yuv420p -an -f mp4 /dev/null
ffmpeg -v error -y -i $M -c:v libx265 -preset medium -b:v $VB -x265-params "pass=2:stats=$T/x265.log:log-level=error" -pix_fmt yuv420p \
  -color_range tv -colorspace bt709 -color_trc bt709 -color_primaries bt709 -tag:v hvc1 -c:a aac -b:a 256k -ar 48000 -movflags +faststart \
  entrega/Hyman-Rickover-reel-final.mp4
ls -la entrega
