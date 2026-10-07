"""Janelas de leitura de roteiro na timeline a partir de gaze/tl.json (gaze_tl.py).
Suspeito = |side - mediana| > SIDE ou down - mediana > DOWN, sem piscada, sustentado >= MIN s.
Imprime as janelas (timeline) e grava gaze/tl-windows.json. E pista: confirmar nas faixas (vw_tl.py)."""
import json, numpy as np, sys
M=[o for o in json.load(open('gaze/tl.json')) if o['ok']]
SIDE=float(sys.argv[1]) if len(sys.argv)>1 else 0.17
DOWN=float(sys.argv[2]) if len(sys.argv)>2 else 0.11
MIN=0.15
ms=np.median([o['side'] for o in M]); md=np.median([o['down'] for o in M])
def flag(o): return o['blink']<0.4 and (abs(o['side']-ms)>SIDE or o['down']-md>DOWN)
W=[];cur=None
for o in M:
    if flag(o):
        if cur and o['t']-cur[1]<=0.1: cur[1]=o['t']; cur[2].append(o)
        else:
            if cur: W.append(cur)
            cur=[o['t'],o['t'],[o]]
if cur: W.append(cur)
W=[w for w in W if w[1]-w[0]>=MIN]
res=[]
for a,b,os_ in W:
    sd=np.mean([o['side'] for o in os_])-ms; dn=np.mean([o['down'] for o in os_])-md
    res.append({"t0":round(a,2),"t1":round(b+0.033,2),"seg":os_[0]['seg'],"side":round(float(sd),3),"down":round(float(dn),3)})
    print(f"{a:6.2f}-{b+0.033:6.2f} ({b-a+0.033:.2f}s) seg{os_[0]['seg']:>2}  side{sd:+.2f} down{dn:+.2f}")
json.dump(res,open('gaze/tl-windows.json','w'),indent=1)
print(f"{len(res)} janelas, {sum(r['t1']-r['t0'] for r in res):.1f}s (mediana side {ms:+.3f} down {md:.3f})")
