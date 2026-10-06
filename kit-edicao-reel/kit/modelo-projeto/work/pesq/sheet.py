#!/usr/bin/env python3
# uso: sheet.py <out.jpg> <glob...>  -> grade de miniaturas rotuladas
import sys,glob,os
from PIL import Image,ImageDraw,ImageFont
out=sys.argv[1]; files=[]
def key(p):
    b=os.path.basename(p)[:-4]; a,_,n=b.rpartition('-')
    return (a,int(n) if n.isdigit() else 0)
for g in sys.argv[2:]: files+=glob.glob(g)
files=sorted(set(files),key=key)
C=4; TW,TH=420,420
rows=(len(files)+C-1)//C
S=Image.new('RGB',(C*TW,rows*(TH+30)),'white'); d=ImageDraw.Draw(S)
try: F=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',22)
except: F=None
for k,f in enumerate(files):
    try: im=Image.open(f); w,h=im.size; im=im.convert('RGB'); im.thumbnail((TW-8,TH-8))
    except Exception as e: continue
    x=(k%C)*TW; y=(k//C)*(TH+30)
    S.paste(im,(x+(TW-im.width)//2,y+(TH-im.height)//2))
    d.text((x+6,y+TH+2),f"{os.path.basename(f)[:-4]}  {w}x{h}",fill='black',font=F)
S.save(out,quality=85); print(out,len(files))
