import json, subprocess, os
segs=json.load(open('work/segs.json'))
# SEM clamp do out no in do take seguinte (reel REED HASTINGS): out = aout + lead (cuts.py) e o video do take
# segura o lead de 5 quadros depois da voz. Em takes CONTIGUOS no source (frase dividida num vale), o clamp
# cortava o lead e a voz perdia os ultimos 14-75 ms da palavra final ("familia", "porta", "Africa").
# O cuts.py ja garante aout <= in do seguinte, entao out <= in_seguinte + lead: nenhum quadro repetido.
# Os chunks de TRANSCRIÇÃO saem do áudio LIMPO (sem o bipe de censura): o bipe está só na
# voz final (assets/ikea-voz.m4a) e em work/full.wav, usado pelo cuts.py para o tail.
SRC='work/full-clean.wav'
meta=[]
for s in segs:
    i=s['i']; off=round(max(0.0,s['in']-0.3),3); end=round(s['out']+0.3,3)
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(off),'-t',str(round(end-off,3)),
        '-i',SRC,'-ac','1','-ar','16000','-c:a','pcm_s16le',
        f'assets/chunks/ch{i:02d}.wav'],check=True)
    meta.append({"i":i,"off":off,"end":end})
json.dump(meta,open('assets/chunks/meta.json','w'),indent=1)
json.dump(segs,open('work/segs.json','w'),indent=1)
print(f"{len(meta)} chunks")
