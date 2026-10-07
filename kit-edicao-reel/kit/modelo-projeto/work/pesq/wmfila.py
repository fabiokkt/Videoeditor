#!/usr/bin/env python3
# uso (de work/pesq): wmfila.py <slug> <idx,...>  -> raw/wm_<slug>_<i>.jpg + wm_lic.json   (reel Ernest Shackleton, 2026-10-07)
# Variante do wmstd.py: largura padrao pelo tamanho do original (1920 / 1280 / 960) e ate 8 tentativas com espera crescente (429).
# A fila e a ordem dos indices: passar primeiro o que falta no layout; matar o laco por PID (nunca pkill -f com o proprio texto).
import sys, json, os, time, subprocess, random
slug, ids = sys.argv[1], sys.argv[2]
lic = json.load(open('wm_lic.json')) if os.path.exists('wm_lic.json') else {}
j = json.load(open(f'q/wm_{slug}.json'))
for i in ids.split(','):
    r = j[int(i)]; tag = f'wm_{slug}_{i}'
    if os.path.exists(f'raw/{tag}.jpg'): continue
    base, name = r['url'].split('?')[0].rsplit('/', 1)
    w = 1920 if r['w'] > 1920 else 1280 if r['w'] > 1280 else 960
    t = base.replace('/commons/', '/commons/thumb/') + f'/{name}/{w}px-{name}'
    if name.lower().endswith(('.tif', '.tiff')): t += '.jpg'
    if name.lower().endswith('.png'): t = t  # png thumb mantem png
    ok = False
    for k in range(8):
        if subprocess.run(['python3', 'dl.py', tag, t, r['page'], 'commons.wikimedia.org']).returncode == 0: ok = True; break
        time.sleep(20 + random.uniform(0, 10) + 10 * k)
    if ok:
        lic[tag] = dict(lic=r['lic'], title=r['title'], page=r['page'], date=r.get('date', ''), artist=r.get('artist', ''))
        json.dump(lic, open('wm_lic.json', 'w'), ensure_ascii=False, indent=0)
    time.sleep(3)
