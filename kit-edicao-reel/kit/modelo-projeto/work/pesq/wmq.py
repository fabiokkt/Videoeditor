#!/usr/bin/env python3
# (reel Gordon Bethune, 2026-10-07) uso (de work/pesq): wmq.py "sub:Category:X" "wp:Titulo da Wikipedia" "busca por texto" ... -> q/wmq.json
# Consultas avulsas ao Commons (subcats + busca por texto em arquivos) honrando o retry-after do 429.
import json,urllib.request,urllib.parse,urllib.error,time,random,sys
UA='ReelPhotoResearch/1.0 (public-domain archive photo lookup)'
def api(p,host='commons.wikimedia.org'):
    u=f'https://{host}/w/api.php?'+urllib.parse.urlencode(p)
    for k in range(40):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60))
        except urllib.error.HTTPError as e:
            ra=int(e.headers.get('retry-after') or 20); w=ra+random.uniform(2,12); print(f'  429 -> espera {w:.0f}s',flush=True); time.sleep(w)
        except Exception as e: print('  erro',e,flush=True); time.sleep(15)
out={}
for a in sys.argv[1:]:
    if a.startswith('sub:'):
        j=api(dict(action='query',format='json',list='categorymembers',cmtitle=a[4:],cmlimit=500,cmtype='subcat'))
        out[a]=[x['title'] for x in j['query']['categorymembers']]
    elif a.startswith('wp:'):
        j=api(dict(action='query',format='json',prop='pageimages|images',titles=a[3:],piprop='original',imlimit=50),host='en.wikipedia.org')
        out[a]=j['query']['pages']
    else:
        j=api(dict(action='query',format='json',list='search',srsearch=a,srnamespace=6,srlimit=50))
        out[a]=[x['title'] for x in j['query']['search']]
    print(a,'->',json.dumps(out[a],ensure_ascii=False)[:1500],flush=True)
    time.sleep(5)
json.dump(out,open('q/wmq.json','w'),ensure_ascii=False,indent=1)
