"""POR VIDEO — reel KAZUO INAMORI. Foto escolhida por slot (work/pesq/slot-picks.json) -> assets/broll-src/<slot>.jpg (original)
e o recorte de ENTREGA no aspecto do slot: assets/broll-src/entrega/<slot>-9x16.jpg (tela cheia) ou <slot>-16x9.jpg (split).
ax/ay = ancora do recorte (0 = esquerda/topo, 1 = direita/base). fill = foto inteira sobre fundo borrado (foto pequena ou
assunto largo demais para o 9:16). Folha de conferencia: work/pesq/sheet_entrega.jpg"""
import json, shutil
from PIL import Image, ImageFilter, ImageDraw, ImageFont
PK={ # slot: (candidata, ax, ay, fill[, box]) — box = pre-recorte (x0,y0,x1,y1 em fracao) antes do aspecto
 "s01":("C1",.5,.2,0), "s02":("c04a_7",.5,.5,0), "s03":("C2",.5,.3,0), "s04":("d02a_11",.5,.35,0),
 "s05":("b03a_9",.5,.5,0), "s06":("b03a_2",.5,.2,0), "s07":("b05a_7",.6,.5,0),
 "s08":("b07a_0",.5,.5,1,(.1,.0,.9,1.0)), "s09":("b08b_10",.5,.5,1,(.15,.0,.85,1.0)), "s10":("b03c_19",.5,.5,0), "s11":("c09b_6",.5,.5,1),
 "s12":("b10b_11",.5,.5,0), "s13":("po-1",.65,.5,0), "s14":("d12a_3",.5,.5,0), "s15":("b13a_0",.5,.5,0),
 "s16":("b12a_11",.5,.5,0), "s17":("b15a_18",.5,.5,0), "s18":("b18c_6",.5,.5,1,(.15,.0,1.0,1.0)), "s19":("c18a_15",.5,.5,1,(.2,.0,.8,1.0)),
 "s20":("b19c_16",.5,.5,1,(.1,.0,.9,1.0)), "s21":("d20a_4",.5,.5,0)}
S={s['id']:s for s in json.load(open('assets/broll-slots.json'))['slots']}
json.dump({k:v[0] for k,v in PK.items()},open('work/pesq/slot-picks.json','w'),indent=1)
th=[]; fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',26)
for sid,(cid,ax,ay,fill,*bx) in PK.items():
    im=Image.open(f'work/pesq/cand/{cid}.jpg').convert('RGB')
    if bx: W0,H0=im.size; x0,y0,x1,y1=bx[0]; im=im.crop((int(W0*x0),int(H0*y0),int(W0*x1),int(H0*y1)))
    shutil.copy(f'work/pesq/cand/{cid}.jpg',f'assets/broll-src/{sid}.jpg')
    split=S[sid]['mode']=='split'; A=16/9 if split else 9/16; W,H=im.size
    if fill:  # foto inteira na largura do quadro, sobre a propria foto ampliada e borrada
        cw,ch=(2560,1440) if split else (1440,2560)   # canvas na resolucao de saida (antes: altura da foto -> 487x866)
        bg=im.resize((int(ch*W/H),ch)) if W/H<A else im.resize((cw,int(cw*H/W)))
        bg=bg.resize((cw,ch)).filter(ImageFilter.GaussianBlur(45))
        if fill==2:  # fundo liso (foto de estudio com fundo de cor unica: o borrado mostrava o produto borrado)
            import numpy as np; a=np.asarray(im); bd=np.concatenate([a[:8].reshape(-1,3),a[-8:].reshape(-1,3),a[:,:8].reshape(-1,3),a[:,-8:].reshape(-1,3)])
            bg=Image.new('RGB',(cw,ch),tuple(int(x) for x in np.median(bd,0)))
        fg=im.resize((cw,int(cw*H/W))); out=bg.copy(); out.paste(fg,(0,(ch-fg.size[1])//2))
    else:
        if W/H>A: cw,ch=int(H*A),H
        else: cw,ch=W,int(W/A)
        x0=int((W-cw)*ax); y0=int((H-ch)*ay); out=im.crop((x0,y0,x0+cw,y0+ch))
    p=f"assets/broll-src/entrega/{sid}-{'16x9' if split else '9x16'}.jpg"; out.save(p,quality=93)
    t=out.copy(); t.thumbnail((360,360)); c=Image.new('RGB',(360,380),(20,20,20)); c.paste(t,((360-t.size[0])//2,0))
    ImageDraw.Draw(c).text((6,352),f"{sid} {cid} {out.size[0]}x{out.size[1]}",font=fnt,fill=(255,255,0)); th.append(c)
    print(sid,cid,out.size)
sh=Image.new('RGB',(360*7,380*((len(th)+6)//7)),(40,40,40))
for i,c in enumerate(th): sh.paste(c,(360*(i%7),380*(i//7)))
sh.save('work/pesq/sheet_entrega.jpg',quality=85)
