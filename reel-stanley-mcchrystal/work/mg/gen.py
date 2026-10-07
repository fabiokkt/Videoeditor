"""POR VIDEO — reel STANLEY McCHRYSTAL. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Tempos absolutos de work/tl-words.txt.
Dosagem (docs/05 §24): abertura só com fotos (capa gerada + visão noturna no Iraque); no corpo foto real é o padrão; motion só nos
capítulos (PASSO 1/2/3), no objeto que a fala nomeia e não existe em foto (as lanchonetes proibidas; o quartinho com os sacos), nos números
(7.000 pessoas por dia; 18 -> 300+ operações por mês) e na frase dele (saber tudo, o tempo todo) (~40% da cobertura).
Fotos: Exército / DoD dos EUA (Commons, domínio público) — LICENCAS-FOTOS.txt.
uso: python3 work/mg/gen.py"""
import sys
sys.path.insert(0, 'work/mg')
from parts import CSS, grid, sacks
T = open('work/mg/template.html').read()

F = dict(  # foto por papel (assets/mg/)
    capa='capa-stanley.jpg', nv1='pre-visao-noturna-helicoptero.jpg', nv2='iraque-visao-noturna-soldado.jpg',
    r2003='stanley-2003.jpg', aviao='stanley-aviao-2010.jpg', toc='sala-de-operacoes.jpg', muro='iraque-visao-noturna-muro.jpg',
    roda='time-em-roda.jpg', afeg='stanley-soldados-afegaos-2010.jpg', estrelas='stanley-4-estrelas.jpg',
    raid='iraque-incursao-noturna.jpg', raid2='incursao-noturna-2.jpg', flynn='stanley-flynn-2010.jpg')
OP = dict(  # object-position de cada foto (medido no snapshot)
    capa_split='46% 50%', capa_l='70% 40%', nv1='50% 50%', nv2='50% 40%', r2003='50% 30%', aviao='18% 50%', toc='40% 50%', muro='50% 50%',
    roda='50% 50%', afeg='58% 50%', estrelas='50% 20%', raid='42% 50%', raid2='50% 50%', flynn='38% 40%')
def img(k, cls='', op=None, extra=''):
    return f'<img id="{{id}}" class="{cls}" src="assets/mg/{F[k]}" style="object-position:{op or OP.get(k, "50% 50%")}{extra}" />'
def full(id_, k, cls='', inner='', op=None, extra=''):
    return f'<div class="full" id="{id_}">' + img(k, cls, op, extra).replace('{id}', id_ + 'img') + inner + '</div>'
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
def roll(id_, seq, cls='col'):
    return f'<span class="{cls}"><div id="{id_}">' + ''.join(f'<span>{d}</span>' for d in seq) + '</div></span>'

GRID, GRID_ORDER = grid()
SACKS, SACK_IDS = sacks()

HTML = f'''
        <!-- A · SPLIT DA CAPA (0–5,19, o gancho inteiro): CAPA GERADA A PEDIDO (Codex: general de costas no corredor, visão noturna, o quartinho dos sacos) -->
        <div class="scene" id="A" style="height:845px">{full('A-capa', 'capa', op=OP['capa_split'])}</div>

        <!-- P · PRÉ-REVELAÇÃO (5,19–10,45): visão noturna no Iraque, nada do Stanley -->
        <div class="scene" id="P"><div class="world dark"></div>
          {full('P-nv1', 'nv1', 'nvd')}
          {full('P-nv2', 'nv2')}
        </div>

        <!-- B · REVELAÇÃO ("Stanley" 11,74 → 11,81): retrato de 2003 + nome → no avião com o laptop → as lanchonetes da base: PROIBIDO -->
        <div class="scene" id="B"><div class="world dark"><div class="band" id="B-band"></div></div>
          {full('B-por', 'r2003')}
          <div class="name" id="B-name" style="top:1040px"><b>STANLEY McCHRYSTAL</b><i>GENERAL · EXÉRCITO DOS EUA</i></div>
          <div class="tag" id="B-fe" style="left:90px;top:1236px;background:#11141A">FORÇAS ESPECIAIS · IRAQUE</div>
          {full('B-avi', 'aviao', 'bw')}
          <div class="tag" id="B-sono" style="left:90px;top:1060px;background:#11141A">4 HORAS DE SONO</div>
          <div class="tag" id="B-ref" style="left:90px;top:1170px;background:#11141A">1 REFEIÇÃO POR DIA</div>
          <div class="req" id="B-req" style="top:470px">
            <div class="hd">BASE MILITAR · PRAÇA DE ALIMENTAÇÃO</div>
            <div class="tt">Lanchonetes</div>
            <div class="it" id="B-i1">BURGER KING<div class="pill"><span class="pg" id="B-p1a">ABERTO</span><span class="pr" id="B-p1b">PROIBIDO</span></div></div>
            <div class="it" id="B-i2">PIZZA HUT<div class="pill"><span class="pg" id="B-p2a">ABERTO</span><span class="pr" id="B-p2b">PROIBIDO</span></div></div>
            <div class="it" id="B-i3">SUBWAY<div class="pill"><span class="pg" id="B-p3a">ABERTO</span><span class="pr" id="B-p3b">PROIBIDO</span></div></div>
          </div>
        </div>

        <!-- D · PASSO 1 (27,45–37,63) → a reunião diária: grade de telas + 7.000 → dois times separados + PERDE -->
        <div class="scene" id="D"><div class="world dark"><div class="band" id="D-band"></div></div>
          {chip('D', 1, '#1FB45A')}
          {title('D', ['NA', 'MESMA'], ['REUNIÃO.'])}
          <div class="full" id="D-grid"><div class="world dark"></div>
            <div class="grid" style="top:200px">{GRID}</div>
            <div class="shade" style="top:230px"></div>
            <div class="big" id="D-num" style="top:440px">{roll('D-c1', '0369147')}<span class="pt">.</span>{roll('D-c2', '0730')}{roll('D-c3', '05820')}{roll('D-c4', '096380')}</div>
            <div class="lbl2" id="D-pes" style="top:720px;font-size:72px">PESSOAS</div>
            <div class="tag" id="D-dia" style="left:270px;top:1180px;background:#1FB45A">1 REUNIÃO POR DIA</div>
          </div>
          <div class="full" id="D-sep"><div class="world dark"></div>
            <div class="card" id="D-ca" style="left:50px;top:250px;width:470px;height:820px">{img('toc').replace('{id}', 'D-caimg')}<div class="ccap">TIME 1</div></div>
            <div class="card" id="D-cb" style="left:560px;top:250px;width:470px;height:820px">{img('muro').replace('{id}', 'D-cbimg')}<div class="ccap">TIME 2</div></div>
            <div class="stamp" data-layout-allow-overlap id="D-perde" style="left:290px;top:560px">PERDE</div>
          </div>
        </div>

        <!-- F · PASSO 2 (41,40–51,55) → um time em roda (6 MESES NO OUTRO TIME) → Stanley agachado com soldados afegãos -->
        <div class="scene" id="F"><div class="world dark"><div class="band" id="F-band"></div></div>
          {chip('F', 2, '#F2B705')}
          {title('F', ['EMPRESTA'], ['O', 'MELHOR.'])}
          {full('F-roda', 'roda', 'dim', '<div class="floor"></div>')}
          <div class="tag" id="F-mel" style="left:90px;top:1060px;background:#11141A">OS MELHORES</div>
          <div class="tag" id="F-6m" style="left:90px;top:1170px;background:#F2B705;color:#11141A">6 MESES NO OUTRO TIME</div>
          {full('F-afg', 'afeg', 'dim', '<div class="floor"></div>')}
        </div>

        <!-- H · PASSO 3 (56,70–63,01) → retrato de 4 estrelas + a frase dele -->
        <div class="scene" id="H"><div class="world dark"><div class="band" id="H-band"></div></div>
          {chip('H', 3, '#E5322D')}
          {title('H', ['ABRE'], ['TUDO.'])}
          {full('H-por', 'estrelas', 'dim')}
          <div class="quote" id="H-q" style="top:880px"><span class="qm">“</span>
            <p><span id="H-q1">A META É</span> <span id="H-q2">TODO MUNDO</span> <span id="H-q3">SABER TUDO,</span> <span id="H-q4">O TEMPO TODO.</span></p>
            <i id="H-qa">STANLEY McCHRYSTAL</i></div>
        </div>

        <!-- L · SPLIT DA VIRADA (67,63–69,70): a capa de volta, a câmera entra na porta do quartinho -->
        <div class="scene" id="L" style="height:845px">{full('L-capa', 'capa', op=OP['capa_l'], extra=';transform-origin:72% 30%')}</div>

        <!-- N · A VIRADA (69,70–84,40): incursão noturna → o quartinho (os sacos que ninguém lia) → soldado + analista → CLÍMAX 18 → 300+ -->
        <div class="scene" id="N"><div class="world dark"></div>
          {full('N-raid', 'raid', 'nvb')}
          {full('N-raid2', 'raid2', 'nvb')}
          <div class="full" id="N-room"><div class="room"></div><div class="wire"></div><div class="bulb" id="N-bulb"></div>
            {SACKS}
            <div class="stamp" data-layout-allow-overlap id="N-lia" style="left:75px;top:330px;font-size:104px">NINGUÉM LIA</div>
          </div>
          <div class="full" id="N-mesa"><div class="world dark"></div>
            <div class="card" id="N-mcard" style="left:30px;top:330px;width:1020px;height:678px">{img('flynn', op='50% 50%').replace('{id}', 'N-mesaimg')}</div>
          </div>
          <div class="tag" id="N-sa" style="left:255px;top:1070px;background:#1FB45A">SOLDADO + ANALISTA</div>
          <div class="full" id="N-ops"><div class="world dark"><div class="band" id="N-band"></div></div>
            <div class="ops" style="top:380px">
              <div class="bar b1" id="N-b1"></div><div class="bar b2" id="N-b2"></div>
              <div class="v" id="N-v1" style="left:40px;top:530px">{roll('N-v1c1', '1')}{roll('N-v1c2', '8')}</div>
              <div class="v" id="N-v2" style="left:450px;width:440px;top:-200px">{roll('N-c1', '0123')}{roll('N-c2', '0740')}{roll('N-c3', '05820')}<span class="plus" id="N-plus">+</span></div>
              <div class="k" style="left:40px">ANTES</div><div class="k" style="left:520px">DEPOIS</div>
            </div>
            <div class="lbl2" id="N-lbl" style="top:1250px;font-size:44px;color:#2BE07A">OPERAÇÕES POR MÊS</div>
          </div>
        </div>
'''

GO = ', '.join(f'"{x}"' for x in GRID_ORDER)
SK = ', '.join(f'"{x}"' for x in SACK_IDS)
JS = r'''
          gsap.set(["#P-nv2",
                    "#B-name", "#B-fe", "#B-avi", "#B-sono", "#B-ref", "#B-req", "#B-i1", "#B-i2", "#B-i3", "#B-p1b", "#B-p2b", "#B-p3b",
                    "#D-chip", "#D-w1", "#D-w2", "#D-w3", "#D-grid", "#D-num", "#D-pes", "#D-dia", "#D-sep", "#D-ca", "#D-cb", "#D-perde",
                    "#F-chip", "#F-w1", "#F-w2", "#F-w3", "#F-roda", "#F-mel", "#F-6m", "#F-afg",
                    "#H-chip", "#H-w1", "#H-w2", "#H-por", "#H-q", "#H-q1", "#H-q2", "#H-q3", "#H-q4", "#H-qa",
                    "#N-raid2", "#N-room", "#N-lia", "#N-mesa", "#N-sa", "#N-ops", "#N-v1", "#N-v2", "#N-lbl"], { autoAlpha: 0 });
          gsap.set([__GO__], { autoAlpha: 0.22, scale: 0.86 });   // a grade ja aparece apagada (sem quadro quase preto na entrada) e acende em onda
          gsap.set([__SK__], { autoAlpha: 0 });
          gsap.set(["#D-sel", "#F-sel", "#H-sel"], { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set(["#D-sel .h", "#F-sel .h", "#H-sel .h"], { scale: 0 });
          gsap.set(["#N-b1", "#N-b2"], { scaleY: 0 });
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
          function rollTo(id, n, t, dur, h) { tl.fromTo(id, { y: 0, filter: "blur(5px)" }, { y: -n * h, filter: "blur(0px)", duration: dur * q, ease: "power4.out" }, Q(t)); }

          // ===== A · CAPA (quadro 0 = capa; o gancho inteiro em split) =====
          splitIn("#A", 0, true);
          kenburns("#A-capaimg", 0, 5.191, 1.0, 1.08);
          splitOut("#A", 5.191);

          // ===== P · PRÉ-REVELAÇÃO (só fotos, nada do Stanley) =====
          sceneIn("#P", 5.191);
          kenburns("#P-nv1img", 5.191, 7.86, 1.0, 1.06);
          whip("#P-nv1", "#P-nv2", 7.86);
          kenburns("#P-nv2img", 7.86, 10.45, 1.12, 1.0);
          sceneOut("#P", 10.45);

          // ===== B · REVELAÇÃO ("Stanley" 11,74 → 11,81) → O AVIÃO → AS LANCHONETES =====
          sceneIn("#B", 11.81); drift("#B-band", 11.81, 21.918);
          kenburns("#B-porimg", 11.81, 15.6, 1.0, 1.07);
          rise("#B-name", 11.98);
          pop("#B-fe", 12.69);
          whip(["#B-por", "#B-name", "#B-fe"], "#B-avi", 15.6);
          kenburns("#B-aviimg", 15.6, 18.45, 1.08, 1.0);
          pop("#B-sono", 16.17);
          pop("#B-ref", 17.17);
          drop(["#B-avi", "#B-sono", "#B-ref"], "#B-req", 18.45);
          tl.set("#B-req", { autoAlpha: 1 }, Q(18.45) - q);
          pop("#B-i1", 18.6, { x: -60, autoAlpha: 0 }, "tique");
          pop("#B-i2", 18.72, { x: -60, autoAlpha: 0 }, "tique");
          pop("#B-i3", 18.84, { x: -60, autoAlpha: 0 }, "tique");
          flip("#B-p1b", 19.05); flip("#B-p2b", 19.53); flip("#B-p3b", 19.86);
          tl.fromTo("#B-i1", { scale: 1 }, { scale: 1.05, duration: 6 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(20.19));
          sceneOut("#B", 21.918);

          // ===== D · PASSO 1 → A REUNIÃO DIÁRIA (7.000) → DOIS TIMES SEPARADOS: PERDE =====
          sceneIn("#D", 27.45); drift("#D-band", 27.45, 37.626);
          cap("D", [27.85, 27.45, 28.98, 29.14, 29.53], 29.75, 30.3, "#D-grid");
          tl.to([__GO__], { autoAlpha: 1, scale: 1, duration: 8 * q, ease: "back.out(2)", stagger: 0.01 }, Q(30.36));
          cue(30.42, "tique", -24); cue(30.8, "tique", -25); cue(31.2, "tique", -26);
          pop("#D-dia", 31.6);
          tl.set("#D-num", { autoAlpha: 1 }, Q(32.4));
          rollTo("#D-c1", 6, 32.4, 22, 250); rollTo("#D-c2", 3, 32.4, 24, 250); rollTo("#D-c3", 4, 32.4, 26, 250); rollTo("#D-c4", 5, 32.4, 28, 250);
          tl.fromTo("#D-num", { scale: 0.6 }, { scale: 1, duration: 10 * q, ease: "back.out(1.8)" }, Q(32.4));
          cue(32.42, "cacaniquel", -20);
          rise("#D-pes", 33.22);
          drop(["#D-grid"], "#D-sep", 34.4);
          pop("#D-ca", 34.4, { y: 80, autoAlpha: 0 });
          pop("#D-cb", 34.6, { y: 80, autoAlpha: 0 });
          tl.to("#D-ca", { x: -40, rotation: -4, duration: 12 * q, ease: "power3.inOut" }, Q(35.82));
          tl.to("#D-cb", { x: 40, rotation: 4, duration: 12 * q, ease: "power3.inOut" }, Q(35.82));
          cue(35.84, "swish", -20);
          tl.to(["#D-ca", "#D-cb"], { opacity: 0.45, duration: 6 * q }, Q(36.6));
          slam("#D-perde", 36.79, -6);
          sceneOut("#D", 37.626);

          // ===== F · PASSO 2 → UM TIME EM RODA (6 MESES NO OUTRO TIME) → DO LADO DE LÁ =====
          sceneIn("#F", 41.4); drift("#F-band", 41.4, 51.553);
          cap("F", [41.75, 41.4, 42.05, 42.72, 43.08], 43.3, 43.96, "#F-roda");
          kenburns("#F-rodaimg", 43.96, 47.72, 1.0, 1.1);
          pop("#F-mel", 44.53);
          pop("#F-6m", 45.45);
          whip(["#F-roda", "#F-mel", "#F-6m"], "#F-afg", 47.72);
          kenburns("#F-afgimg", 47.72, 51.553, 1.1, 1.0);
          sceneOut("#F", 51.553);

          // ===== H · PASSO 3 → A FRASE DELE =====
          sceneIn("#H", 56.7); drift("#H-band", 56.7, 63.007);
          cap("H", [57.0, 56.7, 57.49, 57.91], 58.1, 58.62, "#H-por");
          kenburns("#H-porimg", 58.62, 63.007, 1.0, 1.08);
          pop("#H-q", 59.0, { y: 90, autoAlpha: 0 }, "pop");
          rise("#H-q1", 59.23); rise("#H-q2", 59.86); rise("#H-q3", 60.44); rise("#H-q4", 61.4);
          cue(59.86, "tique", -24); cue(60.44, "tique", -24); cue(61.4, "tique", -24);
          rise("#H-qa", 62.17);
          sceneOut("#H", 63.007);

          // ===== L · SPLIT DA VIRADA (a capa de volta: a câmera entra no quartinho) =====
          splitIn("#L", 67.634);
          kenburns("#L-capaimg", 67.634, 69.698, 1.0, 1.25);
          splitOut("#L", 69.698);

          // ===== N · A VIRADA → O QUARTINHO → SOLDADO + ANALISTA → CLÍMAX =====
          sceneIn("#N", 69.698);
          kenburns("#N-raidimg", 69.698, 72.15, 1.0, 1.12);
          whip("#N-raid", "#N-raid2", 72.15);
          kenburns("#N-raid2img", 72.15, 74.66, 1.12, 1.0);
          drop(["#N-raid2"], "#N-room", 74.66);
          tl.fromTo([__SK__], { y: -1300, autoAlpha: 1 }, { y: 0, autoAlpha: 1, immediateRender: false, duration: 10 * q, ease: "bounce.out", stagger: 0.05 }, Q(75.2));
          for (var k = 0; k < 6; k++) cue(75.45 + k * 0.15, "impacto", -24, { dur: 0.3 });
          tl.fromTo("#N-bulb", { opacity: 1 }, { opacity: 0.55, duration: 2 * q, yoyo: true, repeat: 3 }, Q(76.4));
          slam("#N-lia", 76.95, -5);
          whip(["#N-room"], "#N-mesa", 78.03);
          kenburns("#N-mesaimg", 78.03, 80.58, 1.0, 1.08);
          pop("#N-sa", 79.09);
          drop(["#N-mesa", "#N-sa"], "#N-ops", 80.58);
          drift("#N-band", 80.58, 84.399);
          rise("#N-lbl", 80.6);
          tl.to("#N-b1", { scaleY: 1, duration: 10 * q, ease: "expo.out" }, Q(81.09));
          rise("#N-v1", 81.09); cue(81.1, "pop", -22, { f0: 600 });
          tl.to("#N-b2", { scaleY: 1, duration: 22 * q, ease: "expo.out" }, Q(82.9));
          tl.set("#N-v2", { autoAlpha: 1 }, Q(82.9));
          rollTo("#N-c1", 3, 82.9, 24, 170); rollTo("#N-c2", 3, 82.9, 26, 170); rollTo("#N-c3", 4, 82.9, 28, 170);
          pop("#N-plus", 83.8, { scale: 0.3, autoAlpha: 0 }, "clique");
          cue(82.92, "cacaniquel", -18); cue(83.04, "impacto", -17, { dur: 0.8 });
          sceneOut("#N", 84.399);
'''.replace('__GO__', GO).replace('__SK__', SK)

T = T.replace('            </style>', CSS + '            </style>', 1)
i = T.index('-->', T.index('CENAS (por video)')) + 3
T = T[:i] + HTML + T[i:]
T = T.replace('          // (vazio = camada transparente)', JS, 1)
open('compositions/mg.html', 'w').write(T)
print('compositions/mg.html', len(T), 'bytes')
