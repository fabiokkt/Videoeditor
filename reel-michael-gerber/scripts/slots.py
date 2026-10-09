"""POR VIDEO — reel MICHAEL GERBER. Mapa dos slots em tempo ABSOLUTO de timeline (rate 1.1).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava assets/broll-slots.json.
Kit v3: MG={"*"} — toda cobertura e da camada de motion (compositions/mg.html, gerada por work/mg/gen.py); os splits
continuam no plan.broll com file "" (o split arrasta o apresentador).
Os tempos das janelas vem de work/mg/tempos.json (gravado por work/mg/gen.py a partir das FRASES em work/tl-words.txt):
mudar o tempo de uma cena num lugar so (docs/05 §33). Rodar work/mg/gen.py antes."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
X=json.load(open('work/mg/tempos.json'))
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- INTRO EM SPLIT (PRE-REVELACAO: nada do Michael antes de "Michael") ---
 ("s01","split", 0.00, X['P_in'],"Esse cara é um dos donos mais atrapalhados e mais copiados do planeta Terra.","CAPA gerada a pedido (padaria às 4 h, a mulher de costas no forno) → a mesma cena mais perto","—"),
 ("s02","full", X['P_in'], X['P_out'],"E ele criou um protocolo polêmico pra provar que você não tem uma empresa.","foto: relógio de ponto (British Library) → a dona do armazém (NARA, 1973)","—"),
 # --- REVELACAO ---
 ("s03","full", X['michael'], X['B_out'],"Michael ensinava dono a não quebrar. Até o sócio avisar: a gente tá quebrando.","REVELAÇÃO: o Michael em 2009 (Flickr, CC BY-SA) + nome → MOTION o sócio: “A gente tá quebrando.” (1985)","—"),
 # --- PASSO 1 ---
 ("s04","full", X['D_in'], X['D_out'],"Primeiro, desenha o organograma. Cada cadeira: vendas, financeiro, compras, entrega. Ele manda escrever o seu nome em cada cadeira que é sua. Seu nome tá em seis cadeiras?","MOTION chip PASSO 1 + título → o organograma (VOCÊ em cada cadeira, SEU NOME EM 6 CADEIRAS)","—"),
 # --- PASSO 2 ---
 ("s05","full", X['F_in'], X['F_out'],"Segundo, monta a empresa como se fosse vender franquia. Tudo que você faz de cabeça, escreve passo a passo. Ele disse que ela tem que funcionar com gente comum, não com gênio.","MOTION chip PASSO 2 + título → a mesma loja 9 vezes → o passo a passo → GENTE COMUM × GÊNIO","—"),
 # --- PASSO 3 ---
 ("s06","full", X['H_in'], X['H_out'],"E terceiro, assina o contrato de cada cadeira. Escreve numa folha o que aquela cadeira entrega, e você assina como se fosse funcionário. Ele diz: primeiro a cadeira, depois a pessoa. Na sua, primeiro veio o sobrinho.","MOTION chip PASSO 3 + título → o contrato da cadeira assinado → 1º A CADEIRA / 2º A PESSOA → 1º O SOBRINHO / 2º A CADEIRA","—"),
 # --- SEGUNDO SPLIT (A VIRADA) ---
 ("s07","split",X['L_in'], X['L_out'],"E a virada foi uma loja de torta.","foto: a padaria de San Angelo, 1939 (FSA/LOC)","—"),
 ("s08","full", X['N_in'], X['N_out'],"Sarah aprendeu a fazer torta com a tia e abriu a própria loja. Três anos depois, com a loja cheirando a torta, ela falou: odeio fazer torta. Não aguento nem o cheiro.","fotos: a moça com a torta (Harris & Ewing) → a mesa cheia de formas → 3 ANOS DEPOIS: o forno → a capa (callback)","—"),
 # --- CLIMAX ---
 ("s09","full", X['C_in'], X['C_out'],"Ela não abriu uma empresa. Abriu um emprego.","CLÍMAX: MOTION EMPRESA → EMPREGO","—"),
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
