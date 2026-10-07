"""POR VIDEO — reel MATTHEW RIDGWAY. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 0:([5.94],set()),                # GANCHO "...dos Estados Unidos." | "E ele criou um protocolo polemico... Ta abandonado."
 6:([40.29,42.03],set()),         # "O soldado nem reclamava mais." | "Ele diz que teve que arrancar:" | "faltava luva, comida quente e envelope pra escrever pra casa."
 17:([92.48,96.20],set()),        # "Ele reconhecia uns cinco mil soldados de cara," | "e parava na estrada so pra dizer: bom trabalho." | "Ele dizia que isso levantava um batalhao inteiro."
 20:([111.15],set()),             # "E voce nao sabe nem o nome do filho do seu melhor vendedor, pequeno gafanhoto." | "E a virada foi uma pergunta."
 22:([118.64],{1}),               # "Ele perguntou: o plano de ataque?" | DROP falso inicio "O cara gaguejou sem..." (refeito em r23)
 26:([133.89],set()),             # "Em menos de tres meses, o exercito que fugia retomou a capital." | "Sua empresa tem plano pra cortar custo, meu amigo?"
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel MATTHEW RIDGWAY:
#  r01 "Matthew andava com uma granada no peito e pregou na parede." (parou no meio) + r02 "O primeiro e..." (ruido de falso inicio) -> r03 (frase inteira)
#  r07 "resolveu antes de falar" (falso inicio) -> r08
#  r09 "Seu vendedor ta sem computador que presta e voce manda" (parou) -> r10
#  r14 "chefe que so aparece na festa" (parou) -> r15
#  r18 "Voce nao sabe nem o nome do filho do seu vendedor, pequeno gafanhoto?" (sem "melhor") + r19 "E voce nao sabe nem o..." (falso inicio) -> r20
#  r22 parte 1 "O cara gaguejou sem..." (falso inicio) -> r23
#  r25 "Em menos de tres meses, o exercito que..." (parou) -> r26
#  Nao gravado: o CTA "E comenta GENERAL que eu te mando o PDF." (o bruto termina em "porque voce e demais", 144,35 s) — vale o audio.
DROP={1,2,7,9,14,18,19,25}
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
