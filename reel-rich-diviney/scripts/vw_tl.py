"""Folhas de conferencia das janelas de leitura (gaze/tl-windows.json): 1 linha por janela, quadros
da faixa dos olhos de t0-0.2 a t1+0.2 (tempos de TIMELINE, rotulados). Uso: vw_tl.py [saida] [i0 i1]"""
import json, cv2, sys, os, numpy as np
from PIL import Image, ImageDraw, ImageFont
from _src import SRC  # recorte dos olhos: reel KAZUO INAMORI, olhos em y~1220-1260, x~580-900 do 1440x2560
W=json.load(open('gaze/tl-windows.json')); T=[o for o in json.load(open('gaze/tl.json')) if o['ok']]
out=sys.argv[1] if len(sys.argv)>1 else 'gaze/tlw'; os.makedirs(out,exist_ok=True)
i0,i1=(int(sys.argv[2]),int(sys.argv[3])) if len(sys.argv)>3 else (0,len(W))
cap=cv2.VideoCapture(SRC); fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',22)
def frame(t):
    o=min(T,key=lambda x:abs(x['t']-t)); cap.set(cv2.CAP_PROP_POS_MSEC,o['src']*1000); ok,f=cap.read()
    c=f[1100:1380,380:1100]; c=cv2.resize(c,(300,117)); im=Image.fromarray(cv2.cvtColor(c,cv2.COLOR_BGR2RGB))
    d=ImageDraw.Draw(im); lab=f"{t:.2f}"; d.rectangle([0,0,70,24],fill=(0,0,0)); d.text((3,0),lab,font=fnt,fill=(255,255,0)); return im
COLS=8; rows=[]
for k in range(i0,min(i1,len(W))):
    w=W[k]; a,b=w['t0']-0.2,w['t1']+0.2; ts=list(np.linspace(a,b,COLS))
    row=Image.new('RGB',(300*COLS+90,117),(16,16,20)); d=ImageDraw.Draw(row); d.text((4,40),f"w{k}",font=fnt,fill=(255,255,255))
    for j,t in enumerate(ts): row.paste(frame(t),(90+300*j,0))
    rows.append(row)
for g in range(0,len(rows),9):
    B=rows[g:g+9]; sh=Image.new('RGB',(B[0].width,117*len(B)+4*(len(B)-1)),(60,60,60))
    for j,r in enumerate(B): sh.paste(r,(0,j*121))
    p=f"{out}/s{(i0+g)//9:02d}.jpg"; sh.save(p,quality=88); print(p, f"w{i0+g}-w{i0+g+len(B)-1}")
