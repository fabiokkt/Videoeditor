"""POR VIDEO — reel DEMING. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 0:([6.735],set()),               # GANCHO "...idolatrados no Japao." | "E ele criou um protocolo polemico ... nao resolve nada."
 3:([27.545,29.46],set()),        # "Deming foi dar aulas ... depois da guerra," | "ganhou medalha do imperador" | "e ate hoje ... nome dele."
 4:([41.545],set()),              # "E esse e o protocolo ... mesmo problema." | "Primeiro" (+ r05 "troca o culpado")
 10:([65.535],set()),             # "E quem montou esse jeito foi voce, meu querido." | "Segundo, acaba com o ranking."
 11:([72.415,77.195],{2}),        # "Ele diz que ranking..." | "Se o melhor vendedor ... topo da lista," | DROP "foi o ranking que..." (refeito em r12)
 17:([101.345,104.225],set()),    # "Seu time ri do cartaz no almoco pequeno gafanhoto." | "E a virada foi uma caixa de bolinhas." | "Ele montava uma fabrica de mentira."
 23:([126.495],set()),            # "Uma em cada cinco bolinhas era vermelha." | "Seu funcionario so erra, meu amigo."
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel DEMING:
#  r01 "Demi foi dar aulas para as fabricas," (falso inicio) e r02 "Deming foi dar aula ... medalha do empre..." -> refeito em r03
#  r09 "E quem montou esse jeito foi voce, meu querido." -> refeito em r10
#  r11 parte 3 "foi o ranking que..." -> refeito em r12 "Foi o ranking quem ensinou."
#  r16 "Seu time ri do cartaz no almoco biquen..." -> refeito em r17
DROP={1,2,9,16}
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
