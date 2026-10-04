"""POR VIDEO — reel DAVID MARQUET. Recupera o "Se voce" de "Se voce e a unica pessoa que pensa na sua empresa".
O take valido (r30) diz "(ce) e a unica..." com o "voce" quase engolido (whisper ouve so "E a unica"); o
"Se voce" claro so existe no tropeco r29 ("Se voce...", com o "e" final arrastado).
Envelope 10 ms de r29: /s/ 108,61-108,69 · "e" 108,70-108,76 · "vo" 108,78-108,84 · /s/ 108,85-108,94 · "e" 108,95-109,12.
Copia "Se voce" (108,59-109,06: corta o "e" arrastado, fade de 20 ms) e encosta no "e a unica" de r30 (109,49).
Antes, SILENCIA 108,55-109,49 na voz (o resto do tropeco nao pode vazar: o take CTA-UNICA agora comeca em 108,87).
O trecho fica sob o B-roll s18 (sem lip-sync a respeitar).
Entrada: work/marquet-voz-limpa.m4a (audio do bruto) -> work/voz-limpa-se.wav (48k estereo, base do bipe.py)
e work/full-clean.wav (mono 44,1k, transcricao). Depois: bipe.py -> assets/marquet-voz.m4a + work/full.wav."""
import numpy as np, subprocess, wave
A,B=108.59,109.06     # "Se voce" no tropeco r29
DST_END=109.49        # onset do "e a unica" de r30
MUTE=(108.55,109.49)  # resto do tropeco, silenciado
subprocess.run(['ffmpeg','-v','error','-y','-i','work/marquet-voz-limpa.m4a','-ar','48000','-ac','2','-c:a','pcm_s16le','work/_limpa48.wav'],check=True)
w=wave.open('work/_limpa48.wav'); sr=w.getframerate(); ch=w.getnchannels()
x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32).reshape(-1,ch)/32768
seg=x[int(A*sr):int(B*sr)].copy(); n=len(seg)
fi,fo=int(0.005*sr),int(0.020*sr)
env=np.ones(n); env[:fi]=np.linspace(0,1,fi); env[-fo:]=np.linspace(1,0,fo); seg*=env[:,None]
m0,m1=int(MUTE[0]*sr),int(MUTE[1]*sr); g=int(0.005*sr)
x[m0:m0+g]*=np.linspace(1,0,g)[:,None]; x[m0+g:m1]=0
d1=int(DST_END*sr); d0=d1-n; x[d0:d1]+=seg
y=(np.clip(x,-1,1)*32767).astype(np.int16)
o=wave.open('work/voz-limpa-se.wav','wb'); o.setnchannels(ch); o.setsampwidth(2); o.setframerate(sr); o.writeframes(y.tobytes()); o.close()
subprocess.run(['ffmpeg','-v','error','-y','-i','work/voz-limpa-se.wav','-ac','1','-ar','44100','-c:a','pcm_s16le','work/full-clean.wav'],check=True)
print(f'"Se voce" {A}-{B}s colado em {d0/sr:.3f}-{DST_END}s (tropeco silenciado {MUTE[0]}-{MUTE[1]}) -> work/voz-limpa-se.wav + work/full-clean.wav')
