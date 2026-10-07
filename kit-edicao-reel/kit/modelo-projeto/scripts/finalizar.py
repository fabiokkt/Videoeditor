"""Fecha o export: audio final + mux das partes + QC. NOVO no kit v2 (2026-10-01): junta os comandos que eram digitados a cada reel.
Uso: python3 scripts/finalizar.py renders/<Nome>-reel-final.mp4 [--fps 60] [--sem-preto]
Pre-requisito: todas as partes em renders/chunks/chunk-NN.mp4 (work/render-all.sh) e assets/voz-mix.m4a + assets/bed.m4a (bake.py).
 1. renders/_audio.m4a = amix(voz-mix, bed, normalize=0) + alimiter a -1 dBTP.
    `level=disabled` e obrigatorio: com o auto-level (padrao) o limiter normaliza de volta para 0 dB.
 2. mux direto da lista de partes + _audio.m4a, video COPIADO, SEM -shortest (ele decepa o ultimo quadro),
    com -frames:v = quadros da timeline (a ultima parte pode vir com +1 quadro).
 3. QC: quadros = timeline · duracoes A/V · pico e media (volumedetect) · trechos pretos (blackdetect).
Nao confere sincronia boca/voz (scripts/sync-check.mjs) nem compara quadros-chave com o preview — fazer a parte."""
import json, glob, math, os, re, subprocess, sys
out=sys.argv[1]; FPS=int(sys.argv[sys.argv.index('--fps')+1]) if '--fps' in sys.argv else 60
TOTAL=json.load(open('work/mix-plan.json'))['total']; NF=math.ceil(TOTAL*FPS-1e-6)
def sh(c): return subprocess.run(c,capture_output=True,text=True)
def nq(f): return int(sh(['ffprobe','-v','error','-select_streams','v:0','-count_packets','-show_entries','stream=nb_read_packets','-of','csv=p=0',f]).stdout.strip().rstrip(','))
parts=sorted(glob.glob('renders/chunks/chunk-[0-9][0-9].mp4'))
q=[nq(p) for p in parts]; soma=sum(q)
print(f"timeline {TOTAL}s = {NF} quadros @{FPS} · {len(parts)} partes · soma {soma}")
if not (NF<=soma<=NF+1): raise SystemExit(f"PARTES NAO FECHAM: soma {soma}, timeline {NF} — {list(zip([os.path.basename(p) for p in parts],q))}")
os.makedirs('renders',exist_ok=True)
subprocess.run(['ffmpeg','-v','error','-y','-i','assets/voz-mix.m4a','-i','assets/bed.m4a','-filter_complex',
  '[0:a][1:a]amix=inputs=2:normalize=0:dropout_transition=0,alimiter=limit=0.891:level=disabled[a]','-map','[a]',
  '-t',f'{TOTAL:.3f}','-c:a','aac','-b:a','256k','-ar','48000','-ac','2','renders/_audio.m4a'],check=True)
open('renders/parts.txt','w').write('\n'.join(f"file '{os.path.abspath(p)}'" for p in parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','renders/parts.txt','-i','renders/_audio.m4a',
  '-map','0:v','-map','1:a','-c','copy','-frames:v',str(NF),'-movflags','+faststart',out],check=True)
# ---- QC ----
pr=lambda s,e: sh(['ffprobe','-v','error','-select_streams',s,'-show_entries',e,'-of','csv=p=0',out]).stdout.strip().rstrip(',')
w,hh,fr=pr('v:0','stream=width,height,r_frame_rate').split(','); dv=float(pr('v:0','stream=duration')); da=float(pr('a:0','stream=duration'))
fq=nq(out); ok=fq==NF
vd=sh(['ffmpeg','-v','info','-i',out,'-vn','-af','volumedetect','-f','null','-']).stderr
pico=float(re.search(r'max_volume: ([-\d.]+)',vd)[1]); media=float(re.search(r'mean_volume: ([-\d.]+)',vd)[1])
print(f"{out}: {w}x{hh} @{fr} · {fq} quadros ({'= timeline' if ok else 'DIFERENTE da timeline '+str(NF)}) · video {dv:.3f}s / audio {da:.3f}s · {os.path.getsize(out)/1e6:.0f} MB")
print(f"audio: pico {pico} dB (alvo -1; nunca 0) · media {media} dB")
if pico>-0.3: ok=False; print("  PICO ALTO — o limiter nao atuou")
if abs(dv-da)>2/FPS: ok=False; print("  A/V com mais de 2 quadros de diferenca")
if '--sem-preto' not in sys.argv:
    bd=sh(['ffmpeg','-v','info','-i',out,'-an','-vf','scale=180:-2,blackdetect=d=0.05:pic_th=0.98','-f','null','-']).stderr
    pretos=re.findall(r'black_start:([\d.]+) black_end:([\d.]+)',bd)
    print(f"trechos pretos: {len(pretos)} {pretos or ''}")
    if pretos: ok=False
print("QC OK" if ok else "QC COM PROBLEMA"); sys.exit(0 if ok else 1)
