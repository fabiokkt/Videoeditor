"""POR VIDEO — reel RICH DIVINEY. Mapa das janelas de cobertura em tempo ABSOLUTO de timeline (rate 1.1, timeline 92,944 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava assets/broll-slots.json.
Kit v3: todo slot e da camada de motion (MG={"*"}); os splits continuam no plano (arrastam o apresentador).
Layout desenhado a mao sobre gaze/pose-windows.json (gaze_pose.py 2.0) — janelas NITIDAS cobertas: 20,8-21,9 · 30,5-30,9 ·
74,3-74,8 · 75,6-75,8 · 87,6-87,8. Capa em split 0-10,97 (pre-revelacao so com fotos); revelacao em 10,97 ("Rich" em 10,90 s);
split 2 (a virada) 65,15-71,19; climax 79,25 ("Nadar, a gente ensina. Coragem..."); apresentador no bipe (40,40-42,30) e no CTA."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 ("s01","split", 0.00, 10.97,"Esse cara é um dos militares mais carrascos… não sabe fazer o trabalho.","CAPA + PRÉ-REVELAÇÃO: treino de SEALs (sem o Rich)","— (quadro 0 = capa)"),
 ("s02","full", 10.97, 14.39,"Rich escolhia quem entrava na elite da elite dos SEALs.","REVELAÇÃO: retrato do Rich Diviney + nome","—"),
 ("s03","full", 14.39, 18.69,"Só os melhores SEALs se candidatavam e metade reprovava.","SEALs em formação → 10 candidatos, 5 reprovados","sutil 16,1–16,3 s"),
 ("s04","full", 20.60, 25.30,"…parar de se apaixonar por currículo. Primeiro, separa o que dá pra ensinar.","currículo com coração → chip PASSO 1","nítida 20,8–21,9 s"),
 ("s05","full", 27.30, 30.95,"Dá pra ensinar? Planilha, dá. Paciência, não dá.","lista da vaga: planilha ✓ ensina · paciência ✗","nítida 30,5–30,9 s"),
 ("s06","full", 36.05, 38.90,"Segundo, pergunta pelo pior dia.","chip PASSO 2","—"),
 ("s07","full", 38.90, 40.40,"Ele diz que a pessoa só mostra quem é","treino extremo (exaustão, lama, frio)","—"),
 ("s08","full", 42.30, 45.90,"Na entrevista, me conta o dia que tudo deu errado… O que você fez?","cartão da pergunta de entrevista","—"),
 ("s09","full", 50.10, 54.24,"E terceiro, antes de mandar embora, troca de cadeira.","chip PASSO 3","—"),
 ("s10","full", 54.24, 61.15,"Ele tinha uma marinheira que não rendia… e ela decolou.","marinheira trabalhando → convés de voo (decolagem)","—"),
 ("s11","split",65.15, 71.19,"E a virada foi uma piscina. Ele conta que o moleque apareceu… pro teste de natação.","piscina de treinamento dos SEALs","—"),
 ("s12","full", 71.19, 76.00,"Pulou, afundou e atravessou a piscina andando no fundo. Subiu sem ar.","teste de natação / debaixo d'água","nítidas 74,3–74,8 · 75,6–75,8 s"),
 ("s13","full", 79.25, 84.40,"Nadar, a gente ensina. Coragem de aparecer ali, ninguém ensina.","CLÍMAX: ficha do candidato (natação ✗ ensina · coragem ✓ ninguém ensina)","—"),
 ("s14","full", 87.27, 89.01,"Nadar a gente ensina.","volta à piscina da capa","nítida 87,6–87,8 s"),
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
