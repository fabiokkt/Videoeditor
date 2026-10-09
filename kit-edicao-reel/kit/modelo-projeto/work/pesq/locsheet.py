#!/usr/bin/env python3
# uso: locsheet.py <tag> [max]  -> loc/sheet_<tag>.jpg (miniaturas 640 px rotuladas com o índice) a partir de loc/q_<tag>.json
import sys,json,urllib.request,io
from PIL import Image,ImageDraw,ImageFont
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
tag=sys.argv[1]; mx=int(sys.argv[2]) if len(sys.argv)>2 else 24
q=[r for r in json.load(open(f'loc/q_{tag}.json')) if r['img'] and '/item/' in (r['id'] or '')][:mx]
W=360; cells=[]
for r in q:
    u=r['img'].split('#')[0]
    for a,b in (('v.jpg','r.jpg'),):
        u=u.replace(a,b) if u.endswith(a) else u
    try:
        im=Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60).read())).convert('RGB')
    except Exception as e: print('erro',r['i'],e); continue
    im.thumbnail((W,W)); c=Image.new('RGB',(W,W+22),(30,30,30)); c.paste(im,((W-im.width)//2,0))
    d=ImageDraw.Draw(c); d.text((4,W+4),f"{r['i']} {r['date'][:4]} {r['title'][:48]}",fill=(255,255,0)); cells.append(c)
n=len(cells); cols=6; rows=(n+cols-1)//cols
S=Image.new('RGB',(cols*W,rows*(W+22)),(0,0,0))
for k,c in enumerate(cells): S.paste(c,((k%cols)*W,(k//cols)*(W+22)))
S.save(f'loc/sheet_{tag}.jpg',quality=85); print(f'loc/sheet_{tag}.jpg',n)
