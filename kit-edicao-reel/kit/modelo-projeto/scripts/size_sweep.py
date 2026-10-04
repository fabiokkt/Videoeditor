"""Escolhe o --size do render em partes (scripts/render-chunks.mjs). NOVO no kit v2 (2026-10-01): era uma conta refeita a mao a cada reel.
O render aborta no gate de cobertura quando uma parte fica com poucos quadros de um clipe ("captured 2 of expected 3 frames").
Para cada tamanho candidato, mede a MENOR sobra de <video> dentro de qualquer pedaco (parte dividida em --split) e lista os melhores.
Regras ja pagas:
 - varrer SO os <video> (as legendas sempre ficam fatiadas e nao passam pelo gate);
 - a varredura tem que incluir os pedacos do --split (354 era bom sem split e deixava 8 quadros com --split 3);
 - sobra minima >= ~15 quadros; quanto maior, melhor;
 - a 60 fps nao passar de ~460 quadros por parte (o Chrome travou em ~530 e ~570 em sessoes longas); nao desligar o gate.
Uso: python3 scripts/size_sweep.py [--fps 60] [--split 3] [--min 300] [--max 460] [--top 8]"""
import re, sys, math
def arg(k, d): return type(d)(sys.argv[sys.argv.index(k)+1]) if k in sys.argv else d
FPS=arg('--fps',60); SPLIT=arg('--split',3); LO=arg('--min',300); HI=arg('--max',460); TOP=arg('--top',8)
h=open('index.html').read()
TOTAL=float(re.search(r'id="root"[^>]*data-duration="([\d.]+)"',h)[1]); TF=math.ceil(TOTAL*FPS-1e-6)
at=lambda t,k: float(re.search(r'(?<![\w-])'+k+r'="([^"]*)"',t)[1])
V=[(at(t,'data-start')*FPS,(at(t,'data-start')+at(t,'data-duration'))*FPS,re.search(r' id="([^"]*)"',t)[1])
   for t in re.findall(r'<video\b[^>]*data-start="[^"]*"[^>]*>',h)]
def pedacos(S):
    out=[]
    for k0 in range(0,TF,S):
        k1=min(TF,k0+S); step=math.ceil((k1-k0)/SPLIT)
        out+=[(k0+j*step,min(k1,k0+(j+1)*step)) for j in range(SPLIT) if k0+j*step<k1]
    return out
def pior(S):
    w=(1e9,None,None)
    for a,b in pedacos(S):
        for s,e,i in V:
            o=min(b,e)-max(a,s)
            if o>1e-6 and o<w[0]: w=(o,i,(a,b))
    return w
res=sorted(((pior(S),S) for S in range(LO,HI+1)),key=lambda x:(-x[0][0],-x[1]))
print(f"timeline {TOTAL}s = {TF} quadros @{FPS} · {len(V)} <video> · --split {SPLIT} · tamanhos {LO}-{HI}")
for (o,i,p),S in res[:TOP]:
    print(f"  --size {S}: {math.ceil(TF/S)} partes · sobra minima {o:.0f} quadros ({i} no pedaco {p[0]}-{p[1]})")
