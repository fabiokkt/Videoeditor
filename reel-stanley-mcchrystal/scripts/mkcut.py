"""POR VIDEO — reel STANLEY McCHRYSTAL. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 0:([6.05],set()),                # GANCHO "...dos Estados Unidos." | "E ele criou um protocolo polemico ... nao se odeiam."
 5:([33.11],set()),               # "E esse e o protocolo ... a operacao." | "Primeiro," (emenda com r06 num take so)
 6:([36.10,40.30],{2}),           # "todo mundo na mesma reuniao" | "ele fazia uma reuniao por dia com ate 7 mil pessoas" | DROP "ele disse que time excelente trabalhando separado" (refeito em r08+r09)
 19:([89.74],{1}),                # "Ele diz que a meta e todo mundo saber tudo, o tempo todo." | DROP falso inicio "Se o vendedor ve a agenda ... antiprometer"
 31:([141.20],{1}),               # "ia tudo ensacado pro quartinho, e ninguem lia." | DROP falso inicio "Ele juntou o soldado e a analista, e a oper..." (refeito em r34)
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel STANLEY McCHRYSTAL:
#  r02 "Stanley como..." (falso inicio) -> r03
#  r06 parte 2 + r07 "Ele disse que time excelente trabalhando separado." (sem "perde") -> r08+r09 "Ele diz que time excelente trabalhando separado... perde"
#  r13 "Ele diz que quem trabalha do lado de la para de ser..." (parou) -> r14
#  r15 "Seu melhor vendedor passa uma semana na..." (parou) -> r16
#  r19 parte 1, r20 (completo, mas nao e o ultimo), r21 "Se o vendedor ve a porra...", r22 (sem "a porra do" e sem "meu querido"), r23 "Se o vendedor ve a..." -> r24
#  r26 "Os soldados arriscavam a vida de ma..." (parou) -> r27
#  r28 "La, tudo em..." + r29 "La." + r30 "E a tudo..." (falsos inicios) -> r31 parte 0
#  r31 parte 1 "Ele juntou o soldado e a analista, e a oper..." + r32 "...de 18 por mes," + r33 "pra trezentas" (sem "mais de") -> r34
#  r35 "A venda de ontem ja chegou na sua operacao..." (parou) -> r36
#  Nao gravado: o CTA do meio e o final "Comenta BRIGA que eu te mando o protocolo completo no direct." — vale o audio.
DROP={2,7,13,15,20,21,22,23,26,28,29,30,32,33,35}
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
