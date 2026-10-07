"""MOTOR (kit v3, fluxo rapido). Gera assets/chunks/chNN-words.json de TODOS os takes a partir do passe por REGIAO
(work/region-words-cut.json), sem rodar o whisper de novo por chunk. Substitui whisper_chunks.sh + rebuild_chunk.py:
nos reels Sun Tzu, Kazuo e Alan Mulally quase todo chunk acabava reconstruido do passe por regiao (o passe por chunk
vaza palavra do take vizinho, alucina e colapsa tempos). Depois: align.py -> fix_captions.py, como sempre.
uso: python3 scripts/chunks_from_regions.py      (depois de mkchunks.py)"""
import json, os
M = {m['i']: m for m in json.load(open('assets/chunks/meta.json'))}
RW = json.load(open('work/region-words-cut.json'))
RC = {r['i']: r for r in json.load(open('work/regions_cut.json'))}
segs = json.load(open('work/segs.json'))
os.makedirs('work/chunks-raw', exist_ok=True)
for s in segs:
    ci = s['i']; a, b = s['region']; off = M[ci]['off']
    ws = [w for r in range(a, b + 1) if not RC[r]['drop'] for w in RW.get(str(r), [])]
    tr = [{"text": " " + w[0].strip(), "offsets": {"from": int(round((w[1] - off) * 1000)), "to": int(round((w[2] - off) * 1000))}} for w in ws]
    d = {"transcription": tr}
    json.dump(d, open(f'assets/chunks/ch{ci:02d}-words.json', 'w'), ensure_ascii=False)
    json.dump(d, open(f'work/chunks-raw/ch{ci:02d}-words.json', 'w'), ensure_ascii=False)
    print(f"ch{ci:02d} {s['label']:<20} " + ' '.join(t['text'].strip() for t in tr))
print(f"{len(segs)} chunks a partir do passe por regiao (indices de palavra = os desta lista, para a captions_fix_table.py)")
