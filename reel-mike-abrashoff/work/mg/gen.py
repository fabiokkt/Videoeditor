"""POR VIDEO — reel MIKE ABRASHOFF. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Tempos absolutos de work/tl-words.txt.
Dosagem (docs/05 §24): abertura só com fotos; no corpo foto real é o padrão; motion só nos capítulos (PASSO 1/2/3),
nos números (pior → 1º em 7 meses, o ranking dos motivos com salário em 5º, os 310 um por um) e no mecanismo (o pedido
de demissão que chega tarde). Fotos: Marinha dos EUA (Commons, domínio público) — LICENCAS-FOTOS.txt.
uso: python3 work/mg/gen.py"""
T = open('work/mg/template.html').read()

CSS = r'''
        /* ===== reel MIKE ABRASHOFF ===== */
        #mg .tag { white-space: nowrap; }
        #mg .full img.dim { filter: brightness(.8); }
        #mg .lad { position: absolute; left: 110px; width: 860px; border-radius: 44px; background: #fff; color: #11141A; padding: 34px 40px 30px;
                   box-shadow: 0 34px 90px rgba(0,0,0,.45); }
        #mg .lad .hd { display: flex; justify-content: space-between; font-weight: 800; font-size: 32px; letter-spacing: .08em; margin-bottom: 14px; }
        #mg .lad .hd i { font-style: normal; color: #8C93A1; font-weight: 600; }
        #mg .lad .row { position: relative; display: flex; align-items: center; height: 104px; border-top: 2px solid rgba(128,136,150,.18);
                        font-weight: 800; font-size: 40px; color: #8C93A1; justify-content: flex-start; }
        #mg .lad .row b { width: 230px; flex: none; font-size: 44px; color: #11141A; }
        #mg .lad .row .bar { height: 26px; border-radius: 13px; background: #E3E5E9; }
        #mg .lad .pill { position: absolute; left: 270px; width: auto; min-width: 0; max-width: none; overflow: visible; padding: 0 34px; height: 74px; line-height: 74px; border-radius: 999px; font-weight: 800;
                         font-size: 38px; letter-spacing: .06em; color: #fff; background: #E5322D; white-space: nowrap; box-shadow: 0 10px 30px rgba(0,0,0,.25); }
        #mg .lad .mes { font-weight: 800; font-size: 32px; letter-spacing: .08em; color: #8C93A1; }
        #mg .lad .mes .w { display: inline-block; height: 40px; overflow: hidden; vertical-align: top; }
        #mg .lad .mes .w div span { display: block; height: 40px; line-height: 40px; color: #E5322D; }
        #mg .mot { position: absolute; left: 60px; width: 960px; border-radius: 44px; background: #fff; color: #11141A; padding: 34px 40px 22px;
                   box-shadow: 0 34px 90px rgba(0,0,0,.45); }
        #mg .mot .hd { font-weight: 800; font-size: 30px; letter-spacing: .1em; color: #8C93A1; margin-bottom: 10px; }
        #mg .mot .row { position: relative; display: flex; align-items: center; height: 118px; border-top: 2px solid rgba(128,136,150,.18);
                        font-weight: 800; font-size: 46px; justify-content: flex-start; text-align: left; }
        #mg .mot .row b { width: 120px; font-size: 52px; color: #8C93A1; }
        #mg .mot .row.r1 { color: #1FB45A; } #mg .mot .row.r1 b { color: #1FB45A; }
        #mg .mot .row.r5 { color: #E5322D; } #mg .mot .row.r5 b { color: #E5322D; }
        #mg .mot .row.dimr { color: #A8ADB7; }
        #mg .mot .hl { position: absolute; left: -16px; right: -16px; top: 8px; bottom: 8px; border-radius: 22px; }
        #mg .ctr { position: absolute; left: 0; width: 1080px; text-align: center; color: #fff; font-weight: 800; }
        #mg .ctr .col { display: inline-block; height: 300px; overflow: hidden; vertical-align: top; }
        #mg .ctr .col div span { display: block; height: 300px; line-height: 300px; font-size: 300px; width: 190px; text-align: center; }
        #mg .ctr .un { display: block; font-size: 64px; letter-spacing: .14em; color: #8C93A1; margin-top: 30px; }
        #mg .doc { position: absolute; left: 160px; width: 760px; height: 980px; border-radius: 30px; background: #FBFAF7; color: #11141A;
                   box-shadow: 0 40px 100px rgba(0,0,0,.55); padding: 70px 64px; }
        #mg .doc .t { font-weight: 800; font-size: 54px; letter-spacing: .04em; text-align: center; margin-bottom: 60px; }
        #mg .doc .l { height: 22px; border-radius: 11px; background: #DADCE0; margin-bottom: 34px; }
        #mg .doc .sig { position: absolute; left: 64px; bottom: 120px; width: 300px; border-top: 3px solid #11141A; padding-top: 12px;
                        font-weight: 600; font-size: 28px; color: #5A606B; }
'''

HTML = '''
        <!-- A · SPLIT DA CAPA (0–7,22), nada do Mike/Benfold antes de "Mike": CAPA GERADA A PEDIDO (Codex: oficial de costas descendo
             a prancha do destróier à noite, tripulação comemorando no convés) → canhão de destróier à noite (USS Oscar Austin) -->
        <div class="scene" id="A" style="height:845px">
          <div class="full" id="A-capa"><img id="A-capaimg" src="assets/mg/capa-mike.jpg" style="object-position:30% 50%" /></div>
          <div class="full" id="A-noite"><img id="A-noiteimg" src="assets/mg/noite-canhao.jpg" style="object-position:50% 62%" /></div>
        </div>

        <!-- P · PRÉ-REVELAÇÃO (7,22–10,70): proa furando onda (USS Barry, sem nome legível) -->
        <div class="scene" id="P"><div class="full" id="P-proa"><img id="P-proaimg" class="dim" src="assets/mg/proa-ondas.jpg" style="object-position:50% 50%" /></div></div>

        <!-- B · REVELAÇÃO (12,78–21,27): USS Benfold + nome → pior → 1º em 7 meses → míssil → a mesma tripulação -->
        <div class="scene" id="B"><div class="world dark"><div class="band" id="B-band"></div></div>
          <div class="full" id="B-ben"><img id="B-benimg" src="assets/mg/benfold-mar.jpg" style="object-position:38% 50%" /></div>
          <div class="name" id="B-name" style="top:1060px"><b>MIKE ABRASHOFF</b><i>CAPITÃO DO USS BENFOLD · 1997</i></div>
          <div class="tag" id="B-pior" style="left:150px;top:260px;background:#E5322D">UM DOS PIORES DA MARINHA</div>
          <div class="lad" id="B-lad" style="top:250px">
            <div class="hd"><span>FROTA DO PACÍFICO</span><span class="mes">MÊS <span class="w"><div id="B-mes"><span>0</span><span>2</span><span>4</span><span>6</span><span>7</span></div></span></span></div>
            <div class="row"><b>1º</b><div class="bar" style="width:520px"></div></div>
            <div class="row"><b>2º</b><div class="bar" style="width:470px"></div></div>
            <div class="row"><b>3º</b><div class="bar" style="width:430px"></div></div>
            <div class="row"><b>…</b><div class="bar" style="width:300px"></div></div>
            <div class="row"><b>ÚLTIMOS</b><div class="bar" style="width:180px"></div></div>
            <div class="pill" id="B-pill" style="top:530px">USS BENFOLD</div>
          </div>
          <div class="full" id="B-mis"><img id="B-misimg" src="assets/mg/benfold-missil.jpg" style="object-position:50% 40%" /></div>
          <div class="tag" id="B-n1" style="left:250px;top:1180px;background:#1FB45A">O MAIS PREPARADO</div>
          <div class="full" id="B-tri"><img id="B-triimg" src="assets/mg/benfold-tripulacao.jpg" style="object-position:55% 50%" /></div>
          <div class="tag" id="B-mesma" style="left:230px;top:1180px;background:#11141A">A MESMA TRIPULAÇÃO</div>
        </div>

        <!-- D · PASSO 1 → A CONVERSA → OS MOTIVOS (25,19–36,05) -->
        <div class="scene" id="D"><div class="world light"><div class="band" id="D-band"></div></div>
          <div class="chip" id="D-chip" style="top:300px"><span class="dot" style="background:#1FB45A"></span><div class="win"><div class="roll" id="D-roll"><span>PASSO 3</span><span>PASSO 2</span><span>PASSO 1</span></div></div><div class="plus" id="D-plus">+</div></div>
          <div class="title" id="D-title" style="top:520px"><span id="D-w1">OLHA</span> <span id="D-w2">NA</span> <span id="D-w3">CARA</span><br /><span id="D-w4">DE</span> <span id="D-w5">QUEM</span> <span class="sel" id="D-sel"><span id="D-w6">FALA.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="full" id="D-conv"><img id="D-convimg" src="assets/mg/conversa-oficial.jpg" style="object-position:50% 45%" /></div>
          <div class="tag" id="D-palp" style="left:180px;top:1180px;background:#11141A">O PALPITE DELE: SALÁRIO</div>
          <div class="mot" id="D-mot" style="top:220px">
            <div class="hd">POR QUE O MARINHEIRO VAI EMBORA</div>
            <div class="row r1" id="D-r1"><b>1º</b><span id="D-t1">NÃO SER RESPEITADO</span><div class="hl" id="D-h1" style="box-shadow:inset 0 0 0 6px #1FB45A"></div></div>
            <div class="row dimr" id="D-r2"><b>2º</b>NÃO FAZER DIFERENÇA</div>
            <div class="row dimr" id="D-r3"><b>3º</b>NÃO SER OUVIDO</div>
            <div class="row dimr" id="D-r4"><b>4º</b>SEM RESPONSABILIDADE</div>
            <div class="row r5" id="D-r5"><b>5º</b><span id="D-t5">SALÁRIO</span><div class="hl" id="D-h5" style="box-shadow:inset 0 0 0 6px #E5322D"></div></div>
          </div>
        </div>

        <!-- F · PASSO 2 → OS 310 (39,40–45,30) -->
        <div class="scene" id="F"><div class="world dark"><div class="band" id="F-band"></div></div>
          <div class="chip" id="F-chip" style="top:300px;background:#fff;color:#11141A"><span class="dot" style="background:#F2B705"></span><div class="win"><div class="roll" id="F-roll"><span>PASSO 1</span><span>PASSO 3</span><span>PASSO 2</span></div></div><div class="plus" id="F-plus" style="background:#fff;color:#11141A">+</div></div>
          <div class="title" id="F-title" style="top:520px;color:#fff"><span id="F-w1">O</span> <span id="F-w2">QUE</span> <span id="F-w3">VOCÊ</span><br /><span class="sel" id="F-sel"><span id="F-w4">MUDARIA?</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="ctr" id="F-ctr" style="top:380px"><span class="col"><div id="F-c1"><span>0</span><span>1</span><span>2</span><span>3</span></div></span><span class="col"><div id="F-c2"><span>0</span><span>5</span><span>9</span><span>3</span><span>7</span><span>1</span></div></span><span class="col"><div id="F-c3"><span>0</span><span>4</span><span>8</span><span>2</span><span>6</span><span>0</span></div></span><span class="un">MARINHEIROS</span></div>
          <div class="tag" id="F-um" style="left:350px;top:1000px;background:#F2B705;color:#11141A">UM POR UM</div>
        </div>

        <!-- G · A TINTA E O PARAFUSO (49,35–57,15) -->
        <div class="scene" id="G">
          <div class="full" id="G-pint"><img id="G-pintimg" class="dim" src="assets/mg/pintura-casco.jpg" style="object-position:62% 50%" /></div>
          <div class="tag" id="G-2m" style="left:270px;top:1180px;background:#E5322D">A CADA 2 MESES</div>
          <div class="full" id="G-fer"><img id="G-ferimg" class="dim" src="assets/mg/ferrugem.jpg" style="object-position:40% 50%" /></div>
          <div class="tag" id="G-par" style="left:200px;top:1180px;background:#11141A">PARAFUSO ENFERRUJADO</div>
          <div class="full" id="G-sil"><img id="G-silimg" src="assets/mg/benfold-silhuetas.jpg" style="object-position:40% 50%" /></div>
          <div class="tag" id="G-novo" style="left:230px;top:1180px;background:#1FB45A">PARAFUSO TROCADO</div>
          <div class="stamp" data-layout-allow-overlap id="G-cop" style="left:150px;top:420px;font-size:84px">A MARINHA COPIOU</div>
        </div>

        <!-- H · PASSO 3 → O REENGAJAMENTO (57,15–62,68) -->
        <div class="scene" id="H"><div class="world light"><div class="band" id="H-band"></div></div>
          <div class="chip" id="H-chip" style="top:300px"><span class="dot" style="background:#E5322D"></span><div class="win"><div class="roll" id="H-roll"><span>PASSO 2</span><span>PASSO 1</span><span>PASSO 3</span></div></div><div class="plus" id="H-plus">+</div></div>
          <div class="title" id="H-title" style="top:520px"><span id="H-w1">PEDE</span> <span id="H-w2">PRA</span><br /><span class="sel" id="H-sel"><span id="H-w3">FICAR.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="full" id="H-ree"><img id="H-reeimg" src="assets/mg/reengajamento.jpg" style="object-position:6% 40%" /></div>
          <div class="tag" id="H-ant" style="left:150px;top:1180px;background:#11141A">ANTES DO CONTRATO ACABAR</div>
        </div>

        <!-- K · O PEDIDO DE DEMISSÃO (64,34–67,10) -->
        <div class="scene" id="K"><div class="world dark"><div class="band" id="K-band"></div></div>
          <div class="doc" id="K-doc" style="top:170px">
            <div class="t">PEDIDO DE DEMISSÃO</div>
            <div class="l" style="width:100%"></div><div class="l" style="width:92%"></div><div class="l" style="width:97%"></div>
            <div class="l" style="width:70%"></div><div class="l" style="width:88%"></div><div class="l" style="width:54%"></div>
            <div class="sig">assinatura</div>
          </div>
          <div class="stamp" data-layout-allow-overlap id="K-tarde" style="left:200px;top:560px;font-size:100px">TARDE DEMAIS</div>
        </div>

        <!-- L · SPLIT DA VIRADA (70,75–78,55): troca de comando → o capitão antigo sai → a tripulação comemora -->
        <div class="scene" id="L" style="height:845px">
          <div class="full" id="L-troca"><img id="L-trocaimg" src="assets/mg/troca-comando.jpg" style="object-position:50% 45%" /></div>
          <div class="full" id="L-sai"><img id="L-saiimg" src="assets/mg/sai-do-navio.jpg" style="object-position:50% 35%" /></div>
          <div class="full" id="L-com"><img id="L-comimg" src="assets/mg/comemoram.jpg" style="object-position:60% 50%" /></div>
        </div>

        <!-- M · CLÍMAX (81,44–87,98): a continência → nenhum olho seco -->
        <div class="scene" id="M">
          <div class="full" id="M-cont"><img id="M-contimg" src="assets/mg/continencia-saida.jpg" style="object-position:50% 35%" /></div>
          <div class="tag" id="M-dois" style="left:220px;top:1180px;background:#11141A">DOIS ANOS DEPOIS · 1999</div>
          <div class="full" id="M-abr"><img id="M-abrimg" src="assets/mg/abraco-cais.jpg" style="object-position:45% 40%" /></div>
        </div>

        <!-- O · A MESMA TRIPULAÇÃO (92,39–94,95): volta da revelação -->
        <div class="scene" id="O"><div class="full" id="O-tri"><img id="O-triimg" src="assets/mg/benfold-tripulacao.jpg" style="object-position:45% 50%" /></div></div>
'''

JS = r'''
          gsap.set(["#A-noite",
                    "#B-name", "#B-pior", "#B-lad", "#B-mis", "#B-n1", "#B-tri", "#B-mesma",
                    "#D-chip", "#D-w1", "#D-w2", "#D-w3", "#D-w4", "#D-w5", "#D-w6", "#D-conv", "#D-palp", "#D-mot",
                    "#D-r1", "#D-r2", "#D-r3", "#D-r4", "#D-r5", "#D-h1", "#D-h5",
                    "#F-chip", "#F-w1", "#F-w2", "#F-w3", "#F-w4", "#F-ctr", "#F-um",
                    "#G-2m", "#G-fer", "#G-par", "#G-sil", "#G-novo", "#G-cop",
                    "#H-chip", "#H-w1", "#H-w2", "#H-w3", "#H-ree", "#H-ant",
                    "#K-doc", "#K-tarde",
                    "#L-sai", "#L-com",
                    "#M-dois", "#M-abr"], { autoAlpha: 0 });
          gsap.set(["#D-sel", "#F-sel", "#H-sel"], { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set(["#D-sel .h", "#F-sel .h", "#H-sel .h"], { scale: 0 });
          function sel(base, t) {
            tl.to("#" + base + "-sel", { borderColor: "rgba(242,183,5,1)", backgroundColor: "rgba(242,183,5,.16)", duration: 4 * q, ease: "none" }, Q(t));
            tl.to("#" + base + "-sel .h", { scale: 1, duration: 6 * q, ease: "back.out(3)", stagger: q }, Q(t) + q);
          }
          function out(sel_, t) { tl.to(sel_, { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(t) - 5 * q); }

          // ===== A · CAPA (quadro 0 = capa) → SÓ FOTOS, nada do Mike =====
          splitIn("#A", 0, true);
          kenburns("#A-capaimg", 0, 5.28, 1.12, 1.0);
          whip("#A-capa", "#A-noite", 5.28);
          kenburns("#A-noiteimg", 5.28, 7.22, 1.0, 1.1);
          splitOut("#A", 7.22);

          // ===== P · PRÉ-REVELAÇÃO =====
          sceneIn("#P", 7.22);
          kenburns("#P-proaimg", 7.22, 10.7, 1.14, 1.0);
          sceneOut("#P", 10.7);

          // ===== B · REVELAÇÃO ("Mike" 12,71 → 12,78) =====
          sceneIn("#B", 12.78); drift("#B-band", 12.78, 21.27);
          kenburns("#B-benimg", 12.78, 15.51, 1.12, 1.0);
          rise("#B-name", 12.98);
          pop("#B-pior", 13.66);
          // "Sete meses depois, era o mais preparado": do fundo da frota ao topo
          drop(["#B-ben", "#B-name", "#B-pior"], "#B-lad", 15.51);
          tl.fromTo("#B-mes", { y: 0 }, { y: -4 * 40, duration: 24 * q, ease: "power3.inOut" }, Q(15.73));
          tl.fromTo("#B-pill", { y: 0 }, { y: -416, duration: 22 * q, ease: "power4.inOut" }, Q(16.2));
          tl.to("#B-pill", { backgroundColor: "#1FB45A", duration: 6 * q }, Q(16.9));
          cue(16.2, "cacaniquel", -20); cue(16.95, "clique", -19);
          whip("#B-lad", "#B-mis", 17.99);
          kenburns("#B-misimg", 17.99, 19.66, 1.0, 1.12);
          pop("#B-n1", 18.2);
          whip(["#B-mis", "#B-n1"], "#B-tri", 19.66);
          kenburns("#B-triimg", 19.66, 21.27, 1.12, 1.0);
          pop("#B-mesma", 20.02);
          sceneOut("#B", 21.27);

          // ===== D · PASSO 1 → A CONVERSA → OS MOTIVOS =====
          sceneIn("#D", 25.19); drift("#D-band", 25.19, 36.05);
          chip("D", 25.45, 25.22);
          rise("#D-w1", 25.62); rise("#D-w2", 25.92); rise("#D-w3", 26.08); rise("#D-w4", 26.38); rise("#D-w5", 26.66); rise("#D-w6", 26.84); sel("D", 27.05);
          smear("#D-chip", 27.6);
          out("#D-title", 27.6);
          zoomIn("#D-conv", 27.6);
          kenburns("#D-convimg", 27.6, 30.34, 1.0, 1.1);
          pop("#D-palp", 29.43);
          drop(["#D-conv", "#D-palp"], "#D-mot", 30.34);
          pop("#D-r5", 31.95);
          tl.fromTo("#D-h5", { autoAlpha: 0, scale: 1.08 }, { autoAlpha: 1, scale: 1, duration: 6 * q, ease: "back.out(3)" }, Q(32.35));
          cue(32.37, "clique", -20);
          stagger(["#D-r4", "#D-r3", "#D-r2"], 32.9, 3, 3);
          tl.to("#D-h5", { autoAlpha: 0, duration: 6 * q }, Q(33.3));
          pop("#D-r1", 33.41);
          tl.fromTo("#D-h1", { autoAlpha: 0, scale: 1.08 }, { autoAlpha: 1, scale: 1, duration: 6 * q, ease: "back.out(3)" }, Q(35.08));
          tl.fromTo("#D-r1", { scale: 1 }, { scale: 1.05, duration: 6 * q, ease: "back.out(3)", yoyo: true, repeat: 1 }, Q(35.08));
          cue(35.1, "clique", -19);
          sceneOut("#D", 36.05);

          // ===== F · PASSO 2 → OS 310 =====
          sceneIn("#F", 39.4); drift("#F-band", 39.4, 45.3);
          chip("F", 39.62, 39.42);
          rise("#F-w1", 40.58); rise("#F-w2", 40.76); rise("#F-w3", 40.85); rise("#F-w4", 41.11); sel("F", 41.4);
          smear("#F-chip", 42.0);
          out("#F-title", 42.0);
          tl.fromTo("#F-ctr", { y: -900, autoAlpha: 1 }, { immediateRender: false, y: 0, autoAlpha: 1, duration: 13 * q, ease: "expo.out" }, Q(42.0) - q);
          cue(41.95, "whoosh", -15);
          tl.fromTo("#F-c1", { y: 0 }, { y: -3 * 300, duration: 36 * q, ease: "power4.out" }, Q(42.3));
          tl.fromTo("#F-c2", { y: 0 }, { y: -5 * 300, duration: 38 * q, ease: "power4.out" }, Q(42.3));
          tl.fromTo("#F-c3", { y: 0 }, { y: -5 * 300, duration: 40 * q, ease: "power4.out" }, Q(42.3));
          cue(42.3, "cacaniquel", -20);
          pop("#F-um", 44.06);
          sceneOut("#F", 45.3);

          // ===== G · A TINTA E O PARAFUSO =====
          sceneIn("#G", 49.35);
          kenburns("#G-pintimg", 49.35, 52.37, 1.0, 1.12);
          pop("#G-2m", 51.19);
          whip(["#G-pint", "#G-2m"], "#G-fer", 52.37);
          kenburns("#G-ferimg", 52.37, 53.98, 1.12, 1.0);
          pop("#G-par", 52.79);
          drop(["#G-fer", "#G-par"], "#G-sil", 53.98);
          kenburns("#G-silimg", 53.98, 57.15, 1.0, 1.1);
          pop("#G-novo", 54.26);
          slam("#G-cop", 56.33, -6);
          sceneOut("#G", 57.15);

          // ===== H · PASSO 3 → O REENGAJAMENTO =====
          sceneIn("#H", 57.15); drift("#H-band", 57.15, 62.68);
          chip("H", 57.4, 57.18);
          rise("#H-w1", 57.95); rise("#H-w2", 58.28); rise("#H-w3", 58.53); sel("H", 58.8);
          smear("#H-chip", 59.38);
          out("#H-title", 59.38);
          zoomIn("#H-ree", 59.38);
          kenburns("#H-reeimg", 59.38, 62.68, 1.0, 1.1);
          pop("#H-ant", 59.89);
          sceneOut("#H", 62.68);

          // ===== K · O PEDIDO DE DEMISSÃO =====
          sceneIn("#K", 64.34); drift("#K-band", 64.34, 67.1);
          tl.fromTo("#K-doc", { y: 900, autoAlpha: 1, rotation: 5 }, { immediateRender: false, y: 0, autoAlpha: 1, rotation: -2, duration: 13 * q, ease: "expo.out" }, Q(64.4));
          cue(64.42, "whoosh", -16);
          slam("#K-tarde", 66.2, -8);
          sceneOut("#K", 67.1);

          // ===== L · SPLIT DA VIRADA =====
          splitIn("#L", 70.75);
          kenburns("#L-trocaimg", 70.75, 74.1, 1.0, 1.12);
          whip("#L-troca", "#L-sai", 74.1);
          kenburns("#L-saiimg", 74.1, 76.79, 1.12, 1.0);
          whip("#L-sai", "#L-com", 76.79);
          kenburns("#L-comimg", 76.79, 78.55, 1.0, 1.1);
          splitOut("#L", 78.55);

          // ===== M · CLÍMAX: A CONTINÊNCIA =====
          sceneIn("#M", 81.44);
          kenburns("#M-contimg", 81.44, 85.34, 1.14, 1.0);
          pop("#M-dois", 81.83);
          tl.to(["#M-cont", "#M-dois"], { autoAlpha: 0, duration: 14 * q }, Q(85.34));
          tl.fromTo("#M-abr", { autoAlpha: 0, scale: 1.15 }, { autoAlpha: 1, scale: 1, duration: 20 * q, ease: "power2.out" }, Q(85.34) - 2 * q);
          kenburns("#M-abrimg", 85.34, 87.98, 1.0, 1.08);
          sceneOut("#M", 87.98);

          // ===== O · A MESMA TRIPULAÇÃO =====
          sceneIn("#O", 92.39);
          kenburns("#O-triimg", 92.39, 94.95, 1.12, 1.0);
          sceneOut("#O", 94.95);
'''

T = T.replace('            </style>', CSS + '            </style>', 1)
i = T.index('-->', T.index('CENAS (por video)')) + 3
T = T[:i] + HTML + T[i:]
T = T.replace('          // (vazio = camada transparente)', JS, 1)
open('compositions/mg.html', 'w').write(T)
print('compositions/mg.html', len(T), 'bytes')
