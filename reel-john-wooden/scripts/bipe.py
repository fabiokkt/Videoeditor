"""POR VIDEO — reel JOHN WOODEN. Bipe de censura gravado na voz, na palavra INTEIRA
(fala: "Ta perdendo a porra do resto do time.", r24 do bruto).
Mapa (envelope 10 ms + fracao de energia < 400 Hz, source): "a" 108,69-108,81 · oclusao /p/ (silencio, -40 a -55 dB) 108,83-108,96 ·
explosao 108,97 · "o" 108,98-109,11 · "rr" 109,12-109,16 · "a" 109,17-109,22 · /d/ de "do" a partir de 109,23.
Whisper em recortes cumulativos do audio limpo (de 107,90): ate 108,95 "...perdendo a"; ate 109,05 "...perdendo apoio" (o "po");
ate 109,12 "...a porra."; ate 109,25 "Ta perdendo a porra.".
Varredura da transcricao INTEIRA (34 regioes, inclusive as descartadas): so este palavrao ("Boa droga.", r03, e descartado e nao e palavrao)."""
import numpy as np, subprocess, wave, json, os
VOZ=json.load(open('assets/edit-plan.json'))['voiceSrc']                      # assets/<slug>-voz.m4a (voz do projeto, COM bipe)
LIMPA='work/'+os.path.basename(VOZ).replace('.m4a','-limpa.m4a')             # work/<slug>-voz-limpa.m4a (audio do bruto, SEM bipe)
JANELAS=[(108.86,109.23)]  # POR VIDEO: [(ini, fim)] em s do source, palavra INTEIRA. Ex. (reel Kazuo): [(75.905,76.505)]. Vazio = sem bipe (fase2.sh pula)
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
