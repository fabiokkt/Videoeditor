"""POR VIDEO — reel MIKE ABRASHOFF. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 0:([6.33],set()),                # GANCHO "...da Marinha americana" | "e ele criou um protocolo polemico" (capa so com a 1a frase)
 32:([103.71],{1}),               # "E a virada foi uma despedida," | DROP "no dia que ele assumiu o cap..." (refeito em r33)
 33:([111.17,113.08],set()),      # "...com a familia." | "E a tripulacao comemorou." | "Mike pensou: daqui a dois anos, vai ser eu?"
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel MIKE ABRASHOFF:
#  r04 "com o mesmo atributo" (tropeco) -> r05 "com a mesma tripulacao."
#  r07 "E esse e o protocolo ... ninguem mais quer PARAR DE trabalhar" (tropeco no fim; whisper em recorte confirma) -> fica r06
#      "E o protocolo pra voce parar de dizer que ninguem mais quer trabalhar." (take limpo anterior; o audio nao diz "esse e")
#  r13 "Segundo," + r14 "Pergunta o que voce mudaria." + r15 "Pergu..." (falso inicio) -> r16 "Segundo, pergunta:" + r17
#  r18 "Perguntou pros trezentos e dez pessoas." -> r19 "...marinheiros, um por um."
#  r30 "E leilao." -> r31 "E leilao." (ultimo)
#  r32 parte 2 "no dia que ele assumiu o cap..." -> r33
#  r36 "Ele..." (falso inicio) · r38 "Se voce acha que ninguem..." (falso inicio) -> r39+r40 (um take: "porque voce... e demais")
DROP={4,7,13,14,15,18,30,36,38}
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
