"""Timeline dos takes (mesma conta do build-edit.mjs) + palavras em tempo de timeline. Uso: tl.py [--words]"""
import json, sys
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
M={m['i']:m for m in json.load(open('assets/chunks/meta.json'))}
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3),lead)); t=round(t+d,3)
def src2tl(i,x):  # voz do take i: comeca lead antes de t0
    s=P['segments'][i]; return round(segs[i][0]-segs[i][2]+(x-s['in'])/R,3)
if __name__=='__main__':
    for i,s in enumerate(P['segments']):
        d=json.load(open(f"assets/chunks/ch{i:02d}-words.json"))
        ws=[(e['text'].strip(),src2tl(i,M[i]['off']+e['offsets']['from']/1000)) for e in d['transcription'] if e['text'].strip()]
        txt=' '.join(f"{w}@{x:.2f}" for w,x in ws) if '--words' in sys.argv else ' '.join(w for w,_ in ws)
        print(f"{i:2d} {s['label']:<20} {segs[i][0]:6.2f}-{segs[i][1]:6.2f} ({segs[i][1]-segs[i][0]:.2f})  {txt}")
    print('TOTAL',t)
