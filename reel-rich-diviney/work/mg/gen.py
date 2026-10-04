"""POR VIDEO — reel RICH DIVINEY. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Tempos absolutos de work/tl-words.txt.
As 3 respostas (showreel-interface):
  chip   = "PASSO N" (pilula com o ponto da cor do passo) — o protocolo de selecao em 3 passos
  prova  = fotos reais da Marinha dos EUA (BUD/S, operadores, marinheiras, piscina do teste) + retrato do Rich
  frase que o final inverte = a capa (o instrutor na beira da piscina: "o melhor candidato pode ser o que nao sabe fazer o trabalho")
           volta em "Nadar a gente ensina" — o moleque que nao sabia nadar.
uso: python3 work/mg/gen.py"""
T = open('work/mg/template.html').read()

CSS = r'''
        /* ===== reel RICH DIVINEY ===== */
        #mg .tag { white-space: nowrap; }
        #mg .cv { position: absolute; left: 190px; top: 190px; width: 700px; height: 900px; border-radius: 40px; background: #fff;
                  box-shadow: 0 34px 90px rgba(0,0,0,.45); overflow: hidden; }
        #mg .cv .hd { height: 120px; background: #11141A; color: #fff; font-weight: 800; font-size: 46px; letter-spacing: .14em; line-height: 120px; text-align: center; }
        #mg .cv .av { position: absolute; left: 60px; top: 170px; width: 170px; height: 170px; border-radius: 50%; background: #D9DCE2; overflow: hidden; }
        #mg .cv .av::before { content: ""; position: absolute; left: 52px; top: 28px; width: 66px; height: 66px; border-radius: 50%; background: #9AA0AB; }
        #mg .cv .av::after { content: ""; position: absolute; left: 26px; top: 108px; width: 118px; height: 96px; border-radius: 59px 59px 0 0; background: #9AA0AB; }
        #mg .cv .ln { position: absolute; height: 22px; border-radius: 11px; background: #E3E5EA; }
        #mg .cv .ln.d { background: #C4C8D0; }
        #mg .heart { position: absolute; left: 400px; top: 470px; width: 280px; height: 280px; color: #E5322D; font-size: 280px; line-height: 280px; text-align: center;
                     text-shadow: 0 18px 40px rgba(229,50,45,.45); }
        #mg .ppl10 { position: absolute; left: 115px; width: 850px; display: grid; grid-template-columns: repeat(5, 150px); gap: 25px; }
        #mg .ppl10 span { width: 150px; height: 150px; border-radius: 50%; background: #2A303C; position: relative; overflow: hidden; display: block; }
        #mg .ppl10 span::before { content: ""; position: absolute; left: 48px; top: 26px; width: 54px; height: 54px; border-radius: 50%; background: #8C93A1; }
        #mg .ppl10 span::after { content: ""; position: absolute; left: 25px; top: 90px; width: 100px; height: 80px; border-radius: 50px 50px 0 0; background: #8C93A1; }
        #mg .xs b { position: absolute; width: 150px; height: 150px; border-radius: 50%; border: 10px solid #E5322D; box-sizing: border-box;
                       color: #E5322D; font-size: 110px; line-height: 128px; text-align: center; font-weight: 800; background: rgba(20,8,10,.55); }
        #mg .big { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; color: #fff; line-height: 1; }
        #mg .lrow { position: relative; height: 150px; display: flex; align-items: center; justify-content: space-between; border-top: 2px solid rgba(128,136,150,.18); }
        #mg .lrow .nm { font-weight: 800; font-size: 58px; color: #11141A; }
        #mg .b-dark .lrow .nm { color: #E9ECF2; }
        #mg .pill2 { position: relative; width: 420px; height: 84px; }
        #mg .pill2 span { position: absolute; inset: 0; border-radius: 999px; color: #fff; font-weight: 800; font-size: 34px; letter-spacing: .05em;
                          display: flex; align-items: center; justify-content: center; gap: 14px; white-space: nowrap; }
        #mg .pill2 span::before { content: ""; width: 20px; height: 20px; border-radius: 50%; background: rgba(255,255,255,.9); }
        #mg .q { position: absolute; left: 70px; width: 940px; padding: 46px 54px; border-radius: 48px; background: #fff; color: #11141A;
                 box-shadow: 0 30px 80px rgba(0,0,0,.35); font-weight: 800; font-size: 62px; line-height: 1.12; }
        #mg .q small { display: block; font-weight: 600; font-size: 30px; letter-spacing: .12em; color: #8C93A1; margin-bottom: 18px; }
        #mg .q.me { background: #1E8BE5; color: #fff; }
        #mg .q.me small { color: rgba(255,255,255,.75); }
        #mg .shade { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0) 55%, rgba(0,0,0,.55) 100%); }
'''

def title(base, top, words, sel_last=True, color=None):
    sp = []
    for k, w in enumerate(words):
        if w == '<br>':
            sp.append('<br />'); continue
        sp.append(f'<span id="{base}-w{k}">{w}</span>')
    # a ultima palavra ganha a caixa de selecao com alcas
    last = sp[-1]
    sp[-1] = f'<span class="sel" id="{base}-sel">{last}<i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span>'
    st = f'top:{top}px' + (f';color:{color}' if color else '')
    return f'<div class="title" id="{base}-title" style="{st}">' + ' '.join(sp).replace(' <br /> ', '<br />') + '</div>'

def chip(base, top, roll, dot):
    spans = ''.join(f'<span>{r}</span>' for r in roll)
    return (f'<div class="chip" id="{base}-chip" style="top:{top}px"><span class="dot" style="background:{dot}"></span>'
            f'<div class="win"><div class="roll" id="{base}-roll">{spans}</div></div><div class="plus" id="{base}-plus">+</div></div>')

RED = "radial-gradient(circle at 34% 30%,#FF9A90,#E5322D 50%,#8E1612)"
YEL = "radial-gradient(circle at 34% 30%,#FFE58A,#F2B705 50%,#9A7300)"
GRN = "radial-gradient(circle at 34% 30%,#9BF0B9,#1FB45A 50%,#0E6A33)"

ppl = ''.join(f'<span id="C-p{k}"></span>' for k in range(10))
xs = ''.join(f'<b id="C-x{k}" style="left:{(k % 5) * 175}px;top:{(k // 5) * 175}px">✕</b>' for k in (1, 3, 4, 6, 8))

HTML = f'''
        <!-- A · SPLIT DA CAPA (0–10,97), nada do Rich antes do nome: CAPA GERADA A PEDIDO (Codex gpt-5.6-sol: instrutor SEAL em silhueta na
             beira da piscina de treino, contraluz vermelha — padrão docs/05 §25) → arrebentação → sino -->
        <div class="scene" id="A" style="height:845px">
          <div class="full" id="A-capa"><img id="A-capaimg" src="assets/mg/capa-rich.jpg" style="object-position:58% 0%" /></div>
          <div class="full" id="A-bote"><img id="A-boteimg" src="assets/mg/budS-botes-1.jpg" style="object-position:45% 50%" /></div>
          <div class="full" id="A-sino"><img id="A-sinoimg" src="assets/mg/seal-sino.jpg" style="object-position:30% 50%" /></div>
        </div>

        <!-- B · REVELAÇÃO (10,97–14,39): retrato do Rich + nome → a elite da elite -->
        <div class="scene" id="B"><div class="world dark"><div class="band" id="B-band"></div></div>
          <div class="card" id="B-rich" style="left:90px;top:170px;width:900px;height:704px"><img src="assets/mg/rich-retrato.jpg" style="object-position:50% 40%" /></div>
          <div class="name" id="B-name" style="top:930px"><b>RICH DIVINEY</b><i>EX-COMANDANTE DOS NAVY SEALs</i></div>
          <div class="full" id="B-op"><img id="B-opimg" src="assets/mg/seal-operador-1.jpg" style="object-position:40% 45%" /><div class="shade"></div></div>
          <div class="tag" id="B-elite" style="left:250px;top:1120px;background:#E5322D;font-size:46px">A ELITE DA ELITE</div>
        </div>

        <!-- C · SÓ OS MELHORES → METADE REPROVAVA (14,39–18,69) -->
        <div class="scene" id="C"><div class="world dark"><div class="band" id="C-band"></div></div>
          <div class="full" id="C-op2"><img id="C-op2img" src="assets/mg/seal-operador-2.jpg" style="object-position:58% 50%" /><div class="shade"></div></div>
          <div class="tag" id="C-mel" style="left:200px;top:1120px;background:#11141A;font-size:46px">SÓ OS MELHORES</div>
          <div class="big" id="C-tt" style="top:260px;font-size:84px;letter-spacing:.02em">CANDIDATOS</div>
          <div class="ppl10" id="C-ppl" style="top:420px">{ppl}</div>
          <div class="xs" id="C-xs" style="position:absolute;left:115px;top:420px;width:850px;height:330px">{xs}</div>
          <div class="tag" id="C-met" style="left:255px;top:880px;background:#E5322D;font-size:50px">METADE REPROVAVA</div>
        </div>

        <!-- D · APAIXONADO POR CURRÍCULO → PASSO 1 (20,60–25,30) -->
        <div class="scene" id="D"><div class="world light"><div class="band" id="D-band"></div></div>
          <div class="cv" id="D-cv"><div class="hd">CURRÍCULO</div><div class="av"></div>
            <i class="ln d" style="left:270px;top:200px;width:360px"></i><i class="ln" style="left:270px;top:250px;width:280px"></i><i class="ln" style="left:270px;top:300px;width:320px"></i>
            <i class="ln d" style="left:60px;top:420px;width:300px"></i><i class="ln" style="left:60px;top:470px;width:580px"></i><i class="ln" style="left:60px;top:520px;width:540px"></i>
            <i class="ln d" style="left:60px;top:620px;width:260px"></i><i class="ln" style="left:60px;top:670px;width:580px"></i><i class="ln" style="left:60px;top:720px;width:500px"></i><i class="ln" style="left:60px;top:770px;width:560px"></i>
          </div>
          <div class="heart" id="D-heart">♥</div>
          <div class="strike" id="D-strike" style="left:330px;top:640px;width:420px;transform:rotate(-38deg)"></div>
          {chip("D", 300, ["PASSO 3", "PASSO 2", "PASSO 1"], GRN)}
          {title("D", 520, ["SEPARA", "O", "QUE", "<br>", "DÁ", "PRA", "ENSINAR."])}
        </div>

        <!-- E · A VAGA PEDE: dá pra ensinar? (27,30–30,95) -->
        <div class="scene" id="E"><div class="world light"><div class="band" id="E-band"></div></div>
          <div class="board b-light" id="E-board" style="top:330px">
            <div class="hd"><span>A VAGA PEDE</span><i>DÁ PRA ENSINAR?</i></div>
            <div class="lrow" id="E-r1"><span class="nm">PLANILHA</span><div class="pill2"><span class="p0" id="E-p1a">?</span><span class="pg" id="E-p1b">DÁ</span></div></div>
            <div class="lrow" id="E-r2"><span class="nm">PACIÊNCIA</span><div class="pill2"><span class="p0" id="E-p2a">?</span><span class="pr" id="E-p2b">NÃO DÁ</span></div></div>
          </div>
        </div>

        <!-- F · PASSO 2 (36,05–38,90) -->
        <div class="scene" id="F"><div class="world light"><div class="band" id="F-band"></div></div>
          {chip("F", 300, ["PASSO 1", "PASSO 3", "PASSO 2"], YEL)}
          {title("F", 520, ["PERGUNTA", "<br>", "PELO", "PIOR", "<br>", "DIA."])}
        </div>

        <!-- G · QUEM É DE VERDADE (38,90–40,40): Hell Week na lama -->
        <div class="scene" id="G"><div class="world dark"></div>
          <div class="full" id="G-lama"><img id="G-lamaimg" src="assets/mg/extremo-lama.jpg" style="object-position:45% 50%" /></div>
        </div>

        <!-- H · A PERGUNTA DA ENTREVISTA (42,30–45,90) -->
        <div class="scene" id="H"><div class="world dark"><div class="band" id="H-band"></div></div>
          <div class="q" id="H-q1" style="top:300px"><small>NA ENTREVISTA</small>Me conta o dia que tudo deu errado no seu último emprego.</div>
          <div class="q me" id="H-q2" style="top:860px;left:300px;width:710px">O que você fez?</div>
        </div>

        <!-- I · PASSO 3 (50,10–54,24) -->
        <div class="scene" id="I"><div class="world light"><div class="band" id="I-band"></div></div>
          {chip("I", 300, ["PASSO 2", "PASSO 1", "PASSO 3"], RED)}
          <div class="tag" id="I-antes" style="left:205px;top:470px;background:#11141A;font-size:40px">ANTES DE MANDAR EMBORA</div>
          {title("I", 600, ["TROCA", "DE", "<br>", "CADEIRA."])}
        </div>

        <!-- J · A MARINHEIRA (54,24–61,15): não rendia → nova função → decolou -->
        <div class="scene" id="J"><div class="world dark"></div>
          <div class="full" id="J-m1"><img id="J-m1img" src="assets/mg/marinheira-2.jpg" style="object-position:45% 50%" /><div class="shade"></div></div>
          <div class="tag" id="J-nr" style="left:300px;top:1120px;background:#E5322D;font-size:46px">NÃO RENDIA</div>
          <div class="full" id="J-m2"><img id="J-m2img" src="assets/mg/marinheira-decolagem-1.jpg" style="object-position:30% 50%" /><div class="shade"></div></div>
          <div class="tag" id="J-nf" style="left:290px;top:1120px;background:#11141A;font-size:46px">NOVA FUNÇÃO</div>
          <div class="tag" id="J-dec" style="left:320px;top:1120px;background:#1FB45A;font-size:46px">DECOLOU ↗</div>
        </div>

        <!-- K · SPLIT DA VIRADA (65,15–71,19): a piscina do teste -->
        <div class="scene" id="K" style="height:845px">
          <div class="full" id="K-p3"><img id="K-p3img" src="assets/mg/piscina-3.jpg" style="object-position:50% 50%" /></div>
          <div class="full" id="K-lim"><img id="K-limimg" src="assets/mg/piscina-limite-2.jpg" style="object-position:40% 50%" /></div>
        </div>

        <!-- L · PULOU, AFUNDOU, ATRAVESSOU (71,19–76,00) -->
        <div class="scene" id="L"><div class="world dark"></div>
          <div class="full" id="L-p2"><img id="L-p2img" src="assets/mg/piscina-2.jpg" style="object-position:55% 50%" /></div>
          <div class="full" id="L-lim"><img id="L-limimg" src="assets/mg/piscina-limite-1.jpg" style="object-position:50% 40%" /></div>
        </div>

        <!-- M · CLÍMAX (79,25–83,57): a ficha do candidato -->
        <div class="scene" id="M"><div class="world dark"><div class="band" id="M-band"></div></div>
          <div class="board b-dark" id="M-board" style="top:300px">
            <div class="hd"><span>FICHA DO CANDIDATO</span><i>SELEÇÃO</i></div>
            <div class="lrow" id="M-r1"><span class="nm">NATAÇÃO</span><div class="pill2"><span class="pr" id="M-p1a">NÃO SABE</span><span class="py" id="M-p1b">A GENTE ENSINA</span></div></div>
            <div class="lrow" id="M-r2"><span class="nm">CORAGEM</span><div class="pill2"><span class="p0" id="M-p2a">?</span><span class="pg" id="M-p2b">NINGUÉM ENSINA</span></div></div>
          </div>
          <div class="stamp" data-layout-allow-overlap id="M-st" style="left:215px;top:820px;font-size:100px">APROVADO</div>
          <div class="ring" id="M-ring1" style="left:540px;top:900px;border-color:#1FB45A"></div>
          <div class="ring" id="M-ring2" style="left:540px;top:900px;border-color:#1FB45A"></div>
        </div>

        <!-- N · NADAR A GENTE ENSINA (86,44–88,18): volta à onda da capa -->
        <div class="scene" id="N"><div class="world dark"></div>
          <div class="full" id="N-capa"><img id="N-capaimg" src="assets/mg/capa-rich.jpg" style="object-position:59% 30%" /></div>
        </div>
'''

JS = r'''
          gsap.set(["#A-bote", "#A-sino",
                    "#B-name", "#B-op", "#B-elite",
                    "#C-mel", "#C-tt", "#C-ppl", "#C-met", "#C-xs b",
                    "#D-heart", "#D-strike", "#D-chip", "#D-w0", "#D-w1", "#D-w2", "#D-w4", "#D-w5", "#D-w6",
                    "#E-p1b", "#E-p2b",
                    "#F-chip", "#F-w0", "#F-w2", "#F-w3", "#F-w5",
                    "#H-q1", "#H-q2",
                    "#I-chip", "#I-antes", "#I-w0", "#I-w1", "#I-w3",
                    "#J-nr", "#J-m2", "#J-nf", "#J-dec",
                    "#K-lim", "#L-lim",
                    "#M-p1b", "#M-p2b", "#M-st"], { autoAlpha: 0 });
          gsap.set(["#D-sel", "#F-sel", "#I-sel"], { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set(["#D-sel .h", "#F-sel .h", "#I-sel .h"], { scale: 0 });
          gsap.set("#D-strike", { scaleX: 0 });
          gsap.set(["#E-r1", "#E-r2", "#M-r1", "#M-r2"], { autoAlpha: 0, x: 80 });
          function sel(base, t) {
            tl.to("#" + base + "-sel", { borderColor: "rgba(242,183,5,1)", backgroundColor: "rgba(242,183,5,.16)", duration: 4 * q, ease: "none" }, Q(t));
            tl.to("#" + base + "-sel .h", { scale: 1, duration: 6 * q, ease: "back.out(3)", stagger: q }, Q(t) + q);
          }
          function swap(a, b, t, som) {                                                   // pilula muda de estado
            tl.to(a, { scale: 0.6, autoAlpha: 0, duration: 4 * q, ease: "power2.in" }, Q(t) - 4 * q);
            flip(b, t);
          }

          // ===== A · CAPA (quadro 0 = capa) → SÓ FOTOS =====
          splitIn("#A", 0, true);
          kenburns("#A-capaimg", 0, 5.1, 1.12, 1.0);
          whip("#A-capa", "#A-bote", 5.1);
          kenburns("#A-boteimg", 5.1, 8.4, 1.0, 1.1);
          drop("#A-bote", "#A-sino", 8.4);
          kenburns("#A-sinoimg", 8.4, 10.97, 1.12, 1.0);
          splitOut("#A", 10.97);

          // ===== B · REVELAÇÃO =====
          sceneIn("#B", 10.97); drift("#B-band", 10.97, 14.39);
          tl.fromTo("#B-rich", { scale: 1.1 }, { scale: 1, duration: 1.6, ease: "power2.out" }, Q(10.97));
          rise("#B-name", 11.2);
          whip(["#B-rich", "#B-name"], "#B-op", 12.47);
          kenburns("#B-opimg", 12.47, 14.39, 1.0, 1.1);
          pop("#B-elite", 12.99);
          sceneOut("#B", 14.39);

          // ===== C · SÓ OS MELHORES → METADE =====
          sceneIn("#C", 14.39); drift("#C-band", 14.39, 18.69);
          kenburns("#C-op2img", 14.39, 16.3, 1.12, 1.0);
          pop("#C-mel", 14.58);
          tl.to(["#C-op2", "#C-mel"], { y: 1900, duration: 5 * q, ease: "power4.in" }, Q(16.3) - 5 * q);
          rise("#C-tt", 16.25);
          tl.set("#C-ppl", { autoAlpha: 1 }, Q(16.3));
          tl.fromTo("#C-ppl span", { scale: 0 }, { scale: 1, immediateRender: false, duration: 8 * q, ease: "back.out(2.4)", stagger: q }, Q(16.3));
          for (var k = 0; k < 5; k++) cue(16.3 + k * 2 * q, "tique", -26);
          tl.fromTo("#C-xs b", { scale: 2.2, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 5 * q, ease: "power4.in", stagger: 2 * q }, Q(16.89));
          for (var k = 0; k < 5; k++) cue(16.89 + 5 * q + k * 2 * q, "clique", -21);
          pop("#C-met", 17.34);
          sceneOut("#C", 18.69);

          // ===== D · APAIXONADO POR CURRÍCULO → PASSO 1 =====
          sceneIn("#D", 20.6); drift("#D-band", 20.6, 25.3);
          tl.fromTo("#D-heart", { scale: 0.3, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 9 * q, ease: "back.out(2.6)" }, Q(20.23));
          tl.fromTo("#D-heart", { scale: 1 }, { scale: 1.12, duration: 5 * q, ease: "sine.inOut", yoyo: true, repeat: 3 }, Q(20.6));
          cue(20.25, "pop", -20);
          tl.set("#D-strike", { autoAlpha: 1 }, Q(21.0));
          tl.to("#D-strike", { scaleX: 1, duration: 6 * q, ease: "expo.out" }, Q(21.0));
          cue(21.0, "swish", -19);
          tl.to(["#D-cv", "#D-heart", "#D-strike"], { y: 1900, rotation: 8, duration: 6 * q, ease: "power4.in" }, Q(22.05) - 6 * q);
          chip("D", 22.4, 22.1);
          rise("#D-w0", 22.88); rise("#D-w1", 23.05); rise("#D-w2", 23.12); rise("#D-w4", 23.35); rise("#D-w5", 23.55); rise("#D-w6", 23.83); sel("D", 24.15);
          sceneOut("#D", 25.3);

          // ===== E · A VAGA PEDE =====
          sceneIn("#E", 27.3); drift("#E-band", 27.3, 30.95);
          stagger(["#E-r1", "#E-r2"], 27.45, 2, 4);
          swap("#E-p1a", "#E-p1b", 28.7);
          swap("#E-p2a", "#E-p2b", 30.57);
          tl.to("#E-r2", { x: -14, duration: 2 * q, ease: "power2.out", yoyo: true, repeat: 3 }, Q(30.62));
          sceneOut("#E", 30.95);

          // ===== F · PASSO 2 =====
          sceneIn("#F", 36.05); drift("#F-band", 36.05, 38.9);
          chip("F", 36.3, 36.07);
          rise("#F-w0", 36.68); rise("#F-w2", 37.08); rise("#F-w3", 37.35); rise("#F-w5", 37.66); sel("F", 37.9);
          smear("#F-chip", 38.9);
          tl.to("#F-title", { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(38.9) - 5 * q);
          zoomIn("#G", 38.9);
          tl.set("#F", { autoAlpha: 0 }, Q(38.9));

          // ===== G · A LAMA =====
          tl.set("#G", { autoAlpha: 1 }, Q(38.9));
          kenburns("#G-lamaimg", 38.9, 40.4, 1.0, 1.12);
          sceneOut("#G", 40.4);

          // ===== H · A PERGUNTA =====
          sceneIn("#H", 42.3); drift("#H-band", 42.3, 45.9);
          tl.fromTo("#H-q1", { y: 600, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 12 * q, ease: "expo.out" }, Q(42.35));
          cue(42.38, "pop", -19);
          tl.fromTo("#H-q2", { y: 500, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 12 * q, ease: "expo.out" }, Q(45.35));
          cue(45.38, "pop", -19);
          sceneOut("#H", 45.9);

          // ===== I · PASSO 3 =====
          sceneIn("#I", 50.1); drift("#I-band", 50.1, 54.24);
          chip("I", 50.45, 50.15);
          pop("#I-antes", 51.3);
          rise("#I-w0", 52.89); rise("#I-w1", 53.01); rise("#I-w3", 53.14); sel("I", 53.45);
          smear("#I-chip", 54.24);
          tl.to(["#I-title", "#I-antes"], { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(54.24) - 5 * q);
          tl.set("#I", { autoAlpha: 0 }, Q(54.24));

          // ===== J · A MARINHEIRA =====
          tl.set("#J", { autoAlpha: 1 }, Q(54.24));
          zoomIn("#J-m1", 54.24);
          kenburns("#J-m1img", 54.24, 58.27, 1.0, 1.12);
          pop("#J-nr", 55.61);
          whip(["#J-m1", "#J-nr"], "#J-m2", 58.27);
          kenburns("#J-m2img", 58.27, 61.15, 1.12, 1.0);
          pop("#J-nf", 59.01);
          tl.to("#J-nf", { autoAlpha: 0, y: -30, duration: 4 * q }, Q(59.8));
          pop("#J-dec", 59.92, null, "ding");
          sceneOut("#J", 61.15);

          // ===== K · SPLIT DA VIRADA: A PISCINA =====
          splitIn("#K", 65.15);
          kenburns("#K-p3img", 65.15, 68.31, 1.0, 1.1);
          whip("#K-p3", "#K-lim", 68.31);
          kenburns("#K-limimg", 68.31, 71.19, 1.12, 1.0);
          splitOut("#K", 71.19);

          // ===== L · PULOU, AFUNDOU =====
          sceneIn("#L", 71.19);
          tl.fromTo("#L-p2img", { scale: 1.18, y: -60 }, { scale: 1.0, y: 40, duration: 3.76, ease: "none" }, Q(71.19));
          drop("#L-p2", "#L-lim", 74.95, "sobe");
          kenburns("#L-limimg", 74.95, 76.0, 1.0, 1.08);
          sceneOut("#L", 76.0);

          // ===== M · CLÍMAX: A FICHA =====
          sceneIn("#M", 79.25); drift("#M-band", 79.25, 83.57);
          stagger(["#M-r1", "#M-r2"], 79.3, 2, 4);
          swap("#M-p1a", "#M-p1b", 80.03);
          swap("#M-p2a", "#M-p2b", 82.51);
          slam("#M-st", 82.92, -6);
          rings("#M-ring1", "#M-ring2", 82.92);
          sceneOut("#M", 83.57);

          // ===== N · NADAR A GENTE ENSINA: volta à capa =====
          sceneIn("#N", 86.44);
          kenburns("#N-capaimg", 86.44, 88.18, 1.0, 1.12);
          sceneOut("#N", 88.18);
'''

T = T.replace('            </style>', CSS + '            </style>', 1)
i = T.index('-->', T.index('CENAS (por video)')) + 3
T = T[:i] + HTML + T[i:]
T = T.replace('          // (vazio = camada transparente)', JS, 1)
open('compositions/mg.html', 'w').write(T)
print('compositions/mg.html', len(T), 'bytes')
