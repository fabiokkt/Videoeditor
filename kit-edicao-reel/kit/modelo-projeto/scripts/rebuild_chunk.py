"""Reconstroi ch<NN>-words.json a partir do passe por REGIAO (work/region-words-cut.json)
quando o passe por chunk colapsa/alucina. Uso: rebuild_chunk.py ch:regiao_cut[+regiao_cut...] ..."""
import json, sys
M={m['i']:m for m in json.load(open('assets/chunks/meta.json'))}
RW=json.load(open('work/region-words-cut.json'))
for spec in sys.argv[1:]:
    ci,rc=spec.split(':'); ci=int(ci); off=M[ci]['off']; ws=[w for r in rc.split('+') for w in RW[r]]
    tr=[{"text":" "+w[0].strip(),"offsets":{"from":int(round((w[1]-off)*1000)),"to":int(round((w[2]-off)*1000))}} for w in ws]
    json.dump({"transcription":tr},open(f'assets/chunks/ch{ci:02d}-words.json','w'),ensure_ascii=False)
    print(f"ch{ci:02d} <- c{rc}:",' '.join(f"{t['text'].strip()}[{t['offsets']['from']}-{t['offsets']['to']}]" for t in tr))
