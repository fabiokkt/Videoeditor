#!/usr/bin/env python3
# uso: locmaster.py <saida.jpg> <digital-id ex fsac.1a35306 | fsa.8c02378>  -> mestre TIF (u/a) -> JPG <= 3200 px (apaga o tif)
import sys,urllib.request,os,io
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
out,rid=sys.argv[1],sys.argv[2]; col,n=rid.split('.')
d1=n[:-3]+'000'; d2=n[:-2]+'00'
# FSA: duas pastas (8b23000/8b23500); hec, mrg e outras: uma (26900, 00100) — reel Michael Gerber, docs/05 §36
for dirs,suf in [(f'{d1}/{d2}',x) for x in ('u','a')]+[(d2,x) for x in ('u','a')]:
    u=f'https://tile.loc.gov/storage-services/master/pnp/{col}/{dirs}/{n}{suf}.tif'
    try: data=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=600).read()
    except Exception as e: print(rid,suf,'falhou',e); continue
    if len(data)<3_000_000: continue
    im=Image.open(io.BytesIO(data))
    if im.mode in ('I;16','I;16B','I;16L','I'): im=im.point(lambda x:x*(1/256)).convert('L')
    if im.mode not in ('RGB','L'): im=im.convert('RGB')
    im.thumbnail((3200,3200),Image.LANCZOS); im.save(out,quality=93); print(rid,suf,len(data)//1_000_000,'MB ->',out,im.size,flush=True); break
