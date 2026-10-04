"""Varredura das FRONTEIRAS de take: últimos ~0,8 s e primeiros ~0,3 s de cada take,
onde o apresentador lê o roteiro. Monta uma folha de olhos por lote, com o gx medido."""
import subprocess,sys,os,json
from _src import SRC
M={round(o['t'],3):o for o in json.load(open('gaze/measure.json')) if o.get('ok')}
P=json.load(open('assets/edit-plan.json'))
os.makedirs('work/gb',exist_ok=True)
CROP='crop=680:320:220:1080,scale=340:160'
subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=c=#101014:s=340x160:d=1','-frames:v','1','work/gb/pad.jpg'],check=True)
def gx(t):
    n=min(M,key=lambda k:abs(k-t)); return M[n]['gx']
def folha(nome,itens,cols=6):
    files=[]
    for k,(lab,t) in enumerate(itens):
        f=f'work/gb/{nome}_{k:03d}.jpg'
        subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{t:.3f}','-i',SRC,'-frames:v','1',
            '-vf',CROP,f],check=True)
        files.append(f)
    while len(files)%cols: files.append('work/gb/pad.jpg')
    args=[];  [args.extend(['-i',f]) for f in files]
    rows=[files[i:i+cols] for i in range(0,len(files),cols)]
    fc='';ro=[];idx=0
    for ri,r in enumerate(rows):
        fc+=''.join(f'[{idx+j}:v]' for j in range(len(r)))+f'hstack=inputs={len(r)}[r{ri}];'; idx+=len(r); ro.append(f'[r{ri}]')
    fc+=''.join(ro)+f'vstack=inputs={len(rows)}[out]'
    subprocess.run(['ffmpeg','-v','error','-y']+args+['-filter_complex',fc,'-map','[out]',f'work/gb/{nome}.jpg'],check=True)
    print(f'work/gb/{nome}.jpg  ({len(itens)} quadros, {cols} col)')
    for r in range(0,len(itens),cols):
        print('   '+'  '.join(f'{lab}@{t:.2f}:{gx(t):+.3f}' for lab,t in itens[r:r+cols]))
segs=P['segments']
tails=[];heads=[]
for i,s in enumerate(segs):
    for d in (0.55,0.38,0.22,0.07):
        tails.append((f'{i}T', s['out']-d))
    if i: 
        for d in (0.04,0.16,0.30):
            heads.append((f'{i}H', s['in']+d))
lote=sys.argv[1] if len(sys.argv)>1 else 'todos'
if lote in ('todos','tails'):
    for b in range(0,len(tails),36): folha(f'tails{b//36}',tails[b:b+36])
if lote in ('todos','heads'):
    for b in range(0,len(heads),36): folha(f'heads{b//36}',heads[b:b+36])
