"""POR VIDEO — reel STANLEY McCHRYSTAL. CSS e markup gerado das pecas da camada (importado por work/mg/gen.py).
Pecas: grade da reuniao diaria (7.000 pessoas) · troca de time (o melhor passa 6 meses no outro time) · citacao (saber tudo) ·
o quartinho com os sacos que ninguem lia · o contador do climax (18 -> 300+ operacoes por mes). Aleatorio com semente fixa."""
import random

CSS = r'''
        /* ===== reel STANLEY McCHRYSTAL ===== */
        #mg .full img.dim { filter: brightness(.78); }
        #mg .full img.nvd { filter: brightness(.88); }
        #mg .full img.nvb { filter: brightness(1.18) contrast(1.08); }
        #mg .floor { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0) 56%, rgba(0,0,0,.5) 70%, rgba(0,0,0,.72) 100%); }
        #mg .full img.bw { filter: grayscale(1) contrast(1.05) brightness(.9); }
        /* mundo verde de visao noturna (a capa) */
        #mg .nv { background: radial-gradient(120% 75% at 50% 26%, #13301A 0%, #07120A 62%, #030704 100%); }
        /* grade da reuniao diaria: telas de videochamada */
        #mg .grid { position: absolute; left: 60px; width: 960px; }
        #mg .grid .tile { position: absolute; width: 92px; height: 70px; border-radius: 12px; background: #1B2230; border: 2px solid #2A3344; overflow: hidden; }
        #mg .grid .tile::before { content: ""; position: absolute; left: 34px; top: 12px; width: 24px; height: 24px; border-radius: 50%; background: #5A6578; }
        #mg .grid .tile::after { content: ""; position: absolute; left: 22px; top: 40px; width: 48px; height: 40px; border-radius: 24px 24px 0 0; background: #5A6578; }
        #mg .grid .tile.on { border-color: #1FB45A; }
        #mg .grid .tile.on::before, #mg .grid .tile.on::after { background: #8FA1BA; }
        #mg .big { position: absolute; left: 0; width: 1080px; text-align: center; color: #fff; font-weight: 800; font-size: 250px; line-height: 1;
                   text-shadow: 0 10px 50px rgba(0,0,0,.8); }
        #mg .big .col { display: inline-block; height: 250px; overflow: hidden; vertical-align: top; }
        #mg .big .col div span { display: block; height: 250px; line-height: 250px; width: 160px; text-align: center; }
        #mg .big .pt { display: inline-block; width: 64px; }
        #mg .lbl2 { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; letter-spacing: .1em; color: #fff;
                    text-shadow: 0 6px 30px rgba(0,0,0,.8); }
        #mg .shade { position: absolute; left: 0; width: 1080px; height: 700px;
                     background: radial-gradient(60% 50% at 50% 50%, rgba(8,11,16,.92) 0%, rgba(8,11,16,.75) 55%, rgba(8,11,16,0) 100%); }
        /* troca de time: dois paineis com avatares; o melhor (dourado) atravessa */
        #mg .team { position: absolute; left: 90px; width: 900px; height: 330px; border-radius: 44px; background: #151A23; border: 3px solid #2C3442; }
        #mg .team .hd { position: absolute; left: 44px; top: 30px; font-weight: 800; font-size: 34px; letter-spacing: .14em; color: #8C93A1; }
        #mg .av { position: absolute; width: 130px; height: 130px; border-radius: 50%; background: #2C3442; overflow: hidden; }
        #mg .av::before { content: ""; position: absolute; left: 41px; top: 22px; width: 48px; height: 48px; border-radius: 50%; background: #6B768A; }
        #mg .av::after { content: ""; position: absolute; left: 22px; top: 78px; width: 86px; height: 70px; border-radius: 43px 43px 0 0; background: #6B768A; }
        #mg .av.gold { background: #F2B705; box-shadow: 0 0 0 8px rgba(242,183,5,.25), 0 20px 50px rgba(0,0,0,.5); }
        #mg .av.gold::before, #mg .av.gold::after { background: #11141A; }
        #mg .av.hole { background: transparent; border: 5px dashed #3A4354; }
        #mg .av.hole::before, #mg .av.hole::after { display: none; }
        #mg .arc { position: absolute; left: 0; top: 0; overflow: visible; }
        /* citacao */
        #mg .quote { position: absolute; left: 70px; width: 940px; padding: 54px 60px 46px; border-radius: 44px; background: rgba(255,255,255,.97); color: #11141A;
                     box-shadow: 0 34px 90px rgba(0,0,0,.5); }
        #mg .quote .qm { position: absolute; left: 40px; top: -70px; font-weight: 800; font-size: 200px; line-height: 1; color: #1FB45A; }
        #mg .quote p { margin: 0; font-weight: 800; font-size: 62px; line-height: 1.1; }
        #mg .quote p span { display: inline-block; }
        #mg .quote i { display: block; font-style: normal; font-weight: 700; font-size: 30px; letter-spacing: .1em; color: #5A606B; margin-top: 26px; }
        /* o quartinho: luz verde de cima, sacos caindo e empilhando */
        #mg .room { position: absolute; inset: 0; background: radial-gradient(70% 45% at 50% 18%, #2B5A33 0%, #0D1F12 55%, #040905 100%); }
        #mg .room::after { content: ""; position: absolute; left: 0; right: 0; top: 1240px; bottom: 0; background: linear-gradient(180deg, #050A06 0%, #020403 40%); }
        #mg .bulb { position: absolute; left: 510px; top: 120px; width: 60px; height: 80px; border-radius: 50% 50% 46% 46%; background: #E9FFE6;
                    box-shadow: 0 0 60px 30px rgba(170,255,170,.45), 0 0 200px 90px rgba(90,200,100,.25); }
        #mg .wire { position: absolute; left: 538px; top: 0; width: 4px; height: 124px; background: #0A140C; }
        #mg .sack { position: absolute; width: 200px; height: 200px; }
        #mg .sack svg { position: absolute; left: 0; top: 0; overflow: visible; }
        /* contador do climax */
        #mg .ops { position: absolute; left: 110px; width: 860px; height: 760px; }
        #mg .ops .bar { position: absolute; bottom: 0; width: 300px; border-radius: 30px 30px 8px 8px; transform-origin: 50% 100%; }
        #mg .ops .b1 { left: 40px; height: 46px; background: #5A6578; }
        #mg .ops .b2 { left: 520px; height: 760px; background: linear-gradient(180deg, #2BE07A 0%, #1FB45A 100%); box-shadow: 0 0 60px rgba(31,180,90,.35); }
        #mg .ops .v { position: absolute; width: 300px; text-align: center; font-weight: 800; color: #fff; }
        #mg .ops .k { position: absolute; width: 300px; text-align: center; font-weight: 800; font-size: 32px; letter-spacing: .12em; color: #8C93A1; top: 790px; }
        #mg .ops .v .col { display: inline-block; height: 170px; overflow: hidden; vertical-align: top; }
        #mg .ops .v .col div span { display: block; height: 170px; line-height: 170px; font-size: 160px; width: 104px; text-align: center; }
        #mg .ops .v .plus { display: inline-block; height: 170px; line-height: 170px; font-size: 130px; vertical-align: top; color: #2BE07A; }
'''


def grid(cols=9, rows=11, seed=7):
    """telas de videochamada: (markup, lista de ids na ordem de entrada por distancia ao centro, ids acesos)"""
    rnd = random.Random(seed)
    tiles, order = [], []
    for r in range(rows):
        for c in range(cols):
            k = r * cols + c
            on = rnd.random() < 0.28
            x, y = 12 + c * 104, r * 82
            tiles.append(f'<div class="tile{" on" if on else ""}" id="G-t{k}" style="left:{x}px;top:{y}px"></div>')
            d = ((c - (cols - 1) / 2) ** 2 + (r - (rows - 1) / 2) ** 2) ** .5 + rnd.random() * 0.8
            order.append((d, k))
    order.sort()
    return ''.join(tiles), [f'#G-t{k}' for _, k in order]


SACK_SVG = '''<svg width="200" height="200" viewBox="0 0 200 200">
                <path d="M30 190 Q8 156 16 108 Q24 68 70 54 L84 46 L116 46 L130 54 Q176 68 184 108 Q192 156 170 190 Q100 202 30 190 Z" fill="{c}" />
                <path d="M30 190 Q100 200 170 190 Q182 172 184 150 Q100 182 16 148 Q18 172 30 190 Z" fill="rgba(0,0,0,.30)" />
                <path d="M60 70 Q48 120 58 182 M140 70 Q152 120 142 182" stroke="rgba(0,0,0,.18)" stroke-width="5" fill="none" stroke-dasharray="10 8" />
                <path d="M84 46 L88 30 L112 30 L116 46 Z" fill="{c}" />
                <path d="M88 30 Q74 10 90 4 Q100 16 100 18 Q102 16 110 4 Q126 10 112 30 Z" fill="{c}" />
                <path d="M88 30 Q74 10 90 4 Q100 16 100 18 Q102 16 110 4 Q126 10 112 30 Z" fill="rgba(0,0,0,.12)" />
                <path d="M80 40 Q100 48 120 40" stroke="#3B2E1E" stroke-width="7" fill="none" stroke-linecap="round" />
              </svg>'''


def sacks(seed=11):
    """pilha de sacos no chao do quartinho: (markup, ids na ordem de queda). Base em y~1100 (o pe da pilha), acima da legenda."""
    rnd = random.Random(seed)
    cols = [(5, 1030), (4, 890), (4, 760), (3, 630), (2, 500)]   # (quantos, y do topo do saco) — piramide de baixo para cima
    out, ids, k = [], [], 0
    for n, y in cols:
        w = n * 190
        x0 = 540 - w / 2
        for j in range(n):
            x = x0 + j * 190 + rnd.uniform(-18, 18)
            rot = rnd.uniform(-10, 10)
            c = rnd.choice(['#B9C79A', '#A9B98A', '#C6D2A6', '#9DAE80'])
            out.append(f'<div class="sack" id="S-s{k}" style="left:{x - 15:.0f}px;top:{y + rnd.uniform(-10, 10):.0f}px;transform:rotate({rot:.1f}deg)">'
                       + SACK_SVG.replace('{c}', c) + '</div>')
            ids.append(f'#S-s{k}'); k += 1
    return ''.join(out), ids

CSS += r'''
        /* lista das lanchonetes da base (o proibido) */
        #mg .req { position: absolute; left: 90px; width: 900px; border-radius: 44px; background: #fff; color: #11141A; padding: 38px 46px 26px;
                   box-shadow: 0 34px 90px rgba(0,0,0,.35); }
        #mg .req .hd { font-weight: 800; font-size: 28px; letter-spacing: .14em; color: #8C93A1; }
        #mg .req .tt { font-weight: 800; font-size: 64px; margin: 10px 0 22px; }
        #mg .req .it { position: relative; height: 128px; display: flex; align-items: center; justify-content: space-between; font-weight: 800; font-size: 54px;
                       border-top: 2px solid rgba(128,136,150,.2); }
        #mg .req .it .pill { width: 300px; height: 74px; }
        /* dois cards de foto lado a lado (times separados) */
        #mg .card .ccap { position: absolute; left: 0; right: 0; bottom: 0; padding: 22px 0 20px; text-align: center; font-weight: 800; font-size: 34px;
                         letter-spacing: .12em; color: #fff; background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,.75) 60%); }
'''
