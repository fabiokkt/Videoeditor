"""POR VIDEO — reel KAZUO INAMORI. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 1:([8.25],set()),                # "E ele criou um protocolo polemico" | "pra provar que seu funcionario nao pensa como dono porque voce esconde o numero."
 2:([15.495,21.095],set()),       # "Kazuo fundou duas gigantes," | "virou monge budista e com 78 anos assumiu uma companhia aerea falida," | "sem salario."
 16:([60.955],set()),             # "Na sua, so voce ve o numero." | "E olhe la, pequeno gafanhoto."
 17:([64.115],set()),             # "E terceiro," | "proibe a palavra orcamento."
 26:([92.715,95.73],set()),       # "E a virada foi uma reuniao." | "Um diretor ia gastar um bilhao de ienes." | "Ele cortou:"
 34:([116.10],{1}),               # "No primeiro ano, a empresa falida bateu recorde de lucro." | DROP "Seu time gasta..." (falso inicio, refeito em r36)
 37:([126.645],set()),            # "Numero escondido." | "Se voce e o unico que liga pro dinheiro da sua empresa, me segue,"
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel KAZUO INAMORI:
#  r09 "Pela empresa inteira." (falso inicio) -> refeito em r10 "Pela empresa inteira, ninguem briga."
#  r22+r23+r24 "E se voce quiser o protocolo completo / Comenta Monge. / Que eu te mando." -> refeito em r25
#     "Comenta MONGE, que eu te mando o protocolo completo." (a frase do roteiro)
#  r34 parte 2 "Seu time gasta..." (falso inicio) e r35 "Se o time gasta como se o dinheiro..." (falso inicio) -> refeito em r36
DROP={9,22,23,24,35}
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
