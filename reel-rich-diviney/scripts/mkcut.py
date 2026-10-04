"""POR VIDEO — reel RICH DIVINEY. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 0:([5.76,12.35],{2}),            # "Esse cara ... Estados Unidos." (GANCHO) | "E ele criou um protocolo polemico ... fazer o trabalho." | DROP "Rick." (falso inicio, refeito em r02)
 2:([21.25,26.02],{2}),           # "Rich escolhia quem entrava na elite da elite dos SEALs," | "so os melhores SEALs se candidatavam e metade reprovava." | DROP "E esse e o protocolo ... de apaixonar" (refeito em r03, com o "se")
 3:([35.05],{1}),                 # "E esse e o protocolo para voce parar de se apaixonar por curriculo." | DROP "primeiro" (falso inicio, refeito em r05)
 5:([42.92],set()),               # "Primeiro, separa o que da para ensinar ... e pergunta." | "Da para ensinar? Planilha, da."
 14:([67.32],set()),              # "Na entrevista, me conta o dia ... ultimo emprego." | "O que voce fez?"
 17:([77.35],{1}),                # "troca de cadeira." | DROP "ele tinha uma marinheira" (refeito em r18)
 18:([83.89,87.10],set()),        # "Ele tinha uma marinheira ... do setor." | "Ele so mudou ela de funcao e ela decolou." | "As vezes a pessoa nao e ruim, pequeno gafanhoto."
 23:([106.70],set()),             # "Pulou, afundou e atravessou a piscina andando no fundo." | "Subiu sem ar. Desculpa, eu nao sei nadar."
 25:([114.32],{1}),               # "Nadar, a gente ensina." | DROP "Coragem." (falso inicio: ~1 s de pausa e recomeca em r26 — apontado pelo Fabio na v2)
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel RICH DIVINEY:
#  r00 fim "Rick." + r01 "Rich escolhia quem entrava na elite da..." (falsos inicios) -> r02
#  r02 fim "E esse e o protocolo para voce parar de apaixonar..." -> r03 · r03 fim "primeiro" + r04 "Se voce..." -> r05
#  r07 "E so isso que voce..." -> r08 · r13 "Na entrevista, me conta." -> r14 · r17 fim "ele tinha uma marinheira" -> r18
#  r21 "Ele conta que um moleque apareceu no treinamento dos SEALs" -> r22 · r28 "Se voce se ia..." -> r29
#  r25 fim "Coragem." (falso inicio, ~1 s de pausa) -> r26 "Coragem de aparecer ali..." (apontado pelo Fabio na v2)
#  r27 "Nadar a gente ensina." depois de "meu amigo?" = callback do roteiro (fica)
DROP={1,4,7,13,21,28}
out=[];ww={}
for k in sorted(R):
    r=R[k]; pts,dr=SPLIT.get(k,([],set()))
    b=[r['s']]+pts+[r['e']]
    for p in range(len(b)-1):
        s,e=round(b[p],3),round(b[p+1],3)
        n=len(out)
        out.append({"i":n,"s":s,"e":e,"parent":k,"drop":(k in DROP) or (p in dr)})
        # bordas EXTERNAS da regiao: tolerancia de 0,35 s (o whisper poe palavras fracas como "E", "tudo,"
        # alem da borda do silencedetect); divisoes internas: estritas no ponto de corte
        lo=0.35 if p==0 else 0.0; hi=0.35 if p==len(b)-2 else 0.0
        ws=[x for x in W.get(k,[]) if s-lo<=(x[1]+x[2])/2<e+hi]
        if ws: ww[str(n)]=ws
json.dump(out,open('work/regions_cut.json','w'),indent=1)
json.dump(ww,open('work/region-words-cut.json','w'),ensure_ascii=False,indent=1)
for r in out:
    t=''.join(x[0] for x in ww.get(str(r['i']),[])).strip()
    print(f"c{r['i']:02d} (r{r['parent']:02d}) {r['s']:7.2f}-{r['e']:7.2f} {'DROP ' if r['drop'] else '     '}{t}")
