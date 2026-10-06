#!/usr/bin/env python3
# uso: wmstd.py <largura> <slug>:<idx>[,<idx>] ...  -> raw/wm_<slug>_<i>.jpg pela miniatura de TAMANHO PADRAO (960/1280/1920),
# montada da URL original de q/wm_<slug>.json — sem nova chamada a API por arquivo (reel John Wooden, 2026-10-06).
# Por que: o wmthumb.py pede a URL de cada arquivo a API e, depois de umas 20 buscas, a API passa a devolver 429 em tudo; e o
# 'thumb' gravado pelo wm.py vira o ORIGINAL quando a largura pedida passa a do arquivo (429 tambem). A URL vem com "?utm_..." -> cortar.
import sys, json, os, time, subprocess
W = int(sys.argv[1]); lic = json.load(open('wm_lic.json')) if os.path.exists('wm_lic.json') else {}
for arg in sys.argv[2:]:
    slug, ids = arg.split(':'); j = json.load(open(f'q/wm_{slug}.json'))
    for i in ids.split(','):
        r = j[int(i)]; tag = f'wm_{slug}_{i}'
        if os.path.exists(f'raw/{tag}.jpg'): continue
        base, name = r['url'].split('?')[0].rsplit('/', 1)
        w = W if r['w'] > W else 960                      # tamanhos padrao (https://w.wiki/GHai); fora deles a 429 vem mais cedo
        t = base.replace('/commons/', '/commons/thumb/') + f'/{name}/{w}px-{name}'
        if name.lower().endswith(('.tif', '.tiff')): t += '.jpg'
        for k in range(3):
            if subprocess.run(['python3', 'dl.py', tag, t, r['page'], 'commons.wikimedia.org']).returncode == 0: break
            time.sleep(10 * (k + 1))
        lic[tag] = dict(lic=r['lic'], title=r['title'], page=r['page'])
        json.dump(lic, open('wm_lic.json', 'w'), ensure_ascii=False, indent=0)
        time.sleep(3)
