"""Otimizador do ritmo de cenas (pedido do Fabio: troca de cena/efeito a cada ~4 s, nao 1-2 s).
Particiona a timeline em cenas de LMIN..LMAX s. Tipos: P (apresentador), B (B-roll tela cheia),
S (split, so nas janelas de split). Custo = segundos de leitura de roteiro EXPOSTA (P/S) * 1
+ segundos de B-roll * WB (preferir o apresentador quando o olhar esta limpo).
Cortes obrigatorios: FORCE. Trechos so-B: ONLYB. Saida: work/cenas-opt.json"""
import json, math
TOTAL=json.load(open('work/mix-plan.json'))['total']
# leituras de roteiro (timeline) — gaze/tl-windows.json (scripts/gaze_tl.py + gaze_windows.py), revisadas nas folhas
# gaze/rev/*.jpg. Reel MIKE MICHALOWICZ (rate 1.1, timeline 100,87 s): as 59 janelas tratadas como desvio
# (conservador: o pedido e aparecer 100% olhando para a camera) -> gaze/tl-windows-conf-uniao.json.
G=[(w['t0']-0.03,w['t1']+0.03) for w in json.load(open(__import__('os').environ.get('GW','gaze/tl-windows-conf.json')))]
SPLIT=[(0.0,12.31),(66.98,76.72)]  # intro (pre-revelacao, segs 0-3) e split 2 (a virada: "foi um cofrinho... cada centavo", segs 23-26)
FORCE=[12.31,66.98,82.75]          # revelacao ("Mike" em 12,19 s) · entrada do split 2 · climax ("Papai, a gente vai conseguir")
ONLYB=[(12.31,13.40),(82.75,84.30)] # revelacao (Mike) · climax
ONLYP=[(48.35,48.72),(98.50,100.87)] # bipe no rosto (a boca sob o bipe le como censura) · "me segue, porque voce e demais"
FIRST=('S',0.0)                    # a CAPA (quadro 0) e sempre split
WBS=0.5                           # custo extra por s de tela cheia DENTRO de split (preserva o formato)
LMIN,LMAX,WB,STEP=2.5,5.0,0.05,0.05
def expo(a,b): return sum(max(0,min(b,g1)-max(a,g0)) for g0,g1 in G)
N=int(round(TOTAL/STEP)); T=lambda i: min(TOTAL,i*STEP)
F={int(round(f/STEP)) for f in FORCE}
def allowed(a,b,k):
    ta,tb=T(a),T(b)
    if any(ta<f*STEP<tb for f in F if 0<f<N): return False
    insp=any(s0-1e-6<=ta and tb<=s1+1e-6 for s0,s1 in SPLIT)
    inb=any(ta<b1 and tb>b0 for b0,b1 in ONLYB)
    if k!='P' and any(ta<p1 and tb>p0 for p0,p1 in ONLYP): return False
    if k=='S': return insp
    ovs=any(ta<s1-1e-6 and tb>s0+1e-6 for s0,s1 in SPLIT)
    if k=='P': return not inb and not ovs
    return True
INF=1e9; best=[{} for _ in range(N+1)]; best[0]={None:(0,None)}
for i in range(N+1):
    for last,(c,_) in list(best[i].items()):
        for L in range(int(LMIN/STEP),int(LMAX/STEP)+1):
            j=i+L
            if j>N:
                j=N
                if (j-i)*STEP<1.2: continue
            for k in 'PBS':
                if i==0 and FIRST and k!=FIRST[0]: continue
                if not allowed(i,j,k): continue
                if k=='P' and last=='P': continue      # P->P sem troca nao conta como cena nova
                cost=c+(expo(T(i),T(j)) if k in 'PS' else WB*(T(j)-T(i))+WBS*sum(max(0,min(T(j),s1)-max(T(i),s0)) for s0,s1 in SPLIT))
                if cost<best[j].get(k,(INF,))[0]: best[j][k]=(cost,(i,last))
            if j==N: break
k=min(best[N],key=lambda x:best[N][x][0]); cost=best[N][k][0]; out=[]; j=N
while j>0:
    c,(i,prev)=best[j][k]; out.append((round(T(i),2),round(T(j),2),k)); j,k=i,prev
out.reverse()
json.dump([{"t0":a,"t1":b,"tipo":k,"exposto":round(expo(a,b),2) if k!='B' else 0} for a,b,k in out],open('work/cenas-opt.json','w'),indent=1)
tot=sum(expo(a,b) for a,b,k in out if k!='B'); allg=sum(g1-g0 for g0,g1 in G)
for a,b,k in out: print(f"{k} {a:6.2f}-{b:6.2f} ({b-a:4.2f})"+(f"  expoe {expo(a,b):.2f}s" if k!='B' and expo(a,b)>0 else ''))
print(f"{len(out)} cenas · B-roll {sum(1 for x in out if x[2]=='B')} · leitura exposta {tot:.2f}s de {allg:.2f}s")
