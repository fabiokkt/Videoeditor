"""POR VIDEO — reel STANLEY McCHRYSTAL. Bipe de censura gravado na voz, na palavra INTEIRA
(fala: "Seu vendedor ve a agenda da operacao antes de prometer a porra do prazo, meu querido." — take r24, o ultimo valido).
Entrada: work/stanley-mcchrystal-voz-limpa.m4a (audio do bruto) -> assets/stanley-mcchrystal-voz.m4a (voz do projeto)
e work/full.wav (mono, o que o cuts.py le). Transcricao continua usando work/full-clean.wav (sem bipe).
Mapa (envelope 10 ms + bandas, source): "prometer a" ate 118,33 · decaimento 118,34-118,39 · oclusao /p/ (-42 a -56 dB) 118,40-118,50 ·
explosao 118,51 · "o" 118,52-118,63 · "rr" 118,64-118,67 · "a" 118,68-118,76 · "do" a partir de 118,77 (/d/ sonoro 118,77-118,81).
Whisper em recortes cumulativos do audio limpo (de 115,00): ate 118,50 "...antes de prometer a"; ate 118,64 "...prometera porra"; ate 118,77
"...antes de prometer a porra"; de 118,78 em diante: "do prazo, meu querido." (nada da palavra sobra; de 118,65 ainda ouve "Porra").
Varredura da transcricao INTEIRA (39 regioes, inclusive as descartadas r20/r21): so este palavrao no take mantido (o roteiro marca 1 piiii)."""
import numpy as np, subprocess, wave, json, os
VOZ=json.load(open('assets/edit-plan.json'))['voiceSrc']                      # assets/<slug>-voz.m4a (voz do projeto, COM bipe)
LIMPA='work/'+os.path.basename(VOZ).replace('.m4a','-limpa.m4a')             # work/<slug>-voz-limpa.m4a (audio do bruto, SEM bipe)
JANELAS=[(118.44,118.77)]  # POR VIDEO: [(ini, fim)] em s do source, palavra INTEIRA. Ex. (reel Kazuo): [(75.905,76.505)]. Vazio = sem bipe (fase2.sh pula)
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
