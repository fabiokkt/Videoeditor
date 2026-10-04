"""Varredura de olhar: amostra frames do mezanino nos tempos de TIMELINE em que o
apresentador esta visivel e monta grades para revisao visual."""
import re,subprocess,os,sys,json,math
def win(w0,w1,b):
    f0,f1=b.get('span',[0,1]); return (round(w0+(w1-w0)*f0,3), round(w0+(w1-w0)*f1,3))
from _src import SRC
plan=json.load(open('assets/edit-plan.json')); RATE=plan.get("rate",1.1)
# janelas cobertas por B-roll full (apresentador invisivel)
# timeline -> source pelo plano (o vídeo do apresentador virou um arquivo só: assets/aroll.mp4)
segT=[]; t=0; LEAD=plan.get("jcutLeadFrames",5)/30
for i,s in enumerate(plan["segments"]):
    sd=(s["out"]-s["in"])/RATE; lead=0 if i==0 else min(LEAD,sd-10/30); d=sd-lead
    segT.append({"i":i,"label":s["label"],"t0":round(t,3),"t1":round(t+d,3),
                 "vMedia":round(s["in"]+lead*RATE,3)}); t+=d
cov=[]
for b in (plan.get("broll") or json.load(open("assets/broll-slots.json"))["slots"]):
    if b.get("mode")=="full":
        cov.append(win(segT[b["fromSeg"]]["t0"]-b.get("preStart",0), segT[b["toSeg"]]["t1"], b))
covered=lambda x: any(a<=x<bb for a,bb in cov)
times=[]
x=0.0
while x < segT[-1]["t1"] and '--bordas' not in sys.argv:
    times.append(round(x,2)); x+=0.65
for s in segT:  # densidade extra nas bordas do take (onde ele le o roteiro)
    for off in (0.03,0.12,0.22,0.33):
        times.append(round(s["t0"]+off,2))
    for off in (0.08,0.2,0.32,0.45,0.6,0.8):
        times.append(round(s["t1"]-off,2))
times=sorted({t for t in times if 0<=t<segT[-1]["t1"] and not covered(t)})
args=[a for a in sys.argv[1:] if not a.startswith('--')]
out=args[0] if args else 'gaze/pass1'
os.makedirs(out,exist_ok=True)
for f in os.listdir(out):
    if f.endswith('.jpg') or f.endswith('.png'): os.remove(os.path.join(out,f))
rows=[]
for k,tt in enumerate(times):
    seg=[s for s in segT if s["t0"]-1e-6<=tt<s["t1"]]
    if not seg: continue
    src=round(seg[0]["vMedia"]+(tt-seg[0]["t0"])*RATE,3)
    lab=seg[0]["label"]
    rel_end=round((seg[0]["t1"]-tt),2)
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(src),'-i',SRC,
      '-frames:v','1','-vf','crop=720:280:250:1100,scale=300:-1',f'{out}/f{k:03d}.jpg'],check=True)
    rows.append({"k":k,"t":tt,"src":src,"seg":seg[0]["i"],"label":lab,"toEnd":rel_end})
json.dump(rows,open(f'{out}/index.json','w'),indent=1)
print(f"{len(rows)} frames -> {out}")
