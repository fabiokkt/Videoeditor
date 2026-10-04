"""Extrai um wav por regiao de fala (+-0.3s) -> work/reg/rNN.wav + work/reg/meta.json"""
import json, subprocess
regs=json.load(open('work/regions.json'))
meta=[]
for r in regs:
    off=round(max(0.0,r['s']-0.3),3); end=round(r['e']+0.3,3)
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(off),'-t',str(round(end-off,3)),
        '-i','work/full-clean.wav','-ac','1','-ar','16000','-c:a','pcm_s16le',
        f"work/reg/r{r['i']:02d}.wav"],check=True)
    meta.append({"i":r['i'],"off":off,"end":end})
json.dump(meta,open('work/reg/meta.json','w'),indent=1)
print(f"{len(meta)} regioes extraidas")
