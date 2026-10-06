"""POR VIDEO — reel HYMAN RICKOVER. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Tempos absolutos de work/tl-words.txt.
Dosagem (docs/05 §24): abertura só com fotos (capa gerada + estaleiro); no corpo foto real é o padrão; motion só no mecanismo
(a cadeira de pés serrados), nos capítulos (PASSO 1/2/3), no objeto que a fala nomeia (a tarefa com responsável: o comercial,
o pessoal, o João), no número (99% do tempo) e no vendedor sem venda há 6 meses (~30% da cobertura).
Fotos: Marinha dos EUA / NARA / biblioteca presidencial (Commons, domínio público) — LICENCAS-FOTOS.txt.
uso: python3 work/mg/gen.py"""
T = open('work/mg/template.html').read()

CSS = r'''
        /* ===== reel HYMAN RICKOVER ===== */
        #mg .tag { white-space: nowrap; }
        #mg .full img.dim { filter: brightness(.78); }
        /* a cadeira de pés serrados (SVG) */
        #mg .chairbox { position: absolute; left: 190px; top: 250px; width: 700px; height: 760px; }
        #mg .chairbox svg { position: absolute; left: 0; top: 0; overflow: visible; }
        #mg .saw { position: absolute; left: 430px; top: 616px; width: 150px; height: 0; border-top: 9px dashed #E5322D; transform-origin: 0 50%; }
        /* tarefa com responsável */
        #mg .task { position: absolute; left: 100px; width: 880px; border-radius: 44px; background: #fff; color: #11141A; padding: 40px 48px 30px;
                    box-shadow: 0 34px 90px rgba(0,0,0,.35); }
        #mg .task .hd { display: flex; align-items: center; gap: 18px; font-weight: 800; font-size: 30px; letter-spacing: .12em; color: #8C93A1; }
        #mg .task .hd i { width: 34px; height: 34px; border-radius: 10px; border: 5px solid #C9CCD2; display: block; }
        #mg .task .tt { font-weight: 800; font-size: 60px; margin: 16px 0 34px; }
        #mg .task .lab { font-weight: 800; font-size: 28px; letter-spacing: .14em; color: #8C93A1; margin-bottom: 6px; }
        #mg .task .opt { position: relative; height: 122px; display: flex; align-items: center; gap: 26px; font-weight: 800; font-size: 52px;
                         border-top: 2px solid rgba(128,136,150,.18); }
        #mg .task .opt .av { width: 78px; height: 78px; border-radius: 50%; background: #C9CCD2; color: #fff; font-size: 40px; line-height: 78px;
                             text-align: center; flex: none; }
        #mg .task .opt .st { position: absolute; left: 96px; top: 56px; height: 12px; border-radius: 6px; background: #E5322D; transform-origin: 0 50%; }
        #mg .task .opt.ok .av { background: #1FB45A; }
        #mg .task .opt .dono { margin-left: auto; padding: 0 30px; height: 70px; line-height: 70px; border-radius: 999px; background: #1FB45A; color: #fff;
                               font-size: 32px; letter-spacing: .08em; }
        /* contador 99% */
        #mg .dkp { position: absolute; inset: 0; background: radial-gradient(130% 80% at 50% 28%, #1B2130 0%, #0C0F15 68%); }
        #mg .ctr { position: absolute; left: 0; width: 1080px; text-align: center; color: #fff; font-weight: 800; }
        #mg .ctr .col { display: inline-block; height: 320px; overflow: hidden; vertical-align: top; }
        #mg .ctr .col div span { display: block; height: 320px; line-height: 320px; font-size: 330px; width: 210px; text-align: center; }
        #mg .ctr .pc { display: inline-block; height: 320px; line-height: 320px; font-size: 200px; vertical-align: top; color: #F2B705; margin-left: 8px; }
        #mg .lbl2 { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; letter-spacing: .1em; }
        /* vendas zeradas */
        #mg .sales { position: absolute; left: 80px; width: 920px; border-radius: 44px; background: #fff; color: #11141A; padding: 38px 46px 30px;
                     box-shadow: 0 34px 90px rgba(0,0,0,.45); }
        #mg .sales .hd { display: flex; justify-content: space-between; font-weight: 800; font-size: 30px; letter-spacing: .1em; color: #8C93A1; }
        #mg .sales .big { font-weight: 800; font-size: 130px; color: #E5322D; margin: 6px 0 4px; }
        #mg .sales .sb { position: relative; height: 280px; display: flex; align-items: flex-end; gap: 26px; border-bottom: 4px solid #E3E5E9; }
        #mg .sales .sb i { flex: 1; height: 14px; border-radius: 8px 8px 3px 3px; background: #E5322D; transform-origin: 50% 100%; display: block; }
        #mg .sales .ms { display: flex; gap: 26px; margin-top: 14px; }
        #mg .sales .ms span { flex: 1; text-align: center; font-weight: 800; font-size: 30px; color: #8C93A1; letter-spacing: .06em; }
'''

CHAIR = '''<svg width="700" height="760" viewBox="0 0 700 760">
              <rect x="40" y="702" width="620" height="6" rx="3" fill="rgba(255,255,255,.22)" />
              <g id="B-chairg">
                <rect x="190" y="40" width="32" height="662" rx="9" fill="#B8783F" />
                <rect x="180" y="40" width="52" height="150" rx="12" fill="#C98A4B" />
                <rect x="186" y="378" width="336" height="36" rx="9" fill="#D9A062" />
                <rect x="206" y="560" width="290" height="16" rx="7" fill="#9C6533" />
                <rect x="480" y="414" width="32" height="206" fill="#B8783F" />
                <rect id="B-cutend" x="480" y="612" width="32" height="8" fill="#F3DDB2" />
              </g>
              <rect id="B-piece" x="480" y="620" width="32" height="82" rx="4" fill="#B8783F" />
            </svg>'''

HTML = '''
        <!-- A · SPLIT DA CAPA (0–5,52), nada do Rickover antes de "Hyman": CAPA GERADA A PEDIDO (Codex: velho de costas na mesa,
             cadeira de pés serrados sob uma lâmpada) — só a capa durante o gancho -->
        <div class="scene" id="A" style="height:845px">
          <div class="full" id="A-capa"><img id="A-capaimg" src="assets/mg/capa-rickover.jpg" style="object-position:50% 50%" /></div>
        </div>

        <!-- P · PRÉ-REVELAÇÃO (5,52–10,45): Nautilus em construção (1953) → operário no casco (Electric Boat) -->
        <div class="scene" id="P">
          <div class="full" id="P-naut"><img id="P-nautimg" class="dim" src="assets/mg/nautilus-construcao.jpg" style="object-position:50% 50%" /></div>
          <div class="full" id="P-est"><img id="P-estimg" class="dim" src="assets/mg/estaleiro-casco.jpg" style="object-position:50% 50%" /></div>
        </div>

        <!-- B · REVELAÇÃO (12,13–19,67): retrato + nome → a cadeira serrada → USS Ohio (1981) + DEMITIDO + AOS 82 ANOS -->
        <div class="scene" id="B"><div class="world dark"><div class="band" id="B-band"></div></div>
          <div class="full" id="B-r65"><img id="B-r65img" src="assets/mg/rickover-1965.jpg" style="object-position:50% 30%" /></div>
          <div class="name" id="B-name" style="top:1090px"><b>HYMAN RICKOVER</b><i>ALMIRANTE · MARINHA DOS EUA</i></div>
          <div class="chairbox" id="B-chair">''' + CHAIR + '''
            <div class="saw" id="B-saw"></div>
          </div>
          <div class="tag" id="B-pes" style="left:200px;top:1110px;background:#E5322D">PÉS DA FRENTE SERRADOS</div>
          <div class="full" id="B-ohio"><img id="B-ohioimg" src="assets/mg/rickover-ohio-1981.jpg" style="object-position:46% 50%" /></div>
          <div class="stamp" data-layout-allow-overlap id="B-dem" style="left:230px;top:1010px;font-size:104px">DEMITIDO</div>
          <div class="tag" id="B-82" style="left:330px;top:1230px;background:#11141A">AOS 82 ANOS</div>
        </div>

        <!-- D · PASSO 1 → A TAREFA COM DONO → O RETRATO DE 1955 (23,70–34,33) -->
        <div class="scene" id="D"><div class="world light"><div class="band" id="D-band"></div></div>
          <div class="chip" id="D-chip" style="top:300px"><span class="dot" style="background:#1FB45A"></span><div class="win"><div class="roll" id="D-roll"><span>PASSO 3</span><span>PASSO 2</span><span>PASSO 1</span></div></div><div class="plus" id="D-plus">+</div></div>
          <div class="title" id="D-title" style="top:520px"><span id="D-w1">TODA</span> <span id="D-w2">TAREFA</span><br /><span id="D-w3">TEM</span> <span id="D-w4">UM</span> <span class="sel" id="D-sel"><span id="D-w5">NOME.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="task" id="D-task" style="top:260px">
            <div class="hd"><i></i>TAREFA</div>
            <div class="tt">Proposta do cliente</div>
            <div class="lab">RESPONSÁVEL</div>
            <div class="opt" id="D-o1"><span class="av">?</span>O COMERCIAL<i class="st" id="D-s1" style="width:430px"></i></div>
            <div class="opt" id="D-o2"><span class="av">?</span>O PESSOAL<i class="st" id="D-s2" style="width:350px"></i></div>
            <div class="opt ok" id="D-o3"><span class="av">J</span>JOÃO<span class="dono" id="D-dono">✓ DONO</span></div>
          </div>
          <div class="full" id="D-r55"><img id="D-r55img" src="assets/mg/rickover-1955.jpg" style="object-position:50% 30%" /></div>
          <div class="tag" id="D-quem" style="left:290px;top:1180px;background:#11141A">DE QUEM ERA?</div>
        </div>

        <!-- F · PASSO 2 → O REATOR → 99% DO TEMPO → O ESTALEIRO (36,77–50,45) -->
        <div class="scene" id="F"><div class="world light"><div class="band" id="F-band"></div></div>
          <div class="chip" id="F-chip" style="top:300px"><span class="dot" style="background:#F2B705"></span><div class="win"><div class="roll" id="F-roll"><span>PASSO 1</span><span>PASSO 3</span><span>PASSO 2</span></div></div><div class="plus" id="F-plus">+</div></div>
          <div class="title" id="F-title" style="top:520px"><span id="F-w1">CUIDA</span> <span id="F-w2">DO</span><br /><span class="sel" id="F-sel"><span id="F-w3">DETALHE.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="full" id="F-reat"><img id="F-reatimg" src="assets/mg/rickover-reator.jpg" style="object-position:22% 50%" /></div>
          <div class="dkp" id="F-dk">
            <div class="ctr" style="top:330px"><span class="col"><div id="F-c1"><span>0</span><span>3</span><span>6</span><span>8</span><span>9</span></div></span><span class="col"><div id="F-c2"><span>0</span><span>4</span><span>1</span><span>7</span><span>2</span><span>9</span></div></span><span class="pc">%</span></div>
            <div class="lbl2" id="F-tempo" style="top:690px;font-size:76px;color:#fff">DO TEMPO</div>
            <div class="lbl2" id="F-outros" style="top:830px;font-size:42px;color:#8C93A1">NO QUE OS OUTROS CHAMAM DE</div>
            <div class="stamp" data-layout-allow-overlap id="F-best" style="left:205px;top:940px;font-size:110px">BESTEIRA</div>
          </div>
          <div class="full" id="F-est"><img id="F-estimg" src="assets/mg/rickover-estaleiro.jpg" style="object-position:68% 40%" /></div>
        </div>

        <!-- H · PASSO 3 → TORCER PRA DAR CERTO (o Nautilus no mar, 1955) → AS VENDAS ZERADAS (52,21–61,37) -->
        <div class="scene" id="H"><div class="world dark"><div class="band" id="H-band"></div></div>
          <div class="chip" id="H-chip" style="top:300px;background:#fff;color:#11141A"><span class="dot" style="background:#E5322D"></span><div class="win"><div class="roll" id="H-roll"><span>PASSO 2</span><span>PASSO 1</span><span>PASSO 3</span></div></div><div class="plus" id="H-plus" style="background:#fff;color:#11141A">+</div></div>
          <div class="title" id="H-title" style="top:520px;color:#fff"><span id="H-w1">PARA</span> <span id="H-w2">DE</span><br /><span class="sel" id="H-sel"><span id="H-w3">TORCER.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="full" id="H-lanc"><img id="H-lancimg" src="assets/mg/nautilus-mar.jpg" style="object-position:50% 50%" /></div>
          <div class="sales" id="H-sales" style="top:250px">
            <div class="hd"><span>VENDAS DO VENDEDOR</span><span>POR MÊS</span></div>
            <div class="big">R$ 0</div>
            <div class="sb" id="H-sb"><i></i><i></i><i></i><i></i><i></i><i></i></div>
            <div class="ms"><span>JAN</span><span>FEV</span><span>MAR</span><span>ABR</span><span>MAI</span><span>JUN</span></div>
          </div>
          <div class="tag" id="H-6m" style="left:340px;top:1120px;background:#E5322D">6 MESES</div>
        </div>

        <!-- L · SPLIT DA VIRADA (65,23–71,41): a cadeira vazia da entrevista (capa) → formatura de um guarda-marinha em 1946 -->
        <div class="scene" id="L" style="height:845px">
          <div class="full" id="L-sala"><img id="L-salaimg" src="assets/mg/capa-rickover.jpg" style="object-position:72% 45%" /></div>
          <div class="full" id="L-form"><img id="L-formimg" src="assets/mg/carter-formatura-1946.jpg" style="object-position:50% 30%" /></div>
        </div>

        <!-- N · "VOCÊ DEU O SEU MELHOR?" (71,41–73,65): Rickover encarando (USS Virginia, 1974) -->
        <div class="scene" id="N"><div class="full" id="N-vir"><img id="N-virimg" src="assets/mg/rickover-virginia-1974.jpg" style="object-position:67% 50%" /></div></div>

        <!-- M · "E VIROU A CADEIRA" → CLÍMAX (78,73–82,88): o velho de costas (capa) → o presidente + nome → os dois em 1977 -->
        <div class="scene" id="M"><div class="world dark"></div>
          <div class="full" id="M-costas"><img id="M-costasimg" src="assets/mg/capa-rickover.jpg" style="object-position:8% 50%" /></div>
          <div class="full" id="M-pres"><img id="M-presimg" src="assets/mg/carter-presidente.jpg" style="object-position:50% 20%" /></div>
          <div class="name" id="M-name" style="top:1090px"><b>JIMMY CARTER</b><i>39º PRESIDENTE DOS EUA</i></div>
          <div class="full" id="M-juntos"><img id="M-juntosimg" src="assets/mg/carter-rickover-1977.jpg" style="object-position:67% 50%" /></div>
          <div class="tag" id="M-1977" style="left:175px;top:1180px;background:#11141A">CARTER E RICKOVER · 1977</div>
        </div>

        <!-- O · "E VOCÊ? POR QUE NÃO?" → O MAIS OU MENOS (84,85–88,95): Rickover encarando (Nautilus) → operário no casco -->
        <div class="scene" id="O">
          <div class="full" id="O-olha"><img id="O-olhaimg" src="assets/mg/rickover-nautilus.jpg" style="object-position:68% 20%" /></div>
          <div class="full" id="O-est"><img id="O-estimg" class="dim" src="assets/mg/estaleiro-casco.jpg" style="object-position:50% 50%" /></div>
        </div>
'''

JS = r'''
          gsap.set(["#P-est",
                    "#B-name", "#B-chair", "#B-pes", "#B-ohio", "#B-dem", "#B-82",
                    "#D-chip", "#D-w1", "#D-w2", "#D-w3", "#D-w4", "#D-w5", "#D-task", "#D-o1", "#D-o2", "#D-o3", "#D-dono", "#D-r55", "#D-quem",
                    "#F-chip", "#F-w1", "#F-w2", "#F-w3", "#F-reat", "#F-dk", "#F-tempo", "#F-outros", "#F-best", "#F-est",
                    "#H-chip", "#H-w1", "#H-w2", "#H-w3", "#H-lanc", "#H-sales", "#H-6m",
                    "#L-form",
                    "#M-pres", "#M-name", "#M-juntos", "#M-1977",
                    "#O-est"], { autoAlpha: 0 });
          gsap.set(["#D-sel", "#F-sel", "#H-sel"], { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set(["#D-sel .h", "#F-sel .h", "#H-sel .h"], { scale: 0 });
          gsap.set(["#D-s1", "#D-s2"], { scaleX: 0 });
          gsap.set("#B-saw", { scaleX: 0 });
          gsap.set("#B-cutend", { autoAlpha: 0 });
          gsap.set("#H-sb i", { scaleY: 0 });
          function sel(base, t) {
            tl.to("#" + base + "-sel", { borderColor: "rgba(242,183,5,1)", backgroundColor: "rgba(242,183,5,.16)", duration: 4 * q, ease: "none" }, Q(t));
            tl.to("#" + base + "-sel .h", { scale: 1, duration: 6 * q, ease: "back.out(3)", stagger: q }, Q(t) + q);
          }
          function out(sel_, t) { tl.to(sel_, { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(t) - 5 * q); }
          function risca(id, t) { tl.to(id, { scaleX: 1, duration: 5 * q, ease: "power3.out" }, Q(t)); cue(t + 0.03, "clique", -20); }

          // ===== A · CAPA (quadro 0 = capa) → SÓ A CAPA durante o gancho =====
          splitIn("#A", 0, true);
          kenburns("#A-capaimg", 0, 5.52, 1.0, 1.08);
          splitOut("#A", 5.52);

          // ===== P · PRÉ-REVELAÇÃO (só fotos, nada do Rickover) =====
          sceneIn("#P", 5.52);
          kenburns("#P-nautimg", 5.52, 7.7, 1.12, 1.0);
          whip("#P-naut", "#P-est", 7.7);
          kenburns("#P-estimg", 7.7, 10.45, 1.0, 1.1);
          sceneOut("#P", 10.45);

          // ===== B · REVELAÇÃO ("Hyman" 12,03 → 12,13) =====
          sceneIn("#B", 12.13); drift("#B-band", 12.13, 19.67);
          kenburns("#B-r65img", 12.13, 13.4, 1.12, 1.0);
          rise("#B-name", 12.3);
          // "serrava a cadeira pro candidato escorregar": a perna da frente é serrada, o pedaço cai e a cadeira inclina
          drop(["#B-r65", "#B-name"], "#B-chair", 13.4);
          tl.to("#B-saw", { scaleX: 1, duration: 6 * q, ease: "power2.inOut" }, Q(13.62));
          cue(13.64, "swish", -17); cue(13.8, "swish", -18);
          tl.to("#B-saw", { autoAlpha: 0, duration: 3 * q }, Q(13.88));
          tl.to("#B-cutend", { autoAlpha: 1, duration: 2 * q }, Q(13.88));
          tl.to("#B-piece", { x: 70, y: 40, rotation: 70, svgOrigin: "496 660", autoAlpha: 0, duration: 9 * q, ease: "power2.in" }, Q(13.88));
          tl.to("#B-chairg", { rotation: 15, svgOrigin: "206 702", duration: 14 * q, ease: "bounce.out" }, Q(14.04));
          cue(14.1, "impacto", -19, { dur: 0.6 });
          pop("#B-pes", 14.45);
          whip(["#B-chair", "#B-pes"], "#B-ohio", 15.81);
          kenburns("#B-ohioimg", 15.81, 19.67, 1.0, 1.12);
          slam("#B-dem", 17.36, -6);
          pop("#B-82", 18.21);
          sceneOut("#B", 19.67);

          // ===== D · PASSO 1 → A TAREFA COM DONO → O RETRATO =====
          sceneIn("#D", 23.7); drift("#D-band", 23.7, 34.33);
          chip("D", 23.95, 23.72);
          rise("#D-w1", 24.25); rise("#D-w2", 24.4); rise("#D-w3", 24.86); rise("#D-w4", 25.08); rise("#D-w5", 25.24); sel("D", 25.45);
          smear("#D-chip", 26.1);
          out("#D-title", 26.1);
          zoomIn("#D-task", 26.1);
          pop("#D-o1", 26.72, { x: -60, autoAlpha: 0 });
          risca("#D-s1", 27.8);
          tl.to("#D-o1", { opacity: 0.35, duration: 6 * q }, Q(27.95));
          pop("#D-o2", 28.37, { x: -60, autoAlpha: 0 });
          risca("#D-s2", 29.1);
          tl.to("#D-o2", { opacity: 0.35, duration: 6 * q }, Q(29.2));
          pop("#D-o3", 29.32, { x: -60, autoAlpha: 0 });
          pop("#D-dono", 29.5, null, "clique");
          whip("#D-task", "#D-r55", 29.99);
          kenburns("#D-r55img", 29.99, 34.33, 1.0, 1.12);
          pop("#D-quem", 31.96);
          sceneOut("#D", 34.33);

          // ===== F · PASSO 2 → O REATOR → 99% DO TEMPO → O ESTALEIRO =====
          sceneIn("#F", 36.77); drift("#F-band", 36.77, 50.45);
          chip("F", 36.95, 36.72);
          rise("#F-w1", 37.5); rise("#F-w2", 37.99); rise("#F-w3", 38.21); sel("F", 38.45);
          smear("#F-chip", 39.05);
          out("#F-title", 39.05);
          zoomIn("#F-reat", 39.05);
          kenburns("#F-reatimg", 39.05, 42.83, 1.0, 1.1);
          drop(["#F-reat"], "#F-dk", 42.83);
          tl.fromTo("#F-c1", { y: 0, filter: "blur(5px)" }, { y: -4 * 320, filter: "blur(0px)", duration: 24 * q, ease: "power4.out" }, Q(43.5));
          tl.fromTo("#F-c2", { y: 0, filter: "blur(5px)" }, { y: -5 * 320, filter: "blur(0px)", duration: 27 * q, ease: "power4.out" }, Q(43.5));
          cue(43.52, "cacaniquel", -20);
          rise("#F-tempo", 44.66);
          rise("#F-outros", 45.55);
          slam("#F-best", 46.81, -6);
          whip(["#F-dk"], "#F-est", 47.8);
          kenburns("#F-estimg", 47.8, 50.45, 1.0, 1.1);
          sceneOut("#F", 50.45);

          // ===== H · PASSO 3 → O NAUTILUS NO MAR → AS VENDAS ZERADAS =====
          sceneIn("#H", 52.21); drift("#H-band", 52.21, 61.37);
          chip("H", 52.4, 52.22);
          rise("#H-w1", 53.1); rise("#H-w2", 53.23); rise("#H-w3", 53.47); sel("H", 53.75);
          smear("#H-chip", 54.44);
          out("#H-title", 54.44);
          zoomIn("#H-lanc", 54.44);
          kenburns("#H-lancimg", 54.44, 58.74, 1.0, 1.14);
          drop(["#H-lanc"], "#H-sales", 58.74);
          tl.to("#H-sb i", { scaleY: 1, duration: 8 * q, ease: "expo.out", stagger: 2 * q }, Q(59.12));
          for (var k = 0; k < 6; k++) cue(59.12 + k * 2 * q, "tique", -27);
          pop("#H-6m", 60.23);
          sceneOut("#H", 61.37);

          // ===== L · SPLIT DA VIRADA =====
          splitIn("#L", 65.23);
          kenburns("#L-salaimg", 65.23, 67.23, 1.0, 1.14);
          whip("#L-sala", "#L-form", 67.23);
          kenburns("#L-formimg", 67.23, 71.41, 1.0, 1.12);
          splitOut("#L", 71.41);

          // ===== N · "VOCÊ DEU O SEU MELHOR?" =====
          sceneIn("#N", 71.41);
          kenburns("#N-virimg", 71.41, 73.65, 1.0, 1.12);
          sceneOut("#N", 73.65);

          // ===== M · "E VIROU A CADEIRA" → CLÍMAX: O PRESIDENTE =====
          sceneIn("#M", 78.73);
          kenburns("#M-costasimg", 78.73, 79.94, 1.0, 1.08);
          whip("#M-costas", "#M-pres", 79.94);
          kenburns("#M-presimg", 79.94, 81.47, 1.12, 1.0);
          rise("#M-name", 80.44);
          whip(["#M-pres", "#M-name"], "#M-juntos", 81.47);
          kenburns("#M-juntosimg", 81.47, 82.88, 1.0, 1.03);
          pop("#M-1977", 81.7);
          sceneOut("#M", 82.88);

          // ===== O · "E VOCÊ? POR QUE NÃO?" → O MAIS OU MENOS =====
          sceneIn("#O", 84.85);
          kenburns("#O-olhaimg", 84.85, 86.77, 1.0, 1.1);
          whip("#O-olha", "#O-est", 86.77);
          kenburns("#O-estimg", 86.77, 88.95, 1.1, 1.0);
          sceneOut("#O", 88.95);
'''

T = T.replace('            </style>', CSS + '            </style>', 1)
i = T.index('-->', T.index('CENAS (por video)')) + 3
T = T[:i] + HTML + T[i:]
T = T.replace('          // (vazio = camada transparente)', JS, 1)
open('compositions/mg.html', 'w').write(T)
print('compositions/mg.html', len(T), 'bytes')
