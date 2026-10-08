"""POR VIDEO — reel GORDON BETHUNE. Mapa dos slots em tempo ABSOLUTO de timeline (rate 1.1, timeline 96,324 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava assets/broll-slots.json.
Kit v3: MG={"*"} — toda cobertura e da camada de motion (compositions/mg.html, gerada por work/mg/gen.py); os splits
continuam no plan.broll com file "" (o split arrasta o apresentador).
Olhar (gaze_pose 2.0: 16 janelas / 3,6 s; gaze_windows: 20 / 7,3 s; conferido nas folhas gaze/me/g00-g02): o apresentador olha para a camera
o tempo todo — so piscadas e palpebra baixando em fim de frase (o maior, 59,96-60,32 no "pequeno gafanhoto", e expressao). Leitura exposta: 0 s.
Capa em split 0-5,55 (o gancho inteiro); pre-revelacao 5,55-10,20 (a cabine sem marca e a capa em tela cheia); apresentador no callout de
digitacao (10,20-11,56); revelacao em 11,56 ("Gordon" em 11,49 + 2 quadros); split 2 (a virada) 61,47-63,99; climax 79,91 (a pior virou a melhor);
apresentador em "pra fazer besteira" (callout), no bipe (34,45-37,47, callout), em "Vao passar o ano brigando" (seco), em "Quem escreveu foi voce"
(apontando, callout) e no fecho/CTA (82,46-fim), com a pergunta escrita na tela de 91,60 ao fim."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- INTRO EM SPLIT (PRE-REVELACAO: nada da Continental nem do Gordon antes de "Gordon", 11,49 s) ---
 ("s01","split", 0.00,  5.55,"Esse cara é um dos chefes mais boca-suja e mais amados dos Estados Unidos.","CAPA gerada a pedido (o manual pegando fogo no estacionamento, homem de terno de costas) → detalhe do manual queimando","—"),
 ("s02","full",  5.55, 10.20,"E ele criou um protocolo polêmico pra provar que o seu time não faz o que você pede.","foto: os pilotos de costas na cabine (sem marca) → a capa em tela cheia","7,82–8,19"),
 # --- REVELACAO ---
 ("s03","full", 11.56, 18.71,"Gordon pegou a pior companhia aérea do país, que já tinha falido duas vezes. E tacou fogo no manual da empresa.","REVELAÇÃO: o 777 batizado “Gordon M. Bethune” + nome → Miami, 1994 (A PIOR DO PAÍS) → FALÊNCIA 1983 / 1990 → o manual pegando fogo (capa)","17,40–17,59"),
 # --- PASSO 1 ---
 ("s04","full", 23.24, 34.45,"Primeiro, premia o que importa pro cliente. Ele diz que o que você mede e premia é o que você recebe. Paga comissão só por venda fechada? Seu vendedor vende até pra quem não paga.","MOTION chip PASSO 1 + título → a frase dele sobre a frota de 1994 → MOTION comissão por venda × o cliente que não paga","30,97–31,76"),
 # --- PASSO 2 ---
 ("s05","full", 37.47, 47.23,"Segundo, todo mundo ganha junto. Ele diz que o time inteiro ganha ou perde pelo mesmo número. Seu comercial ganha por venda e seu financeiro ganha por corte de custo?","MOTION chip PASSO 2 + título → foto: o hangar da Continental em Houston → MOTION COMERCIAL × FINANCEIRO","38,30–39,22 · 44,88–46,67"),
 # --- PASSO 3 ---
 ("s06","full", 49.17, 59.17,"E terceiro, queima o manual. Ele mandou o time fazer o que é certo pro cliente e pra empresa, não o que tá no manual. Seu atendente fala “é política da empresa”?","MOTION chip PASSO 3 + título → foto: a tripulação da Continental → MOTION o manual riscado → “É POLÍTICA DA EMPRESA.”","49,89–50,15 · 52,34–52,52 · 56,76–57,40"),
 # --- SEGUNDO SPLIT (A VIRADA) ---
 ("s07","split",61.47, 63.99,"E a virada foi o ar-condicionado.","foto: o A300 da Continental no calor de Miami, 1994","—"),
 ("s08","full", 63.99, 79.91,"O piloto ganhava bônus pra economizar combustível. Ele desligava o ar e voava devagar. O passageiro chegava suado e atrasado. Gordon trocou esse bônus por setenta e cinco dólares pra todo mundo, todo mês que a empresa ficasse entre as mais pontuais.","foto: os pilotos → MOTION o painel (AR DESLIGADO, DEVAGAR) → foto: os passageiros (SUADO, ATRASADO) → MOTION o bônus antigo × o novo (PRA TODO MUNDO) → MOTION o ranking de pontualidade","68,36–68,60 · 70,46–71,04"),
 # --- CLIMAX ---
 ("s09","full", 79.91, 82.46,"Um ano depois, a pior virou a melhor.","CLÍMAX: um DC-10 da Continental em 1996 + 1996 · COMPANHIA AÉREA DO ANO","—"),
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
