"""POR VIDEO — reel ALAN MULALLY. Mapa dos slots de B-roll em tempo ABSOLUTO de timeline (rate 1.1, timeline 103,309 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava
assets/broll-slots.json. Com --placeholders, gera cartoes rotulados em assets/broll/_ph/ e
escreve o plan.broll apontando para eles (so para ver a estrutura no preview).
Com --real, escreve o plan.broll apontando para assets/broll/<arquivo final>.
Layout desenhado a mao sobre as leituras NITIDAS conferidas nas folhas gaze/me/g*.jpg (36,2-37,1 · 66,3-66,8 · 68,1-68,5 ·
77,0-77,2 · 86,4-86,7): capa em split 0-3,40; pre-revelacao ate "Alan" (13,16 s) -> revelacao em 13,23; apresentador no bipe
(31,62-36,20; bipe 35,30-35,82); split 2 (a virada) 69,78-75,95; climax 88,12 ("O Alan bate palma") com riser + impact."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- INTRO EM SPLIT (PRE-REVELACAO: nada de Alan Mulally, Ford, Boeing ou GM antes de "Alan", 13,16 s) ---
 ("s01","split", 0.00,  3.40,"Esse cara é um dos CEOs mais sorridentes e mais implacáveis","CAPA (imagem gerada a pedido, Codex): diretoria à noite, telão todo verde, executivos olhando para a mesa","— (quadro 0 = capa)"),
 ("s02","full",  3.40,  6.90,"…dos Estados Unidos. E ele criou um protocolo polêmico","PRÉ-REVELAÇÃO: arranha-céus americanos / bandeira dos EUA (sem marca)","—"),
 ("s03","split", 6.90, 10.40,"pra provar que “não me traz problema, me traz solução”","PRÉ-REVELAÇÃO: chefe cobrando o time numa reunião","—"),
 ("s04","split",10.40, 13.23,"faz seu time esconder tudo de você.","PRÉ-REVELAÇÃO: funcionário escondendo papel / cochicho (callout de digitação)","—"),
 # --- CORPO ---
 ("s05","full", 13.23, 15.67,"Alan nunca tinha trabalhado com carro,","REVELAÇÃO: Alan Mulally sorrindo diante do logo da Ford","—"),
 ("s06","full", 15.67, 17.98,"penhorou até o logotipo da Ford.","o oval azul da Ford na sede","—"),
 ("s07","full", 17.98, 20.75,"E na crise de 2008 a GM quebrou.","sede da GM (Renaissance Center, Detroit)","—"),
 ("s08","full", 24.87, 27.79,"Primeiro, aceita problema sem solução.","reunião de equipe (problema sobre a mesa)","—"),
 ("s09","full", 27.79, 31.62,"Na Ford, ninguém contava problema pro chefe sem ter a solução.","sede mundial da Ford, Dearborn","—"),
 ("s10","full", 36.20, 40.61,"…meu querido. Segundo, faz o semáforo toda semana.","semáforo","olhadas 36,23–36,67 · 36,87–37,02 s"),
 ("s11","full", 45.13, 48.70,"Verde tá no plano. Amarelo, tem problema, mas tem saída.","relatório de status verde/amarelo/vermelho","—"),
 ("s12","full", 48.70, 52.11,"Vermelho, ninguém sabe resolver ainda.","semáforo no vermelho","—"),
 ("s13","full", 56.03, 59.34,"E terceiro, proíbe a piada com a cara dos outros.","colegas rindo de alguém no escritório","—"),
 ("s14","full", 63.22, 66.99,"Seu gerente trouxe um problema e você zoou ele na frente do time?","gerente constrangido na frente do time","olhada 66,27–66,77 s"),
 ("s15","full", 66.99, 69.78,"O próximo, ele não traz, pequeno gafanhoto.","“pequeno gafanhoto”: série Kung Fu (Mestre Po)","olhada 68,10–68,50 s"),
 # --- SEGUNDO SPLIT (A VIRADA) ---
 ("s16","split",69.78, 72.56,"E a virada foi uma palma. Tudo verde,","reunião semanal de Mulally com a diretoria","—"),
 ("s17","split",72.56, 75.95,"e a empresa ia perder dezessete bilhões.","prejuízo recorde da Ford (gráfico de perdas)","—"),
 ("s18","full", 75.95, 78.40,"Aí o Mark, um diretor,","Mark Fields","olhada 77,00–77,22 s"),
 ("s19","full", 78.40, 81.44,"parou a produção de um novo carro. Um cara do time dele falou:","Ford Edge 2007","—"),
 # --- CLIMAX ---
 ("s20","full", 84.66, 88.12,"Na reunião sobre o primeiro vermelho, silêncio.","diretoria em silêncio","olhada 86,38–86,70 s"),
 ("s21","full", 88.12, 91.17,"O Alan bate palma e pergunta: quem pode ajudar o Mark?","CLÍMAX: Alan Mulally aplaudindo — riser + impact","—"),
 ("s22","full", 91.17, 94.65,"Semanas depois, os gráficos pareciam um arco-íris.","painel de gráficos coloridos","—"),
]
NOMES={"s01":"s01-split-capa-diretoria-verde","s02":"s02-implacaveis-eua","s03":"s03-split-me-traz-solucao","s04":"s04-split-esconder-tudo",
 "s05":"s05-alan-revelacao","s06":"s06-logo-penhorado","s07":"s07-gm-quebrou","s08":"s08-aceita-problema","s09":"s09-ninguem-contava",
 "s10":"s10-semaforo","s11":"s11-verde-amarelo","s12":"s12-vermelho","s13":"s13-proibe-piada","s14":"s14-zoou-gerente",
 "s15":"s15-pequeno-gafanhoto","s16":"s16-split-virada-palma","s17":"s17-split-17-bilhoes","s18":"s18-mark-fields","s19":"s19-ford-edge",
 "s20":"s20-silencio","s21":"s21-climax-palma","s22":"s22-arco-iris"}
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
# slots que viraram motion graphics (compositions/mg.html): ficam no broll-slots.json (tempos de referencia), fora do plan.broll
MG={"s05","s06","s07","s08","s09","s10","s11","s12","s13","s14","s15","s18","s19","s20","s21","s22"}
def plan_broll(path_of):
    return [{k:s[k] for k in ('mode','fromSeg','toSeg','span')}|{"file":path_of(s)} for s in slots if s['id'] not in MG]
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
