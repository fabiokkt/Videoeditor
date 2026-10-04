"""Junta as transcricoes por regiao -> work/region-words.json (tempos ABSOLUTOS do source)
e imprime o texto de cada regiao para a selecao de takes."""
import json, glob, os
meta={m['i']:m for m in json.load(open('work/reg/meta.json'))}
R={r['i']:r for r in json.load(open('work/regions.json'))}
out={}
for p in sorted(glob.glob('work/reg/r*.json')):
    i=int(os.path.basename(p)[1:3]); off=meta[i]['off']
    d=json.load(open(p))
    ws=[[e['text'], round(off+e['offsets']['from']/1000,3), round(off+e['offsets']['to']/1000,3)]
        for e in d['transcription'] if e['text'].strip() and not e['text'].strip().startswith('[')]
    if not ws: continue
    out[i]=ws
json.dump({str(k):v for k,v in sorted(out.items())},open('work/region-words.json','w'),ensure_ascii=False,indent=1)
for i in sorted(out):
    txt=''.join(w[0] for w in out[i]).strip()
    print(f"r{i:02d} [{R[i]['s']:6.2f} -> {R[i]['e']:6.2f}]  {txt}")
print(f"\n{len(out)} regioes transcritas")
