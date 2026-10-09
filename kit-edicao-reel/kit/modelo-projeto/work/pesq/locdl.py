#!/usr/bin/env python3
# uso (de work/pesq): locdl.py <tag> <loc-item-url|digital-id ex fsa.8d10515> ...  -> loc/<tag>_<id>.jpg (maior arquivo: tif mestre ou v.jpg) + loc/licencas.tsv
import sys,json,urllib.request,os,io,re,time
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
def get(u,js=True):
    for k in range(3):
        try:
            d=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=180).read()
            return json.loads(d) if js else d
        except Exception as e: print('  erro',e,flush=True); time.sleep(8)
tag=sys.argv[1]; os.makedirs('loc',exist_ok=True)
for a in sys.argv[2:]:
    if a.startswith('http'):
        it=get(a.split('?')[0].rstrip('/')+'/?fo=json'); rid=[x for x in it['item'].get('digital_id',[]) if ' ' in x][0].split()[0:2]; rid='.'.join(rid)
        title=it['item'].get('title'); who=it['item'].get('contributor_names'); date=it['item'].get('date'); item=a
    else:
        rid=a; title=who=date=item=''
    j=get(f'https://www.loc.gov/resource/{rid}/?fo=json')
    if not j: print(rid,'sem recurso online'); continue
    files=[]
    for p in j.get('page') or []:
        files.append(p)
    tifs=sorted([f for f in files if f.get('mimetype')=='image/tiff'],key=lambda f:-(f.get('size') or 0))
    jp=[f for f in files if f.get('mimetype')=='image/jpeg']
    best=None
    if tifs and (tifs[0].get('size') or 0)>2_000_000: best=tifs[0]['url']
    if not best:
        jp=sorted(jp,key=lambda f:-(f.get('width') or 0)); best=jp[0]['url'] if jp else None
    if not best: print(rid,'sem arquivo'); continue
    d=get(best,js=False); im=Image.open(io.BytesIO(d)); im=im.convert('L' if im.mode in ('I;16','I;16B','I') else im.mode)
    if im.mode not in ('RGB','L'): im=im.convert('RGB')
    out=f'loc/{tag}_{rid.replace(".","-")}.jpg'; im.save(out,quality=93)
    print(rid,im.size,best.rsplit('/',1)[-1],'->',out,'|',(title or '')[:90],flush=True)
    with open('loc/licencas.tsv','a') as f: f.write(f'{out}\t{rid}\t{item}\t{date}\t{who}\t{title}\tLibrary of Congress, Prints & Photographs Division (dominio publico, sem restricoes conhecidas)\n')
