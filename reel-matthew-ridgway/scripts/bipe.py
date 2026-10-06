"""POR VIDEO — reel MATTHEW RIDGWAY. Bipe de censura gravado na voz, na palavra INTEIRA
(fala: "Seu vendedor ta sem computador que presta e voce manda a porra do video motivacional, meu querido?").
Entrada: work/matthew-ridgway-voz-limpa.m4a (audio do bruto) -> assets/matthew-ridgway-voz.m4a (voz do projeto)
e work/full.wav (mono, o que o cuts.py le). Transcricao continua usando work/full-clean.wav (sem bipe).
Mapa (envelope 10 ms + bandas, source): "manda a" ate 64,01 · oclusao /p/ (silencio, -45 a -47 dB) 64,02-64,07 · explosao 64,08 ·
"o" 64,08-64,20 (-10 dB) · "rr" fricativo 64,21-64,35 (-30 a -53 dB) · "a" 64,36-64,52 · "do" a partir de 64,54.
Whisper em recortes cumulativos do audio limpo (de 61,00): ate 64,30 "...manda a"; ate 64,40 "...manda a aposta,"; ate 64,53 "...manda a porra.";
ate 64,75 "...a porra do"; de 64,54 em diante: "do video motivacional, meu querido." (nada da palavra sobra).
Varredura da transcricao INTEIRA (29 regioes, inclusive as descartadas): so este palavrao ("bunda" nao e bipado; o roteiro marca 1 piiii)."""
import numpy as np, subprocess, wave, json, os
VOZ=json.load(open('assets/edit-plan.json'))['voiceSrc']                      # assets/<slug>-voz.m4a (voz do projeto, COM bipe)
LIMPA='work/'+os.path.basename(VOZ).replace('.m4a','-limpa.m4a')             # work/<slug>-voz-limpa.m4a (audio do bruto, SEM bipe)
JANELAS=[(64.03,64.53)]  # POR VIDEO: [(ini, fim)] em s do source, palavra INTEIRA. Ex. (reel Kazuo): [(75.905,76.505)]. Vazio = sem bipe (fase2.sh pula)
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
