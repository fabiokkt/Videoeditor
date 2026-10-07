"""POR VIDEO — reel ERNEST SHACKLETON. Mapa dos slots em tempo ABSOLUTO de timeline (rate 1.1, timeline 93,272 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava assets/broll-slots.json.
Kit v3: MG={"*"} — toda cobertura e da camada de motion (compositions/mg.html, gerada por work/mg/gen.py); os splits
continuam no plan.broll com file "" (o split arrasta o apresentador).
Olhar (gaze_pose 2.0: 13 janelas / 2,7 s; gaze_windows: 31 / 12,8 s; conferido nas folhas gaze/me/g00-g02): o apresentador olha para a camera
o tempo todo — so piscadas e desvios minimos (o maior, 16,19-16,50, fica coberto pela foto do gelo). Leitura exposta: 0 s.
Capa em split 0-5,52 (o gancho inteiro); pre-revelacao 5,52-10,40 (o Endurance no gelo, nada do Shackleton); apresentador no callout de
digitacao (10,40-12,13); revelacao em 12,13 ("Ernest" em 12,06 + 2 quadros); split 2 (a virada) 63,42-66,30; climax 81,30 (o bote);
apresentador em "E nao perdeu um homem" (callout), "senta do seu lado", "manter o seu carro", no bipe (59,63-63,42) e no fecho/CTA (85,33-fim)."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- INTRO EM SPLIT (PRE-REVELACAO: nada do Shackleton antes de "Ernest", 12,06 s) ---
 ("s01","split", 0.00,  5.52,"Esse cara é um dos exploradores mais fracassados e mais admirados do planeta Terra.","CAPA gerada a pedido (Shackleton de costas diante do Endurance esmagado, à noite)","—"),
 ("s02","full",  5.52, 10.40,"E ele criou um protocolo polêmico pra provar que o funcionário que reclama você não afasta.","fotos: o Endurance à noite no gelo (Hurley, 1915) → o navio preso no gelo do mar de Weddell","6,01–6,56 · 9,47–9,84"),
 # --- REVELACAO ---
 ("s03","full", 12.13, 19.10,"Ernest ficou quase dois anos preso no gelo na Antártida. Sem rádio pra pedir socorro, comendo pinguim.","REVELAÇÃO: retrato do Shackleton na expedição + nome → o navio preso (QUASE 2 ANOS · SEM RÁDIO) → pinguins","16,19–16,50"),
 # --- PASSO 1 ---
 ("s04","full", 24.76, 35.06,"Primeiro, põe o reclamão do seu lado. No gelo, ele botou um dos mais encrenqueiros pra dormir na barraca dele. Ele sabia que reclamão longe do chefe junta torcida.","MOTION chip PASSO 1 + título → foto: Hurley e Shackleton no acampamento → MOTION a torcida (o reclamão longe do chefe junta gente)","24,79–25,28"),
 # --- PASSO 2 ---
 ("s05","full", 38.47, 47.12,"Segundo, você larga primeiro. Ele mandou cada homem largar quase tudo no gelo. E o primeiro a jogar fora foi ele: as moedas de ouro.","MOTION chip PASSO 2 + título → foto: o acampamento no gelo (MENOS DE 1 KG POR HOMEM) → MOTION as moedas de ouro caindo na neve","42,47–42,80"),
 # --- PASSO 3 ---
 ("s06","full", 50.38, 59.63,"E terceiro, ninguém fica parado. Ele sabia que homem parado no gelo começa a reclamar. Então tinha tarefa todo dia e até o futebol no gelo.","MOTION chip PASSO 3 + título → foto: a noite longa no gelo → foto: abrindo caminho no gelo (TAREFA TODO DIA) + a bola (FUTEBOL NO GELO)","50,26–50,94 · 51,69–51,94 · 53,07–53,34 · 54,13–54,41"),
 # --- SEGUNDO SPLIT (A VIRADA) ---
 ("s07","split",63.42, 66.30,"E a virada foi um motim. O navio afundou,","fotos: o Endurance adernado pelo gelo → o naufrágio (nov/1915)","65,13–65,41"),
 ("s08","full", 66.30, 81.30,"e o carpinteiro, o mais reclamão de todos, parou de puxar o bote: sem navio, ninguém manda em mim. Ernest leu o contrato pra todo mundo e avisou: o salário continua até o porto. Acabou o motim. Era medo, não rebeldia.","foto: os homens puxando o bote → MOTION a fala do carpinteiro, o contrato (SALÁRIO ATÉ O PORTO), FIM DO MOTIM, MEDO × REBELDIA","67,46–68,01 · 69,52–69,74 · 71,16–71,35 · 80,11–80,35"),
 # --- CLIMAX ---
 ("s09","full", 81.30, 85.33,"Meses depois, no bote que foi buscar socorro, o carpinteiro foi junto.","CLÍMAX: o lançamento do James Caird em Elephant Island, abril de 1916","81,36–82,02 · 82,48–82,78 · 83,05–83,36 · 84,17–84,72"),
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
