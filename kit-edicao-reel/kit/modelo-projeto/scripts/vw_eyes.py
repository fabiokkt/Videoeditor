"""Olhos em ZOOM (tempos de TIMELINE, rotulados) para tirar duvida de leitura x movimento de cabeca. Uso: vw_eyes.py saida.jpg t1 t2 ..."""
import json, cv2, sys
from PIL import Image, ImageDraw, ImageFont
from _src import SRC
T=[o for o in json.load(open('gaze/tl.json')) if o['ok']]
cap=cv2.VideoCapture(SRC); fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',24)
ims=[]
for t in [float(x) for x in sys.argv[2:]]:
    o=min(T,key=lambda x:abs(x['t']-t)); cap.set(cv2.CAP_PROP_POS_MSEC,o['src']*1000); ok,f=cap.read()
    c=cv2.resize(f[1060:1420,340:1140],(500,225)); im=Image.fromarray(cv2.cvtColor(c,cv2.COLOR_BGR2RGB))
    d=ImageDraw.Draw(im); d.rectangle([0,0,150,28],fill=(0,0,0)); d.text((4,1),f"{t:.2f} s{o['side']:+.2f} d{o['down']:.2f}",font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',15),fill=(255,255,0)); ims.append(im)
C=4; R=(len(ims)+C-1)//C; sh=Image.new('RGB',(500*C,225*R),(20,20,20))
for k,im in enumerate(ims): sh.paste(im,(500*(k%C),225*(k//C)))
sh.save(sys.argv[1],quality=90); print(sys.argv[1])
