"""POR VIDEO — reel BOB CHAPMAN. CSS das pecas da camada (importado por work/mg/gen.py). Base: pecas do reel Gordon Bethune + Ridgway."""

CSS = r'''
        /* ===== reel BOB CHAPMAN ===== */
        #mg .full img.dim { filter: brightness(.78); }
        #mg .full img.dark2 { filter: brightness(.42) saturate(.8); }
        #mg .full img.warm { filter: sepia(.25) saturate(1.25) brightness(.92) contrast(1.05); }
        #mg .full .vig { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,10,14,0) 50%, rgba(8,10,14,.74) 80%); }
        #mg .full .floor { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,10,14,0) 56%, rgba(8,10,14,.82) 76%); }
        /* anel que marca um detalhe da foto (o nome no nariz do 777) */
        #mg .mark { position: absolute; width: 300px; height: 150px; margin: -75px 0 0 -150px; border-radius: 80px; border: 9px solid #F2B705;
                    box-shadow: 0 0 0 6px rgba(0,0,0,.35), 0 0 40px rgba(242,183,5,.55); }
        #mg .lbl2 { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; letter-spacing: .1em; }
        /* a frase exata dele */
        #mg .quote { position: absolute; left: 90px; width: 900px; color: #fff; font-weight: 800; font-size: 92px; line-height: 1.06; letter-spacing: -.005em; }
        #mg .quote span { display: inline-block; }
        #mg .quote .y { color: #F2B705; }
        #mg .qmark { position: absolute; left: 70px; font-weight: 800; font-size: 300px; line-height: 1; color: #F2B705; }
        #mg .qby { position: absolute; left: 90px; width: 900px; font-weight: 700; font-size: 34px; letter-spacing: .08em; color: #C9CED8; }
        #mg .qlbl { position: absolute; left: 90px; padding: 14px 30px; border-radius: 999px; background: #F2B705; color: #11141A; font-weight: 800; font-size: 34px; letter-spacing: .1em; }
        /* lista: comissao do vendedor / painel da cabine */
        #mg .req { position: absolute; left: 70px; width: 940px; border-radius: 44px; background: #fff; color: #11141A; padding: 38px 42px 22px;
                   box-shadow: 0 34px 90px rgba(0,0,0,.35); }
        #mg .req .hd { font-weight: 800; font-size: 28px; letter-spacing: .14em; color: #8C93A1; }
        #mg .req .tt { font-weight: 800; font-size: 58px; margin: 10px 0 18px; }
        #mg .req .it { position: relative; height: 124px; display: flex; align-items: center; justify-content: space-between; gap: 18px; font-weight: 800; font-size: 46px;
                       border-top: 2px solid rgba(128,136,150,.2); }
        #mg .req .it .nm { flex: 1; white-space: nowrap; }
        #mg .req .it .pill { width: 290px; height: 72px; flex: none; }
        #mg .req .it .pill span { font-size: 27px; }
        #mg .req .cols { display: flex; justify-content: flex-end; gap: 18px; font-weight: 800; font-size: 22px; letter-spacing: .12em; color: #8C93A1; margin-bottom: 8px; }
        #mg .req .cols b { width: 290px; text-align: center; font-weight: 800; }
        /* comercial x financeiro */
        #mg .vcard { position: absolute; top: 330px; width: 450px; height: 640px; border-radius: 44px; background: #151A23; border: 3px solid #2C3442;
                     box-shadow: 0 34px 90px rgba(0,0,0,.45); text-align: center; color: #E9ECF2; }
        #mg .vcard .dp { margin-top: 48px; font-weight: 800; font-size: 50px; letter-spacing: .06em; }
        #mg .vcard .gp { margin-top: 18px; font-weight: 700; font-size: 28px; letter-spacing: .12em; color: #8C93A1; }
        #mg .vcard .gv { margin: 10px 30px 0; font-weight: 800; font-size: 44px; line-height: 1.1; }
        #mg .vcard .ar { position: absolute; left: 50%; bottom: 46px; width: 200px; height: 230px; margin-left: -100px; font-weight: 800; font-size: 230px; line-height: 230px; }
        #mg .vs { position: absolute; left: 0; top: 590px; width: 1080px; text-align: center; font-weight: 800; font-size: 64px; color: #F2B705; }
        /* o manual (fichario preto) */
        #mg .binder { position: absolute; left: 270px; top: 300px; width: 540px; height: 720px; border-radius: 26px; background: linear-gradient(90deg, #050608 0 64px, #1B1F27 64px 70px, #11141A 70px);
                      box-shadow: 0 40px 90px rgba(0,0,0,.6); }
        #mg .binder .lb { position: absolute; left: 130px; right: 60px; top: 110px; padding: 26px 20px; border: 4px solid #3A4150; border-radius: 12px; text-align: center;
                          color: #E9ECF2; font-weight: 800; font-size: 54px; letter-spacing: .12em; }
        #mg .binder .lb i { display: block; font-style: normal; font-weight: 600; font-size: 24px; letter-spacing: .16em; color: #8C93A1; margin-top: 8px; }
        #mg .binder .pg { position: absolute; left: 130px; right: 60px; height: 16px; border-radius: 8px; background: #252B36; }
        /* conversa com o atendente */
        #mg .who { position: absolute; display: flex; align-items: center; gap: 18px; font-weight: 800; font-size: 30px; letter-spacing: .1em; color: #8C93A1; }
        #mg .who i { width: 64px; height: 64px; border-radius: 50%; display: block; font-style: normal; color: #fff; font-size: 32px; line-height: 64px; text-align: center; }
        #mg .bubble.big { font-size: 62px; padding: 28px 44px; line-height: 1.15; }
        /* o bonus novo: a nota de dolar + todo mundo */
        #mg .bill { position: absolute; left: 190px; top: 320px; width: 700px; height: 300px; border-radius: 22px; background: linear-gradient(135deg, #CFE3C4 0%, #9CC28A 55%, #7FAA70 100%);
                    box-shadow: inset 0 0 0 14px rgba(255,255,255,.35), inset 0 0 0 20px rgba(46,90,40,.35), 0 30px 70px rgba(0,0,0,.55); }
        #mg .bill::before { content: "$"; position: absolute; left: 50%; top: 50%; width: 190px; height: 190px; margin: -95px 0 0 -95px; border-radius: 50%;
                    background: #E8F1E1; border: 8px solid #3E6B36; color: #2F5529; font-weight: 800; font-size: 130px; line-height: 176px; text-align: center; }
        #mg .bill::after { content: ""; position: absolute; left: 44px; right: 44px; top: 40px; bottom: 40px; border: 4px dashed rgba(46,90,40,.45); border-radius: 12px; }
        #mg .ppl { position: absolute; left: 90px; width: 900px; display: flex; justify-content: space-between; }
        #mg .ppl .pp { position: relative; width: 92px; height: 150px; }
        #mg .ppl .pp i { position: absolute; inset: 0; display: block; }
        #mg .ppl .pp i::before { content: ""; position: absolute; left: 22px; top: 0; width: 48px; height: 48px; border-radius: 50%; background: #3A4150; }
        #mg .ppl .pp i::after { content: ""; position: absolute; left: 6px; top: 58px; width: 80px; height: 92px; border-radius: 40px 40px 14px 14px; background: #3A4150; }
        #mg .ppl .pp i.y::before, #mg .ppl .pp i.y::after { background: #F2B705; }
        #mg .ppl .pp i.on::before, #mg .ppl .pp i.on::after { background: #1FB45A; }
        #mg .ppl b { position: absolute; left: 50%; top: 162px; transform: translateX(-50%); white-space: nowrap; font-weight: 800; font-size: 22px; letter-spacing: .08em; color: #8C93A1; }
        /* ranking de pontualidade */
        #mg .rank { position: absolute; left: 70px; width: 940px; top: 250px; height: 1060px; border-radius: 44px; background: #151A23; border: 3px solid #2C3442;
                    box-shadow: 0 34px 90px rgba(0,0,0,.45); overflow: hidden; }
        #mg .rank .hd { position: absolute; left: 46px; top: 34px; font-weight: 800; font-size: 30px; letter-spacing: .14em; color: #8C93A1; }
        #mg .rank .tt { position: absolute; left: 46px; top: 76px; font-weight: 800; font-size: 56px; color: #E9ECF2; }
        #mg .rank .top { position: absolute; left: 24px; right: 24px; top: 176px; height: 430px; border-radius: 28px; background: rgba(31,180,90,.14); border: 4px solid rgba(31,180,90,.75); }
        #mg .rank .toplbl { position: absolute; right: 40px; top: 84px; padding: 12px 26px; border-radius: 999px; background: #1FB45A; color: #fff; font-weight: 800; font-size: 30px; letter-spacing: .1em; }
        #mg .rank .top b { position: absolute; right: 26px; top: 18px; padding: 10px 22px; border-radius: 999px; background: #1FB45A; color: #fff; font-weight: 800; font-size: 26px; letter-spacing: .1em; }
        #mg .rank .r { position: absolute; left: 46px; right: 46px; height: 72px; display: flex; align-items: center; gap: 22px; font-weight: 800; font-size: 32px; color: #8C93A1; }
        #mg .rank .r .n { width: 60px; }
        #mg .rank .r i { display: block; height: 24px; border-radius: 12px; background: #303746; }
        #mg .rank .co { position: absolute; left: 34px; right: 34px; height: 76px; border-radius: 38px; background: #F2B705; color: #11141A; display: flex; align-items: center;
                        padding: 0 34px; font-weight: 800; font-size: 36px; letter-spacing: .08em; box-shadow: 0 16px 40px rgba(0,0,0,.45); }
        /* foto inteira na largura da tela sobre a propria foto desfocada (climax) */
        #mg .full img.bgblur { filter: blur(30px) brightness(.42); transform: scale(1.2); }
        #mg .fitimg { position: absolute; left: 0; width: 1080px; height: 648px; overflow: hidden; box-shadow: 0 30px 80px rgba(0,0,0,.6); }
        #mg .fitimg img { width: 100%; height: 100%; object-fit: cover; display: block; }
        /* a pergunta do fim (comentario) */
        #mg .ask { position: absolute; left: 70px; width: 940px; top: 150px; border-radius: 40px; background: #fff; color: #11141A; padding: 34px 40px 30px;
                   box-shadow: 0 30px 80px rgba(0,0,0,.45); }
        #mg .ask .hd { display: flex; align-items: center; gap: 18px; font-weight: 800; font-size: 28px; letter-spacing: .12em; color: #8C93A1; }
        #mg .ask .hd i { width: 56px; height: 56px; border-radius: 50%; background: #FF4A1C; display: block; }
        #mg .ask p { margin: 18px 0 22px; font-weight: 800; font-size: 54px; line-height: 1.12; }
        #mg .ask .qh { border-radius: 10px; padding: 0 6px; margin: 0 -6px; background-color: rgba(242,183,5,0); }
        #mg .follow { position: absolute; left: 340px; top: 330px; width: 400px; height: 112px; border-radius: 26px; background: #0095F6; color: #fff;
                      font-weight: 800; font-size: 50px; line-height: 112px; text-align: center; box-shadow: 0 20px 50px rgba(0,0,0,.4); }
        #mg .ask .in { height: 78px; border-radius: 39px; background: #EEF0F3; color: #8C93A1; font-weight: 600; font-size: 30px; line-height: 78px; padding: 0 32px; }

        #mg .full img.night { filter: grayscale(1) brightness(.72) contrast(1.12); }
        #mg .full .blue { position: absolute; inset: 0; background: rgba(20,40,90,.32); mix-blend-mode: multiply; }
        #mg .full img.bw { filter: grayscale(1) contrast(1.05); }
        /* contador por rolo (reel Ridgway) */
        #mg .ctr { position: absolute; left: 0; width: 1080px; text-align: center; color: #fff; font-weight: 800; white-space: nowrap; }
        #mg .ctr .col { display: inline-block; height: 260px; overflow: hidden; vertical-align: top; }
        #mg .ctr .col div span { display: block; height: 260px; line-height: 260px; font-size: 250px; width: 165px; text-align: center; }
        #mg .ctr .pt { display: inline-block; height: 260px; line-height: 260px; font-size: 250px; vertical-align: top; width: 60px; }
        #mg .ctr .cur { display: inline-block; height: 260px; line-height: 290px; font-size: 96px; vertical-align: top; margin-right: 18px; color: #F2B705; }
        #mg .ctr .suf { display: inline-block; height: 260px; line-height: 290px; font-size: 96px; vertical-align: top; margin-left: 22px; color: #F2B705; }
        /* split da virada: o grafico de pedidos de 2009 */
        #mg .chart { position: absolute; left: 90px; top: 210px; width: 900px; height: 470px; }
        #mg .chart .bar { position: absolute; bottom: 70px; width: 300px; border-radius: 26px 26px 8px 8px; transform-origin: 50% 100%; }
        #mg .chart .yr { position: absolute; bottom: 0; width: 300px; text-align: center; font-weight: 800; font-size: 46px; color: #C9CED8; }
        #mg .chart .base { position: absolute; left: 0; right: 0; bottom: 64px; height: 6px; border-radius: 3px; background: #3A4150; }
        #mg .neg { position: absolute; font-weight: 800; font-size: 150px; color: #FF4A3D; letter-spacing: -.02em; }
        /* as semanas sem salario: quem pega a semana do colega */
        #mg .wk { position: absolute; left: 70px; width: 940px; height: 300px; border-radius: 40px; background: #151A23; border: 3px solid #2C3442;
                  box-shadow: 0 30px 80px rgba(0,0,0,.45); }
        #mg .wk .nm { position: absolute; left: 44px; top: 34px; font-weight: 800; font-size: 40px; letter-spacing: .08em; color: #E9ECF2; }
        #mg .wk .nm i { font-style: normal; font-weight: 700; font-size: 28px; letter-spacing: .1em; color: #8C93A1; margin-left: 14px; }
        #mg .wk .row { position: absolute; left: 44px; top: 120px; display: flex; gap: 16px; border: 0; height: auto; }
        #mg .w { position: relative; width: 150px; height: 130px; border-radius: 22px; background: #252C39; color: #8C93A1; font-weight: 800; font-size: 26px;
                     letter-spacing: .06em; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; }
        #mg .w b { font-size: 50px; color: #E9ECF2; letter-spacing: 0; }
        #mg .w.off { background: #E5322D; color: #FFD9D6; }
        #mg .w.off b { color: #fff; }
        #mg .w.ok { background: #1FB45A; color: #D8F5E3; }
        #mg .w.ok b { color: #fff; }
        #mg .w.ghost { background: transparent; border: 4px dashed #3A4150; }
        #mg .mv { position: absolute; width: 150px; height: 130px; border-radius: 22px; background: #F2B705; color: #11141A; font-weight: 800; font-size: 26px;
                  letter-spacing: .06em; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; box-shadow: 0 20px 50px rgba(0,0,0,.5); }
        #mg .mv b { font-size: 50px; letter-spacing: 0; }
        /* do chao de fabrica a diretoria: a lista com a pilula das 4 semanas */
        #mg .req .it .pill.wide { width: 380px; }
        /* cracha que vira */
        #mg .badge { position: absolute; left: 290px; top: 300px; width: 500px; height: 720px; border-radius: 36px; background: #F4F1EA; color: #11141A;
                     box-shadow: 0 40px 90px rgba(0,0,0,.6); text-align: center; overflow: hidden; }
        #mg .badge .clip { position: absolute; left: 50%; top: 26px; width: 120px; height: 26px; margin-left: -60px; border-radius: 13px; background: #C9CED8; }
        #mg .badge .ph { position: absolute; left: 130px; top: 110px; width: 240px; height: 280px; border-radius: 20px; background: #3A4150; overflow: hidden; }
        #mg .badge .ph img { width: 100%; height: 100%; object-fit: cover; }
        #mg .badge .l1 { position: absolute; left: 0; right: 0; top: 430px; font-weight: 800; font-size: 30px; letter-spacing: .14em; color: #8C93A1; }
        #mg .badge .l2 { position: absolute; left: 30px; right: 30px; top: 480px; font-weight: 800; font-size: 54px; line-height: 1.08; }
        #mg .badge .bar2 { position: absolute; left: 0; right: 0; bottom: 0; height: 90px; background: #FF4A1C; }
        /* lucro recorde */
        #mg .bars2 { position: absolute; left: 110px; width: 860px; height: 520px; display: flex; align-items: flex-end; gap: 40px; }
        #mg .bars2 i { flex: 1; display: block; border-radius: 22px 22px 6px 6px; transform-origin: 50% 100%; background: #3A4150; }
        #mg .bars2 i.hi { background: #1FB45A; }
        #mg .yrs { position: absolute; left: 110px; width: 860px; display: flex; gap: 40px; }
        #mg .yrs span { flex: 1; text-align: center; font-weight: 800; font-size: 36px; color: #8C93A1; }
'''
