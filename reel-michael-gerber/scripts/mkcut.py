"""POR VIDEO — reel MICHAEL GERBER. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 11:([44.52],set()),               # "Cada cadeira. Vendas, financeiro, compras, entrega." | "Ele manda escrever o seu nome em cada cadeira que e sua."
 12:([50.42,52.53],set()),         # "Seu nome ta em seis cadeiras," | "voce nao e o dono, meu querido," | "voce e a P**** do organograma."
 14:([58.86],set()),               # "Monta a empresa como se fosse vender franquia." | "Tudo que voce faz de cabeca, escreve passo a passo."
 17:([72.73],set()),               # "se so funciona com voce, pequeno gafanhoto, ela nao funciona." | "E terceiro, assina o contrato de cada cadeira."
 22:([89.63],set()),               # "Na sua, primeiro veio o sobrinho," | "depois inventaram a cadeira."
 25:([104.16],set()),              # "E a virada foi uma loja de torta." | "Sarah aprendeu a fazer torta com a tia e abriu a propria loja."
 27:([116.90,118.73,120.41],set()),# "Tres anos depois, ... ela falou: odeio fazer torta," | "nao aguento nem o cheiro," | "ela nao abriu uma empresa," | "abriu um emprego."
 30:([130.62],set()),              # "Loja de torta." | "Se voce e o funcionario mais explorado da sua empresa, me segue, porque voce..." (+ r31 "e demais!")
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel MICHAEL GERBER:
#  r01 "E ele criou um protocolo polemico para provar para voce..." (parou) -> r02
#  r06 "E ele estava ocupado demais trabalhando para olhar..." (parou) -> r07
#  r08 "E esse e o protocolo para voce parar de ser o funcionario." (parou antes de "mais explorado") -> r09
#  r16 "Se..." (falso inicio) -> r17 · r21 "Na sua..." -> r22 · r23 "Comenta Cadeira." (parou) -> r24
#  r26 "Tres anos depois, a loja..." -> r27 · r28 "Voce abriu..." -> r29
DROP={1,6,8,16,21,23,26,28}
# Palavra que o whisper poe dentro do silencio real cai no pedaco errado da divisao (docs/05 §31): tempo corrigido antes de atribuir.
# r14 "Tudo" (whisper 58,61-58,92) e "o" ficam no vale 58,62-59,10; a fala de "Tudo" comeca em ~59,10.
WFIX={(14,8):(59.10,59.24),(14,9):(59.24,59.30)}
for (k,i),(a,b) in WFIX.items(): W[k][i]=[W[k][i][0],a,b]+list(W[k][i][3:])
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
