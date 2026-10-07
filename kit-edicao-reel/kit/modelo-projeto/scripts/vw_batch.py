"""Varredura de olhar em lote: para cada janela (source a-b), monta uma faixa quadro a
quadro so da regiao dos olhos, com o gx medido. Uso: vw_batch.py nome:a:b[:passo] ..."""
import subprocess,sys,os,json
from _src import SRC
M={round(o['t'],3):o for o in json.load(open('gaze/measure.json')) if o.get('ok')}
os.makedirs('work/vb',exist_ok=True)
pad='work/vb/pad.jpg'
subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=c=#101014:s=420x163:d=1','-frames:v','1',pad],check=True)
for spec in sys.argv[1:]:
    p=spec.split(':'); name=p[0]; a=float(p[1]); b=float(p[2]); step=float(p[3]) if len(p)>3 else 0.1
    ts=[];x=a
    while x<=b+1e-6: ts.append(round(x,2)); x+=step
    files=[];line=[]
    for i,t in enumerate(ts):
        f=f"work/vb/{name}_{i:02d}.jpg"
        subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',SRC,'-frames:v','1',
          '-vf','crop=720:280:250:1100,scale=420:163',f],check=True)
        files.append(f); n=min(M,key=lambda k:abs(k-t)); line.append(f"{t:.2f}:{M[n]['gx']:+.3f}")
    COLS=6
    while len(files)%COLS: files.append(pad)
    args=[]
    for f in files: args+=['-i',f]
    rows=[files[i:i+COLS] for i in range(0,len(files),COLS)]
    fc="";idx=0;ro=[]
    for ri,r in enumerate(rows):
        fc+="".join(f"[{idx+j}:v]" for j in range(COLS))+f"hstack=inputs={COLS}[r{ri}];";idx+=COLS;ro.append(f"[r{ri}]")
    fc+="".join(ro)+f"vstack=inputs={len(ro)}[out]" if len(ro)>1 else f"{ro[0]}copy[out]"
    subprocess.run(['ffmpeg','-v','error','-y']+args+['-filter_complex',fc,'-map','[out]',f'work/vb/{name}.jpg'],check=True)
    for f in files:
        if f!=pad: os.remove(f)
    print(name, '  '.join(line))
