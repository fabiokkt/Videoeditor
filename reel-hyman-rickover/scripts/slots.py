"""POR VIDEO — reel HYMAN RICKOVER. Mapa dos slots em tempo ABSOLUTO de timeline (rate 1.1, timeline 91,088 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava assets/broll-slots.json.
Kit v3: MG={"*"} — toda cobertura e da camada de motion (compositions/mg.html, gerada por work/mg/gen.py); os splits
continuam no plan.broll com file "" (o split arrasta o apresentador).
Layout desenhado a mao sobre as janelas NITIDAS de gaze/me (gaze_pose 2.0 + gaze_windows): 9,82-10,40 · 13,20-13,54 · 29,26-29,51 ·
31,73-32,28 · 33,49-34,34 · 41,42-42,03 · 46,07-46,62 · 48,87-49,66 · 49,84-50,33 · 52,33-52,91 · 60,53-60,72 · 72,31-72,74 · 85,81-86,51 ·
87,98-88,23 — todas cobertas. Expostas (sutis/piscada): capa 1,97-3,19 (dentro do split) · 10,88-11,04 · 12,00-12,17 · 21,81-22,00 ·
34,72-34,90 · 61,70-61,92 · split da virada 66,38-66,66 e 67,32-67,53 · 74,29-74,44 · 83,09-83,73 · 89,62-90,47 (cabeca no "porque voce e demais").
Capa em split 0-5,52 (so o gancho); pre-revelacao 5,52-10,45 (estaleiro, nada do Rickover); revelacao em 12,13 ("Hyman" em 12,03 + 3 quadros);
split 2 (a virada) 65,23-71,41; climax 79,94 (o presidente); apresentador no callout de digitacao (10,45-12,13), no bipe (61,37-65,23) e no fim do CTA (88,95-fim)."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- INTRO EM SPLIT (PRE-REVELACAO: nada do Rickover antes de "Hyman", 12,03 s) ---
 ("s01","split", 0.00,  5.52,"Esse cara é um dos militares mais insuportáveis e mais respeitados dos Estados Unidos.","CAPA gerada a pedido (velho de costas, cadeira de pés serrados sob a lâmpada)","olhada sutil 1,97–3,19 (dentro da capa)"),
 ("s02","full",  5.52, 10.45,"E ele criou um protocolo polêmico pra provar que seu time entrega mais ou menos…","fotos: operário no casco (Electric Boat) → Nautilus em construção (1953)","9,82–10,40"),
 # --- REVELACAO ---
 ("s03","full", 12.13, 19.67,"Hyman serrava a cadeira pro candidato escorregar na entrevista. E só saiu da Marinha porque foi demitido. Aos oitenta e dois anos.","REVELAÇÃO: retrato 1965 + nome → MOTION a cadeira serrada (corta, cai, inclina) → Rickover a bordo do USS Ohio (1981) + carimbo DEMITIDO + AOS 82 ANOS","13,20–13,54 · 16,66–16,81 · 17,35–17,51"),
 # --- PASSO 1 ---
 ("s04","full", 23.70, 34.33,"Primeiro, toda tarefa tem um nome. Não é o comercial, não é o pessoal. É o João. Ele diz que se deu errado e ninguém sabe de quem era…","MOTION chip PASSO 1 + título → tarefa com responsável (riscados O COMERCIAL e O PESSOAL, JOÃO) → foto: retrato oficial de 1955","27,93–28,17 · 29,26–29,51 · 31,73–32,28 · 33,49–34,34"),
 # --- PASSO 2 ---
 ("s05","full", 36.77, 50.45,"Segundo, cuida do detalhe… noventa e nove por cento do tempo… besteira. O erro que você deixa passar hoje vira o padrão amanhã,","MOTION chip PASSO 2 + título → foto: Rickover com o modelo do reator → MOTION 99% DO TEMPO + carimbo BESTEIRA → foto: Rickover no estaleiro","41,42–42,03 · 46,07–46,62 · 48,87–50,33"),
 # --- PASSO 3 ---
 ("s06","full", 52.21, 61.37,"E terceiro, para de torcer. Ele diz que todo chefe torce pra dar certo… Aquele vendedor que não vende nada há seis meses?","MOTION chip PASSO 3 + título → foto: o Nautilus navegando (1955) → MOTION vendas zeradas, 6 MESES","52,33–52,91 · 53,48–53,72 · 60,53–60,72"),
 # --- SEGUNDO SPLIT (A VIRADA) ---
 ("s07","split",65.23, 71.41,"E a virada foi uma entrevista. Um oficial jovem contou, todo orgulhoso, que foi um dos melhores da turma.","capa (a cadeira vazia da entrevista) → formatura de um guarda-marinha em 1946 (Carter, sem nome)","—"),
 ("s08","full", 71.41, 73.65,"Hyman perguntou: você deu o seu melhor?","foto: Rickover encarando (lançamento do USS Virginia, 1974)","72,31–72,74"),
 # --- CLIMAX ---
 ("s09","full", 78.73, 82.88,"E virou a cadeira. Esse oficial virou o presidente dos Estados Unidos.","capa (o velho de costas) → CLÍMAX: retrato oficial do presidente + nome JIMMY CARTER → Carter e Rickover no USS Los Angeles (1977)","80,80–80,96"),
 # --- FECHO / CTA ---
 ("s10","full", 84.85, 88.95,"E você? Por que não? Se você ainda aceita trabalho mais ou menos,","foto: Rickover encarando (Nautilus) com o callout → operário no casco (volta da abertura)","85,81–86,51 · 87,98–88,23"),
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
