import sys,json
from faster_whisper import WhisperModel
m=WhisperModel("small",device="cpu",compute_type="int8")
for f in sys.argv[1:]:
    segs,_=m.transcribe(f,language="pt",word_timestamps=True,vad_filter=False)
    out=[]
    for s in segs:
        out.append({"start":s.start,"end":s.end,"text":s.text,"words":[{"w":w.word,"s":w.start,"e":w.end} for w in s.words]})
    json.dump(out,open(f+".json","w"),ensure_ascii=False,indent=0)
    print("==",f); [print(f"{o['start']:6.2f}-{o['end']:6.2f} {o['text']}") for o in out]
