"""POR VIDEO — reel GENE KRANZ. Bipe de censura gravado na voz, na palavra INTEIRA
(fala: "Ele juntou o time e disse, nenhum de nos levantou e gritou: porra, para!" — o roteiro marca "porra... piiii, para!").
Entrada: work/gene-kranz-voz-limpa.m4a (audio do bruto) -> assets/gene-kranz-voz.m4a (voz do projeto)
e work/full.wav (mono, o que o cuts.py le). Transcricao continua usando work/full-clean.wav (sem bipe).
Mapa (envelope 20 ms + bandas, source): fim do "gritou" 115,80-115,94 · oclusao /p/ 115,96-116,02 (-48 dB) · "po" 116,04-116,22 ·
vao 116,24-116,36 (-47 a -58 dB) · "rra" 116,38-116,72 (vogal aberta, gritada) · oclusao do /p/ de "para" 116,74-116,90 · "para!" 116,92-117,26.
Whisper em recortes do audio limpo: ate 116,03 e ate 116,30 "...levantou e gritou..." (sem a palavra); ate 116,74 "...gritou, porra,";
de 116,74 so "Para...". Bipe 115,97-116,75 (palavra inteira, da oclusao do /p/ ao fim do "rra"; o /p/ de "para" fica limpo).
Varredura da transcricao INTEIRA (40 regioes, inclusive as descartadas): so este palavrao (o r25, descartado, tem o mesmo)."""
import numpy as np, subprocess, wave, json, os
VOZ=json.load(open('assets/edit-plan.json'))['voiceSrc']                      # assets/<slug>-voz.m4a (voz do projeto, COM bipe)
LIMPA='work/'+os.path.basename(VOZ).replace('.m4a','-limpa.m4a')             # work/<slug>-voz-limpa.m4a (audio do bruto, SEM bipe)
JANELAS=[(115.97,116.75)]  # POR VIDEO: [(ini, fim)] em s do source, palavra INTEIRA. Ex. (reel Kazuo): [(75.905,76.505)]. Vazio = sem bipe (fase2.sh pula)
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
