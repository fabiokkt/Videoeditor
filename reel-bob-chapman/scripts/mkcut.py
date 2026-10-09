"""POR VIDEO — reel BOB CHAPMAN. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# palavras que o whisper pos dentro do silencio real (caem no pedaco errado da divisao — docs/05 §31)
WFIX={(13,98.94):(99.27,99.36),(0,6.57):(6.80,6.86)}   # "O conselho" e "E ele": comecam depois dos vales 99,00-99,27 e 6,40-6,80
for (rg,t0),(a,b) in WFIX.items():
    for x in W[rg]:
        if abs(x[1]-t0)<0.005: x[1],x[2]=a,b
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 0:([6.60,11.415],set()),         # GANCHO "Esse cara e um dos donos mais bobos e mais bem-sucedidos dos Estados Unidos." | "E ele criou um protocolo polemico pra provar que o seu funcionario nao e custo." | "E o filho de alguem."
 2:([25.99,30.06],{2}),           # "Bob herdou ... de dolares." | "E esse e o protocolo pra voce parar de tratar gente como despesa." | DROP "Primeiro, escuta de verdade. Ele pagava..." (refeito em r03+r04)
 4:([44.50],set()),               # "Escuta de verdade. Ele pagava um curso de tres dias so pra ensinar o time a escutar." | "Ele dizia: chefe fala, lider escuta."
 10:([68.00],set()),              # "Todo funcionario e o filho querido de alguem." | "Voce trata o seu time como trataria o filho do seu melhor amigo, pequeno gafanhoto?"
 12:([76.35],{1}),                # "lembra que ele volta pra casa." | DROP "Ele dizia que o jeito... com ele." (refeito em r13)
 13:([86.83,90.30,93.25,95.30,99.13],set()),  # "Ele dizia..." | "Voce deu a P**** de um esporro na frente de todo mundo?" | "De noite, quem escuta e o filho dele." | "E a virada foi uma crise." | "Em 2009, os pedidos cairam quarenta por cento." | "O conselho perguntou: nao vai demitir ninguem?"
 17:([116.45],{1}),               # "Todo mundo, do chao de fabrica a diretoria, tirou quatro semanas de folga sem salario." | DROP "E teve o funcion..." (refeito em r18)
 19:([125.475],set()),            # "Ninguem foi demitido." | "No ano seguinte,"
 21:([131.69],set()),             # "E na ultima crise, voce demitiu ou dividiu, meu amigo?" | "Se voce trata gente como despesa,"
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel BOB CHAPMAN:
#  r01 "Bob herdou ... tres bilhoes e meio..." (parou) -> r02
#  r02 parte 3 "Primeiro, escuta de verdade. Ele pagava um curso..." -> refeito em r03 "Primeiro" + r04
#  r06 "Segundo, faz o teste do pai." + r07 "Ele viu um pai entregando a filha no alto mar" (tropecou) -> r08 + r09
#  r12 parte 2 "Ele dizia que o jeito que voce trata alguem no trabalho vai pra casa com ele." -> refeito em r13
#  r14 "Ele pensou, o que eu..." (parou) -> r15
#  r16 "Todo mundo!" (falso inicio) -> r17
#  r17 parte 2 "E teve o funcion..." (parou) -> r18
#  O CTA de palavra-chave ("Comenta PALAVRA...") nao existe neste roteiro (sem palavra-chave falada); nao ha nada a procurar.
DROP={1,6,7,14,16}
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
