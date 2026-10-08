"""POR VIDEO — reel GORDON BETHUNE. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 7:([34.97],{1}),                 # "Primeiro, premia o que importa pro cliente," | DROP "ele diz que o que voce mede" (parou; refeito em r08)
 18:([72.78],set()),              # "Seu comercial ganha por venda e seu financeiro ganha por corte de custo," | "vao passar o ano brigando."
 21:([82.22],set()),              # "Ele mandou o time fazer o que e certo pro cliente e pra empresa," | "nao o que ta no manual."
 24:([93.45,97.38],set()),        # "E a virada foi o ar-condicionado." | "O piloto ganhava bonus pra economizar combustivel." | "Ele desligava o ar e voava devagar."
 25:([102.69],{1}),               # "O passageiro chegava suado e atrasado." | DROP "Gordon trocou" (parou; refeito em r28)
 34:([132.18],set()),             # "paga pro seu time fazer besteira," | "me segue, porque voce e demais."
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel GORDON BETHUNE:
#  r06 "Primeiro, premia que..." (falso inicio) + r07 parte 2 "ele diz que o que voce mede" (parou) -> r07 parte 1 + r08
#  r09 "Paga comissao so por venda..." (parou) -> r10
#  r12 "E porra do ca..." (tropecou) -> r13 "E a porra do calote fica com voce, meu querido."
#  r17 "Seu comercial ganha por venda, seu financeiro ganha por..." (parou) -> r18
#  r25 parte 2 "Gordon trocou" + r26 "Gordon trocou esse bonus" + r27 "por setenta e cinco dolares pra..." (pararam) -> r28
#  O CTA de palavra-chave ("Comenta PALAVRA...") nao existe neste roteiro (v2.2: pergunta aberta no fim, r35).
DROP={6,9,12,17,26,27}
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
