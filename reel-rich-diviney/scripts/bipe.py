"""POR VIDEO — reel RICH DIVINEY. Bipe de censura gravado na voz, na palavra INTEIRA
("Ele diz que a pessoa so mostra quem e quando da merda.").
Entrada: work/<slug>-voz-limpa.m4a (audio do bruto) -> assets/<slug>-voz.m4a (voz do projeto)
e work/full.wav (mono, o que o cuts.py le). Transcricao continua usando work/full-clean.wav (sem bipe).
Mapa (envelope 10 ms + bandas de espectro 30 ms, source): "quan" 59,88-59,96 · nasal /n/ 59,97-60,02 · "do" 60,03-60,09 ·
oclusao /d/ 60,10-60,14 · "da" 60,15-60,25 · nasal /m/ 60,26-60,34 (energia < 400 Hz > 90%) · "er" 60,35-60,49 ·
oclusao /d/ 60,50-60,51 · "a" 60,52-60,68 · decaimento ate 60,74.
Whisper em recortes cumulativos (de 57,45): ate 60,25 "...quando da" · ate 60,36 "...quando da medo" · ate 60,75 "...quando da merda".
Varredura da transcricao INTEIRA (31 regioes, inclusive as descartadas): so este palavrao."""
import numpy as np, subprocess, wave, json, os
VOZ=json.load(open('assets/edit-plan.json'))['voiceSrc']                      # assets/<slug>-voz.m4a (voz do projeto, COM bipe)
LIMPA='work/'+os.path.basename(VOZ).replace('.m4a','-limpa.m4a')             # work/<slug>-voz-limpa.m4a (audio do bruto, SEM bipe)
JANELAS=[(60.255,60.745)]  # POR VIDEO: [(ini, fim)] em s do source, palavra INTEIRA. Ex. (reel Kazuo): [(75.905,76.505)]. Vazio = sem bipe (fase2.sh pula)
GAIN=10**(-18/20)*1.75    # bipe ~1 dB acima da frase (Dan Martell: -17,2 contra -18,4)
subprocess.run(['ffmpeg','-v','error','-y','-i',LIMPA,'-ar','48000','-ac','2','-c:a','pcm_s16le','work/voz-limpa48.wav'],check=True)
w=wave.open('work/voz-limpa48.wav'); sr=w.getframerate(); ch=w.getnchannels()
x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32).reshape(-1,ch)/32768
for A,B in JANELAS:
    i0,i1=int(A*sr),int(B*sr); n=i1-i0; t=np.arange(n)/sr
    f=int(0.006*sr); env=np.ones(n); env[:f]=np.linspace(0,1,f); env[-f:]=np.linspace(1,0,f)
    x[i0:i1]=0; x[i0:i1]+= (GAIN*np.sin(2*np.pi*1000*t)*env)[:,None]
y=(np.clip(x,-1,1)*32767).astype(np.int16)
o=wave.open('work/voz-bipe48.wav','wb'); o.setnchannels(ch); o.setsampwidth(2); o.setframerate(sr); o.writeframes(y.tobytes()); o.close()
subprocess.run(['ffmpeg','-v','error','-y','-i','work/voz-bipe48.wav','-c:a','aac','-b:a','192k',VOZ],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i','work/voz-bipe48.wav','-ac','1','-ar','44100','-c:a','pcm_s16le','work/full.wav'],check=True)
print(f'bipes {JANELAS} gravados em {VOZ} e work/full.wav')
