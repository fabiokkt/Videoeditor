"""POR VIDEO — reel GENE KRANZ. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Tempos absolutos de work/tl-words.txt (janelas em work/mg/tempos.py).
Dosagem (docs/05 §24): abertura só com fotos (capa gerada + a sala de controle + o time da Apollo 13, nada do rosto do Kranz antes de
"Gene"); no corpo foto real é o padrão (NASA, domínio público); motion só nos capítulos (PASSO 1/2/3), no objeto que a fala nomeia e não
existe em foto (a semana com a sexta prometida; os avisos do time = 0; a ordem DESCOBRE → MEXE) e no mecanismo da virada (os problemas
VISTOS que ninguém parou) (~30% da cobertura). A capa é gerada a pedido (Codex). Fotos: LICENCAS-FOTOS.txt.
uso: python3 work/mg/gen.py"""
import sys
sys.path.insert(0, 'work/mg')
from parts import CSS
from tempos import T
TPL = open('work/mg/template.html').read()

F = dict(  # foto por papel (assets/mg/, preparadas por work/mg/fotos.py)
    capa='capa-gene-kranz.jpg', sala65='sala-gemini-1965.jpg', time1='time-apollo13-console-1970.jpg', time2='time-apollo13-monitor-1970.jpg',
    colete='kranz-colete-1972.jpg', sala11='sala-apollo11-1969.jpg', lua='aldrin-lua-1969.jpg',
    fab='nave-012-fabrica-1967.jpg', pad='nave-012-pad34-1967.jpg', k65='kranz-console-1965.jpg', crise='crise-apollo13-1970.jpg',
    k66='kranz-imprensa-1966.jpg', apollo1='tripulacao-apollo1-1966.jpg', sm='modulo-servico-apollo13-1970.jpg',
    sala13='sala-apollo13-kranz-costas-1970.jpg', viva='tripulacao-apollo13-viva-1970.jpg')
OP = dict(  # object-position de cada foto (medido no snapshot)
    capa_split='50% 50%', sala65_split='50% 45%', capa_b='50% 30%', time1='45% 50%', time2='42% 50%', colete='62% 50%', sala11='50% 50%',
    lua='45% 50%', fab='50% 40%', pad='50% 22%', pad_n='50% 30%', k65='18% 50%', crise='30% 50%', k66_split='10% 30%', k66='39% 40%',
    viva='50% 45%')
def img(k, op=None, cls=''):
    return f'<img id="{{id}}" class="{cls}" src="assets/mg/{F[k]}" style="object-position:{op or OP.get(k, "50% 50%")}" />'
def full(id_, k, op=None, cls='', extra=''):
    return f'<div class="full" id="{id_}">' + img(k, op, cls).replace('{id}', id_ + 'img') + extra + '</div>'
def fit(id_, k, top, h, extra=''):   # foto inteira na largura da tela sobre ela mesma desfocada
    return (f'<div class="full" id="{id_}"><div class="world dark"></div><img class="bgblur" src="assets/mg/{F[k]}" />'
            f'<div class="fitimg" id="{id_}fit" style="top:{top}px;height:{h}px"><img src="assets/mg/{F[k]}" />{extra}</div></div>')
def chip(b, n, dot):
    rolls = {1: ('PASSO 3', 'PASSO 2', 'PASSO 1'), 2: ('PASSO 1', 'PASSO 3', 'PASSO 2'), 3: ('PASSO 2', 'PASSO 1', 'PASSO 3')}[n]
    return (f'<div class="chip" id="{b}-chip" style="top:300px;background:#fff;color:#11141A"><span class="dot" style="background:{dot}"></span>'
            f'<div class="win"><div class="roll" id="{b}-roll">' + ''.join(f'<span>{r}</span>' for r in rolls)
            + f'</div></div><div class="plus" id="{b}-plus" style="background:#fff;color:#11141A">+</div></div>')
def title(b, l1, l2, size=112):
    w = l1 + l2; n = len(w)
    sp = [f'<span id="{b}-w{k+1}">{x}</span>' for k, x in enumerate(w)]
    sel = f'<span class="sel" id="{b}-sel">{sp[-1]}<i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span>'
    return (f'<div class="title" id="{b}-title" style="top:520px;color:#fff;font-size:{size}px">' + ' '.join(sp[:len(l1)]) + '<br />'
            + ' '.join(sp[len(l1):n - 1] + [sel]) + '</div>')
def day(b, k, nome, num, hot=False):
    extra = ''
    if hot:
        extra = (f'<div class="d hot" id="{b}-hot" style="position:absolute;left:0;top:0"><b>{nome}</b><i>{num}</i></div>'
                 f'<div class="ring2" id="{b}-ring"></div><div class="x" id="{b}-x1"></div><div class="x" id="{b}-x2"></div>')
    return f'<div class="d" id="{b}-d{k}"><b>{nome}</b><i>{num}</i>{extra}</div>'
SEMANA = ''.join(day('D', k + 1, n, d, k == 4) for k, (n, d) in enumerate([('SEG', 13), ('TER', 14), ('QUA', 15), ('QUI', 16), ('SEX', 17)]))

HTML = f'''
        <!-- A · SPLIT DA CAPA (0–4,86, o gancho inteiro): CAPA GERADA A PEDIDO (Codex: homem de costas, colete branco, sala de controle no escuro,
             alarme vermelho) → "e mais temidos": a sala de controle de Houston em 1965 (sem logo) -->
        <div class="scene" id="A" style="height:845px"><div class="world dark"></div>
          {full('A-capa', 'capa', OP['capa_split'])}
          {full('A-sala', 'sala65', OP['sala65_split'])}
        </div>

        <!-- P · PRÉ-REVELAÇÃO (4,86–9,38): o time da Apollo 13 em volta do console → controladores e astronautas no console (nada do rosto do Kranz) -->
        <div class="scene" id="P"><div class="world dark"></div>
          {full('P-t1', 'time1', None, 'bw')}
          {full('P-t2', 'time2', None, 'bw')}
        </div>

        <!-- B · REVELAÇÃO (10,36–18,37): a capa de costas (cobre a olhada) → "Gene" (10,85 + 2 quadros): Kranz de colete branco no console (1972)
             + nome + anel no colete → "e comandava a sala": a sala da Apollo 11 → "pousou na Lua": Aldrin na Lua -->
        <div class="scene" id="B"><div class="world dark"></div>
          {full('B-capa', 'capa', OP['capa_b'])}
          {full('B-ret', 'colete', None, 'bw', '<div class="mark" id="B-ring" style="left:900px;top:1300px"></div>')}
          <div class="name" id="B-name" style="top:150px"><b>GENE KRANZ</b><i>DIRETOR DE VOO DA NASA</i></div>
          {full('B-sala', 'sala11', None, 'dim', '<div class="floor"></div>')}
          <div class="tag" id="B-a11" style="left:90px;top:1180px;background:#11141A">HOUSTON · APOLLO 11 · 1969</div>
          {full('B-lua', 'lua', None, '', '<div class="floor"></div>')}
          <div class="tag" id="B-data" style="left:90px;top:1180px;background:#11141A">20 DE JULHO DE 1969</div>
        </div>

        <!-- D · PASSO 1 (22,50–34,80) → a nave da Apollo 1 na montagem (jan/1967) → içada no Pad 34 → a semana com a sexta prometida (NÃO DÁ) -->
        <div class="scene" id="D"><div class="world dark"><div class="band" id="D-band"></div></div>
          {chip('D', 1, '#1FB45A')}
          {title('D', ['PRESSA', 'NÃO'], ['É', 'DESCULPA.'])}
          {full('D-fab', 'fab', None, 'cold', '<div class="vig"></div>')}
          <div class="tag" id="D-1967" style="left:90px;top:1180px;background:#11141A">JANEIRO DE 1967 · NO PRAZO</div>
          {full('D-pad', 'pad', None, 'cold', '<div class="vig"></div>')}
          <div class="wk" id="D-wk" style="top:330px">
            <div class="hd">SUA SEMANA</div><div class="tt">Prazo da entrega</div>
            <div class="days">{SEMANA}</div>
          </div>
          <div class="tag" id="D-ent" style="left:90px;top:850px;background:#F2B705;color:#11141A">ENTREGA</div>
          <div class="tag" id="D-nao" style="left:90px;top:950px;background:#E5322D">NÃO DÁ</div>
        </div>

        <!-- F · PASSO 2 (36,62–46,75) → Kranz no console (1965) + O QUE VOCÊ FAZ / O QUE DEIXA DE FAZER → os avisos do time: 0 -->
        <div class="scene" id="F"><div class="world dark"><div class="band" id="F-band"></div></div>
          {chip('F', 2, '#F2B705')}
          {title('F', ['FICAR', 'QUIETO'], ['TAMBÉM', 'É', 'ERRO.'], 100)}
          {full('F-k65', 'k65', None, 'bw', '<div class="vig"></div>')}
          <div class="tag" id="F-faz" style="left:90px;top:1080px;background:#1FB45A">O QUE VOCÊ FAZ</div>
          <div class="tag" id="F-deixa" style="left:90px;top:1190px;background:#E5322D">O QUE DEIXA DE FAZER</div>
          <div class="inbox" id="F-inb" style="top:330px">
            <div class="hd"><span>AVISOS DO SEU TIME</span><span>HOJE</span></div>
            <div class="n" id="F-n">0</div>
            <div class="z" id="F-z">ninguém te avisou de nada</div>
          </div>
        </div>

        <!-- H · PASSO 3 (49,25–58,20) → a sala no último dia da Apollo 13 + a fala do Kranz → a ordem: 1 DESCOBRE, 2 MEXE, CHUTAR NUNCA -->
        <div class="scene" id="H"><div class="world dark"><div class="band" id="H-band"></div></div>
          {chip('H', 3, '#E5322D')}
          {title('H', ['NÃO'], ['CHUTA.'])}
          {full('H-cri', 'crise', None, 'bw', '<div class="floor"></div>')}
          <div class="tag" id="H-a13" style="left:90px;top:1180px;background:#11141A">APOLLO 13 · ABRIL DE 1970</div>
          <div class="who" id="H-who" style="left:90px;top:250px"><i style="background:#F2B705">G</i>GENE KRANZ</div>
          <div class="bubble big" id="H-bub" style="left:90px;top:340px;width:820px">VAMOS RESOLVER, MAS SEM PIORAR CHUTANDO.</div>
          <div class="req" id="H-req" style="top:300px">
            <div class="hd">DEU PROBLEMA</div>
            <div class="tt">A ordem</div>
            <div class="it" id="H-i1">1 · DESCOBRE<div class="pill"><span class="pg" id="H-p1">PRIMEIRO</span></div></div>
            <div class="it" id="H-i2">2 · MEXE<div class="pill"><span class="py" id="H-p2">DEPOIS</span></div></div>
            <div class="it later" id="H-i3">CHUTAR<div class="pill"><span class="pr" id="H-p3">NUNCA</span></div></div>
          </div>
        </div>

        <!-- L · SPLIT DA VIRADA (61,64–62,80): Kranz na mesa de imprensa (1966) -->
        <div class="scene" id="L" style="height:845px"><div class="world dark"></div>
          {full('L-k66', 'k66', OP['k66_split'], 'bw')}
        </div>

        <!-- N · A VIRADA (62,80–72,72): a mesma foto abre em tela cheia (cobre a olhada) → "Em 1967": a tripulação da Apollo 1 → "teste no chão":
             a nave no Pad 34 → "Todo mundo via problema. Ninguém parou.": VISTO, VISTO, VISTO · ALGUÉM PAROU? NINGUÉM -->
        <div class="scene" id="N"><div class="world dark"></div>
          {full('N-k66', 'k66', None, 'bw', '<div class="vig"></div>')}
          {fit('N-a1', 'apollo1', 300, 864)}
          <div class="tag" id="N-a1t" style="left:90px;top:1200px;background:#11141A">APOLLO 1 · JANEIRO DE 1967</div>
          {full('N-pad', 'pad', OP['pad_n'], 'bw', '<div class="vig"></div>')}
          <div class="tag" id="N-padt" style="left:90px;top:1200px;background:#11141A">TESTE NO CHÃO · PAD 34</div>
          <div class="full" id="N-lst"><div class="world dark"></div>
            <div class="req" style="top:300px">
              <div class="hd">APOLLO 1 · TODO DIA</div>
              <div class="tt">Problemas</div>
              <div class="it" id="N-i1">PROBLEMA<div class="pill"><span class="py">VISTO</span></div></div>
              <div class="it" id="N-i2">PROBLEMA<div class="pill"><span class="py">VISTO</span></div></div>
              <div class="it" id="N-i3">PROBLEMA<div class="pill"><span class="py">VISTO</span></div></div>
              <div class="it" id="N-i4">ALGUÉM PAROU?<div class="pill"><span class="pr" id="N-p4">NINGUÉM</span></div></div>
            </div>
          </div>
        </div>

        <!-- C · CLÍMAX (78,62–86,14): o módulo de serviço da Apollo 13 sem o painel (anel no rombo) → "Mesma sala, mesmo chefe": Kranz de costas
             na sala da Apollo 13 (13 abr 1970; anel nele) → "Os três voltaram vivos": a tripulação no USS Iwo Jima -->
        <div class="scene" id="C"><div class="world dark"></div>
          {fit('C-sm', 'sm', 330, 676, '<div class="mark" id="C-ring1" style="left:507px;top:433px;width:300px;height:300px;margin:-150px 0 0 -150px"></div>')}
          <div class="tag" id="C-a13" style="left:90px;top:1080px;background:#E5322D">APOLLO 13 · ABRIL DE 1970</div>
          {fit('C-sala', 'sala13', 300, 730, '<div class="mark" id="C-ring2" style="left:675px;top:493px"></div>')}
          <div class="tag" id="C-mesma" style="left:90px;top:1080px;background:#11141A">MESMA SALA</div>
          <div class="tag" id="C-chefe" style="left:90px;top:1180px;background:#F2B705;color:#11141A">MESMO CHEFE · GENE KRANZ</div>
          {full('C-viva', 'viva', None, '', '<div class="floor"></div>')}
          <div class="tag" id="C-data" style="left:90px;top:1180px;background:#1FB45A">17 DE ABRIL DE 1970 · USS IWO JIMA</div>
        </div>
'''

JS = r'''
          gsap.set(["#A-sala", "#P-t2",
                    "#B-ret", "#B-ring", "#B-name", "#B-sala", "#B-a11", "#B-lua", "#B-data",
                    "#D-chip", "#D-w1", "#D-w2", "#D-w3", "#D-w4", "#D-fab", "#D-1967", "#D-pad", "#D-wk",
                    "#D-d1", "#D-d2", "#D-d3", "#D-d4", "#D-d5", "#D-hot", "#D-ring", "#D-x1", "#D-x2", "#D-ent", "#D-nao",
                    "#F-chip", "#F-w1", "#F-w2", "#F-w3", "#F-w4", "#F-w5", "#F-k65", "#F-faz", "#F-deixa", "#F-inb", "#F-n", "#F-z",
                    "#H-chip", "#H-w1", "#H-w2", "#H-cri", "#H-a13", "#H-who", "#H-bub", "#H-req", "#H-i1", "#H-i2", "#H-i3", "#H-p1", "#H-p2", "#H-p3",
                    "#N-a1", "#N-a1t", "#N-pad", "#N-padt", "#N-lst", "#N-i1", "#N-i2", "#N-i3", "#N-i4", "#N-p4",
                    "#C-a13", "#C-ring1", "#C-sala", "#C-ring2", "#C-mesma", "#C-chefe", "#C-viva", "#C-data"], { autoAlpha: 0 });
          gsap.set(["#D-sel", "#F-sel", "#H-sel"], { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set(["#D-sel .h", "#F-sel .h", "#H-sel .h"], { scale: 0 });
          gsap.set("#D-x1", { rotation: 45, scaleX: 0 }); gsap.set("#D-x2", { rotation: -45, scaleX: 0 });
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
          function ring(id, t) {
            tl.fromTo(id, { scale: 2.2, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 8 * q, ease: "back.out(1.8)" }, Q(t));
            cue(t + 0.05, "swish", -20);
          }

          // ===== A · CAPA (quadro 0 = capa) =====
          splitIn("#A", T.A0, true);
          kenburns("#A-capaimg", T.A0, 2.38, 1.0, 1.06);
          // "e mais temidos": a sala de controle de Houston (Gemini 4, 1965)
          whip("#A-capa", "#A-sala", 2.38);
          kenburns("#A-salaimg", 2.38, T.A1, 1.0, 1.08);
          splitOut("#A", T.A1);

          // ===== P · PRÉ-REVELAÇÃO (só fotos: o time; nada do rosto do Kranz) =====
          sceneIn("#P", T.P0);
          kenburns("#P-t1img", T.P0, 7.18, 1.1, 1.0);
          // "o seu time"
          whip("#P-t1", "#P-t2", 7.18);
          kenburns("#P-t2img", 7.18, T.P1, 1.0, 1.08);
          sceneOut("#P", T.P1);

          // ===== B · REVELAÇÃO ("Gene" 10,85 → 10,92) =====
          sceneIn("#B", T.B0);
          kenburns("#B-capaimg", T.B0, 10.92, 1.12, 1.2);
          whip("#B-capa", "#B-ret", 10.92);
          kenburns("#B-ret", 10.92, 14.94, 1.0, 1.06);
          rise("#B-name", 11.1);
          // "colete branco"
          ring("#B-ring", 12.39);
          // "e comandava a sala"
          whip(["#B-ret", "#B-name"], "#B-sala", 14.94);
          kenburns("#B-salaimg", 14.94, 17.09, 1.0, 1.08);
          pop("#B-a11", 15.3);
          // "pousou na Lua"
          whip(["#B-sala", "#B-a11"], "#B-lua", 17.09);
          kenburns("#B-luaimg", 17.09, T.B1, 1.08, 1.0);
          pop("#B-data", 17.5);
          sceneOut("#B", T.B1);

          // ===== D · PASSO 1 → A NAVE DA APOLLO 1 → A SEMANA =====
          sceneIn("#D", T.D0); drift("#D-band", T.D0, T.D1);
          cap("D", [22.72, T.D0, 23.27, 23.76, 23.96, 24.06], 24.35, 25.18, "#D-fab");
          kenburns("#D-fabimg", 25.18, 27.73, 1.0, 1.08);
          pop("#D-1967", 26.17);
          // "que parou de ver os problemas de todo dia"
          whip(["#D-fab", "#D-1967"], "#D-pad", 27.73);
          kenburns("#D-padimg", 27.73, 30.34, 1.08, 1.0);
          // "Você promete entrega pra sexta sabendo que não dá, e reza."
          drop(["#D-pad"], "#D-wk", 30.34);
          stagger(["#D-d1", "#D-d2", "#D-d3", "#D-d4", "#D-d5"], 30.4, 5, 2);
          pop("#D-ent", 30.82);
          flip("#D-hot", 31.55);
          tl.fromTo("#D-ring", { scale: 1.6, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 7 * q, ease: "back.out(2)" }, Q(32.5));
          tl.to(["#D-x1", "#D-x2"], { autoAlpha: 1, scaleX: 1, duration: 5 * q, ease: "power3.out", stagger: 2 * q }, Q(32.6));
          cue(32.55, "impacto", -21, { dur: 0.5 });
          pop("#D-nao", 32.68);
          tl.fromTo("#D-wk", { rotation: 0 }, { rotation: -2, duration: 1.2, ease: "power2.out" }, Q(33.13));
          sceneOut("#D", T.D1);

          // ===== F · PASSO 2 → KRANZ NO CONSOLE → OS AVISOS DO TIME =====
          sceneIn("#F", T.F0); drift("#F-band", T.F0, T.F1);
          cap("F", [36.85, T.F0, 37.68, 37.99, 38.48, 38.95, 39.03], 39.3, 39.66, "#F-k65");
          kenburns("#F-k65img", 39.66, 44.9, 1.0, 1.1);
          pop("#F-faz", 42.45);
          pop("#F-deixa", 43.61);
          // "Ninguém no seu time te avisa de nada?"
          drop(["#F-k65", "#F-faz", "#F-deixa"], "#F-inb", 44.9);
          pop("#F-n", 45.52, { scale: 0.3, autoAlpha: 0 }, "clique");
          rise("#F-z", 46.08);
          sceneOut("#F", T.F1);

          // ===== H · PASSO 3 → A SALA NA CRISE + A FALA → A ORDEM =====
          sceneIn("#H", T.H0); drift("#H-band", T.H0, T.H1);
          cap("H", [49.6, T.H0, 50.04, 50.21], 50.45, 51.07, "#H-cri");
          kenburns("#H-criimg", 51.07, 55.57, 1.0, 1.08);
          pop("#H-a13", 51.36);
          // "ele falou: vamos resolver, mas sem piorar chutando"
          rise("#H-who", 51.82);
          pop("#H-bub", 52.06, { scale: 0.5, autoAlpha: 0, y: 30 });
          // "Primeiro descobre o que aconteceu, depois mexe."
          drop(["#H-cri", "#H-a13", "#H-who", "#H-bub"], "#H-req", 55.57);
          pop("#H-i1", 55.75, { x: -60, autoAlpha: 0 }); flip("#H-p1", 56.36);
          pop("#H-i2", 56.93, { x: -60, autoAlpha: 0 }); flip("#H-p2", 57.46);
          pop("#H-i3", 57.75, { x: -60, autoAlpha: 0 }, "tique"); flip("#H-p3", 57.9);
          sceneOut("#H", T.H1);

          // ===== L · SPLIT DA VIRADA =====
          splitIn("#L", T.L0);
          kenburns("#L-k66img", T.L0, T.L1, 1.0, 1.06);
          splitOut("#L", T.L1);

          // ===== N · A VIRADA EM TELA CHEIA =====
          sceneIn("#N", T.N0);
          kenburns("#N-k66img", T.N0, 64.22, 1.06, 1.12);
          // "Em 1967, três astronautas morreram"
          whip("#N-k66", "#N-a1", 64.22);
          kenburns("#N-a1fit", 64.22, 68.2, 1.0, 1.05);
          pop("#N-a1t", 65.11);
          // "num teste no chão"
          whip(["#N-a1", "#N-a1t"], "#N-pad", 68.2);
          kenburns("#N-padimg", 68.2, 70.03, 1.0, 1.08);
          pop("#N-padt", 68.46);
          // "Todo mundo via problema. Ninguém parou."
          drop(["#N-pad", "#N-padt"], "#N-lst", 70.03);
          pop("#N-i1", 70.3, { x: -60, autoAlpha: 0 }, "tique");
          pop("#N-i2", 70.48, { x: -60, autoAlpha: 0 }, "tique");
          pop("#N-i3", 70.66, { x: -60, autoAlpha: 0 }, "tique");
          pop("#N-i4", 70.95, { x: -60, autoAlpha: 0 });
          flip("#N-p4", 71.23);
          cue(71.25, "impacto", -21, { dur: 0.5 });
          sceneOut("#N", T.N1);

          // ===== C · CLÍMAX: A APOLLO 13 =====
          sceneIn("#C", T.C0);
          kenburns("#C-smfit", T.C0, 82.09, 1.0, 1.06);
          pop("#C-a13", 79.0);
          // "explodiu"
          ring("#C-ring1", 80.01);
          cue(80.05, "impacto", -19, { dur: 0.8 });
          // "Mesma sala, mesmo chefe."
          whip(["#C-sm", "#C-a13"], "#C-sala", 82.09);
          kenburns("#C-salafit", 82.09, 84.17, 1.0, 1.05);
          pop("#C-mesma", 82.4);
          ring("#C-ring2", 82.99);
          pop("#C-chefe", 83.4);
          // "Os três voltaram vivos."
          whip(["#C-sala", "#C-mesma", "#C-chefe"], "#C-viva", 84.17);
          kenburns("#C-vivaimg", 84.17, T.C1, 1.0, 1.06);
          pop("#C-data", 84.55);
          sceneOut("#C", T.C1);
'''
JS = '          var T = ' + str({k: v for k, v in T.items()}).replace("'", '"') + ';\n' + JS

out = TPL.replace('            </style>', CSS + '            </style>', 1)
i = out.index('-->', out.index('CENAS (por video)')) + 3
out = out[:i] + HTML + out[i:]
out = out.replace('          // (vazio = camada transparente)', JS, 1)
open('compositions/mg.html', 'w').write(out)
print('compositions/mg.html', len(out), 'bytes')
