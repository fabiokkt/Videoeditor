#!/bin/bash
# QC do MP4 final (reel Bob Chapman): bipe medido no MP4 e na voz-mix (janela achada pelo tom de 1 kHz), sincronia boca/voz, MD5 do bruto.
# uso: bash work/qc_final.sh
set -e; cd "$(dirname "$0")/.."; export PATH=$HOME/Claude/.venv-reel/bin:$PATH
M=renders/Bob-Chapman-reel-final.mp4; Q=work/qc; mkdir -p $Q
ffmpeg -v error -y -i $M -vn -ac 1 -ar 48000 $Q/final48.wav
ffmpeg -v error -y -i assets/voz-mix.m4a -vn -ac 1 -ar 48000 $Q/vozmix48.wav 2>/dev/null || true
python3 - <<'PY'
import numpy as np, wave
def load(f):
    w = wave.open(f); sr = w.getframerate(); return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32), sr
def band(x, sr, t0, t1):
    s = x[int(t0*sr):int(t1*sr)]; X = np.abs(np.fft.rfft(s*np.hanning(len(s))))**2; fr = np.fft.rfftfreq(len(s), 1/sr)
    tot = X.sum()+1e-9; return X[(fr>=950)&(fr<=1050)].sum()/tot, X[(fr<900)|(fr>1100)].sum()/tot
x, sr = load('work/qc/vozmix48.wav')
# acha a janela do bipe na voz-mix: blocos de 10 ms com > 90% da energia em 950-1050 Hz entre 51 e 54 s
on = [t for t in np.arange(51.0, 54.0, 0.01) if band(x, sr, t, t+0.02)[0] > 0.9]
t0, t1 = (min(on), max(on)+0.02) if on else (52.0, 52.5)
print(f'bipe achado na voz-mix: {t0:.2f}-{t1:.2f} s ({t1-t0:.2f} s)')
for f in ['work/qc/final48.wav', 'work/qc/vozmix48.wav']:
    y, s2 = load(f); a, b = band(y, s2, t0+0.02, t1-0.02)
    print(f'bipe {f}: {a*100:.1f}% em 950-1050 Hz · {b*100:.1f}% fora de 900-1100 Hz')
PY
ffmpeg -v error -y -i $M -vn -ac 1 -ar 16000 $Q/final16k.wav
ffmpeg -v error -y -i ~/Claude/videos-brutos/bob-chapman-bruto.mov -vn -ac 1 -ar 16000 $Q/bruto16k.wav
node scripts/sync-check.mjs $Q/final16k.wav $Q/bruto16k.wav | tail -4
echo "MD5 bruto agora: $(md5sum ~/Claude/videos-brutos/bob-chapman-bruto.mov | cut -d' ' -f1) · antes: $(cat work/md5-bruto.txt)"
