"""POR VIDEO — reel JAMES STOCKDALE. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 1:([7.83],{1}),                  # "E ele criou um protocolo polemico" | DROP "pra provar que na crise do dono" (refeito em r02)
 5:([26.07],set()),               # "Errou, foram sete e meio." | "E esse e o protocolo pra voce parar de prometer..."
 14:([60.77],set()),              # "Segundo, encara o fato mais feio," | "ele diz que tudo comeca por encarar a realidade mais brutal..."
 18:([75.90],{1}),                # "e medo." | DROP "e terceiro nunca perda" (refeito em r19+r20)
 20:([83.76],{1}),                # "nunca perde a fe no final." | DROP "Ele diz que nunca duvidou..." (refeito em r21)
 25:([107.89],{1}),               # "perguntaram quem nao aguentou, ele respondeu: os otimistas." | DROP "o que" (falso inicio, refeito em r26)
 29:([126.86],set()),             # "e eles morriam de coracao partido." | "Voce prometeu pro seu time que mes que vem melhora, meu amigo?"
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel JAMES STOCKDALE:
#  r01 parte 2 "pra provar que na crise do dono" (tropeco) -> refeito em r02
#  r07 "Ele aprendeu com um filosofo grego" + r08 "que voce..." -> refeito em r09
#  r13 "Segundo, encara o fato..." -> refeito em r14
#  r15 "Faz quanto tempo que voce nao abre..." -> refeito em r16
#  r18 parte 2 "e terceiro nunca perda" -> refeito em r19 "E terceiro," + r20 "nunca perde a fe no final"
#  r20 parte 2 "Ele diz que nunca duvidou... mais forte" -> refeito em r21
#  r23 "E na virada..." -> refeito em r24 "E a virada foi o Natal."
#  r25 parte 2 "o que" (falso inicio) -> r26 "Os que diziam..."
#  r27 "O Natal a gente chegava e passava." -> refeito em r28 "O Natal chegava e passava."
DROP={7,8,13,15,23,27}
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
