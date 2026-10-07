"""POR VIDEO — reel JOHN WOODEN. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Tempos absolutos de work/tl-words.txt.
Dosagem (docs/05 §24): abertura só com fotos (capa gerada + jogo de basquete dos anos 50, sem nada da UCLA); no corpo foto real
é o padrão; motion só no número (10 títulos em 12 temporadas), no objeto que a fala nomeia e não existe em foto (a meia, o relógio
das dez, o grupo da empresa: o parabéns pro vendedor, a proposta esquecida, o financeiro esculachado) e nos capítulos (PASSO 1/2/3).
Fotos: Wikimedia Commons (domínio público — anuários Southern Campus da UCLA, Trail Blazers, DPLA; CC BY 4.0 — arquivo do
Los Angeles Times na UCLA Library) — LICENCAS-FOTOS.txt.
uso: python3 work/mg/gen.py"""
T = open('work/mg/template.html').read()

CSS = r'''
        /* ===== reel JOHN WOODEN ===== */
        #mg .tag { white-space: nowrap; }
        #mg .full img.dim { filter: brightness(.78); }
        #mg .full img.bw { filter: grayscale(1) contrast(1.05); }
        /* retrato em card (o original tem fundo branco) */
        #mg .pcard { position: absolute; left: 175px; top: 150px; width: 730px; height: 900px; border-radius: 44px; overflow: hidden; background: #fff;
                     box-shadow: 0 34px 90px rgba(0,0,0,.45), 0 6px 18px rgba(0,0,0,.25); }
        #mg .pcard img { width: 100%; height: 100%; object-fit: cover; display: block; }
        /* 12 temporadas, 10 títulos */
        #mg .big10 { position: absolute; left: 0; width: 1080px; text-align: center; color: #F2B705; font-weight: 800; font-size: 300px; line-height: 1; }
        #mg .lbl3 { position: absolute; left: 0; width: 1080px; text-align: center; color: #fff; font-weight: 800; font-size: 50px; letter-spacing: .1em; }
        #mg .seasons { position: absolute; left: 90px; width: 900px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 22px; }
        #mg .seasons .s { position: relative; height: 140px; border-radius: 30px; background: #1C2029; border: 3px solid #2A303C; overflow: hidden; }
        #mg .seasons .s .g { position: absolute; inset: 0; background: linear-gradient(180deg, #FFD54A, #F2B705); opacity: 0; }
        #mg .seasons .s b { position: absolute; left: 0; top: 22px; width: 100%; text-align: center; font-weight: 800; font-size: 50px; color: #5A606B; }
        #mg .seasons .s i { position: absolute; left: 0; top: 86px; width: 100%; text-align: center; font-style: normal; font-weight: 800; font-size: 24px;
                            letter-spacing: .14em; color: #11141A; opacity: 0; }
        /* a meia */
        #mg .sockbox { position: absolute; left: 300px; top: 200px; width: 480px; height: 760px; transform: scale(1.3); transform-origin: 50% 0%; }
        #mg .sockbox svg { position: absolute; left: 0; top: 0; overflow: visible; }
        #mg .okb { position: absolute; width: 150px; height: 150px; border-radius: 50%; background: #1FB45A; color: #fff; font-weight: 800; font-size: 96px;
                   line-height: 150px; text-align: center; box-shadow: 0 18px 44px rgba(0,0,0,.3); }
        /* relógio das dez */
        #mg .clockbox { position: absolute; left: 250px; top: 720px; width: 580px; height: 580px; }
        #mg .clockbox svg { position: absolute; left: 0; top: 0; overflow: visible; }
        /* grupo da empresa */
        #mg .chat { position: absolute; left: 70px; width: 940px; border-radius: 44px; background: #fff; color: #11141A; padding: 30px 34px 40px;
                    box-shadow: 0 34px 90px rgba(0,0,0,.32); }
        #mg .chat .hd { display: flex; align-items: center; gap: 22px; padding-bottom: 22px; border-bottom: 2px solid #E3E5E9; margin-bottom: 14px; }
        #mg .chat .hd .av { width: 84px; height: 84px; border-radius: 50%; background: #1FB45A; color: #fff; font-weight: 800; font-size: 36px;
                            line-height: 84px; text-align: center; flex: none; }
        #mg .chat .hd b { display: block; font-weight: 800; font-size: 46px; }
        #mg .chat .hd i { display: block; font-style: normal; font-weight: 600; font-size: 28px; color: #8C93A1; margin-top: 2px; }
        #mg .msg { position: relative; margin: 26px 0 0; max-width: 780px; padding: 22px 30px 24px; border-radius: 30px; background: #F1F2F4;
                   font-weight: 600; font-size: 46px; line-height: 1.25; }
        #mg .msg .who { display: block; font-weight: 800; font-size: 30px; letter-spacing: .04em; color: #1E8BE5; margin-bottom: 6px; }
        #mg .msg.me { margin-left: auto; background: #DCF8C6; }
        #mg .msg.me .who { color: #1FB45A; }
        #mg .msg .hl { color: #E5322D; font-weight: 800; }
        #mg .react { position: absolute; right: -14px; bottom: -30px; padding: 8px 22px; border-radius: 999px; background: #fff; white-space: nowrap;
                     box-shadow: 0 6px 18px rgba(0,0,0,.2); font-weight: 800; font-size: 32px; color: #11141A; z-index: 5; }
        #mg .react.zero { color: #E5322D; }
        #mg .ring2 { position: absolute; inset: -12px; border-radius: 40px; border: 7px solid #F2B705; background: rgba(242,183,5,.12); }
'''

SOCK = '''<svg width="480" height="760" viewBox="0 0 480 760">
              <ellipse cx="250" cy="735" rx="200" ry="16" fill="rgba(0,0,0,.10)" />
              <g id="K-sock">
                <path d="M80,20 L320,20 L320,470 Q320,525 372,548 L405,560 Q452,580 446,630 Q440,676 384,676 L160,676 Q80,676 80,592 Z"
                      fill="#FFFFFF" stroke="#C9CCD2" stroke-width="5" stroke-linejoin="round" />
                <rect x="80" y="20" width="240" height="64" rx="6" fill="#ECEDEF" stroke="#C9CCD2" stroke-width="5" />
                <rect x="82" y="110" width="236" height="22" fill="#2774AE" />
                <rect x="82" y="150" width="236" height="22" fill="#F2B705" />
                <g id="K-dobras" stroke="#AEB4BF" stroke-width="8" stroke-linecap="round" fill="none">
                  <path d="M104,430 Q170,410 236,436" />
                  <path d="M112,470 Q190,450 280,476" />
                  <path d="M128,510 Q206,494 300,514" />
                  <path d="M150,560 Q240,544 330,566" />
                </g>
              </g>
            </svg>'''

CLOCK = '''<svg width="580" height="580" viewBox="0 0 580 580">
              <circle cx="290" cy="290" r="282" fill="#11141A" />
              <circle cx="290" cy="290" r="262" fill="#FFFFFF" />
              <g stroke="#11141A" stroke-linecap="round">
                <line x1="290" y1="44" x2="290" y2="92" stroke-width="14" />
                <line x1="536" y1="290" x2="488" y2="290" stroke-width="14" />
                <line x1="290" y1="536" x2="290" y2="488" stroke-width="14" />
                <line x1="44" y1="290" x2="92" y2="290" stroke-width="14" />
                <line x1="413" y1="77" x2="401" y2="98" stroke-width="8" />
                <line x1="503" y1="167" x2="482" y2="179" stroke-width="8" />
                <line x1="503" y1="413" x2="482" y2="401" stroke-width="8" />
                <line x1="413" y1="503" x2="401" y2="482" stroke-width="8" />
                <line x1="167" y1="503" x2="179" y2="482" stroke-width="8" />
                <line x1="77" y1="413" x2="98" y2="401" stroke-width="8" />
                <line x1="77" y1="167" x2="98" y2="179" stroke-width="8" />
                <line x1="167" y1="77" x2="179" y2="98" stroke-width="8" />
              </g>
              <text x="290" y="400" text-anchor="middle" font-family="Montserrat, sans-serif" font-weight="800" font-size="64" fill="#E5322D" id="J-dig">10:00</text>
              <rect id="J-hour" x="282" y="142" width="16" height="160" rx="8" fill="#11141A" />
              <rect id="J-min" x="285" y="70" width="10" height="232" rx="5" fill="#11141A" />
              <circle cx="290" cy="290" r="20" fill="#E5322D" />
            </svg>'''

SEASONS = ''.join(f'<div class="s" id="C-s{y}"><span class="g"></span><b>{y}</b><i>CAMPEÃO</i></div>' for y in range(1964, 1976))

HTML = '''
        <!-- A · SPLIT DA CAPA (0–5,19), nada do Wooden antes de "John": CAPA GERADA A PEDIDO (Codex: vestiário escuro, o técnico
             baixinho de terno e o gigante de costas, a navalha na pia) — só a capa durante o gancho -->
        <div class="scene" id="A" style="height:845px">
          <div class="full" id="A-capa"><img id="A-capaimg" src="assets/mg/capa-wooden.jpg" style="object-position:55% 40%" /></div>
        </div>

        <!-- P · PRÉ-REVELAÇÃO (5,19–9,95): jogo de basquete de colégio nos anos 50 (DPLA), nada da UCLA -->
        <div class="scene" id="P">
          <div class="full" id="P-j1"><img id="P-j1img" class="dim" src="assets/mg/jogo-1.jpg" style="object-position:50% 50%" /></div>
          <div class="full" id="P-j2"><img id="P-j2img" class="dim bw" src="assets/mg/jogo-2.jpg" style="object-position:50% 50%" /></div>
        </div>

        <!-- C · REVELAÇÃO (11,35–19,05): retrato + nome → 10 títulos em 12 temporadas → o quadro-negro (1949–50) → a meia -->
        <div class="scene" id="C"><div class="world dark"><div class="band" id="C-band"></div></div>
          <div class="pcard" id="C-ret"><img id="C-retimg" src="assets/mg/wooden-retrato.jpg" style="object-position:50% 20%" /></div>
          <div class="name" id="C-name" style="top:1110px"><b>JOHN WOODEN</b><i>TÉCNICO DE BASQUETE · UCLA</i></div>
          <div class="world dark" id="C-tit">
            <div class="big10" id="C-10" style="top:215px">10</div>
            <div class="lbl3" id="C-tl" style="top:530px">TÍTULOS NACIONAIS</div>
            <div class="seasons" id="C-grid" style="top:640px">''' + SEASONS + '''</div>
            <div class="tag" id="C-12" style="left:330px;top:1170px;background:#E5322D">EM 12 ANOS</div>
          </div>
          <div class="full" id="C-quadro"><img id="C-quadroimg" src="assets/mg/wooden-quadro-1950.jpg" style="object-position:0% 50%" /></div>
          <div class="tag" id="C-treino" style="left:250px;top:1170px;background:#11141A">O PRIMEIRO TREINO</div>
          <div class="world light" id="C-meia"><div class="band"></div>
            <div class="sockbox" id="C-sock">''' + SOCK + '''</div>
            <div class="okb" id="C-ok" style="left:770px;top:250px">✓</div>
            <div class="tag" id="C-sem" style="left:345px;top:1150px;background:#1FB45A">SEM DOBRA</div>
          </div>
        </div>

        <!-- D · PASSO 1 → O WOODEN (23,25–30,51) -->
        <div class="scene" id="D"><div class="world light"><div class="band" id="D-band"></div></div>
          <div class="chip" id="D-chip" style="top:300px"><span class="dot" style="background:#E5322D"></span><div class="win"><div class="roll" id="D-roll"><span>PASSO 3</span><span>PASSO 2</span><span>PASSO 1</span></div></div><div class="plus" id="D-plus">+</div></div>
          <div class="title" id="D-title" style="top:520px;font-size:100px"><span id="D-w1">NINGUÉM</span> <span id="D-w2">CHEGA</span><br /><span class="sel" id="D-sel"><span id="D-w3">ATRASADO.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="tag" id="D-nem" style="left:325px;top:880px;background:#E5322D">NEM O MELHOR.</div>
          <div class="full" id="D-foto"><img id="D-fotoimg" class="dim" src="assets/mg/wooden-1960.jpg" style="object-position:62% 30%" /></div>
        </div>

        <!-- E · O RELÓGIO DAS DEZ (callout) → PASSO 2 → O JOGO → O GRUPO DE VENDAS (32,99–46,24) -->
        <div class="scene" id="E"><div class="world dark"><div class="band" id="E-band"></div></div>
          <div class="clockbox" id="E-clock">''' + CLOCK + '''</div>
          <div class="world light" id="E-p2"><div class="band" id="E-band2"></div>
            <div class="chip" id="E-chip" style="top:300px"><span class="dot" style="background:#F2B705"></span><div class="win"><div class="roll" id="E-roll"><span>PASSO 1</span><span>PASSO 3</span><span>PASSO 2</span></div></div><div class="plus" id="E-plus">+</div></div>
            <div class="title" id="E-title" style="top:540px;font-size:84px"><span id="E-w1">QUEM</span> <span id="E-w2">FAZ</span> <span id="E-w3">O</span> <span id="E-w4">PONTO</span><br /><span id="E-w5">AGRADECE</span> <span id="E-w6">O</span> <span class="sel" id="E-sel"><span id="E-w7">PASSE.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          </div>
          <div class="full" id="E-jogo"><img id="E-jogoimg" src="assets/mg/ucla-jogo.jpg" style="object-position:50% 40%" /></div>
          <div class="world light" id="E-grupo"><div class="band"></div>
            <div class="chat" id="E-chat" style="top:200px">
              <div class="hd"><span class="av">V</span><div><b>Time de vendas</b><i>14 participantes</i></div></div>
              <div class="msg" id="E-m1"><span class="who">ANA · PRÉ-VENDAS</span>Segue a proposta do cliente, com os preços revisados.<span class="react zero" id="E-r1">0 reações</span><span class="ring2" id="E-ring"></span></div>
              <div class="msg" id="E-m2"><span class="who">GERENTE</span>VENDA FECHADA! Parabéns, Carlos! Comissão garantida.<span class="react" id="E-r2">PARABÉNS ×14</span></div>
            </div>
          </div>
        </div>

        <!-- G · PASSO 3 → O TIME → O VENDEDOR ESTRELA NO GRUPO (47,90–57,21) -->
        <div class="scene" id="G"><div class="world dark"><div class="band" id="G-band"></div></div>
          <div class="chip" id="G-chip" style="top:300px;background:#fff;color:#11141A"><span class="dot" style="background:#1FB45A"></span><div class="win"><div class="roll" id="G-roll"><span>PASSO 2</span><span>PASSO 1</span><span>PASSO 3</span></div></div><div class="plus" id="G-plus" style="background:#fff;color:#11141A">+</div></div>
          <div class="title" id="G-title" style="top:520px;color:#fff;font-size:92px"><span id="G-w1">NINGUÉM</span> <span id="G-w2">FALA</span> <span id="G-w3">MAL</span><br /><span id="G-w4">DE</span> <span class="sel" id="G-sel"><span id="G-w5">COLEGA.</span><i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span></div>
          <div class="full" id="G-foto"><img id="G-fotoimg" src="assets/mg/wooden-time.jpg" style="object-position:0% 40%" /></div>
          <div class="world light" id="G-grupo"><div class="band"></div>
            <div class="chat" id="G-chat" style="top:230px">
              <div class="hd"><span class="av" style="background:#1E8BE5">E</span><div><b>Grupo da empresa</b><i>23 participantes</i></div></div>
              <div class="msg" id="G-m1"><span class="who" style="color:#E5322D">CARLOS ★ · VENDAS</span>O <span class="hl" id="G-fin">financeiro</span> é uma piada. Nem boleto sabem emitir.</div>
              <div class="msg me" id="G-m2"><span class="who">VOCÊ · DONO</span>kkkkkkkkk</div>
            </div>
          </div>
        </div>

        <!-- L · SPLIT DA VIRADA (62,34–69,70): a navalha (capa) → o jogador barbudo (sem nome) → o time de cabelo curto + PROIBIDA →
             o protesto (1972) -->
        <div class="scene" id="L" style="height:845px">
          <div class="full" id="L-nav"><img id="L-navimg" src="assets/mg/capa-wooden.jpg" style="object-position:80% 46%;transform-origin:72% 54%" /></div>
          <div class="full" id="L-barba"><img id="L-barbaimg" src="assets/mg/walton-barbudo.jpg" style="object-position:40% 18%" /></div>
          <div class="full" id="L-time"><img id="L-timeimg" class="dim" src="assets/mg/ucla-time.jpg" style="object-position:50% 45%" /></div>
          <div class="stamp" data-layout-allow-overlap id="L-proib" style="left:270px;top:330px;font-size:104px">PROIBIDA</div>
          <div class="full" id="L-prot"><img id="L-protimg" src="assets/mg/walton-protesto-1972.jpg" style="object-position:50% 40%" /></div>
        </div>

        <!-- M · "DIREITO DELE" → "VOCÊ ACREDITA MESMO NISSO?" → BILL (69,70–75,40) -->
        <div class="scene" id="M"><div class="world dark"></div>
          <div class="full" id="M-prot"><img id="M-protimg" src="assets/mg/walton-protesto-1972.jpg" style="object-position:52% 40%" /></div>
          <div class="full" id="M-woo"><img id="M-wooimg" src="assets/mg/wooden-pergunta.jpg" style="object-position:100% 25%" /></div>
          <div class="world dark" id="M-bill"><div class="band"></div>
            <div class="pcard" id="M-billc"><img src="assets/mg/walton-retrato.jpg" style="object-position:50% 0%;transform:scale(1.3);transform-origin:50% 2%" /></div>
          </div>
          <div class="name" id="M-name" style="top:1090px"><b>BILL WALTON</b><i>O MELHOR JOGADOR DO PAÍS · 1972–74</i></div>
        </div>

        <!-- N · "ANTES DO TREINO, ELE TAVA SEM BARBA." (79,12–81,38): a navalha → Walton sem barba na UCLA -->
        <div class="scene" id="N"><div class="world dark"></div>
          <div class="full" id="N-nav"><img id="N-navimg" src="assets/mg/capa-wooden.jpg" style="object-position:78% 46%;transform-origin:72% 54%" /></div>
          <div class="full" id="N-ucla"><img id="N-uclaimg" src="assets/mg/walton-ucla.jpg" style="object-position:50% 0%;transform-origin:50% 0%" /></div>
          <div class="tag" id="N-sem" style="left:345px;top:1180px;background:#1FB45A">SEM BARBA</div>
        </div>

        <!-- O · "E POR QUE ELE AINDA TÁ DE BARBA?" (83,41–85,11): o Walton barbudo, callout baixo (top 60) -->
        <div class="scene" id="O"><div class="world dark"><div class="band" id="O-band"></div></div>
          <div class="pcard" id="O-billc"><img src="assets/mg/walton-retrato.jpg" style="object-position:50% 0%;transform:scale(1.3);transform-origin:50% 2%" /></div>
        </div>
'''

JS = r'''
          gsap.set(["#P-j2",
                    "#C-name", "#C-tit", "#C-quadro", "#C-treino", "#C-meia", "#C-ok", "#C-sem", "#C-12",
                    "#D-chip", "#D-w1", "#D-w2", "#D-w3", "#D-nem", "#D-foto",
                    "#E-p2", "#E-chip", "#E-w1", "#E-w2", "#E-w3", "#E-w4", "#E-w5", "#E-w6", "#E-w7", "#E-jogo", "#E-grupo", "#E-m2", "#E-r1", "#E-r2", "#E-ring",
                    "#G-chip", "#G-w1", "#G-w2", "#G-w3", "#G-w4", "#G-w5", "#G-foto", "#G-grupo", "#G-m1", "#G-m2",
                    "#L-barba", "#L-time", "#L-proib", "#L-prot",
                    "#M-woo", "#M-bill", "#M-name",
                    "#N-ucla", "#N-sem"], { autoAlpha: 0 });
          gsap.set(["#D-sel", "#E-sel", "#G-sel"], { borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" });
          gsap.set(["#D-sel .h", "#E-sel .h", "#G-sel .h"], { scale: 0 });
          gsap.set("#J-hour", { rotation: 240, svgOrigin: "290 290" });
          gsap.set("#J-min", { rotation: 0, svgOrigin: "290 290" });
          gsap.set("#J-dig", { autoAlpha: 0 });
          function sel(base, t) {
            tl.to("#" + base + "-sel", { borderColor: "rgba(242,183,5,1)", backgroundColor: "rgba(242,183,5,.16)", duration: 4 * q, ease: "none" }, Q(t));
            tl.to("#" + base + "-sel .h", { scale: 1, duration: 6 * q, ease: "back.out(3)", stagger: q }, Q(t) + q);
          }
          function out(sel_, t) { tl.to(sel_, { scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }, Q(t) - 5 * q); }

          // ===== A · CAPA (quadro 0 = capa) → SÓ A CAPA durante o gancho =====
          splitIn("#A", 0, true);
          kenburns("#A-capaimg", 0, 5.19, 1.0, 1.08);
          splitOut("#A", 5.19);

          // ===== P · PRÉ-REVELAÇÃO (só fotos, nada do Wooden nem da UCLA) =====
          sceneIn("#P", 5.19);
          kenburns("#P-j1img", 5.19, 7.67, 1.12, 1.0);
          whip("#P-j1", "#P-j2", 7.67);
          kenburns("#P-j2img", 7.67, 9.95, 1.0, 1.1);
          sceneOut("#P", 9.95);

          // ===== C · REVELAÇÃO ("John" 11,28 → 11,35) =====
          sceneIn("#C", 11.35); drift("#C-band", 11.35, 19.05);
          kenburns("#C-retimg", 11.35, 12.3, 1.1, 1.0);
          rise("#C-name", 11.5);
          // "ganhou dez campeonatos em doze anos": 12 temporadas, 10 acendem (1966 e 1974 ficam apagadas)
          drop(["#C-ret", "#C-name"], "#C-tit", 12.28);
          var anos = [1964, 1965, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1975];
          anos.forEach(function (y, k) {
            var t = 12.55 + k * 2 * q;
            tl.to("#C-s" + y + " .g", { opacity: 1, duration: 4 * q, ease: "power2.out" }, Q(t));
            tl.to("#C-s" + y + " b", { color: "#11141A", y: -12, duration: 4 * q, ease: "power2.out" }, Q(t));
            tl.to("#C-s" + y + " i", { opacity: 1, duration: 4 * q }, Q(t) + q);
            cue(t, "pop", -24, { f0: 700 + 60 * k });
          });
          tl.fromTo("#C-10", { scale: 0.6 }, { scale: 1, duration: 10 * q, ease: "back.out(2)", immediateRender: false }, Q(12.3));
          pop("#C-12", 13.35);
          // "e, no primeiro treino, ensinava os melhores jogadores do país": o quadro-negro com o time (1949–50)
          whip(["#C-tit", "#C-12"], "#C-quadro", 14.34);
          kenburns("#C-quadroimg", 14.34, 17.44, 1.0, 1.12);
          pop("#C-treino", 14.7);
          // "a calçar a meia": a meia cai, as dobras somem (puxada), ✓ SEM DOBRA
          drop(["#C-quadro", "#C-treino"], "#C-meia", 17.44);
          tl.fromTo("#K-sock", { y: 0 }, { y: -26, duration: 5 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(18.15));
          tl.to("#K-dobras path", { scaleX: 0, transformOrigin: "50% 50%", autoAlpha: 0, duration: 6 * q, ease: "power3.in", stagger: q }, Q(18.15));
          cue(18.17, "swish", -19);
          pop("#C-ok", 18.4, null, "clique");
          pop("#C-sem", 18.55);
          sceneOut("#C", 19.05);

          // ===== D · PASSO 1 → O WOODEN =====
          sceneIn("#D", 23.25); drift("#D-band", 23.25, 30.51);
          chip("D", 24.1, 23.32);
          rise("#D-w1", 24.7); rise("#D-w2", 25.06); rise("#D-w3", 25.46); sel("D", 25.85);
          pop("#D-nem", 26.36, null, "clique");
          smear("#D-chip", 27.25);
          out(["#D-title", "#D-nem"], 27.25);
          zoomIn("#D-foto", 27.25);
          kenburns("#D-fotoimg", 27.25, 30.51, 1.0, 1.12);
          sceneOut("#D", 30.51);

          // ===== E · O RELÓGIO DAS DEZ → PASSO 2 → O JOGO → O GRUPO =====
          sceneIn("#E", 32.99); drift("#E-band", 32.99, 34.74);
          tl.to("#J-min", { rotation: 720, duration: 26 * q, ease: "power3.inOut" }, Q(33.0));
          tl.to("#J-hour", { rotation: 300, duration: 26 * q, ease: "power3.inOut" }, Q(33.0));
          cue(33.04, "cacaniquel", -22);
          tl.to("#J-dig", { autoAlpha: 1, duration: 3 * q }, Q(33.87));
          tl.fromTo("#E-clock", { scale: 1 }, { scale: 1.05, duration: 3 * q, ease: "power2.out", yoyo: true, repeat: 1 }, Q(33.87));
          cue(33.88, "clique", -18);
          drop(["#E-clock"], "#E-p2", 34.74);
          drift("#E-band2", 34.74, 38.07);
          chip("E", 34.92, 34.78);
          rise("#E-w1", 35.6); rise("#E-w2", 35.88); rise("#E-w3", 36.15); rise("#E-w4", 36.18);
          rise("#E-w5", 36.59); rise("#E-w6", 37.31); rise("#E-w7", 37.32); sel("E", 37.6);
          smear("#E-chip", 38.07);
          out("#E-title", 38.07);
          zoomIn("#E-jogo", 38.07);
          kenburns("#E-jogoimg", 38.07, 42.2, 1.0, 1.12);
          // "Seu vendedor leva a comissão e o parabéns no grupo." → "E quem fez a proposta?"
          drop(["#E-jogo"], "#E-grupo", 42.2);
          pop("#E-m2", 42.85, { y: 60, autoAlpha: 0 }, "clique");
          pop("#E-r2", 43.7);
          tl.fromTo("#E-ring", { autoAlpha: 0, scale: 1.08 }, { autoAlpha: 1, scale: 1, duration: 6 * q, ease: "back.out(2)", immediateRender: false }, Q(44.66));
          cue(44.68, "swish", -21);
          pop("#E-r1", 45.1, null, "clique");
          sceneOut("#E", 46.24);

          // ===== G · PASSO 3 → O TIME → O VENDEDOR ESTRELA NO GRUPO =====
          sceneIn("#G", 47.9); drift("#G-band", 47.9, 50.6);
          chip("G", 48.28, 47.96);
          rise("#G-w1", 48.92); rise("#G-w2", 49.42); rise("#G-w3", 49.61); rise("#G-w4", 49.83); rise("#G-w5", 49.97); sel("G", 50.2);
          smear("#G-chip", 50.62);
          out("#G-title", 50.62);
          zoomIn("#G-foto", 50.62);
          kenburns("#G-fotoimg", 50.62, 53.95, 1.0, 1.12);
          drop(["#G-foto"], "#G-grupo", 53.95);
          pop("#G-m1", 54.72, { y: 60, autoAlpha: 0 }, "clique");
          tl.fromTo("#G-fin", { backgroundColor: "rgba(229,50,45,0)" }, { backgroundColor: "rgba(229,50,45,.14)", duration: 4 * q }, Q(55.3));
          pop("#G-m2", 56.55, { y: 60, autoAlpha: 0 }, "clique");
          sceneOut("#G", 57.21);

          // ===== L · SPLIT DA VIRADA =====
          splitIn("#L", 62.34);
          kenburns("#L-navimg", 62.34, 63.98, 1.0, 1.18);
          whip("#L-nav", "#L-barba", 63.98);
          kenburns("#L-barbaimg", 63.98, 67.14, 1.0, 1.1);
          whip("#L-barba", "#L-time", 67.14);
          kenburns("#L-timeimg", 67.14, 68.78, 1.0, 1.06);
          slam("#L-proib", 67.72, -6);
          whip(["#L-time", "#L-proib"], "#L-prot", 68.78);
          kenburns("#L-protimg", 68.78, 69.7, 1.0, 1.05);
          splitOut("#L", 69.7);

          // ===== M · "DIREITO DELE" → A PERGUNTA → BILL =====
          sceneIn("#M", 69.7);
          kenburns("#M-protimg", 69.7, 70.76, 1.05, 1.12);
          whip("#M-prot", "#M-woo", 70.76);
          kenburns("#M-wooimg", 70.76, 73.44, 1.0, 1.12);
          whip("#M-woo", "#M-bill", 73.44);
          kenburns("#M-billc", 73.44, 75.4, 1.0, 1.04);
          rise("#M-name", 73.97);
          sceneOut("#M", 75.4);

          // ===== N · CLÍMAX: "ANTES DO TREINO, ELE TAVA SEM BARBA." =====
          sceneIn("#N", 79.12);
          kenburns("#N-navimg", 79.12, 79.58, 1.0, 1.12);
          whip("#N-nav", "#N-ucla", 79.58);
          kenburns("#N-uclaimg", 79.58, 81.38, 1.0, 1.08);
          pop("#N-sem", 80.25, null, "clique");
          sceneOut("#N", 81.38);

          // ===== O · "E POR QUE ELE AINDA TÁ DE BARBA?" =====
          sceneIn("#O", 83.41);
          kenburns("#O-billc", 83.41, 85.11, 1.0, 1.05); drift("#O-band", 83.41, 85.11);
          sceneOut("#O", 85.11);
'''

T = T.replace('            </style>', CSS + '            </style>', 1)
i = T.index('-->', T.index('CENAS (por video)')) + 3
T = T[:i] + HTML + T[i:]
T = T.replace('          // (vazio = camada transparente)', JS, 1)
open('compositions/mg.html', 'w').write(T)
print('compositions/mg.html', len(T), 'bytes')
