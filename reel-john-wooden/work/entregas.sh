#!/bin/bash
# Entregas pedidas pelo usuario a partir do master (renders/John-Wooden-reel-final.mp4):
#  1) copia para o chat: 1440x2560 @60, x264 dois passes, < 30 MB
#  2) versao final: 1440x2560 @60, HEVC libx265 dois passes ~8 Mbps de video, tag hvc1, AAC 256k, +faststart, < 100 MB
#     (89,4 s: 8 Mbps cabe; acima de ~95 s baixar VB)
#  3) comparacao: um quadro do master x o mesmo quadro da versao final, lado a lado (+ SSIM do video inteiro)
set -e; cd "$(dirname "$0")/.."
M=renders/John-Wooden-reel-final.mp4; mkdir -p entrega; T=work/2pass; mkdir -p $T
VB=${VB:-8000k}; CB=${CB:-2200k}; TQ=${TQ:-72.70}
# 1) chat
ffmpeg -v error -y -i $M -c:v libx264 -preset slow -b:v $CB -pass 1 -passlogfile $T/x264 -pix_fmt yuv420p -g 120 -an -f mp4 /dev/null
ffmpeg -v error -y -i $M -c:v libx264 -preset slow -b:v $CB -pass 2 -passlogfile $T/x264 -pix_fmt yuv420p -g 120 \
  -color_range tv -colorspace bt709 -color_trc bt709 -color_primaries bt709 -c:a aac -b:a 160k -movflags +faststart entrega/John-Wooden-reel-chat.mp4
# 2) HEVC final
ffmpeg -v error -y -i $M -c:v libx265 -preset medium -b:v $VB -x265-params "pass=1:stats=$T/x265.log:log-level=error" -pix_fmt yuv420p -an -f mp4 /dev/null
ffmpeg -v error -y -i $M -c:v libx265 -preset medium -b:v $VB -x265-params "pass=2:stats=$T/x265.log:log-level=error" -pix_fmt yuv420p \
  -color_range tv -colorspace bt709 -color_trc bt709 -color_primaries bt709 -tag:v hvc1 -c:a aac -b:a 256k -ar 48000 -movflags +faststart \
  entrega/John-Wooden-reel-final.mp4
# 3) comparacao lado a lado no mesmo quadro (TQ s) + SSIM
ffmpeg -v error -y -ss $TQ -i $M -frames:v 1 $T/q-master.png
ffmpeg -v error -y -ss $TQ -i entrega/John-Wooden-reel-final.mp4 -frames:v 1 $T/q-hevc.png
python3 - "$T/q-master.png" "$T/q-hevc.png" entrega/comparacao-master-x-hevc.jpg "$TQ" <<'PY'
import sys; from PIL import Image, ImageDraw, ImageFont
a,b=Image.open(sys.argv[1]).convert('RGB'),Image.open(sys.argv[2]).convert('RGB'); W,H=a.size; G=24; TOP=110
S=Image.new('RGB',(2*W+G,H+TOP),'white'); S.paste(a,(0,TOP)); S.paste(b,(W+G,TOP)); d=ImageDraw.Draw(S)
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',54)
d.text((30,26),f'MASTER (render) · {sys.argv[4]} s',fill='black',font=F); d.text((W+G+30,26),f'FINAL HEVC 8 Mbps · {sys.argv[4]} s',fill='black',font=F)
S.save(sys.argv[3],quality=90); print(sys.argv[3],S.size)
PY
ffmpeg -i entrega/John-Wooden-reel-final.mp4 -i $M -lavfi "[0:v][1:v]ssim" -f null - 2>&1 | grep -o "All:[0-9.]*" | tail -1
ls -la entrega
