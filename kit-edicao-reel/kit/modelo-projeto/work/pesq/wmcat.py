#!/usr/bin/env python3
# uso: wmcat.py "Category:Nome" [n]  -> lista ARQUIVOS da categoria do Commons (generator=categorymembers, docs/05 §29)
# mesmo formato do wm.py: q/wm_<slug>.json (titulo, tamanho, licenca, url, descricao curta) ; imprime idx WxH titulo | licenca | data
import sys, json, urllib.request, urllib.parse, re, time, html
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
cat=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 100
p=dict(action='query',format='json',generator='categorymembers',gcmtitle=cat,gcmtype='file',gcmlimit=min(n,50),prop='imageinfo',iiprop='url|size|extmetadata',iiurlwidth=1280)
u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(p)
def get(u):
    for k in range(4):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA})))
        except Exception as e: print('retry',e); time.sleep(15*(k+1))
allp={}; cont={}
while True:
    j=get(u+('&'+urllib.parse.urlencode(cont) if cont else ''))
    for pid,pg in j.get('query',{}).get('pages',{}).items():
        if 'imageinfo' in pg: allp[pid]=pg
        else: allp.setdefault(pid,pg)
    if 'continue' not in j or len(allp)>=n: break
    cont=j['continue']; time.sleep(2)
pages=sorted([p for p in allp.values() if 'imageinfo' in p], key=lambda x:x['title'])
out=[]
def clean(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',s or ''))).strip()
for i,pg in enumerate(pages):
  ii=pg['imageinfo'][0]; em=ii.get('extmetadata',{})
  lic=em.get('LicenseShortName',{}).get('value','')
  desc=clean(em.get('ImageDescription',{}).get('value',''))[:160]
  date=clean(em.get('DateTimeOriginal',{}).get('value',''))[:20]
  w,h=ii['width'],ii['height']
  out.append(dict(i=i,title=pg['title'],w=w,h=h,lic=lic,url=ii['url'],thumb=ii.get('thumburl',ii['url']),page=ii['descriptionurl'],desc=desc,date=date))
  print(i,f'{w}x{h}',pg['title'][5:80],'|',lic,'|',date,'|',desc[:110])
slug=re.sub(r'\W+','_',cat.replace('Category:',''))[:40]
json.dump(out,open(f'q/wm_{slug}.json','w'),indent=0,ensure_ascii=False)
print('->',f'q/wm_{slug}.json')
