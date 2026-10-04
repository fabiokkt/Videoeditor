"""Renderiza os B-rolls a partir das fotos reais em assets/broll-src/ (padrão do formato, sem fal.ai).
POR VÍDEO: editar a lista S (um slot por foto; dur = data-duration da janela no index.html).
Fotos com lado menor < ~900 px em tela cheia: usar fill=1 (foto inteira sobre fundo borrado).
Move APENAS a camera sobre a foto (push-in / pan / crane) — como nada e' gerado por
modelo, texto, logotipo e marca ficam matematicamente identicos ao original: zero
morphing, zero deformacao. Saida em assets/broll/."""
import json, math, subprocess, os
FPS=60
# out: 1080x846 nos splits (a faixa de 44%), 1080x1920 nos cutaways de tela cheia
# ax/ay: ancora do recorte (0=esq/topo, .5=centro, 1=dir/base)
# z0,z1: zoom no inicio/fim · dx,dy: deriva em fracao da janela · fill: fundo borrado
# dim: escurece a foto (produto sobre fundo branco) para a legenda branca SEM contorno ter
#      contraste. A legenda do formato so tem sombra-halo; sobre estudio branco ela some.
S=[
 # reel KAZUO INAMORI — 21 tomadas (scripts/slots.py), fotos recortadas em assets/broll-src/entrega/ (PESQUISAS-BROLL-KAZUO-INAMORI.md)
 # movimento = o do prompt de cada slot. Splits: 1440x1128 (faixa de 44%); tela cheia: 1440x2560
 dict(id="s01-split-capa-monge-pista", src="s01", w=1440,h=1128, ax=0.50,ay=0.50, z0=1.00,z1=1.04, dx= 0.00,dy= 0.00, dim=0.00),  # CAPA: conceito do monge na pista (4:3 inteira: monge e aviao acima da caixa do gancho)
 dict(id="s02-monge-temido", src="entrega/s02-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy=-0.02, dim=0.00),  # monge de costas no templo
 dict(id="s03-split-protocolo-polemico", src="s03", w=1440,h=1128, ax=0.50,ay=0.50, z0=1.03,z1=1.05, dx= 0.04,dy= 0.00, dim=0.00),  # conceito da reuniao (capa B)
 dict(id="s04-split-esconde-numero", src="entrega/s04-16x9", w=1440,h=1128, ax=0.80,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy= 0.00, dim=0.00),  # homem escondendo o papel (callout de digitacao)
 dict(id="s05-kazuo-revelacao", src="entrega/s05-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.06, dx= 0.00,dy=-0.01, dim=0.00),  # REVELACAO: retrato
 dict(id="s06-virou-monge", src="entrega/s06-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.03,z1=1.06, dx= 0.00,dy=-0.05, dim=0.00),  # Inamori de monge (tilt para cima)
 dict(id="s07-jal-sem-salario", src="entrega/s07-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.05,z1=1.05, dx= 0.00,dy= 0.05, dim=0.00),  # pulpito sob o logo JAL (tilt para baixo)
 dict(id="s08-quebra-em-pedacinhos", src="entrega/s08-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.05,z1=1.05, dx= 0.04,dy= 0.00, dim=0.00),  # equipe Kyocera (travelling esq->dir)
 dict(id="s09-briga-pelo-lucro", src="entrega/s09-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy= 0.00, dim=0.00),  # equipe de punho erguido
 dict(id="s10-empresa-inteira", src="entrega/s10-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.04,z1=1.06, dx= 0.00,dy=-0.06, dim=0.00),  # sede da Kyocera (tilt para cima)
 dict(id="s11-conta-de-casa", src="entrega/s11-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy= 0.00, dim=0.00),  # kakeibo + calculadora
 dict(id="s12-painel-do-aviao", src="entrega/s12-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.06, dx= 0.00,dy= 0.00, dim=0.00),  # cockpit 787
 dict(id="s13-pequeno-gafanhoto", src="entrega/s13-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.06, dx= 0.00,dy=-0.01, dim=0.00),  # Mestre Po
 dict(id="s14-orcamento-gastar-tudo", src="entrega/s14-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.05,z1=1.05, dx= 0.00,dy= 0.05, dim=0.00),  # pilha de papeis ACCEPTED (tilt para baixo)
 dict(id="s15-verba-de-dezembro", src="entrega/s15-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy= 0.00, dim=0.00),  # nota em chamas
 dict(id="s16-split-reuniao", src="entrega/s16-16x9", w=1440,h=1128, ax=0.50,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy= 0.00, dim=0.00),  # Inamori entre dois executivos
 dict(id="s17-split-bilhao-de-ienes", src="entrega/s17-16x9", w=1440,h=1128, ax=0.40,ay=0.50, z0=1.05,z1=1.05, dx= 0.05,dy= 0.00, dim=0.00),  # macos de ienes (travelling esq->dir)
 dict(id="s18-aprovado-no-orcamento", src="entrega/s18-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.05,z1=1.05, dx=-0.04,dy= 0.00, dim=0.00),  # diretores da JAL (travelling dir->esq)
 dict(id="s19-climax-rastejando", src="entrega/s19-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.06, dx= 0.00,dy= 0.00, dim=0.00),  # CLIMAX: reverencia na pista
 dict(id="s20-recorde-de-lucro", src="entrega/s20-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.04,z1=1.04, dx= 0.04,dy=-0.02, dim=0.00),  # 787 da JAL decolando
 dict(id="s21-unico-que-liga", src="entrega/s21-9x16", w=1440,h=2560, ax=0.50,ay=0.50, z0=1.00,z1=1.05, dx= 0.00,dy= 0.00, dim=0.00),  # sozinho com as contas
]
import sys
def _janelas():
    """Duracao de cada tomada = janela do slot (assets/broll-slots.json), casada pelo nome do arquivo."""
    return {x['file'].split('/')[-1][:-4]: x['dur'] for x in json.load(open('assets/broll-slots.json'))['slots']}
W=_janelas()
for _s in S:
    _s['dur']=W[_s['id']]   # janela do slot na timeline; o script soma 0,1 s
ONLY=sys.argv[sys.argv.index('--only')+1].split(',') if '--only' in sys.argv else None
os.makedirs('assets/broll',exist_ok=True)
for s in S:
    if ONLY and not any(s['id'].startswith(o) for o in ONLY): continue
    import glob as _g
    src=_g.glob(f"assets/broll-src/{s['src']}.*")[0]
    W,H=s['w'],s['h']; A=W/H
    sw,sh=[int(x) for x in subprocess.run(['ffprobe','-v','error','-show_entries',
        'stream=width,height','-of','csv=p=0',src],capture_output=True,text=True).stdout.strip().split(',')]
    N=int(math.ceil((s['dur']+0.10)*FPS))
    # 1,5x nos splits; 1,25x em tela cheia. A 1,5x o buffer do zoompan fica 2160x3840 e o
    # ffmpeg leva SIGKILL no Air de 8 GB (aconteceu em 3 tomadas). 1,25x = 1800x3200 passa.
    K=1.5 if H<2000 else 1.15
    UW,UH=int(W*K)//2*2,int(H*K)//2*2
    if s.get('pan'):
        # travelling puro em tela cheia: crop movel numa copia 2x, depois reduz
        x0,x1=s['pan']; K=1.5; CW,CH=int(W*K),int(H*K); ph=s.get('ph',1.0)
        vf=(f"[0:v]scale=-2:{int(CH/ph)}:flags=lanczos,"
            f"crop={CW}:{CH}:x='(iw-ow)*({x0}+({x1}-{x0})*min(1,n/{N-1}))':y='(ih-oh)*{s['ay']}',"
            f"scale={W}:{H}:flags=lanczos,unsharp=5:5:0.55:5:5:0.0"
            +(f",eq=brightness={-s['dim']}:contrast=1.04:saturation=1.06" if s.get('dim') else "")
            +f",format=yuv420p[v]")
        out=f"assets/broll/{s['id']}.mp4"
        subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-i',src,'-filter_complex',vf,
            '-map','[v]','-frames:v',str(N),'-r',str(FPS),'-c:v','libx264','-crf','17',
            '-preset','slow','-pix_fmt','yuv420p','-g','30','-keyint_min','30','-sc_threshold','0',
            '-an','-movflags','+faststart',out],check=True)
        dd=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out],
            capture_output=True,text=True).stdout.strip()
        print(f"  {s['id']:<20} {W}x{H} {N:>4}f  {float(dd):.2f}s  (janela {s['dur']:.2f}s) [travelling]")
        continue
    if s.get('fill'):
        # foto ajustada a largura + fundo borrado dela mesma (preserva a cena inteira).
        # ANTES disso, `far` (fit aspect ratio) recorta a foto para um formato mais ALTO:
        # sem ele uma foto 16:9 ocupa so ~32% da altura do 9:16 e a tarja borrada domina a tela.
        # far e' escolhido por foto pelo maior recorte que nao passa de ~1,8x de ampliacao.
        far=s.get('far')
        if far:
            if sw/sh > far: fw,fh=int(round(sh*far)),sh; fx,fy=int(round((sw-fw)*s.get('ax',.5))),0
            else:           fw,fh=sw,int(round(sw/far)); fx,fy=0,int(round((sh-fh)*s.get('ay',.5)))
            src_chain=f"[0:v]crop={fw}:{fh}:{fx}:{fy},split=2[c0][c1];"
            a,b="[c0]","[c1]"
        else:
            src_chain=""; a,b="[0:v]","[0:v]"
        pre=(src_chain+
             f"{a}scale={UW}:{UH}:force_original_aspect_ratio=increase:flags=lanczos,"
             f"crop={UW}:{UH},gblur=sigma=54,eq=brightness=-0.16:saturation=0.75[bg];"
             f"{b}scale={UW}:-2:flags=lanczos[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2[base];")
    else:
        if sw/sh > A: cw,ch=int(round(sh*A)),sh; cx,cy=int(round((sw-cw)*s['ax'])),0
        else:         cw,ch=sw,int(round(sw/A)); cx,cy=0,int(round((sh-ch)*s['ay']))
        pre=(f"[0:v]crop={cw}:{ch}:{cx}:{cy},scale={UW}:{UH}:flags=lanczos[base];")
    # DOIS PASSOS quando ha fundo borrado: o composite (crop + gblur sigma 54 + overlay) e o
    # zoompan no mesmo processo estouram a RAM do Air de 8 GB (SIGKILL). O passo 1 grava o
    # quadro-base em PNG; o passo 2 so faz a camera em cima dele.
    # DOIS PASSOS SEMPRE (nao so no fill): com foto de 12 MP o crop+scale junto com o zoompan
    # no mesmo processo leva SIGKILL no Air de 8 GB (aconteceu na 02f, 3024x4032). O passo 1
    # grava o quadro-base ja no tamanho final em PNG; o passo 2 so faz a camera em cima dele.
    base_png=f"work/base_{s['id']}.png"
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-filter_complex',
        pre[:-1].replace('[base]','[out]'),'-map','[out]','-frames:v','1',base_png],check=True)
    src=base_png; pre="[0:v]null[base];"
    # easing (skill showreel-interface, lei 1 "antecipacao -> rajada -> assentamento"): ease='out' faz a camera chegar com
    # velocidade logo depois da transicao e ASSENTAR devagar (1-(1-p)^2.2); sem 'ease' = linear. Nasceu no reel ALAN MULALLY.
    p=f"(on/{N-1})" if s.get('ease')!='out' else f"(1-pow(1-on/{N-1},2.2))"
    z=f"({s['z0']}+({s['z1']}-{s['z0']})*{p})"
    xc=f"(iw-iw/zoom)/2"; yc=f"(ih-ih/zoom)/2"
    xe=f"max(0,min(iw-iw/zoom,{xc}+(iw/zoom)*{s['dx']}*({p}-0.5)))"
    ye=f"max(0,min(ih-ih/zoom,{yc}+(ih/zoom)*{s['dy']}*({p}-0.5)))"
    dim=f",eq=brightness={-s['dim']}:contrast=1.04:saturation=1.06" if s.get('dim') else ""
    vf=(pre+f"[base]zoompan=z='{z}':x='{xe}':y='{ye}':d={N}:s={W}x{H}:fps={FPS},"
        f"unsharp=5:5:0.55:5:5:0.0{dim},format=yuv420p[v]")
    out=f"assets/broll/{s['id']}.mp4"
    subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-i',src,'-filter_complex',vf,
        '-map','[v]','-frames:v',str(N),'-r',str(FPS),'-c:v','libx264','-crf','17',
        '-preset','slow','-pix_fmt','yuv420p','-g','30','-keyint_min','30','-sc_threshold','0',
        '-an','-movflags','+faststart',out],check=True)
    d=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out],
        capture_output=True,text=True).stdout.strip()
    print(f"  {s['id']:<20} {W}x{H} {N:>4}f  {float(d):.2f}s  (janela {s['dur']:.2f}s)")
