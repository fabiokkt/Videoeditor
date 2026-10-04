"""Quadros grandes (rosto) em tempos de TIMELINE, rotulados. Uso: vw_big.py saida.jpg t1 t2 ..."""
import json, cv2, sys
from PIL import Image, ImageDraw, ImageFont
from _src import SRC
T=[o for o in json.load(open('gaze/tl.json')) if o['ok']]
cap=cv2.VideoCapture(SRC); fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',26)
ts=[float(x) for x in sys.argv[2:]]; ims=[]
for t in ts:
    o=min(T,key=lambda x:abs(x['t']-t)); cap.set(cv2.CAP_PROP_POS_MSEC,o['src']*1000); ok,f=cap.read()
    c=cv2.resize(f[1000:1700,300:1200],(360,280)); im=Image.fromarray(cv2.cvtColor(c,cv2.COLOR_BGR2RGB))
    d=ImageDraw.Draw(im); d.rectangle([0,0,86,30],fill=(0,0,0)); d.text((4,1),f"{t:.2f}",font=fnt,fill=(255,255,0)); ims.append(im)
C=6; R=(len(ims)+C-1)//C; sh=Image.new('RGB',(360*C,280*R),(20,20,20))
for k,im in enumerate(ims): sh.paste(im,(360*(k%C),280*(k//C)))
sh.save(sys.argv[1],quality=88); print(sys.argv[1])
