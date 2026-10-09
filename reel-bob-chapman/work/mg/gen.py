"""POR VIDEO — reel BOB CHAPMAN. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Tempos absolutos de work/tl-words.txt.
Dosagem (docs/05 §24, Deming v2): abertura só com imagem (a capa gerada + dois operários de 1942; nada do Bob antes de "Bob", 11,01 s);
no corpo foto real é o padrão (Library of Congress, FSA/OWI e Matson, domínio público: o curso, o pai e a noiva, o rapaz do torno, a volta pra
casa, o jantar, os filhos, a família, o chão de fábrica, a diretoria); motion só nos capítulos (PASSO 1/2/3), no número (US$ 3,5 bilhões),
na frase exata dele ("chefe fala, líder escuta"), no FUNCIONÁRIO → FILHO DE ALGUÉM, no gráfico da crise (−40%) e no mecanismo do clímax
(a semana do colega que passa pra ele). Clímax = callback da capa (os crachás todos no lugar).
uso: python3 work/mg/gen.py"""
import sys
sys.path.insert(0, 'work/mg')
from parts import CSS
T = open('work/mg/template.html').read()

F = dict(  # foto por papel (assets/mg/, preparadas por work/mg/fotos.py)
    capa='capa.jpg', cracha='capa-crachas.jpg', fur='furadeira.jpg', moca='torno-moca.jpg', rap='torno-rapaz.jpg', beu='beulah.jpg',
    cur='curso.jpg', cur2='curso2.jpg', alt='altar.jpg', volta='volta-casa.jpg', jan='jantar-casal.jpg', fil='filhos.jpg',
    fam='familia.jpg', dir='diretoria.jpg')
OP = dict(  # object-position de cada foto (medido no snapshot)
    capa_split='40% 50%', cracha_split='45% 50%', capa='29% 50%', capa_climax='80% 50%', fur='12% 50%', beu='40% 50%', cur='27% 50%', cur2='50% 50%',
    alt='42% 50%', rap='21% 50%', volta='29% 50%', jan='71% 50%', fil='44% 50%', fam='45% 50%', moca='50% 50%', dir='50% 50%')
def img(k, cls=''):
    return f'<img id="{{id}}" class="{cls}" src="assets/mg/{F[k]}" style="object-position:{OP.get(k, "50% 50%")}" />'
def full(id_, k, cls='', extra='', op=None):
    s = img(k, cls).replace('{id}', id_ + 'img')
    if op: s = s.replace(OP.get(k, '50% 50%'), op)
    return f'<div class="full" id="{id_}">' + s + extra + '</div>'
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
def col(id_, digs):
    return f'<span class="col"><div id="{id_}">' + ''.join(f'<span>{d}</span>' for d in digs) + '</div></span>'
# as semanas sem salario: 4 por pessoa; a 5a casa de ELE fica vazia ate a semana do colega chegar
COLX = [114 + k * 166 for k in range(5)]
def weeks(pre, n=4, ghost=False):
    s = ''.join(f'<div class="w off" id="{pre}{k}">SEMANA<b>{k+1}</b></div>' for k in range(n))
    if ghost: s += f'<div class="w ghost" id="{pre}g"></div>'
    return '<div class="row">' + s + '</div>'

HTML = f'''
        <!-- A · SPLIT DA CAPA (0–5,74, o gancho inteiro): CAPA GERADA A PEDIDO (Codex: galpão à noite, crachás todos no lugar, homem de terno
             de costas) → em "e mais bem-sucedidos" o detalhe da parede de crachás. Nada do Bob. -->
        <div class="scene" id="A" style="height:845px"><div class="world dark"></div>{full('A-capa', 'capa', op=OP['capa_split'])}
          {full('A-cra', 'cracha', op=OP['cracha_split'])}</div>

        <!-- P · PRÉ-REVELAÇÃO (5,74–9,85): o operário na furadeira (1942) → Beulah Faith, 20, no torno (1942). Só foto. -->
        <div class="scene" id="P"><div class="world dark"></div>
          {full('P-fur', 'fur')}
          {full('P-beu', 'beu')}
        </div>

        <!-- B · REVELAÇÃO (11,08–16,48): a capa (ele de costas, no galpão) + nome → o contador US$ 3,5 BILHÕES -->
        <div class="scene" id="B"><div class="world dark"><div class="band" id="B-band"></div></div>
          {full('B-capa', 'capa', '', '<div class="floor"></div>')}
          <div class="name" id="B-name" style="top:1110px"><b>BOB CHAPMAN</b><i>BARRY-WEHMILLER · DESDE 1975</i></div>
          <div class="full" id="B-ctr"><div class="world dark"></div>
            <div class="lbl2" id="B-uma" style="top:470px;font-size:46px;color:#C9CED8">FEZ DELA UMA EMPRESA DE</div>
            <div class="ctr" id="B-num" style="top:590px"><span class="cur" id="B-cur">US$</span>{col('B-c1', '0123')}<span class="pt">,</span>{col('B-c2', '097531905')}</div>
            <div class="lbl2" id="B-bi" style="top:870px;font-size:120px;letter-spacing:.04em;color:#F2B705">BILHÕES</div>
          </div>
        </div>

        <!-- D · PASSO 1 (19,97–28,89): chip + título → o curso (jovens ouvindo os palestrantes, Detroit, 1942) → a frase dele -->
        <div class="scene" id="D"><div class="world dark"><div class="band" id="D-band"></div></div>
          {chip('D', 1, '#1FB45A')}
          {title('D', ['ESCUTA', 'DE'], ['VERDADE.'])}
          {full('D-cur', 'cur', 'dim', '<div class="floor"></div>')}
          <div class="tag" id="D-3d" style="left:90px;top:1060px;background:#1FB45A">CURSO DE 3 DIAS</div>
          <div class="tag" id="D-esc" style="left:90px;top:1160px;background:#11141A">SÓ PRA ENSINAR A ESCUTAR</div>
          <div class="full" id="D-quo">{img('cur2', 'dark2').replace('{id}', 'D-quoimg')}<div class="world" style="background:linear-gradient(180deg,rgba(8,10,14,.35),rgba(8,10,14,.78))"></div>
            <div class="qlbl" id="D-ele" style="top:360px">ELE DIZIA:</div>
            <div class="quote" style="top:500px;font-size:104px"><span id="D-q1">CHEFE</span> <span id="D-q2">FALA.</span><br /><span id="D-q3" class="y">LÍDER</span> <span id="D-q4" class="y">ESCUTA.</span></div>
            <div class="qby" id="D-by" style="top:770px">BOB CHAPMAN</div>
          </div>
        </div>

        <!-- F · PASSO 2 (32,69–40,15): chip + título → o pai entrega a noiva (1938) → o rapaz do torno (1942): FUNCIONÁRIO → FILHO QUERIDO DE ALGUÉM -->
        <div class="scene" id="F"><div class="world dark"><div class="band" id="F-band"></div></div>
          {chip('F', 2, '#F2B705')}
          {title('F', ['FAZ', 'O', 'TESTE'], ['DO', 'PAI.'])}
          {full('F-alt', 'alt', '', '<div class="floor"></div>')}
          {full('F-rap', 'rap', '', '<div class="vig"></div>')}
          <div class="tag" id="F-fun" style="left:90px;top:1050px;background:#fff;color:#11141A">FUNCIONÁRIO</div>
          <div class="strike" id="F-x" style="left:76px;top:1086px;width:340px"></div>
          <div class="tag" id="F-fil" style="left:90px;top:1160px;background:#1FB45A">O FILHO QUERIDO DE ALGUÉM</div>
        </div>

        <!-- H · PASSO 3 (44,03–51,69): chip + título → indo pra casa depois da usina (1940) → o jantar em casa (1938) -->
        <div class="scene" id="H"><div class="world dark"><div class="band" id="H-band"></div></div>
          {chip('H', 3, '#E5322D')}
          {title('H', ['ELE', 'VOLTA'], ['PRA', 'CASA.'])}
          {full('H-vol', 'volta', '', '<div class="floor"></div>')}
          {full('H-jan', 'jan', '', '<div class="floor"></div>')}
          <div class="tag" id="H-cas" style="left:90px;top:1160px;background:#11141A">VAI PRA CASA COM ELE</div>
        </div>

        <!-- K · "De noite, quem escuta é o filho dele." (54,64–57,29): os filhos no jantar (1939), luz da noite -->
        <div class="scene" id="K"><div class="world dark"></div>
          {full('K-fil', 'fil', 'night', '<div class="blue"></div><div class="vig"></div>')}
        </div>

        <!-- L · SPLIT DA VIRADA (57,29–62,36): A VIRADA: UMA CRISE → o gráfico dos pedidos 2008 × 2009 (−40%) -->
        <div class="scene" id="L" style="height:845px"><div class="panel"></div>
          <div class="lbl2" id="L-vir" style="top:250px;font-size:44px;color:#F3B4B0">A VIRADA</div>
          <div class="lbl2" id="L-cri" style="top:330px;font-size:150px;letter-spacing:.02em;color:#fff">UMA CRISE.</div>
          <div class="lbl" id="L-ped" style="top:56px">PEDIDOS DE MÁQUINAS NOVAS</div>
          <div class="chart" id="L-ch">
            <div class="base"></div>
            <div class="bar" id="L-b1" style="left:60px;height:400px;background:#5A606B"></div>
            <div class="bar" id="L-b2" style="left:520px;height:400px;background:#E5322D"></div>
            <div class="yr" id="L-y1" style="left:60px">2008</div>
            <div class="yr" id="L-y2" style="left:520px">2009</div>
          </div>
          <div class="neg" id="L-neg" style="left:500px;top:180px;font-size:140px">−40%</div>
        </div>

        <!-- N · A VIRADA (65,18–78,88): uma família (1937) → a operária do torno (DO CHÃO DE FÁBRICA) → executivos (À DIRETORIA · 4 SEMANAS SEM SALÁRIO)
             → as semanas: a semana do colega que não ia aguentar passa pra ele -->
        <div class="scene" id="N"><div class="world dark"><div class="band" id="N-band"></div></div>
          {full('N-fam', 'fam', '', '<div class="floor"></div>')}
          {full('N-cha', 'moca')}
          <div class="tag" id="N-chao" style="left:90px;top:1120px;background:#11141A">DO CHÃO DE FÁBRICA</div>
          {full('N-dir', 'dir', '', '<div class="floor"></div>')}
          <div class="tag" id="N-dirt" style="left:90px;top:1000px;background:#11141A">À DIRETORIA</div>
          <div class="tag" id="N-4s" style="left:90px;top:1100px;background:#E5322D">4 SEMANAS</div>
          <div class="tag" id="N-ss" style="left:90px;top:1200px;background:#E5322D">SEM SALÁRIO</div>
          <div class="full" id="N-wk"><div class="world dark"></div>
            <div class="lbl2" id="N-hd" style="top:220px;font-size:34px;color:#8C93A1">CADA UM: 4 SEMANAS SEM SALÁRIO</div>
            <div class="wk" id="N-k1" style="top:300px"><div class="nm">ELE<i>FUNCIONÁRIO</i></div>{weeks('N-a', ghost=True)}</div>
            <div class="wk" id="N-k2" style="top:690px"><div class="nm">O COLEGA<i id="N-nao">NÃO IA AGUENTAR</i></div>{weeks('N-b')}</div>
            <div class="w ok" id="N-paga" style="position:absolute;left:{COLX[3]}px;top:810px;width:150px;height:130px">SEMANA<b style="font-size:38px">PAGA</b></div>
            <div class="mv" id="N-mv" style="left:{COLX[3]}px;top:810px">SEMANA<b>+1</b></div>
            <div class="tag" id="N-lug" style="left:90px;top:1100px;background:#F2B705;color:#11141A">NO LUGAR DO COLEGA</div>
          </div>
        </div>

        <!-- C · CLÍMAX (78,88–82,34): a parede de crachás da capa, todos no lugar + 0 DEMITIDOS + 2010 · RECORDE DE LUCRO -->
        <div class="scene" id="C"><div class="world dark"></div>
          {full('C-cra', 'capa', '', '<div class="floor"></div>', op=OP['capa_climax'])}
          <div class="tag" id="C-zero" style="left:90px;top:1060px;background:#1FB45A;font-size:52px">0 DEMITIDOS</div>
          <div class="tag" id="C-rec" style="left:90px;top:1180px;background:#11141A">2010 · RECORDE DE LUCRO</div>
        </div>

        <!-- S · "me segue" (87,83): o botão de seguir aparece sobre o apresentador -->
        <div class="scene" id="S"><div class="follow" id="S-btn">Seguir</div></div>
'''

JS = r'''
          gsap.set(["#A-cra", "#P-beu",
                    "#B-name", "#B-ctr", "#B-uma", "#B-num", "#B-bi",
                    "#D-chip", "#D-w1", "#D-w2", "#D-w3", "#D-cur", "#D-3d", "#D-esc", "#D-quo", "#D-ele", "#D-q1", "#D-q2", "#D-q3", "#D-q4", "#D-by",
                    "#F-chip", "#F-w1", "#F-w2", "#F-w3", "#F-w4", "#F-w5", "#F-alt", "#F-rap", "#F-fun", "#F-x", "#F-fil",
                    "#H-chip", "#H-w1", "#H-w2", "#H-w3", "#H-w4", "#H-vol", "#H-jan", "#H-cas",
                    "#L-vir", "#L-cri", "#L-ped", "#L-ch", "#L-neg",
                    "#N-cha", "#N-chao", "#N-dir", "#N-dirt", "#N-4s", "#N-ss", "#N-wk", "#N-hd", "#N-k1", "#N-k2", "#N-nao", "#N-paga", "#N-mv", "#N-lug",
                    "#N-a0", "#N-a1", "#N-a2", "#N-a3", "#N-ag", "#N-b0", "#N-b1", "#N-b2", "#N-b3",
                    "#C-zero", "#C-rec", "#S-btn"], { autoAlpha: 0 });
          gsap.set(["#D-sel", "#F-sel", "#H-sel"], { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set(["#D-sel .h", "#F-sel .h", "#H-sel .h"], { scale: 0 });
          gsap.set(["#F-x"], { scaleX: 0 });
          gsap.set(["#L-b1", "#L-b2"], { scaleY: 0 });
          gsap.set(["#N-a0", "#N-a1", "#N-a2", "#N-a3", "#N-ag", "#N-b0", "#N-b1", "#N-b2", "#N-b3"], { x: -40 });
          function sel(base, t) {
            tl.to("#" + base + "-sel", { borderColor: "rgba(242,183,5,1)", backgroundColor: "rgba(242,183,5,.16)", duration: 4 * q, ease: "none" }, Q(t));
            tl.to("#" + base + "-sel .h", { scale: 1, duration: 6 * q, ease: "back.out(3)", stagger: q }, Q(t) + q);
          }
          function out(sel_, t) { tl.to(sel_, { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(t) - 5 * q); }

          // ===== A · CAPA (quadro 0 = capa) =====
          splitIn("#A", 0, true);
          kenburns("#A-capaimg", 0, 2.84, 1.0, 1.06);
          // "e mais bem-sucedidos": o detalhe da parede de crachás
          whip("#A-capa", "#A-cra", 2.84);
          kenburns("#A-craimg", 2.84, 5.74, 1.0, 1.08);
          splitOut("#A", 5.74);

          // ===== P · PRÉ-REVELAÇÃO (só foto, nada do Bob) =====
          sceneIn("#P", 5.74);
          kenburns("#P-furimg", 5.74, 8.34, 1.1, 1.0);
          // "o seu funcionário não é custo": Beulah Faith, 20
          whip("#P-fur", "#P-beu", 8.34);
          kenburns("#P-beuimg", 8.34, 9.85, 1.0, 1.06);
          sceneOut("#P", 9.85);

          // ===== B · REVELAÇÃO ("Bob" 11,01 → 11,08) =====
          sceneIn("#B", 11.08); drift("#B-band", 11.08, 16.48);
          kenburns("#B-capaimg", 11.08, 13.24, 1.0, 1.08);
          rise("#B-name", 11.25);
          // "e fez dela uma empresa de três bilhões e meio de dólares"
          drop(["#B-capa", "#B-name"], "#B-ctr", 13.24);
          rise("#B-uma", 13.4);
          pop("#B-num", 14.4, { scale: 0.7, autoAlpha: 0 });
          tl.fromTo("#B-c1", { y: 0, filter: "blur(5px)" }, { y: -3 * 260, filter: "blur(0px)", duration: 20 * q, ease: "power4.out" }, Q(14.52));
          tl.fromTo("#B-c2", { y: 0, filter: "blur(5px)" }, { y: -8 * 260, filter: "blur(0px)", duration: 26 * q, ease: "power4.out" }, Q(14.52));
          cue(14.54, "cacaniquel", -20);
          rise("#B-bi", 14.75);
          cue(15.4, "impacto", -21, { dur: 0.5 });
          sceneOut("#B", 16.48);

          // ===== D · PASSO 1 → O CURSO → A FRASE DELE =====
          sceneIn("#D", 19.97); drift("#D-band", 19.97, 28.89);
          chip("D", 20.3, 19.97);
          rise("#D-w1", 20.67); rise("#D-w2", 21.16); rise("#D-w3", 21.33);
          cue(20.67, "tique", -24); cue(21.16, "tique", -24); cue(21.33, "tique", -24);
          sel("D", 21.6);
          // "Ele pagava um curso de três dias só pra ensinar o time a escutar."
          smear("#D-chip", 21.94); out("#D-title", 21.94); zoomIn("#D-cur", 21.94);
          kenburns("#D-curimg", 21.94, 25.91, 1.0, 1.08);
          pop("#D-3d", 22.69);
          pop("#D-esc", 24.02);
          // "E dizia: chefe fala, líder escuta."
          drop(["#D-cur", "#D-3d", "#D-esc"], "#D-quo", 25.91);
          kenburns("#D-quoimg", 25.91, 28.89, 1.0, 1.06);
          pop("#D-ele", 25.98);
          rise("#D-q1", 26.7); rise("#D-q2", 27.19); rise("#D-q3", 27.73); rise("#D-q4", 28.16);
          cue(26.7, "tique", -22); cue(27.19, "tique", -22); cue(27.73, "tique", -22); cue(28.16, "tique", -22);
          rise("#D-by", 28.4);
          sceneOut("#D", 28.89);

          // ===== F · PASSO 2 → O PAI E A NOIVA → O FILHO QUERIDO DE ALGUÉM =====
          sceneIn("#F", 32.69); drift("#F-band", 32.69, 40.15);
          chip("F", 33.05, 32.69);
          rise("#F-w1", 33.48); rise("#F-w2", 33.53); rise("#F-w3", 33.6); rise("#F-w4", 34.0); rise("#F-w5", 34.09);
          cue(33.48, "tique", -24); cue(33.6, "tique", -24); cue(34.0, "tique", -24); cue(34.09, "tique", -24);
          sel("F", 34.3);
          // "Ele viu um pai entregando a filha no altar"
          smear("#F-chip", 34.65); out("#F-title", 34.65); zoomIn("#F-alt", 34.65);
          kenburns("#F-altimg", 34.65, 37.49, 1.0, 1.1);
          // "todo funcionário é o filho querido de alguém"
          whip("#F-alt", "#F-rap", 37.49);
          kenburns("#F-rapimg", 37.49, 40.15, 1.0, 1.08);
          pop("#F-fun", 37.6);
          tl.to("#F-x", { autoAlpha: 1, scaleX: 1, duration: 6 * q, ease: "power3.out" }, Q(38.35));
          cue(38.37, "swish", -19);
          pop("#F-fil", 38.7);
          sceneOut("#F", 40.15);

          // ===== H · PASSO 3 → A VOLTA PRA CASA → O JANTAR =====
          sceneIn("#H", 44.03); drift("#H-band", 44.03, 51.69);
          chip("H", 44.27, 44.03);
          rise("#H-w1", 45.41); rise("#H-w2", 45.63); rise("#H-w3", 46.01); rise("#H-w4", 46.31);
          cue(45.41, "tique", -24); cue(45.63, "tique", -24); cue(46.01, "tique", -24); cue(46.31, "tique", -24);
          sel("H", 46.6);
          // "Ele dizia que o jeito que você trata alguém no trabalho"
          smear("#H-chip", 47.16); out("#H-title", 47.16); zoomIn("#H-vol", 47.16);
          kenburns("#H-volimg", 47.16, 49.71, 1.0, 1.1);
          // "vai pra casa com ele"
          whip("#H-vol", "#H-jan", 49.71);
          kenburns("#H-janimg", 49.71, 51.69, 1.0, 1.06);
          pop("#H-cas", 50.39);
          sceneOut("#H", 51.69);

          // ===== K · "De noite, quem escuta é o filho dele." =====
          sceneIn("#K", 54.64);
          kenburns("#K-filimg", 54.64, 57.29, 1.0, 1.12);
          sceneOut("#K", 57.29);

          // ===== L · SPLIT DA VIRADA: A CRISE → PEDIDOS 2008 × 2009 =====
          splitIn("#L", 57.29);
          rise("#L-vir", 57.4);
          rise("#L-cri", 58.05); cue(58.07, "impacto", -21, { dur: 0.6 });
          // "Em 2009, os pedidos caíram quarenta por cento."
          tl.to(["#L-vir", "#L-cri"], { autoAlpha: 0, y: -60, duration: 6 * q, ease: "power3.in" }, Q(59.0));
          tl.set("#L-ch", { autoAlpha: 1 }, Q(59.12));
          rise("#L-y1", 59.18); rise("#L-y2", 59.18);
          tl.to("#L-b1", { scaleY: 1, duration: 10 * q, ease: "expo.out" }, Q(59.2)); cue(59.2, "pop", -24, { f0: 700 });
          tl.to("#L-b2", { scaleY: 1, duration: 10 * q, ease: "expo.out" }, Q(59.35)); cue(59.35, "pop", -24, { f0: 820 });
          rise("#L-ped", 59.98);
          tl.to("#L-b2", { scaleY: 0.6, duration: 12 * q, ease: "power3.inOut" }, Q(60.76)); cue(60.78, "swish", -19);
          slam("#L-neg", 61.3, -4);
          splitOut("#L", 62.36);

          // ===== N · A VIRADA: A FAMÍLIA → DO CHÃO DE FÁBRICA À DIRETORIA → A SEMANA DO COLEGA =====
          sceneIn("#N", 65.18); drift("#N-band", 65.18, 78.88);
          kenburns("#N-famimg", 65.18, 67.92, 1.0, 1.08);
          // "Todo mundo, do chão de fábrica"
          whip("#N-fam", "#N-cha", 67.92);
          kenburns("#N-chaimg", 67.92, 69.7, 1.0, 1.06);
          pop("#N-chao", 68.63);
          // "à diretoria, tirou quatro semanas de folga sem salário."
          whip(["#N-cha", "#N-chao"], "#N-dir", 69.7);
          kenburns("#N-dirimg", 69.7, 73.67, 1.0, 1.1);
          pop("#N-dirt", 69.94);
          pop("#N-4s", 71.1);
          pop("#N-ss", 72.6);
          // "E teve funcionário que tirou uma semana a mais no lugar do colega que não ia aguentar."
          drop(["#N-dir", "#N-dirt", "#N-4s", "#N-ss"], "#N-wk", 73.67);
          rise("#N-hd", 73.8);
          rise("#N-k1", 73.93); rise("#N-k2", 74.08);
          stagger(["#N-a0", "#N-a1", "#N-a2", "#N-a3", "#N-ag"], 74.2, 5, 2);
          stagger(["#N-b0", "#N-b1", "#N-b2", "#N-b3"], 74.45, 4, 2);
          pop("#N-mv", 75.47, { scale: 0.4, autoAlpha: 0 });
          pop("#N-paga", 75.5, { scale: 0.5, autoAlpha: 0 }, "clique");
          tl.set("#N-b3", { autoAlpha: 0 }, Q(75.5) + 4 * q);
          tl.to("#N-mv", { x: __DX__, y: -390, duration: 14 * q, ease: "power3.inOut" }, Q(75.62));
          cue(75.64, "whoosh", -18);
          tl.fromTo("#N-mv", { scale: 1 }, { scale: 1.08, duration: 4 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(75.62) + 14 * q);
          cue(75.62 + 14 * q, "clique", -18);
          pop("#N-lug", 76.52);
          rise("#N-nao", 77.6);
          sceneOut("#N", 78.88);

          // ===== C · CLÍMAX: os crachás todos no lugar =====
          sceneIn("#C", 78.88);
          kenburns("#C-craimg", 78.88, 82.34, 1.0, 1.1);
          pop("#C-zero", 79.4, { scale: 0.4, autoAlpha: 0 });
          cue(79.42, "impacto", -20, { dur: 0.6 });
          pop("#C-rec", 81.02);
          sceneOut("#C", 82.34);

          // ===== S · "me segue" =====
          tl.set("#S", { autoAlpha: 1 }, Q(87.75));
          pop("#S-btn", 87.85, { scale: 0.4, autoAlpha: 0, y: 40 });
          tl.fromTo("#S-btn", { scale: 1 }, { scale: 0.94, duration: 3 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(88.54));
          cue(88.56, "clique", -20);
          tl.to("#S-btn", { autoAlpha: 0, y: -40, duration: 6 * q, ease: "power3.in" }, Q(89.35));
          tl.set("#S", { autoAlpha: 0 }, Q(89.6));
'''.replace('__DX__', str(COLX[4] - COLX[3]))

T = T.replace('            </style>', CSS + '            </style>', 1)
i = T.index('-->', T.index('CENAS (por video)')) + 3
T = T[:i] + HTML + T[i:]
T = T.replace('          // (vazio = camada transparente)', JS, 1)
open('compositions/mg.html', 'w').write(T)
print('compositions/mg.html', len(T), 'bytes')
