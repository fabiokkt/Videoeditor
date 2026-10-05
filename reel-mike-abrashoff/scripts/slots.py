"""POR VIDEO — reel MIKE ABRASHOFF. Mapa dos slots em tempo ABSOLUTO de timeline (rate 1.1, timeline 96,654 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava assets/broll-slots.json.
Kit v3: MG={"*"} — toda cobertura e da camada de motion (compositions/mg.html, gerada por work/mg/gen.py); os splits
continuam no plan.broll com file "" (o split arrasta o apresentador).
Layout desenhado a mao sobre as janelas NITIDAS de gaze/me (gaze_pose 2.0): 8,05-8,32 · 54,15-54,30 · 94,49-94,88 — todas cobertas.
37,7-38,9 (olha o celular) e de proposito (nota de gravacao) e fica no apresentador com o bipe.
Capa em split 0-7,22; revelacao em 12,78 ("Mike" em 12,71 s + 2 quadros); split 2 (a virada) 70,75-78,55; climax 81,44
(continencia); apresentador no callout "VAI EMBORA POR SUA CAUSA" (10,70-12,78), no bipe (36,05-39,40) e no fim do CTA (94,95-fim)."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- INTRO EM SPLIT (PRE-REVELACAO: nada do Mike/Benfold antes de "Mike", 12,71 s) ---
 ("s01","split", 0.00,  7.22,"Esse cara é um dos capitães mais rebeldes… e ele criou um protocolo polêmico","CAPA gerada a pedido (de costas, cais à noite) → canhão de destróier à noite (só fotos)","—"),
 ("s02","full",  7.22, 10.70,"pra provar que o seu funcionário não vai embora por salário.","foto: proa de destróier furando onda (USS Barry, sem nome legível)","olhada 8,05–8,32"),
 # --- REVELACAO ---
 ("s03","full", 12.78, 21.27,"Mike pegou um dos piores navios… sete meses depois, o mais preparado… com a mesma tripulação.","REVELAÇÃO: USS Benfold + nome → MOTION ranking PIOR → 1º (7 MESES) sobre o míssil → tripulação na amurada","—"),
 # --- PASSO 1 ---
 ("s04","full", 25.19, 36.05,"Primeiro, olha na cara de quem fala… salário era o quinto motivo. O primeiro… respeito.","MOTION chip PASSO 1 → foto: oficial conversando com marinheiro no Benfold → MOTION ranking dos motivos (5º salário, 1º respeito)","—"),
 # --- PASSO 2 ---
 ("s05","full", 39.40, 45.30,"Segundo, pergunta: o que você mudaria? Perguntou pros trezentos e dez marinheiros, um por um.","MOTION chip PASSO 2 + pergunta → contador 0 → 310 UM POR UM","—"),
 ("s06","full", 49.35, 57.15,"A gente pinta esse navio a cada dois meses… Trocaram o parafuso. A Marinha inteira copiou.","foto: marinheiros pintando o casco → ferrugem → silhuetas no Benfold + carimbo PADRÃO DA MARINHA","olhada 54,15–54,30"),
 # --- PASSO 3 ---
 ("s07","full", 57.15, 62.68,"E terceiro, pede pra ficar. Meses antes do contrato acabar, ele chamava o marinheiro:","MOTION chip PASSO 3 → foto: reengajamento (mão levantada)","—"),
 ("s08","full", 64.34, 67.10,"Você só pergunta isso quando o cara já pediu demissão.","MOTION: carta PEDIDO DE DEMISSÃO + carimbo TARDE DEMAIS","—"),
 # --- SEGUNDO SPLIT (A VIRADA) ---
 ("s09","split",70.75, 78.55,"E a virada foi uma despedida. O capitão antigo desceu do navio com a família. E a tripulação comemorou.","fotos: troca de comando → comandante saindo do navio → marinheiros comemorando","—"),
 # --- CLIMAX ---
 ("s10","full", 81.44, 87.98,"Dois anos depois, ele bateu continência pra tripulação e desceu. Não tinha um olho seco no navio.","CLÍMAX: comandante batendo continência ao sair (1999) → abraço no cais","—"),
 ("s11","full", 92.39, 94.95,"Se você acha que ninguém mais quer trabalhar, me segue,","foto: a mesma tripulação na amurada (volta da revelação)","olhada 94,49–94,88"),
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
    P['broll']=plan_broll(lambda s:f"assets/broll/_ph/{s['id']}.mp4"); P['_broll']="PLACEHOLDERS (cartoes rotulados) — slots aguardando os B-rolls do usuario. Ver PESQUISAS-BROLL-KAZUO-INAMORI.md."
    json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1); print("plan.broll -> placeholders")
if '--real' in sys.argv:
    P['broll']=plan_broll(lambda s:s['file']); json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1); print("plan.broll -> arquivos finais")
