"""POR VIDEO — reel ERNEST SHACKLETON. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Tempos absolutos de work/tl-words.txt.
Dosagem (docs/05 §24): abertura só com fotos (capa gerada + o Endurance no gelo, nada do Shackleton antes de "Ernest"); no corpo foto
real é o padrão (Frank Hurley, 1914–1916); motion só nos capítulos (PASSO 1/2/3), no mecanismo (a torcida que o reclamão junta longe do
chefe), no objeto que a fala nomeia e não existe em foto (as moedas de ouro na neve; a bola do futebol no gelo) e na virada (a fala do
carpinteiro, o contrato com SALÁRIO ATÉ O PORTO, FIM DO MOTIM, MEDO × REBELDIA) (~38% da cobertura).
Fotos: Commons / State Library of NSW / RMG (domínio público) — LICENCAS-FOTOS.txt. A capa é gerada a pedido (Codex).
uso: python3 work/mg/gen.py"""
import sys
sys.path.insert(0, 'work/mg')
from parts import CSS
T = open('work/mg/template.html').read()

F = dict(  # foto por papel (assets/mg/, preparadas por work/mg/fotos.py)
    capa='capa-shackleton.jpg', noite='endurance-noite-1915.jpg', vela='endurance-vela-gelo-1915.jpg',
    retrato='shackleton-expedicao-1915.jpg', preso='endurance-preso-1915.jpg', pinguim='pinguins-1915.jpg',
    barraca='hurley-shackleton-acampamento.jpg', acamp='acampamento-gelo-1915.jpg', trenos='trenos-prontos-1915.jpg', noitelonga='solidao-gelo-1915.jpg',
    trabalho='abrindo-caminho-gelo-1915.jpg', aderna='endurance-adernado-1915.jpg', afunda='endurance-afundando-1915.jpg',
    bote='puxando-bote-1915.jpg', caird='james-caird-partida-1916.jpg')
OP = dict(  # object-position de cada foto (medido no snapshot)
    capa_split='50% 50%', vela_split='45% 34%', capa='48.5% 50%', noite='57% 50%', vela='45% 50%', retrato='42% 30%', preso='41% 50%', pinguim='50% 50%',
    barraca='56% 50%', acamp='38% 50%', trenos='50% 50%', noitelonga='50% 50%', trabalho='40% 50%', aderna='60% 50%', afunda='55% 50%', bote='50% 50%',
    caird='46% 50%')
def img(k, cls=''):
    return f'<img id="{{id}}" class="{cls}" src="assets/mg/{F[k]}" style="object-position:{OP.get(k, "50% 50%")}" />'
def full(id_, k, cls='', extra=''):
    return f'<div class="full" id="{id_}">' + img(k, cls).replace('{id}', id_ + 'img') + extra + '</div>'
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
# a torcida: 7 pessoas cinza espalhadas (perto do chefe) -> em volta do reclamao (longe do chefe)
GENTE0 = [(170, 520), (900, 470), (250, 760), (840, 760), (520, 640), (140, 1130), (960, 1120)]
GENTE1 = [(160, 860), (395, 845), (120, 1080), (430, 1110), (180, 1290), (400, 1300), (290, 760)]
TORCIDA = ''.join(f'<div class="pt" id="D-g{k}" style="left:{x}px;top:{y}px"></div>' for k, (x, y) in enumerate(GENTE0))
# moedas de ouro: (x final, y final no chao de neve, rotacao)
MOEDAS = [(300, 930, -18), (470, 960, 12), (640, 925, -6), (790, 965, 22), (560, 1000, -30)]
COINS = ''.join(f'<div class="coin" id="F-c{k}" style="left:{x}px;top:{y}px"></div>' for k, (x, y, r) in enumerate(MOEDAS))

HTML = f'''
        <!-- A · SPLIT DA CAPA (0–5,52, o gancho inteiro): CAPA GERADA A PEDIDO (Codex: Shackleton de costas diante do Endurance esmagado, à noite) -->
        <div class="scene" id="A" style="height:845px"><div class="world dark"></div>{full('A-capa', 'capa').replace(OP['capa'], OP['capa_split'])}
          {full('A-preso', 'vela').replace(OP['vela'], OP['vela_split'])}</div>

        <!-- P · PRÉ-REVELAÇÃO (5,52–10,40): o Endurance à noite (Hurley, 1915) → o navio forçando o gelo — nada do Shackleton -->
        <div class="scene" id="P"><div class="world dark"></div>
          {full('P-noite', 'noite')}
          {full('P-vela', 'preso', 'cold')}
        </div>

        <!-- B · REVELAÇÃO (12,13–19,10): retrato do Shackleton na expedição + nome → o navio preso (QUASE 2 ANOS, SEM RÁDIO) → pinguins -->
        <div class="scene" id="B"><div class="world dark"></div>
          {full('B-ret', 'retrato')}
          <div class="name" id="B-name" style="top:1090px"><b>ERNEST SHACKLETON</b><i>EXPLORADOR · ANTÁRTIDA, 1914–1916</i></div>
          {full('B-preso', 'acamp', 'cold', '<div class="vig"></div>')}
          <div class="tag" id="B-2a" style="left:90px;top:1150px;background:#11141A">QUASE 2 ANOS NO GELO</div>
          <div class="tag" id="B-radio" style="left:90px;top:1250px;background:#E5322D">SEM RÁDIO</div>
          {full('B-ping', 'pinguim')}
        </div>

        <!-- D · PASSO 1 (24,76–35,06) → Hurley e Shackleton no acampamento (a barraca) → a torcida -->
        <div class="scene" id="D"><div class="world dark"><div class="band" id="D-band"></div></div>
          {chip('D', 1, '#1FB45A')}
          {title('D', ['PÕE', 'DO'], ['SEU', 'LADO.'])}
          {full('D-bar', 'barraca', 'cold', '<div class="vig"></div>')}
          <div class="tag" id="D-enc" style="left:60px;top:880px;background:#E5322D">O ENCRENQUEIRO</div>
          <div class="tag" id="D-btag" style="left:300px;top:330px;background:#11141A">A BARRACA DO CHEFE</div>
          <div class="full" id="D-tor"><div class="world dark"></div>
            <div class="lnk" id="D-lnk"></div>
            <div class="tag" id="D-longe" style="left:560px;top:690px;background:#252C39">LONGE</div>
            <div class="halo" id="D-halo" style="left:290px;top:1060px"></div>
            {TORCIDA}
            <div class="pt boss" id="D-boss" style="left:780px;top:330px"><b>CHEFE</b></div>
            <div class="pt bad" id="D-bad" style="left:540px;top:700px"><b>RECLAMÃO</b></div>
            <div class="tag" id="D-torc" style="left:560px;top:1180px;background:#E5322D">JUNTA TORCIDA</div>
          </div>
        </div>

        <!-- F · PASSO 2 (38,47–47,12) → o acampamento no gelo (MENOS DE 1 KG) → as moedas de ouro na neve -->
        <div class="scene" id="F"><div class="world dark"><div class="band" id="F-band"></div></div>
          {chip('F', 2, '#F2B705')}
          {title('F', ['VOCÊ', 'LARGA'], ['PRIMEIRO.'])}
          <div class="card" id="F-acamp" style="left:60px;top:400px;width:960px;height:610px"><img id="F-acampimg" class="cold" src="assets/mg/{F['trenos']}" style="object-position:{OP['trenos']}" /></div>
          <div class="tag" id="F-kg" style="left:90px;top:1080px;background:#11141A">MENOS DE 1 KG POR HOMEM</div>
          <div class="full" id="F-neve"><div class="snow"></div>
            <div class="lbl2" id="F-l1" style="top:250px;font-size:64px;color:#fff">O 1º A LARGAR:</div>
            <div class="lbl2" id="F-l2" style="top:350px;font-size:110px;color:#F2B705">O CHEFE.</div>
            {COINS}
            <div class="tag" id="F-ouro" style="left:300px;top:1120px;background:#C9952A">MOEDAS DE OURO</div>
          </div>
        </div>

        <!-- H · PASSO 3 (50,38–59,63) → a noite longa no gelo → abrindo caminho no gelo (TAREFA TODO DIA) + a bola (FUTEBOL NO GELO) -->
        <div class="scene" id="H"><div class="world dark"><div class="band" id="H-band"></div></div>
          {chip('H', 3, '#E5322D')}
          {title('H', ['NINGUÉM'], ['FICA', 'PARADO.'])}
          {full('H-noite', 'noitelonga', 'cold', '<div class="vig"></div>')}
          {full('H-trab', 'trabalho', 'cold', '<div class="vig"></div>')}
          <div class="tag" id="H-tar" style="left:90px;top:1080px;background:#11141A">TAREFA TODO DIA</div>
          <div class="ball" id="H-ball" style="left:760px;top:900px"></div>
          <div class="tag" id="H-fut" style="left:90px;top:1180px;background:#1FB45A">ATÉ FUTEBOL NO GELO</div>
        </div>

        <!-- L · SPLIT DA VIRADA (63,42–66,30): o Endurance adernado pelo gelo → "O navio afundou" (nov/1915) -->
        <div class="scene" id="L" style="height:845px"><div class="world dark"></div>
          {full('L-ader', 'aderna')}
          {full('L-afun', 'afunda')}
        </div>

        <!-- N · O MOTIM (66,30–81,30): os homens puxando o bote → a fala do carpinteiro → o contrato → FIM DO MOTIM → MEDO × REBELDIA -->
        <div class="scene" id="N"><div class="world dark"><div class="band" id="N-band"></div></div>
          {full('N-bote', 'bote', 'cold', '<div class="vig"></div>')}
          <div class="tag" id="N-carp" style="left:90px;top:330px;background:#11141A">O CARPINTEIRO</div>
          <div class="tag" id="N-parou" style="left:90px;top:430px;background:#E5322D">PAROU DE PUXAR</div>
          <div id="N-chat" style="position:absolute;inset:0">
            <div class="who" id="N-wc" style="left:90px;top:330px"><i style="background:#E5322D">C</i>O CARPINTEIRO</div>
            <div class="bubble big" id="N-b1" style="left:90px;top:420px;width:800px">SEM NAVIO, NINGUÉM MANDA EM MIM.</div>
          </div>
          <div class="paper" id="N-paper" style="top:250px">
            <div class="hd">ENDURANCE · 1914</div>
            <div class="tt">CONTRATO DE BORDO</div>
            <div class="ln" style="width:92%"></div><div class="ln" style="width:78%"></div><div class="ln" style="width:86%"></div>
            <div class="hl" id="N-hl"><i id="N-mk"></i><span>O SALÁRIO CONTINUA ATÉ O PORTO.</span></div>
            <div class="ln" style="width:70%"></div><div class="ln" style="width:84%"></div>
          </div>
          <div class="who" id="N-we" style="right:110px;top:1030px"><i style="background:#F2B705;color:#11141A">E</i>ERNEST LEU PRA TODOS</div>
          <div class="stamp" data-layout-allow-overlap id="N-fim" style="left:150px;top:800px;font-size:96px">FIM DO MOTIM</div>
          <div class="full" id="N-medo"><div class="world dark"></div>
            <div class="word" id="N-m1" style="top:420px;font-size:230px;color:#F2B705">MEDO</div>
            <div class="word" id="N-m2" style="top:760px;font-size:100px;color:#8C93A1">NÃO REBELDIA</div>
            <div class="strike" id="N-mx" style="left:180px;top:815px;width:720px"></div>
          </div>
        </div>

        <!-- C · CLÍMAX (81,30–85,33): o James Caird sai de Elephant Island para buscar socorro, 24 abr 1916 — o carpinteiro foi junto -->
        <div class="scene" id="C">
          <div class="full"><img class="bgblur" src="assets/mg/{F['caird']}" /></div>
          <div class="fitimg" id="C-caird" style="top:420px"><img id="C-cairdimg" src="assets/mg/{F['caird']}" /></div>
          <div class="tag" id="C-data" style="left:90px;top:1150px;background:#11141A">ABRIL DE 1916 · O BOTE DO SOCORRO</div>
          <div class="tag" id="C-junto" style="left:90px;top:1250px;background:#1FB45A">O CARPINTEIRO FOI JUNTO</div>
        </div>
'''

JS = r'''
          gsap.set(["#A-preso", "#P-vela",
                    "#B-name", "#B-preso", "#B-2a", "#B-radio", "#B-ping",
                    "#D-chip", "#D-w1", "#D-w2", "#D-w3", "#D-w4", "#D-bar", "#D-enc", "#D-btag", "#D-tor", "#D-lnk", "#D-longe", "#D-halo",
                    "#D-g0", "#D-g1", "#D-g2", "#D-g3", "#D-g4", "#D-g5", "#D-g6", "#D-boss", "#D-bad", "#D-torc",
                    "#F-chip", "#F-w1", "#F-w2", "#F-w3", "#F-acamp", "#F-kg", "#F-neve", "#F-l1", "#F-l2",
                    "#F-c0", "#F-c1", "#F-c2", "#F-c3", "#F-c4", "#F-ouro",
                    "#H-chip", "#H-w1", "#H-w2", "#H-w3", "#H-noite", "#H-trab", "#H-tar", "#H-ball", "#H-fut",
                    "#L-afun",
                    "#N-carp", "#N-parou", "#N-chat", "#N-wc", "#N-b1", "#N-paper", "#N-we", "#N-fim", "#N-medo", "#N-m1", "#N-m2", "#N-mx",
                    "#C-data", "#C-junto"], { autoAlpha: 0 });
          gsap.set(["#D-sel", "#F-sel", "#H-sel"], { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set(["#D-sel .h", "#F-sel .h", "#H-sel .h"], { scale: 0 });
          gsap.set("#N-mk", { scaleX: 0 });
          gsap.set("#N-mx", { scaleX: 0 });
          gsap.set("#D-lnk", { scaleX: 0, rotation: 123.9 });
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
          kenburns("#A-capaimg", 0, 3.1, 1.0, 1.06);
          // "e mais admirados": o navio de verdade, preso no gelo (Hurley, 1915)
          whip("#A-capa", "#A-preso", 3.1);
          kenburns("#A-presoimg", 3.1, 5.52, 1.0, 1.08);
          splitOut("#A", 5.52);

          // ===== P · PRÉ-REVELAÇÃO (só fotos, nada do Shackleton) =====
          sceneIn("#P", 5.52);
          kenburns("#P-noiteimg", 5.52, 7.95, 1.12, 1.0);
          whip("#P-noite", "#P-vela", 7.95);
          kenburns("#P-velaimg", 7.95, 10.4, 1.0, 1.1);
          sceneOut("#P", 10.4);

          // ===== B · REVELAÇÃO ("Ernest" 12,06 → 12,13) =====
          sceneIn("#B", 12.13);
          kenburns("#B-retimg", 12.13, 13.9, 1.0, 1.06);
          rise("#B-name", 12.3);
          // "preso no gelo": o navio preso no gelo do mar de Weddell
          whip(["#B-ret", "#B-name"], "#B-preso", 13.9);
          kenburns("#B-presoimg", 13.9, 17.7, 1.0, 1.1);
          pop("#B-2a", 14.15);
          pop("#B-radio", 15.97);
          // "comendo pinguim"
          whip(["#B-preso", "#B-2a", "#B-radio"], "#B-ping", 17.7);
          kenburns("#B-pingimg", 17.7, 19.1, 1.08, 1.0);
          sceneOut("#B", 19.1);

          // ===== D · PASSO 1 → A BARRACA → A TORCIDA =====
          sceneIn("#D", 24.76); drift("#D-band", 24.76, 35.06);
          cap("D", [24.95, 24.76, 25.1, 26.1, 26.25, 26.48], 26.7, 27.2, "#D-bar");
          kenburns("#D-barimg", 27.2, 31.4, 1.0, 1.02);
          pop("#D-enc", 28.78);
          pop("#D-btag", 30.38);
          // "Ele sabia que reclamão longe do chefe junta torcida."
          drop(["#D-bar", "#D-enc", "#D-btag"], "#D-tor", 31.4);
          pop("#D-g0", 31.55, { scale: 0.3, autoAlpha: 0 }, false); pop("#D-g1", 31.6, { scale: 0.3, autoAlpha: 0 }, false);
          pop("#D-g2", 31.65, { scale: 0.3, autoAlpha: 0 }, false); pop("#D-g3", 31.7, { scale: 0.3, autoAlpha: 0 }, false);
          pop("#D-g4", 31.75, { scale: 0.3, autoAlpha: 0 }, false); pop("#D-g5", 31.8, { scale: 0.3, autoAlpha: 0 }, false);
          pop("#D-g6", 31.85, { scale: 0.3, autoAlpha: 0 }, false);
          cue(31.6, "tique", -24);
          pop("#D-bad", 32.1, { scale: 0.3, autoAlpha: 0 });
          // "longe": o reclamao vai para o canto, longe do chefe
          tl.to("#D-bad", { x: 290 - 540, y: 1060 - 700, duration: 10 * q, ease: "power3.inOut" }, Q(32.66));
          cue(32.7, "swish", -20);
          pop("#D-boss", 33.21, { scale: 0.3, autoAlpha: 0 });
          tl.to("#D-lnk", { autoAlpha: 1, scaleX: 1, duration: 8 * q, ease: "power2.out" }, Q(33.35));
          pop("#D-longe", 33.4, { scale: 0.6, autoAlpha: 0 }, false);
          // "junta torcida": a gente vai para perto do reclamao
          GENTE1.forEach(function (p, k) { tl.to("#D-g" + k, { x: p[0] - GENTE0[k][0], y: p[1] - GENTE0[k][1], duration: 14 * q, ease: "power3.inOut" }, Q(33.65) + k * q); });
          cue(33.7, "whoosh", -18);
          tl.fromTo("#D-halo", { scale: 0.4, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 9 * q, ease: "back.out(2)" }, Q(34.04));
          pop("#D-torc", 34.1);
          sceneOut("#D", 35.06);

          // ===== F · PASSO 2 → O ACAMPAMENTO → AS MOEDAS DE OURO =====
          sceneIn("#F", 38.47); drift("#F-band", 38.47, 47.12);
          cap("F", [38.66, 38.47, 39.41, 39.65, 40.01], 40.3, 40.83, "#F-acamp");
          kenburns("#F-acampimg", 40.83, 43.62, 1.0, 1.06);
          pop("#F-kg", 42.25);
          drop(["#F-acamp", "#F-kg"], "#F-neve", 43.62);
          rise("#F-l1", 43.75);
          rise("#F-l2", 44.98);
          cue(45.0, "impacto", -21, { dur: 0.5 });
          // "as moedas de ouro": caem uma a uma e afundam na neve
          MOEDAS.forEach(function (m, k) {
            var t = 45.48 + k * 3 * q;
            tl.fromTo("#F-c" + k, { y: -1300, rotation: m[2] - 140, autoAlpha: 1 }, { y: 0, rotation: m[2], autoAlpha: 1, immediateRender: false, duration: 10 * q, ease: "power3.in" }, Q(t));
            tl.fromTo("#F-c" + k, { scaleY: 1 }, { scaleY: 0.82, duration: 2 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(t) + 10 * q);
            cue(t + 10 * q, "clique", -19);
          });
          pop("#F-ouro", 46.28);
          sceneOut("#F", 47.12);

          // ===== H · PASSO 3 → A NOITE LONGA → TAREFA TODO DIA + FUTEBOL NO GELO =====
          sceneIn("#H", 50.38); drift("#H-band", 50.38, 59.63);
          cap("H", [50.55, 50.38, 51.23, 51.67, 51.96], 52.2, 52.79, "#H-noite");
          kenburns("#H-noiteimg", 52.79, 55.82, 1.1, 1.0);
          whip("#H-noite", "#H-trab", 55.82);
          kenburns("#H-trabimg", 55.82, 59.63, 1.0, 1.1);
          pop("#H-tar", 56.19);
          // "e até o futebol no gelo": a bola quica no gelo
          tl.fromTo("#H-ball", { y: -900, rotation: -200, autoAlpha: 1 }, { y: 0, rotation: 0, autoAlpha: 1, immediateRender: false, duration: 9 * q, ease: "power3.in" }, Q(57.66));
          tl.to("#H-ball", { y: -170, duration: 6 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(57.66) + 9 * q);
          cue(57.66 + 9 * q, "pop", -18, { f0: 260 });
          pop("#H-fut", 57.95);
          sceneOut("#H", 59.63);

          // ===== L · SPLIT DA VIRADA =====
          splitIn("#L", 63.42);
          kenburns("#L-aderimg", 63.42, 65.57, 1.0, 1.1);
          whip("#L-ader", "#L-afun", 65.57);
          kenburns("#L-afunimg", 65.57, 66.3, 1.06, 1.0);
          splitOut("#L", 66.3);

          // ===== N · O MOTIM =====
          sceneIn("#N", 66.3); drift("#N-band", 66.3, 81.3);
          kenburns("#N-boteimg", 66.3, 70.14, 1.0, 1.1);
          pop("#N-carp", 66.5);
          // "parou de puxar o bote": a imagem para e escurece
          tl.to("#N-boteimg", { filter: "grayscale(1) brightness(.55)", duration: 6 * q, ease: "power2.out" }, Q(68.52));
          pop("#N-parou", 68.6);
          cue(68.55, "impacto", -21, { dur: 0.5 });
          // "sem navio, ninguém manda em mim"
          drop(["#N-bote", "#N-carp", "#N-parou"], "#N-chat", 70.14);
          rise("#N-wc", 70.15);
          pop("#N-b1", 70.3, { scale: 0.5, autoAlpha: 0, y: 30 });
          // "Ernest leu o contrato pra todo mundo e avisou: o salário continua até o porto."
          drop(["#N-chat"], "#N-paper", 72.95);
          rise("#N-we", 73.7);
          tl.to("#N-mk", { scaleX: 1, duration: 1.6, ease: "power1.inOut" }, Q(75.42));
          cue(75.45, "swish", -22);
          tl.fromTo("#N-hl", { scale: 1 }, { scale: 1.05, duration: 5 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(77.08));
          // "Acabou o motim."
          slam("#N-fim", 78.27, -7);
          // "Era medo, não rebeldia."
          drop(["#N-paper", "#N-we", "#N-fim"], "#N-medo", 79.05);
          rise("#N-m1", 79.08);
          rise("#N-m2", 79.8);
          tl.to("#N-mx", { autoAlpha: 1, scaleX: 1, duration: 7 * q, ease: "power3.out" }, Q(80.3));
          cue(80.32, "swish", -19);
          sceneOut("#N", 81.3);

          // ===== C · CLÍMAX: o bote do socorro =====
          sceneIn("#C", 81.3);
          kenburns("#C-cairdimg", 81.3, 85.33, 1.0, 1.08);
          pop("#C-data", 81.6);
          pop("#C-junto", 84.39);
          sceneOut("#C", 85.33);
'''
JS = JS.replace('GENTE1.forEach', 'var GENTE0 = ' + str([list(p) for p in GENTE0]) + ', GENTE1 = ' + str([list(p) for p in GENTE1]) + ';\n          GENTE1.forEach', 1)
JS = JS.replace('MOEDAS.forEach', 'var MOEDAS = ' + str([list(m) for m in MOEDAS]) + ';\n          MOEDAS.forEach', 1)

T = T.replace('            </style>', CSS + '            </style>', 1)
i = T.index('-->', T.index('CENAS (por video)')) + 3
T = T[:i] + HTML + T[i:]
T = T.replace('          // (vazio = camada transparente)', JS, 1)
open('compositions/mg.html', 'w').write(T)
print('compositions/mg.html', len(T), 'bytes')
