#!/bin/bash
# QC do MP4 final (reel Ernest Shackleton): bipe medido no MP4 e na voz-mix, sincronia boca/voz, MD5 do bruto, folha de quadros.
# uso: bash work/qc_final.sh
set -e; cd "$(dirname "$0")/.."; export PATH=$HOME/Claude/.venv-reel/bin:$PATH
M=renders/Ernest-Shackleton-reel-final.mp4; Q=work/qc; mkdir -p $Q
# 1) bipe: janela de timeline do M**** (87,85-88,32 do source -> 61,11 + 0,47/1,1)
ffmpeg -v error -y -i $M -vn -ac 1 -ar 48000 $Q/final48.wav
ffmpeg -v error -y -i assets/voz-mix.m4a -vn -ac 1 -ar 48000 $Q/vozmix48.wav 2>/dev/null || true
python3 - <<'EOF'
import numpy as np, wave
def band(f, t0, t1):
    w = wave.open(f); sr = w.getframerate(); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)
    s = x[int(t0*sr):int(t1*sr)]; X = np.abs(np.fft.rfft(s*np.hanning(len(s))))**2; fr = np.fft.rfftfreq(len(s), 1/sr)
    tot = X.sum()+1e-9; return X[(fr>=950)&(fr<=1050)].sum()/tot, X[(fr<900)|(fr>1100)].sum()/tot
t0 = 61.11 + 0.03; t1 = 61.11 + 0.47/1.1 - 0.03
for f in ['work/qc/final48.wav', 'work/qc/vozmix48.wav']:
    try: a, b = band(f, t0, t1); print(f'bipe {f}: {a*100:.1f}% em 950-1050 Hz · {b*100:.1f}% fora de 900-1100 Hz ({t0:.2f}-{t1:.2f} s)')
    except Exception as e: print('bipe', f, 'erro', e)
EOF
# 2) sincronia boca/voz
ffmpeg -v error -y -i $M -vn -ac 1 -ar 16000 $Q/final16k.wav
ffmpeg -v error -y -i ~/Claude/videos-brutos/ernest-shackleton-bruto.mov -vn -ac 1 -ar 16000 $Q/bruto16k.wav
node scripts/sync-check.mjs $Q/final16k.wav $Q/bruto16k.wav | tail -4
# 3) bruto intacto
echo "MD5 bruto agora: $(md5sum ~/Claude/videos-brutos/ernest-shackleton-bruto.mov | cut -d' ' -f1) · antes: $(cat work/md5-bruto.txt)"
