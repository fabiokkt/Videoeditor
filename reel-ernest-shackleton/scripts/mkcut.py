"""POR VIDEO — reel ERNEST SHACKLETON. Subdivide as regioes de fala nos vales de silencio reais
(scripts/valleys.py) e remove os takes repetidos -> work/regions_cut.json + work/region-words-cut.json.
Cada entrada: i (novo id), s, e (source), parent (regiao original), drop (True = descartada).
Regioes descartadas continuam na lista: o cuts.py usa os vizinhos para achar o silencio real."""
import json
R={r['i']:r for r in json.load(open('work/regions.json'))}
W={int(k):v for k,v in json.load(open('work/region-words.json')).items()}
# POR VIDEO: palavra que o passe por regiao poe DENTRO do silencio real (whisper ~0,3 s adiantado) cai no pedaco errado da divisao.
# (regiao, inicio do whisper) -> (inicio, fim) reais (vales: 57,90-58,22 e 61,10-61,48; o align.py reancora depois).
WFIX={(14,57.80):(58.22,58.40),(14,61.18):(61.48,61.53)}
for (rg,t0),(a,b) in WFIX.items():
    for x in W[rg]:
        if abs(x[1]-t0)<0.005: x[1],x[2]=a,b
# (regiao, [pontos de divisao no MEIO do vale], {indices das partes descartadas})
SPLIT={
 1:([14.00],set()),               # "E ele criou um protocolo polemico... voce traz pra perto." | "Ernest ficou quase dois anos preso no gelo na Antartida." (revelacao)
 14:([58.06,61.29],set()),        # "Segundo, voce larga primeiro" | "Ele mandou cada homem largar quase tudo no gelo" | "E o primeiro a jogar fora foi ele: as moedas de ouro."
 16:([74.45],set()),              # "E terceiro, ninguem fica parado." | "Ele sabia que homem parado no gelo comeca a reclamar."
}
# TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido) — reel ERNEST SHACKLETON:
#  r03 "E nao perdeu um..." (parou) -> r04
#  r05 "E esse e o protocolo pra voce parar de deixar um reclamao contamin..." (parou) -> r06
#  r10 "Ele sai..." (falso inicio) -> r11
#  r13 "Segundo" (falso inicio) -> r14
#  r17 "Entao tinha tarefa todo dia, ate o..." (parou) -> r18
#  r23 "Ernest leu conta..." (falso inicio) -> r24
#  r28 "Quem mais reclama na sua empresa" (parou) + r29 "Quem mais reclama nas..." (tropecou) -> r30
#  Nao gravado: o CTA do meio "Comenta GELO que eu te mando o protocolo completo no direct." (entre r19 e r20 so ha 1,5 s de silencio) — vale o audio.
DROP={3,5,10,13,17,23,28,29}
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
