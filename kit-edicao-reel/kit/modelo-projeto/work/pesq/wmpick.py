#!/usr/bin/env python3
# uso: wmpick.py <slug> <idx...> -> raw/wm_<slug>_<i>.jpg (original; tif/png convertidos), registra em g_index.json com lic
import sys,json,subprocess,time
slug=sys.argv[1]; j=json.load(open(f'q/wm_{slug}.json'))
lic=json.load(open('wm_lic.json')) if __import__('os').path.exists('wm_lic.json') else {}
for i in sys.argv[2:]:
    r=j[int(i)]; tag=f'wm_{slug}_{i}'
    u=r['url'] if r['url'].lower().endswith(('.jpg','.jpeg','.png')) and r['w']*r['h']<40e6 else r['thumb']
    subprocess.run(['python3','dl.py',tag,u,r['page'],'commons.wikimedia.org'])
    lic[tag]=dict(lic=r['lic'],title=r['title']); time.sleep(3)
json.dump(lic,open('wm_lic.json','w'),ensure_ascii=False,indent=0)
