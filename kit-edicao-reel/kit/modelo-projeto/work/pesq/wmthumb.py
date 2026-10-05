#!/usr/bin/env python3
# uso: wmthumb.py <slug> <largura> <idx...> -> baixa a miniatura padrao (o original da 429 no container) -> raw/wm_<slug>_<i>.jpg
import sys,json,subprocess,time,urllib.request,urllib.parse
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
slug,W=sys.argv[1],int(sys.argv[2]); j=json.load(open(f'q/wm_{slug}.json'))
import os
lic=json.load(open('wm_lic.json')) if os.path.exists('wm_lic.json') else {}
for i in sys.argv[3:]:
    r=j[int(i)]; tag=f'wm_{slug}_{i}'
    u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(dict(action='query',format='json',titles=r['title'],prop='imageinfo',iiprop='url',iiurlwidth=W))
    for k in range(6):
        try: p=list(json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA})))['query']['pages'].values())[0]; break
        except Exception as e: print('api retry',e); time.sleep(15*(k+1))
    t=p['imageinfo'][0]['thumburl']
    for k in range(3):
        if subprocess.run(['python3','dl.py',tag,t,r['page'],'commons.wikimedia.org']).returncode==0: break
        time.sleep(10*(k+1))
    lic[tag]=dict(lic=r['lic'],title=r['title']); time.sleep(4)
json.dump(lic,open('wm_lic.json','w'),ensure_ascii=False,indent=0)
