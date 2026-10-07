"""silencedetect -> regioes de fala -> work/regions.json"""
import subprocess, re, json, sys
SRC='work/full.wav'
NOISE=sys.argv[1] if len(sys.argv)>1 else '-35dB'
D=sys.argv[2] if len(sys.argv)>2 else '0.35'
out=subprocess.run(['ffmpeg','-v','info','-i',SRC,'-af',f'silencedetect=noise={NOISE}:d={D}','-f','null','-'],
                   capture_output=True,text=True).stderr
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',SRC],
                         capture_output=True,text=True).stdout.strip())
sil=[]
cur=None
for m in re.finditer(r'silence_(start|end): ([\d.\-]+)', out):
    k,v=m.group(1),float(m.group(2))
    if k=='start': cur=v
    elif cur is not None: sil.append((cur,v)); cur=None
if cur is not None: sil.append((cur,dur))
regs=[];prev=0.0
for s,e in sil:
    if s-prev>0.25: regs.append((prev,s))
    prev=e
if dur-prev>0.25: regs.append((prev,dur))
res=[{"i":i,"s":round(s,3),"e":round(e,3),"d":round(e-s,3)} for i,(s,e) in enumerate(regs)]
json.dump(res,open('work/regions.json','w'),indent=1)
for r in res: print(f"r{r['i']:02d}  {r['s']:7.2f} -> {r['e']:7.2f}  ({r['d']:.2f}s)")
print(f"\n{len(res)} regioes de fala")
