"""Revisão visual por take: [meio do take = referência] | início +0.03/+0.25 | fim -0.9/-0.6/-0.35/-0.12.
Cada linha = 1 take (tempos de SOURCE, já descontando videoTail). Uso: gaze_pairs.py <saida> [seg ...]"""
import json,subprocess,os,sys
from _src import SRC
plan=json.load(open('assets/edit-plan.json')); out=sys.argv[1]; only=[int(x) for x in sys.argv[2:]]
os.makedirs(out,exist_ok=True)
rows=[]
for i,s in enumerate(plan['segments']):
    if only and i not in only: continue
    a=s['in']+ (0.17*1.1 if i else 0); b=s.get('videoTail') or s['out']
    ts=[(a+b)/2, a+0.03, a+0.25, b-0.9, b-0.6, b-0.35, b-0.12]
    files=[]
    for k,t in enumerate(ts):
        f=f'{out}/s{i:02d}_{k}.jpg'
        subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{t:.3f}','-i',SRC,'-frames:v','1','-vf',
          'crop=640:400:230:1040,scale=320:-1',f],check=True); files.append(f)
    subprocess.run(['ffmpeg','-v','error','-y',*sum([['-i',f] for f in files],[]),'-filter_complex',
      f"{''.join(f'[{k}]' for k in range(7))}hstack=7",f'{out}/row{i:02d}.jpg'],check=True)
    for f in files: os.remove(f)
    rows.append(i)
for g in range(0,len(rows),8):
    rr=rows[g:g+8]
    subprocess.run(['ffmpeg','-v','error','-y',*sum([['-i',f'{out}/row{i:02d}.jpg'] for i in rr],[]),'-filter_complex',
      (f"{''.join(f'[{k}]' for k in range(len(rr)))}vstack={len(rr)}" if len(rr)>1 else '[0]copy'),f'{out}/P{g//8}.jpg'],check=True)
    print(f'P{g//8}: segs {rr}')
