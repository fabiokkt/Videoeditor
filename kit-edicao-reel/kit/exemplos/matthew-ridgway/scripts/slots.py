"""POR VIDEO — reel MATTHEW RIDGWAY. Mapa dos slots em tempo ABSOLUTO de timeline (rate 1.1, timeline 96,189 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava assets/broll-slots.json.
Kit v3: MG={"*"} — toda cobertura e da camada de motion (compositions/mg.html, gerada por work/mg/gen.py); os splits
continuam no plan.broll com file "" (o split arrasta o apresentador).
Olhar (gaze_pose 2.0 + gaze_windows, conferido nas folhas gaze/me): o apresentador olha para a camera quase o tempo todo. Nitidas: 2,90-3,32
(capa: o split encurta para 0-2,75 e a capa abre em tela cheia antes da olhada) e 90,10-90,60 ("Cade o plano de ataque?", coberta pela camada).
Sutis/piscada expostas: 9,45-9,62 · 22,10-22,25 · 54,77-54,99 · 70,32-70,50 · 93,71-94,02.
Capa em split 0-2,75 + capa em tela cheia 2,75-5,23 (o gancho); pre-revelacao 5,23-9,45 (soldados na neve, nada do Ridgway); revelacao em 10,93
("Matthew" em 10,86 + 2 quadros); split 2 (a virada) 72,29-76,51; climax 83,50 (a capital); apresentador no callout de digitacao (9,45-10,93), no bipe
(37,52-42,64) e no CTA (91,23-fim)."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- INTRO EM SPLIT (PRE-REVELACAO: nada do Ridgway antes de "Matthew", 10,86 s) ---
 ("s01","split", 0.00,  2.75,"Esse cara é um dos generais mais brutos…","CAPA gerada a pedido (general de costas na nevasca, jipe com farol)","—"),
 ("s02","full",  2.75,  9.70,"…e mais paizões dos Estados Unidos. E ele criou um protocolo polêmico pra provar que o seu time não tá desmotivado.","capa em tela cheia → soldados na neve (Coreia, inverno de 1950)","2,90–3,32 (leitura) · 5,34–5,53 · 9,01–9,45"),
 # --- REVELACAO ---
 ("s03","full", 10.93, 19.54,"Matthew andava com uma granada no peito e pregou na parede, de presente pro general inimigo, uma calça de pijama rasgada na bunda.","REVELAÇÃO: Ridgway com a granada no suspensório (1951) + nome → MOTION a parede: o bilhete ao comandante inimigo e a calça de pijama rasgada","15,07–15,23"),
 # --- PASSO 1 ---
 ("s04","full", 24.47, 37.52,"Primeiro, resolve a luva. O soldado nem reclamava mais. Ele diz que teve que arrancar: faltava luva, comida quente e envelope… Resolveu antes de falar em atacar.","MOTION chip PASSO 1 + título → foto: soldados exaustos no frio → MOTION a lista do que faltava (LUVA, COMIDA QUENTE, ENVELOPE → RESOLVIDO; ATACAR depois)","28,39–28,54 · 32,35–32,72 · 33,41–33,60 · 36,10–36,62"),
 # --- PASSO 2 ---
 ("s05","full", 42.64, 52.65,"Segundo, aparece no frio. Ele rodou três dias na linha de frente num jipe aberto, na neve. Ele diz que o soldado precisa ver o chefe passando o mesmo frio.","MOTION chip PASSO 2 + título → foto: Ridgway no jipe aberto → foto: Ridgway com a tropa no inverno","50,80–50,95"),
 # --- PASSO 3 ---
 ("s06","full", 56.30, 68.44,"E terceiro, chama pelo nome. Ele reconhecia uns cinco mil soldados de cara, e parava na estrada só pra dizer: bom trabalho. Ele dizia que isso levantava um batalhão inteiro.","MOTION chip PASSO 3 + título → contador 5.000 → foto: Ridgway falando com um soldado + balão BOM TRABALHO → foto: a tropa","56,26–56,53 · 61,13–61,44 · 62,22–62,53 · 63,37–63,53"),
 # --- SEGUNDO SPLIT (A VIRADA) ---
 ("s07","split",72.29, 76.51,"E a virada foi uma pergunta. Um oficial mostrou pra ele um plano de recuar.","fotos: oficiais no mapa (posto de comando)","—"),
 ("s08","full", 76.51, 83.50,"Ele perguntou: o plano de ataque? O cara gaguejou: senhor, a gente tá recuando. Dias depois, o cara tava fora.","MOTION a conversa: PLANO DE RECUO, balões, FORA","82,11–82,36"),
 # --- CLIMAX + FECHO ---
 ("s09","full", 83.50, 91.23,"Em menos de três meses, o exército que fugia retomou a capital. Sua empresa tem plano pra cortar custo, meu amigo? Cadê o plano de ataque?","CLÍMAX: soldados na neve (volta da abertura) → a tropa avançando / Seul, março de 1951 → MOTION as pastas: PLANO DE CORTE DE CUSTOS × PLANO DE ATAQUE (vazia)","83,59–83,81 · 90,10–90,60 (leitura)"),
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
    P['broll']=plan_broll(lambda s:f"assets/broll/_ph/{s['id']}.mp4"); P['_broll']="PLACEHOLDERS (cartoes rotulados) — slots aguardando os B-rolls do usuario. Ver LICENCAS-FOTOS.txt."
    json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1); print("plan.broll -> placeholders")
if '--real' in sys.argv:
    P['broll']=plan_broll(lambda s:s['file']); json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1); print("plan.broll -> arquivos finais")
