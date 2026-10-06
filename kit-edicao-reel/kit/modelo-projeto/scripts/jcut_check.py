"""Validacao do J-cut por dados (work/mix-plan.json + work/segs.json + plano):
 - cobertura da voz sem buracos; crossfade inteiro no silencio (nem sobre a ultima palavra nem sobre a primeira);
 - LEAD DE FALA = corte de imagem - inicio da 1a palavra do take seguinte (quadros a 30 fps). Alvo: 5 f.
 - respiro = silencio entre a ultima palavra de um take e a primeira do seguinte (timeline)."""
import json, statistics as st
P=json.load(open('assets/edit-plan.json')); M=json.load(open('work/mix-plan.json')); S=json.load(open('work/segs.json'))
R=P['rate']; F=1/30; LEAD=P.get('jcutLeadFrames',5)*F; V=M['voice']; t=0; T=[]
for i,s in enumerate(P['segments']):
    sd=(s['out']-s['in'])/R; lead=0 if i==0 else min(LEAD,sd-10*F); T.append((t,t-lead)); t+=sd-lead
holes=0; bad=[]; sl=[]; resp=[]
for k in range(len(V)-1):
    a,b=V[k],V[k+1]
    if b['start']>a['start']+a['dur']+1e-3: holes+=1
    if a['in']+a['dur']*R-a['xfade']*R < S[k]['off']-1e-3: bad.append((k,'fim'))
    if b['in']+b['xfade']*R > S[k+1]['on']+1e-3: bad.append((k+1,'inicio'))
    tcut,astart=T[k+1]; on=astart+(S[k+1]['on']-S[k+1]['in'])/R
    sl.append(round((tcut-on)*30,1))
    resp.append((S[k+1]['on']-S[k+1]['in'])/R+(S[k]['aout']-S[k]['off'])/R)
print(f"emendas {len(V)-1} · buracos {holes} · crossfade sobre fala: {bad or 'nenhum'}")
print(f"lead de FALA (quadros): mediana {st.median(sl)} · min {min(sl)} · max {max(sl)} -> {sorted(set(sl))}")
print(f"respiro entre falas: mediana {st.median(resp):.3f}s · min {min(resp):.3f} · max {max(resp):.3f}")
