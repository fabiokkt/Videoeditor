#!/bin/bash
# Entregas pedidas pelo usuario a partir do master (renders/Stanley-McChrystal-reel-final.mp4):
#  1) copia para o chat: 1440x2560 @60, x264 dois passes, < 30 MB
#  2) versao final: 1440x2560 @60, HEVC libx265 dois passes, tag hvc1, AAC 256k, +faststart, < 100 MB
#     (reel de 93,4 s < ~95 s: video a 8 Mbps; docs/05 §26)
#  3) comparacao: o mesmo quadro do master e da versao final, lado a lado (+ SSIM do video inteiro)
set -e; cd "$(dirname "$0")/.."
M=renders/Stanley-McChrystal-reel-final.mp4; N=Stanley-McChrystal; mkdir -p entrega; T=work/2pass; mkdir -p $T
VB=${VB:-8000k}; CB=${CB:-2000k}; QF=${QF:-780}   # QF = quadro da comparacao (13,0 s: o retrato de 2003 com o nome)
# 1) chat
ffmpeg -v error -y -i $M -c:v libx264 -preset slow -b:v $CB -pass 1 -passlogfile $T/x264 -pix_fmt yuv420p -g 120 -an -f mp4 /dev/null
ffmpeg -v error -y -i $M -c:v libx264 -preset slow -b:v $CB -pass 2 -passlogfile $T/x264 -pix_fmt yuv420p -g 120 \
  -color_range tv -colorspace bt709 -color_trc bt709 -color_primaries bt709 -c:a aac -b:a 160k -movflags +faststart entrega/$N-reel-chat.mp4
# 2) HEVC final
ffmpeg -v error -y -i $M -c:v libx265 -preset medium -b:v $VB -x265-params "pass=1:stats=$T/x265.log:log-level=error" -pix_fmt yuv420p -an -f mp4 /dev/null
ffmpeg -v error -y -i $M -c:v libx265 -preset medium -b:v $VB -x265-params "pass=2:stats=$T/x265.log:log-level=error" -pix_fmt yuv420p \
  -color_range tv -colorspace bt709 -color_trc bt709 -color_primaries bt709 -tag:v hvc1 -c:a aac -b:a 256k -ar 48000 -movflags +faststart \
  entrega/$N-reel-final.mp4
# 3) comparacao (quadro QF exato nos dois arquivos)
for f in $M entrega/$N-reel-final.mp4; do
  ffmpeg -v error -y -i $f -vf "select=eq(n\,$QF)" -frames:v 1 -update 1 $T/q-$(basename $f .mp4).png
done
SSIM=$(ffmpeg -v info -i entrega/$N-reel-final.mp4 -i $M -lavfi "[0:v][1:v]ssim" -f null - 2>&1 | grep -o "All:[0-9.]*" | tail -1)
python3 - "$T/q-$(basename $M .mp4).png" "$T/q-$N-reel-final.png" "$SSIM" "$QF" "$VB" <<'EOF'
import sys
from PIL import Image, ImageDraw, ImageFont
a,b=Image.open(sys.argv[1]).convert('RGB'),Image.open(sys.argv[2]).convert('RGB'); W,H=a.size
S=Image.new('RGB',(W*2+40,H+150),(17,20,26)); S.paste(a,(0,150)); S.paste(b,(W+40,150)); d=ImageDraw.Draw(S)
try: f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',54); g=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',38)
except Exception: f=g=ImageFont.load_default()
q=int(sys.argv[4]); vb=sys.argv[5].replace('k','')
d.text((30,20),'MASTER (H.264, render)',font=f,fill='white'); d.text((W+70,20),f'FINAL HEVC {int(vb)/1000:.1f} Mbps (2 passes)'.replace('.',','),font=f,fill='white')
d.text((30,88),f'quadro {q} · {q/60:.2f} s'.replace('.',','),font=g,fill=(170,176,188)); d.text((W+70,88),f'SSIM do video inteiro {sys.argv[3]}',font=g,fill=(170,176,188))
S.save('entrega/comparacao-master-x-hevc.jpg',quality=90)
EOF
echo "SSIM $SSIM"; ls -la entrega
