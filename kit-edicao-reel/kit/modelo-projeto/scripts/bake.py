"""Renderiza offline as faixas pesadas da composição, a partir do edit-plan.json:
  aroll  -> assets/aroll.mp4      (corte do apresentador: takes + L-cuts + velocidade)
  voz    -> assets/voz-mix.m4a    (J-cut: clipes + crossfades no silêncio)
  bed    -> assets/bed.m4a        (trilha com emenda/automação + todos os SFX)
  cenas  -> assets/broll/_cenaNN.mp4 (tomadas seguidas da mesma cena num arquivo)
  brollfull -> assets/broll-full.mp4 (todas as cenas de tela cheia numa faixa, no tempo da timeline)
  leaks  -> assets/leaks.mp4       (todos os light-leaks numa faixa)
Motivo: o Chrome cria um player (e uma sessão de decodificação) por <video>/<audio>; com um
elemento por take a composição passava de 160 elementos e a imagem sumia no preview.
Uso: python3 scripts/bake.py [aroll|voz|bed|cenas ...]   (sem argumento = tudo)
"""
import json, math, os, shutil, subprocess, sys, tempfile
FPS=60                      # quadros do ARQUIVO de saida (2K/60)
P=json.load(open('assets/edit-plan.json'))
# A matematica da TIMELINE (lead do J-cut, duracao minima de take) tem que usar o MESMO fps
# do gerador (plan.fps, 30) — com 60 aqui o lead virava 5/60 e cada take saia 0,083 s mais
# longo: o aroll fechou 3671 quadros contra 3555 da timeline (1,9 s de dessincronia).
TLFPS=P.get('fps',30)
M=json.load(open('work/mix-plan.json'))
RATE=P.get('rate',1.1); TOTAL=M['total']
def run(cmd): subprocess.run(cmd,check=True)
import platform
ENC_AROLL=(['-c:v','libx264','-crf','16','-preset','medium'] if os.environ.get('BAKE_X264') or platform.system()!='Darwin'
           else ['-c:v','h264_videotoolbox','-b:v','45M','-maxrate','60M','-profile:v','high'])
def nf(d): return int(round(d*FPS))

def bake_aroll():
    """Concatena os takes do mezanino já na velocidade final (vídeo mudo)."""
    F=1/TLFPS; LEAD=P.get('jcutLeadFrames',5)*F
    segs=[];t=0
    for i,s in enumerate(P['segments']):
        sd=round((s['out']-s['in'])/RATE,3); lead=0 if i==0 else min(LEAD,sd-10*F); d=round(sd-lead,3)
        segs.append(dict(i=i,**s,lead=lead,dur=d,t0=round(t,3))); t=round(t+d,3)
    ed=[round((s['out']-s['videoTail'])/RATE,3) if s.get('videoTail') else 0 for s in segs]
    tmp=tempfile.mkdtemp(prefix='aroll'); parts=[]
    # fronteiras de quadro ACUMULADAS: cada take começa no quadro em que a timeline o coloca
    # (arredondar take por take somava erro e o arquivo saía 3 quadros curto, tirando o lip-sync)
    jobs=[]
    for k,s in enumerate(segs):
        dPrev=ed[k-1] if k>0 else 0
        vStart=round(s['t0']-dPrev,3); vEnd=round(s['t0']+s['dur']-ed[k],3)
        frames=nf(vEnd)-nf(vStart); vMedia=round(s['in']+(s['lead']-dPrev)*RATE,3)
        out=f'{tmp}/p{k:03d}.mp4'
        jobs.append(['ffmpeg','-v','error','-y','-ss',f'{vMedia:.3f}','-i',P['src'],
             # setpts + fps nesta ordem: com '-r' no lugar do filtro fps o conteúdo saía
             # 2 quadros atrasado dentro de cada take (medido quadro a quadro)
             '-vf',f'setpts=PTS/{RATE},fps={FPS}','-frames:v',str(frames),
             # -g 30: sem GOP denso o renderizador avisa "sparse keyframes ... causes seek
             # failures and frame freezing" e a captura TRAVA num quadro (reel Costco: parou
             # em 572/600, duas vezes no mesmo quadro).
             # crf 16 (era 18): o aroll e' a imagem principal do reel — pedido "sem perder nada de qualidade"
             # kit v3: no Mac, codificador de HARDWARE (VideoToolbox) a 45 Mb/s: 4,3x mais rapido e PSNR igual ou melhor
             # que x264 crf 16 medium (43,9 x 43,7 dB, reel Alan Mulally); GOP 30 respeitado. BAKE_X264=1 volta ao x264.
             *ENC_AROLL,'-pix_fmt','yuv420p',
             '-g','30','-keyint_min','30','-sc_threshold','0','-an',out])
        parts.append(out)
    from concurrent.futures import ThreadPoolExecutor   # kit v3: 3 takes de cada vez
    with ThreadPoolExecutor(3) as ex: list(ex.map(run, jobs))
    lst=f'{tmp}/list.txt'; open(lst,'w').write('\n'.join(f"file '{p}'" for p in parts))
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-c','copy','-movflags','+faststart','assets/aroll.mp4'])
    n=subprocess.run(['ffprobe','-v','error','-select_streams','v','-count_frames','-show_entries','stream=nb_read_frames','-of','csv=p=0','assets/aroll.mp4'],capture_output=True,text=True).stdout.strip().rstrip(',')
    shutil.rmtree(tmp,ignore_errors=True)
    print(f'  aroll.mp4  {int(n)} quadros (timeline {nf(TOTAL)}) · {len(parts)} takes')

def bake_voz():
    """Mix do J-cut: cada take na velocidade final, com fade de crossfade dentro do silêncio."""
    ins=[];fc=[];n=0
    for v in M['voice']:
        ins+=['-ss',f"{v['in']:.3f}",'-t',f"{(v['out']-v['in']):.3f}",'-i',M['voiceSrc']]
        xf=v['xfade']
        f=f"[{n}:a]atempo={RATE},asetpts=N/SR/TB"
        if not v['first']: f+=f",afade=t=in:st=0:d={xf:.3f}"
        f+=f",afade=t=out:st={max(0,v['dur']-xf):.3f}:d={xf:.3f}"
        f+=f",adelay={int(v['start']*1000)}|{int(v['start']*1000)}[a{n}]"
        fc.append(f); n+=1
    fc.append(''.join(f'[a{i}]' for i in range(n))+f'amix=inputs={n}:normalize=0:dropout_transition=0[out]')
    run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[out]',
         '-t',f'{TOTAL:.3f}','-c:a','aac','-b:a','256k','-ar','48000','-ac','2','assets/voz-mix.m4a'])
    print(f'  voz-mix.m4a  {n} takes')

def bake_bed():
    """Trilha (com emenda e automação de volume) + todos os SFX one-shot."""
    T=M['trilha']; V=T['vol']; low=T['lowAt']; loop=T['loop']
    # automação: V até lowAt, 1 s para 0.045, e fade final de 0,7 s
    aut=(f"volume=eval=frame:volume='({V}+({T['fadeLow']}-{V})*max(0,min(1,(t-{low})/1)))"
         f"*(1-max(0,min(1,(t-{TOTAL-T['endFade']})/{T['endFade']})))'")
    ins=[];fc=[];n=0
    if loop:
        at,back,xf=loop['at'],loop['back'],loop.get('xfade',2.5)
        ins+=['-i',T['file']]; fc.append(f"[{n}:a]atrim=0:{at+xf},asetpts=N/SR/TB,afade=t=out:st={at}:d={xf},{aut}[t0]"); n+=1
        ins+=['-ss',f'{at-back:.3f}','-i',T['file']]
        fc.append(f"[{n}:a]atrim=0:{TOTAL-at},asetpts=N/SR/TB,afade=t=in:st=0:d={xf},adelay={int(at*1000)}|{int(at*1000)},{aut}[t1]"); n+=1
        beds=['[t0]','[t1]']
    else:
        ins+=['-i',T['file']]; fc.append(f"[{n}:a]atrim=0:{TOTAL},asetpts=N/SR/TB,{aut}[t0]"); n+=1; beds=['[t0]']
    for s in M['sfx']:
        ins+=['-i',s['file']]
        fc.append(f"[{n}:a]atrim=0:{s['dur']},asetpts=N/SR/TB,volume={s['vol']},adelay={int(s['start']*1000)}|{int(s['start']*1000)}[s{n}]")
        beds.append(f'[s{n}]'); n+=1
    fc.append(''.join(beds)+f'amix=inputs={len(beds)}:normalize=0:dropout_transition=0[out]')
    run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[out]',
         '-t',f'{TOTAL:.3f}','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','assets/bed.m4a'])
    print(f"  bed.m4a  trilha{' + emenda' if loop else ''} + {len(M['sfx'])} SFX")

def bake_cenas():
    """Tomadas seguidas da mesma cena num arquivo só, cada uma cortada no quadro exato."""
    G=json.load(open('work/broll-groups.json')); n=0
    for g in G:
        if len(g['shots'])<2 or not g['file']: continue  # kit v3: split da camada de motion nao tem arquivo
        ins=[];fc=[]
        # fronteiras por quadro ACUMULADO da janela: arredondar tomada a tomada perdia ate um
        # quadro no fim da cena (o arquivo ficava mais curto que a janela do index.html)
        acc=g['t0']; prev=nf(g['t0'])
        for k,sh in enumerate(g['shots']):
            acc=round(acc+sh['dur'],6); cur=nf(acc); nfr=cur-prev; prev=cur
            if k==len(g['shots'])-1: nfr+=3   # folga (como no make_broll): a janela pede ate
            # ceil((start+dur)*30)-1, que cai alguns milissegundos depois do ultimo quadro exato
            ins+=['-i',sh['file']]
            fc.append(f"[{k}:v]trim=end_frame={nfr},setpts=N/{FPS}/TB,setsar=1[v{k}]")
        fc.append(''.join(f'[v{k}]' for k in range(len(g['shots'])))+f"concat=n={len(g['shots'])}:v=1:a=0[out]")
        run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[out]','-r',str(FPS),
             '-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p',
             '-g','30','-keyint_min','30','-sc_threshold','0','-an','-movflags','+faststart',g['file']])
        d=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',g['file']],capture_output=True,text=True).stdout.strip()
        print(f"  {g['file'].split('/')[-1]}  {float(d):.2f}s (janela {g['t1']-g['t0']:.2f}s) · {len(g['shots'])} tomadas"); n+=1
    print(f'  {n} cenas concatenadas')

def _enc(args,out):
    run(['ffmpeg','-v','error','-y',*args,'-c:v','libx264','-crf','18','-preset','medium','-pix_fmt','yuv420p',
         '-g','30','-keyint_min','30','-sc_threshold','0','-an',out])
def _black(n,out):
    _enc(['-f','lavfi','-i',f'color=c=black:s=1440x2560:r={FPS}','-frames:v',str(n)],out)
def _concat(parts,out):
    lst=out+'.txt'; open(lst,'w').write('\n'.join(f"file '{os.path.abspath(p)}'" for p in parts))
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-c','copy','-movflags','+faststart',out]); os.remove(lst)
def _nframes(f):
    return int(subprocess.run(['ffprobe','-v','error','-select_streams','v','-count_frames','-show_entries','stream=nb_read_frames','-of','csv=p=0',f],capture_output=True,text=True).stdout.strip().rstrip(','))

def bake_brollfull():
    """Todas as cenas de B-roll de TELA CHEIA numa faixa so, no tempo exato da timeline (preto entre elas;
    a composicao so mostra a camada dentro das janelas). Um <video> no lugar de ~27: com um player por
    cena + um por light-leak o Chrome esgotava os decoders e o B-roll sumia no preview."""
    G=sorted([g for g in json.load(open('work/broll-groups.json')) if g['mode']!='split'],key=lambda g:g['t0'])
    if not G: print('  broll-full: nenhuma cena de tela cheia em video (camada de motion) — pulado'); return
    tmp=tempfile.mkdtemp(prefix='bfull'); parts=[]; c=0; END=nf(TOTAL)
    for k,g in enumerate(G):
        # conteudo cobre floor(t0) .. ceil(t1): a camada liga em t0 e desliga em t1, entao a imagem
        # tem que existir no quadro inteiro que contem cada borda (senao pisca 1 quadro preto)
        s0=max(c,math.floor(g['t0']*FPS)); e0=min(END,math.ceil(g['t1']*FPS))
        if s0>c: b=f'{tmp}/b{k:03d}.mp4'; _black(s0-c,b); parts.append(b)
        n=e0-s0; o=f'{tmp}/g{k:03d}.mp4'
        _enc(['-i',g['file'],'-vf',f'fps={FPS},scale=1440:2560,setsar=1','-frames:v',str(n)],o)
        got=_nframes(o)
        if got<n: raise SystemExit(f"{g['file']} tem {got} quadros, precisa de {n}")
        parts.append(o); c=e0
    if END>c: b=f'{tmp}/bfim.mp4'; _black(END-c,b); parts.append(b)
    _concat(parts,'assets/broll-full.mp4'); shutil.rmtree(tmp,ignore_errors=True)
    print(f"  broll-full.mp4  {_nframes('assets/broll-full.mp4')} quadros (timeline {END}) · {len(G)} cenas")

def bake_leaks():
    """Todos os light-leaks numa faixa so (preto no resto: com blend screen, preto nao altera a imagem)."""
    L=json.load(open('work/leaks.json')); tmp=tempfile.mkdtemp(prefix='leaks'); END=nf(TOTAL)
    one=f'{tmp}/leak.mp4'; _enc(['-i',L['file'],'-vf',f'fps={FPS},scale=1440:2560,setsar=1'],one); nl=_nframes(one)
    parts=[]; c=0
    for k,x in enumerate(L['leaks']):
        s0=max(c,nf(x['start'])); n=min(nl,END-s0)
        if s0>c: b=f'{tmp}/b{k:03d}.mp4'; _black(s0-c,b); parts.append(b)
        if n<nl: o=f'{tmp}/l{k:03d}.mp4'; _enc(['-i',one,'-frames:v',str(n)],o); parts.append(o)
        else: parts.append(one)
        c=s0+n
    if END>c: b=f'{tmp}/bfim.mp4'; _black(END-c,b); parts.append(b)
    _concat(parts,'assets/leaks.mp4'); shutil.rmtree(tmp,ignore_errors=True)
    print(f"  leaks.mp4  {_nframes('assets/leaks.mp4')} quadros (timeline {END}) · {len(L['leaks'])} leaks")

alvos=sys.argv[1:] or ['cenas','brollfull','leaks','voz','bed','aroll']
for a in alvos: globals()['bake_'+a]()
