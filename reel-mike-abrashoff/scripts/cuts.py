"""Detecta head e tail de cada take mantido -> work/segs.json.
Head: onset por RMS (20 ms, -27 dB, 4 de 8 janelas), recuando ate o piso de ruido, - HEAD_PAD.
Tail: ultima janela acima do piso de ruido (-45 dB) + TAIL_PAD — garante a palavra inteira."""
import numpy as np, wave, json
w=wave.open('work/full.wav'); n=w.getnframes(); sr=w.getframerate()
a=np.frombuffer(w.readframes(n),dtype=np.int16).astype(np.float32)/32768.0
W=int(0.020*sr); nw=len(a)//W
db=20*np.log10(np.sqrt(np.maximum((a[:nw*W].reshape(nw,W)**2).mean(1),1e-12)))
t2w=lambda t:max(0,min(nw-1,int(t/0.020))); w2t=lambda i:round(i*0.020,3)
NOISE=-45.0
# folgas: o crossfade do J-cut (3f) cai inteiro no silêncio e sobra ~0,1 s de respiro entre as falas
# (com 0,12/0,10 e crossfade 5f o fade comia até 76 ms da palavra final — reel André Esteves)
HEAD_PAD=0.20; TAIL_PAD=0.13
# J-cut sem soma de vozes (reel Atul Gawande, 2026-09-27: "as J-cuts nao ficaram tao boas"): a voz de cada
# take termina em `aout` = fim da fala + TA e a do take seguinte comeca em `in` = inicio da fala - HH, emendadas
# ponta a ponta (crossfade de 3 quadros dentro do silencio). O VIDEO do take segura mais LEAD_SRC depois do
# `aout` (out = aout + lead*rate): a voz nova entra 5 quadros ANTES do corte de imagem. Respiro = (TA+HH)/rate.
import json as _j
_P=_j.load(open('assets/edit-plan.json')); RATE=_P.get('rate',1.1); LEAD_SRC=round(_P.get('jcutLeadFrames',5)/30*RATE,3)
TA=0.12; HH=0.15
R={r['i']:r for r in json.load(open('work/regions_cut.json'))}
# Fim da ULTIMA PALAVRA de cada regiao (whisper -ml 1 -sow). Serve de ancora para o tail:
# o piso de -45 dB sozinho entra no decaimento da respiracao e deixa ~1 s de ar morto
# (medido no IKEA: CAMADAS +0,57 s, PROVA +0,86 s).
WEND={int(k):v[-1][2] for k,v in json.load(open('work/region-words-cut.json')).items()}
# POR VIDEO: (label, 1a regiao, ultima regiao) em work/regions_cut.json — reel MIKE ABRASHOFF
# (regions_cut.json vem de scripts/mkcut.py). TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido):
#   c05 "com o mesmo atributo" -> c06 · c08 "...quer parar de trabalhar" (tropeco) -> fica c07 · c14+c15+c16 -> c17+c18
#   c19 "310 pessoas" -> c20 · c31 "E leilao." -> c32 · c34 "no dia que ele assumiu o cap..." -> c35 · c40 "Ele..." · c42 falso inicio
# c43+c44 = "Se voce acha... me segue, porque voce... e demais" (um take so, pausa dramatica)
TAKES=[
 ("GANCHO",0,0),
 ("PROTOCOLO-POLEMICO",1,1),
 ("PROVAR-SALARIO",2,2),
 ("MIKE-PIOR-NAVIO",3,3),
 ("SETE-MESES",4,4),
 ("MESMA-TRIPULACAO",6,6),
 ("PROTOCOLO-TRABALHAR",7,7),
 ("P1-OLHA",9,9),
 ("P1-ACHAVA",10,10),
 ("P1-PESQUISA",11,11),
 ("P1-RESPEITO",12,12),
 ("P1-CELULAR-BIPE",13,13),
 ("P2-SEGUNDO",17,17),
 ("P2-MUDARIA",18,18),
 ("P2-310",20,20),
 ("P2-PINTOU",21,21),
 ("P2-CHATO",22,22),
 ("P2-PARAFUSO",23,23),
 ("P2-TROCARAM",24,24),
 ("P2-COPIOU",25,25),
 ("P3-TERCEIRO",26,26),
 ("P3-FICAR",27,27),
 ("P3-CONTRATO",28,28),
 ("P3-O-QUE-FACO",29,29),
 ("P3-DEMISSAO",30,30),
 ("P3-LEILAO",32,32),
 ("VIRADA-DESPEDIDA",33,33),
 ("VIRADA-ASSUMIU",35,35),
 ("VIRADA-COMEMOROU",36,36),
 ("VIRADA-PENSOU",37,37),
 ("CLIMAX-CONTINENCIA",38,38),
 ("CLIMAX-OLHO-SECO",39,39),
 ("CTA-ROJAO",41,41),
 ("CTA-ME-SEGUE",43,44),
]
AP=[(lab,R[a]['s'],R[b]['e']) for lab,a,b in TAKES]
res=[];tot=0
print(f"{'i':>2} {'label':<15} {'IN':>7} {'OUT':>7} {'dur':>5}   onset/offset")
for k,(lab,s0,s1) in enumerate(AP):
    # vizinhos no SOURCE (um take descartado pode ficar entre dois mantidos)
    pe=max([r['e'] for r in R.values() if r['e']<=s0+1e-6], default=-1e9)
    ns=min([r['s'] for r in R.values() if r['s']>=s1-1e-6], default=1e9)
    lo,hi=t2w(max(s0-0.8,pe+0.12)),t2w(min(s0+1.2,ns-0.2)); on=None
    for j in range(lo,max(lo+1,hi)):
        if (db[j:j+8]>=-27.0).sum()>=4: on=j; break
    if on is None: on=t2w(s0)
    j=on
    while j>lo and db[j-1]>=NOISE: j-=1
    onset=w2t(j); IN=round(max(0,onset-HEAD_PAD),3)
    # POR VIDEO: head fixo onde a deteccao nao serve (reel MIKE ABRASHOFF: nenhum)
    # (nenhum ate agora)
    FORCE_IN={}
    if lab in FORCE_IN: onset=round(FORCE_IN[lab]+HEAD_PAD,3); IN=FORCE_IN[lab]
    hi2=t2w(min(s1+0.8,ns-0.15)); lo2=t2w(max(s1-0.8,pe))
    # Tail: ultima janela acima do piso. Mas um respiro/estalo DESTACADO (separado do corpo da
    # fala por >= GAP_MIN de silencio) nao e palavra — e o take ficaria com ~1 s de ar morto
    # (medido no IKEA: CAMADAS +1,2 s e PROVA +0,9 s). Nesses casos recua para o bloco anterior.
    # Nunca corta DENTRO de um bloco contiguo, entao a palavra inteira fica sempre preservada.
    off=None
    for j in range(hi2,lo2,-1):
        if db[j]>=NOISE: off=j+1; break
    if off is None: off=t2w(s1)
    # O whisper as vezes estoura alem do audio (GANCHO: 7,59 contra 7,28 real) e o RMS as vezes
    # entra no respiro (PROVA: 67,00 contra 66,14). Pega o MENOR dos dois...
    we=WEND.get(TAKES[k][2])
    if we is not None:
        cand=min(off,t2w(we)+1)
        # ...e TRAVA: nunca cortar dentro de fala energetica. Se o corpo acima de -35 dB
        # continua depois do candidato, o tail vai ate o fim desse bloco (palavra inteira).
        body=cand
        while body<hi2 and db[body]>=-35.0: body+=1
        cand=max(cand,body)
        if cand<off: print(f"     [{lab}] tail {w2t(off):.2f} -> {w2t(cand):.2f} (fim da palavra {we:.2f}s; -{(off-cand)*0.02:.2f}s de ar morto)")
        off=cand
    # POR VIDEO: fim de fala fixo onde a respiracao seguinte fica acima do piso (reel REED HASTINGS:
    # "fim." termina em 105,42; o piso de -45 dB entrava no respiro ate o "Em" do take seguinte)
    FORCE_OFF={}
    if lab in FORCE_OFF: off=t2w(FORCE_OFF[lab])
    offset=w2t(off); OUT=round(offset+TAIL_PAD,3); d=round(OUT-IN,3); tot+=d
    print(f"{k:>2} {lab:<15} {IN:7.2f} {OUT:7.2f} {d:5.2f}   {onset:.2f}/{offset:.2f}")
    res.append({"i":k,"label":lab,"in":IN,"out":OUT,"region":[TAKES[k][1],TAKES[k][2]],"_on":onset,"_off":offset})
print(f"\nsource {tot:.2f}s -> /1.1 = {tot/1.1:.2f}s ; menos {len(AP)-1} leads(5f) = {tot/1.1-(len(AP)-1)*5/30:.2f}s")
for r in res: r['on'],r['off']=r.pop('_on'),r.pop('_off')
for k,r in enumerate(res):
    r['in']=round(max(0,r['on']-(HEAD_PAD if k==0 else HH)),3); r['aout']=round(r['off']+TA,3)
# Pausa curta (fala a fala < TA+HH no source): a emenda vai no silencio real, 45% para o tail e 55% para a cabeca.
print(f"\nrate {RATE} · lead {LEAD_SRC}s de source · respiro alvo {(TA+HH)/RATE:.3f}s de timeline")
for k in range(len(res)-1):
    a,b=res[k],res[k+1]; g=round(b['on']-a['off'],3)
    if b['in']<a['aout']:
        a['aout']=round(a['off']+g*0.45,3); b['in']=round(b['on']-g*0.55,3)
        # reel HERB KELLEHER: com 45/55 o crossfade (3 f) invadia o inicio da palavra seguinte ("piloto|foi grosso",
        # pausa 0,14 s). Se o crossfade cabe na pausa, a emenda vai logo antes da fala nova e o fade termina no silencio.
        XF=_P.get('jcutCrossfadeFrames',3)/30*RATE
        if g*0.55<XF+0.005 and g>=XF+0.01: b['in']=round(b['on']-XF-0.005,3); a['aout']=b['in']
        print(f"  pausa curta {a['label']} | {b['label']}: fala a fala {g:.2f}s -> emenda em {a['aout']} (respiro {g/RATE:.3f}s)")
for k,r in enumerate(res):
    last=k==len(res)-1
    r['out']=round(r['aout'] if last else r['aout']+LEAD_SRC,3)
    if last: r['out']=r['aout']=round(r['off']+TAIL_PAD,3)
tot=sum(r['out']-r['in'] for r in res)
print(f"source {tot:.2f}s -> /{RATE} menos {len(res)-1} leads = {tot/RATE-(len(res)-1)*5/30:.2f}s")
json.dump(res,open('work/segs.json','w'),indent=1)
