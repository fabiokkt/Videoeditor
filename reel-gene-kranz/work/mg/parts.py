"""POR VIDEO — reel GENE KRANZ. CSS das pecas da camada (importado por work/mg/gen.py).
Pecas reaproveitadas: anel no detalhe da foto (.mark, Ridgway), lista FALTA -> RESOLVIDO (.req, Ridgway), fala com avatar (.who + .bubble.big,
Shackleton), foto inteira na largura sobre ela mesma desfocada (.bgblur + .fitimg, Shackleton)."""

CSS = r'''
        /* ===== reel GENE KRANZ ===== */
        #mg .full img.dim { filter: brightness(.8); }
        #mg .full img.bw { filter: grayscale(1) contrast(1.06) brightness(.86); }
        #mg .full img.cold, #mg .card img.cold { filter: grayscale(.2) brightness(.8) contrast(1.06); }
        #mg .full .vig { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,10,14,0) 52%, rgba(8,10,14,.74) 80%); }
        #mg .floor { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,10,14,0) 56%, rgba(8,10,14,.82) 74%); }
        /* anel que marca um detalhe da foto */
        #mg .mark { position: absolute; width: 230px; height: 230px; margin: -115px 0 0 -115px; border-radius: 50%; border: 9px solid #F2B705;
                    box-shadow: 0 0 0 6px rgba(0,0,0,.35), 0 0 40px rgba(242,183,5,.55); }
        /* foto inteira na largura da tela sobre a propria foto desfocada */
        #mg .full img.bgblur { filter: blur(30px) brightness(.42); transform: scale(1.2); }
        #mg .fitimg { position: absolute; left: 0; width: 1080px; overflow: hidden; box-shadow: 0 30px 80px rgba(0,0,0,.6); }
        #mg .fitimg img { width: 100%; height: 100%; object-fit: cover; display: block; }
        /* a semana do prazo: SEG..SEX, a sexta marcada */
        #mg .wk { position: absolute; left: 60px; width: 960px; padding: 40px 40px 46px; border-radius: 44px; background: #fff; color: #11141A;
                  box-shadow: 0 34px 90px rgba(0,0,0,.4); }
        #mg .wk .hd { font-weight: 800; font-size: 28px; letter-spacing: .14em; color: #8C93A1; }
        #mg .wk .tt { font-weight: 800; font-size: 60px; margin: 8px 0 30px; }
        #mg .wk .days { display: flex; justify-content: space-between; }
        #mg .wk .d { position: relative; width: 160px; height: 190px; border-radius: 30px; background: #EEF0F3; text-align: center; }
        #mg .wk .d b { display: block; margin-top: 26px; font-weight: 800; font-size: 32px; letter-spacing: .08em; color: #8C93A1; }
        #mg .wk .d i { display: block; font-style: normal; font-weight: 800; font-size: 74px; line-height: 1.2; color: #11141A; }
        #mg .wk .d.hot { background: #11141A; } #mg .wk .d.hot b { color: #F2B705; } #mg .wk .d.hot i { color: #fff; }
        #mg .wk .ring2 { position: absolute; left: -16px; top: -16px; right: -16px; bottom: -16px; border-radius: 40px; border: 8px solid #E5322D; }
        #mg .wk .x { position: absolute; left: 50%; top: 50%; width: 150px; height: 14px; margin: -7px 0 0 -75px; border-radius: 7px; background: #E5322D; }
        /* lista: descobre -> mexe */
        #mg .req { position: absolute; left: 90px; width: 900px; border-radius: 44px; background: #fff; color: #11141A; padding: 38px 46px 26px;
                   box-shadow: 0 34px 90px rgba(0,0,0,.35); }
        #mg .req .hd { font-weight: 800; font-size: 28px; letter-spacing: .14em; color: #8C93A1; }
        #mg .req .tt { font-weight: 800; font-size: 64px; margin: 10px 0 22px; }
        #mg .req .it { position: relative; height: 128px; display: flex; align-items: center; justify-content: space-between; font-weight: 800; font-size: 50px;
                       border-top: 2px solid rgba(128,136,150,.2); }
        #mg .req .it .pill { width: 280px; height: 74px; }
        #mg .req .it.later { color: #B5BAC4; }
        /* a fala do Kranz (avatar + balao) */
        #mg .who { position: absolute; display: flex; align-items: center; gap: 18px; font-weight: 800; font-size: 30px; letter-spacing: .1em; color: #C9CED8; }
        #mg .who i { width: 64px; height: 64px; border-radius: 50%; display: block; font-style: normal; color: #11141A; font-size: 32px; line-height: 64px; text-align: center; }
        #mg .bubble.big { font-size: 60px; padding: 28px 44px; line-height: 1.15; }
        /* toast vazio: avisos do time */
        #mg .inbox { position: absolute; left: 90px; width: 900px; border-radius: 44px; background: #151A23; border: 2px solid #252C39; padding: 40px 46px 44px;
                     color: #E9ECF2; box-shadow: 0 34px 90px rgba(0,0,0,.45); }
        #mg .inbox .hd { display: flex; justify-content: space-between; font-weight: 800; font-size: 32px; letter-spacing: .1em; color: #8C93A1; }
        #mg .inbox .n { font-weight: 800; font-size: 230px; line-height: 1; text-align: center; margin: 30px 0 6px; color: #fff; }
        #mg .inbox .z { text-align: center; font-weight: 700; font-size: 40px; color: #8C93A1; }
        #mg .lbl2 { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; letter-spacing: .06em; }
        #mg .word { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; letter-spacing: .02em; }
'''
