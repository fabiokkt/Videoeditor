"""POR VIDEO — reel GORDON BETHUNE. Bipe de censura gravado na voz, na palavra INTEIRA
(fala: "E a porra do calote fica com voce, meu querido.").
Entrada: work/gordon-bethune-voz-limpa.m4a (audio do bruto) -> assets/gordon-bethune-voz.m4a (voz do projeto)
e work/full.wav (mono, o que o cuts.py le). Transcricao continua usando work/full-clean.wav (sem bipe).
Mapa (envelope 10 ms + bandas, source): "E a" 53,78-53,93 · oclusao /p/ 53,94-54,09 (decaimento do "a" ate -34 dB, sem agudos) · explosao 54,10 ·
"o" 54,11-54,28 · "rr" 54,29-54,33 · "a" 54,34-54,41 · /d/ de "do" 54,42-54,46 · "o" 54,47-54,51 · oclusao /k/ de "calote" 54,52-54,57.
O whisper pos "porra" ~0,3 s adiantado (53,79-54,20). Recortes cumulativos do audio limpo: de 54,42 em diante "do calote e fica com voce,
meu querido" (nada da palavra); de 54,30 e 54,10 ainda "Porra do calote" (o whisper completa palavra previsivel, docs/05 §9).
Bipe 53,95-54,42 (palavra inteira, da oclusao do /p/ ao fim do "a").
Varredura da transcricao INTEIRA (36 regioes, inclusive as descartadas): so este palavrao (o roteiro marca 1 piiii; o r12 descartado
"E porra do ca..." fica fora do corte)."""
import numpy as np, subprocess, wave, json, os
VOZ=json.load(open('assets/edit-plan.json'))['voiceSrc']                      # assets/<slug>-voz.m4a (voz do projeto, COM bipe)
LIMPA='work/'+os.path.basename(VOZ).replace('.m4a','-limpa.m4a')             # work/<slug>-voz-limpa.m4a (audio do bruto, SEM bipe)
JANELAS=[(53.95,54.42)]  # POR VIDEO: [(ini, fim)] em s do source, palavra INTEIRA. Ex. (reel Kazuo): [(75.905,76.505)]. Vazio = sem bipe (fase2.sh pula)
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
