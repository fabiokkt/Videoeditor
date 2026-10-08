#!/usr/bin/env python3
# uso: wmtitles.py q/wm_<slug>.json titulos.txt  -> mesmo formato do wmcatlote.py (para o wmfila.py), honrando o 429.
import sys,json,re,time,random,urllib.request,urllib.parse,urllib.error
UA='ReelPhotoResearch/1.0 (public-domain archive photo lookup)'
def api(p):
    u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(p)
    for k in range(40):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60))
        except urllib.error.HTTPError as e:
            ra=int(e.headers.get('retry-after') or 20); w=ra+random.uniform(2,12); print(f'  429 -> espera {w:.0f}s',flush=True); time.sleep(w)
        except Exception as e: print('  erro',e,flush=True); time.sleep(15)
out=sys.argv[1]; titles=[l.strip() for l in open(sys.argv[2]) if l.strip()]
recs=[]
for b in range(0,len(titles),50):
    j=api(dict(action='query',format='json',titles='|'.join(titles[b:b+50]),prop='imageinfo',iiprop='url|size|extmetadata',iiextmetadatafilter='LicenseShortName|ImageDescription|DateTimeOriginal|Artist|ObjectName'))
    for pg in j['query']['pages'].values():
        if 'imageinfo' not in pg: print('sem info',pg.get('title')); continue
        ii=pg['imageinfo'][0]; em=ii.get('extmetadata',{})
        cl=lambda k:re.sub(r'\s+',' ',re.sub('<[^>]+>','',em.get(k,{}).get('value','')))
        recs.append(dict(title=pg['title'],w=ii['width'],h=ii['height'],lic=cl('LicenseShortName'),url=ii['url'],page=ii['descriptionurl'],
                         desc=cl('ImageDescription')[:300],date=cl('DateTimeOriginal')[:40],artist=cl('Artist')[:60],cat='titles'))
    time.sleep(4)
recs.sort(key=lambda r:titles.index(r['title']) if r['title'] in titles else 999)
for i,r in enumerate(recs): r['i']=i
json.dump(recs,open(out,'w'),indent=0,ensure_ascii=False)
for r in recs: print(r['i'],f"{r['w']}x{r['h']}",r['title'][5:90],'|',r['lic'],'|',r['date'][:20],'|',r['artist'][:30],'|',r['desc'][:120])
