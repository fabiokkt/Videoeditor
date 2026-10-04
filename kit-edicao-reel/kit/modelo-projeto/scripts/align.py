"""Reancora os timestamps de palavra do whisper na energia real do chunk.
O whisper deriva ate ~1s dentro de um chunk; aqui cada grupo de palavras e
encaixado sobre o grupo de fala correspondente detectado por RMS."""
import numpy as np, wave, json, glob, os, shutil, sys
SOMENTE={int(x) for x in sys.argv[1:]}  # sem argumento = todos os chunks
META={m['i']:m for m in json.load(open('assets/chunks/meta.json'))}
PLAN=json.load(open('assets/edit-plan.json'))
sys.path.insert(0, os.path.dirname(__file__))
from captions_fix_table import FIX  # palavras DROP (vazamento do take vizinho) ficam fora do encaixe
NOISE=-45.0
def envelope(path):
    w=wave.open(path); n=w.getnframes(); sr=w.getframerate()
    a=np.frombuffer(w.readframes(n),dtype=np.int16).astype(np.float32)/32768.0
    W=int(0.020*sr); nw=len(a)//W
    return 20*np.log10(np.sqrt(np.maximum((a[:nw*W].reshape(nw,W)**2).mean(1),1e-12))), nw
def runs(db,nw,merge=0.16,minrun=0.07):
    on=db>=NOISE; out=[];i=0
    while i<nw:
        if on[i]:
            j=i
            while j<nw and on[j]: j+=1
            out.append([i*0.02,j*0.02]); i=j
        else: i+=1
    m=[]
    for r in out:
        if m and r[0]-m[-1][1]<merge: m[-1][1]=r[1]
        else: m.append(r)
    return [r for r in m if r[1]-r[0]>=minrun]
def groups(ws,gap=0.22):
    g=[[ws[0]]]
    for p,c in zip(ws,ws[1:]):
        if c[0]-p[1]>gap: g.append([c])
        else: g[-1].append(c)
    return g
def warp(ws,src,dst):
    s0,s1=src; d0,d1=dst
    k=(d1-d0)/(s1-s0) if s1-s0>1e-6 else 1.0
    return [(round(d0+(a-s0)*k,3), round(d0+(b-s0)*k,3), t) for a,b,t in ws]
report=[]
for p in sorted(glob.glob('assets/chunks/ch*-words.json')):
    if SOMENTE and int(os.path.basename(p)[2:4]) not in SOMENTE: continue
    ci=int(os.path.basename(p)[2:4]); wav=f'assets/chunks/ch{ci:02d}.wav'
    d=json.load(open(p))
    ents=[e for e in d['transcription'] if e['text'].strip() and not e['text'].strip().startswith('[')]
    keep=[k for k in range(len(ents)) if not (k in FIX.get(ci,{}) and FIX[ci][k] is None)]
    ents=[ents[k] for k in keep]
    ws=[(e['offsets']['from']/1000,e['offsets']['to']/1000,e['text'].strip()) for e in ents]
    if not ws: continue
    db,nw=envelope(wav); R=runs(db,nw)
    # o chunk tem +-0.3s de folga e pode conter o fim do take anterior / inicio do
    # proximo: so valem os trechos de fala dentro do corpo do proprio take.
    off=META[ci]['off']; seg=PLAN['segments'][ci]
    b0,b1=seg['in']-off-0.06, seg.get('aout',seg['out'])-off+0.06  # so a VOZ do take (o out inclui o lead do J-cut)
    R=[r for r in R if r[1]>b0 and r[0]<b1]
    R=[[max(r[0],b0),min(r[1],b1)] for r in R]
    if not R: continue
    G=groups(ws)
    if len(G)==len(R):                      # alinhamento grupo-a-grupo
        new=[]
        for g,r in zip(G,R): new+=warp(g,(g[0][0],g[-1][1]),(r[0],r[1]))
        mode=f"grupos {len(G)}"
    else:                                   # fallback: ancora so os extremos
        new=warp(ws,(ws[0][0],ws[-1][1]),(R[0][0],R[-1][1]))
        mode=f"extremos (w{len(G)}/r{len(R)})"
    shift=max(abs(n[0]-o[0]) for n,o in zip(new,ws))
    report.append(f"ch{ci:02d}: {mode:<18} corr.max {shift*1000:4.0f}ms  '{' '.join(t for _,_,t in ws)[:52]}'")
    for e,(a,b,_) in zip(ents,new):
        e['offsets']['from']=int(round(a*1000)); e['offsets']['to']=int(round(b*1000))
    json.dump(d,open(p,'w'),ensure_ascii=False)
print("\n".join(report))
