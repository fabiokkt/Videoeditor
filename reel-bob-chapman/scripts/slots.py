"""POR VIDEO — reel BOB CHAPMAN. Mapa dos slots em tempo ABSOLUTO de timeline (rate 1.1, timeline 90,107 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava assets/broll-slots.json.
Kit v3: MG={"*"} — toda cobertura e da camada de motion (compositions/mg.html, gerada por work/mg/gen.py); os splits
continuam no plan.broll com file "" (o split arrasta o apresentador).
Olhar (gaze_pose 2.0: 17 janelas / 4,2 s; gaze_windows: 23 / 8,7 s; conferido nas folhas gaze/me/g00-g02): o apresentador olha para a camera
o tempo todo — so piscadas, sobrancelha e expressao (o giro de cabeca em "demitiu ou dividiu" e gesto). Leitura exposta: 0 s.
Capa em split 0-5,74 (o gancho inteiro); pre-revelacao 5,74-9,85 (dois operarios de 1942, sem o Bob); apresentador no callout de digitacao
"E O FILHO DE ALGUEM." (9,85-11,08, o primeiro pico da nota de gravacao); revelacao em 11,08 ("Bob" em 11,01 + 2 quadros); split 2 (a virada)
57,29-62,36; climax 78,88 (ninguem foi demitido, os crachas todos no lugar); apresentador nos callouts (respondendo, o bipe, o conselheiro
impaciente, demitiu ou dividiu) e no CTA."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- INTRO EM SPLIT (PRE-REVELACAO: nada do Bob antes de "Bob", 11,01 s) ---
 ("s01","split", 0.00,  5.74,"Esse cara é um dos donos mais bobos e mais bem-sucedidos dos Estados Unidos.","CAPA gerada a pedido (galpão à noite, crachás todos no lugar, homem de terno de costas) → detalhe dos crachás","—"),
 ("s02","full",  5.74,  9.85,"E ele criou um protocolo polêmico pra provar que o seu funcionário não é custo.","fotos: operário na furadeira (1942) → Beulah Faith, 20, no torno (1942)","6,81–7,36 · 7,90–8,14"),
 # --- REVELACAO ---
 ("s03","full", 11.08, 16.48,"Bob herdou uma fábrica mal das pernas e fez dela uma empresa de três bilhões e meio de dólares.","REVELAÇÃO: a capa (ele de costas) + nome → MOTION contador US$ 3,5 BILHÕES","12,69–13,26"),
 # --- PASSO 1 ---
 ("s04","full", 19.97, 28.89,"Primeiro, escuta de verdade. Ele pagava um curso de três dias só pra ensinar o time a escutar. E dizia: chefe fala, líder escuta.","MOTION chip PASSO 1 + título → foto: jovens ouvindo os palestrantes (Detroit, 1942) → a frase dele","22,41–22,90 · 26,72–26,90"),
 # --- PASSO 2 ---
 ("s05","full", 32.69, 40.15,"Segundo, faz o teste do pai. Ele viu um pai entregando a filha no altar e entendeu: todo funcionário é o filho querido de alguém.","MOTION chip PASSO 2 + título → foto: a noiva entra com o pai (1938) → foto: o rapaz do torno (1942)","37,88–38,09"),
 # --- PASSO 3 ---
 ("s06","full", 44.03, 51.69,"E terceiro, lembra que ele volta pra casa. Ele dizia que o jeito que você trata alguém no trabalho vai pra casa com ele.","MOTION chip PASSO 3 + título → foto: indo pra casa depois da usina (1940) → foto: o jantar em casa (1938)","48,09–49,43 · 50,76–50,95"),
 ("s07","full", 54.64, 57.29,"De noite, quem escuta é o filho dele.","foto: os filhos no jantar (1939), luz da noite","55,72–55,90"),
 # --- SEGUNDO SPLIT (A VIRADA) ---
 ("s08","split",57.29, 62.36,"E a virada foi uma crise. Em 2009, os pedidos caíram quarenta por cento.","MOTION o gráfico de pedidos: 2008 × 2009, −40%","—"),
 ("s09","full", 65.18, 78.88,"Ele pensou: o que uma família faria? Todo mundo, do chão de fábrica à diretoria, tirou quatro semanas de folga sem salário. E teve funcionário que tirou uma semana a mais no lugar do colega que não ia aguentar.","foto: uma família (1937) → foto: a operária do torno (DO CHÃO DE FÁBRICA) → foto: executivos (À DIRETORIA, 4 SEMANAS SEM SALÁRIO) → MOTION as semanas: a semana do colega passa pra ele","68,73–71,21 · 74,35–74,60"),
 # --- CLIMAX ---
 ("s10","full", 78.88, 82.34,"Ninguém foi demitido. No ano seguinte, recorde de lucro.","CLÍMAX: a parede de crachás da capa, todos no lugar + 0 DEMITIDOS + 2010 · RECORDE DE LUCRO","79,18–79,42"),
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
