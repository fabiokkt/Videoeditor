#!/bin/bash
# QC do MP4 final (reel Gene Kranz): bipe medido no MP4 e na voz-mix, sincronia boca/voz, MD5 do bruto.
# uso: bash work/qc_final.sh
set -e; cd "$(dirname "$0")/.."; export PATH=$HOME/Claude/.venv-reel/bin:$PATH
M=renders/Gene-Kranz-reel-final.mp4; Q=work/qc; mkdir -p $Q
# 1) bipe: janela de timeline do P**** (115,97-116,75 do source -> segmento VIRADA-PORRA-BIPE)
T0=$(python3 - <<'PY'
import json
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30; L=P['jcutLeadFrames']*F; t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(L,sd-10*F); d=round(sd-lead,3)
    if s['in']<=115.97<s['out']: print(round(t+(115.97-s['in'])/R-lead,3)); break
    t=round(t+d,3)
PY
)
ffmpeg -v error -y -i $M -vn -ac 1 -ar 48000 $Q/final48.wav
ffmpeg -v error -y -i assets/voz-mix.m4a -vn -ac 1 -ar 48000 $Q/vozmix48.wav 2>/dev/null || true
python3 - $T0 <<'PY'
import numpy as np, wave, sys
def band(f, t0, t1):
    w = wave.open(f); sr = w.getframerate(); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)
    s = x[int(t0*sr):int(t1*sr)]; X = np.abs(np.fft.rfft(s*np.hanning(len(s))))**2; fr = np.fft.rfftfreq(len(s), 1/sr)
    tot = X.sum()+1e-9; return X[(fr>=950)&(fr<=1050)].sum()/tot, X[(fr<900)|(fr>1100)].sum()/tot
t0 = float(sys.argv[1]) + 0.03; t1 = float(sys.argv[1]) + 0.78/1.1 - 0.03
for f in ['work/qc/final48.wav', 'work/qc/vozmix48.wav']:
    a, b = band(f, t0, t1); print(f'bipe {f}: {a*100:.1f}% em 950-1050 Hz · {b*100:.1f}% fora de 900-1100 Hz ({t0:.2f}-{t1:.2f} s)')
PY
# 2) sincronia boca/voz
ffmpeg -v error -y -i $M -vn -ac 1 -ar 16000 $Q/final16k.wav
ffmpeg -v error -y -i ~/Claude/videos-brutos/gene-kranz-bruto.mov -vn -ac 1 -ar 16000 $Q/bruto16k.wav
node scripts/sync-check.mjs $Q/final16k.wav $Q/bruto16k.wav | tail -4
# 3) bruto intacto
echo "MD5 bruto agora: $(md5sum ~/Claude/videos-brutos/gene-kranz-bruto.mov | cut -d' ' -f1) · antes: 7be4c0dc2d6909d92cefa8883bb274db"
