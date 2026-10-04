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
