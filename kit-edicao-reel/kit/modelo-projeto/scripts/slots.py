"""POR VIDEO — reel KAZUO INAMORI. Mapa dos slots de B-roll em tempo ABSOLUTO de timeline (rate 1.1, timeline 98,275 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava
assets/broll-slots.json. Com --placeholders, gera cartoes rotulados em assets/broll/_ph/ e
escreve o plan.broll apontando para eles (so para ver a estrutura no preview).
Com --real, escreve o plan.broll apontando para assets/broll/<arquivo final>.
Layout desenhado a mao sobre as janelas de gaze/pose-windows.json (scripts/gaze_pose.py, olhar compensado pela pose da cabeca):
capa em split 0-1,65; cutaway 1,65-5,05 (olhada 1,72-2,24 do gancho); split 5,05-11,25 (pre-revelacao); revelacao em 11,25
("Kazuo" em 11,18 s); split 2 (a virada) 67,30-71,89 com a transicao de arrastar; climax 82,28 s ("E o lucro que o funcionario
tirou rastejando no chao"); apresentador no bipe (61,40-67,30) e no fim do CTA (96,15-fim)."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- SLOT 1: INTRO EM SPLIT (PRE-REVELACAO: nada de Inamori, Kyocera, KDDI ou JAL antes de "Kazuo", 11,18 s) ---
 ("s01","split", 0.00,  1.65,"Esse cara é um dos monges…","CAPA (ideia do Fabio): pista de aeroporto à noite, monge de costas diante de um avião sem logotipo, luz vermelha no alto","— (quadro 0 = capa)"),
 ("s02","full",  1.65,  5.05,"…mais temidos e mais lucrativos do planeta Terra.","PRÉ-REVELAÇÃO: monge zen japonês de costas / templo (sem rosto identificável)","olhada 1,72–2,24 s"),
 ("s03","split", 5.05,  8.00,"E ele criou um protocolo polêmico pra provar","PRÉ-REVELAÇÃO: sala de reunião com a mão batendo na mesa e planilhas voando (capa B, ideia do Fabio)","—"),
 ("s04","split", 8.00, 11.25,"que seu funcionário não pensa como dono porque você esconde o número.","PRÉ-REVELAÇÃO: dono escondendo a planilha / número fechado (callout de digitação)","—"),
 # --- SLOT 2: CUTAWAYS DO CORPO ---
 ("s05","full", 11.25, 13.60,"Kazuo fundou duas gigantes,","REVELAÇÃO: Kazuo Inamori + Kyocera","—"),
 ("s06","full", 13.60, 16.25,"virou um monge budista e, com setenta e oito anos,","Inamori de monge (1997)","—"),
 ("s07","full", 16.25, 19.60,"assumiu uma companhia aérea falida. Sem salário.","Inamori na Japan Airlines, 2010","olhadas 16,30–16,67 · 17,18–17,61 s"),
 ("s08","full", 22.40, 26.42,"…liga pro dinheiro da sua empresa. Primeiro, quebra a empresa em pedacinhos.","Gestão Ameba: equipes pequenas no chão de fábrica da Kyocera","olhadas 22,59–22,92 · 24,69–24,98 s"),
 ("s09","full", 31.00, 34.00,"Ele diz que quem vê o próprio resultado briga pelo lucro.","funcionários da Kyocera / equipe reunida","—"),
 ("s10","full", 34.00, 36.75,"Pela empresa inteira, ninguém briga.","a empresa inteira: sede/fábrica vista de fora","olhada 34,60–35,05 s"),
 ("s11","full", 40.30, 43.60,"Simples, igual conta de casa. Ele diz que tocar empresa","caderno de contas de casa (kakeibo)","olhada 41,58–41,86 s"),
 ("s12","full", 43.60, 47.30,"sem olhar número é pilotar avião sem olhar o painel.","cockpit: painel de instrumentos do avião","olhada 45,18–45,37 s"),
 ("s13","full", 47.30, 51.06,"Na sua, só você vê o número. E olhe lá, pequeno gafanhoto.","“pequeno gafanhoto”: série Kung Fu (Mestre Po)","olhada 48,65–49,11 s"),
 ("s14","full", 55.54, 58.82,"porque quem tem orçamento acha que o certo é gastar tudo.","orçamento aprovado / gastar tudo","—"),
 ("s15","full", 58.82, 61.40,"Sobrou verba em dezembro e o time torrou","verba torrada no fim do ano","—"),
 # --- SLOT 3: SEGUNDO SPLIT (A VIRADA) ---
 ("s16","split",67.30, 69.16,"E a virada foi uma reunião","reunião de diretoria da JAL com Inamori","—"),
 ("s17","split",69.16, 71.89,"com o diretor que ia gastar um bilhão de ienes.","maços de notas de 10.000 ienes","—"),
 ("s18","full", 74.94, 78.28,"O diretor: “Mas senhor, já está aprovado no orçamento.”","diretores da JAL","—"),
 # --- SLOT 4: CLIMAX EMOCIONAL ---
 ("s19","full", 82.28, 85.69,"“É o lucro que o funcionário tirou rastejando no chão.”","CLÍMAX: equipe de solo / manutenção da JAL — riser + impact","olhada 85,33–85,48 s"),
 ("s20","full", 85.69, 89.20,"No primeiro ano, a empresa falida bateu recorde de lucro.","JAL decolando / relistagem na bolsa em 2012","olhada 88,90–89,09 s"),
 ("s21","full", 93.45, 96.15,"Se você é o único que liga pro dinheiro da sua empresa,","dono sozinho olhando as contas","olhadas 94,71–95,04 · 95,65–96,11 s"),
]
NOMES={"s01":"s01-split-capa-monge-pista","s02":"s02-monge-temido","s03":"s03-split-protocolo-polemico","s04":"s04-split-esconde-numero",
 "s05":"s05-kazuo-revelacao","s06":"s06-virou-monge","s07":"s07-jal-sem-salario","s08":"s08-quebra-em-pedacinhos",
 "s09":"s09-briga-pelo-lucro","s10":"s10-empresa-inteira","s11":"s11-conta-de-casa","s12":"s12-painel-do-aviao",
 "s13":"s13-pequeno-gafanhoto","s14":"s14-orcamento-gastar-tudo","s15":"s15-verba-de-dezembro","s16":"s16-split-reuniao",
 "s17":"s17-split-bilhao-de-ienes","s18":"s18-aprovado-no-orcamento","s19":"s19-climax-rastejando","s20":"s20-recorde-de-lucro",
 "s21":"s21-unico-que-liga"}
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
