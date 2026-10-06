# Exemplos — reels Deming (padrão atual) e Alan Mulally

Dois reels reais como molde de preenchimento. **Deming v2** é o padrão atual (dosagem foto × motion; camada gerada por `gen.py`). **Alan Mulally** tem o `mg.html` escrito à mão, com o markup de todas as peças da biblioteca. Ficaram de fora o `mg.html` gerado do Deming e o `gen-v1.py` (versão reprovada por excesso de motion).

_kit em 47e642e · v3.1: dosagem foto x motion (reel Deming), exemplo Deming, instalador e guia para outro computador, showreel-interface no kit · gerado em 2026-10-04_

## Índice

- `exemplos/deming/EDICAO.md`
- `exemplos/deming/LICENCAS-FOTOS.txt`
- `exemplos/deming/regioes.txt`
- `exemplos/deming/scripts/mkcut.py`
- `exemplos/deming/scripts/cuts.py`
- `exemplos/deming/scripts/bipe.py`
- `exemplos/deming/chunks.txt`
- `exemplos/deming/scripts/captions_fix_table.py`
- `exemplos/deming/tl-words.txt`
- `exemplos/deming/assets/edit-plan.json`
- `exemplos/deming/scripts/slots.py`
- `exemplos/deming/assets/broll-slots.json`
- `exemplos/deming/gen.py`
- `exemplos/alan-mulally/EDICAO.md`
- `exemplos/alan-mulally/mg.html`
- `exemplos/alan-mulally/scripts/mg_sfx.py`
- `exemplos/alan-mulally/scripts/slots.py`
- `exemplos/alan-mulally/PESQUISAS-BROLL-ALAN-MULALLY.md`


---

# ARQUIVO: `exemplos/deming/EDICAO.md`

# EDICAO.md — mapa do projeto (reel Deming)

Kit v3 (fluxo rápido, docs/14) + camada de motion (showreel-interface). Palco 1440x2560, timeline 30 fps, saída 1440x2560 @ 60 fps, 1,1x.
**Estado (2026-10-02): RENDERIZADO** (`renders/Deming-reel-final.mp4`), comando único sem parada.
Duração **101,31 s** · 30 takes · 1 bipe · 102 legendas · 4 callouts · 3 light-leaks (virada, clímax, CTA) · 11 cenas de motion · 2 splits.

> Regra de ouro: nunca editar `index.html` nem `compositions/mg.html` à mão. A camada sai de `work/mg/gen.py` (`python3 work/mg/gen.py`), depois `zsh scripts/montar.sh`.

## Bruto
`~/Claude/videos-brutos/deming-bruto.MP4` (cópia de ~/Downloads/89D5923E-….MP4) — MD5 `85706cdb154fce6e15e6209f03e42339`. HEVC 1440x2560 @60, 137,5 s, SDR full-range → mezanino full→limited.

## Takes descartados (mantido o ÚLTIMO)
r01 "Demi foi dar aulas…" e r02 "…medalha do empre…" → r03 · r09 "E quem montou…" → r10 · r11 fim "foi o ranking que…" → r12 · r16 "…no almoço biquen…" → r17. CTA r25–r27 = um take.

## Áudio ≠ roteiro (vale o áudio)
"dar aulas", "esconde O cliente", "Vermelho era O defeito". Grafia do roteiro: "pras", "pra", "cem", "noventa e quatro", "três", "Seu melhor", "que ensinou".
Não dá para ouvir o "de" em "de cada cem" (legenda: "Ele diz que cada cem problemas").

## Bipe
"porra" (51,13–51,645 s do source): /p/ 51,14 · decaimento até 51,64. Medido na voz-mix: 99,9% em 950–1050 Hz, 0% fora de 900–1100. Legenda `P****`. Apresentador em tela cheia.

## J-cut
29 emendas · 0 buracos · nenhum crossfade sobre fala · lead 4,9 quadros · respiro 0,245 s.

## Olhar
70 janelas nas folhas (gaze/me). Nítidas: 11,58 · 14,04 · 30,46–30,70 · 33,38–33,59 · 45,20 · 84,02–84,55 · 95,17–95,41 — todas sob motion. Leitura exposta: 0 s.

## Split
`splitShiftY` 520 (olhos medidos ~1213–1282 com 400 → ~1371). Splits: capa 0–11,37 · virada 71,34–75,99.

## Marca só depois do nome
"Deming" em 11,30 s → revelação em 11,37 (capa = professor de costas, sem rosto).

## Imagens
Capa: Codex gpt-5.6-sol (gerada a pedido — cena escolhida por mim, o pedido veio com o placeholder "[DESCRIÇÃO DA CENA]"): aula numa fábrica japonesa em 1950, professor de costas.
Retrato: Wikimedia `W. Edwards Deming.jpg` (domínio público, 393 px). Aula em Tóquio 1950, Deming com a Ordem do Tesouro Sagrado, medalha do Prêmio Deming: JUSE (juse.or.jp/deming_en/award, 200 px — usadas como cartões pequenos, ampliadas 4x).
Insígnia da Ordem do Tesouro Sagrado (2ª classe): Wikimedia CC BY 4.0. Mestre Po: reaproveitado do reel Alan Mulally.
deming.org bloqueou com verificação anti-robô (não contornada).

## Lições para o kit
- Fundo `.light` da camada precisa de "chão" escuro abaixo de ~64% da tela: legenda branca a 76% sobre cena clara reprova no contraste (check) e some.
- `.tag` com `white-space: nowrap` (tag longa quebrava em 2 linhas).
- Fonte primária com Cloudflare (deming.org) bloqueia o navegador do app: cair para site institucional (JUSE) + Commons.

## v2 (2026-10-02) — pedido: "diminuir os motion graphics, mais imagens; o início só com imagens"
- Abertura (split 0–11,37) só com fotos: capa (Codex) → operário na fábrica (LOC/FSA, domínio público) → desempregado encostado na vitrine "TO LEASE"
  (Dorothea Lange, NARA, domínio público). Saíram as etiquetas EUA/JAPÃO, os crachás e o DEMITIDO. O callout de digitação continua.
- Corpo: saíram o loop de crachás, os 3 crachás de vendedor + gráfico de vendas, os balões "kkkk", a fileira de voluntários e o gráfico "não diminui".
  Entraram fotos: linha de montagem A-20 (NARA, DP) · vendedor 1958 (Commons, CC BY 4.0) · mural "Employee of the Month" (Commons, CC BY-SA 4.0) ·
  operários rindo no almoço (NARA, DP). "E a vermelha não diminuía" (87,94–90,00) passou para o apresentador.
- Motion ficou nos capítulos (PASSO 1/2/3), nos 94 de 100, no ranking (só o trecho do cliente escondido), no cartaz, na caixa de bolinhas, na pá, no placar e no clímax.
- Licenças: work/pesq/q2/licencas.txt. Camada v1 guardada em work/mg/gen-v1.py.
- Render v2: `renders/Deming-reel-final-v2.mp4` (QC OK). Lição para o kit: `render-par.sh` RETOMA — pula toda `renders/chunks/chunk-NN.mp4` que já existe.
  Depois de mudar a camada, apagar as partes afetadas antes (na 1ª tentativa ele reaproveitou as 14 partes da v1 e o MP4 saiu igual à v1).


---

# ARQUIVO: `exemplos/deming/LICENCAS-FOTOS.txt`

```text
operario: File:Chrysler factory 40mm barrel production LOC fsa 8e11025.jpg · Public domain · https://upload.wikimedia.org/wikipedia/commons/8/87/Chrysler_factory_40mm_barrel_production_LOC_fsa_8e11025.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original
desempregado: File:Depression, Unemployed,destitute man leaning against vacant store-photo by Dorothea Lange - NARA - 195825.tif · Public domain · https://upload.wikimedia.org/wikipedia/commons/c/cc/Depression%2C_Unemployed%2Cdestitute_man_leaning_against_vacant_store-photo_by_Dorothea_Lange_-_NARA_-_195825.tif?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original
vendedor: File:Shoe salesman 1958 (JOKAUAS2 4434-4).tif · CC BY 4.0 · https://upload.wikimedia.org/wikipedia/commons/8/81/Shoe_salesman_1958_%28JOKAUAS2_4434-4%29.tif?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original
emp-mes: File:Employee of the Month Wall.jpg · CC BY-SA 4.0 · https://upload.wikimedia.org/wikipedia/commons/d/d8/Employee_of_the_Month_Wall.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original
almoco: File:Men and women employees on the "swing shift" of North American's Inglewood, Calif., aircraft plant enjoy their lunch... - NARA - 195482.jpg · Public domain · https://upload.wikimedia.org/wikipedia/commons/3/37/Men_and_women_employees_on_the_%22swing_shift%22_of_North_American%27s_Inglewood%2C_Calif.%2C_aircraft_plant_enjoy_their_lunch..._-_NARA_-_195482.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original
linha: File:Experienced assembly line workers of both sexes contribute to the production of A-20 attack bombers in the Douglas... - NARA - 196397.jpg · Public domain · https://upload.wikimedia.org/wikipedia/commons/2/29/Experienced_assembly_line_workers_of_both_sexes_contribute_to_the_production_of_A-20_attack_bombers_in_the_Douglas..._-_NARA_-_196397.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original
```


---

# ARQUIVO: `exemplos/deming/regioes.txt`

```text
r00 [  0.68 ->  12.54]  Esse cara é um dos americanos mais ignorados nos Estados Unidos e mais idolatrados no Japão. E ele criou um protocolo polêmico pra provar que demitir funcionário que erra não resolve nada.
r01 [ 13.06 ->  15.47]  Demi foi dar aulas para as fábricas,
r02 [ 16.03 ->  21.26]  Deming foi dar aula para as fábricas do Japão depois da guerra, ganhou medalha do empre...
r03 [ 22.87 ->  34.46]  Deming foi dar aulas para as fábricas do Japão depois da guerra, ganhou medalha do imperador e até hoje as empresas japonesas disputam um prêmio com o nome dele.
r04 [ 34.91 ->  42.41]  E esse é o protocolo para você parar de trocar de funcionário e continuar com o mesmo problema. Primeiro...
r05 [ 42.88 ->  44.22]  "TROCA O CULPADO"
r06 [ 44.61 ->  48.77]  Já trocou 3 vendedores e a venda continua não saindo?
r07 [ 49.23 ->  51.60]  O problema não é o vendedor, porra!
r08 [ 52.04 ->  57.90]  Ele diz que, cada 100 problemas, 94 são do jeito que a empresa funciona.
r09 [ 58.26 ->  61.82]  E quem montou esse jeito foi você, meu querido.
r10 [ 62.31 ->  67.82]  E quem montou esse jeito foi você, meu querido. Segundo, acaba com o ranking.
r11 [ 68.19 ->  78.93]  Ele diz que ranking de funcionário bota um contra o outro. Se o melhor vendedor esconde o cliente do colega pra ficar no topo da lista, foi o ranking que...
r12 [ 79.89 ->  81.66]  Foi o ranking quem ensinou.
r13 [ 82.27 ->  85.07]  E terceiro, arranca o cartaz da parede.
r14 [ 85.44 ->  88.94]  Aquele "Aqui a gente faz certo da primeira vez"
r15 [ 89.34 ->  94.08]  Ele diz que cartaz cobra do funcionário um problema que é da empresa.
r16 [ 94.51 ->  97.28]  Seu time ri do cartaz no almoço biquen...
r17 [ 97.78 -> 106.60]  Seu time ri do cartaz no almoço pequeno gafanhoto. E a virada foi uma caixa de bolinhas. Ele montava uma fábrica de mentira.
r18 [106.96 -> 109.72]  Seis voluntários tiravam bolinha com uma pá
r19 [110.12 -> 112.16]  vermelho era o defeito
r20 [112.59 -> 117.88]  Ele fazia o chefe, elogiava quem tirava pouca e xingava quem tirava muita.
r21 [118.38 -> 120.54]  depois demitia os piores.
r22 [120.99 -> 122.91]  e a vermelha não diminuía
r23 [123.49 -> 128.56]  Uma em cada cinco bolinhas era vermelha. Seu funcionário só erra, meu amigo.
r24 [128.94 -> 129.88]  Olha a caixa
r25 [130.45 -> 133.48]  Se você troca de funcionário e o problema continua
r26 [133.85 -> 134.38]  Me segue.
r27 [134.82 -> 136.50]  Porque você é demais!

28 regioes transcritas
```


---

# ARQUIVO: `exemplos/deming/scripts/mkcut.py`

```python
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
```


---

# ARQUIVO: `exemplos/deming/scripts/cuts.py`

```python
"""Detecta head e tail de cada take mantido -> work/segs.json.
Head: onset por RMS (20 ms, -27 dB, 4 de 8 janelas), recuando ate o piso de ruido, - HEAD_PAD.
Tail: ultima janela acima do piso de ruido (-45 dB) + TAIL_PAD — garante a palavra inteira."""
import numpy as np, wave, json
w=wave.open('work/full.wav'); n=w.getnframes(); sr=w.getframerate()
a=np.frombuffer(w.readframes(n),dtype=np.int16).astype(np.float32)/32768.0
W=int(0.020*sr); nw=len(a)//W
db=20*np.log10(np.sqrt(np.maximum((a[:nw*W].reshape(nw,W)**2).mean(1),1e-12)))
t2w=lambda t:max(0,min(nw-1,int(t/0.020))); w2t=lambda i:round(i*0.020,3)
NOISE=-45.0
# folgas: o crossfade do J-cut (3f) cai inteiro no silêncio e sobra ~0,1 s de respiro entre as falas
# (com 0,12/0,10 e crossfade 5f o fade comia até 76 ms da palavra final — reel André Esteves)
HEAD_PAD=0.20; TAIL_PAD=0.13
# J-cut sem soma de vozes (reel Atul Gawande, 2026-09-27: "as J-cuts nao ficaram tao boas"): a voz de cada
# take termina em `aout` = fim da fala + TA e a do take seguinte comeca em `in` = inicio da fala - HH, emendadas
# ponta a ponta (crossfade de 3 quadros dentro do silencio). O VIDEO do take segura mais LEAD_SRC depois do
# `aout` (out = aout + lead*rate): a voz nova entra 5 quadros ANTES do corte de imagem. Respiro = (TA+HH)/rate.
import json as _j
_P=_j.load(open('assets/edit-plan.json')); RATE=_P.get('rate',1.1); LEAD_SRC=round(_P.get('jcutLeadFrames',5)/30*RATE,3)
TA=0.12; HH=0.15
R={r['i']:r for r in json.load(open('work/regions_cut.json'))}
# Fim da ULTIMA PALAVRA de cada regiao (whisper -ml 1 -sow). Serve de ancora para o tail:
# o piso de -45 dB sozinho entra no decaimento da respiracao e deixa ~1 s de ar morto
# (medido no IKEA: CAMADAS +0,57 s, PROVA +0,86 s).
WEND={int(k):v[-1][2] for k,v in json.load(open('work/region-words-cut.json')).items()}
# POR VIDEO: (label, 1a regiao, ultima regiao) em work/regions_cut.json — reel DEMING
# (regions_cut.json vem de scripts/mkcut.py). TAKES DESCARTADOS (mantido SEMPRE o ULTIMO take valido):
#   c12 (r09 "Pela empresa inteira.") -> c13 · c27+c28+c29 (r22-r24 "E se voce quiser o protocolo completo / Comenta Monge. / Que eu te mando.") -> c30
#   c42 (r34 parte 2 "Seu time gasta...") e c43 (r35 "Se o time gasta como se o dinheiro...") -> c44
# c46+c47+c48 = "Se voce e o unico... me segue, porque voce... e demais" (pausa dramatica, NAO e repeticao: um take so)
TAKES=[
 ("GANCHO",0,0),
 ("PROTOCOLO-POLEMICO",1,1),
 ("DEMING-AULA",4,4),
 ("MEDALHA",5,5),
 ("PREMIO",6,6),
 ("ESSE-PROTOCOLO",7,7),
 ("P1-TROCA-CULPADO",8,9),
 ("P1-TRES-VENDEDORES",10,10),
 ("P1-NAO-E-VENDEDOR",11,11),
 ("P1-NOVENTA-E-QUATRO",12,12),
 ("P1-MEU-QUERIDO",14,14),
 ("P2-RANKING",15,15),
 ("P2-UM-CONTRA-OUTRO",16,16),
 ("P2-ESCONDE-CLIENTE",17,17),
 ("P2-RANKING-ENSINOU",19,19),
 ("P3-CARTAZ",20,20),
 ("P3-FAZ-CERTO",21,21),
 ("P3-COBRA",22,22),
 ("P3-GAFANHOTO",24,24),
 ("VIRADA-CAIXA",25,25),
 ("VIRADA-FABRICA",26,26),
 ("BOLA-PA",27,27),
 ("BOLA-VERMELHA",28,28),
 ("BOLA-CHEFE",29,29),
 ("BOLA-DEMITIA",30,30),
 ("BOLA-NAO-DIMINUIA",31,31),
 ("CLIMAX-UMA-EM-CINCO",32,32),
 ("CLIMAX-SO-ERRA",33,33),
 ("CLIMAX-OLHA-A-CAIXA",34,34),
 ("CTA-ME-SEGUE",35,37),
]
AP=[(lab,R[a]['s'],R[b]['e']) for lab,a,b in TAKES]
res=[];tot=0
print(f"{'i':>2} {'label':<15} {'IN':>7} {'OUT':>7} {'dur':>5}   onset/offset")
for k,(lab,s0,s1) in enumerate(AP):
    # vizinhos no SOURCE (um take descartado pode ficar entre dois mantidos)
    pe=max([r['e'] for r in R.values() if r['e']<=s0+1e-6], default=-1e9)
    ns=min([r['s'] for r in R.values() if r['s']>=s1-1e-6], default=1e9)
    lo,hi=t2w(max(s0-0.8,pe+0.12)),t2w(min(s0+1.2,ns-0.2)); on=None
    for j in range(lo,max(lo+1,hi)):
        if (db[j:j+8]>=-27.0).sum()>=4: on=j; break
    if on is None: on=t2w(s0)
    j=on
    while j>lo and db[j-1]>=NOISE: j-=1
    onset=w2t(j); IN=round(max(0,onset-HEAD_PAD),3)
    # POR VIDEO: head fixo onde a deteccao nao serve (reel DEMING: nenhum)
    # (nenhum ate agora)
    FORCE_IN={}
    if lab in FORCE_IN: onset=round(FORCE_IN[lab]+HEAD_PAD,3); IN=FORCE_IN[lab]
    hi2=t2w(min(s1+0.8,ns-0.15)); lo2=t2w(max(s1-0.8,pe))
    # Tail: ultima janela acima do piso. Mas um respiro/estalo DESTACADO (separado do corpo da
    # fala por >= GAP_MIN de silencio) nao e palavra — e o take ficaria com ~1 s de ar morto
    # (medido no IKEA: CAMADAS +1,2 s e PROVA +0,9 s). Nesses casos recua para o bloco anterior.
    # Nunca corta DENTRO de um bloco contiguo, entao a palavra inteira fica sempre preservada.
    off=None
    for j in range(hi2,lo2,-1):
        if db[j]>=NOISE: off=j+1; break
    if off is None: off=t2w(s1)
    # O whisper as vezes estoura alem do audio (GANCHO: 7,59 contra 7,28 real) e o RMS as vezes
    # entra no respiro (PROVA: 67,00 contra 66,14). Pega o MENOR dos dois...
    we=WEND.get(TAKES[k][2])
    if we is not None:
        cand=min(off,t2w(we)+1)
        # ...e TRAVA: nunca cortar dentro de fala energetica. Se o corpo acima de -35 dB
        # continua depois do candidato, o tail vai ate o fim desse bloco (palavra inteira).
        body=cand
        while body<hi2 and db[body]>=-35.0: body+=1
        cand=max(cand,body)
        if cand<off: print(f"     [{lab}] tail {w2t(off):.2f} -> {w2t(cand):.2f} (fim da palavra {we:.2f}s; -{(off-cand)*0.02:.2f}s de ar morto)")
        off=cand
    # POR VIDEO: fim de fala fixo onde a respiracao seguinte fica acima do piso (reel REED HASTINGS:
    # "fim." termina em 105,42; o piso de -45 dB entrava no respiro ate o "Em" do take seguinte)
    FORCE_OFF={}
    if lab in FORCE_OFF: off=t2w(FORCE_OFF[lab])
    offset=w2t(off); OUT=round(offset+TAIL_PAD,3); d=round(OUT-IN,3); tot+=d
    print(f"{k:>2} {lab:<15} {IN:7.2f} {OUT:7.2f} {d:5.2f}   {onset:.2f}/{offset:.2f}")
    res.append({"i":k,"label":lab,"in":IN,"out":OUT,"region":[TAKES[k][1],TAKES[k][2]],"_on":onset,"_off":offset})
print(f"\nsource {tot:.2f}s -> /1.1 = {tot/1.1:.2f}s ; menos {len(AP)-1} leads(5f) = {tot/1.1-(len(AP)-1)*5/30:.2f}s")
for r in res: r['on'],r['off']=r.pop('_on'),r.pop('_off')
for k,r in enumerate(res):
    r['in']=round(max(0,r['on']-(HEAD_PAD if k==0 else HH)),3); r['aout']=round(r['off']+TA,3)
# Pausa curta (fala a fala < TA+HH no source): a emenda vai no silencio real, 45% para o tail e 55% para a cabeca.
print(f"\nrate {RATE} · lead {LEAD_SRC}s de source · respiro alvo {(TA+HH)/RATE:.3f}s de timeline")
for k in range(len(res)-1):
    a,b=res[k],res[k+1]; g=round(b['on']-a['off'],3)
    if b['in']<a['aout']:
        a['aout']=round(a['off']+g*0.45,3); b['in']=round(b['on']-g*0.55,3)
        # reel HERB KELLEHER: com 45/55 o crossfade (3 f) invadia o inicio da palavra seguinte ("piloto|foi grosso",
        # pausa 0,14 s). Se o crossfade cabe na pausa, a emenda vai logo antes da fala nova e o fade termina no silencio.
        XF=_P.get('jcutCrossfadeFrames',3)/30*RATE
        if g*0.55<XF+0.005 and g>=XF+0.01: b['in']=round(b['on']-XF-0.005,3); a['aout']=b['in']
        print(f"  pausa curta {a['label']} | {b['label']}: fala a fala {g:.2f}s -> emenda em {a['aout']} (respiro {g/RATE:.3f}s)")
for k,r in enumerate(res):
    last=k==len(res)-1
    r['out']=round(r['aout'] if last else r['aout']+LEAD_SRC,3)
    if last: r['out']=r['aout']=round(r['off']+TAIL_PAD,3)
tot=sum(r['out']-r['in'] for r in res)
print(f"source {tot:.2f}s -> /{RATE} menos {len(res)-1} leads = {tot/RATE-(len(res)-1)*5/30:.2f}s")
json.dump(res,open('work/segs.json','w'),indent=1)
```


---

# ARQUIVO: `exemplos/deming/scripts/bipe.py`

```python
"""POR VIDEO — reel DEMING. Bipe de censura gravado na voz, na palavra INTEIRA
(roteiro: "O problema nao e o vendedor, porra... piiii.").
Mapa (envelope 10 ms + bandas, source): "vendedor" decai ate 51,07 · silencio 51,08-51,13 · explosao /p/ 51,14 · "orra" 51,16-51,54 ·
decaimento ate 51,64 · respiracao (alta frequencia) 51,75-51,98.
Varredura da transcricao INTEIRA (28 regioes, inclusive as descartadas): so este palavrao."""
import numpy as np, subprocess, wave, json, os
VOZ=json.load(open('assets/edit-plan.json'))['voiceSrc']                      # assets/<slug>-voz.m4a (voz do projeto, COM bipe)
LIMPA='work/'+os.path.basename(VOZ).replace('.m4a','-limpa.m4a')             # work/<slug>-voz-limpa.m4a (audio do bruto, SEM bipe)
JANELAS=[(51.13,51.645)]  # POR VIDEO: [(ini, fim)] em s do source, palavra INTEIRA. Ex. (reel Kazuo): [(75.905,76.505)]. Vazio = sem bipe (fase2.sh pula)
GAIN=10**(-18/20)*1.75    # bipe ~1 dB acima da frase (Dan Martell: -17,2 contra -18,4)
subprocess.run(['ffmpeg','-v','error','-y','-i',LIMPA,'-ar','48000','-ac','2','-c:a','pcm_s16le','work/voz-limpa48.wav'],check=True)
w=wave.open('work/voz-limpa48.wav'); sr=w.getframerate(); ch=w.getnchannels()
x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32).reshape(-1,ch)/32768
for A,B in JANELAS:
    i0,i1=int(A*sr),int(B*sr); n=i1-i0; t=np.arange(n)/sr
    f=int(0.006*sr); env=np.ones(n); env[:f]=np.linspace(0,1,f); env[-f:]=np.linspace(1,0,f)
    x[i0:i1]=0; x[i0:i1]+= (GAIN*np.sin(2*np.pi*1000*t)*env)[:,None]
y=(np.clip(x,-1,1)*32767).astype(np.int16)
o=wave.open('work/voz-bipe48.wav','wb'); o.setnchannels(ch); o.setsampwidth(2); o.setframerate(sr); o.writeframes(y.tobytes()); o.close()
subprocess.run(['ffmpeg','-v','error','-y','-i','work/voz-bipe48.wav','-c:a','aac','-b:a','192k',VOZ],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i','work/voz-bipe48.wav','-ac','1','-ar','44100','-c:a','pcm_s16le','work/full.wav'],check=True)
print(f'bipes {JANELAS} gravados em {VOZ} e work/full.wav')
```


---

# ARQUIVO: `exemplos/deming/chunks.txt`

```text
ch00 GANCHO               Esse cara é um dos americanos mais ignorados nos Estados Unidos e mais idolatrados no Japão.
ch01 PROTOCOLO-POLEMICO   E ele criou um protocolo polêmico pra provar que demitir funcionário que erra não resolve nada.
ch02 DEMING-AULA          Deming foi dar aulas para as fábricas do Japão depois da guerra,
ch03 MEDALHA              ganhou medalha do imperador e
ch04 PREMIO               até hoje as empresas japonesas disputam um prêmio com o nome dele.
ch05 ESSE-PROTOCOLO       E esse é o protocolo para você parar de trocar de funcionário e continuar com o mesmo problema.
ch06 P1-TROCA-CULPADO     Primeiro... "TROCA O CULPADO"
ch07 P1-TRES-VENDEDORES   Já trocou 3 vendedores e a venda continua não saindo?
ch08 P1-NAO-E-VENDEDOR    O problema não é o vendedor, porra!
ch09 P1-NOVENTA-E-QUATRO  Ele diz que, cada 100 problemas, 94 são do jeito que a empresa funciona.
ch10 P1-MEU-QUERIDO       E quem montou esse jeito foi você, meu querido.
ch11 P2-RANKING           Segundo, acaba com o ranking.
ch12 P2-UM-CONTRA-OUTRO   Ele diz que ranking de funcionário bota um contra o outro.
ch13 P2-ESCONDE-CLIENTE   Se o melhor vendedor esconde o cliente do colega pra ficar no topo da lista,
ch14 P2-RANKING-ENSINOU   Foi o ranking quem ensinou.
ch15 P3-CARTAZ            E terceiro, arranca o cartaz da parede.
ch16 P3-FAZ-CERTO         Aquele "Aqui a gente faz certo da primeira vez"
ch17 P3-COBRA             Ele diz que cartaz cobra do funcionário um problema que é da empresa.
ch18 P3-GAFANHOTO         Seu time ri do cartaz no almoço pequeno gafanhoto.
ch19 VIRADA-CAIXA         E a virada foi uma caixa de bolinhas.
ch20 VIRADA-FABRICA       Ele montava uma fábrica de mentira.
ch21 BOLA-PA              Seis voluntários tiravam bolinha com uma pá
ch22 BOLA-VERMELHA        vermelho era o defeito
ch23 BOLA-CHEFE           Ele fazia o chefe, elogiava quem tirava pouca e xingava quem tirava muita.
ch24 BOLA-DEMITIA         depois demitia os piores.
ch25 BOLA-NAO-DIMINUIA    e a vermelha não diminuía
ch26 CLIMAX-UMA-EM-CINCO  Uma em cada cinco bolinhas era vermelha.
ch27 CLIMAX-SO-ERRA       Seu funcionário só erra, meu amigo.
ch28 CLIMAX-OLHA-A-CAIXA  Olha a caixa
ch29 CTA-ME-SEGUE         Se você troca de funcionário e o problema continua Me segue. Porque você é demais!
30 chunks a partir do passe por regiao (indices de palavra = os desta lista, para a captions_fix_table.py)
```


---

# ARQUIVO: `exemplos/deming/scripts/captions_fix_table.py`

```python
"""POR VIDEO — reel DEMING. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Grafia do roteiro onde o whisper erra so grafia/pontuacao ("pras", "pra", numeros por extenso, "Seu melhor", "que ensinou").
Vale o audio onde ele diz outra coisa: "dar aulas", "esconde O cliente", "vermelhO era O defeito" (roteiro: "Vermelha era defeito").
ch08: "porra" -> P**** (bipe de censura na palavra inteira, scripts/bipe.py, 51,13-51,645 s do source)."""
DROP=None
FIX={
 2:{4:"pras",5:DROP},
 3:{3:"imperador,",4:DROP},
 4:{0:"e até"},
 5:{5:"pra"},
 6:{0:"Primeiro,",1:"troca",2:"o",3:"culpado."},
 7:{2:"três"},
 8:{6:"P****."},
 9:{2:"que",4:"cem",6:"noventa e quatro"},
 13:{0:"Seu",1:DROP},
 14:{3:"que"},
 16:{0:"Aquele",1:"“Aqui",8:"vez.”"},
 18:{6:"almoço,",8:"gafanhoto."},
 21:{6:"pá."},
 22:{0:"Vermelho",3:"defeito."},
 23:{3:"chefe:"},
 24:{0:"Depois,"},
 25:{0:"E",4:"diminuía."},
 27:{5:"amigo?"},
 28:{0:"Olha",2:"caixa."},
 29:{8:"continua,",9:"me",10:"segue,",11:"porque"},
}
FIXT={8:{6:51.13}}  # legenda P**** entra junto com o bipe
```


---

# ARQUIVO: `exemplos/deming/tl-words.txt`

```text
 0 GANCHO                 0.00-  5.90 (5.90)  Esse@0.26 cara@0.27 é@0.55 um@0.61 dos@0.74 americanos@0.94 mais@1.65 ignorados@1.94 nos@2.58 Estados@2.75 Unidos@3.12 e@3.47 mais@3.56 idolatrados@4.07 no@4.78 Japão.@4.92
 1 PROTOCOLO-POLEMICO     5.90- 11.47 (5.57)  E@5.78 ele@6.01 criou@6.04 um@6.36 protocolo@6.49 polêmico@7.11 pra@7.65 provar@7.77 que@8.09 demitir@8.25 funcionário@8.62 que@9.23 erra@9.39 não@9.65 resolve@9.90 nada.@10.53
 2 DEMING-AULA           11.47- 15.55 (4.08)  Deming@11.30 foi@11.91 dar@12.12 aulas@12.54 pras@12.85 fábricas@13.25 do@13.78 Japão@13.90 depois@14.30 da@14.63 guerra,@14.73
 3 MEDALHA               15.55- 17.27 (1.72)  ganhou@15.38 medalha@15.77 do@16.25 imperador,@16.41
 4 PREMIO                17.27- 21.68 (4.41)  e até@17.10 hoje@17.29 as@17.73 empresas@17.83 japonesas@18.30 disputam@18.96 um@19.54 prêmio@19.68 com@20.14 o@20.32 nome@20.39 dele.@20.68
 5 ESSE-PROTOCOLO        21.68- 27.69 (6.01)  E@21.55 esse@21.84 é@21.96 o@22.04 protocolo@22.13 pra@22.92 você@23.08 parar@23.27 de@23.57 trocar@23.86 de@24.28 funcionário@24.38 e@25.05 continuar@25.32 com@26.01 o@26.47 mesmo@26.64 problema.@26.89
 6 P1-TROCA-CULPADO      27.69- 30.19 (2.50)  Primeiro,@27.48 troca@28.21 o@28.86 culpado.@29.02
 7 P1-TRES-VENDEDORES    30.19- 34.26 (4.06)  Já@30.07 trocou@30.34 três@30.73 vendedores@31.07 e@31.87 a@31.96 venda@32.02 continua@32.49 não@33.05 saindo?@33.25
 8 P1-NAO-E-VENDEDOR     34.26- 36.72 (2.46)  O@34.10 problema@34.33 não@34.77 é@34.98 o@35.06 vendedor,@35.13 P****.@35.83
 9 P1-NOVENTA-E-QUATRO   36.72- 42.33 (5.61)  Ele@36.58 diz@36.63 que@36.92 cada@37.30 cem@37.48 problemas,@37.91 noventa e quatro@38.45 são@39.03 do@39.38 jeito@39.53 que@40.02 a@40.32 empresa@40.41 funciona.@41.10
10 P1-MEU-QUERIDO        42.33- 45.10 (2.77)  E@42.01 quem@42.25 montou@42.47 esse@42.87 jeito@43.10 foi@43.51 você,@43.72 meu@43.99 querido.@44.16
11 P2-RANKING            45.10- 47.16 (2.06)  Segundo,@44.97 acaba@45.29 com@45.58 o@45.83 ranking.@45.94
12 P2-UM-CONTRA-OUTRO    47.16- 51.12 (3.95)  Ele@47.03 diz@47.06 que@47.30 ranking@47.60 de@48.02 funcionário@48.17 bota@48.81 um@49.22 contra@49.43 o@50.07 outro.@50.17
13 P2-ESCONDE-CLIENTE    51.12- 55.37 (4.25)  Seu@51.00 melhor@51.21 vendedor@51.27 esconde@51.70 o@52.14 cliente@52.17 do@52.60 colega@52.72 pra@53.19 ficar@53.35 no@53.66 topo@53.79 da@54.04 lista,@54.19
14 P2-RANKING-ENSINOU    55.37- 57.23 (1.86)  Foi@55.23 o@55.48 ranking@55.55 que@55.92 ensinou.@56.24
15 P3-CARTAZ             57.23- 60.04 (2.81)  E@57.07 terceiro,@57.32 arranca@58.09 o@58.53 cartaz@58.60 da@59.03 parede.@59.17
16 P3-FAZ-CERTO          60.04- 63.50 (3.46)  Aquele@59.90 “Aqui@60.49 a@60.93 gente@60.97 faz@61.48 certo@61.62 da@62.01 primeira@62.21 vez.”@62.73
17 P3-COBRA              63.50- 68.04 (4.54)  Ele@63.37 diz@63.44 que@63.59 cartaz@63.86 cobra@64.24 do@64.75 funcionário@64.76 um@65.59 problema@65.69 que@66.12 é@66.60 da@66.65 empresa.@66.93
18 P3-GAFANHOTO          68.04- 71.34 (3.30)  Seu@67.88 time@67.98 ri@68.39 do@68.58 cartaz@68.78 no@69.44 almoço,@69.57 pequeno@70.06 gafanhoto.@70.44
19 VIRADA-CAIXA          71.34- 73.89 (2.56)  E@71.22 a@71.22 virada@71.22 foi@71.53 uma@71.71 caixa@71.97 de@72.38 bolinhas.@72.55
20 VIRADA-FABRICA        73.89- 75.99 (2.10)  Ele@73.76 montava@73.76 uma@74.07 fábrica@74.27 de@74.74 mentira.@74.87
21 BOLA-PA               75.99- 78.82 (2.83)  Seis@75.88 voluntários@76.21 tiravam@76.86 bolinha@77.21 com@77.65 uma@77.93 pá.@78.40
22 BOLA-VERMELHA         78.82- 80.65 (1.83)  Vermelho@78.65 era@79.57 o@79.65 defeito.@79.73
23 BOLA-CHEFE            80.65- 85.69 (5.04)  Ele@80.53 fazia@80.57 o@80.94 chefe:@81.02 elogiava@81.73 quem@82.34 tirava@82.63 pouca@83.11 e@83.42 xingava@83.58 quem@84.09 tirava@84.48 muita.@84.90
24 BOLA-DEMITIA          85.69- 87.94 (2.25)  Depois,@85.56 demitia@86.24 os@86.77 piores.@86.95
25 BOLA-NAO-DIMINUIA     87.94- 90.00 (2.06)  E@87.84 a@87.95 vermelha@88.05 não@88.68 diminuía.@88.81
26 CLIMAX-UMA-EM-CINCO   90.00- 92.81 (2.81)  Uma@89.92 em@89.94 cada@90.09 cinco@90.43 bolinhas@90.85 era@91.54 vermelha.@91.78
27 CLIMAX-SO-ERRA        92.81- 94.67 (1.86)  Seu@92.69 funcionário@92.69 só@93.01 erra,@93.14 meu@93.52 amigo?@93.72
28 CLIMAX-OLHA-A-CAIXA   94.67- 95.86 (1.19)  Olha@94.57 a@94.79 caixa.@94.93
29 CTA-ME-SEGUE          95.86-101.31 (5.45)  Se@95.73 você@96.00 troca@96.16 de@96.55 funcionário@96.61 e@97.41 o@97.56 problema@97.57 continua,@98.26 me@98.95 segue,@99.03 porque@99.91 você@100.18 é@100.54 demais!@100.78
TOTAL 101.31
```


---

# ARQUIVO: `exemplos/deming/assets/edit-plan.json`

```json
{
 "_nota": "Reel Deming — formato viral do Fabio. NUNCA editar index.html a mao: mexer aqui e rodar `node scripts/build-edit.mjs && python3 scripts/bake.py && npm run check`.",
 "fps": 30,
 "rate": 1.1,
 "jcutLeadFrames": 9,
 "jcutCrossfadeFrames": 3,
 "src": "assets/deming-2560-sdr.mp4",
 "voiceSrc": "assets/deming-voz.m4a",
 "segments": [
  {
   "in": 0.4,
   "out": 6.89,
   "label": "GANCHO",
   "chunk": 0,
   "aout": 6.56
  },
  {
   "in": 6.83,
   "out": 13.29,
   "label": "PROTOCOLO-POLEMICO",
   "chunk": 1,
   "aout": 12.96
  },
  {
   "in": 23.01,
   "out": 27.83,
   "label": "DEMING-AULA",
   "chunk": 2,
   "aout": 27.5
  },
  {
   "in": 27.53,
   "out": 29.75,
   "label": "MEDALHA",
   "chunk": 3,
   "aout": 29.42
  },
  {
   "in": 29.43,
   "out": 34.61,
   "label": "PREMIO",
   "chunk": 4,
   "aout": 34.28
  },
  {
   "in": 34.73,
   "out": 41.67,
   "label": "ESSE-PROTOCOLO",
   "chunk": 5,
   "aout": 41.34
  },
  {
   "in": 41.61,
   "out": 44.69,
   "label": "P1-TROCA-CULPADO",
   "chunk": 6,
   "aout": 44.36
  },
  {
   "in": 44.41,
   "out": 49.21,
   "label": "P1-TRES-VENDEDORES",
   "chunk": 7,
   "aout": 48.88
  },
  {
   "in": 49.07,
   "out": 52.11,
   "label": "P1-NAO-E-VENDEDOR",
   "chunk": 8,
   "aout": 51.78
  },
  {
   "in": 51.85,
   "out": 58.35,
   "label": "P1-NOVENTA-E-QUATRO",
   "chunk": 9,
   "aout": 58.02
  },
  {
   "in": 62.33,
   "out": 65.71,
   "label": "P1-MEU-QUERIDO",
   "chunk": 10,
   "aout": 65.38
  },
  {
   "in": 65.63,
   "out": 68.23,
   "label": "P2-RANKING",
   "chunk": 11,
   "aout": 67.9
  },
  {
   "in": 68.01,
   "out": 72.69,
   "label": "P2-UM-CONTRA-OUTRO",
   "chunk": 12,
   "aout": 72.36
  },
  {
   "in": 72.39,
   "out": 77.39,
   "label": "P2-ESCONDE-CLIENTE",
   "chunk": 13,
   "aout": 77.06
  },
  {
   "in": 79.73,
   "out": 82.11,
   "label": "P2-RANKING-ENSINOU",
   "chunk": 14,
   "aout": 81.78
  },
  {
   "in": 82.11,
   "out": 85.53,
   "label": "P3-CARTAZ",
   "chunk": 15,
   "aout": 85.2
  },
  {
   "in": 85.25,
   "out": 89.39,
   "label": "P3-FAZ-CERTO",
   "chunk": 16,
   "aout": 89.06
  },
  {
   "in": 89.15,
   "out": 94.47,
   "label": "P3-COBRA",
   "chunk": 17,
   "aout": 94.14
  },
  {
   "in": 97.61,
   "out": 101.57,
   "label": "P3-GAFANHOTO",
   "chunk": 18,
   "aout": 101.24
  },
  {
   "in": 101.37,
   "out": 104.51,
   "label": "VIRADA-CAIXA",
   "chunk": 19,
   "aout": 104.18
  },
  {
   "in": 104.19,
   "out": 106.83,
   "label": "VIRADA-FABRICA",
   "chunk": 20,
   "aout": 106.5
  },
  {
   "in": 106.77,
   "out": 110.21,
   "label": "BOLA-PA",
   "chunk": 21,
   "aout": 109.88
  },
  {
   "in": 110.27,
   "out": 112.61,
   "label": "BOLA-VERMELHA",
   "chunk": 22,
   "aout": 112.28
  },
  {
   "in": 112.39,
   "out": 118.27,
   "label": "BOLA-CHEFE",
   "chunk": 23,
   "aout": 117.94
  },
  {
   "in": 118.19,
   "out": 120.99,
   "label": "BOLA-DEMITIA",
   "chunk": 24,
   "aout": 120.66
  },
  {
   "in": 120.77,
   "out": 123.37,
   "label": "BOLA-NAO-DIMINUIA",
   "chunk": 25,
   "aout": 123.04
  },
  {
   "in": 123.25,
   "out": 126.67,
   "label": "CLIMAX-UMA-EM-CINCO",
   "chunk": 26,
   "aout": 126.34
  },
  {
   "in": 126.61,
   "out": 128.99,
   "label": "CLIMAX-SO-ERRA",
   "chunk": 27,
   "aout": 128.66
  },
  {
   "in": 128.71,
   "out": 130.35,
   "label": "CLIMAX-OLHA-A-CAIXA",
   "chunk": 28,
   "aout": 130.02
  },
  {
   "in": 130.27,
   "out": 136.59,
   "label": "CTA-ME-SEGUE",
   "chunk": 29,
   "aout": 136.59
  }
 ],
 "sections": [
  {
   "afterSegment": 18,
   "name": "PASSO 3 -> VIRADA (a caixa de bolinhas)"
  },
  {
   "afterSegment": 25,
   "name": "VIRADA -> CLIMAX (uma em cada cinco)"
  },
  {
   "afterSegment": 28,
   "name": "FECHO -> CTA"
  }
 ],
 "broll": [
  {
   "mode": "split",
   "fromSeg": 0,
   "toSeg": 1,
   "span": [
    0.0,
    0.99102
   ],
   "file": ""
  },
  {
   "mode": "split",
   "fromSeg": 19,
   "toSeg": 20,
   "span": [
    0.00043,
    0.99936
   ],
   "file": ""
  }
 ],
 "impacts": [
  {
   "phrase": "nao resolve nada",
   "seg": 1,
   "style": "typing",
   "lines": [
    "NÃO RESOLVE",
    "NADA."
   ],
   "hold": 0.9,
   "top": 6
  },
  {
   "phrase": "foi voce meu querido",
   "seg": 10,
   "lines": [
    "FOI",
    "VOCÊ."
   ],
   "hold": 0.7
  },
  {
   "phrase": "foi o ranking que ensinou",
   "seg": 14,
   "lines": [
    "FOI O RANKING",
    "QUE ENSINOU."
   ],
   "hold": 0.6
  },
  {
   "phrase": "so erra meu amigo",
   "seg": 27,
   "lines": [
    "SÓ",
    "ERRA?"
   ],
   "hold": 0.6
  }
 ],
 "presenterZoom": {
  "scales": [
   1.06,
   1.14
  ],
  "maxHold": 3.5,
  "origin": "50% 53%",
  "mode": "scene",
  "sceneMax": 4.5
 },
 "leakMinGap": 3.5,
 "brollKenBurns": false,
 "bakedAroll": true,
 "bakedAudio": true,
 "bakedBroll": true,
 "bakedLeaks": true,
 "hookSeg": 0,
 "capLowSegs": [],
 "splitShiftY": 520,
 "ctaSeg": 29,
 "_splitShiftY": "400 e so o valor inicial: MEDIR pelos olhos (docs/05, secao Split-screen). Nunca copiar de outro reel.",
 "_ctaSeg": "indice do 1o segmento do encerramento (push-in 1->1.05). Trocar depois do plan_segments.py.",
 "_impacts": "phrase casa com as palavras da legenda normalizadas (sem acento/pontuacao). O 1o leva style typing + drum-fill.",
 "mg": {
  "src": "compositions/mg.html",
  "id": "mg"
 },
 "_mg": "kit v3: camada de motion graphics (docs/13, docs/14). Splits e tela cheia desenhados em compositions/mg.html; sections so nas trocas grandes (virada, CLIMAX, CTA)."
}
```


---

# ARQUIVO: `exemplos/deming/scripts/slots.py`

```python
"""POR VIDEO — reel DEMING. Mapa dos slots em tempo ABSOLUTO de timeline (rate 1.1, timeline 101,31 s).
Kit v3: TODO slot vira camada de motion (compositions/mg.html); os splits continuam no plan.broll com file "" (o split arrasta
o apresentador; a faixa de cima e da camada). Layout desenhado sobre as folhas gaze/me/g*.jpg — nitidas: 11,58 · 14,04 ·
30,46-30,70 · 33,38-33,59 · 45,20 · 84,02-84,55 · 95,17-95,41 (todas cobertas por motion). Revelacao em 11,37 ("Deming" em 11,30 s);
apresentador no bipe (34,26-36,72); split 2 (a virada) 71,34-75,99; climax 90,00 ("Uma em cada cinco bolinhas")."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 ("s01","split", 0.00, 11.37,"Esse cara é um dos americanos mais ignorados… E ele criou um protocolo polêmico… não resolve nada.","CAPA (Codex, a pedido): aula na fábrica japonesa em 1950, professor de costas → crachás trocados + DEMITIDO (pré-revelação)","— (quadro 0 = capa)"),
 ("s02","full", 11.37, 21.68,"Deming foi dar aulas pras fábricas do Japão… medalha do imperador… prêmio com o nome dele.","REVELAÇÃO: retrato (Wikipedia) → aula em Tóquio 1950 (JUSE) → medalha do imperador (JUSE + Commons) → Prêmio Deming (JUSE)","olhadas 11,58 · 14,04"),
 ("s03","full", 25.30, 34.26,"…continuar com o mesmo problema. Primeiro, troca o culpado. Já trocou três vendedores…","loop de crachás · chip PASSO 1 · três vendedores e a venda parada","olhadas 30,46–30,70 · 33,38–33,59"),
 ("s04","full", 36.72, 42.33,"De cada cem problemas, noventa e quatro são do jeito que a empresa funciona.","grade de 100 pontos, 94 do sistema","—"),
 ("s05","full", 45.10, 55.37,"Segundo, acaba com o ranking… um contra o outro… esconde o cliente do colega","chip PASSO 2 · ranking de vendedores","olhada 45,20"),
 ("s06","full", 57.23, 64.90,"E terceiro, arranca o cartaz da parede. Aquele “Aqui a gente faz certo da primeira vez.”","chip PASSO 3 · cartaz motivacional arrancado","—"),
 ("s07","full", 68.04, 71.34,"Seu time ri do cartaz no almoço, pequeno gafanhoto.","balões kkkk + Mestre Po (Kung Fu)","olhadas 68,97–70,46"),
 ("s08","split",71.34, 75.99,"E a virada foi uma caixa de bolinhas. Ele montava uma fábrica de mentira.","a caixa de contas: brancas e vermelhas","—"),
 ("s09","full", 75.99, 87.94,"Seis voluntários tiravam bolinha com uma pá… elogiava… xingava… demitia os piores… não diminuía.","a pá de 50 furos · placar dos 6 · elogio/bronca · DEMITIDO · gráfico parado","olhadas 76,5 · 78,98 · 84,02–84,55 · 86,40"),
 ("s10","full", 90.00, 92.81,"Uma em cada cinco bolinhas era vermelha.","CLÍMAX: 5 bolinhas, 1 vermelha — 20% (riser + impact)","—"),
 ("s11","full", 94.67, 95.86,"Olha a caixa.","volta à caixa (callback da virada)","olhada 95,17–95,41"),
]
NOMES={k[0]:k[0] for k in S}
def seg_of(x, end=False):
    for i,(a,b) in enumerate(segs):
        if (a<=x<b) if not end else (a<x<=b+1e-6): return i
    return len(segs)-1
slots=[]
for sid,mode,t0,t1,fala,tema,cobre in S:
    f=seg_of(t0); g=seg_of(t1,end=True); w0,w1=segs[f][0],segs[g][1]
    sp=[round((t0-w0)/(w1-w0),5),round((t1-w0)/(w1-w0),5)]
    slots.append(dict(id=sid,file=f"assets/broll/{NOMES[sid]}.mp4",mode=mode,fromSeg=f,toSeg=g,span=sp,
                      t0=t0,t1=t1,dur=round(t1-t0,2),fala=fala,tema=tema,cobre=cobre))
old={x['id']:x for x in json.load(open('assets/broll-slots.json')).get('slots',[])} if os.path.exists('assets/broll-slots.json') else {}
for s in slots:  # preserva campos da pesquisa (img, link, fonte, prompt...) ja gravados
    for k,v in old.get(s['id'],{}).items():
        if k not in s: s[k]=v
json.dump({"total":TOTAL,"slots":slots},open('assets/broll-slots.json','w'),ensure_ascii=False,indent=1)
print(f"{len(slots)} slots · timeline {TOTAL}s")
# POR VIDEO: slots que viraram motion graphics (compositions/mg.html, docs/13): ficam no broll-slots.json (tempos de
# referencia) e saem do plan.broll. Vazio = todo slot vira video de B-roll (fluxo antigo).
MG={"*"}  # "*" = TODO slot vira camada de motion (kit v3, padrao). set() = fluxo antigo (todo slot vira video)
def plan_broll(path_of):
    # kit v3: slot MG em split continua no plano com file "" (o split arrasta o apresentador; a faixa de cima e da camada)
    return [{k:s[k] for k in ('mode','fromSeg','toSeg','span')}|{"file":("" if ('*' in MG or s['id'] in MG) else path_of(s))} for s in slots
            if not ('*' in MG or s['id'] in MG) or s['mode']=='split']
if '--placeholders' in sys.argv:
    from PIL import Image, ImageDraw, ImageFont
    os.makedirs('assets/broll/_ph',exist_ok=True)
    try: fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',46); fs=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',30)
    except Exception: fnt=fs=ImageFont.load_default()
    for k,s in enumerate(slots):
        W,H=(720,1280) if s["mode"]=="full" else (720,564)
        im=Image.new('RGB',(W,H),[(38,52,86),(70,44,86),(40,78,70),(86,62,36)][k%4]); d=ImageDraw.Draw(im)
        y=H*0.30 if s['mode']=='full' else 60
        for line in [f"B-ROLL {s['id']}", "aguardando arquivo", NOMES[s['id']]+".mp4", f"{s['dur']:.2f}s"]:
            d.text((W/2,y),line,font=fnt if line.startswith('B-') else fs,fill=(255,255,255),anchor='mm'); y+=70
        png=f"assets/broll/_ph/{s['id']}.png"; im.save(png)
        subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-i',png,'-t',f"{s['dur']+0.2:.2f}",'-r','60','-c:v','libx264','-pix_fmt','yuv420p','-g','30','-crf','30',f"assets/broll/_ph/{s['id']}.mp4"],check=True)
    P['broll']=plan_broll(lambda s:f"assets/broll/_ph/{s['id']}.mp4"); P['_broll']="PLACEHOLDERS (cartoes rotulados) — slots aguardando os B-rolls do usuario. Ver PESQUISAS-BROLL-DEMING.md."
    json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1); print("plan.broll -> placeholders")
if '--real' in sys.argv:
    P['broll']=plan_broll(lambda s:s['file']); json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1); print("plan.broll -> arquivos finais")
```


---

# ARQUIVO: `exemplos/deming/assets/broll-slots.json`

```json
{
 "total": 101.31,
 "slots": [
  {
   "id": "s01",
   "file": "assets/broll/s01.mp4",
   "mode": "split",
   "fromSeg": 0,
   "toSeg": 1,
   "span": [
    0.0,
    0.99102
   ],
   "t0": 0.0,
   "t1": 11.37,
   "dur": 11.37,
   "fala": "Esse cara é um dos americanos mais ignorados… E ele criou um protocolo polêmico… não resolve nada.",
   "tema": "CAPA (Codex, a pedido): aula na fábrica japonesa em 1950, professor de costas → crachás trocados + DEMITIDO (pré-revelação)",
   "cobre": "— (quadro 0 = capa)"
  },
  {
   "id": "s02",
   "file": "assets/broll/s02.mp4",
   "mode": "full",
   "fromSeg": 1,
   "toSeg": 4,
   "span": [
    0.3466,
    0.99987
   ],
   "t0": 11.37,
   "t1": 21.68,
   "dur": 10.31,
   "fala": "Deming foi dar aulas pras fábricas do Japão… medalha do imperador… prêmio com o nome dele.",
   "tema": "REVELAÇÃO: retrato (Wikipedia) → aula em Tóquio 1950 (JUSE) → medalha do imperador (JUSE + Commons) → Prêmio Deming (JUSE)",
   "cobre": "olhadas 11,58 · 14,04"
  },
  {
   "id": "s03",
   "file": "assets/broll/s03.mp4",
   "mode": "full",
   "fromSeg": 5,
   "toSeg": 8,
   "span": [
    0.24061,
    0.83647
   ],
   "t0": 25.3,
   "t1": 34.26,
   "dur": 8.96,
   "fala": "…continuar com o mesmo problema. Primeiro, troca o culpado. Já trocou três vendedores…",
   "tema": "loop de crachás · chip PASSO 1 · três vendedores e a venda parada",
   "cobre": "olhadas 30,46–30,70 · 33,38–33,59"
  },
  {
   "id": "s04",
   "file": "assets/broll/s04.mp4",
   "mode": "full",
   "fromSeg": 9,
   "toSeg": 10,
   "span": [
    0.00012,
    0.66941
   ],
   "t0": 36.72,
   "t1": 42.33,
   "dur": 5.61,
   "fala": "De cada cem problemas, noventa e quatro são do jeito que a empresa funciona.",
   "tema": "grade de 100 pontos, 94 do sistema",
   "cobre": "—"
  },
  {
   "id": "s05",
   "file": "assets/broll/s05.mp4",
   "mode": "full",
   "fromSeg": 10,
   "toSeg": 14,
   "span": [
    0.18603,
    0.87524
   ],
   "t0": 45.1,
   "t1": 55.37,
   "dur": 10.27,
   "fala": "Segundo, acaba com o ranking… um contra o outro… esconde o cliente do colega",
   "tema": "chip PASSO 2 · ranking de vendedores",
   "cobre": "olhada 45,20"
  },
  {
   "id": "s06",
   "file": "assets/broll/s06.mp4",
   "mode": "full",
   "fromSeg": 15,
   "toSeg": 17,
   "span": [
    9e-05,
    0.70969
   ],
   "t0": 57.23,
   "t1": 64.9,
   "dur": 7.67,
   "fala": "E terceiro, arranca o cartaz da parede. Aquele “Aqui a gente faz certo da primeira vez.”",
   "tema": "chip PASSO 3 · cartaz motivacional arrancado",
   "cobre": "—"
  },
  {
   "id": "s07",
   "file": "assets/broll/s07.mp4",
   "mode": "full",
   "fromSeg": 18,
   "toSeg": 19,
   "span": [
    0.00034,
    0.56396
   ],
   "t0": 68.04,
   "t1": 71.34,
   "dur": 3.3,
   "fala": "Seu time ri do cartaz no almoço, pequeno gafanhoto.",
   "tema": "balões kkkk + Mestre Po (Kung Fu)",
   "cobre": "olhadas 68,97–70,46"
  },
  {
   "id": "s08",
   "file": "assets/broll/s08.mp4",
   "mode": "split",
   "fromSeg": 19,
   "toSeg": 20,
   "span": [
    0.00043,
    0.99936
   ],
   "t0": 71.34,
   "t1": 75.99,
   "dur": 4.65,
   "fala": "E a virada foi uma caixa de bolinhas. Ele montava uma fábrica de mentira.",
   "tema": "a caixa de contas: brancas e vermelhas",
   "cobre": "—"
  },
  {
   "id": "s09",
   "file": "assets/broll/s09.mp4",
   "mode": "full",
   "fromSeg": 20,
   "toSeg": 25,
   "span": [
    0.13018,
    0.87205
   ],
   "t0": 75.99,
   "t1": 87.94,
   "dur": 11.95,
   "fala": "Seis voluntários tiravam bolinha com uma pá… elogiava… xingava… demitia os piores… não diminuía.",
   "tema": "a pá de 50 furos · placar dos 6 · elogio/bronca · DEMITIDO · gráfico parado",
   "cobre": "olhadas 76,5 · 78,98 · 84,02–84,55 · 86,40"
  },
  {
   "id": "s10",
   "file": "assets/broll/s10.mp4",
   "mode": "full",
   "fromSeg": 25,
   "toSeg": 26,
   "span": [
    0.42335,
    1.0
   ],
   "t0": 90.0,
   "t1": 92.81,
   "dur": 2.81,
   "fala": "Uma em cada cinco bolinhas era vermelha.",
   "tema": "CLÍMAX: 5 bolinhas, 1 vermelha — 20% (riser + impact)",
   "cobre": "—"
  },
  {
   "id": "s11",
   "file": "assets/broll/s11.mp4",
   "mode": "full",
   "fromSeg": 27,
   "toSeg": 28,
   "span": [
    0.60884,
    0.99836
   ],
   "t0": 94.67,
   "t1": 95.86,
   "dur": 1.19,
   "fala": "Olha a caixa.",
   "tema": "volta à caixa (callback da virada)",
   "cobre": "olhada 95,17–95,41"
  }
 ]
}
```


---

# ARQUIVO: `exemplos/deming/gen.py`

```python
"""POR VIDEO — reel DEMING. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Markup repetitivo (bolinhas, grade de 100, pa) sai daqui, deterministico.
uso: python3 work/mg/gen.py"""
import random
T = open('work/mg/template.html').read()
R = random.Random(1950)

WHITE = "b"; RED = "b r"
def beads(cols, rows, nred, size, gap, cls=""):
    idx = set(R.sample(range(cols * rows), nred))
    out = []
    for k in range(cols * rows):
        x, y = (k % cols) * (size + gap), (k // cols) * (size + gap)
        out.append(f'<i class="{RED if k in idx else WHITE} {cls}" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px"></i>')
    return ''.join(out)

CSS = r'''
        /* ===== reel DEMING ===== */
        #mg .light { background: linear-gradient(180deg, rgba(17,20,26,0) 0%, rgba(17,20,26,0) 64%, #11141A 73%), radial-gradient(130% 80% at 50% 28%, #FFFFFF 0%, #E8E6E1 78%); }
        #mg .tag { white-space: nowrap; }
        #mg .b { position: absolute; display: block; border-radius: 50%;
                 background: radial-gradient(circle at 34% 30%, #FFFFFF 0%, #E9E5DC 45%, #A8A196 100%); box-shadow: 0 3px 6px rgba(0,0,0,.35); }
        #mg .b.r { background: radial-gradient(circle at 34% 30%, #FF9A90 0%, #E5322D 50%, #8E1612 100%); }
        #mg .box { position: absolute; border-radius: 40px; background: linear-gradient(180deg, #6B4A2E, #4A3220); padding: 0;
                   box-shadow: inset 0 0 0 14px #3A2616, 0 30px 80px rgba(0,0,0,.55); overflow: hidden; }
        #mg .box .in { position: absolute; }
        #mg .badge { position: absolute; width: 300px; height: 400px; border-radius: 30px; background: #fff; box-shadow: 0 24px 60px rgba(0,0,0,.4); overflow: hidden; }
        #mg .badge .hd { height: 64px; background: #11141A; color: #fff; font-weight: 800; font-size: 24px; letter-spacing: .12em; line-height: 64px; text-align: center; }
        #mg .badge .av { position: absolute; left: 80px; top: 92px; width: 140px; height: 140px; border-radius: 50%; background: #D9DCE2; overflow: hidden; }
        #mg .badge .av::before { content: ""; position: absolute; left: 42px; top: 24px; width: 56px; height: 56px; border-radius: 50%; background: #9AA0AB; }
        #mg .badge .av::after { content: ""; position: absolute; left: 22px; top: 90px; width: 96px; height: 80px; border-radius: 48px 48px 0 0; background: #9AA0AB; }
        #mg .badge b { position: absolute; left: 0; width: 300px; top: 256px; text-align: center; font-weight: 800; font-size: 34px; color: #11141A; }
        #mg .badge .ln { position: absolute; left: 60px; width: 180px; height: 16px; border-radius: 8px; background: #E3E5EA; }
        #mg .err { position: absolute; padding: 10px 24px; border-radius: 999px; background: #E5322D; color: #fff; font-weight: 800; font-size: 28px; letter-spacing: .08em; }
        #mg .grid100 { position: absolute; left: 161px; width: 758px; height: 758px; }
        #mg .grid100 i { position: absolute; width: 56px; height: 56px; border-radius: 50%; background: #2A303C; }
        #mg .legend { position: absolute; left: 0; width: 1080px; display: flex; justify-content: center; gap: 24px; }
        #mg .legend span { padding: 16px 30px; border-radius: 999px; font-weight: 800; font-size: 32px; letter-spacing: .05em; color: #fff; display: flex; gap: 14px; align-items: center; }
        #mg .legend span::before { content: ""; width: 26px; height: 26px; border-radius: 50%; background: currentColor; }
        #mg .big { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; color: #fff; line-height: 1; }
        #mg .digit { display: inline-block; height: 230px; overflow: hidden; vertical-align: top; }
        #mg .digit div span { display: block; height: 230px; line-height: 230px; font-size: 230px; width: 150px; text-align: center; }
        #mg .lb { position: absolute; left: 60px; width: 960px; border-radius: 44px; background: #fff; padding: 34px 40px 20px; box-shadow: 0 34px 90px rgba(0,0,0,.22); }
        #mg .lb .hd { display: flex; justify-content: space-between; font-weight: 800; font-size: 32px; letter-spacing: .08em; color: #11141A; margin-bottom: 10px; }
        #mg .lb .hd i { font-style: normal; color: #8C93A1; font-weight: 600; }
        #mg .lr { position: relative; height: 116px; display: flex; align-items: center; gap: 26px; border-top: 2px solid rgba(128,136,150,.18); font-weight: 800; color: #11141A; background: #fff; }
        #mg .lr .pos { width: 80px; font-size: 44px; color: #8C93A1; }
        #mg .lr .av2 { width: 72px; height: 72px; border-radius: 50%; background: #D9DCE2; flex: none; }
        #mg .lr .nm { flex: 1; font-size: 40px; }
        #mg .lr .val { font-size: 40px; color: #1FB45A; }
        #mg .poster { position: absolute; left: 150px; top: 230px; width: 780px; height: 1010px; border-radius: 10px; background: #13294B; color: #FFD23F;
                      box-shadow: 0 30px 70px rgba(0,0,0,.4); text-align: center; font-weight: 800; transform-origin: 50% 0%; }
        #mg .poster .star { margin-top: 90px; font-size: 150px; line-height: 1; color: #FFD23F; }
        #mg .poster .pl { display: block; font-size: 92px; line-height: 1.06; letter-spacing: .01em; }
        #mg .poster .ft { position: absolute; left: 0; bottom: 60px; width: 780px; font-size: 28px; letter-spacing: .3em; color: #8FA3C4; }
        #mg .tape { position: absolute; width: 170px; height: 54px; background: rgba(240,232,210,.85); }
        #mg .paddle { position: absolute; left: 190px; width: 700px; height: 380px; border-radius: 36px; background: linear-gradient(180deg, #8A8F99, #5D626C);
                      box-shadow: 0 30px 70px rgba(0,0,0,.55); }
        #mg .paddle .h { position: absolute; left: 290px; top: 370px; width: 120px; height: 360px; border-radius: 0 0 40px 40px; background: linear-gradient(90deg, #6E737D, #4B5059); }
        #mg .paddle .hole { position: absolute; width: 50px; height: 50px; border-radius: 50%; background: #2A2E35; box-shadow: inset 0 4px 8px rgba(0,0,0,.6); }
        #mg .ppl { position: absolute; left: 0; width: 1080px; display: flex; justify-content: center; gap: 26px; }
        #mg .ppl span { width: 120px; height: 120px; border-radius: 50%; background: #2A303C; position: relative; overflow: hidden; }
        #mg .ppl span::before { content: ""; position: absolute; left: 38px; top: 20px; width: 44px; height: 44px; border-radius: 50%; background: #8C93A1; }
        #mg .ppl span::after { content: ""; position: absolute; left: 20px; top: 72px; width: 80px; height: 64px; border-radius: 40px 40px 0 0; background: #8C93A1; }
        #mg .sb { position: absolute; left: 60px; width: 960px; border-radius: 44px; background: #151A23; border: 2px solid #252C39; padding: 30px 40px 16px; box-shadow: 0 34px 90px rgba(0,0,0,.4); }
        #mg .sb .hd { display: flex; justify-content: space-between; font-weight: 800; font-size: 32px; letter-spacing: .08em; color: #E9ECF2; margin-bottom: 6px; }
        #mg .sb .hd i { font-style: normal; color: #8C93A1; font-weight: 600; }
        #mg .sr { position: relative; height: 112px; display: flex; align-items: center; gap: 24px; border-top: 2px solid rgba(128,136,150,.18); color: #E9ECF2; font-weight: 800; }
        #mg .sr .nm { width: 220px; font-size: 40px; }
        #mg .sr .cnt { display: flex; align-items: center; gap: 12px; font-size: 40px; color: #FF6B5E; width: 150px; }
        #mg .sr .cnt::before { content: ""; width: 34px; height: 34px; border-radius: 50%; background: radial-gradient(circle at 34% 30%, #FF9A90, #E5322D 50%, #8E1612); }
        #mg .sr .msg { padding: 10px 24px; border-radius: 999px; font-size: 30px; letter-spacing: .05em; }
        #mg .chart { position: absolute; left: 60px; width: 960px; height: 720px; border-radius: 44px; background: #151A23; border: 2px solid #252C39; }
'''

# ---------------- markup ----------------
def badge(id_, nome, left, top, extra=""):
    return (f'<div class="badge" id="{id_}" style="left:{left}px;top:{top}px{extra}"><div class="hd">CRACHÁ</div><div class="av"></div>'
            f'<b>{nome}</b><i class="ln" style="top:316px"></i><i class="ln" style="top:346px;width:120px;left:90px"></i></div>')

grid = ''.join(f'<i class="{"D-sys" if k < 94 else "D-pes"}" style="left:{(k%10)*78}px;top:{(k//10)*78}px"></i>' for k in range(100))
# pa: 10 x 5 furos; algumas vermelhas dentro
holes, pbeads = [], []
pred = set(R.sample(range(50), 9))
for k in range(50):
    x, y = 45 + (k % 10) * 63, 40 + (k // 10) * 63
    holes.append(f'<i class="hole" style="left:{x}px;top:{y}px"></i>')
    pbeads.append(f'<i class="{RED if k in pred else WHITE} {"I-red" if k in pred else "I-wh"}" style="left:{x+2}px;top:{y+2}px;width:46px;height:46px"></i>')

SC = [('ANA', 7), ('BIA', 12), ('CAIO', 9), ('DANI', 15), ('EDU', 6), ('LUCA', 10)]
MSG = {4: ("PARABÉNS!", "#1FB45A"), 0: ("MUITO BEM!", "#1FB45A"), 3: ("INACEITÁVEL!", "#E5322D"), 1: ("DE NOVO?!", "#E5322D")}
rows = ''.join(f'<div class="sr" id="I-s{k}"><span class="nm">{n}</span><span class="cnt">{c}</span>'
               + (f'<span class="msg" id="I-m{k}" style="background:{MSG[k][1]};color:#fff">{MSG[k][0]}</span>' if k in MSG else '') + '</div>'
               for k, (n, c) in enumerate(SC))

HTML = f'''
        <!-- A · SPLIT DA CAPA (0–11,37), faixa de cima SÓ COM IMAGENS: aula na fábrica (Codex) → operário (LOC) → desempregado (Dorothea Lange) -->
        <div class="scene" id="A" style="height:845px">
          <div class="full" id="A-capa"><img id="A-capaimg" src="assets/mg/capa.png" style="object-position:50% 30%" /></div>
          <div class="full" id="A-op"><img id="A-opimg" src="assets/mg/operario.jpg" style="object-position:55% 40%" /></div>
          <div class="full" id="A-des"><img id="A-desimg" src="assets/mg/desempregado.jpg" style="object-position:62% 38%" /></div>
        </div>

        <!-- B · REVELAÇÃO (11,37–21,68): Deming → aula em Tóquio 1950 → medalha do imperador → Prêmio Deming -->
        <div class="scene" id="B"><div class="world dark"><div class="band" id="B-band"></div></div>
          <div class="card" id="B-dem" style="left:70px;top:190px;width:940px;height:655px"><img src="assets/mg/deming.jpg" style="object-position:60% 30%" /></div>
          <div class="name" id="B-name" style="top:900px"><b>W. EDWARDS DEMING</b><i>ESTATÍSTICO AMERICANO · 1900–1993</i></div>
          <div class="card" id="B-aula" style="left:190px;top:170px;width:700px;height:790px"><img src="assets/mg/aula1950.jpg" style="filter:sepia(.25)" /></div>
          <div class="tag" id="B-tq" style="left:190px;top:1000px;background:#BC002D">TÓQUIO · JULHO DE 1950</div>
          <div class="card" id="B-med" style="left:120px;top:170px;width:560px;height:840px"><img src="assets/mg/medalha-imperador.jpg" style="filter:sepia(.2)" /></div>
          <div class="card" id="B-ord" style="left:600px;top:420px;width:400px;height:407px"><img src="assets/mg/tesouro-sagrado.png" /></div>
          <div class="tag" id="B-imp" style="left:120px;top:1060px;background:#BC002D">MEDALHA DO IMPERADOR · 1960</div>
          <div class="card" id="B-prem" style="left:210px;top:180px;width:660px;height:660px;border-radius:50%;background:#fff"><img src="assets/mg/premio-deming.jpg" style="object-fit:contain;transform:scale(.94)" /></div>
          <div class="title" id="B-pt" style="top:900px;color:#fff;font-size:96px">PRÊMIO DEMING</div>
          <div class="tag" id="B-desde" style="left:250px;top:1030px;background:#BC002D">DISPUTADO DESDE 1951</div>
        </div>

        <!-- C · LINHA DE MONTAGEM → PASSO 1 → O VENDEDOR (25,30–34,26) -->
        <div class="scene" id="C"><div class="world light"><div class="band" id="C-band"></div></div>
          <div class="full" id="C-linha"><img id="C-linhaimg" src="assets/mg/linha.jpg" style="object-position:50% 45%" /></div>
          <div class="chip" id="C-chip" style="top:300px"><span class="dot" style="background:radial-gradient(circle at 34% 30%,#FF9A90,#E5322D 50%,#8E1612)"></span><div class="win"><div class="roll" id="C-roll"><span>PASSO 3</span><span>PASSO 2</span><span>PASSO 1</span></div></div><div class="plus" id="C-plus">+</div></div>
          <div class="title" id="C-title" style="top:520px"><span id="C-w1">TROCA</span> <span id="C-w2">O</span><br /><span class="sel" id="C-sel"><span id="C-w3">CULPADO.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="full" id="C-vend"><img id="C-vendimg" src="assets/mg/vendedor.jpg" style="object-position:72% 50%" /></div>
          <div class="tag" id="C-n3" style="left:330px;top:180px;background:#E5322D;font-size:46px">VENDEDOR Nº 3</div>
        </div>

        <!-- D · 94 DE CADA 100 (36,72–42,33) -->
        <div class="scene" id="D"><div class="world dark"><div class="band" id="D-band"></div></div>
          <div class="big" id="D-num" style="top:120px;color:#FF5A4E"><span class="digit"><div id="D-d1"><span>0</span><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span></div></span><span class="digit"><div id="D-d2"><span>0</span><span>1</span><span>2</span><span>3</span><span>4</span></div></span><span style="font-size:120px;vertical-align:top;line-height:230px">&nbsp;de 100</span></div>
          <div class="grid100" id="D-grid" style="top:390px">{grid}</div>
          <div class="legend" id="D-leg" style="top:1190px"><span id="D-l1" style="background:#2A1416;color:#FF5A4E"><em style="font-style:normal;color:#fff">94 · O JEITO DA EMPRESA</em></span><span id="D-l2" style="background:#2A303C;color:#fff"><em style="font-style:normal">6 · A PESSOA</em></span></div>
        </div>

        <!-- E · PASSO 2: ACABA COM O RANKING (45,10–55,37) -->
        <div class="scene" id="E"><div class="world light"><div class="band" id="E-band"></div></div>
          <div class="chip" id="E-chip" style="top:250px"><span class="dot" style="background:radial-gradient(circle at 34% 30%,#FF9A90,#E5322D 50%,#8E1612)"></span><div class="win"><div class="roll" id="E-roll"><span>PASSO 1</span><span>PASSO 3</span><span>PASSO 2</span></div></div><div class="plus" id="E-plus">+</div></div>
          <div class="title" id="E-title" style="top:470px"><span id="E-w1">ACABA</span> <span id="E-w2">COM</span> <span id="E-w3">O</span><br /><span class="sel" id="E-sel"><span id="E-w4">RANKING.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="full" id="E-mes"><img id="E-mesimg" src="assets/mg/emp-mes.jpg" style="object-position:50% 50%" /></div>
          <div class="lb" id="E-lb" style="top:200px">
            <div class="hd"><span>RANKING DE VENDAS</span><i>OUTUBRO</i></div>
            <div class="lr" id="E-r1"><span class="pos" style="color:#F2B705">1º</span><span class="av2"></span><span class="nm">RAFAEL</span><span class="val">R$ 182 mil</span></div>
            <div class="lr" id="E-r2"><span class="pos">2º</span><span class="av2"></span><span class="nm">CAMILA</span><span class="val">R$ 176 mil</span></div>
            <div class="lr" id="E-r3"><span class="pos">3º</span><span class="av2"></span><span class="nm">BRUNO</span><span class="val">R$ 171 mil</span></div>
            <div class="lr" id="E-r4"><span class="pos">4º</span><span class="av2"></span><span class="nm">JÚLIA</span><span class="val">R$ 140 mil</span></div>
            <div class="lr" id="E-r5"><span class="pos">5º</span><span class="av2"></span><span class="nm">TIAGO</span><span class="val">R$ 122 mil</span></div>
          </div>
          <div class="tag" id="E-vs" style="left:330px;top:1140px;background:#E5322D;font-size:46px">UM CONTRA O OUTRO</div>
          <div class="toast" id="E-toast" style="top:1110px"><div class="ic" style="background:#1FB45A;color:#fff">$</div><div><b>CLIENTE DA CAMILA</b><p>Pedido de R$ 40 mil</p></div></div>
          <div class="tag" id="E-esc" style="left:520px;top:303px;background:#11141A;font-size:30px;padding:12px 26px">ESCONDEU</div>
          <div class="tag" id="E-topo" style="left:340px;top:1140px;background:#F2B705;color:#11141A;font-size:46px">▲ TOPO DA LISTA</div>
        </div>

        <!-- F · PASSO 3: ARRANCA O CARTAZ (57,23–64,90) -->
        <div class="scene" id="F"><div class="world light"><div class="band" id="F-band"></div></div>
          <div class="chip" id="F-chip" style="top:300px"><span class="dot" style="background:radial-gradient(circle at 34% 30%,#FF9A90,#E5322D 50%,#8E1612)"></span><div class="win"><div class="roll" id="F-roll"><span>PASSO 2</span><span>PASSO 1</span><span>PASSO 3</span></div></div><div class="plus" id="F-plus">+</div></div>
          <div class="title" id="F-title" style="top:520px"><span id="F-w1">ARRANCA</span> <span id="F-w2">O</span><br /><span class="sel" id="F-sel"><span id="F-w3">CARTAZ.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="poster" id="F-poster">
            <div class="star">★</div>
            <div style="margin-top:50px"><span class="pl" id="F-p1">AQUI A</span><span class="pl" id="F-p2">GENTE FAZ</span><span class="pl" id="F-p3">CERTO DA</span><span class="pl" id="F-p4">PRIMEIRA</span><span class="pl" id="F-p5">VEZ!</span></div>
            <div class="ft">QUALIDADE TOTAL</div>
            <div class="tape" style="left:-40px;top:-14px;transform:rotate(-30deg)"></div><div class="tape" style="right:-40px;top:-14px;transform:rotate(30deg)"></div>
          </div>
          <div class="tag" id="F-cobra" style="left:180px;top:150px;background:#E5322D">COBRA DO FUNCIONÁRIO</div>
        </div>

        <!-- G · RI DO CARTAZ → PEQUENO GAFANHOTO (68,04–71,34) -->
        <div class="scene" id="G"><div class="world dark"><div class="band" id="G-band"></div></div>
          <div class="full" id="G-alm"><img id="G-almimg" src="assets/mg/almoco.jpg" style="object-position:40% 45%" /></div>
          <div class="card" id="G-po" style="left:70px;top:220px;width:940px;height:900px"><img src="assets/mg/gafanhoto.jpg" style="object-position:40% 50%" /></div>
          <div class="tag" id="G-gaf" style="left:190px;top:1170px;background:#F2B705;color:#11141A">PEQUENO GAFANHOTO</div>
        </div>

        <!-- H · SPLIT DA VIRADA (71,34–75,99), faixa de cima: a caixa de bolinhas -->
        <div class="scene" id="H" style="height:845px"><div class="panel" id="H-panel" style="background:radial-gradient(120% 90% at 50% 20%, #1B2130 0%, #0C0F15 70%)">
          <div class="box" id="H-box" style="left:80px;top:170px;width:920px;height:560px"><div class="in" id="H-in" style="left:46px;top:58px">{beads(14,8,22,52,8,'H-b')}</div></div>
          <div class="tag" id="H-cx" style="left:80px;top:50px;background:#2A303C">A CAIXA · 20% SÃO VERMELHAS</div>
          <div class="tag" id="H-fab" style="left:80px;top:50px;background:#BC002D">FÁBRICA DE MENTIRA</div>
        </div></div>

        <!-- I · O EXPERIMENTO (75,99–90,00): a pá → defeito → o chefe → demitidos → não diminuía -->
        <div class="scene" id="I"><div class="world dark"><div class="band" id="I-band"></div></div>
          <div class="paddle" id="I-pad" style="top:300px">{''.join(holes)}<div id="I-pb">{''.join(pbeads)}</div><div class="h"></div></div>
          <div class="tag" id="I-def" style="left:250px;top:1080px;background:#E5322D;font-size:46px">VERMELHA = DEFEITO</div>
          <div class="sb" id="I-sb" style="top:220px"><div class="hd"><span>PLACAR DO DIA</span><i>BOLINHAS VERMELHAS</i></div>{rows}</div>
          <div class="stamp" data-layout-allow-overlap id="I-st1" style="left:520px;top:626px;font-size:70px">DEMITIDA</div>
          <div class="stamp" data-layout-allow-overlap id="I-st2" style="left:520px;top:402px;font-size:70px">DEMITIDA</div>
        </div>

        <!-- J · CLÍMAX (90,00–92,81): uma em cada cinco -->
        <div class="scene" id="J"><div class="world light"><div class="band" id="J-band"></div></div>
          <div class="title" id="J-title" style="top:280px"><span id="J-w1">1</span> <span id="J-w2">EM</span> <span id="J-w3">CADA</span> <span id="J-w4">5</span></div>
          <div id="J-row" style="position:absolute;left:70px;top:560px;width:940px;height:200px">
            <i class="b" id="J-b1" style="left:0;top:0;width:172px;height:172px"></i><i class="b" id="J-b2" style="left:192px;top:0;width:172px;height:172px"></i>
            <i class="b" id="J-b3" style="left:384px;top:0;width:172px;height:172px"></i><i class="b" id="J-b4" style="left:576px;top:0;width:172px;height:172px"></i>
            <i class="b" id="J-b5" style="left:768px;top:0;width:172px;height:172px"></i>
            <i class="b r" id="J-red" style="left:576px;top:0;width:172px;height:172px;opacity:0"></i>
          </div>
          <div class="ring" id="J-ring1" style="left:732px;top:646px;border-color:#E5322D"></div>
          <div class="ring" id="J-ring2" style="left:732px;top:646px;border-color:#E5322D"></div>
          <div class="tag" id="J-20" style="left:170px;top:880px;background:#E5322D;font-size:48px">20% DE DEFEITO. SEMPRE.</div>
        </div>

        <!-- K · OLHA A CAIXA (94,67–95,86): callback da virada -->
        <div class="scene" id="K"><div class="world dark"><div class="band" id="K-band"></div></div>
          <div class="box" id="K-box" style="left:60px;top:260px;width:960px;height:960px"><div class="in" style="left:40px;top:40px">{beads(12,12,29,66,8)}</div></div>
          <div class="tag" id="K-tag" style="left:200px;top:140px;background:#BC002D;font-size:44px">O PROBLEMA É A CAIXA</div>
        </div>
'''

JS = r'''
          gsap.set(["#A-op", "#A-des",
                    "#B-name", "#B-aula", "#B-tq", "#B-med", "#B-ord", "#B-imp", "#B-prem", "#B-pt", "#B-desde",
                    "#C-chip", "#C-w1", "#C-w2", "#C-w3", "#C-vend", "#C-n3",
                    "#D-l1", "#D-l2", "#D-num",
                    "#E-w1", "#E-w2", "#E-w3", "#E-w4", "#E-mes", "#E-lb", "#E-vs", "#E-toast", "#E-esc", "#E-topo",
                    "#F-w1", "#F-w2", "#F-w3", "#F-poster", "#F-p1", "#F-p2", "#F-p3", "#F-p4", "#F-p5", "#F-cobra",
                    "#G-po", "#G-gaf",
                    "#H-cx", "#H-fab",
                    "#I-pad", "#I-pb", "#I-def", "#I-sb", "#I-m0", "#I-m1", "#I-m3", "#I-m4", "#I-st1", "#I-st2",
                    "#J-w1", "#J-w2", "#J-w3", "#J-w4", "#J-row .b", "#J-20", "#K-tag"], { autoAlpha: 0 });
          gsap.set(["#C-sel", "#E-sel", "#F-sel"], { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set(["#C-sel .h", "#E-sel .h", "#F-sel .h"], { scale: 0 });
          gsap.set("#D-grid i", { scale: 0 });
          gsap.set(".H-b", { scale: 0 });
          gsap.set(["#E-r1", "#E-r2", "#E-r3", "#E-r4", "#E-r5"], { autoAlpha: 0, x: 80 });
          gsap.set("#I-sb .sr", { autoAlpha: 0, x: 80 });
          function sel(base, t) {
            tl.to("#" + base + "-sel", { borderColor: "rgba(242,183,5,1)", backgroundColor: "rgba(242,183,5,.16)", duration: 4 * q, ease: "none" }, Q(t));
            tl.to("#" + base + "-sel .h", { scale: 1, duration: 6 * q, ease: "back.out(3)", stagger: q }, Q(t) + q);
          }

          // ===== A · CAPA (quadro 0 = capa) → SÓ IMAGENS =====
          splitIn("#A", 0, true);
          kenburns("#A-capaimg", 0, 5.9, 1.12, 1.0);
          whip("#A-capa", "#A-op", 5.9);
          kenburns("#A-opimg", 5.9, 8.65, 1.0, 1.1);
          drop("#A-op", "#A-des", 8.62);
          kenburns("#A-desimg", 8.62, 11.37, 1.12, 1.0);
          splitOut("#A", 11.37);

          // ===== B · REVELAÇÃO =====
          sceneIn("#B", 11.37); drift("#B-band", 11.37, 21.68);
          tl.fromTo("#B-dem", { scale: 1.1 }, { scale: 1, duration: 1.9, ease: "power2.out" }, 11.37);
          rise("#B-name", 11.6);
          whip(["#B-dem", "#B-name"], "#B-aula", 13.25);
          tl.fromTo("#B-aula", { scale: 1 }, { scale: 1.04, duration: 2.3, ease: "none" }, Q(13.6));
          pop("#B-tq", 13.9);
          drop(["#B-aula", "#B-tq"], "#B-med", 15.5);
          tl.fromTo("#B-ord", { scale: 0.3, autoAlpha: 0, rotation: -40 }, { scale: 1, autoAlpha: 1, rotation: 0, duration: 12 * q, ease: "back.out(1.8)" }, Q(16.41));
          cue(16.43, "ding", -22);
          rise("#B-imp", 16.6);
          tl.to(["#B-med", "#B-ord", "#B-imp"], { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(17.29) - 5 * q);
          zoomIn("#B-prem", 17.29);
          tl.fromTo("#B-prem", { rotation: -8 }, { rotation: 8, duration: 4.3, ease: "none" }, Q(17.4));
          words(["#B-pt"], [19.68]);
          pop("#B-desde", 20.39);
          sceneOut("#B", 21.68);

          // ===== C · LINHA → PASSO 1 → VENDEDOR =====
          sceneIn("#C", 25.3);
          kenburns("#C-linhaimg", 25.3, 27.6, 1.12, 1.0);
          tl.to("#C-linha", { y: 1900, duration: 5 * q, ease: "power4.in" }, Q(27.55) - 5 * q);
          chip("C", 28.0, 27.5);
          rise("#C-w1", 28.21); rise("#C-w2", 28.86); rise("#C-w3", 29.02); sel("C", 29.4);
          smear("#C-chip", 30.25);
          tl.to("#C-title", { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(30.25) - 5 * q);
          zoomIn("#C-vend", 30.25);
          kenburns("#C-vendimg", 30.25, 34.26, 1.15, 1.0);
          pop("#C-n3", 30.73);
          sceneOut("#C", 34.26);

          // ===== D · 94 DE 100 =====
          sceneIn("#D", 36.72); drift("#D-band", 36.72, 42.33);
          tl.to("#D-grid i", { scale: 1, duration: 8 * q, ease: "back.out(2)", stagger: { each: 0.006, from: "start" } }, Q(37.3));
          cue(37.3, "tique", -24); cue(37.5, "tique", -26); cue(37.7, "tique", -27);
          tl.set("#D-num", { autoAlpha: 1 }, Q(37.48));
          tl.fromTo("#D-d1", { y: 0 }, { y: -9 * 230, duration: 26 * q, ease: "power4.out" }, Q(38.45));
          tl.fromTo("#D-d2", { y: 0 }, { y: -4 * 230, duration: 22 * q, ease: "power4.out" }, Q(38.45));
          cue(38.5, "cacaniquel", -20);
          tl.to(".D-sys", { backgroundColor: "#E5322D", duration: 4 * q, stagger: 0.008 }, Q(38.45));
          tl.to(".D-pes", { backgroundColor: "#FFFFFF", scale: 1.15, duration: 6 * q, ease: "back.out(3)" }, Q(39.4));
          pop("#D-l1", 40.41); pop("#D-l2", 40.9);
          sceneOut("#D", 42.33);

          // ===== E · PASSO 2: RANKING =====
          sceneIn("#E", 45.1); drift("#E-band", 45.1, 55.37);
          chip("E", 45.45, 45.12);
          rise("#E-w1", 45.29); rise("#E-w2", 45.58); rise("#E-w3", 45.83); rise("#E-w4", 45.94); sel("E", 46.4);
          smear("#E-chip", 47.2);
          tl.to("#E-title", { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(47.2) - 5 * q);
          zoomIn("#E-mes", 47.2);
          kenburns("#E-mesimg", 47.2, 51.12, 1.0, 1.12);
          pop("#E-vs", 49.22);
          tl.to(["#E-mes", "#E-vs"], { x: -1400, filter: "blur(18px)", duration: 5 * q, ease: "power4.in" }, Q(51.12) - 5 * q);
          tl.fromTo("#E-lb", { x: 1300, autoAlpha: 1, filter: "blur(18px)" }, { immediateRender: false, x: 0, autoAlpha: 1, filter: "blur(0px)", duration: 13 * q, ease: "expo.out" }, Q(51.12) - q);
          cue(51.07, "whoosh", -14);
          tl.set(["#E-r1", "#E-r2", "#E-r3", "#E-r4", "#E-r5"], { autoAlpha: 1, x: 0 }, Q(51.08));
          tl.to("#E-r1", { scale: 1.05, backgroundColor: "#FFF6D6", duration: 8 * q, ease: "expo.out" }, Q(51.21));
          tl.fromTo("#E-toast", { y: 700, autoAlpha: 1 }, { immediateRender: false, autoAlpha: 1, y: 0, duration: 12 * q, ease: "expo.out" }, Q(52.17));
          cue(52.2, "pop", -19);
          // esconde: o cliente da colega voa para dentro do 1º lugar
          tl.to("#E-toast", { x: 120, y: -880, scale: 0.25, autoAlpha: 0, duration: 12 * q, ease: "power3.in" }, Q(53.19));
          cue(53.5, "swish", -20);
          pop("#E-esc", 53.6);
          tl.to(["#E-r2", "#E-r3", "#E-r4", "#E-r5"], { opacity: 0.3, duration: 8 * q }, Q(53.79));
          pop("#E-topo", 53.79);
          sceneOut("#E", 55.37);

          // ===== F · PASSO 3: CARTAZ =====
          sceneIn("#F", 57.23); drift("#F-band", 57.23, 64.9);
          chip("F", 57.5, 57.25);
          rise("#F-w1", 58.09); rise("#F-w2", 58.53); rise("#F-w3", 58.6); sel("F", 59.0);
          smear("#F-chip", 59.9);
          tl.to("#F-title", { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(59.9) - 5 * q);
          tl.fromTo("#F-poster", { y: -1400, rotation: -6, autoAlpha: 1 }, { immediateRender: false, autoAlpha: 1, y: 0, rotation: -2, duration: 14 * q, ease: "expo.out" }, Q(59.85));
          cue(59.9, "whoosh", -16);
          words(["#F-p1", "#F-p2", "#F-p3", "#F-p4", "#F-p5"], [60.49, 60.97, 61.62, 62.21, 62.73]);
          pop("#F-cobra", 64.24);
          // arranca: o cartaz solta de um canto, gira e cai
          tl.to("#F-poster", { rotation: 14, duration: 6 * q, ease: "power2.in" }, Q(64.24));
          tl.to("#F-poster", { y: 1900, rotation: 32, duration: 10 * q, ease: "power3.in" }, Q(64.44));
          cue(64.3, "reverso", -20);
          sceneOut("#F", 64.9);

          // ===== G · GAFANHOTO =====
          sceneIn("#G", 68.04); drift("#G-band", 68.04, 71.34);
          kenburns("#G-almimg", 68.04, 70.1, 1.14, 1.0);
          whip("#G-alm", "#G-po", 70.06);
          tl.fromTo("#G-po", { scale: 1 }, { scale: 1.04, duration: 1.3, ease: "none" }, Q(70.1));
          rise("#G-gaf", 70.44);
          sceneOut("#G", 71.34);

          // ===== H · SPLIT DA VIRADA: A CAIXA =====
          splitIn("#H", 71.34);
          tl.to(".H-b", { scale: 1, duration: 7 * q, ease: "back.out(2.5)", stagger: { each: 0.008, from: "random" } }, Q(71.97));
          cue(71.97, "tique", -24); cue(72.2, "tique", -26); cue(72.45, "tique", -26); cue(72.7, "tique", -27);
          pop("#H-cx", 72.55);
          tl.to("#H-cx", { autoAlpha: 0, y: -30, duration: 5 * q }, Q(74.1));
          pop("#H-fab", 74.27);
          tl.fromTo("#H-box", { scale: 1 }, { scale: 1.05, duration: 2.0, ease: "sine.inOut" }, Q(73.9));
          splitOut("#H", 75.99);

          // ===== I · O EXPERIMENTO =====
          sceneIn("#I", 75.99); drift("#I-band", 75.99, 87.94);
          tl.fromTo("#I-pad", { y: 900, autoAlpha: 1 }, { immediateRender: false, autoAlpha: 1, y: 0, duration: 13 * q, ease: "expo.out" }, Q(76.21));
          tl.fromTo("#I-pad", { rotation: 0 }, { rotation: -6, duration: 8 * q, ease: "sine.inOut", yoyo: true, repeat: 1 }, Q(77.65));
          cue(76.25, "whoosh", -17);
          tl.fromTo("#I-pb", { y: -60, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 8 * q, ease: "bounce.out" }, Q(78.4));
          cue(78.45, "clique", -20);
          tl.to(".I-wh", { opacity: 0.35, duration: 6 * q }, Q(79.57));
          tl.fromTo(".I-red", { scale: 1 }, { scale: 1.3, duration: 5 * q, ease: "back.out(3)", yoyo: true, repeat: 1 }, Q(79.57));
          pop("#I-def", 79.73);
          // o chefe: placar
          tl.to(["#I-pad", "#I-def"], { y: -1900, duration: 6 * q, ease: "power4.in" }, Q(80.65) - 6 * q);
          tl.set("#I-sb", { autoAlpha: 1 }, Q(80.6));
          stagger("#I-sb .sr", 80.65, 6);
          // elogia quem tirou pouca (EDU 6, ANA 7)
          pop("#I-m4", 82.63); pop("#I-m0", 83.11);
          pop("#I-m3", 84.09); pop("#I-m1", 84.48);
          tl.to(["#I-s3", "#I-s1"], { x: -16, duration: 2 * q, ease: "power2.out", yoyo: true, repeat: 3 }, Q(84.55));
          // demitia os piores: DANI (15) e BIA (12)
          slam("#I-st1", 86.24, -8);
          slam("#I-st2", 86.77, 6);
          tl.to(["#I-s3", "#I-s1", "#I-st1", "#I-st2"], { y: 1900, duration: 6 * q, ease: "power4.in" }, Q(87.4));
          sceneOut("#I", 87.94);

          // ===== J · CLÍMAX: 1 EM 5 =====
          sceneIn("#J", 90.0); drift("#J-band", 90.0, 92.81);
          words(["#J-w1", "#J-w2", "#J-w3", "#J-w4"], [90.02, 90.06, 90.09, 90.43]);
          tl.to("#J-row .b:not(#J-red)", { autoAlpha: 1, scale: 1, duration: 8 * q, ease: "back.out(2.4)", stagger: 2 * q }, Q(90.45));
          for (var j = 0; j < 5; j++) cue(90.47 + j * 2 * q, "pop", -22, { f0: 700 + 100 * j });
          tl.fromTo("#J-red", { autoAlpha: 0, scale: 0.6 }, { autoAlpha: 1, opacity: 1, scale: 1.18, duration: 8 * q, ease: "back.out(3)" }, Q(91.78));
          tl.to(["#J-b1", "#J-b2", "#J-b3", "#J-b5"], { opacity: 0.35, duration: 8 * q }, Q(91.85));
          rings("#J-ring1", "#J-ring2", 91.8);
          rise("#J-20", 92.05);
          sceneOut("#J", 92.81);

          // ===== K · OLHA A CAIXA =====
          sceneIn("#K", 94.67);
          tl.fromTo("#K-box", { scale: 0.92 }, { scale: 1.08, duration: 1.2, ease: "power2.out" }, Q(94.67));
          pop("#K-tag", 94.93);
          sceneOut("#K", 95.86);
'''

T = T.replace('            </style>', CSS + '            </style>', 1)
i = T.index('-->', T.index('CENAS (por video)')) + 3
T = T[:i] + HTML + T[i:]
T = T.replace('          // (vazio = camada transparente)', JS, 1)
open('compositions/mg.html', 'w').write(T)
print('compositions/mg.html', len(T), 'bytes')
```


---

# ARQUIVO: `exemplos/alan-mulally/EDICAO.md`

# EDICAO.md — mapa do projeto (reel Alan Mulally)

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**. Kit v2 (4db7732), 1º reel feito do zero com `novo-projeto.sh`.
**Estado (2026-10-02): EXPORTADO** (`renders/Alan-Mulally-reel-final.mp4`), comando único, sem parada (pedido do usuário).
Duração **103,309 s** · 35 takes · 1 bipe · 96 legendas · 9 callouts · 19 light-leaks · 26 SFX · 22 slots de B-roll.

> **Regra de ouro: nunca editar `index.html` à mão.**
```
editar assets/edit-plan.json (ou scripts/slots.py para B-roll)  ->  node scripts/build-edit.mjs  ->  python3 scripts/bake.py <alvos>  ->  npm run check
```
Python desta máquina: `~/Claude/.venv-reel/bin` (3.12 + mediapipe 0.10.14) na frente do PATH.

## Onde mexer em cada coisa

| Quero mudar… | Arquivo |
|---|---|
| cortes / takes | `scripts/mkcut.py` → `scripts/cuts.py` → `python3 scripts/plan_segments.py` |
| texto de legenda | `scripts/captions_fix_table.py` → `python3 scripts/fix_captions.py` |
| callouts | `impacts` no plano (seg 2 `top` 6, seg 31 `top` 60) |
| B-roll | `scripts/slots.py` → `scripts/entrega.py` → `scripts/make_broll.py` (`ease='out'` novo) → `slots.py --real` |
| legenda baixa sobre B-roll | `capLowSegs` [1, 3, 4, 24, 28, 29, 30, 31] |
| enquadramento do split | `splitShiftY` **469** (olhos medidos em y≈908/1920 nas janelas de split) |
| bipe | `scripts/bipe.py` (49,435–50,005 s do source) |

## Bruto original

`~/Downloads/857F3F29-3490-4046-8493-26C4BAEBA1EA 2.MP4` — **não alterado**. MD5 `ea3ccbeb7a40f5a0ef063091568af7b8`.
HEVC 1440x2560 @60, 152,32 s, **SDR full-range** (`yuvj420p`/`pc`, BT.709), áudio AAC 44,1 kHz.

## Mezanino

full→limited (`mezanino.sh`). Bruto × mezanino (15/76/137 s): 129,59/128,32 · 130,53/129,23 · 130,72/129,43; desvio 70,46→70,41 — não lavou.

## Transcrição

33 regiões → whisper large-v3 por região → `mkcut.py` divide em 6,44 · 12,55 · 15,18 · 22,83 · 25,88 · 27,19 · 30,75 · 41,44 · 61,13 ·
71,20 · 78,72 · 82,52 · 97,83 · 107,49 → 35 chunks. Passe por chunk mantido, vazamentos de borda apagados com DROP; ch33 com o
passe cru (o `align.py` jogou "gerente" 3 s para frente) + FIXT do "Seu" no início da fala (140,44).
Áudio ≠ roteiro (vale o áudio): "proíbe A piada", "dezessete bilhões" (sem "de dólares"), "um novo carro", "Na reunião SOBRE o primeiro
vermelho" (3 passes, inclusive com `--prompt` "sobe"), "O Alan bate palma E PERGUNTA". Grafia do roteiro: "pra", "pro", "Seu gerente", "com carro".

**O bruto não tem estas frases do roteiro** (não gravadas — nada a cortar ou recuperar): "Antes, era o engenheiro-chefe do Boeing 777. E em
quatro anos… a mais lucrativa do mundo." · "Na sua empresa: o vendedor sabe no dia dez… no dia trinta." · "Não tô falando de você… meu
amiguinho." · "Ele parou a reunião e perguntou… Todo mundo olhou pro chão." · "Todo mundo achou que iam entrar dois seguranças…" ·
"E o Mark? Anos depois, virou o CEO da Ford."

## Takes descartados (mantido sempre o ÚLTIMO)

r00 fim "Alan nunca tinha trabalho…" → r01 · r02 fim "Primeiro, aceita" → r03 · r05 "…quando dá merda." → r06 · r07/r08 "Segundo,…" → r09 ·
r12 → r13 · r14 fim "E a virada foi uma pal…" → r15 · r17 fim "Aí o Mark…" · r18 (igual ao r19) → r19 · r21 "Boa sorte!" → r22.
CTA r30–r32 = um take só.

## J-cut

34 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9–5,4 quadros · respiro mediano 0,245 s.

## Bipe

"…quando a M**** já tá feita": nasal /m/ 49,44 · "er" · /d/ 49,82–49,87 · "a" até 50,00 · /ʒ/ de "já" em 50,02. Bipe **49,435–50,005**.
Timeline 35,30–35,82: 100% da energia em 950–1050 Hz, 0% fora de 900–1100 Hz. Apresentador em tela cheia no bipe. Legenda `M****`.

## Varredura de olhar

`gaze_tl` 52 janelas/23,7 s → `gaze_pose` 22/5,7 s. Recorte do `gaze_review` corta a testa neste bruto: folhas próprias com rosto inteiro
(`work/gzsheet.py` → `gaze/me/g*.jpg`, 62 janelas). Nítidas: 36,2–37,1 · 66,3–66,8 · 68,1–68,5 · 77,0–77,2 · 86,4–86,7 — todas cobertas por
B-roll. 2ª passada nos quadros da composição (`snapshots/g2/`): olhando para a lente. **Leitura exposta: 0 s** (piscadela expressiva de
~0,2 s em 83,0 s, "foi um prazer te conhecer", não é leitura).

## Marca só depois do áudio

1ª vez que o áudio diz "Alan": **13,16 s**. s01–s04 sem Mulally/Ford/GM. Revelação (s05) em **13,23 s**.

## Capa / imagem gerada a pedido

Codex `gpt-5.6-sol` (o `gpt-6.1-sol` do config é recusado no login ChatGPT): diretoria à noite, telão todo verde, executivos olhando para a
mesa (`work/conceito/capa-diretoria-verde.png`, 1536x1024). Reusada no s16 (a virada "Tudo verde") como callback.

## B-roll

`PESQUISAS-BROLL-ALAN-MULALLY.md`. Busca por Bing Imagens (`scripts/bimg.py`, sem chave Serper nesta máquina) + Wikimedia.
s02 e s20 trocados depois do QC (westend61 e stockcake são bancos de imagem) por Wikimedia CC0 / domínio público.

## Lições para o kit

- `bimg.py`: busca de imagens sem chave (Bing) no mesmo formato do `gimg.mjs`; `work/pesq/s.sh` aponta para ele.
- `make_broll.py`: `ease='out'` (1-(1-p)^2,2) — câmera chega depois do leak e assenta (lei 1 da skill showreel-interface).
- `filt.py` não barra westend61 e stockcake: acrescentar à lista de bancos.
- `align.py` pode deslocar palavras em chunk cuja 1ª palavra tem duração zero ("Faz[500-500]"): conferir `tl.py --words`.
- Codex como gerador da imagem a pedido: `codex exec -m gpt-5.6-sol …` (~70 s, sai 1536x1024 em paisagem).


---

# ARQUIVO: `exemplos/alan-mulally/mg.html`

```html
<!doctype html>
<html>
  <head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>
        /* Camada de motion graphics do reel Alan Mulally (skill showreel-interface).
           Geometria 1080x1920 (dentro do #stage do host). Transparente fora das cenas.
           Faixa das legendas (76% = y~1460) fica livre: o conteúdo mora entre y 140 e 1340. */
        #mg { position: absolute; inset: 0; overflow: hidden; pointer-events: none; font-family: "Montserrat", sans-serif; }
        #mg .scene { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; visibility: hidden; opacity: 0; overflow: hidden; }
        #mg .world { position: absolute; inset: 0; }
        #mg .dark { background: radial-gradient(130% 80% at 50% 28%, #1B2130 0%, #0C0F15 68%); }
        #mg .light { background: radial-gradient(130% 80% at 50% 28%, #FFFFFF 0%, #E8E6E1 78%); }
        #mg .band { position: absolute; left: -400px; top: 520px; width: 1900px; height: 520px; border-radius: 260px; transform: rotate(-14deg); }
        #mg .dark .band { background: rgba(255,255,255,.035); }
        #mg .light .band { background: rgba(0,0,0,.03); }
        #mg .card { position: absolute; border-radius: 44px; overflow: hidden; box-shadow: 0 34px 90px rgba(0,0,0,.45), 0 6px 18px rgba(0,0,0,.25); background: #222; }
        #mg .card img { width: 100%; height: 100%; object-fit: cover; display: block; }
        #mg .full { position: absolute; inset: 0; overflow: hidden; }
        #mg .full img { width: 100%; height: 100%; object-fit: cover; display: block; }
        /* chip de capítulo (status do BPR) */
        #mg .chip { position: absolute; left: 270px; width: 540px; height: 104px; border-radius: 999px; background: #11141A; color: #fff;
                    display: flex; align-items: center; justify-content: center; gap: 24px; box-shadow: 0 18px 44px rgba(0,0,0,.28); }
        #mg .light .chip, #mg .chip.on-light { background: #11141A; }
        #mg .chip .dot { width: 34px; height: 34px; border-radius: 50%; flex: none; }
        #mg .chip .win { height: 104px; overflow: hidden; }
        #mg .chip .roll span { display: block; height: 104px; line-height: 104px; font-weight: 800; font-size: 44px; letter-spacing: .06em; }
        #mg .chip .plus { position: absolute; left: 50%; top: 50%; width: 104px; height: 104px; margin: -52px 0 0 -52px; border-radius: 50%;
                          background: #11141A; color: #fff; font-weight: 600; font-size: 78px; line-height: 98px; text-align: center; }
        /* etiqueta de nome */
        #mg .name { position: absolute; left: 90px; width: 900px; padding: 26px 40px; border-radius: 34px; background: rgba(255,255,255,.96);
                    color: #11141A; box-shadow: 0 20px 50px rgba(0,0,0,.3); }
        #mg .name b { display: block; font-weight: 800; font-size: 58px; letter-spacing: .01em; }
        #mg .name i { display: block; font-style: normal; font-weight: 600; font-size: 30px; letter-spacing: .08em; color: #5A606B; margin-top: 6px; }
        #mg .tag { position: absolute; padding: 18px 34px; border-radius: 999px; font-weight: 800; font-size: 38px; letter-spacing: .06em; color: #fff; }
        /* carimbo */
        #mg .stamp { position: absolute; padding: 8px 40px; border: 12px solid #E5322D; border-radius: 26px; color: #E5322D; background: rgba(255,255,255,.9);
                     font-weight: 800; font-size: 112px; letter-spacing: .04em; }
        /* título palavra a palavra */
        #mg .title { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; font-size: 112px; line-height: 1.04; color: #11141A; }
        #mg .title span { display: inline-block; }
        #mg .sel { position: relative; display: inline-block; padding: 6px 30px 14px; border: 6px solid #F2B705; background: rgba(242,183,5,.16); }
        #mg .sel .h { position: absolute; width: 26px; height: 26px; background: #fff; border: 4px solid #F2B705; border-radius: 5px; }
        #mg .sel .tl { left: -17px; top: -17px; } #mg .sel .tr { right: -17px; top: -17px; } #mg .sel .bl { left: -17px; bottom: -17px; } #mg .sel .br { right: -17px; bottom: -17px; }
        /* toast */
        #mg .toast { position: absolute; left: 90px; width: 900px; padding: 30px 36px; border-radius: 38px; background: #fff; color: #11141A;
                     box-shadow: 0 26px 70px rgba(0,0,0,.35); display: flex; gap: 28px; align-items: center; }
        #mg .toast .ic { width: 92px; height: 92px; border-radius: 26px; background: #F2B705; color: #11141A; font-weight: 800; font-size: 64px; line-height: 92px; text-align: center; flex: none; }
        #mg .toast b { display: block; font-weight: 800; font-size: 34px; letter-spacing: .06em; color: #5A606B; }
        #mg .toast p { margin: 6px 0 0; font-weight: 600; font-size: 46px; }
        /* semáforo */
        #mg .tlight { position: absolute; left: 400px; width: 280px; height: 760px; border-radius: 64px; background: #050608; border: 6px solid #2A303C;
                      box-shadow: 0 40px 90px rgba(0,0,0,.6); }
        #mg .tlight .lamp { position: absolute; left: 40px; width: 188px; height: 188px; border-radius: 50%; background: #1C2029; }
        #mg .tlight .glow { position: absolute; inset: 0; border-radius: 50%; opacity: 0; }
        #mg .week { position: absolute; left: 60px; width: 960px; display: flex; justify-content: space-between; }
        #mg .week span { width: 120px; height: 120px; border-radius: 30px; background: #1C2029; color: #8C93A1; font-weight: 800; font-size: 46px; line-height: 120px; text-align: center; }
        /* quadro de status (BPR) */
        #mg .board { position: absolute; left: 60px; width: 960px; border-radius: 44px; padding: 40px 44px 30px; box-shadow: 0 34px 90px rgba(0,0,0,.28); }
        #mg .board.b-light { background: #fff; }
        #mg .board.b-dark { background: #151A23; border: 2px solid #252C39; }
        #mg .board .hd { display: flex; justify-content: space-between; font-weight: 800; font-size: 34px; letter-spacing: .08em; margin-bottom: 18px; }
        #mg .b-light .hd { color: #11141A; } #mg .b-dark .hd { color: #E9ECF2; }
        #mg .board .hd i { font-style: normal; font-weight: 600; color: #8C93A1; }
        #mg .row { position: relative; height: 112px; display: flex; align-items: center; justify-content: space-between; border-top: 2px solid rgba(128,136,150,.18); }
        #mg .row .g { display: flex; gap: 14px; }
        #mg .row .g i { display: block; height: 22px; border-radius: 11px; }
        #mg .b-light .row .g i { background: #D9DCE2; } #mg .b-dark .row .g i { background: #303746; }
        #mg .pill { position: relative; width: 330px; height: 74px; border-radius: 999px; }
        #mg .pill span { position: absolute; inset: 0; border-radius: 999px; color: #fff; font-weight: 800; font-size: 30px; letter-spacing: .05em;
                         display: flex; align-items: center; justify-content: center; gap: 14px; }
        #mg .pill span::before { content: ""; width: 20px; height: 20px; border-radius: 50%; background: rgba(255,255,255,.9); }
        #mg .p0 { background: #C9CCD2; } #mg .b-dark .p0 { background: #343B49; }
        #mg .pg { background: #1FB45A; } #mg .py { background: #F2B705; color: #11141A !important; } #mg .pr { background: #E5322D; }
        #mg .bars { position: absolute; left: 60px; width: 960px; height: 300px; display: flex; align-items: flex-end; gap: 22px; padding: 0 30px; }
        #mg .bars i { flex: 1; border-radius: 18px 18px 6px 6px; transform-origin: 50% 100%; }
        #mg .rainbow { position: absolute; left: 60px; width: 960px; height: 14px; border-radius: 7px;
                       background: linear-gradient(90deg, #E5322D, #F28C05, #F2B705, #1FB45A, #1E8BE5, #7B3FE4); }
        /* balões */
        #mg .bubble { position: absolute; padding: 22px 38px; border-radius: 40px; background: #fff; color: #11141A; font-weight: 800; font-size: 58px;
                      box-shadow: 0 18px 44px rgba(0,0,0,.3); }
        #mg .bubble.me { background: #1FB45A; color: #fff; }
        #mg .strike { position: absolute; height: 14px; border-radius: 7px; background: #E5322D; transform-origin: 0 50%; }
        #mg .ring { position: absolute; width: 300px; height: 300px; margin: -150px 0 0 -150px; border-radius: 50%; border: 10px solid #fff; opacity: 0; }
        /* split: prejuízo */
        #mg .panel { position: absolute; left: 0; top: 0; width: 1080px; height: 845px; background: radial-gradient(120% 90% at 50% 20%, #2A1416 0%, #0E0B0D 70%); overflow: hidden; }
        #mg .lbl { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; font-size: 36px; letter-spacing: .1em; color: #F3B4B0; }
        #mg .money { position: absolute; left: 0; width: 1080px; display: flex; justify-content: center; align-items: center; gap: 10px; color: #FF4A3D; font-weight: 800; }
        #mg .money .cur { font-size: 96px; margin-right: 16px; }
        #mg .money .col { height: 210px; overflow: hidden; }
        #mg .money .col div span { display: block; height: 210px; line-height: 210px; font-size: 220px; text-align: center; width: 140px; }
        #mg .money .suf { font-size: 96px; margin-left: 18px; }
        #mg .dots { position: absolute; display: flex; gap: 18px; padding: 30px 40px; border-radius: 40px; background: #fff; box-shadow: 0 18px 44px rgba(0,0,0,.3); }
        #mg .dots i { width: 26px; height: 26px; border-radius: 50%; background: #8C93A1; display: block; }
      </style>

      <div id="mg" data-composition-id="mg" data-width="1080" data-height="1920">

        <!-- S1 · REVELAÇÃO (13,23–20,75): Alan → logotipo penhorado → GM quebrou -->
        <div class="scene" id="S1"><div class="world dark"><div class="band" id="S1-band"></div></div>
          <div class="card" id="S1-alan" style="left:70px;top:150px;width:940px;height:1060px"><img src="assets/mg/alan.jpg" style="object-position:30% 40%" /></div>
          <div class="name" id="S1-name" style="top:1110px"><b>ALAN MULALLY</b><i>CEO DA FORD · 2006–2014</i></div>
          <div class="card" id="S1-oval" style="left:70px;top:330px;width:940px;height:590px;background:#fff"><img src="assets/mg/oval.jpg" /></div>
          <div class="stamp" id="S1-stamp" style="left:150px;top:520px">PENHORADO</div>
          <div class="tag" id="S1-loan" style="left:150px;top:1010px;background:#1C3F94">2006 · GARANTIA DE US$ 23,6 BI</div>
          <div class="card" id="S1-gm" style="left:70px;top:330px;width:940px;height:705px"><img id="S1-gmimg" src="assets/mg/gm.jpg" /></div>
          <div class="tag" id="S1-crise" style="left:330px;top:200px;background:#E5322D">CRISE DE 2008</div>
          <div class="stamp" id="S1-faliu" style="left:300px;top:560px">FALIU</div>
        </div>

        <!-- S2 · PASSO 1 (24,87–31,62): chip → ACEITA PROBLEMA SEM SOLUÇÃO → sede da Ford + toast -->
        <div class="scene" id="S2"><div class="world light"><div class="band" id="S2-band"></div></div>
          <div class="chip" id="S2-chip" style="top:330px"><span class="dot" style="background:#F2B705"></span><div class="win"><div class="roll" id="S2-roll"><span>PASSO 3</span><span>PASSO 2</span><span>PASSO 1</span></div></div><div class="plus" id="S2-plus">+</div></div>
          <div class="title" id="S2-title" style="top:560px"><span id="S2-w1">ACEITA</span><br /><span id="S2-w2">PROBLEMA</span><br /><span class="sel" id="S2-sel"><span id="S2-w3">SEM</span> <span id="S2-w4">SOLUÇÃO.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="card" id="S2-hq" style="left:70px;top:250px;width:940px;height:646px"><img src="assets/mg/fordhq.jpg" /></div>
          <div class="toast" id="S2-toast" style="top:960px"><div class="ic">!</div><div><b>PARA: CHEFE</b><p id="S2-msg">“Temos um problema…”</p></div></div>
          <div class="tag" id="S2-nao" style="left:250px;top:1180px;background:#E5322D">✕ SEM SOLUÇÃO? NÃO TRAZ.</div>
        </div>

        <!-- S3 · PASSO 2 (36,20–40,61): + → chip → semáforo → toda semana -->
        <div class="scene" id="S3"><div class="world dark"><div class="band" id="S3-band"></div></div>
          <div class="chip" id="S3-chip" style="top:170px;background:#fff;color:#11141A"><span class="dot" style="background:#1FB45A"></span><div class="win"><div class="roll" id="S3-roll"><span>PASSO 1</span><span>PASSO 3</span><span>PASSO 2</span></div></div><div class="plus" id="S3-plus" style="background:#fff;color:#11141A">+</div></div>
          <div class="tlight" id="S3-tl" style="top:330px">
            <div class="lamp" style="top:44px"><div class="glow" id="S3-r" style="background:radial-gradient(circle,#FF6B5E 0%,#E5322D 60%);box-shadow:0 0 70px 18px rgba(229,50,45,.7)"></div></div>
            <div class="lamp" style="top:280px"><div class="glow" id="S3-y" style="background:radial-gradient(circle,#FFE07A 0%,#F2B705 60%);box-shadow:0 0 70px 18px rgba(242,183,5,.7)"></div></div>
            <div class="lamp" style="top:516px"><div class="glow" id="S3-g" style="background:radial-gradient(circle,#7DF0A6 0%,#1FB45A 60%);box-shadow:0 0 70px 18px rgba(31,180,90,.7)"></div></div>
          </div>
          <div class="week" id="S3-week" style="top:1150px"><span>S</span><span>T</span><span id="S3-day">Q</span><span>Q</span><span>S</span><span>S</span><span>D</span></div>
        </div>

        <!-- S4 · O QUADRO (45,13–52,11): verde / amarelo / vermelho -->
        <div class="scene" id="S4"><div class="world light"><div class="band" id="S4-band"></div></div>
          <div class="board b-light" id="S4-board" style="top:300px">
            <div class="hd"><span>REVISÃO SEMANAL</span><i>QUINTA · 8H</i></div>
            <div class="row" id="S4-r1"><div class="g"><i style="width:210px"></i><i style="width:120px"></i></div><div class="pill p0"><span class="pg" id="S4-p1" style="opacity:0">NO PLANO</span></div></div>
            <div class="row" id="S4-r2"><div class="g"><i style="width:170px"></i><i style="width:160px"></i></div><div class="pill p0"><span class="py" id="S4-p2" style="opacity:0">TEM SAÍDA</span></div></div>
            <div class="row" id="S4-r3"><div class="g"><i style="width:240px"></i><i style="width:90px"></i></div><div class="pill p0"><span class="pr" id="S4-p3" style="opacity:0">NINGUÉM SABE</span></div></div>
            <div class="row" id="S4-r4"><div class="g"><i style="width:150px"></i><i style="width:190px"></i></div><div class="pill p0"></div></div>
            <div class="row" id="S4-r5"><div class="g"><i style="width:200px"></i><i style="width:110px"></i></div><div class="pill p0"></div></div>
          </div>
        </div>

        <!-- S5 · PASSO 3 (56,03–59,34): chip → PROÍBE PIADA → balão riscado -->
        <div class="scene" id="S5"><div class="world light"><div class="band" id="S5-band"></div></div>
          <div class="chip" id="S5-chip" style="top:300px"><span class="dot" style="background:#E5322D"></span><div class="win"><div class="roll" id="S5-roll"><span>PASSO 2</span><span>PASSO 1</span><span>PASSO 3</span></div></div><div class="plus" id="S5-plus">+</div></div>
          <div class="title" id="S5-title" style="top:540px"><span id="S5-w1">PROÍBE</span><br /><span id="S5-w2">PIADA.</span></div>
          <div class="bubble" id="S5-bub" style="left:300px;top:930px">kkkkkkkkk</div>
          <div class="strike" id="S5-strike" style="left:270px;top:990px;width:540px"></div>
        </div>

        <!-- S6 · ZOOU NA FRENTE DO TIME → PEQUENO GAFANHOTO (63,22–69,78) -->
        <div class="scene" id="S6"><div class="world dark"><div class="band" id="S6-band"></div></div>
          <div class="card" id="S6-zoou" style="left:70px;top:220px;width:940px;height:627px"><img src="assets/mg/zoou.jpg" /></div>
          <div class="bubble" id="S6-b1" style="left:520px;top:900px">kkkkkk</div>
          <div class="bubble" id="S6-b2" style="left:110px;top:1010px">KKKKKKKK</div>
          <div class="bubble" id="S6-b3" style="left:600px;top:1120px">kkk</div>
          <div class="tag" id="S6-visto" style="left:300px;top:150px;background:#11141A;border:3px solid #3A404C">VISTO POR 12</div>
          <div class="card" id="S6-po" style="left:70px;top:260px;width:940px;height:900px"><img src="assets/mg/gafanhoto.jpg" style="object-position:40% 50%" /></div>
          <div class="tag" id="S6-gaf" style="left:190px;top:1190px;background:#F2B705;color:#11141A">PEQUENO GAFANHOTO</div>
        </div>

        <!-- S7 · SPLIT DA VIRADA (72,56–75,95), só a faixa de cima: prejuízo de 17 bi -->
        <div class="scene" id="S7" style="height:845px"><div class="panel" id="S7-panel">
          <div class="lbl" style="top:120px">PREJUÍZO PROJETADO · FORD 2006</div>
          <div class="money" style="top:220px"><span class="cur">US$</span>
            <div class="col"><div id="S7-d1"><span>0</span><span>1</span></div></div>
            <div class="col"><div id="S7-d2"><span>0</span><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span></div></div>
            <span class="suf">BI</span></div>
          <div class="bars" id="S7-bars" style="top:470px;height:300px"><i style="background:#5A2A2C;height:70%"></i><i style="background:#6E2F31;height:55%"></i><i style="background:#8A3434;height:42%"></i><i style="background:#B33A36;height:28%"></i><i style="background:#E5322D;height:12%"></i></div>
        </div></div>

        <!-- S8 · MARK → PRODUÇÃO PARADA (75,95–81,44) -->
        <div class="scene" id="S8"><div class="world dark"><div class="band" id="S8-band"></div></div>
          <div class="card" id="S8-mark" style="left:70px;top:150px;width:940px;height:1060px"><img src="assets/mg/mark.jpg" style="object-position:78% 35%" /></div>
          <div class="name" id="S8-name" style="top:1110px"><b>MARK FIELDS</b><i>DIRETOR · FORD AMÉRICAS</i></div>
          <div class="card" id="S8-edge" style="left:70px;top:260px;width:940px;height:655px"><img src="assets/mg/edge.jpg" /></div>
          <div class="board b-dark" id="S8-row" style="top:960px;padding:10px 34px"><div class="row" style="border-top:0"><div class="g" style="color:#E9ECF2;font-weight:800;font-size:36px;letter-spacing:.06em">CARRO NOVO</div><div class="pill p0" style="width:470px"><span class="pr" id="S8-p" style="opacity:0">PRODUÇÃO PARADA</span></div></div></div>
          <div class="dots" id="S8-dots" style="left:640px;top:1150px"><i id="S8-d1"></i><i id="S8-d2"></i><i id="S8-d3"></i></div>
        </div>

        <!-- S9 · O PRIMEIRO VERMELHO → A PALMA (CLÍMAX) → ARCO-ÍRIS (84,66–94,65) -->
        <div class="scene" id="S9"><div class="world dark"><div class="band" id="S9-band"></div></div>
          <div class="board b-dark" id="S9-board" style="top:250px">
            <div class="hd"><span>REVISÃO SEMANAL</span><i>QUINTA · 8H</i></div>
            <div class="row"><div class="g"><i style="width:210px"></i><i style="width:120px"></i></div><div class="pill pg"><span class="pg">NO PLANO</span><span class="py" id="S9-y1" style="opacity:0">TEM SAÍDA</span></div></div>
            <div class="row"><div class="g"><i style="width:170px"></i><i style="width:160px"></i></div><div class="pill pg"><span class="pg">NO PLANO</span><span class="pr" id="S9-r2" style="opacity:0">VERMELHO</span></div></div>
            <div class="row" id="S9-row3"><div class="g"><i style="width:240px"></i><i style="width:90px"></i></div><div class="pill pg"><span class="pg">NO PLANO</span><span class="pr" id="S9-red" style="opacity:0">VERMELHO</span></div></div>
            <div class="row"><div class="g"><i style="width:150px"></i><i style="width:190px"></i></div><div class="pill pg"><span class="pg">NO PLANO</span><span class="py" id="S9-y4" style="opacity:0">TEM SAÍDA</span></div></div>
            <div class="row"><div class="g"><i style="width:200px"></i><i style="width:110px"></i></div><div class="pill pg"><span class="pg">NO PLANO</span><span class="pr" id="S9-r5" style="opacity:0">VERMELHO</span></div></div>
            <div class="row"><div class="g"><i style="width:120px"></i><i style="width:220px"></i></div><div class="pill pg"><span class="pg">NO PLANO</span><span class="py" id="S9-y6" style="opacity:0">TEM SAÍDA</span></div></div>
          </div>
          <div class="rainbow" id="S9-rainbow" style="top:1078px"></div>
          <div class="bars" id="S9-bars" style="top:1110px;height:230px"><i style="background:#E5322D;height:55%"></i><i style="background:#F28C05;height:80%"></i><i style="background:#F2B705;height:62%"></i><i style="background:#1FB45A;height:95%"></i><i style="background:#1E8BE5;height:72%"></i><i style="background:#7B3FE4;height:86%"></i></div>
          <div class="full" id="S9-palma"><img id="S9-palmaimg" src="assets/mg/alanpalma.jpg" style="object-position:45% 30%" /></div>
          <div class="ring" id="S9-ring1" style="left:540px;top:820px"></div>
          <div class="ring" id="S9-ring2" style="left:540px;top:820px"></div>
        </div>

      </div>

      <script>
        (function () {
          var tl = gsap.timeline({ paused: true });
          var q = 1 / 30;
          function Q(t) { return Math.round(t * 30) / 30; }
          function sceneIn(id, t, from) {
            tl.set(id, { autoAlpha: 1 }, Q(t));
            tl.fromTo(id, { clipPath: from || "inset(14% 9% 14% 9% round 72px)", scale: 0.92 },
              { clipPath: "inset(0% 0% 0% 0% round 0px)", scale: 1, duration: 13 * q, ease: "expo.out" }, Q(t));
          }
          function sceneOut(id, t) {
            tl.to(id, { clipPath: "inset(9% 7% 9% 7% round 72px)", scale: 0.9, duration: 8 * q, ease: "power3.in" }, Q(t) - 12 * q);
            tl.to(id, { y: -2300, duration: 4 * q, ease: "power4.in" }, Q(t) - 4 * q);
            tl.set(id, { autoAlpha: 0 }, Q(t));
          }
          function drift(id, t0, t1) { tl.fromTo(id, { x: -60 }, { x: 60, duration: t1 - t0, ease: "none" }, t0); }
          function pop(id, t, from) { tl.fromTo(id, from || { scale: 0.6, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, x: 0, y: 0, duration: 9 * q, ease: "back.out(2.2)" }, Q(t)); }
          function rise(id, t) { tl.fromTo(id, { y: 70, autoAlpha: 0, filter: "blur(10px)" }, { y: 0, autoAlpha: 1, filter: "blur(0px)", duration: 9 * q, ease: "expo.out" }, Q(t)); }
          function slam(id, t, rot) {
            tl.fromTo(id, { scale: 2.4, autoAlpha: 0, rotation: rot }, { scale: 1, autoAlpha: 1, rotation: rot, duration: 4 * q, ease: "power4.in" }, Q(t) - 4 * q);
            tl.fromTo(id, { scale: 1 }, { scale: 1.04, duration: 3 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(t));
          }
          // chip de capítulo: + → pílula → caça-níquel (T2)
          function chip(base, t, tAp) {
            var R = (540 - 104) / 2;
            tl.set("#" + base + "-chip", { clipPath: "inset(0px " + R + "px 0px " + R + "px round 999px)" }, 0);
            tl.fromTo("#" + base + "-chip", { scale: 0.4, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 7 * q, ease: "back.out(2)" }, tAp != null ? Q(tAp) : Q(t) - 14 * q);
            tl.to("#" + base + "-chip", { clipPath: "inset(0px 0px 0px 0px round 999px)", duration: 8 * q, ease: "power3.out" }, Q(t) - 6 * q);
            tl.to("#" + base + "-plus", { rotation: 45, autoAlpha: 0, duration: 6 * q, ease: "power2.in" }, Q(t) - 6 * q);
            tl.fromTo("#" + base + "-roll", { y: 0, filter: "blur(6px)" }, { y: -208, filter: "blur(0px)", duration: 14 * q, ease: "power4.out" }, Q(t) - 6 * q);
          }
          // estado inicial de tudo que entra (fora da timeline)
          gsap.set(["#S1-name", "#S1-oval", "#S1-stamp", "#S1-loan", "#S1-gm", "#S1-crise", "#S1-faliu",
                    "#S2-w1", "#S2-w2", "#S2-w3", "#S2-w4", "#S2-hq", "#S2-toast", "#S2-nao",
                    "#S3-tl", "#S5-w1", "#S5-w2", "#S5-bub", "#S6-b1", "#S6-b2", "#S6-b3", "#S6-visto", "#S6-po", "#S6-gaf",
                    "#S8-name", "#S8-edge", "#S8-row", "#S8-dots", "#S9-palma", "#S9-rainbow"], { autoAlpha: 0 });
          gsap.set("#S2-sel", { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set("#S2-sel .h", { scale: 0 });
          gsap.set("#S3-week span", { autoAlpha: 0, y: -80 });
          gsap.set("#S5-strike", { scaleX: 0 });
          gsap.set(["#S7-bars i", "#S9-bars i"], { scaleY: 0 });
          gsap.set(["#S4-r1", "#S4-r2", "#S4-r3", "#S4-r4", "#S4-r5"], { autoAlpha: 0, x: 80 });
          gsap.set("#S9-board .row", { autoAlpha: 0, x: 80 });

          // ===== S1 · REVELAÇÃO =====
          sceneIn("#S1", 13.23); drift("#S1-band", 13.23, 20.75);
          tl.fromTo("#S1-alan", { scale: 1.12 }, { scale: 1, duration: 2.3, ease: "power2.out" }, 13.23);
          rise("#S1-name", 13.6);
          // logotipo penhorado: chicote para a esquerda, o oval entra no mesmo vetor
          tl.to(["#S1-alan", "#S1-name"], { x: -1400, filter: "blur(18px)", duration: 5 * q, ease: "power4.in" }, Q(15.67) - 5 * q);
          tl.fromTo("#S1-oval", { x: 1300, autoAlpha: 1, filter: "blur(18px)" }, { immediateRender: false, autoAlpha: 1, x: 0, filter: "blur(0px)", duration: 13 * q, ease: "expo.out" }, Q(15.67) - q);
          slam("#S1-stamp", 16.51, -9);
          rise("#S1-loan", 16.85);
          // crise: o oval cai, a GM entra de cima (mesmo vetor)
          tl.to(["#S1-oval", "#S1-stamp", "#S1-loan"], { y: 1900, duration: 5 * q, ease: "power4.in" }, Q(17.98) - 5 * q);
          tl.fromTo("#S1-gm", { y: -1500, autoAlpha: 1 }, { immediateRender: false, autoAlpha: 1, y: 0, duration: 13 * q, ease: "expo.out" }, Q(17.98) - q);
          pop("#S1-crise", 18.33);
          tl.to("#S1-gmimg", { filter: "grayscale(1) brightness(.62)", duration: 8 * q, ease: "power2.out" }, Q(19.33));
          tl.to("#S1-gm", { rotation: 4, y: 50, duration: 6 * q, ease: "power3.out" }, Q(19.33));
          slam("#S1-faliu", 19.38, 8);
          sceneOut("#S1", 20.75);

          // ===== S2 · PASSO 1 =====
          sceneIn("#S2", 24.87); drift("#S2-band", 24.87, 31.62);
          chip("S2", 25.07);
          rise("#S2-w1", 25.07); rise("#S2-w2", 25.44); rise("#S2-w3", 25.94); rise("#S2-w4", 26.37);
          tl.to("#S2-sel", { borderColor: "rgba(242,183,5,1)", backgroundColor: "rgba(242,183,5,.16)", duration: 4 * q, ease: "none" }, Q(26.75));
          tl.to("#S2-sel .h", { scale: 1, duration: 6 * q, ease: "back.out(3)", stagger: q }, Q(26.8));
          // chip estica e vira risco → corte para a sede (T7)
          tl.to("#S2-chip", { scaleX: 1.3, duration: q, ease: "power2.in" }, Q(27.79) - 5 * q);
          tl.to("#S2-chip", { scaleX: 9, scaleY: 0.5, filter: "blur(14px)", autoAlpha: 0, duration: 4 * q, ease: "power4.in" }, Q(27.79) - 4 * q);
          tl.to("#S2-title", { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(27.79) - 5 * q);
          tl.fromTo("#S2-hq", { scale: 0.55, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 13 * q, ease: "expo.out" }, Q(27.79) - q);
          tl.fromTo("#S2-hq", { y: 0 }, { y: -30, duration: 3.5, ease: "none" }, Q(28.2));
          tl.fromTo("#S2-toast", { y: -900, autoAlpha: 1 }, { immediateRender: false, autoAlpha: 1, y: 0, duration: 12 * q, ease: "expo.out" }, Q(28.94));
          tl.to("#S2-toast", { x: -24, duration: 2 * q, ease: "power2.out", yoyo: true, repeat: 3 }, Q(30.67));
          tl.to("#S2-msg", { opacity: 0.35, duration: 6 * q }, Q(30.67));
          pop("#S2-nao", 30.67);
          sceneOut("#S2", 31.62);

          // ===== S3 · PASSO 2 =====
          sceneIn("#S3", 36.2); drift("#S3-band", 36.2, 40.61);
          chip("S3", 37.57, 36.4);
          tl.fromTo("#S3-tl", { y: 900, autoAlpha: 1 }, { immediateRender: false, autoAlpha: 1, y: 0, duration: 12 * q, ease: "expo.out" }, Q(38.25));
          tl.to("#S3-r", { opacity: 1, duration: 2 * q }, Q(38.59));
          tl.to("#S3-y", { opacity: 1, duration: 2 * q }, Q(38.75));
          tl.to("#S3-g", { opacity: 1, duration: 2 * q }, Q(38.91));
          tl.to("#S3-week span", { autoAlpha: 1, y: 0, duration: 8 * q, ease: "back.out(2)", stagger: 2 * q }, Q(39.13));
          tl.to("#S3-day", { backgroundColor: "#1FB45A", color: "#FFFFFF", scale: 1.12, duration: 4 * q, ease: "power2.out" }, Q(39.6));
          sceneOut("#S3", 40.61);

          // ===== S4 · O QUADRO =====
          sceneIn("#S4", 45.13); drift("#S4-band", 45.13, 52.11);
          tl.to(["#S4-r1", "#S4-r2", "#S4-r3", "#S4-r4", "#S4-r5"], { autoAlpha: 1, x: 0, duration: 9 * q, ease: "expo.out", stagger: 2 * q }, Q(45.2));
          pop("#S4-p1", 45.61, { scale: 0.5, autoAlpha: 0 });
          pop("#S4-p2", 46.59, { scale: 0.5, autoAlpha: 0 });
          pop("#S4-p3", 49.2, { scale: 0.5, autoAlpha: 0 });
          tl.to(["#S4-r1", "#S4-r2", "#S4-r4", "#S4-r5"], { opacity: 0.3, duration: 8 * q }, Q(50.03));
          tl.to("#S4-r3", { scale: 1.06, duration: 10 * q, ease: "expo.out" }, Q(50.03));
          tl.fromTo("#S4-board", { scale: 1 }, { scale: 1.05, duration: 2, ease: "sine.inOut" }, Q(50.03));
          sceneOut("#S4", 52.11);

          // ===== S5 · PASSO 3 =====
          sceneIn("#S5", 56.03); drift("#S5-band", 56.03, 59.34);
          chip("S5", 56.5, 56.1);
          rise("#S5-w1", 57.14); rise("#S5-w2", 57.54);
          pop("#S5-bub", 58.1);
          tl.to("#S5-strike", { scaleX: 1, duration: 5 * q, ease: "power4.out" }, Q(58.7));
          tl.to("#S5-bub", { opacity: 0.4, rotation: -4, duration: 6 * q }, Q(58.7));
          sceneOut("#S5", 59.34);

          // ===== S6 · ZOOU → GAFANHOTO =====
          sceneIn("#S6", 63.22); drift("#S6-band", 63.22, 69.78);
          tl.fromTo("#S6-zoou", { scale: 1.08 }, { scale: 1, duration: 3, ease: "power2.out" }, 63.22);
          pop("#S6-b1", 64.91, { scale: 0.4, autoAlpha: 0, y: 40 });
          pop("#S6-b2", 65.18, { scale: 0.4, autoAlpha: 0, y: 40 });
          pop("#S6-b3", 65.45, { scale: 0.4, autoAlpha: 0, y: 40 });
          pop("#S6-visto", 65.63);
          tl.to(["#S6-zoou", "#S6-b1", "#S6-b2", "#S6-b3", "#S6-visto"], { x: -1400, filter: "blur(18px)", duration: 5 * q, ease: "power4.in" }, Q(66.99) - 5 * q);
          tl.fromTo("#S6-po", { x: 1300, autoAlpha: 1, filter: "blur(18px)" }, { immediateRender: false, autoAlpha: 1, x: 0, filter: "blur(0px)", duration: 13 * q, ease: "expo.out" }, Q(66.99) - q);
          tl.fromTo("#S6-po", { scale: 1 }, { scale: 1.04, duration: 2.6, ease: "none" }, Q(67.4));
          rise("#S6-gaf", 68.82);
          sceneOut("#S6", 69.78);

          // ===== S7 · SPLIT: 17 BILHÕES (faixa de cima) =====
          tl.set("#S7", { autoAlpha: 1 }, Q(72.56));
          tl.fromTo("#S7-panel", { x: 1100, filter: "blur(16px)" }, { immediateRender: false, x: 0, filter: "blur(0px)", duration: 6 * q, ease: "power4.out" }, Q(72.56) - 2 * q);
          tl.fromTo("#S7-d1", { y: 0 }, { y: -210, duration: 10 * q, ease: "power4.out" }, Q(73.6));
          tl.fromTo("#S7-d2", { y: 0, filter: "blur(4px)" }, { y: -7 * 210, filter: "blur(0px)", duration: 26 * q, ease: "power4.out" }, Q(73.6));
          tl.to("#S7-bars i", { scaleY: 1, duration: 9 * q, ease: "expo.out", stagger: 2 * q }, Q(74.5));
          tl.to("#S7", { y: -845, duration: 0.55, ease: "power3.inOut" }, Q(75.95 - 0.55));
          tl.set("#S7", { autoAlpha: 0 }, Q(75.95));

          // ===== S8 · MARK → PRODUÇÃO PARADA =====
          sceneIn("#S8", 75.95); drift("#S8-band", 75.95, 81.44);
          tl.fromTo("#S8-mark", { scale: 1.1 }, { scale: 1, duration: 2.4, ease: "power2.out" }, 75.95);
          rise("#S8-name", 76.23);
          tl.to(["#S8-mark", "#S8-name"], { y: -1700, duration: 5 * q, ease: "power4.in" }, Q(78.4) - 5 * q);
          tl.fromTo("#S8-edge", { y: 1500, autoAlpha: 1 }, { immediateRender: false, autoAlpha: 1, y: 0, duration: 13 * q, ease: "expo.out" }, Q(78.4) - q);
          rise("#S8-row", 78.55);
          pop("#S8-p", 78.85, { scale: 0.5, autoAlpha: 0 });
          pop("#S8-dots", 80.52);
          tl.fromTo(["#S8-d1", "#S8-d2", "#S8-d3"], { y: 0 }, { y: -12, duration: 6 * q, ease: "sine.inOut", yoyo: true, repeat: 3, stagger: 3 * q }, Q(80.6));
          sceneOut("#S8", 81.44);

          // ===== S9 · PRIMEIRO VERMELHO → PALMA → ARCO-ÍRIS =====
          sceneIn("#S9", 84.66); drift("#S9-band", 84.66, 94.65);
          tl.to("#S9-board .row", { autoAlpha: 1, x: 0, duration: 9 * q, ease: "expo.out", stagger: 2 * q }, Q(84.72));
          pop("#S9-red", 86.06, { scale: 0.5, autoAlpha: 0 });
          tl.to("#S9-row3", { scale: 1.06, duration: 10 * q, ease: "expo.out" }, Q(86.06));
          // silêncio: todo o resto apaga, a câmera aproxima devagar
          tl.to("#S9-board .row:not(#S9-row3)", { opacity: 0.22, duration: 12 * q }, Q(86.88));
          tl.fromTo("#S9-board", { scale: 1 }, { scale: 1.08, duration: 1.24, ease: "sine.inOut" }, Q(86.88));
          // CLÍMAX: corte seco para o Alan; a palma solta dois anéis
          tl.set("#S9-palma", { autoAlpha: 1 }, Q(88.12));
          tl.fromTo("#S9-palmaimg", { scale: 1.16 }, { immediateRender: false, scale: 1, duration: 1.4, ease: "expo.out" }, Q(88.12));
          tl.fromTo("#S9-ring1", { scale: 0.2, opacity: 0.9 }, { immediateRender: false, scale: 3.2, opacity: 0, duration: 14 * q, ease: "expo.out" }, Q(88.29));
          tl.fromTo("#S9-ring2", { scale: 0.2, opacity: 0.7 }, { immediateRender: false, scale: 2.4, opacity: 0, duration: 14 * q, ease: "expo.out" }, Q(88.29) + 3 * q);
          // semanas depois: o Alan vira card e sai pela esquerda; o quadro volta (mesmo vetor) em arco-íris
          tl.to("#S9-palma", { scale: 0.62, clipPath: "inset(0% 0% 0% 0% round 60px)", duration: 9 * q, ease: "power3.in" }, Q(91.17) - 9 * q);
          tl.to("#S9-palma", { x: -1300, duration: 4 * q, ease: "power4.in" }, Q(91.17) - 3 * q);
          tl.set("#S9-board .row", { opacity: 1 }, Q(91.17));
          tl.set(["#S9-board", "#S9-row3"], { scale: 1 }, Q(91.17));
          tl.fromTo("#S9-board", { x: 1300 }, { immediateRender: false, x: 0, duration: 12 * q, ease: "expo.out" }, Q(91.17) - q);
          pop("#S9-y1", 91.62, { scale: 0.5, autoAlpha: 0 }); pop("#S9-r2", 91.7, { scale: 0.5, autoAlpha: 0 });
          pop("#S9-y4", 91.78, { scale: 0.5, autoAlpha: 0 }); pop("#S9-r5", 91.86, { scale: 0.5, autoAlpha: 0 });
          pop("#S9-y6", 91.94, { scale: 0.5, autoAlpha: 0 });
          tl.to("#S9-bars i", { scaleY: 1, duration: 10 * q, ease: "expo.out", stagger: 2 * q }, Q(92.25));
          tl.fromTo("#S9-rainbow", { autoAlpha: 1, scaleX: 0, transformOrigin: "0% 50%" }, { immediateRender: false, autoAlpha: 1, scaleX: 1, duration: 12 * q, ease: "power3.out" }, Q(93.16));
          sceneOut("#S9", 94.65);

          window.__timelines["mg"] = tl;
        })();
      </script>
    </template>
  </body>
</html>
```


---

# ARQUIVO: `exemplos/alan-mulally/scripts/mg_sfx.py`

```python
"""SFX da camada de motion graphics (compositions/mg.html) — kit sintetizado da skill showreel-interface
(~/.claude/skills/showreel-interface/scripts/sfx.py). Cada cue marca o PICO do som no quadro do evento visual.
Mistura POR CIMA do bed do formato (trilha + SFX fixos, que continuam todos): rodar SEMPRE depois de `bake.py bed`.
uso: python3 scripts/mg_sfx.py            (le assets/bed.m4a recem-assado, guarda copia em work/bed-base.wav, regrava assets/bed.m4a)"""
import sys, os, json, subprocess, shutil
import numpy as np
sys.path.insert(0, os.path.expanduser('~/.claude/skills/showreel-interface/scripts'))
import sfx as K

SR = K.SR
TOTAL = json.load(open('work/mix-plan.json'))['total']

def tiques(t0, n, passo=2/30, g=-26):
    return [(round(t0 + k * passo, 3), 'tique', g, {}) for k in range(n)]

C = [
 # S1 revelacao
 (13.23, 'whoosh', -17, {}), (13.62, 'pop', -21, {}), (15.62, 'whoosh', -14, {}), (16.51, 'impacto', -18, {'dur': 0.9}),
 (16.51, 'clique', -18, {}), (16.87, 'pop', -23, {}), (17.93, 'whoosh', -15, {}), (18.35, 'pop', -20, {}),
 (19.33, 'impacto', -17, {'dur': 1.2}), (19.33, 'subdrop', -21, {}), (20.5, 'swish', -18, {}),
 # S2 passo 1
 (24.87, 'whoosh', -17, {}), (25.07, 'cacaniquel', -20, {}), *[(t, 'tique', -24, {}) for t in (25.07, 25.44, 25.94, 26.37)],
 (26.8, 'clique', -20, {}), (27.72, 'whoosh', -14, {}), (28.96, 'pop', -18, {}), (28.98, 'ding', -24, {}),
 (30.67, 'clique', -17, {}), (30.67, 'pop', -20, {'f0': 420, 'f1': 160, 'dur': 0.14}), (31.4, 'swish', -18, {}),
 # S3 passo 2
 (36.2, 'whoosh', -17, {}), (36.42, 'pop', -21, {}), (37.57, 'cacaniquel', -20, {}), (38.27, 'swish', -18, {}),
 (38.59, 'clique', -18, {'freq': 2400}), (38.75, 'clique', -18, {'freq': 3000}), (38.91, 'clique', -18, {'freq': 3700}),
 *tiques(39.13, 7, g=-27), (39.6, 'ding', -20, {}), (40.4, 'swish', -18, {}),
 # S4 o quadro
 (45.13, 'whoosh', -17, {}), *tiques(45.2, 5, g=-27), (45.61, 'clique', -18, {}), (45.62, 'ding', -25, {}),
 (46.59, 'clique', -18, {}), (49.2, 'clique', -16, {}), (50.03, 'subdrop', -21, {}), (51.9, 'swish', -18, {}),
 # S5 passo 3
 (56.03, 'whoosh', -17, {}), (56.12, 'pop', -21, {}), (56.5, 'cacaniquel', -20, {}), (57.14, 'tique', -24, {}),
 (57.54, 'tique', -24, {}), (58.12, 'pop', -18, {}), (58.72, 'swish', -17, {}), (59.13, 'swish', -18, {}),
 # S6 zoou -> gafanhoto
 (63.22, 'whoosh', -17, {}), (64.91, 'pop', -18, {'f0': 900}), (65.18, 'pop', -18, {'f0': 1100}), (65.45, 'pop', -18, {'f0': 1300}),
 (65.65, 'clique', -19, {}), (66.94, 'whoosh', -14, {}), (68.84, 'pop', -20, {}), (69.58, 'swish', -18, {}),
 # S7 17 bi (split)
 (72.5, 'whoosh', -15, {}), (73.6, 'cacaniquel', -18, {'dur': 0.85, 'n_tiques': 11}), (74.48, 'impacto', -18, {'dur': 1.2}),
 *tiques(74.5, 5, g=-26),
 # S8 Mark -> producao parada
 (75.95, 'whoosh', -17, {}), (76.25, 'pop', -20, {}), (78.35, 'whoosh', -15, {}), (78.87, 'clique', -16, {}),
 (78.87, 'impacto', -22, {'dur': 0.7}), (80.54, 'pop', -21, {}), (81.24, 'swish', -18, {}),
 # S9 primeiro vermelho -> palma -> arco-iris (88,12: riser + impact do formato ja estao no bed)
 (84.66, 'whoosh', -17, {}), *tiques(84.72, 6, g=-27), (86.06, 'clique', -14, {}), (86.06, 'impacto', -20, {'dur': 0.9}),
 (88.29, 'impacto', -19, {'dur': 0.6}), (88.29, 'swish', -20, {}), (91.1, 'whoosh', -14, {}),
 *tiques(91.62, 5, passo=0.08, g=-24), *[(round(92.25 + k * 2/30, 3), 'pop', -24, {'f0': 700 + 120 * k}) for k in range(6)],
 (93.16, 'ding', -16, {}), (94.45, 'swish', -18, {}),
]

N = int((TOTAL + 1) * SR)
bus = np.zeros((N, 2))
for t, som, g, args in C:
    s, pico = K.SONS[som](**args)
    if s.ndim == 1: s = np.stack([s, s], 1)
    k = int(round(t * SR)) - pico
    i0, j0 = max(0, k), max(0, -k); m = min(len(s) - j0, N - i0)
    if m > 0: bus[i0:i0 + m] += s[j0:j0 + m] * K.db(g)
bus = bus[:int(TOTAL * SR)]

base = 'work/bed-base.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'assets/bed.m4a', '-ar', str(SR), '-ac', '2', base], check=True)
b = K.le_audio(base)
n = min(len(b), len(bus)); out = b[:n] + bus[:n]
pk = np.abs(out).max(); print(f'{len(C)} cues · pico do bed+mg {20*np.log10(pk):.1f} dBFS')
K.grava('work/bed-mg.wav', out)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'work/bed-mg.wav', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', 'assets/bed.m4a'], check=True)
json.dump([dict(t=t, som=s, ganho=g, args=a) for t, s, g, a in C], open('work/mg-cues.json', 'w'), indent=0)
print('assets/bed.m4a = bed do formato + SFX do motion')
```


---

# ARQUIVO: `exemplos/alan-mulally/scripts/slots.py`

```python
"""POR VIDEO — reel ALAN MULALLY. Mapa dos slots de B-roll em tempo ABSOLUTO de timeline (rate 1.1, timeline 103,309 s).
Converte cada janela [t0, t1] em fromSeg/toSeg/span (contrato do build-edit.mjs) e grava
assets/broll-slots.json. Com --placeholders, gera cartoes rotulados em assets/broll/_ph/ e
escreve o plan.broll apontando para eles (so para ver a estrutura no preview).
Com --real, escreve o plan.broll apontando para assets/broll/<arquivo final>.
Layout desenhado a mao sobre as leituras NITIDAS conferidas nas folhas gaze/me/g*.jpg (36,2-37,1 · 66,3-66,8 · 68,1-68,5 ·
77,0-77,2 · 86,4-86,7): capa em split 0-3,40; pre-revelacao ate "Alan" (13,16 s) -> revelacao em 13,23; apresentador no bipe
(31,62-36,20; bipe 35,30-35,82); split 2 (a virada) 69,78-75,95; climax 88,12 ("O Alan bate palma") com riser + impact."""
import json, sys, os, subprocess
P=json.load(open('assets/edit-plan.json')); R=P['rate']; F=1/30
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(P.get('jcutLeadFrames',5)*F,sd-10*F); d=round(sd-lead,3)
    segs.append((round(t,3),round(t+d,3))); t=round(t+d,3)
TOTAL=t
# (id, modo, t0, t1, fala, tema, cobre)
S=[
 # --- INTRO EM SPLIT (PRE-REVELACAO: nada de Alan Mulally, Ford, Boeing ou GM antes de "Alan", 13,16 s) ---
 ("s01","split", 0.00,  3.40,"Esse cara é um dos CEOs mais sorridentes e mais implacáveis","CAPA (imagem gerada a pedido, Codex): diretoria à noite, telão todo verde, executivos olhando para a mesa","— (quadro 0 = capa)"),
 ("s02","full",  3.40,  6.90,"…dos Estados Unidos. E ele criou um protocolo polêmico","PRÉ-REVELAÇÃO: arranha-céus americanos / bandeira dos EUA (sem marca)","—"),
 ("s03","split", 6.90, 10.40,"pra provar que “não me traz problema, me traz solução”","PRÉ-REVELAÇÃO: chefe cobrando o time numa reunião","—"),
 ("s04","split",10.40, 13.23,"faz seu time esconder tudo de você.","PRÉ-REVELAÇÃO: funcionário escondendo papel / cochicho (callout de digitação)","—"),
 # --- CORPO ---
 ("s05","full", 13.23, 15.67,"Alan nunca tinha trabalhado com carro,","REVELAÇÃO: Alan Mulally sorrindo diante do logo da Ford","—"),
 ("s06","full", 15.67, 17.98,"penhorou até o logotipo da Ford.","o oval azul da Ford na sede","—"),
 ("s07","full", 17.98, 20.75,"E na crise de 2008 a GM quebrou.","sede da GM (Renaissance Center, Detroit)","—"),
 ("s08","full", 24.87, 27.79,"Primeiro, aceita problema sem solução.","reunião de equipe (problema sobre a mesa)","—"),
 ("s09","full", 27.79, 31.62,"Na Ford, ninguém contava problema pro chefe sem ter a solução.","sede mundial da Ford, Dearborn","—"),
 ("s10","full", 36.20, 40.61,"…meu querido. Segundo, faz o semáforo toda semana.","semáforo","olhadas 36,23–36,67 · 36,87–37,02 s"),
 ("s11","full", 45.13, 48.70,"Verde tá no plano. Amarelo, tem problema, mas tem saída.","relatório de status verde/amarelo/vermelho","—"),
 ("s12","full", 48.70, 52.11,"Vermelho, ninguém sabe resolver ainda.","semáforo no vermelho","—"),
 ("s13","full", 56.03, 59.34,"E terceiro, proíbe a piada com a cara dos outros.","colegas rindo de alguém no escritório","—"),
 ("s14","full", 63.22, 66.99,"Seu gerente trouxe um problema e você zoou ele na frente do time?","gerente constrangido na frente do time","olhada 66,27–66,77 s"),
 ("s15","full", 66.99, 69.78,"O próximo, ele não traz, pequeno gafanhoto.","“pequeno gafanhoto”: série Kung Fu (Mestre Po)","olhada 68,10–68,50 s"),
 # --- SEGUNDO SPLIT (A VIRADA) ---
 ("s16","split",69.78, 72.56,"E a virada foi uma palma. Tudo verde,","reunião semanal de Mulally com a diretoria","—"),
 ("s17","split",72.56, 75.95,"e a empresa ia perder dezessete bilhões.","prejuízo recorde da Ford (gráfico de perdas)","—"),
 ("s18","full", 75.95, 78.40,"Aí o Mark, um diretor,","Mark Fields","olhada 77,00–77,22 s"),
 ("s19","full", 78.40, 81.44,"parou a produção de um novo carro. Um cara do time dele falou:","Ford Edge 2007","—"),
 # --- CLIMAX ---
 ("s20","full", 84.66, 88.12,"Na reunião sobre o primeiro vermelho, silêncio.","diretoria em silêncio","olhada 86,38–86,70 s"),
 ("s21","full", 88.12, 91.17,"O Alan bate palma e pergunta: quem pode ajudar o Mark?","CLÍMAX: Alan Mulally aplaudindo — riser + impact","—"),
 ("s22","full", 91.17, 94.65,"Semanas depois, os gráficos pareciam um arco-íris.","painel de gráficos coloridos","—"),
]
NOMES={"s01":"s01-split-capa-diretoria-verde","s02":"s02-implacaveis-eua","s03":"s03-split-me-traz-solucao","s04":"s04-split-esconder-tudo",
 "s05":"s05-alan-revelacao","s06":"s06-logo-penhorado","s07":"s07-gm-quebrou","s08":"s08-aceita-problema","s09":"s09-ninguem-contava",
 "s10":"s10-semaforo","s11":"s11-verde-amarelo","s12":"s12-vermelho","s13":"s13-proibe-piada","s14":"s14-zoou-gerente",
 "s15":"s15-pequeno-gafanhoto","s16":"s16-split-virada-palma","s17":"s17-split-17-bilhoes","s18":"s18-mark-fields","s19":"s19-ford-edge",
 "s20":"s20-silencio","s21":"s21-climax-palma","s22":"s22-arco-iris"}
def seg_of(x, end=False):
    for i,(a,b) in enumerate(segs):
        if (a<=x<b) if not end else (a<x<=b+1e-6): return i
    return len(segs)-1
slots=[]
for sid,mode,t0,t1,fala,tema,cobre in S:
    f=seg_of(t0); g=seg_of(t1,end=True); w0,w1=segs[f][0],segs[g][1]
    sp=[round((t0-w0)/(w1-w0),5),round((t1-w0)/(w1-w0),5)]
    slots.append(dict(id=sid,file=f"assets/broll/{NOMES[sid]}.mp4",mode=mode,fromSeg=f,toSeg=g,span=sp,
                      t0=t0,t1=t1,dur=round(t1-t0,2),fala=fala,tema=tema,cobre=cobre))
old={x['id']:x for x in json.load(open('assets/broll-slots.json')).get('slots',[])} if os.path.exists('assets/broll-slots.json') else {}
for s in slots:  # preserva campos da pesquisa (img, link, fonte, prompt...) ja gravados
    for k,v in old.get(s['id'],{}).items():
        if k not in s: s[k]=v
json.dump({"total":TOTAL,"slots":slots},open('assets/broll-slots.json','w'),ensure_ascii=False,indent=1)
print(f"{len(slots)} slots · timeline {TOTAL}s")
# slots que viraram motion graphics (compositions/mg.html): ficam no broll-slots.json (tempos de referencia), fora do plan.broll
MG={"s05","s06","s07","s08","s09","s10","s11","s12","s13","s14","s15","s18","s19","s20","s21","s22"}
def plan_broll(path_of):
    return [{k:s[k] for k in ('mode','fromSeg','toSeg','span')}|{"file":path_of(s)} for s in slots if s['id'] not in MG]
if '--placeholders' in sys.argv:
    from PIL import Image, ImageDraw, ImageFont
    os.makedirs('assets/broll/_ph',exist_ok=True)
    try: fnt=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',46); fs=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',30)
    except Exception: fnt=fs=ImageFont.load_default()
    for k,s in enumerate(slots):
        W,H=(720,1280) if s["mode"]=="full" else (720,564)
        im=Image.new('RGB',(W,H),[(38,52,86),(70,44,86),(40,78,70),(86,62,36)][k%4]); d=ImageDraw.Draw(im)
        y=H*0.30 if s['mode']=='full' else 60
        for line in [f"B-ROLL {s['id']}", "aguardando arquivo", NOMES[s['id']]+".mp4", f"{s['dur']:.2f}s"]:
            d.text((W/2,y),line,font=fnt if line.startswith('B-') else fs,fill=(255,255,255),anchor='mm'); y+=70
        png=f"assets/broll/_ph/{s['id']}.png"; im.save(png)
        subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-i',png,'-t',f"{s['dur']+0.2:.2f}",'-r','60','-c:v','libx264','-pix_fmt','yuv420p','-g','30','-crf','30',f"assets/broll/_ph/{s['id']}.mp4"],check=True)
    P['broll']=plan_broll(lambda s:f"assets/broll/_ph/{s['id']}.mp4"); P['_broll']="PLACEHOLDERS (cartoes rotulados) — slots aguardando os B-rolls do usuario. Ver PESQUISAS-BROLL-KAZUO-INAMORI.md."
    json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1); print("plan.broll -> placeholders")
if '--real' in sys.argv:
    P['broll']=plan_broll(lambda s:s['file']); json.dump(P,open('assets/edit-plan.json','w'),ensure_ascii=False,indent=1); print("plan.broll -> arquivos finais")
```


---

# ARQUIVO: `exemplos/alan-mulally/PESQUISAS-BROLL-ALAN-MULALLY.md`

# B-ROLL — Reel Alan Mulally · relatório do que foi usado

Timeline 103,309 s @1,1x · 22 slots · fotos reais (Bing Imagens em tamanho grande — sem chave Serper nesta máquina — e Wikimedia), 
exceto a capa (s01) e o callback da virada (s16), **imagem gerada a pedido** (Codex, `gpt-5.6-sol`). Movimento só de câmera 
(`scripts/make_broll.py`, easing de assentamento), texto e logotipo intactos. **Licenças: as fotos de imprensa/web abaixo são de terceiros — 
pendência para o Fabio decidir antes de publicar.**

## s01 · split · 0.00–3.40 s (3.40 s)
- Fala: “Esse cara é um dos CEOs mais sorridentes e mais implacáveis”
- Tema: CAPA (imagem gerada a pedido, Codex): diretoria à noite, telão todo verde, executivos olhando para a mesa
- Imagem: `C1` — gerada a pedido (Codex), `work/conceito/capa-diretoria-verde.png`
- Movimento: aproximação (zoom 1.00→1.04) — CAPA (gerada a pedido): telao verde acima da caixa do gancho
- Cobre: — (quadro 0 = capa)

## s02 · full · 3.40–6.90 s (3.50 s)
- Fala: “…dos Estados Unidos. E ele criou um protocolo polêmico”
- Tema: PRÉ-REVELAÇÃO: arranha-céus americanos / bandeira dos EUA (sem marca)
- Imagem: `usa1_12` — 1232x821 · [www.westend61.de](https://www.westend61.de/en/photo/GIOF000119/usa-new-york-city-skyscrapers-trees-and-american-flag-at-downtown-manhattan)
- Movimento: aproximação + tilt (zoom 1.02→1.07) — bandeira entre arranha-ceus (tilt para cima)
- Cobre: —

## s03 · split · 6.90–10.40 s (3.50 s)
- Fala: “pra provar que “não me traz problema, me traz solução””
- Tema: PRÉ-REVELAÇÃO: chefe cobrando o time numa reunião
- Imagem: `mock2_5` — 1440x960 · [www.washingtonpost.com](https://www.washingtonpost.com/business/2021/12/09/workplace-bully-advice/)
- Movimento: aproximação (zoom 1.00→1.06) — chefe cobrando o funcionario
- Cobre: —

## s04 · split · 10.40–13.23 s (2.83 s)
- Fala: “faz seu time esconder tudo de você.”
- Tema: PRÉ-REVELAÇÃO: funcionário escondendo papel / cochicho (callout de digitação)
- Imagem: `hide2_29` — 1687x1126 · [markdejesus.com](https://markdejesus.com/confronting-the-bully-in-your-life/fear-of-the-boss/)
- Movimento: aproximação (zoom 1.00→1.08) — homem escondido atras da mesa (callout de digitacao)
- Cobre: —

## s05 · full · 13.23–15.67 s (2.44 s)
- Fala: “Alan nunca tinha trabalhado com carro,”
- Tema: REVELAÇÃO: Alan Mulally sorrindo diante do logo da Ford
- Imagem: `mul1_3` — 1440x959 · [fortune.com](https://fortune.com/tag/alan-mulally/)
- Movimento: afastamento (zoom 1.10→1.00) — REVELACAO: Mulally sorrindo (pull-out)
- Cobre: —

## s06 · full · 15.67–17.98 s (2.31 s)
- Fala: “penhorou até o logotipo da Ford.”
- Tema: o oval azul da Ford na sede
- Imagem: `ova1_8` — 1533x962 · [fity.club](https://fity.club/lists/suggestions/blue-oval-logo/)
- Movimento: aproximação (zoom 1.00→1.07) — oval azul (push-in, logo intacto)
- Cobre: —

## s07 · full · 17.98–20.75 s (2.77 s)
- Fala: “E na crise de 2008 a GM quebrou.”
- Tema: sede da GM (Renaissance Center, Detroit)
- Imagem: `gm1_0` — 2592x1944 · [www.goodfreephotos.com](https://www.goodfreephotos.com/public-domain-images/renaissance-center-the-headquarters-of-general-motors-detroit-michigan.jpg.php)
- Movimento: travelling + tilt (zoom 1.06→1.06) — Renaissance Center (tilt para cima)
- Cobre: —

## s08 · full · 24.87–27.79 s (2.92 s)
- Fala: “Primeiro, aceita problema sem solução.”
- Tema: reunião de equipe (problema sobre a mesa)
- Imagem: `meet1_5` — 2600x1788 · [www.singaporetranscription.com](https://www.singaporetranscription.com/meeting-transcription/business-people-meeting-at-table-in-conference-room/)
- Movimento: travelling + travelling lateral (zoom 1.05→1.05) — reuniao (travelling esq->dir)
- Cobre: —

## s09 · full · 27.79–31.62 s (3.83 s)
- Fala: “Na Ford, ninguém contava problema pro chefe sem ter a solução.”
- Tema: sede mundial da Ford, Dearborn
- Imagem: `fordhq_4` — 2048x1407 · [arabamericannews.com](https://arabamericannews.com/2025/09/19/ford-to-relocate-global-headquarters-to-new-state-of-the-art-campus-in-dearborn/)
- Movimento: aproximação (zoom 1.00→1.07) — sede da Ford (push-in)
- Cobre: —

## s10 · full · 36.20–40.61 s (4.41 s)
- Fala: “…meu querido. Segundo, faz o semáforo toda semana.”
- Tema: semáforo
- Imagem: `sem1_1` — 2000x1333 · [yh.erkaid.de](https://yh.erkaid.de/traffic-light-switching-hacker-creates-device-that-can-turn-traffic-lights-green/)
- Movimento: afastamento (zoom 1.09→1.00) — semaforo (pull-out)
- Cobre: olhadas 36,23–36,67 · 36,87–37,02 s

## s11 · full · 45.13–48.70 s (3.57 s)
- Fala: “Verde tá no plano. Amarelo, tem problema, mas tem saída.”
- Tema: relatório de status verde/amarelo/vermelho
- Imagem: `bpr1_9` — 1024x768 · [templates.rjuuc.edu.np](https://templates.rjuuc.edu.np/en/alan-mulally-business-plan-review-template.html)
- Movimento: aproximação (zoom 1.00→1.06) — slide do BPR (push-in)
- Cobre: —

## s12 · full · 48.70–52.11 s (3.41 s)
- Fala: “Vermelho, ninguém sabe resolver ainda.”
- Tema: semáforo no vermelho
- Imagem: `sem1_3` — 1200x900 · [optraffic.com](https://optraffic.com/blog/temporary-traffic-signals-design-factors/)
- Movimento: aproximação + tilt (zoom 1.00→1.09) — semaforo no vermelho (push-in)
- Cobre: —

## s13 · full · 56.03–59.34 s (3.31 s)
- Fala: “E terceiro, proíbe a piada com a cara dos outros.”
- Tema: colegas rindo de alguém no escritório
- Imagem: `mock2_4` — 1500x1000 · [etactics.com](https://etactics.com/blog/how-to-deal-with-bullying-at-work)
- Movimento: travelling + travelling lateral (zoom 1.05→1.05) — colegas zombando (travelling dir->esq)
- Cobre: —

## s14 · full · 63.22–66.99 s (3.77 s)
- Fala: “Seu gerente trouxe um problema e você zoou ele na frente do time?”
- Tema: gerente constrangido na frente do time
- Imagem: `mock2_9` — 900x600 · [staffsquared.com](https://staffsquared.com/blog/how-to-deal-with-bullying-in-the-workplace/)
- Movimento: aproximação (zoom 1.00→1.07) — zombaria na frente do time (push-in)
- Cobre: olhada 66,27–66,77 s

## s15 · full · 66.99–69.78 s (2.79 s)
- Fala: “O próximo, ele não traz, pequeno gafanhoto.”
- Tema: “pequeno gafanhoto”: série Kung Fu (Mestre Po)
- Imagem: `gafa_6` — 1280x720 · [adarhairstyle.blogspot.com](https://adarhairstyle.blogspot.com/2021/08/kung-fu-master-grasshopper-quotes.html)
- Movimento: aproximação (zoom 1.00→1.05) — Mestre Po (push-in lento)
- Cobre: olhada 68,10–68,50 s

## s16 · split · 69.78–72.56 s (2.78 s)
- Fala: “E a virada foi uma palma. Tudo verde,”
- Tema: reunião semanal de Mulally com a diretoria
- Imagem: `C1` — gerada a pedido (Codex), `work/conceito/capa-diretoria-verde.png`
- Movimento: aproximação (zoom 1.14→1.22) — a mesma diretoria da capa: telao todo verde (callback)
- Cobre: —

## s17 · split · 72.56–75.95 s (3.39 s)
- Fala: “e a empresa ia perder dezessete bilhões.”
- Tema: prejuízo recorde da Ford (gráfico de perdas)
- Imagem: `wall1_1` — 3730x2480 · [fity.club](https://fity.club/lists/suggestions/wall-street-crash-2008/)
- Movimento: travelling + travelling lateral (zoom 1.05→1.05) — operadores em panico (travelling)
- Cobre: —

## s18 · full · 75.95–78.40 s (2.45 s)
- Fala: “Aí o Mark, um diretor,”
- Tema: Mark Fields
- Imagem: `mf1_13` — 3800x2455 · [www.wsj.com](https://www.wsj.com/articles/fords-board-turns-up-heat-on-ceo-1494356089)
- Movimento: aproximação (zoom 1.00→1.06) — Mark Fields (push-in)
- Cobre: olhada 77,00–77,22 s

## s19 · full · 78.40–81.44 s (3.04 s)
- Fala: “parou a produção de um novo carro. Um cara do time dele falou:”
- Tema: Ford Edge 2007
- Imagem: `edge_0` — 3000x2091 · [www.topspeed.com](https://www.topspeed.com/cars/ford/2007-ford-edge/)
- Movimento: travelling + travelling lateral (zoom 1.06→1.06) — Ford Edge (travelling)
- Cobre: —

## s20 · full · 84.66–88.12 s (3.46 s)
- Fala: “Na reunião sobre o primeiro vermelho, silêncio.”
- Tema: diretoria em silêncio
- Imagem: `meet2_16` — 728x408 · [stockcake.com](https://stockcake.com/i/boardroom-executive-meeting_568012_1071644)
- Movimento: aproximação (zoom 1.00→1.04) — diretoria em silencio (push-in lento, linear)
- Cobre: olhada 86,38–86,70 s

## s21 · full · 88.12–91.17 s (3.05 s)
- Fala: “O Alan bate palma e pergunta: quem pode ajudar o Mark?”
- Tema: CLÍMAX: Alan Mulally aplaudindo — riser + impact
- Imagem: `mclap_0` — 1400x1400 · [shows.acast.com](https://shows.acast.com/leadership-and-the-environment/episodes/566-the-ceo-of-ford-and-boeing-alan-mulally-leadership-envir)
- Movimento: afastamento (zoom 1.14→1.00) — CLIMAX: Mulally de bracos abertos (pull-out no impact)
- Cobre: —

## s22 · full · 91.17–94.65 s (3.48 s)
- Fala: “Semanas depois, os gráficos pareciam um arco-íris.”
- Tema: painel de gráficos coloridos
- Imagem: `rain1_2` — 2560x1280 · [animalia-life.club](https://animalia-life.club/qa/pictures/colorful-bar-graphs)
- Movimento: afastamento + tilt (zoom 1.08→1.00) — graficos coloridos (pull-out)
- Cobre: —
