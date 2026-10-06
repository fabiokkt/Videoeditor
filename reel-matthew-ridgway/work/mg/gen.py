"""POR VIDEO — reel MATTHEW RIDGWAY. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Tempos absolutos de work/tl-words.txt.
Dosagem (docs/05 §24): abertura só com fotos (capa gerada + soldados na neve); no corpo foto real é o padrão; motion só nos
capítulos (PASSO 1/2/3), no objeto que a fala nomeia e não existe em foto (o bilhete e a calça de pijama na parede; a lista do que
faltava), no número (5.000 rostos) e no mecanismo da virada (a conversa: plano de recuo × plano de ataque, FORA) (~40% da cobertura).
Fotos: Exército dos EUA / USMC / NARA (Commons, domínio público) — LICENCAS-FOTOS.txt.
uso: python3 work/mg/gen.py"""
import sys
sys.path.insert(0, 'work/mg')
from parts import CSS, PANTS
T = open('work/mg/template.html').read()

F = dict(  # foto por papel (assets/mg/)
    capa='capa-ridgway.jpg', coluna='coreia-coluna-neve.jpg', congel='coreia-congelados.jpg', exaust='coreia-exaustos.jpg',
    granada='ridgway-granada-1951.jpg', antes='coreia-arroz-1950.jpg', jipe='ridgway-jipe-1951.jpg', ponte='ridgway-ponte-1951.jpg',
    bom='ridgway-retrato-1951.jpg', batalhao='coreia-avanco-1951.jpg', mapa='ridgway-oficiais-1951.jpg', seul='coreia-han-1951.jpg',
    retrato='ridgway-oficial.jpg')
OP = dict(  # object-position de cada foto (medido no snapshot)
    capa_split='60% 50%', capa='45.5% 50%', coluna='29% 50%', congel='46% 50%', exaust='21% 50%', granada='82% 40%', antes='50% 45%',
    jipe='24% 50%', ponte='44% 50%', bom='50% 30%', batalhao='26% 50%', mapa='50% 40%', seul='50% 40%', retrato='50% 25%')
def img(k, cls=''):
    return f'<img id="{{id}}" class="{cls}" src="assets/mg/{F[k]}" style="object-position:{OP.get(k, "50% 50%")}" />'
def full(id_, k, cls='', extra=''):
    return f'<div class="full" id="{id_}">' + img(k, cls).replace('{id}', id_ + 'img') + extra + '</div>'
def chip(b, n, dot, dark=True):
    rolls = {1: ('PASSO 3', 'PASSO 2', 'PASSO 1'), 2: ('PASSO 1', 'PASSO 3', 'PASSO 2'), 3: ('PASSO 2', 'PASSO 1', 'PASSO 3')}[n]
    st = ' style="top:300px;background:#fff;color:#11141A"' if dark else ' style="top:300px"'
    ps = ' style="background:#fff;color:#11141A"' if dark else ''
    return (f'<div class="chip" id="{b}-chip"{st}><span class="dot" style="background:{dot}"></span><div class="win"><div class="roll" id="{b}-roll">'
            + ''.join(f'<span>{r}</span>' for r in rolls) + f'</div></div><div class="plus" id="{b}-plus"{ps}>+</div></div>')
def title(b, l1, l2, color='#fff'):
    w = l1 + l2; n = len(w)
    sp = [f'<span id="{b}-w{k+1}">{x}</span>' for k, x in enumerate(w)]
    sel = f'<span class="sel" id="{b}-sel">{sp[-1]}<i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span>'
    return (f'<div class="title" id="{b}-title" style="top:520px;color:{color}">' + ' '.join(sp[:len(l1)]) + '<br />'
            + ' '.join(sp[len(l1):n - 1] + [sel]) + '</div>')

HTML = f'''
        <!-- A · SPLIT DA CAPA (0–2,75): CAPA GERADA A PEDIDO (Codex: general de costas na nevasca, jipe com o farol aceso) -->
        <div class="scene" id="A" style="height:845px">{full('A-capa', 'capa').replace(OP['capa'], OP['capa_split'])}</div>

        <!-- P · A CAPA ABRE EM TELA CHEIA (2,75: cobre a olhada 2,90–3,32) → PRÉ-REVELAÇÃO (5,23–9,45): soldados na neve, nada do Ridgway -->
        <div class="scene" id="P">
          {full('P-capa', 'capa')}
          {full('P-col', 'coluna', 'dim')}
          {full('P-cong', 'congel', 'dim')}
        </div>

        <!-- B · REVELAÇÃO (10,93–19,54): Ridgway com a granada no peito (1951) + nome → a parede: o bilhete e a calça de pijama rasgada -->
        <div class="scene" id="B"><div class="world dark"></div>
          {full('B-gren', 'granada', '', '<div class="mark" id="B-ring" style="left:329px;top:826px"></div>')}
          <div class="name" id="B-name" style="top:1090px"><b>MATTHEW RIDGWAY</b><i>GENERAL · EXÉRCITO DOS EUA</i></div>
          <div class="tag" id="B-gtag" style="left:480px;top:790px;background:#11141A">GRANADA</div>
          <div class="full" id="B-wall"><div class="wall"></div>
            <div class="note" id="B-note"><p id="B-n1">AO COMANDANTE DAS FORÇAS INIMIGAS,</p><p id="B-n2">COM OS CUMPRIMENTOS DO COMANDANTE DO 8º EXÉRCITO.</p>
              <div class="tack" id="B-t0" style="left:367px;top:-20px"></div></div>
            <div class="pants" id="B-pants">{PANTS}
              <div class="tack" id="B-t1" style="left:52px;top:14px"></div><div class="tack" id="B-t2" style="left:402px;top:14px"></div></div>
          </div>
        </div>

        <!-- D · PASSO 1 (24,47–37,52) → os soldados exaustos → a lista do que faltava → RESOLVIDO antes de atacar -->
        <div class="scene" id="D"><div class="world dark"><div class="band" id="D-band"></div></div>
          {chip('D', 1, '#1FB45A')}
          {title('D', ['RESOLVE'], ['A', 'LUVA.'])}
          {full('D-exa', 'exaust', 'dim')}
          <div class="req" id="D-req" style="top:250px">
            <div class="hd">8º EXÉRCITO · LINHA DE FRENTE</div>
            <div class="tt">O que falta</div>
            <div class="it" id="D-i1">LUVA<div class="pill"><span class="pr" id="D-p1a">FALTA</span><span class="pg" id="D-p1b">RESOLVIDO</span></div></div>
            <div class="it" id="D-i2">COMIDA QUENTE<div class="pill"><span class="pr" id="D-p2a">FALTA</span><span class="pg" id="D-p2b">RESOLVIDO</span></div></div>
            <div class="it" id="D-i3">ENVELOPE<div class="pill"><span class="pr" id="D-p3a">FALTA</span><span class="pg" id="D-p3b">RESOLVIDO</span></div></div>
            <div class="it later" id="D-i4">ATACAR<div class="pill"><span class="p0">DEPOIS</span></div></div>
          </div>
          {full('D-antes', 'antes', 'dim')}
        </div>

        <!-- F · PASSO 2 (42,64–52,65) → Ridgway no jipe aberto → Ridgway com a tropa no inverno -->
        <div class="scene" id="F"><div class="world dark"><div class="band" id="F-band"></div></div>
          {chip('F', 2, '#F2B705')}
          {title('F', ['APARECE'], ['NO', 'FRIO.'])}
          {full('F-jipe', 'jipe')}
          <div class="tag" id="F-3d" style="left:300px;top:1140px;background:#11141A">3 DIAS NA NEVE</div>
          {full('F-ponte', 'ponte')}
        </div>

        <!-- H · PASSO 3 (56,30–68,44) → 5.000 rostos → "bom trabalho" → o batalhão -->
        <div class="scene" id="H"><div class="world dark"><div class="band" id="H-band"></div></div>
          {chip('H', 3, '#E5322D')}
          {title('H', ['CHAMA', 'PELO'], ['NOME.'])}
          <div class="full" id="H-ctr"><div class="world dark"></div>
            <div class="ctr" style="top:380px"><span class="col"><div id="H-c1"><span>0</span><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></div></span><span class="pt">.</span><span class="col"><div id="H-c2"><span>0</span><span>7</span><span>3</span><span>9</span><span>5</span><span>0</span></div></span><span class="col"><div id="H-c3"><span>0</span><span>4</span><span>8</span><span>2</span><span>6</span><span>1</span><span>0</span></div></span><span class="col"><div id="H-c4"><span>0</span><span>9</span><span>6</span><span>3</span><span>8</span><span>5</span><span>2</span><span>0</span></div></span></div>
            <div class="lbl2" id="H-sold" style="top:720px;font-size:80px;color:#fff">SOLDADOS</div>
            <div class="lbl2" id="H-cara" style="top:850px;font-size:44px;color:#F2B705">RECONHECIDOS DE CARA</div>
          </div>
          {full('H-bom', 'bom', '', '<div class="bubble big" id="H-bub" style="left:380px;top:640px">BOM TRABALHO.</div>')}
          {full('H-bat', 'batalhao', 'dim')}
        </div>

        <!-- L · SPLIT DA VIRADA (72,29–76,51): oficiais no posto de comando + o plano de recuo -->
        <div class="scene" id="L" style="height:845px">
          {full('L-mapa', 'mapa')}
          <div class="doc" id="L-doc" style="top:640px"><span class="fi"></span>PLANO DE RECUO ↓</div>
        </div>

        <!-- N · A CONVERSA (76,51–83,50) → CLÍMAX (83,50–87,34): o exército que fugia (volta da abertura) → a contraofensiva de 1951 (tanque no rio Han, fev/1951) -->
        <div class="scene" id="N"><div class="world dark"><div class="band" id="N-band"></div></div>
          <div id="N-chat" style="position:absolute;inset:0">
            <div class="doc" id="N-doc" style="top:170px"><span class="fi"></span>PLANO DE RECUO ↓</div>
            <div class="who" id="N-wr" style="right:90px;top:360px">GEN. RIDGWAY<i style="background:#1FB45A">R</i></div>
            <div class="bubble big me" id="N-b1" style="right:90px;top:440px">O PLANO DE ATAQUE?</div>
            <div class="who" id="N-wo" style="left:90px;top:640px"><i style="background:#5A606B">?</i>OFICIAL</div>
            <div class="dots" id="N-dots" style="left:90px;top:720px"><i></i><i></i><i></i></div>
            <div class="bubble big" id="N-b2" style="left:90px;top:720px;width:720px">SENHOR, A GENTE TÁ RECUANDO.</div>
            <div class="divd" id="N-dd" style="top:1010px"><span>DIAS DEPOIS</span></div>
            <div class="stamp" data-layout-allow-overlap id="N-fora" style="left:340px;top:1110px;font-size:100px">FORA</div>
          </div>
          {full('N-ret', 'coluna', 'dim')}
          <div class="tag" id="N-3m" style="left:250px;top:1150px;background:#E5322D">MENOS DE 3 MESES</div>
          {full('N-seul', 'seul')}
          <div class="tag" id="N-seultag" style="left:220px;top:1150px;background:#11141A">1951 · A CONTRAOFENSIVA</div>
        </div>

        <!-- O · "CADÊ O PLANO DE ATAQUE?" (89,77–91,23, cobre a olhada 90,10–90,60): o próprio Ridgway encarando -->
        <div class="scene" id="O">{full('O-ret', 'retrato')}</div>
'''

JS = r'''
          gsap.set(["#P-col", "#P-cong",
                    "#B-name", "#B-ring", "#B-gtag", "#B-wall", "#B-note", "#B-n1", "#B-n2", "#B-t0", "#B-pants", "#B-t1", "#B-t2",
                    "#D-chip", "#D-w1", "#D-w2", "#D-w3", "#D-exa", "#D-req", "#D-i1", "#D-i2", "#D-i3", "#D-i4", "#D-p1b", "#D-p2b", "#D-p3b", "#D-antes",
                    "#F-chip", "#F-w1", "#F-w2", "#F-w3", "#F-jipe", "#F-3d", "#F-ponte",
                    "#H-chip", "#H-w1", "#H-w2", "#H-w3", "#H-ctr", "#H-sold", "#H-cara", "#H-bom", "#H-bub", "#H-bat",
                    "#L-doc",
                    "#N-doc", "#N-wr", "#N-b1", "#N-wo", "#N-dots", "#N-b2", "#N-dd", "#N-fora", "#N-ret", "#N-3m", "#N-seul", "#N-seultag"], { autoAlpha: 0 });
          gsap.set(["#D-sel", "#F-sel", "#H-sel"], { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set(["#D-sel .h", "#F-sel .h", "#H-sel .h"], { scale: 0 });
          gsap.set("#PJ-rasgo", { scale: 0, svgOrigin: "252 212" });
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
          kenburns("#A-capaimg", 0, 2.75, 1.0, 1.06);
          splitOut("#A", 2.75);

          // ===== P · CAPA EM TELA CHEIA → PRÉ-REVELAÇÃO (só fotos, nada do Ridgway) =====
          sceneIn("#P", 2.75);
          kenburns("#P-capaimg", 2.75, 5.23, 1.0, 1.12);
          whip("#P-capa", "#P-col", 5.23);
          kenburns("#P-colimg", 5.23, 7.4, 1.12, 1.0);
          whip("#P-col", "#P-cong", 7.4);
          kenburns("#P-congimg", 7.4, 9.7, 1.0, 1.1);
          sceneOut("#P", 9.7);

          // ===== B · REVELAÇÃO ("Matthew" 10,86 → 10,93) → A PAREDE =====
          sceneIn("#B", 10.93);
          kenburns("#B-gren", 10.93, 13.3, 1.0, 1.05);
          rise("#B-name", 11.1);
          // "granada no peito": o anel marca a granada no suspensório
          tl.fromTo("#B-ring", { scale: 1.8, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 8 * q, ease: "back.out(2)" }, Q(12.15));
          cue(12.17, "pop", -19);
          pop("#B-gtag", 12.5);
          // "pregou na parede": a parede cai, o bilhete é pregado; "de presente pro general inimigo": o texto do bilhete
          drop(["#B-gren", "#B-name", "#B-gtag"], "#B-wall", 13.46);
          tl.fromTo("#B-note", { scale: 1.6, autoAlpha: 0, rotation: -9 }, { scale: 1, autoAlpha: 1, rotation: -2.5, duration: 5 * q, ease: "power4.in" }, Q(14.1) - 5 * q);
          pop("#B-t0", 14.1, { scale: 2.2, autoAlpha: 0 }, "clique");
          cue(14.1, "impacto", -21, { dur: 0.5 });
          rise("#B-n1", 14.66);
          rise("#B-n2", 15.62);
          // "uma calça de pijama rasgada na bunda"
          tl.fromTo("#B-pants", { y: -1300, rotation: 8, autoAlpha: 1 }, { y: 0, rotation: 0, autoAlpha: 1, immediateRender: false, duration: 12 * q, ease: "back.out(1.4)" }, Q(16.89));
          cue(16.9, "whoosh", -16);
          pop("#B-t1", 17.25, { scale: 2.2, autoAlpha: 0 }, "clique");
          pop("#B-t2", 17.4, { scale: 2.2, autoAlpha: 0 }, "clique");
          tl.to("#PJ-rasgo", { scale: 1, duration: 7 * q, ease: "back.out(2.6)" }, Q(17.75));
          cue(17.76, "swish", -16); cue(17.8, "impacto", -20, { dur: 0.5 });
          tl.fromTo("#B-pants", { scale: 1 }, { scale: 1.07, duration: 8 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(18.44));
          sceneOut("#B", 19.54);

          // ===== D · PASSO 1 → OS EXAUSTOS → A LISTA → RESOLVIDO ANTES DE ATACAR =====
          sceneIn("#D", 24.47); drift("#D-band", 24.47, 37.52);
          cap("D", [24.8, 24.47, 25.19, 25.35, 26.11], 26.35, 26.81, "#D-exa");
          kenburns("#D-exaimg", 26.81, 30.41, 1.0, 1.1);
          drop(["#D-exa"], "#D-req", 30.41);
          pop("#D-i1", 30.86, { x: -60, autoAlpha: 0 });
          pop("#D-i2", 31.36, { x: -60, autoAlpha: 0 });
          pop("#D-i3", 32.5, { x: -60, autoAlpha: 0 });
          flip("#D-p1b", 34.72); flip("#D-p2b", 34.88); flip("#D-p3b", 35.04);
          pop("#D-i4", 35.5, { x: -60, autoAlpha: 0 }, "tique");
          whip("#D-req", "#D-antes", 36.1);
          kenburns("#D-antesimg", 36.1, 37.52, 1.0, 1.06);
          sceneOut("#D", 37.52);

          // ===== F · PASSO 2 → O JIPE ABERTO → O MESMO FRIO =====
          sceneIn("#F", 42.64); drift("#F-band", 42.64, 52.65);
          cap("F", [42.85, 42.64, 43.11, 43.67, 43.84], 44.05, 44.63, "#F-jipe");
          kenburns("#F-jipeimg", 44.63, 48.94, 1.0, 1.12);
          pop("#F-3d", 47.69);
          whip(["#F-jipe", "#F-3d"], "#F-ponte", 48.94);
          kenburns("#F-ponteimg", 48.94, 52.65, 1.0, 1.1);
          sceneOut("#F", 52.65);

          // ===== H · PASSO 3 → 5.000 ROSTOS → "BOM TRABALHO" → O BATALHÃO =====
          sceneIn("#H", 56.3); drift("#H-band", 56.3, 68.44);
          cap("H", [56.84, 56.3, 57.49, 57.82, 58.1], 58.3, 58.81, "#H-ctr");
          tl.fromTo("#H-c1", { y: 0, filter: "blur(5px)" }, { y: -5 * 300, filter: "blur(0px)", duration: 22 * q, ease: "power4.out" }, Q(59.6));
          tl.fromTo("#H-c2", { y: 0, filter: "blur(5px)" }, { y: -5 * 300, filter: "blur(0px)", duration: 24 * q, ease: "power4.out" }, Q(59.6));
          tl.fromTo("#H-c3", { y: 0, filter: "blur(5px)" }, { y: -6 * 300, filter: "blur(0px)", duration: 26 * q, ease: "power4.out" }, Q(59.6));
          tl.fromTo("#H-c4", { y: 0, filter: "blur(5px)" }, { y: -7 * 300, filter: "blur(0px)", duration: 28 * q, ease: "power4.out" }, Q(59.6));
          cue(59.62, "cacaniquel", -20);
          rise("#H-sold", 60.44);
          rise("#H-cara", 61.16);
          whip("#H-ctr", "#H-bom", 62.0);
          kenburns("#H-bomimg", 62.0, 65.36, 1.0, 1.1);
          pop("#H-bub", 63.88, { scale: 0.4, autoAlpha: 0, y: 40 });
          whip(["#H-bom"], "#H-bat", 65.36);
          kenburns("#H-batimg", 65.36, 68.44, 1.0, 1.1);
          sceneOut("#H", 68.44);

          // ===== L · SPLIT DA VIRADA =====
          splitIn("#L", 72.29);
          kenburns("#L-mapaimg", 72.29, 76.51, 1.0, 1.12);
          pop("#L-doc", 75.29, { y: 80, autoAlpha: 0 });
          splitOut("#L", 76.51);

          // ===== N · A CONVERSA → CLÍMAX =====
          sceneIn("#N", 76.51); drift("#N-band", 76.51, 83.5);
          rise("#N-doc", 76.6);
          rise("#N-wr", 76.75);
          pop("#N-b1", 77.22, { scale: 0.5, autoAlpha: 0, y: 30 });
          rise("#N-wo", 78.45);
          pop("#N-dots", 78.65, { scale: 0.5, autoAlpha: 0 });
          tl.to("#N-dots i", { y: -14, duration: 4 * q, ease: "power1.inOut", stagger: 2 * q, yoyo: true, repeat: 3 }, Q(78.8));
          tl.to("#N-dots", { autoAlpha: 0, duration: 2 * q }, Q(79.4) - 2 * q);
          pop("#N-b2", 79.4, { scale: 0.5, autoAlpha: 0, y: 30 });
          rise("#N-dd", 81.3);
          tl.to(["#N-wo", "#N-b2"], { opacity: 0.35, duration: 6 * q }, Q(82.5));
          slam("#N-fora", 82.63, -6);
          // CLÍMAX: o mesmo exército que fugia (volta da abertura) → retomou a capital
          drop(["#N-chat"], "#N-ret", 83.5);
          kenburns("#N-retimg", 83.5, 86.04, 1.0, 1.1);
          pop("#N-3m", 83.98);
          whip(["#N-ret", "#N-3m"], "#N-seul", 86.04);
          kenburns("#N-seulimg", 86.04, 87.34, 1.08, 1.0);
          pop("#N-seultag", 86.34);
          sceneOut("#N", 87.34);

          // ===== O · "CADÊ O PLANO DE ATAQUE?" =====
          sceneIn("#O", 89.77);
          kenburns("#O-retimg", 89.77, 91.23, 1.12, 1.0);
          sceneOut("#O", 91.23);
'''

T = T.replace('            </style>', CSS + '            </style>', 1)
i = T.index('-->', T.index('CENAS (por video)')) + 3
T = T[:i] + HTML + T[i:]
T = T.replace('          // (vazio = camada transparente)', JS, 1)
open('compositions/mg.html', 'w').write(T)
print('compositions/mg.html', len(T), 'bytes')
