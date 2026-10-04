"""Normaliza o broll1.mp4 entregue pelo Fabio para os 3 usos do INTRO SPLIT.
Velocidade NORMAL (os cortes internos dele dao o ritmo) e MUDO.
 01a split  broll1[0.000-3.350]  1440x1128  (fachada + vitrine + inicio do close)
 01c full   broll1[3.350-4.300]  1440x2560  (miolo do close do relogio) -> cobre H01+H02
 01b split  broll1[4.300-5.950]  1440x1128  (fim do close + entrada da boutique)
O 'full' usa CROP 9:16 direto ancorado na coroa (x=190): com FILL o relogio virava uma
faixa pequena entre duas tarjas borradas (conferido lado a lado). O texto do mostrador desta
peca de estoque tem uma linha de letra miuda DEFORMADA: o recorte em x=190 deixa ela fora do quadro.
"""
import subprocess
SRC='assets/broll/broll1.mp4'; MARGEM=0.15
CUTS=[("01a","split",0.000,3.350),("01c","full",3.350,4.300),("01b","split",4.300,5.950)]
COM=['-c:v','libx264','-crf','17','-preset','slow','-pix_fmt','yuv420p',
     '-g','30','-keyint_min','30','-sc_threshold','0','-an','-movflags','+faststart',
     '-colorspace','bt709','-color_trc','bt709','-color_primaries','bt709','-color_range','tv']
for sid,modo,a,b in CUTS:
    dur=round(b-a+MARGEM,3)
    out=f'assets/broll/{sid}.mp4'
    if modo=='split':
        W,H=1440,1128
        vf=(f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,"
            f"crop={W}:{H},fps=60,setsar=1,format=yuv420p")
    else:
        W,H=1440,2560
        vf=(f"[0:v]crop=405:720:190:0,scale={W}:{H}:flags=lanczos,"
            f"unsharp=5:5:0.6:5:5:0,fps=60,setsar=1,format=yuv420p[v]")
    cmd=['ffmpeg','-v','error','-y','-ss',f'{a:.3f}','-t',f'{dur:.3f}','-i',SRC]
    cmd += (['-filter_complex',vf,'-map','[v]'] if modo=='full' else ['-vf',vf])
    subprocess.run(cmd+COM+[out],check=True)
    d=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out],
                     capture_output=True,text=True).stdout.strip()
    n=subprocess.run(['ffprobe','-v','error','-select_streams','v','-count_frames',
                      '-show_entries','stream=nb_read_frames,width,height','-of','csv=p=0',out],
                     capture_output=True,text=True).stdout.strip()
    print(f"  {sid}.mp4  {modo:<5} {n}  {float(d):.2f}s  (janela {b-a:.2f}s)")
