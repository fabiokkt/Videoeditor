"""POR VIDEO — reel GENE KRANZ. Mapa dos slots em tempo ABSOLUTO de timeline (rate 1.1, timeline ~93,25 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava assets/broll-slots.json.
Kit v3: MG={"*"} — toda cobertura e da camada de motion (compositions/mg.html, gerada por work/mg/gen.py); os splits
continuam no plan.broll com file "" (o split arrasta o apresentador).
Olhar: ver EDICAO.md (folhas gaze/me). Capa em split (o gancho inteiro); pre-revelacao so com fotos (o time da Apollo 13, nada do rosto do Kranz);
apresentador no callout de digitacao; revelacao 2 quadros depois de "Gene"; split 2 (a virada); climax na Apollo 13; apresentador no bipe e no fecho/CTA."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
import importlib.util as _iu
_sp=_iu.spec_from_file_location('tempos','work/mg/tempos.py'); _m=_iu.module_from_spec(_sp); _sp.loader.exec_module(_m); T=_m.T
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- INTRO EM SPLIT (PRE-REVELACAO: nada do rosto do Kranz antes de "Gene") ---
 ("s01","split", T['A0'], T['A1'],"Esse cara é um dos chefes mais frios e mais temidos da história da NASA.","CAPA gerada a pedido (homem de costas, colete branco, sala de controle no escuro, alarme vermelho) → a sala de controle de Houston, 1965","—"),
 ("s02","full",  T['P0'], T['P1'],"E ele criou um protocolo polêmico pra provar que o seu time não esconde problema de você.","fotos: o time da Apollo 13 em volta do console (abr/1970) → controladores e astronautas no console","—"),
 # --- REVELACAO ---
 ("s03","full",  T['B0'], T['B1'],"Gene usava um colete branco costurado pela esposa em toda missão, e comandava a sala no dia que o homem pousou na Lua.","REVELAÇÃO: Kranz de colete branco no console (1972) + nome + anel no colete → a sala da Apollo 11 → Aldrin na Lua","—"),
 # --- PASSO 1 ---
 ("s04","full",  T['D0'], T['D1'],"Primeiro, pressa não é desculpa. Ele diz que o time correu tanto pra bater o prazo que parou de ver os problemas de todo dia. Você promete entrega pra sexta sabendo que não dá, e reza.","MOTION chip PASSO 1 + título → foto: a nave da Apollo 1 na montagem (jan/1967) → MOTION a semana com a sexta marcada (NÃO DÁ)","—"),
 # --- PASSO 2 ---
 ("s05","full",  T['F0'], T['F1'],"Segundo, ficar quieto também é erro. Ele diz que ser duro é responder pelo que você faz e pelo que você deixa de fazer. Ninguém no seu time te avisa de nada?","MOTION chip PASSO 2 + título → foto: Kranz no console (1965) + O QUE FAZ / O QUE DEIXA DE FAZER → MOTION avisos do time: 0","—"),
 # --- PASSO 3 ---
 ("s06","full",  T['H0'], T['H1'],"E terceiro, não chuta. Deu problema, ele falou: vamos resolver, mas sem piorar chutando. Primeiro descobre o que aconteceu, depois mexe.","MOTION chip PASSO 3 + título → foto: a sala na crise da Apollo 13 + a fala do Kranz → MOTION lista 1 DESCOBRE / 2 MEXE","—"),
 # --- SEGUNDO SPLIT (A VIRADA) ---
 ("s07","split", T['L0'], T['L1'],"E a virada foi numa segunda-feira.","foto: Kranz na mesa de imprensa (1966)","—"),
 ("s08","full",  T['N0'], T['N1'],"Em 1967, três astronautas morreram num incêndio na nave, num teste no chão. Todo mundo via problema. Ninguém parou.","foto: a tripulação da Apollo 1 (Grissom, White, Chaffee) → a nave no Pad 34 (jan/1967) → MOTION problemas: VISTO / VISTO / VISTO · ALGUÉM PAROU? NINGUÉM","—"),
 # --- CLIMAX ---
 ("s09","full",  T['C0'], T['C1'],"Três anos depois, a Apollo 13 explodiu a caminho da Lua. Mesma sala, mesmo chefe. Os três voltaram vivos.","CLÍMAX: o módulo de serviço da Apollo 13 sem o painel → Kranz de costas na sala (13 abr 1970) → a tripulação viva no USS Iwo Jima","—"),
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
