#!/bin/bash
# MOTOR (kit v3.1). Entregas a partir do master renders/<Nome>-reel-final.mp4 (pedido do usuario desde o reel Mike Abrashoff):
#  1) copia para o chat: 1440x2560 @60, x264 dois passes, < 30 MB          -> entrega/<Nome>-reel-chat.mp4
#  2) versao final: HEVC libx265 dois passes, ~8 Mbps de video, tag hvc1, AAC 256k, +faststart, < 100 MB
#     (acima de ~95 s o video desce para caber: docs/05 §26)                  -> entrega/<Nome>-reel-final.mp4
#  3) o mesmo quadro do master e da versao final lado a lado + SSIM do video inteiro -> entrega/comparacao-master-x-hevc.jpg
# A copia do chat (1) codifica EM PARALELO com o HEVC (2) com >= 12 GB e >= 8 nucleos. No container de 4 nucleos fica em serie:
# x265 sozinho ja usa 330-384% e x264 377-387% dos 4 nucleos (medido no reel Ridgway, docs/05 §32). PARALELO=0/1 forca. VB/CB/QF por variavel de ambiente.
# uso: bash work/entregas.sh <Nome>        (ex.: bash work/entregas.sh Matthew-Ridgway; rodar como tarefa de fundo)
set -e; cd "$(dirname "$0")/.."
N=${1:?uso: bash work/entregas.sh <Nome>}; M=renders/$N-reel-final.mp4; [ -f $M ] || { echo "falta $M"; exit 1; }
mkdir -p entrega; T=work/2pass; mkdir -p $T; T0=$(date +%s)
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $M)
# bitrate que cabe: final 96 MB (teto 8 Mbps), chat 28 MB (teto 3 Mbps) — o 2 passes erra < 1% e o AAC vem ~5% acima do pedido
VB=${VB:-$(python3 -c "print(min(8000, int(((96e6*8/$DUR)-270e3)/1e5)*100))")k}
CB=${CB:-$(python3 -c "print(min(3000, int(((28e6*8/$DUR)-170e3)/1e5)*100))")k}
QF=${QF:-$(python3 -c "print(round($DUR*0.133*60))")}     # quadro da comparacao (padrao: ~13% do reel, logo depois da revelacao)
echo "$N: ${DUR}s -> HEVC $VB · chat $CB · comparacao no quadro $QF"
COR=(-color_range tv -colorspace bt709 -color_trc bt709 -color_primaries bt709)
chat() {
  ffmpeg -v error -y -i $M -c:v libx264 -preset slow -b:v $CB -pass 1 -passlogfile $T/x264 -pix_fmt yuv420p -g 120 -an -f mp4 /dev/null
  ffmpeg -v error -y -i $M -c:v libx264 -preset slow -b:v $CB -pass 2 -passlogfile $T/x264 -pix_fmt yuv420p -g 120 \
    "${COR[@]}" -c:a aac -b:a 160k -movflags +faststart entrega/$N-reel-chat.mp4
  echo "chat pronto · $(( $(date +%s)-T0 ))s"
}
hevc() {
  ffmpeg -v error -y -i $M -c:v libx265 -preset medium -b:v $VB -x265-params "pass=1:stats=$T/x265.log:log-level=error" -pix_fmt yuv420p -an -f mp4 /dev/null
  ffmpeg -v error -y -i $M -c:v libx265 -preset medium -b:v $VB -x265-params "pass=2:stats=$T/x265.log:log-level=error" -pix_fmt yuv420p \
    "${COR[@]}" -tag:v hvc1 -c:a aac -b:a 256k -ar 48000 -movflags +faststart entrega/$N-reel-final.mp4
  echo "HEVC pronto · $(( $(date +%s)-T0 ))s"
}
MEM=$( (sysctl -n hw.memsize 2>/dev/null || awk '/MemTotal/{print $2*1024}' /proc/meminfo) | awk '{print int($1/1073741824+0.5)}')
NC=$(sysctl -n hw.ncpu 2>/dev/null || nproc)
PAR=${PARALELO:-$([ "$MEM" -ge 12 ] && [ "$NC" -ge 8 ] && echo 1 || echo 0)}
if [ "$PAR" = 1 ]; then chat & CP=$!; hevc; wait $CP; else chat; hevc; fi
# 3) comparacao: o quadro QF exato nos dois arquivos + SSIM do video inteiro
for f in $M entrega/$N-reel-final.mp4; do ffmpeg -v error -y -i $f -vf "select=eq(n\,$QF)" -frames:v 1 -update 1 $T/q-$(basename $f .mp4).png; done
SSIM=$(ffmpeg -v info -i entrega/$N-reel-final.mp4 -i $M -lavfi "[0:v][1:v]ssim" -f null - 2>&1 | grep -o "All:[0-9.]*" | tail -1 | cut -d: -f2)
python3 - "$T/q-$N-reel-final.png" "$T/q-$(basename $M .mp4).png" "$SSIM" "$QF" "$VB" <<'EOF'
import sys
from PIL import Image, ImageDraw, ImageFont
b, a = Image.open(sys.argv[1]).convert('RGB'), Image.open(sys.argv[2]).convert('RGB'); W, H = a.size
S = Image.new('RGB', (W * 2 + 40, H + 150), (17, 20, 26)); S.paste(a, (0, 150)); S.paste(b, (W + 40, 150)); d = ImageDraw.Draw(S)
try: f = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 54); g = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 38)
except Exception: f = g = ImageFont.load_default()
q = int(sys.argv[4]); vb = int(sys.argv[5].rstrip('k')) / 1000
d.text((30, 20), 'MASTER (H.264, render)', font=f, fill='white'); d.text((W + 70, 20), f'FINAL HEVC {vb:.1f} Mbps (2 passes)'.replace('.', ','), font=f, fill='white')
d.text((30, 88), f'quadro {q} · {q / 60:.2f} s'.replace('.', ','), font=g, fill=(170, 176, 188))
d.text((W + 70, 88), f'SSIM do vídeo inteiro {float(sys.argv[3]):.3f}'.replace('.', ','), font=g, fill=(170, 176, 188))
S.save('entrega/comparacao-master-x-hevc.jpg', quality=90)
EOF
for f in entrega/$N-reel-chat.mp4 entrega/$N-reel-final.mp4; do
  echo "$f: $(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,codec_tag_string,width,height,r_frame_rate,nb_frames -of csv=p=0 $f) · $(( $(stat -c %s $f 2>/dev/null || stat -f %z $f) / 1000000 )) MB"
done
echo "SSIM do video inteiro $SSIM · entregas em $(( $(date +%s)-T0 ))s"
