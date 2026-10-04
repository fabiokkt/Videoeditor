"""POR VIDEO — reel JAMES STOCKDALE. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Tempos absolutos de work/tl-words.txt.
Dosagem (docs/05 §24): abertura só com fotos; no corpo foto real é o padrão; motion só nos capítulos (PASSO 1/2/3),
no número (5 -> 7,5 anos), no mecanismo (depende / não depende, o extrato) e no clímax (o calendário Natal -> Páscoa).
uso: python3 work/mg/gen.py"""
T = open('work/mg/template.html').read()

CSS = r'''
        /* ===== reel JAMES STOCKDALE ===== */
        #mg .tag { white-space: nowrap; }
        #mg .full img.dim { filter: brightness(.82); }
        #mg .bw img { filter: grayscale(1) contrast(1.08); }
        #mg .ctr { position: absolute; left: 0; width: 1080px; text-align: center; color: #fff; font-weight: 800; }
        #mg .ctr .col { display: inline-block; height: 300px; overflow: hidden; vertical-align: top; }
        #mg .ctr .col div span { display: block; height: 300px; line-height: 300px; font-size: 300px; width: 200px; text-align: center; }
        #mg .ctr .frac { display: inline-block; font-size: 300px; line-height: 300px; height: 300px; vertical-align: top; color: #FF5A4E; }
        #mg .ctr .un { display: block; font-size: 64px; letter-spacing: .14em; color: #8C93A1; margin-top: 30px; }
        #mg .twocol { position: absolute; left: 60px; width: 960px; display: flex; gap: 30px; }
        #mg .twocol .c { flex: 1; border-radius: 40px; padding: 34px 30px 26px; box-shadow: 0 30px 80px rgba(0,0,0,.4); }
        #mg .twocol .c.no { background: #151A23; border: 2px solid #252C39; color: #8C93A1; }
        #mg .twocol .c.yes { background: #fff; color: #11141A; }
        #mg .twocol .hd { font-weight: 800; font-size: 34px; letter-spacing: .08em; margin-bottom: 18px; }
        #mg .twocol .c.no .hd { color: #FF6B5E; } #mg .twocol .c.yes .hd { color: #1FB45A; }
        #mg .twocol .it { position: relative; font-weight: 800; font-size: 60px; line-height: 1.5; }
        #mg .twocol .c.no .it { color: #C9CCD2; }
        #mg .ext { position: absolute; left: 70px; width: 940px; border-radius: 44px; background: #fff; color: #11141A; padding: 34px 44px 24px;
                   box-shadow: 0 34px 90px rgba(0,0,0,.4); }
        #mg .ext .hd { display: flex; justify-content: space-between; font-weight: 800; font-size: 32px; letter-spacing: .08em; }
        #mg .ext .hd i { font-style: normal; color: #8C93A1; font-weight: 600; }
        #mg .ext .sal { font-weight: 800; font-size: 96px; color: #E5322D; margin: 10px 0 14px; }
        #mg .ext .sl { font-weight: 600; font-size: 28px; letter-spacing: .1em; color: #8C93A1; }
        #mg .ext .ln { display: flex; justify-content: space-between; height: 92px; align-items: center; border-top: 2px solid rgba(128,136,150,.18);
                       font-weight: 600; font-size: 36px; }
        #mg .ext .ln b { font-weight: 800; color: #E5322D; }
        #mg .cal { position: absolute; left: 190px; width: 700px; height: 760px; border-radius: 48px; background: #fff; overflow: hidden;
                   box-shadow: 0 40px 100px rgba(0,0,0,.55); text-align: center; color: #11141A; }
        #mg .cal .top { height: 170px; background: #E5322D; color: #fff; }
        #mg .cal .win { height: 170px; overflow: hidden; }
        #mg .cal .win div span { display: block; height: 170px; line-height: 170px; font-weight: 800; font-size: 84px; letter-spacing: .1em; }
        #mg .cal .day { height: 380px; overflow: hidden; }
        #mg .cal .day div span { display: block; height: 380px; line-height: 380px; font-weight: 800; font-size: 330px; }
        #mg .cal .ev { height: 190px; overflow: hidden; }
        #mg .cal .ev div span { display: block; height: 190px; line-height: 150px; font-weight: 800; font-size: 74px; letter-spacing: .06em; color: #5A606B; }
        #mg .cal .ring2 { position: absolute; left: 0; top: 0; width: 700px; height: 760px; border-radius: 48px; box-shadow: inset 0 0 0 10px #1FB45A; opacity: 0; }
'''

MESES = ['DEZEMBRO', 'JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO']
DIAS = ['25', '9', '14', '21', '20', '3', '17']
EVS = ['NATAL', '·', '·', '·', 'PÁSCOA', '·', '·']
def roll(items): return ''.join(f'<span>{x}</span>' for x in items)

HTML = f'''
        <!-- A · SPLIT DA CAPA (0–10,74), faixa de cima SÓ COM FOTOS e nada do Stockdale antes de "Jim":
             Hanoi Hilton do alto (NARA) → cama da cela de Hoa Lò → muro de Hoa Lò -->
        <div class="scene" id="A" style="height:845px">
          <div class="full bw" id="A-capa"><img id="A-capaimg" src="assets/mg/hanoi-hilton-aerea.jpg" style="object-position:30% 35%" /></div>
          <div class="full" id="A-cela"><img id="A-celaimg" class="dim" src="assets/mg/hoalo-cama.jpg" style="object-position:50% 55%" /></div>
          <div class="full" id="A-muro"><img id="A-muroimg" class="dim" src="assets/mg/hoalo-muro.jpg" style="object-position:60% 50%" /></div>
        </div>

        <!-- B · REVELAÇÃO (10,74–18,98): Stockdale → A-4 no Vietnã → Hoa Lò → contador 5 → 7,5 anos -->
        <div class="scene" id="B"><div class="world dark"><div class="band" id="B-band"></div></div>
          <div class="card" id="B-st" style="left:110px;top:150px;width:860px;height:1000px"><img src="assets/mg/stockdale-retrato.jpg" style="object-position:50% 25%" /></div>
          <div class="name" id="B-name" style="top:1090px"><b>JAMES STOCKDALE</b><i>PILOTO DA MARINHA DOS EUA</i></div>
          <div class="full" id="B-a4"><img id="B-a4img" class="dim" src="assets/mg/a4-catapulta.jpg" style="object-position:45% 50%" /></div>
          <div class="tag" id="B-viet" style="left:330px;top:1180px;background:#E5322D">VIETNÃ · 1965</div>
          <div class="full" id="B-hl"><img id="B-hlimg" class="dim" src="assets/mg/hoalo-portao.jpg" style="object-position:40% 50%" /></div>
          <div class="tag" id="B-hil" style="left:250px;top:1180px;background:#11141A">HOA LÒ · “HANOI HILTON”</div>
          <div class="ctr" id="B-ctr" style="top:420px"><span class="col"><div id="B-d"><span>5</span><span>6</span><span>7</span></div></span><span class="frac" id="B-fr">,5</span><span class="un" id="B-un">ANOS PRESO</span></div>
        </div>

        <!-- D · PASSO 1 → EPICTETO → DEPENDE / NÃO DEPENDE (23,31–35,00) -->
        <div class="scene" id="D"><div class="world light"><div class="band" id="D-band"></div></div>
          <div class="chip" id="D-chip" style="top:300px"><span class="dot" style="background:#1FB45A"></span><div class="win"><div class="roll" id="D-roll"><span>PASSO 3</span><span>PASSO 2</span><span>PASSO 1</span></div></div><div class="plus" id="D-plus">+</div></div>
          <div class="title" id="D-title" style="top:520px"><span id="D-w1">SEPARA</span> <span id="D-w2">O</span> <span id="D-w3">QUE</span><br /><span id="D-w4">É</span> <span class="sel" id="D-sel"><span id="D-w5">SEU.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="card" id="D-ep" style="left:200px;top:150px;width:680px;height:907px;background:#fff"><img src="assets/mg/epicteto.jpg" style="object-fit:contain" /></div>
          <div class="tag" id="D-epn" style="left:200px;top:1110px;background:#11141A">EPICTETO · FILÓSOFO GREGO</div>
          <div class="twocol" id="D-cols" style="top:250px">
            <div class="c no" id="D-no"><div class="hd">NÃO DEPENDE</div><div class="it" id="D-i1">JUROS</div><div class="it" id="D-i2">GOVERNO</div></div>
            <div class="c yes" id="D-yes"><div class="hd">DEPENDE</div><div class="it" id="D-i3">PREÇO</div><div class="it" id="D-i4">COBRANÇA</div></div>
          </div>
        </div>

        <!-- F · PASSO 2 → A CELA → O EXTRATO (37,85–49,45) -->
        <div class="scene" id="F"><div class="world dark"><div class="band" id="F-band"></div></div>
          <div class="chip" id="F-chip" style="top:300px;background:#fff;color:#11141A"><span class="dot" style="background:#F2B705"></span><div class="win"><div class="roll" id="F-roll"><span>PASSO 1</span><span>PASSO 3</span><span>PASSO 2</span></div></div><div class="plus" id="F-plus" style="background:#fff;color:#11141A">+</div></div>
          <div class="title" id="F-title" style="top:520px;color:#fff"><span id="F-w1">ENCARA</span> <span id="F-w2">O</span> <span id="F-w3">FATO</span><br /><span id="F-w4">MAIS</span> <span class="sel" id="F-sel"><span id="F-w5">FEIO.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="card bw" id="F-cela" style="left:60px;top:250px;width:960px;height:610px"><img src="assets/mg/pow-chuveiro.jpg" style="object-position:20% 50%" /></div>
          <div class="tag" id="F-ct" style="left:60px;top:910px;background:#E5322D">PRISIONEIRO EM HANÓI · 1973</div>
          <div class="ext" id="F-ext" style="top:200px">
            <div class="hd"><span>EXTRATO</span><i>CONTA CORRENTE</i></div>
            <div class="sl">SALDO</div><div class="sal" id="F-sal">−R$ 48.320,00</div>
            <div class="ln" id="F-l1"><span>Juros cheque especial</span><b>−3.912,40</b></div>
            <div class="ln" id="F-l2"><span>Fornecedor</span><b>−21.600,00</b></div>
            <div class="ln" id="F-l3"><span>Folha de pagamento</span><b>−38.450,00</b></div>
            <div class="ln" id="F-l4"><span>Recebimento</span><b style="color:#1FB45A">+15.642,40</b></div>
          </div>
        </div>

        <!-- I · PASSO 3 → A VOLTA (52,94–59,76) -->
        <div class="scene" id="I"><div class="world light"><div class="band" id="I-band"></div></div>
          <div class="chip" id="I-chip" style="top:300px"><span class="dot" style="background:#E5322D"></span><div class="win"><div class="roll" id="I-roll"><span>PASSO 2</span><span>PASSO 1</span><span>PASSO 3</span></div></div><div class="plus" id="I-plus">+</div></div>
          <div class="title" id="I-title" style="top:520px"><span id="I-w1">NUNCA</span> <span id="I-w2">PERDE</span><br /><span id="I-w3">A</span> <span id="I-w4">FÉ</span> <span id="I-w5">NO</span> <span class="sel" id="I-sel"><span id="I-w6">FINAL.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="full" id="I-volta"><img id="I-voltaimg" src="assets/mg/stockdale-volta.jpg" style="object-position:40% 30%" /></div>
          <div class="tag" id="I-vt" style="left:200px;top:1180px;background:#1FB45A">A VOLTA · FEVEREIRO DE 1973</div>
          <div class="full bw" id="I-c141"><img id="I-c141img" src="assets/mg/pow-c141.jpg" style="object-position:45% 50%" /></div>
        </div>

        <!-- K · AS FAMÍLIAS ESPERANDO (62,02–64,82) -->
        <div class="scene" id="K"><div class="full" id="K-esp"><img id="K-espimg" class="dim" src="assets/mg/esposas-espera.jpg" style="object-position:50% 40%" /></div></div>

        <!-- L · SPLIT DA VIRADA (64,82–70,78): o Natal → o Stockdale -->
        <div class="scene" id="L" style="height:845px">
          <div class="full bw" id="L-natal"><img id="L-natalimg" src="assets/mg/natal-arvore.jpg" style="object-position:50% 30%" /></div>
          <div class="full" id="L-st"><img id="L-stimg" src="assets/mg/stockdale-olhar.jpg" style="object-position:50% 22%" /></div>
        </div>

        <!-- M · CLÍMAX (70,78–82,15): o calendário — Natal passa, Páscoa passa → coração partido -->
        <div class="scene" id="M"><div class="world dark"><div class="band" id="M-band"></div></div>
          <div class="cal" id="M-cal" style="top:200px">
            <div class="top"><div class="win"><div id="M-mes">{roll(MESES)}</div></div></div>
            <div class="day"><div id="M-dia">{roll(DIAS)}</div></div>
            <div class="ev"><div id="M-ev">{roll(EVS)}</div></div>
            <div class="ring2" id="M-ok"></div>
          </div>
          <div class="tag" id="M-sai" style="left:310px;top:1010px;background:#1FB45A">“A GENTE SAI”</div>
          <div class="stamp" data-layout-allow-overlap id="M-p1" style="left:250px;top:470px;font-size:96px">PASSOU</div>
          <div class="tag" id="M-sai2" style="left:310px;top:1010px;background:#1FB45A">“A GENTE SAI”</div>
          <div class="stamp" data-layout-allow-overlap id="M-p2" style="left:250px;top:470px;font-size:96px">PASSOU</div>
          <div class="full" id="M-cama"><img id="M-camaimg" class="dim" src="assets/mg/hoalo-cama.jpg" style="object-position:50% 60%;filter:brightness(.62) saturate(.7)" /></div>
        </div>

        <!-- O · O SEU NATAL (84,75–86,97): a capa volta com o sentido trocado -->
        <div class="scene" id="O"><div class="full" id="O-nat"><img id="O-natimg" src="assets/mg/natal-arvore.jpg" style="object-position:50% 40%;filter:grayscale(1) brightness(.7)" /></div></div>
'''

JS = r'''
          gsap.set(["#A-cela", "#A-muro",
                    "#B-name", "#B-a4", "#B-viet", "#B-hl", "#B-hil", "#B-ctr", "#B-fr",
                    "#D-chip", "#D-w1", "#D-w2", "#D-w3", "#D-w4", "#D-w5", "#D-ep", "#D-epn", "#D-cols", "#D-i1", "#D-i2", "#D-i3", "#D-i4",
                    "#F-chip", "#F-w1", "#F-w2", "#F-w3", "#F-w4", "#F-w5", "#F-cela", "#F-ct", "#F-ext",
                    "#I-chip", "#I-w1", "#I-w2", "#I-w3", "#I-w4", "#I-w5", "#I-w6", "#I-volta", "#I-vt", "#I-c141",
                    "#L-st",
                    "#M-cal", "#M-sai", "#M-p1", "#M-sai2", "#M-p2", "#M-cama"], { autoAlpha: 0 });
          gsap.set(["#D-sel", "#F-sel", "#I-sel"], { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set(["#D-sel .h", "#F-sel .h", "#I-sel .h"], { scale: 0 });
          gsap.set(["#F-l1", "#F-l2", "#F-l3", "#F-l4"], { autoAlpha: 0, x: 80 });
          function sel(base, t) {
            tl.to("#" + base + "-sel", { borderColor: "rgba(242,183,5,1)", backgroundColor: "rgba(242,183,5,.16)", duration: 4 * q, ease: "none" }, Q(t));
            tl.to("#" + base + "-sel .h", { scale: 1, duration: 6 * q, ease: "back.out(3)", stagger: q }, Q(t) + q);
          }
          function out(sel_, t) { tl.to(sel_, { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(t) - 5 * q); }

          // ===== A · CAPA (quadro 0 = capa) → SÓ FOTOS, nada do Stockdale =====
          splitIn("#A", 0, true);
          kenburns("#A-capaimg", 0, 5.01, 1.12, 1.0);
          whip("#A-capa", "#A-cela", 5.01);
          kenburns("#A-celaimg", 5.01, 8.0, 1.0, 1.1);
          drop("#A-cela", "#A-muro", 8.0);
          kenburns("#A-muroimg", 8.0, 10.74, 1.12, 1.0);
          splitOut("#A", 10.74);

          // ===== B · REVELAÇÃO ("Jim" 10,67 → 10,74) =====
          sceneIn("#B", 10.74); drift("#B-band", 10.74, 18.98);
          tl.fromTo("#B-st", { scale: 1.1 }, { scale: 1, duration: 1.3, ease: "power2.out" }, 10.74);
          rise("#B-name", 10.95);
          whip(["#B-st", "#B-name"], "#B-a4", 11.88);
          kenburns("#B-a4img", 11.88, 14.73, 1.0, 1.12);
          pop("#B-viet", 12.15);
          drop(["#B-a4", "#B-viet"], "#B-hl", 14.73);
          kenburns("#B-hlimg", 14.73, 16.71, 1.12, 1.0);
          pop("#B-hil", 15.03);
          // o número: "cinco anos" → "foram sete e meio"
          tl.to(["#B-hl", "#B-hil"], { y: 1900, duration: 5 * q, ease: "power4.in" }, Q(16.71) - 5 * q);
          tl.fromTo("#B-ctr", { y: -900, autoAlpha: 1 }, { immediateRender: false, y: 0, autoAlpha: 1, duration: 13 * q, ease: "expo.out" }, Q(16.71) - q);
          cue(16.66, "whoosh", -15);
          tl.fromTo("#B-d", { y: 0, filter: "blur(0px)" }, { y: -600, filter: "blur(0px)", duration: 16 * q, ease: "power4.out" }, Q(17.64));
          cue(17.64, "cacaniquel", -20);
          tl.fromTo("#B-fr", { autoAlpha: 0, scale: 0.4 }, { autoAlpha: 1, scale: 1, duration: 9 * q, ease: "back.out(2.4)" }, Q(17.95));
          cue(17.97, "pop", -19);
          sceneOut("#B", 18.98);

          // ===== D · PASSO 1 → EPICTETO → DEPENDE / NÃO DEPENDE =====
          sceneIn("#D", 23.31); drift("#D-band", 23.31, 35.0);
          chip("D", 23.6, 23.35);
          rise("#D-w1", 23.97); rise("#D-w2", 24.48); rise("#D-w3", 24.52); rise("#D-w4", 24.79); rise("#D-w5", 24.89); sel("D", 25.1);
          smear("#D-chip", 25.6);
          out("#D-title", 25.6);
          zoomIn("#D-ep", 25.6);
          tl.fromTo("#D-ep", { scale: 1 }, { scale: 1.05, duration: 5.2, ease: "none" }, Q(26.0));
          rise("#D-epn", 26.36);
          tl.to(["#D-ep", "#D-epn"], { y: 1900, duration: 5 * q, ease: "power4.in" }, Q(30.8) - 5 * q);
          tl.fromTo("#D-cols", { y: -1500, autoAlpha: 1 }, { immediateRender: false, y: 0, autoAlpha: 1, duration: 13 * q, ease: "expo.out" }, Q(30.8) - q);
          cue(30.75, "whoosh", -15);
          pop("#D-i1", 30.82); pop("#D-i2", 31.18);
          tl.to(["#D-i1", "#D-i2"], { opacity: 0.35, duration: 6 * q }, Q(31.8));
          pop("#D-i3", 33.17); pop("#D-i4", 33.36);
          tl.fromTo("#D-yes", { scale: 1 }, { scale: 1.06, duration: 6 * q, ease: "back.out(3)", yoyo: true, repeat: 1 }, Q(33.88));
          cue(33.9, "clique", -20);
          sceneOut("#D", 35.0);

          // ===== F · PASSO 2 → A CELA → O EXTRATO =====
          sceneIn("#F", 37.85); drift("#F-band", 37.85, 49.45);
          chip("F", 39.4, 38.0);
          rise("#F-w1", 39.83); rise("#F-w2", 40.3); rise("#F-w3", 40.46); rise("#F-w4", 40.69); rise("#F-w5", 41.0); sel("F", 41.25);
          smear("#F-chip", 41.89);
          out("#F-title", 41.89);
          zoomIn("#F-cela", 41.89);
          tl.fromTo("#F-cela", { scale: 1 }, { scale: 1.06, duration: 4.5, ease: "none" }, Q(42.1));
          rise("#F-ct", 43.4);
          tl.to(["#F-cela", "#F-ct"], { y: 1900, duration: 5 * q, ease: "power4.in" }, Q(46.6) - 5 * q);
          tl.fromTo("#F-ext", { y: -1500, autoAlpha: 1 }, { immediateRender: false, y: 0, autoAlpha: 1, duration: 13 * q, ease: "expo.out" }, Q(46.6) - q);
          cue(46.55, "whoosh", -15);
          stagger("#F-ext .ln", 47.6, 4);
          tl.fromTo("#F-sal", { scale: 1 }, { scale: 1.08, duration: 6 * q, ease: "back.out(3)", yoyo: true, repeat: 1 }, Q(48.22));
          cue(48.24, "clique", -20);
          sceneOut("#F", 49.45);

          // ===== I · PASSO 3 → A VOLTA =====
          sceneIn("#I", 52.94); drift("#I-band", 52.94, 59.76);
          chip("I", 53.09, 52.96);
          rise("#I-w1", 53.84); rise("#I-w2", 54.02); rise("#I-w3", 54.45); rise("#I-w4", 54.72); rise("#I-w5", 54.75); rise("#I-w6", 54.89); sel("I", 55.1);
          smear("#I-chip", 55.6);
          out("#I-title", 55.6);
          zoomIn("#I-volta", 55.6);
          kenburns("#I-voltaimg", 55.6, 57.87, 1.12, 1.0);
          pop("#I-vt", 56.27);
          whip(["#I-volta", "#I-vt"], "#I-c141", 57.87);
          kenburns("#I-c141img", 57.87, 59.76, 1.0, 1.1);
          sceneOut("#I", 59.76);

          // ===== K · AS FAMÍLIAS ESPERANDO =====
          sceneIn("#K", 62.02);
          kenburns("#K-espimg", 62.02, 64.82, 1.1, 1.0);
          sceneOut("#K", 64.82);

          // ===== L · SPLIT DA VIRADA =====
          splitIn("#L", 64.82);
          kenburns("#L-natalimg", 64.82, 67.97, 1.0, 1.12);
          whip("#L-natal", "#L-st", 67.97);
          kenburns("#L-stimg", 67.97, 70.78, 1.1, 1.0);
          splitOut("#L", 70.78);

          // ===== M · CLÍMAX: O CALENDÁRIO =====
          sceneIn("#M", 70.78); drift("#M-band", 70.78, 82.15);
          tl.fromTo("#M-cal", { y: 900, autoAlpha: 1, rotation: -4 }, { immediateRender: false, y: 0, autoAlpha: 1, rotation: 0, duration: 13 * q, ease: "expo.out" }, Q(70.9));
          cue(70.92, "whoosh", -16);
          tl.to("#M-ok", { opacity: 1, duration: 6 * q }, Q(71.76));
          pop("#M-sai", 72.11);
          // "o Natal chegava e passava"
          tl.to("#M-ok", { opacity: 0, duration: 6 * q }, Q(73.8));
          slam("#M-p1", 74.52, -8);
          tl.to(["#M-p1", "#M-sai"], { autoAlpha: 0, duration: 5 * q }, Q(75.2));
          // os meses passam até a Páscoa
          tl.fromTo("#M-mes", { y: 0 }, { y: -4 * 170, duration: 24 * q, ease: "power3.inOut" }, Q(75.0));
          tl.fromTo("#M-dia", { y: 0 }, { y: -4 * 380, duration: 24 * q, ease: "power3.inOut" }, Q(75.0));
          tl.fromTo("#M-ev", { y: 0 }, { y: -4 * 190, duration: 24 * q, ease: "power3.inOut" }, Q(75.0));
          cue(75.1, "cacaniquel", -20);
          tl.to("#M-ok", { opacity: 1, duration: 6 * q }, Q(75.96));
          pop("#M-sai2", 76.75);
          tl.to("#M-ok", { opacity: 0, duration: 6 * q }, Q(77.6));
          slam("#M-p2", 78.39, 6);
          tl.to("#M-mes", { y: -6 * 170, duration: 14 * q, ease: "power3.inOut" }, Q(78.8));
          tl.to("#M-dia", { y: -6 * 380, duration: 14 * q, ease: "power3.inOut" }, Q(78.8));
          tl.to("#M-ev", { y: -6 * 190, duration: 14 * q, ease: "power3.inOut" }, Q(78.8));
          // "e eles morriam de coração partido"
          tl.to(["#M-cal", "#M-sai2", "#M-p2"], { y: 1900, duration: 5 * q, ease: "power4.in" }, Q(79.39) - 5 * q);
          tl.fromTo("#M-cama", { autoAlpha: 0, scale: 1.15 }, { autoAlpha: 1, scale: 1, duration: 20 * q, ease: "power2.out" }, Q(79.39) - 2 * q);
          kenburns("#M-camaimg", 79.39, 82.15, 1.0, 1.08);
          sceneOut("#M", 82.15);

          // ===== O · O SEU NATAL =====
          sceneIn("#O", 84.75);
          kenburns("#O-natimg", 84.75, 86.97, 1.14, 1.0);
          sceneOut("#O", 86.97);
'''

T = T.replace('            </style>', CSS + '            </style>', 1)
i = T.index('-->', T.index('CENAS (por video)')) + 3
T = T[:i] + HTML + T[i:]
T = T.replace('          // (vazio = camada transparente)', JS, 1)
open('compositions/mg.html', 'w').write(T)
print('compositions/mg.html', len(T), 'bytes')
