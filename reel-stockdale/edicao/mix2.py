import wave,numpy as np
SR=44100
def load(f):
    w=wave.open(f);assert w.getframerate()==SR
    return np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32).reshape(-1,2)/32768
def save(f,a):
    w=wave.open(f,"wb");w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR)
    w.writeframes((np.clip(a,-1,1)*32767).astype(np.int16).tobytes())
S=lambda t:int(round(t*SR))
voice=load("voice44.wav"); stem=load("sep/htdemucs/ref44/no_vocals.wav")
refmix=load("ref44.wav"); refv=load("sep/htdemucs/ref44/vocals.wav")
N=len(voice)

# 1) tira os whooshes/censura embutidos na cama (picos acima da mediana local)
def despike(x,start=4.4):
    hop=S(0.05);n=len(x)//hop
    e=np.array([np.sqrt((x[i*hop:(i+1)*hop]**2).mean())+1e-9 for i in range(n)])
    from numpy.lib.stride_tricks import sliding_window_view as sw
    med=np.median(sw(np.pad(e,15,mode='edge'),31),axis=1)[:n]
    g=np.minimum(1,(med*1.6)/e)
    g[:int(start/0.05)]=1
    g=np.convolve(g,np.ones(3)/3,'same')
    gs=np.interp(np.arange(len(x)),np.arange(n)*hop+hop/2,g)
    return x*gs[:,None]
bed=despike(stem)

# 2) remapeia a trilha da referência para a nossa estrutura
segs=[(0.0,0.0,69.7),(69.7,73.0,78.5),(75.2,55.0,61.6),(81.8,78.5,89.9)]
music=np.zeros((N+S(1),2),np.float32);XF=S(0.15)
for k,(dst,a,b) in enumerate(segs):
    src=(stem if k==1 else bed)[S(a):S(b)].copy()
    if k>0: src[:XF]*=np.linspace(0,1,XF)[:,None]
    if k<len(segs)-1: src[-XF:]*=np.linspace(1,0,XF)[:,None]
    d=S(dst);music[d:d+len(src)]+=src
music=music[:N]

# 3) mesma proporção voz/música da referência
rv=np.sqrt((refv[S(5):S(89)]**2).mean()); ov=np.sqrt((voice[S(5):S(89)]**2).mean())
music*=ov/rv

# 4) whoosh nos light leaks (amostra da referência, pico 0,3 s depois do início)
wh=stem[S(15.0):S(15.6)].copy();wh[:S(0.03)]*=np.linspace(0,1,S(0.03))[:,None];wh[-S(0.1):]*=np.linspace(1,0,S(0.1))[:,None]
wh*=ov/rv
fx=np.zeros_like(voice)
for t in [8.16,11.02,15.06,25.82,35.84,42.96,47.94,56.58,66.14,72.20,77.06]:
    d=S(t-0.30);fx[d:d+len(wh)]+=wh[:max(0,min(len(wh),N-d))]

# 5) censura: corta o fim do palavrão e põe o som da referência (48,98–49,16)
c0,c1=S(38.70),S(38.96);v=voice.copy()
r=S(0.006);v[c0-r:c0]*=np.linspace(1,0,r)[:,None];v[c0:c1]=0;v[c1:c1+r]*=np.linspace(0,1,r)[:,None]
cz=refmix[S(48.98):S(49.16)]*(ov/np.sqrt((refmix[S(5):S(89)]**2).mean()))
fx[c0:c0+len(cz)]+=cz

save("mix2_raw.wav",v+music+fx)
print("music gain",ov/rv)
