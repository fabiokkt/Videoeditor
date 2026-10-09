# (reel Michael Gerber, 2026-10-08) uso (de work/pesq): flsearch.py "consulta" [licencas=7] -> q/fl_<consulta>.json
# Busca no Flickr pela PAGINA de busca (modelExport), sem chave; licenca 7 = Flickr Commons (sem restricoes conhecidas: LOC, NARA, British Library...).
import sys,re,json,urllib.request,urllib.parse,html
q=sys.argv[1]; lic=sys.argv[2] if len(sys.argv)>2 else '7'
u='https://www.flickr.com/search/?'+urllib.parse.urlencode({'text':q,'license':lic})
t=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'}),timeout=60).read().decode('utf8','ignore')
i=t.find('modelExport: {')
if i<0: print('sem modelExport',len(t)); sys.exit()
d,_=json.JSONDecoder().raw_decode(t[i+13:])
def walk(o):
    if isinstance(o,dict):
        if isinstance(o.get('sizes'),dict) and 'id' in o: yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
seen=set(); out=[]
for p in walk(d):
    if p['id'] in seen: continue
    seen.add(p['id']); s=p['sizes'].get('data',p['sizes'])
    best=None
    for k in ('l','c','z'):
        if k in s: best=s[k].get('data',s[k]); break
    if not best: continue
    url=best.get('url') or best.get('displayUrl'); url=('https:'+url) if url.startswith('//') else url
    desc=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',p.get('description',''))))[:160]
    out.append(dict(id=p['id'],w=best.get('width'),h=best.get('height'),owner=p.get('username',''),title=html.unescape(p.get('title','')),url=url,desc=desc))
    print(p['id'], best.get('width'),'x',best.get('height'), p.get('username',''), '|', html.unescape(p.get('title',''))[:110], '|', url)
json.dump(out,open('q/fl_'+re.sub('[^a-z0-9]+','_',q.lower())+'.json','w'),ensure_ascii=False,indent=1)
