"""Lista os vales de silencio (envelope RMS 10 ms) perto de um instante do source.
Uso: valleys.py t1 t2 ...  -> para cada t, runs abaixo de -38 dB em [t-0.7, t+0.7]"""
import numpy as np, wave, sys
w=wave.open('work/full-clean.wav'); sr=w.getframerate()
a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768.0
W=int(0.010*sr); nw=len(a)//W
db=20*np.log10(np.sqrt(np.maximum((a[:nw*W].reshape(nw,W)**2).mean(1),1e-12)))
THR=float(__import__('os').environ.get('THR','-38'))
for t in map(float,sys.argv[1:]):
    lo,hi=int((t-0.7)/0.01),int((t+0.7)/0.01); runs=[];i=lo
    while i<hi:
        if db[i]<THR:
            j=i
            while j<hi and db[j]<THR: j+=1
            runs.append((i*0.01,j*0.01,db[i:j].min())); i=j
        else: i+=1
    print(f"t={t:.2f}: "+"  ".join(f"[{s:.2f}-{e:.2f} {e-s:.2f}s {m:.0f}dB]" for s,e,m in runs if e-s>=0.04))
