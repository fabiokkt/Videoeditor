"""POR VIDEO — reel GENE KRANZ. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# POR VIDEO: palavra que o passe por regiao poe DENTRO do silencio real cai no pedaco errado da divisao.
# (regiao, inicio do whisper) -> (inicio, fim) reais. r34: "nossa!" vem ate 141,11 no whisper; o vale real e 140,59-140,74
# (recortes: ate 140,66 "A culpa e nossa."; de 140,66 "Tres anos depois, a").
WFIX={(34,140.15):(140.15,140.58)}
for (rg,t0),(a,b) in WFIX.items():
    for x in W[rg]:
        if abs(x[1]-t0)<0.005: x[1],x[2]=a,b
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 22:([97.34],set()),              # "E a virada foi numa segunda-feira." | "Em 1967, tres astronautas morreram num incendio na nave, num teste no chao." (vale 97,17-97,51)
 34:([140.665],set()),            # "A culpa e nossa!" | "Tres anos depois, a Apollo 13 explodiu a caminho da Lua." (vale 140,59-140,74)
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel GENE KRANZ:
#  r04 "e comandava a sala no dia de o homem..." (tropecou) -> r05
#  r19 "Quem chuta desesperado e voce, pequeno agaf..." (tropecou) + r20 (take inteiro) -> r21 (ultimo; o whisper ouve "juta", mas o /ch/
#      e surdo: 91,30-91,36 com 2-4% da energia < 500 Hz, igual ao r20 — e "chuta")
#  r24 "Ele juntou o time e disse..." + r25 "Nenhum de nos levantou e gritou, porra..." -> r26 (a frase inteira refeita)
#  r27-r33: o fim refeito a partir de "A culpa e nossa." (r27 "A culpa e nossa." · r28 "Tres anos depois..." · r29 "Mesma sala, mesmo chefe." ·
#      r30 "Os tres voltaram vivos." · r31 "Seu time ta vendo alguma coisa..." (parou) · r32 "A culpa e nossa." · r33 "Tres anos depois, o ap..." (parou))
#      -> r34-r39 (ultima passada inteira)
DROP={4,19,20,24,25,27,28,29,30,31,32,33}
out=[];ww={}
for k in sorted(R):
    r=R[k]; pts,dr=SPLIT.get(k,([],set()))
    b=[r['s']]+pts+[r['e']]
    for p in range(len(b)-1):
        s,e=round(b[p],3),round(b[p+1],3)
        n=len(out)
        out.append({"i":n,"s":s,"e":e,"parent":k,"drop":(k in DROP) or (p in dr)})
        lo=0.35 if p==0 else 0.0; hi=0.35 if p==len(b)-2 else 0.0
        ws=[x for x in W.get(k,[]) if s-lo<=(x[1]+x[2])/2<e+hi]
        if ws: ww[str(n)]=ws
json.dump(out,open('work/regions_cut.json','w'),indent=1)
json.dump(ww,open('work/region-words-cut.json','w'),ensure_ascii=False,indent=1)
for r in out:
    t=''.join(x[0] for x in ww.get(str(r['i']),[])).strip()
    print(f"c{r['i']:02d} (r{r['parent']:02d}) {r['s']:7.2f}-{r['e']:7.2f} {'DROP ' if r['drop'] else '     '}{t}")
