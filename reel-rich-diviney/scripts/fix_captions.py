"""Correcoes de texto das legendas (o whisper erra grafia, pontuacao e maiuscula quando o chunk
comeca no meio da frase). Roda depois de align.py. Nao muda timing — so o texto de cada palavra.
A tabela POR VIDEO fica em scripts/captions_fix_table.py (o align.py tambem a le para ignorar as palavras DROP).
IDEMPOTENTE: na 1a execucao guarda a saida do align.py em work/chunks-aligned/ e sempre parte dela.
Para regerar do zero depois de um novo align.py: apagar work/chunks-aligned/chNN-words.json."""
import json, os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from captions_fix_table import FIX, FIXT
SOMENTE={int(x) for x in sys.argv[1:]}  # sem argumento = todos
META={m['i']:m for m in json.load(open('assets/chunks/meta.json'))}
os.makedirs('work/chunks-aligned',exist_ok=True)
for ci in range(len(json.load(open('assets/chunks/meta.json')))):
    if SOMENTE and ci not in SOMENTE: continue
    p=f'assets/chunks/ch{ci:02d}-words.json'; b=f'work/chunks-aligned/ch{ci:02d}-words.json'
    if not os.path.exists(b): shutil.copy(p,b)
    d=json.load(open(b)); n=0
    words=[e for e in d['transcription'] if e['text'].strip() and not e['text'].strip().startswith('[')]
    for k,new in FIX.get(ci,{}).items():
        e=words[k]
        e['text']='' if new is None else ' '+new; n+=1
    for k,src in FIXT.get(ci,{}).items():
        e=words[k]; d0=e['offsets']['to']-e['offsets']['from']; e['offsets']['from']=int(round((src-META[ci]['off'])*1000))
        e['offsets']['to']=max(e['offsets']['to'],e['offsets']['from']+1); n+=1
    json.dump(d,open(p,'w'),ensure_ascii=False)
    if n: print(f"  ch{ci:02d}: {n} correcao(oes) -> "+' '.join(e['text'].strip() for e in words if e['text'].strip()))
