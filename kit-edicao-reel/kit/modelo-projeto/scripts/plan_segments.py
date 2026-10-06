"""Copia work/segs.json (scripts/cuts.py) para `segments` do assets/edit-plan.json (in, out, aout, label, chunk).
Preserva campos extras ja postos a mao num segmento (videoTail etc.) quando o label bate."""
import json
P=json.load(open('assets/edit-plan.json')); S=json.load(open('work/segs.json'))
old={s['label']:s for s in P.get('segments',[])}
P['segments']=[{**{k:v for k,v in old.get(s['label'],{}).items() if k not in ('in','out','aout','label','chunk')},
                "in":s['in'],"out":s['out'],"label":s['label'],"chunk":s['i'],"aout":s['aout']} for s in S]
json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1)
print(len(P['segments']),'segments')
