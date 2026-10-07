import json, numpy as np, sys
def win(w0,w1,b):
    f0,f1=b.get('span',[0,1]); return (round(w0+(w1-w0)*f0,3), round(w0+(w1-w0)*f1,3))
M=json.load(open('gaze/measure.json'))
plan=json.load(open('assets/edit-plan.json')); RATE=plan.get('rate',1.1); F=lambda n:n/30
LEAD=F(plan.get('jcutLeadFrames',5))
segs=[];t=0
for i,s in enumerate(plan['segments']):
    sd=(s['out']-s['in'])/RATE; lead=0 if i==0 else min(LEAD,sd-F(10)); d=sd-lead
    segs.append({"i":i,"label":s["label"],"in":s["in"],"out":s["out"],"tail":s.get("videoTail"),
                 "t0":round(t,3),"t1":round(t+d,3),"lead":lead}); t+=d
ed=[ (s['out']-s['tail'])/RATE if s['tail'] else 0 for s in segs]
for i,s in enumerate(segs):
    dPrev=ed[i-1] if i>0 else 0
    s['vStart']=round(s['t0']-dPrev,3); s['vEnd']=round(s['t1']-ed[i],3)
    s['vMedia']=round(s['in']+(s['lead']-dPrev)*RATE,3)
def src2tl(i,x):
    s=segs[i]; return round(s['vStart']+(x-s['vMedia'])/RATE,3)
# janelas em que o apresentador aparece
# cobertura por JANELA de timeline (inclui preStart), nao por segmento:
# um cutaway antecipado cobre o fim do take anterior.
fullW=[]; splitW=[]
for b in (plan.get('broll') or json.load(open('assets/broll-slots.json'))['slots']):
    w=win(segs[b['fromSeg']]['t0']-b.get('preStart',0), segs[b['toSeg']]['t1'], b)
    (fullW if b['mode']=='full' else splitW).append(w)
def merge(ws):
    # tomadas seguidas da mesma cena sao janelas contiguas: sem unir, um desvio em cima da
    # emenda (ex. 18,57 s) era reportado como descoberto so por cair entre duas tomadas.
    out=[]
    for w0,w1 in sorted(ws):
        if out and w0<=out[-1][1]+0.03: out[-1][1]=max(out[-1][1],w1)
        else: out.append([w0,w1])
    return out
fullW=merge(fullW); splitW=merge(splitW)
def cover(a,b):
    if any(w0<=a+0.02 and b<=w1+0.02 for w0,w1 in fullW): return "B-ROLL"
    if any(w0<=a+0.02 and b<=w1+0.02 for w0,w1 in splitW): return "split"
    return "CHEIA"
ok=[o for o in M if o.get('ok')]
med=np.median([o['gx'] for o in ok]); opmed=np.median([o['op'] for o in ok])
byt={round(o['t'],3):o for o in ok}; ts=sorted(byt)
THR=float(sys.argv[1]) if len(sys.argv)>1 else 0.028
rows=[]
for s in segs:
    i=s['i']
    lo,hi=s['vMedia'], s['vMedia']+(s['vEnd']-s['vStart'])*RATE
    flags=[(x,(byt[x]['op']>=opmed*0.55) and abs(byt[x]['gx']-med)>THR,byt[x]['gx'])
           for x in ts if lo-0.02<=x<=hi+0.02]
    wins=[];cur=None
    for x,f,g in flags:
        if f: cur=[x,x,[g]] if cur is None else [cur[0],x,cur[2]+[g]]
        else:
            if cur and cur[1]-cur[0]>=0.15: wins.append(cur)
            cur=None
    if cur and cur[1]-cur[0]>=0.15: wins.append(cur)
    for a,b,gv in wins:
        pos="INICIO" if a-lo<0.5 else ("FIM" if hi-b<1.0 else "MEIO")
        rows.append({"seg":i,"label":s['label'],"vis":cover(src2tl(i,a),src2tl(i,b)),"a":round(a,2),"b":round(b,2),
                     "dur":round(b-a+0.08,2),"gx":round(float(np.mean(gv)),4),"pos":pos,
                     "tl0":src2tl(i,a),"tl1":src2tl(i,b)})
print(f"limiar |gx-{med:+.4f}| > {THR}\n")
print(f"{'seg':<5}{'label':<12}{'visivel':<8}{'src':<16}{'dur':>5} {'gx':>8} {'pos':<7}{'timeline':<15}{'acao'}")
for r in rows:
    need = r['vis']!='B-ROLL'
    print(f"{r['seg']:<5}{r['label']:<12}{r['vis']:<8}{r['a']:.2f}-{r['b']:.2f}   {r['dur']:>4.2f} {r['gx']:+8.4f} {r['pos']:<7}{r['tl0']:.2f}-{r['tl1']:.2f}   {'<< VERIFICAR' if need else 'coberto'}")
json.dump(rows,open('gaze/windows.json','w'),indent=1)
print(f"\n{len(rows)} janelas | {sum(1 for r in rows if r['vis']!='B-ROLL')} com apresentador visivel")
