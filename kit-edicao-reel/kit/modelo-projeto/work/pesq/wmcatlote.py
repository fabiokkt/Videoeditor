#!/usr/bin/env python3
# uso (de work/pesq): wmcatlote.py q/wm_<slug>.json "Category:A" "Category:B" ...   (reel Ernest Shackleton, 2026-10-07)
# Lista categorias do Commons com PACIENCIA: honra o retry-after do 429 (no container o Commons devolveu 429 em quase tudo por horas).
# 1 chamada por categoria (lista) + 1 por lote de 50 arquivos (imageinfo). Grava o formato do wm.py (+desc/date/artist/cat) -> usar com wmfila.py.
import sys, json, urllib.request, urllib.parse, urllib.error, re, time, random
UA='ReelPhotoResearch/1.0 (public-domain archive photo lookup)'
def api(p):
    u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(p)
    for k in range(40):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60))
        except urllib.error.HTTPError as e:
            ra=int(e.headers.get('retry-after') or 20); w=ra+random.uniform(2,12); print(f'  429 -> espera {w:.0f}s',flush=True); time.sleep(w)
        except Exception as e: print('  erro',e,flush=True); time.sleep(15)
    raise SystemExit('desisti')
out=sys.argv[1]; titles=[]; cats={}
for cat in sys.argv[2:]:
    j=api(dict(action='query',format='json',list='categorymembers',cmtitle=cat,cmlimit=500,cmtype='file|subcat'))
    m=j['query']['categorymembers']; fs=[x['title'] for x in m if x['ns']==6]; sc=[x['title'] for x in m if x['ns']==14]
    print(cat,len(fs),'arquivos; subcats:',[s[9:] for s in sc],flush=True)
    for t in fs:
        if t not in titles: titles.append(t); cats[t]=cat
    time.sleep(4)
recs=[]
for b in range(0,len(titles),50):
    j=api(dict(action='query',format='json',titles='|'.join(titles[b:b+50]),prop='imageinfo',iiprop='url|size|extmetadata',iiextmetadatafilter='LicenseShortName|ImageDescription|DateTimeOriginal|Artist|ObjectName'))
    for pg in j['query']['pages'].values():
        if 'imageinfo' not in pg: continue
        ii=pg['imageinfo'][0]; em=ii.get('extmetadata',{})
        cl=lambda k:re.sub(r'\s+',' ',re.sub('<[^>]+>','',em.get(k,{}).get('value','')))
        recs.append(dict(title=pg['title'],w=ii['width'],h=ii['height'],lic=cl('LicenseShortName'),url=ii['url'],page=ii['descriptionurl'],
                         desc=cl('ImageDescription')[:300],date=cl('DateTimeOriginal')[:40],artist=cl('Artist')[:60],cat=cats[pg['title']]))
    print('lote',b,flush=True); time.sleep(4)
recs.sort(key=lambda r:titles.index(r['title']))
for i,r in enumerate(recs): r['i']=i
json.dump(recs,open(out,'w'),indent=0,ensure_ascii=False)
for r in recs: print(r['i'],f"{r['w']}x{r['h']}",r['title'][5:90],'|',r['lic'],'|',r['date'][:20],'|',r['desc'][:110])
