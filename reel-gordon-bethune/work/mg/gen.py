"""POR VIDEO — reel GORDON BETHUNE. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Tempos absolutos de work/tl-words.txt.
Dosagem (docs/05 §24): abertura só com imagem (capa gerada + a cabine de pilotos sem marca; nada da Continental antes de "Gordon", 11,49 s);
no corpo foto real é o padrão (Commons: o 777 "Gordon M. Bethune", a frota de 1994–1996, o hangar de Houston, a tripulação, a cabine);
motion só nos capítulos (PASSO 1/2/3), na frase exata dele, no mecanismo (comissão × calote, comercial × financeiro, o manual, o bônus
antigo × o novo, o ranking de pontualidade) e na pergunta do fim. O valor do bônus NÃO aparece na tela: o áudio diz "setenta e cinco",
o fato é US$ 65 (avisado na entrega).
Fotos: Wikimedia Commons (licenças em LICENCAS-FOTOS.txt). A capa é gerada a pedido (Codex).
uso: python3 work/mg/gen.py"""
import sys
sys.path.insert(0, 'work/mg')
from parts import CSS
T = open('work/mg/template.html').read()

F = dict(  # foto por papel (assets/mg/, preparadas por work/mg/fotos.py)
    capa='capa-gordon.jpg', fogo='capa-fogo.jpg', cab2='cabine-767-b.jpg', b777='gordon-777.jpg', b727='continental-727-1994.jpg',
    b737='continental-737-1994.jpg', hangar='hangar-iah.jpg', trip='tripulacao.jpg', a300='a300-miami-1994.jpg', cab='cabine-767.jpg',
    pax='cabine-passageiros.jpg', dc10='dc10-1996.jpg')
OP = dict(  # object-position de cada foto (medido no snapshot)
    capa_split='50% 40%', fogo_split='50% 45%', capa='50% 50%', fogo='64% 50%', cab2='50% 50%', b777='100% 50%', b727='88% 50%', b737='60% 50%',
    hangar='30% 50%', trip='45% 50%', a300='70% 50%', cab='50% 50%', pax='40% 50%', dc10='50% 50%')
def img(k, cls=''):
    return f'<img id="{{id}}" class="{cls}" src="assets/mg/{F[k]}" style="object-position:{OP.get(k, "50% 50%")}" />'
def full(id_, k, cls='', extra='', op=None):
    s = img(k, cls).replace('{id}', id_ + 'img')
    if op: s = s.replace(OP.get(k, '50% 50%'), op)
    return f'<div class="full" id="{id_}">' + s + extra + '</div>'
def fit(id_, k, top, h, cls='', extra=''):  # foto horizontal pequena: inteira na largura sobre ela mesma desfocada (docs/05 §31)
    return (f'<div class="full" id="{id_}"><img class="bgblur" src="assets/mg/{F[k]}" />'
            f'<div class="fitimg" style="top:{top}px;height:{h}px"><img id="{id_}img" class="{cls}" src="assets/mg/{F[k]}" /></div>{extra}</div>')
def chip(b, n, dot):
    rolls = {1: ('PASSO 3', 'PASSO 2', 'PASSO 1'), 2: ('PASSO 1', 'PASSO 3', 'PASSO 2'), 3: ('PASSO 2', 'PASSO 1', 'PASSO 3')}[n]
    return (f'<div class="chip" id="{b}-chip" style="top:300px;background:#fff;color:#11141A"><span class="dot" style="background:{dot}"></span>'
            f'<div class="win"><div class="roll" id="{b}-roll">' + ''.join(f'<span>{r}</span>' for r in rolls)
            + f'</div></div><div class="plus" id="{b}-plus" style="background:#fff;color:#11141A">+</div></div>')
def title(b, l1, l2, color='#fff'):
    w = l1 + l2; n = len(w)
    sp = [f'<span id="{b}-w{k+1}">{x}</span>' for k, x in enumerate(w)]
    sel = f'<span class="sel" id="{b}-sel">{sp[-1]}<i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span>'
    return (f'<div class="title" id="{b}-title" style="top:520px;color:{color}">' + ' '.join(sp[:len(l1)]) + '<br />'
            + ' '.join(sp[len(l1):n - 1] + [sel]) + '</div>')
def pill2(base, a, acls, b, bcls):  # pilula com dois estados sobrepostos (flip troca a de cima)
    return f'<div class="pill"><span class="{acls}" id="{base}a">{a}</span><span class="{bcls}" id="{base}b">{b}</span></div>'
# ranking: 10 linhas (1º..10º); a Continental começa em ÚLTIMA e sobe para dentro do TOP 5
RY = [190 + k * 84 for k in range(10)]
RW = [62, 59, 56, 54, 51, 47, 43, 39, 35, 31]
RANK = ''.join(f'<div class="r" style="top:{RY[k]}px"><span class="n">{k+1}º</span><i style="width:{RW[k]}%"></i></div>' for k in range(10))
PPL = [('PILOTO', True), ('COMISSÁRIA', False), ('MECÂNICO', False), ('ATENDENTE', False), ('GERENTE', False)]
PEOPLE = ''.join(f'<div class="pp" id="J-pp{k}"><i class="g"></i>' + ('<i class="y" id="J-y"></i>' if y else '') + f'<i class="on" id="J-p{k}"></i><b>{nm}</b></div>'
                 for k, (nm, y) in enumerate(PPL))

HTML = f'''
        <!-- A · SPLIT DA CAPA (0–5,55, o gancho inteiro): CAPA GERADA A PEDIDO (Codex: o manual pegando fogo no estacionamento, homem de terno de costas)
             → em "e mais amados" o detalhe do manual queimando. Nada da Continental. -->
        <div class="scene" id="A" style="height:845px"><div class="world dark"></div>{full('A-capa', 'capa', op=OP['capa_split'])}
          {full('A-fogo', 'fogo', op=OP['fogo_split'])}</div>

        <!-- P · PRÉ-REVELAÇÃO (5,55–10,20): os pilotos de costas na cabine (sem marca) → a capa abre em tela cheia — nada do Gordon nem da Continental -->
        <div class="scene" id="P"><div class="world dark"></div>
          {fit('P-cab', 'cab2', 420, 810)}
          {full('P-capa', 'capa')}
        </div>

        <!-- B · REVELAÇÃO (11,56–18,71): o 777 batizado "Gordon M. Bethune" + nome → Miami, 1994 (A PIOR DO PAÍS) → FALÊNCIA 1983 / 1990 → o manual pegando fogo -->
        <div class="scene" id="B"><div class="world dark"></div>
          {full('B-777', 'b777', '', '<div class="mark" id="B-ring" style="left:478px;top:684px"></div>')}
          <div class="name" id="B-name" style="top:1090px"><b>GORDON BETHUNE</b><i>CEO · CONTINENTAL AIRLINES · 1994–2004</i></div>
          {fit('B-727', 'b727', 300, 721)}
          <div class="tag" id="B-pior" style="left:90px;top:1080px;background:#11141A">MIAMI, 1994 · A PIOR DO PAÍS</div>
          <div class="stamp" data-layout-allow-overlap id="B-f1" style="left:110px;top:560px;font-size:92px">FALÊNCIA 1983</div>
          <div class="stamp" data-layout-allow-overlap id="B-f2" style="left:170px;top:800px;font-size:92px">FALÊNCIA 1990</div>
          {full('B-fogo', 'capa', '', '<div class="floor"></div>', op=OP['fogo'])}
        </div>

        <!-- D · PASSO 1 (23,24–34,45): chip + título → a frase dele sobre a frota de 1994 → comissão por venda fechada × o cliente que não paga -->
        <div class="scene" id="D"><div class="world dark"><div class="band" id="D-band"></div></div>
          {chip('D', 1, '#1FB45A')}
          {title('D', ['PREMIA', 'O', 'QUE'], ['IMPORTA.'])}
          <div class="tag" id="D-cli" style="left:330px;top:790px;background:#1FB45A">PRO CLIENTE</div>
          <div class="full" id="D-quo">{img('b737', 'dark2').replace('{id}', 'D-quoimg')}<div class="world" style="background:linear-gradient(180deg,rgba(8,10,14,.35),rgba(8,10,14,.75))"></div>
            <div class="qlbl" id="D-ele" style="top:330px">ELE DIZ:</div>
            <div class="quote" style="top:450px"><span id="D-q1">O QUE VOCÊ</span><br /><span id="D-q2" class="y">MEDE</span> <span id="D-q3">E</span> <span id="D-q4" class="y">PREMIA</span><br /><span id="D-q5">É O QUE VOCÊ</span><br /><span id="D-q6" class="y">RECEBE.</span></div>
            <div class="qby" id="D-by" style="top:930px;font-size:28px">GORDON BETHUNE · “FROM WORST TO FIRST”, 1998</div>
          </div>
          <div class="req" id="D-req" style="top:250px">
            <div class="hd">SEU VENDEDOR</div>
            <div class="tt">Comissão: venda fechada</div>
            <div class="cols"><b>COMISSÃO</b><b>O CLIENTE</b></div>
            <div class="it" id="D-i1"><span class="nm">VENDA 1</span>{pill2('D-c1', '—', 'p0', 'PAGA', 'pg')}{pill2('D-k1', '—', 'p0', 'PAGOU', 'pg')}</div>
            <div class="it" id="D-i2"><span class="nm">VENDA 2</span>{pill2('D-c2', '—', 'p0', 'PAGA', 'pg')}{pill2('D-k2', '—', 'p0', 'NÃO PAGOU', 'pr')}</div>
            <div class="it" id="D-i3"><span class="nm">VENDA 3</span>{pill2('D-c3', '—', 'p0', 'PAGA', 'pg')}{pill2('D-k3', '—', 'p0', 'NÃO PAGOU', 'pr')}</div>
          </div>
        </div>

        <!-- F · PASSO 2 (37,47–47,23): chip + título → o hangar da Continental em Houston (O TIME INTEIRO · O MESMO NÚMERO) → COMERCIAL × FINANCEIRO -->
        <div class="scene" id="F"><div class="world dark"><div class="band" id="F-band"></div></div>
          {chip('F', 2, '#F2B705')}
          {title('F', ['TODO', 'MUNDO'], ['GANHA', 'JUNTO.'])}
          {full('F-hang', 'hangar', 'dim', '<div class="vig"></div>')}
          <div class="tag" id="F-time" style="left:90px;top:1080px;background:#11141A">O TIME INTEIRO</div>
          <div class="tag" id="F-num" style="left:90px;top:1180px;background:#1FB45A">O MESMO NÚMERO</div>
          <div class="full" id="F-vs"><div class="world dark"></div>
            <div class="vcard" id="F-com" style="left:70px"><div class="dp">COMERCIAL</div><div class="gp">GANHA POR</div><div class="gv">VENDA</div>
              <div class="ar" id="F-up" style="color:#1FB45A">↑</div></div>
            <div class="vcard" id="F-fin" style="left:560px"><div class="dp">FINANCEIRO</div><div class="gp">GANHA POR</div><div class="gv">CORTE DE CUSTO</div>
              <div class="ar" id="F-dn" style="color:#E5322D">↓</div></div>
            <div class="vs" id="F-x" style="top:600px;font-size:130px">×</div>
          </div>
        </div>

        <!-- H · PASSO 3 (49,17–59,17): chip + título → a tripulação da Continental (O CERTO PRO CLIENTE · E PRA EMPRESA) → o manual riscado → "É POLÍTICA DA EMPRESA." -->
        <div class="scene" id="H"><div class="world dark"><div class="band" id="H-band"></div></div>
          {chip('H', 3, '#E5322D')}
          {title('H', ['QUEIMA', 'O'], ['MANUAL.'])}
          {full('H-trip', 'trip', '', '<div class="floor"></div>')}
          <div class="tag" id="H-cli" style="left:90px;top:1150px;background:#1FB45A">O CERTO PRO CLIENTE</div>
          <div class="tag" id="H-emp" style="left:90px;top:1250px;background:#11141A">E PRA EMPRESA</div>
          <div class="full" id="H-man"><div class="world dark"></div>
            <div class="binder"><div class="lb">MANUAL<i>REGRAS DA EMPRESA</i></div>
              <div class="pg" style="top:330px"></div><div class="pg" style="top:380px;right:110px"></div><div class="pg" style="top:430px"></div><div class="pg" style="top:480px;right:160px"></div><div class="pg" style="top:530px"></div></div>
            <div class="strike" id="H-x" style="left:200px;top:640px;width:680px;transform:rotate(-24deg)"></div>
            <div class="tag" id="H-nao" style="left:300px;top:1100px;background:#E5322D">NÃO O MANUAL</div>
          </div>
          <div class="full" id="H-chat"><div class="world dark"></div>
            <div class="who" id="H-wa" style="left:90px;top:420px"><i style="background:#5A606B">A</i>SEU ATENDENTE</div>
            <div class="dots" id="H-dots" style="left:90px;top:510px"><i></i><i></i><i></i></div>
            <div class="bubble big" id="H-b1" style="left:90px;top:510px;width:820px">É POLÍTICA DA EMPRESA.</div>
          </div>
        </div>

        <!-- L · SPLIT DA VIRADA (61,47–63,99): o A300 da Continental no calor de Miami, 1994 -->
        <div class="scene" id="L" style="height:845px"><div class="world dark"></div>
          {full('L-a300', 'a300', 'warm')}
        </div>

        <!-- N · A VIRADA (63,99–79,91): os pilotos (BÔNUS DO PILOTO) → o painel (AR DESLIGADO, DEVAGAR) → os passageiros (SUADO, ATRASADO)
             → o bônus antigo (só o piloto) × o novo (a nota de dólar, PRA TODO MUNDO; sem o valor) → o ranking de pontualidade (TOP 5 = bônus) -->
        <div class="scene" id="N"><div class="world dark"><div class="band" id="N-band"></div></div>
          {fit('N-cab', 'cab', 360, 719)}
          <div class="tag" id="N-bon" style="left:90px;top:1120px;background:#F2B705;color:#11141A">BÔNUS DO PILOTO</div>
          <div class="tag" id="N-comb" style="left:90px;top:1220px;background:#11141A">PRA ECONOMIZAR COMBUSTÍVEL</div>
          <div class="req" id="N-req" style="top:300px">
            <div class="hd">NA CABINE</div>
            <div class="tt">Pra ganhar o bônus</div>
            <div class="it" id="N-i1"><span class="nm">AR-CONDICIONADO</span>{pill2('N-p1', 'LIGADO', 'pg', 'DESLIGADO', 'pr')}</div>
            <div class="it" id="N-i2"><span class="nm">VELOCIDADE</span>{pill2('N-p2', 'NORMAL', 'pg', 'DEVAGAR', 'pr')}</div>
          </div>
          {full('N-pax', 'pax', '', '<div class="floor"></div>')}
          <div class="tag" id="N-sua" style="left:90px;top:1080px;background:#E5322D">SUADO</div>
          <div class="tag" id="N-atr" style="left:90px;top:1180px;background:#E5322D">E ATRASADO</div>
          <div class="full" id="N-bns"><div class="world dark"></div>
            <div class="lbl2" id="N-old" style="top:200px;font-size:40px;color:#8C93A1">O BÔNUS ANTIGO</div>
            <div class="lbl2" id="N-new" style="top:200px;font-size:40px;color:#1FB45A">O BÔNUS NOVO</div>
            <div class="bill" id="N-bill"></div>
            <div class="lbl2" id="N-todo" style="top:690px;font-size:84px;letter-spacing:.02em;color:#fff">PRA TODO MUNDO</div>
            <div class="ppl" id="N-ppl" style="top:860px">{PEOPLE}</div>
            <div class="tag" id="N-so" style="left:330px;top:1120px;background:#252C39">SÓ O PILOTO</div>
            <div class="strike" id="N-sox" style="left:320px;top:1160px;width:440px"></div>
          </div>
          <div class="full" id="N-rk"><div class="world dark"></div>
            <div class="rank"><div class="hd">RANKING DOS EUA · TODO MÊS</div><div class="tt">Pontualidade</div>
              <div class="top" id="N-top"></div>{RANK}<div class="toplbl" id="N-lbl">TOP 5 = BÔNUS</div>
              <div class="co" id="N-co" style="top:{RY[9] - 2}px">CONTINENTAL</div></div>
          </div>
        </div>

        <!-- C · CLÍMAX (79,91–82,46): um DC-10 da Continental em 1996, inteiro na largura sobre ele mesmo desfocado + 1996 · COMPANHIA AÉREA DO ANO -->
        <div class="scene" id="C"><div class="world dark"></div>
          <div class="full"><img class="bgblur" src="assets/mg/{F['dc10']}" /></div>
          <div class="fitimg" id="C-dc10" style="top:400px"><img id="C-dc10img" src="assets/mg/{F['dc10']}" /></div>
          <div class="tag" id="C-ano" style="left:90px;top:1110px;background:#11141A">UM ANO DEPOIS</div>
          <div class="tag" id="C-melhor" style="left:90px;top:1210px;background:#1FB45A">1996 · COMPANHIA AÉREA DO ANO</div>
        </div>

        <!-- S · "me segue" (89,48): o botão de seguir aparece sobre o apresentador -->
        <div class="scene" id="S"><div class="follow" id="S-btn">Seguir</div></div>

        <!-- Q · A PERGUNTA DO FIM (91,60–fim), por cima do apresentador (nota de gravação: a pergunta escrita na tela nos últimos 5 s) -->
        <div class="scene" id="Q">
          <div class="ask" id="Q-ask"><div class="hd"><i></i>E VOCÊ?</div>
            <p>Qual a <span class="qh" id="Q-h1">regra de comissão</span> mais <span class="qh" id="Q-h2">absurda</span> que você já viu?</p><div class="in">Adicione um comentário…</div></div>
        </div>
'''

JS = r'''
          gsap.set(["#A-fogo", "#P-capa",
                    "#B-ring", "#B-name", "#B-727", "#B-pior", "#B-f1", "#B-f2", "#B-fogo",
                    "#D-chip", "#D-w1", "#D-w2", "#D-w3", "#D-w4", "#D-cli", "#D-quo", "#D-ele", "#D-q1", "#D-q2", "#D-q3", "#D-q4", "#D-q5", "#D-q6", "#D-by",
                    "#D-req", "#D-i1", "#D-i2", "#D-i3", "#D-c1b", "#D-c2b", "#D-c3b", "#D-k1b", "#D-k2b", "#D-k3b",
                    "#F-chip", "#F-w1", "#F-w2", "#F-w3", "#F-w4", "#F-hang", "#F-time", "#F-num", "#F-vs", "#F-com", "#F-fin", "#F-up", "#F-dn", "#F-x",
                    "#H-chip", "#H-w1", "#H-w2", "#H-w3", "#H-trip", "#H-cli", "#H-emp", "#H-man", "#H-x", "#H-nao", "#H-chat", "#H-wa", "#H-dots", "#H-b1",
                    "#N-bon", "#N-comb", "#N-req", "#N-p1b", "#N-p2b", "#N-pax", "#N-sua", "#N-atr", "#N-bns", "#N-old", "#N-new", "#N-bill", "#N-todo", "#N-so", "#N-sox",
                    "#N-rk", "#N-top", "#N-lbl", "#J-p0", "#J-p1", "#J-p2", "#J-p3", "#J-p4",
                    "#C-ano", "#C-melhor", "#Q-ask", "#S-btn"], { autoAlpha: 0 });
          gsap.set(["#D-sel", "#F-sel", "#H-sel"], { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set(["#D-sel .h", "#F-sel .h", "#H-sel .h"], { scale: 0 });
          gsap.set(["#H-x", "#N-sox"], { scaleX: 0 });
          function sel(base, t) {
            tl.to("#" + base + "-sel", { borderColor: "rgba(242,183,5,1)", backgroundColor: "rgba(242,183,5,.16)", duration: 4 * q, ease: "none" }, Q(t));
            tl.to("#" + base + "-sel .h", { scale: 1, duration: 6 * q, ease: "back.out(3)", stagger: q }, Q(t) + q);
          }
          function out(sel_, t) { tl.to(sel_, { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(t) - 5 * q); }
          function cap(b, ts, tSel, tOut, entra) {   // chip + titulo palavra a palavra + selecao, e o titulo sai pelo zoom-through
            chip(b, ts[0], ts[1]);
            for (var k = 2; k < ts.length; k++) rise("#" + b + "-w" + (k - 1), ts[k]);
            sel(b, tSel); smear("#" + b + "-chip", tOut); out("#" + b + "-title", tOut); zoomIn(entra, tOut);
          }

          // ===== A · CAPA (quadro 0 = capa) =====
          splitIn("#A", 0, true);
          kenburns("#A-capaimg", 0, 3.0, 1.0, 1.06);
          // "e mais amados": o detalhe do manual pegando fogo
          whip("#A-capa", "#A-fogo", 3.0);
          kenburns("#A-fogoimg", 3.0, 5.55, 1.0, 1.08);
          splitOut("#A", 5.55);

          // ===== P · PRÉ-REVELAÇÃO (só imagem, nada da Continental) =====
          sceneIn("#P", 5.55);
          kenburns("#P-cabimg", 5.55, 7.84, 1.1, 1.0);
          // "o seu time não faz o que você pede": a capa abre em tela cheia
          whip("#P-cab", "#P-capa", 7.84);
          kenburns("#P-capaimg", 7.84, 10.2, 1.0, 1.08);
          sceneOut("#P", 10.2);

          // ===== B · REVELAÇÃO ("Gordon" 11,49 → 11,56) =====
          sceneIn("#B", 11.56);
          kenburns("#B-777", 11.56, 13.59, 1.0, 1.05);
          rise("#B-name", 11.75);
          tl.fromTo("#B-ring", { scale: 1.8, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 9 * q, ease: "back.out(2)" }, Q(12.1));
          cue(12.12, "pop", -19);
          // "do país": Miami, 1994 — a pior do país
          whip(["#B-777", "#B-name", "#B-ring"], "#B-727", 13.59);
          kenburns("#B-727img", 13.59, 16.32, 1.0, 1.08);
          pop("#B-pior", 13.74);
          // "que já tinha falido duas vezes"
          slam("#B-f1", 14.88, -6);
          slam("#B-f2", 15.58, 4);
          // "E tacou fogo no manual da empresa."
          drop(["#B-727", "#B-pior", "#B-f1", "#B-f2"], "#B-fogo", 16.32);
          kenburns("#B-fogoimg", 16.32, 18.71, 1.12, 1.24);
          sceneOut("#B", 18.71);

          // ===== D · PASSO 1 → A FRASE DELE → COMISSÃO × CALOTE =====
          sceneIn("#D", 23.24); drift("#D-band", 23.24, 34.45);
          chip("D", 23.45, 23.24);
          rise("#D-w1", 23.79); rise("#D-w2", 24.19); rise("#D-w3", 24.29); rise("#D-w4", 24.45);
          sel("D", 24.93);
          pop("#D-cli", 25.21);
          smear("#D-chip", 26.1); out(["#D-title", "#D-cli"], 26.1); zoomIn("#D-quo", 26.1);
          kenburns("#D-quoimg", 26.1, 29.49, 1.0, 1.06);
          pop("#D-ele", 26.13);
          rise("#D-q1", 26.58); rise("#D-q2", 27.06); rise("#D-q3", 27.33); rise("#D-q4", 27.42); rise("#D-q5", 27.93); rise("#D-q6", 28.5);
          cue(27.06, "tique", -22); cue(27.42, "tique", -22); cue(28.5, "tique", -22);
          rise("#D-by", 28.75);
          // "Paga comissão só por venda fechada?"
          drop(["#D-quo"], "#D-req", 29.49);
          stagger(["#D-i1", "#D-i2", "#D-i3"], 29.75, 3, 3);
          flip("#D-c1b", 30.57); flip("#D-c2b", 30.72); flip("#D-c3b", 30.87);
          // "Seu vendedor vende até pra quem não paga."
          flip("#D-k1b", 33.02); flip("#D-k2b", 33.52); flip("#D-k3b", 33.8);
          sceneOut("#D", 34.45);

          // ===== F · PASSO 2 → O HANGAR → COMERCIAL × FINANCEIRO =====
          sceneIn("#F", 37.47); drift("#F-band", 37.47, 47.23);
          cap("F", [37.66, 37.47, 38.11, 38.2, 38.51, 38.92], 39.2, 39.75, "#F-hang");
          kenburns("#F-hangimg", 39.75, 43.36, 1.0, 1.06);
          pop("#F-time", 40.29);
          pop("#F-num", 42.19);
          drop(["#F-hang", "#F-time", "#F-num"], "#F-vs", 43.36);
          pop("#F-com", 43.63);
          pop("#F-up", 44.49, { y: 80, autoAlpha: 0, scale: 0.6 });
          pop("#F-x", 44.84, { scale: 0.3, autoAlpha: 0 }, false);
          pop("#F-fin", 45.0);
          pop("#F-dn", 45.95, { y: -80, autoAlpha: 0, scale: 0.6 });
          tl.to("#F-com", { x: 26, rotation: 3, duration: 3 * q, ease: "power2.out", yoyo: true, repeat: 3 }, Q(46.32));
          tl.to("#F-fin", { x: -26, rotation: -3, duration: 3 * q, ease: "power2.out", yoyo: true, repeat: 3 }, Q(46.32));
          cue(46.34, "impacto", -21, { dur: 0.5 });
          sceneOut("#F", 47.23);

          // ===== H · PASSO 3 → A TRIPULAÇÃO → O MANUAL RISCADO → "É POLÍTICA DA EMPRESA" =====
          sceneIn("#H", 49.17); drift("#H-band", 49.17, 59.17);
          cap("H", [49.35, 49.17, 49.86, 49.98, 50.19], 50.5, 51.14, "#H-trip");
          kenburns("#H-tripimg", 51.14, 55.04, 1.0, 1.06);
          pop("#H-cli", 53.09);
          pop("#H-emp", 53.98);
          // "não o que tá no manual."
          drop(["#H-trip", "#H-cli", "#H-emp"], "#H-man", 55.04);
          tl.to("#H-x", { autoAlpha: 1, scaleX: 1, duration: 6 * q, ease: "power3.out" }, Q(55.7));
          cue(55.72, "swish", -19);
          pop("#H-nao", 55.85);
          // "Seu atendente fala: é política da empresa?"
          whip("#H-man", "#H-chat", 56.33);
          rise("#H-wa", 56.5);
          tl.fromTo("#H-dots", { autoAlpha: 0 }, { autoAlpha: 1, duration: 3 * q }, Q(56.7));
          tl.set("#H-dots", { autoAlpha: 0 }, Q(57.37));
          pop("#H-b1", 57.37, { scale: 0.5, autoAlpha: 0, y: 30 });
          sceneOut("#H", 59.17);

          // ===== L · SPLIT DA VIRADA =====
          splitIn("#L", 61.47);
          kenburns("#L-a300img", 61.47, 63.99, 1.0, 1.08);
          splitOut("#L", 63.99);

          // ===== N · A VIRADA =====
          sceneIn("#N", 63.99); drift("#N-band", 63.99, 79.91);
          kenburns("#N-cabimg", 63.99, 67.35, 1.0, 1.08);
          pop("#N-bon", 64.8);
          pop("#N-comb", 66.4);
          // "Ele desligava o ar e voava devagar."
          drop(["#N-cab", "#N-bon", "#N-comb"], "#N-req", 67.35);
          flip("#N-p1b", 68.31);
          flip("#N-p2b", 68.89);
          // "O passageiro chegava suado e atrasado."
          whip("#N-req", "#N-pax", 69.67);
          kenburns("#N-paximg", 69.67, 71.92, 1.0, 1.06);
          pop("#N-sua", 70.58);
          pop("#N-atr", 70.88);
          // "Gordon trocou esse bônus por setenta e cinco dólares pra todo mundo," (o valor não vai na tela: o fato é US$ 65)
          drop(["#N-pax", "#N-sua", "#N-atr"], "#N-bns", 71.92);
          rise("#N-old", 72.0);
          pop("#N-so", 72.16);
          tl.to("#N-sox", { autoAlpha: 1, scaleX: 1, duration: 6 * q, ease: "power3.out" }, Q(72.68));
          cue(72.7, "swish", -20);
          pop("#N-bill", 73.86, { scale: 0.4, autoAlpha: 0, rotation: -12 });
          cue(73.88, "impacto", -21, { dur: 0.5 });
          tl.to(["#N-old", "#N-so", "#N-sox"], { autoAlpha: 0, duration: 4 * q }, Q(73.8));
          rise("#N-new", 73.95);
          rise("#N-todo", 75.16);
          tl.to(["#J-p0", "#J-p1", "#J-p2", "#J-p3", "#J-p4"], { autoAlpha: 1, duration: 3 * q, stagger: 2 * q }, Q(75.2));
          tl.to(["#J-pp0", "#J-pp1", "#J-pp2", "#J-pp3", "#J-pp4"], { scale: 1.12, duration: 4 * q, ease: "back.out(3)", yoyo: true, repeat: 1, stagger: 2 * q }, Q(75.2));
          cue(75.2, "pop", -21); cue(75.27, "pop", -22, { f0: 820 }); cue(75.33, "pop", -22, { f0: 940 }); cue(75.4, "pop", -22, { f0: 1060 }); cue(75.47, "pop", -22, { f0: 1180 });
          // "todo mês que a empresa ficasse entre as mais pontuais."
          whip("#N-bns", "#N-rk", 76.45);
          tl.fromTo("#N-top", { autoAlpha: 0, scale: 0.94 }, { autoAlpha: 1, scale: 1, duration: 8 * q, ease: "back.out(2)" }, Q(77.77));
          pop("#N-lbl", 77.85);
          tl.to("#N-co", { y: -504, duration: 22 * q, ease: "power3.inOut" }, Q(78.3));
          cue(78.35, "whoosh", -18);
          tl.fromTo("#N-co", { scale: 1 }, { scale: 1.06, duration: 4 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(78.3) + 22 * q);
          cue(78.3 + 22 * q, "clique", -18);
          sceneOut("#N", 79.91);

          // ===== C · CLÍMAX =====
          sceneIn("#C", 79.91);
          kenburns("#C-dc10img", 79.91, 82.46, 1.0, 1.08);
          pop("#C-ano", 80.02);
          pop("#C-melhor", 81.56);
          sceneOut("#C", 82.46);

          // ===== Q · A PERGUNTA (por cima do apresentador, até o fim) =====
          // ===== S · "me segue" =====
          tl.set("#S", { autoAlpha: 1 }, Q(89.4));
          pop("#S-btn", 89.48, { scale: 0.4, autoAlpha: 0, y: 40 });
          tl.fromTo("#S-btn", { scale: 1 }, { scale: 0.94, duration: 3 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(90.51));
          cue(90.53, "clique", -20);
          tl.to("#S-btn", { autoAlpha: 0, y: -40, duration: 6 * q, ease: "power3.in" }, Q(91.35));
          tl.set("#S", { autoAlpha: 0 }, Q(91.6));
          tl.set("#Q", { autoAlpha: 1 }, Q(91.6));
          pop("#Q-ask", 91.6, { y: -60, autoAlpha: 0, scale: 0.92 });
          tl.to("#Q-h1", { backgroundColor: "rgba(242,183,5,.5)", duration: 6 * q, ease: "power2.out" }, Q(93.35)); cue(93.37, "tique", -22);
          tl.to("#Q-h2", { backgroundColor: "rgba(242,183,5,.5)", duration: 6 * q, ease: "power2.out" }, Q(94.83)); cue(94.85, "tique", -22);
'''

T = T.replace('            </style>', CSS + '            </style>', 1)
i = T.index('-->', T.index('CENAS (por video)')) + 3
T = T[:i] + HTML + T[i:]
T = T.replace('          // (vazio = camada transparente)', JS, 1)
open('compositions/mg.html', 'w').write(T)
print('compositions/mg.html', len(T), 'bytes')
