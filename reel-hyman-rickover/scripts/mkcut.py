"""POR VIDEO — reel HYMAN RICKOVER. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 0:([6.30,13.60],{2}),            # GANCHO "...dos Estados Unidos." | "E ele criou um protocolo polemico..." | DROP falso inicio "Iman serrava a cadeira do candidato Iman." (refeito em r01)
 1:([21.08],set()),               # "Iman serrava a cadeira pro candidato escorregar na entrevista" | "e so saiu da Marinha porque foi demitido aos 82 anos."
 4:([37.01],set()),               # "O comercial, nao e o pessoal, e o Joao." | "Ele diz que se deu errado..."
 11:([68.85,73.60],set()),        # "Para de torcer." | "Ele diz que todo chefe torce..." | "Aquele vendedor que nao vende nada ha seis meses?"
 13:([90.23,94.85],set()),        # "E a virada foi uma entrevista," | "um oficial jovem contou..." | "Iman perguntou, voce deu o seu melhor?"
 14:([100.15,103.18,104.62,108.00],{4}),  # "O cara engoliu seco, nem sempre." | "Ele olhou um tempao..." | "E virou a cadeira." | "Esse oficial virou o presidente..." | DROP "Seu time deu o melhor essa semana, meu amiguinho." (refeito em r15)
 16:([116.20],{1}),               # "E voce? Por que nao?" | DROP falso inicio "Se voce..." (refeito em r17)
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel HYMAN RICKOVER:
#  r00 parte 3 "Iman serrava a cadeira do candidato Iman." (falso inicio) -> r01
#  r14 parte 5 "Seu time deu o melhor essa semana, meu amiguinho." -> r15 "Seu time deu o melhor essa semana, meu amigo?" (ultimo)
#  r16 parte 2 "Se voce..." (falso inicio) -> r17
#  Nao gravado: o CTA do meio "Comenta ALMIRANTE..." (80,8-88,2 s e silencio puro, -50 dB) — vale o audio.
DROP=set()
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
