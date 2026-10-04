"""Folhas de conferencia MAIORES das janelas de leitura (gaze/tl-windows.json).
Por janela: [REF = quadro do mesmo take com olhar mais proximo da mediana] | 5 quadros de t0-0,1 a t1+0,1.
Recorte acompanha o rosto (centro dos olhos pelo FaceLandmarker), 640x250 px do mezanino -> 384x150.
Uso: gaze_review.py [saida=gaze/rev]"""
import json, cv2, sys, os, numpy as np, mediapipe as mp
from PIL import Image, ImageDraw, ImageFont
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
from _src import SRC
W=json.load(open('gaze/tl-windows.json')); T=[o for o in json.load(open('gaze/tl.json')) if o['ok']]
out=sys.argv[1] if len(sys.argv)>1 else 'gaze/rev'; os.makedirs(out,exist_ok=True)
ms=np.median([o['side'] for o in T]); md=np.median([o['down'] for o in T])
lmk=vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=mpt.BaseOptions(model_asset_path='.models/face_landmarker.task'),num_faces=1))
cap=cv2.VideoCapture(SRC); fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',24)
TW,TH=384,150
def frame(o,lab):
    cap.set(cv2.CAP_PROP_POS_MSEC,o['src']*1000); ok,f=cap.read()
    r=lmk.detect(mp.Image(image_format=mp.ImageFormat.SRGB,data=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)))
    if r.face_landmarks:
        L=r.face_landmarks[0]; cx=int(np.mean([L[i].x for i in (33,263)])*f.shape[1]); cy=int(np.mean([L[i].y for i in (33,133,362,263)])*f.shape[0])
    else: cx,cy=720,1330
    x0=max(0,min(f.shape[1]-640,cx-320)); y0=max(0,min(f.shape[0]-250,cy-125))
    c=cv2.resize(f[y0:y0+250,x0:x0+640],(TW,TH)); im=Image.fromarray(cv2.cvtColor(c,cv2.COLOR_BGR2RGB))
    d=ImageDraw.Draw(im); d.rectangle([0,0,len(lab)*14+6,28],fill=(0,0,0)); d.text((3,1),lab,font=fnt,fill=(255,255,0)); return im
rows=[]
for k,w in enumerate(W):
    seg=[o for o in T if o['seg']==w['seg'] and not (w['t0']-0.3<=o['t']<=w['t1']+0.3) and o['blink']<0.3]
    ref=min(seg or T,key=lambda o:abs(o['side']-ms)+abs(o['down']-md))
    ts=np.linspace(w['t0']-0.1,w['t1']+0.1,5)
    row=Image.new('RGB',(80+TW*6+10,TH),(16,16,20)); d=ImageDraw.Draw(row); d.text((4,55),f"w{k}",font=fnt,fill=(255,255,255))
    row.paste(frame(ref,f"REF {ref['t']:.2f}"),(80,0))
    for j,t in enumerate(ts):
        o=min(T,key=lambda x:abs(x['t']-t)); row.paste(frame(o,f"{o['t']:.2f}"),(80+TW*(j+1)+10,0))
    rows.append(row)
for g in range(0,len(rows),8):
    B=rows[g:g+8]; sh=Image.new('RGB',(B[0].width,(TH+4)*len(B)),(60,60,60))
    for j,r in enumerate(B): sh.paste(r,(0,j*(TH+4)))
    p=f"{out}/r{g//8:02d}.jpg"; sh.save(p,quality=88); print(p,f"w{g}-w{g+len(B)-1}")
