"""POR VIDEO — reel JOHN WOODEN. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 5:([28.98],set()),               # "John ganhou dez campeonatos em doze anos" | "e, no primeiro treino, ensinava ... a calcar a meia."
 10:([50.67],set()),              # "Primeiro, ninguem chega atrasado, nem o melhor." | "Ele diz que o atraso e desrespeito com todo o time."
 19:([83.15,84.83],set()),        # "Seu vendedor leva a comissao e o parabens no grupo." | "E quem fez a proposta?" | "Ninguem lembra, pequeno gafanhoto."
 20:([91.28],set()),              # "E terceiro, ninguem fala mal de colega." | "Ele expulsava do treino quem criticava colega."
 23:([106.13],{1}),               # "Voce nao ta protegendo o seu melhor vendedor, meu amiguinho." | DROP tropeco "esta vendendo a..." (refeito em r24)
 25:([113.25],set()),             # "E a virada foi uma barba." | "O melhor jogador do pais voltou de ferias barbudo."
 26:([118.70,120.74],set()),      # "Barba era proibida." | "Ele disse que era direito dele." | "John perguntou:"
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel JOHN WOODEN:
#  r01 "E ele criou um protocolo polemico para provar que regra nao vale" (falso inicio) · r02 idem ate "...melhor funcionario" · r03 "Boa droga." -> r04
#  r06 "E o protocolo para voce parar de deixar o seu melhor vendedor mandar" (sem o "esse e") · r07 "E esse e o protocolo para..." -> r08+r09
#  r11 "Se o melhor vendedor chega as 10h," (falso inicio) -> r12
#  r15 "Ele obrigava a quem..." -> r16
#  r17 "Seu vendedor leva a comissao e o parabens do grupo?" · r18 ruido ("Siocomi") -> r19
#  r21 "Seu treinador..." (falso inicio) -> r22
#  r23 parte 2 "esta vendendo a..." (tropeco) -> r24 "Ta perdendo a porra do resto do time."
#  Nao gravado: o CTA do meio "Comenta ESTRELA que eu te mando o protocolo completo no direct." — vale o audio (sem callout de ESTRELA).
DROP={1,2,3,6,7,11,15,17,18,21}
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
