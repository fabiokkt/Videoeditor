#!/usr/bin/env python3
# uso: wm.py "consulta" [n]  -> busca arquivos no Commons; imprime idx WxH titulo licenca ; salva q/wm_<slug>.json
import sys, json, urllib.request, urllib.parse, re, os
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
q=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 30
p=dict(action='query',format='json',generator='search',gsrsearch=q+' filetype:bitmap',gsrnamespace=6,gsrlimit=n,prop='imageinfo',iiprop='url|size|extmetadata',iiurlwidth=1920)
u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(p)
import time
for k in range(4):
    try: j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}))); break
    except Exception as e: print('retry',e); time.sleep(15*(k+1))
pages=sorted(j.get('query',{}).get('pages',{}).values(), key=lambda x:x.get('index',0))
out=[]
for i,pg in enumerate(pages):
  ii=pg['imageinfo'][0]; em=ii.get('extmetadata',{})
  lic=em.get('LicenseShortName',{}).get('value','')
  w,h=ii['width'],ii['height']
  rec=dict(i=i,title=pg['title'],w=w,h=h,lic=lic,url=ii['url'],thumb=ii.get('thumburl',ii['url']),page=ii['descriptionurl'])
  out.append(rec)
  if min(w,h)>=800: print(i,f'{w}x{h}',pg['title'][5:90],'|',lic)
slug=re.sub(r'\W+','_',q)[:40]
json.dump(out,open(f'q/wm_{slug}.json','w'),indent=0)
print('->',f'q/wm_{slug}.json')
