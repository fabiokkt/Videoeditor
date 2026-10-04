import json,subprocess,os,sys
d=sys.argv[1]; COLS=int(sys.argv[2]) if len(sys.argv)>2 else 6; ROWS=int(sys.argv[3]) if len(sys.argv)>3 else 5
rows=json.load(open(f'{d}/index.json')); per=COLS*ROWS
os.makedirs(f'{d}/grids',exist_ok=True)
for f in os.listdir(f'{d}/grids'): os.remove(f'{d}/grids/{f}')
w,h=subprocess.run(['ffprobe','-v','error','-show_entries','stream=width,height','-of','csv=p=0',f"{d}/f{rows[0]['k']:03d}.jpg"],capture_output=True,text=True).stdout.strip().split(',')
subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'color=c=#101014:s={w}x{h}:d=1','-frames:v','1',f'{d}/pad.jpg'],check=True)
for g in range(0,len(rows),per):
    batch=rows[g:g+per]; gi=g//per
    files=[f"{d}/f{r['k']:03d}.jpg" for r in batch]
    while len(files)%COLS: files.append(f'{d}/pad.jpg')
    lines=[files[i:i+COLS] for i in range(0,len(files),COLS)]
    args=[];
    for f in files: args+=['-i',f]
    fc="";idx=0;ro=[]
    for ri,l in enumerate(lines):
        fc+="".join(f"[{idx+j}:v]" for j in range(COLS))+f"hstack=inputs={COLS}[r{ri}];";idx+=COLS;ro.append(f"[r{ri}]")
    fc+="".join(ro)+f"vstack=inputs={len(ro)}[out]" if len(ro)>1 else f"{ro[0]}copy[out]"
    subprocess.run(['ffmpeg','-v','error','-y']+args+['-filter_complex',fc,'-map','[out]',f'{d}/grids/g{gi}.jpg'],check=True)
    print(f"g{gi}: k{batch[0]['k']}-{batch[-1]['k']} t={batch[0]['t']}-{batch[-1]['t']}s  segs {sorted({r['seg'] for r in batch})}")
