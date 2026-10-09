"""POR VIDEO — reel BOB CHAPMAN. Bipe de censura gravado na voz, na palavra INTEIRA
(fala: "Voce deu a porra de um esporro na frente de todo mundo?").
Entrada: work/<slug>-voz-limpa.m4a (audio do bruto) -> assets/<slug>-voz.m4a (voz do projeto) e work/full.wav (o que o cuts.py le).
Transcricao continua usando work/full-clean.wav (sem bipe).
Mapa (envelope 10 ms + bandas, source): "Vo" 87,03-87,09 · /s/ 87,10-87,15 · "ce" 87,17-87,23 · /d/ 87,24-87,28 · "eu a" 87,29-87,50 ·
oclusao do /p/ 87,52-87,71 (decaimento do "a" ate -59 dB) · explosao 87,72 · "o" 87,73-87,92 · "rr" 87,93-87,96 · "a" 87,97-88,07 ·
/d/ de "de" 88,08-88,12 · "e um" ate 88,31 · /s/ de "esporro" 88,32-88,38. O whisper pos "porra" ~0,4 s adiantado (87,29-87,54).
Recortes cumulativos do audio limpo: ate 87,53 "Voce deu a..." (nada da palavra); de 88,08 em diante "Um esporro na frente de todo mundo"
(nada da palavra); de 87,70 "porra de um esporro...". Bipe 87,52-88,08 (palavra inteira, da oclusao do /p/ ao fim do "a").
Varredura da transcricao INTEIRA (24 regioes, inclusive as descartadas): so este palavrao (o roteiro marca 1 piiii)."""
import numpy as np, subprocess, wave, json, os
VOZ=json.load(open('assets/edit-plan.json'))['voiceSrc']                      # assets/<slug>-voz.m4a (voz do projeto, COM bipe)
LIMPA='work/'+os.path.basename(VOZ).replace('.m4a','-limpa.m4a')             # work/<slug>-voz-limpa.m4a (audio do bruto, SEM bipe)
JANELAS=[(87.52,88.08)]  # POR VIDEO: [(ini, fim)] em s do source, palavra INTEIRA. Ex. (reel Kazuo): [(75.905,76.505)]. Vazio = sem bipe (fase2.sh pula)
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
