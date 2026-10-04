"""Olhar PARA BAIXO (leitura do roteiro) nas bordas de cada take — o gx do gaze_report só vê
desvio lateral. Usa a abertura do olho (op) de gaze/measure.json: olhar para baixo baixa a
pálpebra por vários quadros seguidos; piscada dura < 0,2 s.
Imprime, por take, a faixa do source em que op < LIM x mediana do próprio take (>= 0,24 s)."""
import json, numpy as np, sys
M=[o for o in json.load(open('gaze/measure.json')) if o.get('ok')]
plan=json.load(open('assets/edit-plan.json'))
LIM=float(sys.argv[1]) if len(sys.argv)>1 else 0.8
for i,s in enumerate(plan['segments']):
    xs=[o for o in M if s['in']-0.05<=o['t']<=s['out']+0.05]
    if not xs: continue
    med=np.median([o['op'] for o in xs])
    runs=[];cur=None
    for o in xs:
        low=o['op']<LIM*med
        if low: cur=[o['t'],o['t']] if cur is None else [cur[0],o['t']]
        else:
            if cur and cur[1]-cur[0]>=0.24: runs.append(cur)
            cur=None
    if cur and cur[1]-cur[0]>=0.24: runs.append(cur)
    tags=[]
    for a,b in runs:
        pos='INICIO' if a-s['in']<0.5 else ('FIM' if s['out']-b<1.0 else 'meio')
        tags.append(f"{a:.2f}-{b:.2f}({pos})")
    if tags: print(f"{i:2} {s['label']:<12} in {s['in']:.2f} out {s['out']:.2f} | "+'  '.join(tags))
