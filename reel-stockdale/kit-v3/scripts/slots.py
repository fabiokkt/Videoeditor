"""POR VIDEO — reel JAMES STOCKDALE. Mapa dos slots em tempo ABSOLUTO de timeline (rate 1.1, timeline 91,091 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava assets/broll-slots.json.
Kit v3: MG={"*"} — toda cobertura e da camada de motion (compositions/mg.html, gerada por work/mg/gen.py); os splits
continuam no plan.broll com file "" (o split arrasta o apresentador).
Layout desenhado a mao sobre as janelas NITIDAS de gaze/me (gaze_pose 2.0): 37,9-38,5 · 63,7-64,7 · 77,0-77,5 · 81,6-82,0 ·
86,3-86,8 — todas cobertas. A do gancho (2,9-3,4, olhar levemente para baixo) e sutil e fica no split da capa.
Capa em split 0-10,74; revelacao em 10,74 ("Jim" em 10,67 s + 2 quadros); split 2 (a virada) 64,82-70,78; climax 70,78
(calendario Natal -> Pascoa); apresentador no bipe (35,0-37,85) e no fim do CTA (86,97-fim)."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- INTRO EM SPLIT (PRE-REVELACAO: nada que identifique o Stockdale antes de "Jim", 10,67 s) ---
 ("s01","split", 0.00, 10.74,"Esse cara é um dos militares mais torturados… o dono otimista é o primeiro a quebrar.","CAPA: Hanoi Hilton visto do alto (NARA) → cela/cama de Hoa Lo → muro de Hoa Lo (só fotos)","olhada sutil 2,9–3,4 (no split)"),
 # --- CORPO ---
 ("s02","full", 10.74, 16.71,"Jim foi derrubado no Vietnã. Ainda no paraquedas pensou: são cinco anos preso, no mínimo.","REVELAÇÃO: retrato do Stockdale + nome → A-4 Skyhawk → portão da Maison Centrale","—"),
 ("s03","full", 16.71, 18.98,"Errou, foram sete e meio.","MOTION: contador 5 → 7,5 ANOS","—"),
 ("s04","full", 23.31, 30.80,"Primeiro, separa o que é seu. Ele aprendeu com o filósofo grego…","MOTION chip PASSO 1 → foto: Epicteto (gravura)","—"),
 ("s05","full", 30.80, 35.00,"Juros e governo não dependem de você. Preço e cobrança dependem.","MOTION: duas colunas NÃO DEPENDE / DEPENDE","—"),
 ("s06","full", 37.85, 41.89,"…meu querido! Segundo, encara o fato mais feio,","MOTION chip PASSO 2","olhada 37,9–38,5"),
 ("s07","full", 41.89, 46.60,"ele diz que tudo começa por encarar a realidade mais brutal, seja ela qual for.","foto: prisioneiro na cela (NARA) → cama de Hoa Lo","—"),
 ("s08","full", 46.60, 49.45,"Faz quanto tempo que você não abre o extrato com calma?","MOTION: extrato bancário","—"),
 ("s09","full", 52.94, 59.76,"E terceiro, nunca perde a fé no final. Ele diz que nunca duvidou que ia sair de lá…","MOTION chip PASSO 3 → foto: Stockdale na volta (1973) → POWs comemorando no C-141","—"),
 ("s10","full", 62.02, 64.82,"o que ele não pode é ver você desistindo.","foto: esposas esperando a volta dos prisioneiros (1973)","olhada 63,7–64,7"),
 # --- SEGUNDO SPLIT (A VIRADA) ---
 ("s11","split",64.82, 70.78,"E a virada foi o Natal. Perguntaram quem não aguentou, ele respondeu: os otimistas.","foto: árvore de Natal (anos 60) → retrato do Stockdale","—"),
 # --- CLIMAX ---
 ("s12","full", 70.78, 79.39,"Os que diziam: no Natal a gente sai. O Natal chegava e passava… a Páscoa passava.","MOTION CLÍMAX: calendário Natal → Páscoa → passa","olhada 77,0–77,5"),
 ("s13","full", 79.39, 82.15,"E eles morriam de coração partido.","foto: cama da cela de Hoa Lo","olhada 81,6–82,0"),
 ("s14","full", 84.75, 86.97,"Mês que vem é o seu Natal.","foto: árvore de Natal (volta da capa, sentido trocado)","olhada 86,3–86,8"),
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
