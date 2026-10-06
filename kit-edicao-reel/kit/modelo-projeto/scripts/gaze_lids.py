"""Leitura do roteiro para BAIXO (padrão do reel André Esteves): cabeça abaixa e a pálpebra
cobre a íris. Métrica: op (abertura do olho) relativa ao começo do PRÓPRIO take (0,15–0,7 s,
quando ele está de olhos abertos na câmera). Sustentado >= 0,24 s abaixo de LIM = desvio
(piscada dura menos). Imprime início do desvio (source) e quanto antes do out ele começa."""
import json, numpy as np, sys
M=[o for o in json.load(open('gaze/measure.json')) if o.get('ok')]
P=json.load(open('assets/edit-plan.json')); LIM=float(sys.argv[1]) if len(sys.argv)>1 else 0.72
res=[]
for i,s in enumerate(P['segments']):
    st=[o['op'] for o in M if s['in']+0.15<=o['t']<=s['in']+0.7]
    ref=np.percentile(st,70)
    xs=[o for o in M if s['in']<=o['t']<=s['out']]
    runs=[];cur=None
    for o in xs:
        if o['op']<LIM*ref: cur=[o['t'],o['t']] if cur is None else [cur[0],o['t']]
        else:
            if cur and cur[1]-cur[0]>=0.24: runs.append(cur)
            cur=None
    if cur and cur[1]-cur[0]>=0.16: runs.append(cur)
    res.append({"seg":i,"label":s['label'],"runs":[[round(a,2),round(b,2)] for a,b in runs]})
    print(f"{i:2} {s['label']:<12} {s['in']:6.2f}-{s['out']:6.2f} "+'  '.join(f"{a:.2f}-{b:.2f}(fim-{s['out']-a:.2f})" for a,b in runs))
json.dump(res,open('gaze/lids.json','w'),indent=1)
