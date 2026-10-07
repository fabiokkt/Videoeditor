"""POR VIDEO — reel STANLEY McCHRYSTAL. Mapa dos slots em tempo ABSOLUTO de timeline (rate 1.1, timeline 93,39 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava assets/broll-slots.json.
Kit v3: MG={"*"} — toda cobertura e da camada de motion (compositions/mg.html, gerada por work/mg/gen.py); os splits
continuam no plan.broll com file "" (o split arrasta o apresentador).
Olhar (gaze_pose 2.0 + gaze_windows, conferido nas folhas gaze/me): o apresentador olha para a camera quase o tempo todo; nenhuma leitura
nitida. Sutis cobertas pela camada: 13,34-14,53 · 15,98-16,16 · 32,48-32,66 · 46,00-46,64 · 50,14-50,44 · 56,82-58,64 · 68,99-69,18 · 70,42-70,61 ·
76,80-77,13 ("ninguem lia", olho para baixo) · 79,29-83,54. Expostas (sutis/piscada, olho no lugar): 11,05-11,48 · 23,97-24,42 (o gesto do apito,
"juiz da briga": labios em bico, nao e leitura) · 38,91-39,09 · 53,80-53,95 · 65,22-65,50 · 66,46-66,65 ("meu querido", olho para baixo) · 84,70-87,91 · 91,93-92,50.
Capa em split 0-5,19 (o gancho inteiro); pre-revelacao 5,19-10,45 (visao noturna no Iraque, nada do Stanley); revelacao em 11,81 ("Stanley" em
11,74 + 2 quadros); split 2 (a virada) 67,63-69,70; climax 78,14 (soldado + analista -> 18 -> 300). Apresentador no callout de digitacao (10,45-11,81),
no "juiz da briga" (21,92-27,45), em "so gente prometendo prazo" (37,63-41,40), no "nao o encostado" (51,55-56,70), no bipe (63,00-67,63) e no fecho/CTA (84,40-fim)."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- INTRO (PRE-REVELACAO: nada do Stanley antes de "Stanley", 11,74 s) ---
 ("s01","split", 0.00,  5.191,"Esse cara e um dos generais mais malucos e mais temidos dos Estados Unidos.","CAPA gerada a pedido (general de costas no corredor, visao noturna, quartinho dos sacos)","—"),
 ("s02","full",  5.191, 10.45,"E ele criou um protocolo polemico pra provar que seu comercial e sua operacao nao se odeiam.","visao noturna no Iraque (soldados, 2004-2006) — nada do Stanley","5,21-5,49 · 7,51-8,33"),
 # --- REVELACAO ---
 ("s03","full", 11.81, 21.918,"Stanley comandava as forcas especiais americanas no Iraque, dormia quatro horas, comia uma vez por dia e proibiu Burger King pros proprios soldados.","REVELACAO: retrato de 2003 + nome → no aviao com o laptop (4 H DE SONO · 1 REFEICAO POR DIA) → MOTION as lanchonetes da base: PROIBIDO","13,34-14,53 · 15,98-16,16 · 18,49-19,22"),
 # --- PASSO 1 ---
 ("s04","full", 27.45, 37.626,"Primeiro, todo mundo na mesma reuniao. Ele fazia uma reuniao por dia com ate sete mil pessoas. Ele diz que time excelente, trabalhando separado, perde.","MOTION chip PASSO 1 + titulo → a reuniao diaria: grade de telas + 7.000 → fotos: dois times separados (sala de operacoes × visao noturna) + carimbo PERDE","28,50-29,23 · 30,29-30,61 · 32,48-32,66 · 34,13-34,70"),
 # --- PASSO 2 ---
 ("s05","full", 41.40, 51.553,"Segundo, empresta o seu melhor. Ele mandava os melhores passar seis meses em outro time. Ele diz que quem trabalha do lado de la para de ver rival.","MOTION chip PASSO 2 + titulo → foto: um time em roda (6 MESES NO OUTRO TIME) → foto: Stanley agachado com soldados afegaos","42,05-42,87 · 46,00-46,64 · 47,84-48,41 · 50,14-50,44"),
 # --- PASSO 3 ---
 ("s06","full", 56.70, 63.007,"E terceiro, abre tudo. Ele diz que a meta e todo mundo saber tudo, o tempo todo.","MOTION chip PASSO 3 + titulo → retrato de 4 estrelas + a frase dele (Stanford GSB)","56,82-58,64"),
 # --- SEGUNDO SPLIT (A VIRADA) ---
 ("s07","split",67.634, 69.698,"E a virada foi um quartinho.","a capa de volta: a porta do quartinho com os sacos","68,96-69,21"),
 ("s08","full", 69.698, 84.399,"Os soldados arriscavam a vida de madrugada pra pegar papel e computador do inimigo. Ia tudo ensacado pro quartinho, e ninguem lia. Ele juntou soldado e analista, e as operacoes foram de dezoito por mes pra mais de trezentas.","fotos: incursao noturna (visao noturna) → MOTION o quartinho: os sacos caem e empilham, NINGUEM LIA → foto: Stanley e o chefe de inteligencia na mesa (SOLDADO + ANALISTA) → CLIMAX barras 18 → 300+","69,97-70,76 · 72,64-73,25 · 76,80-77,13 · 79,29-79,54 · 80,47-84,14"),
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
