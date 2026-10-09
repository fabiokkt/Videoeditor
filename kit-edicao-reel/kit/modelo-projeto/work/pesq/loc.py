#!/usr/bin/env python3
# uso (de work/pesq): loc.py <tag> "consulta" [n] [cor|pb|foto] -> loc/q_<tag>.json + lista. cor/pb = colecoes FSA/OWI (dominio publico), foto = busca geral (reel Bob Chapman, docs/05 §35)
import sys,json,urllib.request,urllib.parse,time
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
tag,q=sys.argv[1],sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 25
fa=sys.argv[4] if len(sys.argv)>4 else 'online-format:image'
base={'cor':'collections/fsa-owi-color-photographs','pb':'collections/fsa-owi-black-and-white-negatives','foto':'photos'}.get(fa,'photos')
u=f'https://www.loc.gov/{base}/?'+urllib.parse.urlencode(dict(q=q,fo='json',c=n))
for k in range(5):
    try: j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60)); break
    except Exception as e: print('erro',e); time.sleep(10)
out=[]
for i,r in enumerate(j.get('results',[])):
    imgs=r.get('image_url') or []
    rec=dict(i=i,title=r.get('title'),date=r.get('date'),id=r.get('id'),img=imgs[-1] if imgs else '',rights=(r.get('rights') or r.get('rights_advisory') or ''),partof=[p for p in (r.get('partof') or []) if 'farm' in p.lower() or 'office of war' in p.lower() or 'documerica' in p.lower()][:1])
    out.append(rec); print(i,'|',rec['date'],'|',(rec['title'] or '')[:120],'|',rec['partof'],'|',rec['id'])
json.dump(out,open(f'loc/q_{tag}.json','w'),ensure_ascii=False,indent=1)
