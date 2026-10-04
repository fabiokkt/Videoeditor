"""POR VIDEO — reel DEMING. Mapa dos slots em tempo ABSOLUTO de timeline (rate 1.1, timeline 101,31 s).
Kit v3: TODO slot vira camada de motion (compositions/mg.html); os splits continuam no plan.broll com file "" (o split arrasta
o apresentador; a faixa de cima e da camada). Layout desenhado sobre as folhas gaze/me/g*.jpg — nitidas: 11,58 · 14,04 ·
30,46-30,70 · 33,38-33,59 · 45,20 · 84,02-84,55 · 95,17-95,41 (todas cobertas por motion). Revelacao em 11,37 ("Deming" em 11,30 s);
apresentador no bipe (34,26-36,72); split 2 (a virada) 71,34-75,99; climax 90,00 ("Uma em cada cinco bolinhas")."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 ("s01","split", 0.00, 11.37,"Esse cara é um dos americanos mais ignorados… E ele criou um protocolo polêmico… não resolve nada.","CAPA (Codex, a pedido): aula na fábrica japonesa em 1950, professor de costas → crachás trocados + DEMITIDO (pré-revelação)","— (quadro 0 = capa)"),
 ("s02","full", 11.37, 21.68,"Deming foi dar aulas pras fábricas do Japão… medalha do imperador… prêmio com o nome dele.","REVELAÇÃO: retrato (Wikipedia) → aula em Tóquio 1950 (JUSE) → medalha do imperador (JUSE + Commons) → Prêmio Deming (JUSE)","olhadas 11,58 · 14,04"),
 ("s03","full", 25.30, 34.26,"…continuar com o mesmo problema. Primeiro, troca o culpado. Já trocou três vendedores…","loop de crachás · chip PASSO 1 · três vendedores e a venda parada","olhadas 30,46–30,70 · 33,38–33,59"),
 ("s04","full", 36.72, 42.33,"De cada cem problemas, noventa e quatro são do jeito que a empresa funciona.","grade de 100 pontos, 94 do sistema","—"),
 ("s05","full", 45.10, 55.37,"Segundo, acaba com o ranking… um contra o outro… esconde o cliente do colega","chip PASSO 2 · ranking de vendedores","olhada 45,20"),
 ("s06","full", 57.23, 64.90,"E terceiro, arranca o cartaz da parede. Aquele “Aqui a gente faz certo da primeira vez.”","chip PASSO 3 · cartaz motivacional arrancado","—"),
 ("s07","full", 68.04, 71.34,"Seu time ri do cartaz no almoço, pequeno gafanhoto.","balões kkkk + Mestre Po (Kung Fu)","olhadas 68,97–70,46"),
 ("s08","split",71.34, 75.99,"E a virada foi uma caixa de bolinhas. Ele montava uma fábrica de mentira.","a caixa de contas: brancas e vermelhas","—"),
 ("s09","full", 75.99, 87.94,"Seis voluntários tiravam bolinha com uma pá… elogiava… xingava… demitia os piores… não diminuía.","a pá de 50 furos · placar dos 6 · elogio/bronca · DEMITIDO · gráfico parado","olhadas 76,5 · 78,98 · 84,02–84,55 · 86,40"),
 ("s10","full", 90.00, 92.81,"Uma em cada cinco bolinhas era vermelha.","CLÍMAX: 5 bolinhas, 1 vermelha — 20% (riser + impact)","—"),
 ("s11","full", 94.67, 95.86,"Olha a caixa.","volta à caixa (callback da virada)","olhada 95,17–95,41"),
]
NOMES={k[0]:k[0] for k in S}
def seg_of(x, end=False):
    for i,(a,b) in enumerate(segs):
        if (a<=x<b) if not end else (a<x<=b+1e-6): return i
    return len(segs)-1
slots=[]
for sid,mode,t0,t1,fala,tema,cobre in S:
    f=seg_of(t0); g=seg_of(t1,end=True); w0,w1=segs[f][0],segs[g][1]
    sp=[round((t0-w0)/(w1-w0),5),round((t1-w0)/(w1-w0),5)]
    slots.append(dict(id=sid,file=f"assets/broll/{NOMES[sid]}.mp4",mode=mode,fromSeg=f,toSeg=g,span=sp,
                      t0=t0,t1=t1,dur=round(t1-t0,2),fala=fala,tema=tema,cobre=cobre))
old={x['id']:x for x in json.load(open('assets/broll-slots.json')).get('slots',[])} if os.path.exists('assets/broll-slots.json') else {}
for s in slots:  # preserva campos da pesquisa (img, link, fonte, prompt...) ja gravados
    for k,v in old.get(s['id'],{}).items():
        if k not in s: s[k]=v
json.dump({"total":TOTAL,"slots":slots},open('assets/broll-slots.json','w'),ensure_ascii=False,indent=1)
print(f"{len(slots)} slots · timeline {TOTAL}s")
# POR VIDEO: slots que viraram motion graphics (compositions/mg.html, docs/13): ficam no broll-slots.json (tempos de
# referencia) e saem do plan.broll. Vazio = todo slot vira video de B-roll (fluxo antigo).
MG={"*"}  # "*" = TODO slot vira camada de motion (kit v3, padrao). set() = fluxo antigo (todo slot vira video)
def plan_broll(path_of):
    # kit v3: slot MG em split continua no plano com file "" (o split arrasta o apresentador; a faixa de cima e da camada)
    return [{k:s[k] for k in ('mode','fromSeg','toSeg','span')}|{"file":("" if ('*' in MG or s['id'] in MG) else path_of(s))} for s in slots
            if not ('*' in MG or s['id'] in MG) or s['mode']=='split']
if '--placeholders' in sys.argv:
    from PIL import Image, ImageDraw, ImageFont
    os.makedirs('assets/broll/_ph',exist_ok=True)
    try: fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',46); fs=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',30)
    except Exception: fnt=fs=ImageFont.load_default()
    for k,s in enumerate(slots):
        W,H=(720,1280) if s["mode"]=="full" else (720,564)
        im=Image.new('RGB',(W,H),[(38,52,86),(70,44,86),(40,78,70),(86,62,36)][k%4]); d=ImageDraw.Draw(im)
        y=H*0.30 if s['mode']=='full' else 60
        for line in [f"B-ROLL {s['id']}", "aguardando arquivo", NOMES[s['id']]+".mp4", f"{s['dur']:.2f}s"]:
            d.text((W/2,y),line,font=fnt if line.startswith('B-') else fs,fill=(255,255,255),anchor='mm'); y+=70
        png=f"assets/broll/_ph/{s['id']}.png"; im.save(png)
        subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-i',png,'-t',f"{s['dur']+0.2:.2f}",'-r','60','-c:v','libx264','-pix_fmt','yuv420p','-g','30','-crf','30',f"assets/broll/_ph/{s['id']}.mp4"],check=True)
    P['broll']=plan_broll(lambda s:f"assets/broll/_ph/{s['id']}.mp4"); P['_broll']="PLACEHOLDERS (cartoes rotulados) — slots aguardando os B-rolls do usuario. Ver PESQUISAS-BROLL-DEMING.md."
    json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1); print("plan.broll -> placeholders")
if '--real' in sys.argv:
    P['broll']=plan_broll(lambda s:s['file']); json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1); print("plan.broll -> arquivos finais")
