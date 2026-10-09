"""POR VIDEO — reel MICHAEL GERBER. CSS das pecas da camada (importado por work/mg/gen.py)."""

CSS = r'''
        /* ===== reel MICHAEL GERBER ===== */
        #mg .full img.dim { filter: brightness(.8); }
        #mg .full img.bw { filter: grayscale(1) contrast(1.08) brightness(.92); }
        #mg .full img.bwdim { filter: grayscale(1) contrast(1.08) brightness(.72); }
        #mg .full .vig { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,10,14,0) 50%, rgba(8,10,14,.74) 80%); }
        #mg .full .floor { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,10,14,0) 56%, rgba(8,10,14,.82) 76%); }
        #mg .full img.bgblur { filter: blur(30px) brightness(.42); transform: scale(1.2); }
        #mg .fitimg { position: absolute; left: 0; width: 1080px; height: 648px; overflow: hidden; box-shadow: 0 30px 80px rgba(0,0,0,.6); }
        #mg .fitimg img { width: 100%; height: 100%; object-fit: cover; display: block; }
        /* conversa (o socio) */
        #mg .who { position: absolute; display: flex; align-items: center; gap: 18px; font-weight: 800; font-size: 30px; letter-spacing: .1em; color: #8C93A1; }
        #mg .who i { width: 64px; height: 64px; border-radius: 50%; display: block; font-style: normal; color: #fff; font-size: 32px; line-height: 64px; text-align: center; }
        #mg .bubble.big { font-size: 66px; padding: 30px 46px; line-height: 1.12; }
        #mg .yr { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; font-size: 210px; line-height: 1; color: rgba(255,255,255,.08); letter-spacing: .02em; }
        /* organograma (papel claro) */
        #mg .paper { position: absolute; left: 50px; width: 980px; border-radius: 40px; background: #F7F5F0; box-shadow: 0 40px 100px rgba(0,0,0,.5); }
        #mg .org .hdr { position: absolute; left: 330px; top: 46px; width: 320px; height: 96px; border-radius: 26px; background: #11141A; color: #fff;
                        font-weight: 800; font-size: 36px; letter-spacing: .08em; line-height: 96px; text-align: center; }
        #mg .org .spine { position: absolute; left: 488px; top: 142px; width: 4px; height: 780px; background: #B9BEC8; transform-origin: 50% 0; }
        #mg .org .arm { position: absolute; height: 4px; width: 40px; background: #B9BEC8; }
        #mg .seat { position: absolute; width: 410px; height: 214px; border-radius: 26px; background: #fff; border: 4px solid #D7DAE0; box-shadow: 0 10px 26px rgba(17,20,26,.08); }
        #mg .seat .k { position: absolute; left: 30px; top: 24px; font-weight: 700; font-size: 22px; letter-spacing: .16em; color: #9AA0AB; }
        #mg .seat .d { position: absolute; left: 30px; top: 56px; font-weight: 800; font-size: 46px; color: #11141A; white-space: nowrap; }
        #mg .seat .ln { position: absolute; left: 30px; right: 30px; top: 168px; border-top: 4px dashed #C9CDD5; }
        #mg .seat .you { position: absolute; left: 24px; top: 112px; font-weight: 800; font-size: 60px; letter-spacing: .02em; color: #E5322D; transform: rotate(-5deg); }
        #mg .seat .red { position: absolute; inset: -4px; border-radius: 26px; border: 6px solid #E5322D; opacity: 0; }
        #mg .cnt { position: absolute; left: 0; width: 1080px; text-align: center; }
        #mg .cnt span { display: inline-block; padding: 20px 46px; border-radius: 999px; background: #E5322D; color: #fff; font-weight: 800; font-size: 50px; letter-spacing: .04em;
                        box-shadow: 0 18px 44px rgba(229,50,45,.35); }
        /* franquia: a mesma loja em todo lugar */
        #mg .shop { position: absolute; width: 250px; height: 230px; }
        #mg .shop .roof { position: absolute; left: 0; top: 0; width: 250px; height: 64px; border-radius: 14px 14px 4px 4px;
                          background: repeating-linear-gradient(90deg, #FF4A1C 0 31px, #fff 31px 62px); box-shadow: 0 8px 18px rgba(0,0,0,.25); }
        #mg .shop .body { position: absolute; left: 14px; top: 64px; width: 222px; height: 166px; background: #E9E4DA; border-radius: 0 0 10px 10px; }
        #mg .shop .door { position: absolute; left: 92px; top: 92px; width: 66px; height: 138px; background: #11141A; border-radius: 8px 8px 0 0; }
        #mg .shop .win { position: absolute; top: 96px; width: 52px; height: 52px; background: #F2B705; border-radius: 6px; }
        #mg .lbl2 { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; letter-spacing: .1em; }
        /* o passo a passo (folha) */
        #mg .sheet { position: absolute; left: 140px; width: 800px; border-radius: 30px; background: #F7F5F0; padding: 50px 56px 40px; box-shadow: 0 40px 100px rgba(0,0,0,.5); color: #11141A; }
        #mg .sheet .hd { font-weight: 800; font-size: 26px; letter-spacing: .16em; color: #9AA0AB; }
        #mg .sheet .tt { font-weight: 800; font-size: 60px; margin: 8px 0 26px; }
        #mg .sheet .st { position: relative; height: 104px; display: flex; align-items: center; gap: 26px; border-top: 2px solid rgba(128,136,150,.2); }
        #mg .sheet .st b { width: 64px; height: 64px; flex: none; border-radius: 50%; background: #11141A; color: #fff; font-weight: 800; font-size: 32px; line-height: 64px; text-align: center; }
        #mg .sheet .st i { display: block; height: 20px; border-radius: 10px; background: #C9CDD5; transform-origin: 0 50%; }
        /* gente comum x genio */
        #mg .vcard { position: absolute; top: 300px; width: 450px; height: 640px; border-radius: 44px; background: #151A23; border: 3px solid #2C3442;
                     box-shadow: 0 34px 90px rgba(0,0,0,.45); text-align: center; color: #E9ECF2; }
        #mg .vcard .dp { position: absolute; left: 0; right: 0; top: 400px; font-weight: 800; font-size: 50px; letter-spacing: .04em; }
        #mg .vcard .mk { position: absolute; left: 50%; top: 482px; width: 104px; height: 104px; margin-left: -52px; border-radius: 50%; font-weight: 800; font-size: 64px; line-height: 104px; color: #fff; }
        #mg .ppl3 { position: absolute; left: 75px; top: 120px; width: 300px; height: 230px; }
        #mg .ppl3 i { position: absolute; top: 40px; width: 92px; height: 190px; display: block; }
        #mg .ppl3 i::before { content: ""; position: absolute; left: 20px; top: 0; width: 52px; height: 52px; border-radius: 50%; background: #8C93A1; }
        #mg .ppl3 i::after { content: ""; position: absolute; left: 4px; top: 62px; width: 84px; height: 110px; border-radius: 42px 42px 14px 14px; background: #8C93A1; }
        #mg .bulb { position: absolute; left: 145px; top: 90px; width: 160px; height: 200px; }
        #mg .bulb::before { content: ""; position: absolute; left: 0; top: 0; width: 160px; height: 160px; border-radius: 50%; background: #F2B705; box-shadow: 0 0 70px rgba(242,183,5,.6); }
        #mg .bulb::after { content: ""; position: absolute; left: 48px; top: 150px; width: 64px; height: 56px; border-radius: 8px; background: repeating-linear-gradient(180deg, #8C93A1 0 10px, #5A606B 10px 16px); }
        /* contrato da cadeira */
        #mg .ctt { position: absolute; left: 100px; width: 880px; border-radius: 30px; background: #F7F5F0; padding: 50px 60px 44px; box-shadow: 0 40px 100px rgba(0,0,0,.5); color: #11141A; }
        #mg .ctt .hd { font-weight: 800; font-size: 26px; letter-spacing: .16em; color: #9AA0AB; }
        #mg .ctt .tt { font-weight: 800; font-size: 62px; margin: 8px 0 22px; }
        #mg .ctt .rw { display: flex; align-items: center; gap: 20px; height: 92px; border-top: 2px solid rgba(128,136,150,.2); font-weight: 800; font-size: 36px; }
        #mg .ctt .rw span { width: 270px; flex: none; font-size: 24px; letter-spacing: .14em; color: #9AA0AB; }
        #mg .ctt .rw i { display: block; height: 18px; border-radius: 9px; background: #C9CDD5; }
        #mg .ctt .sg { position: relative; height: 230px; border-top: 2px solid rgba(128,136,150,.2); }
        #mg .ctt .sg svg { position: absolute; left: 10px; top: 10px; }
        #mg .ctt .sg .bl { position: absolute; left: 0; right: 0; top: 160px; border-top: 4px solid #11141A; }
        #mg .ctt .sg .nm { position: absolute; left: 0; top: 178px; font-weight: 800; font-size: 28px; letter-spacing: .12em; color: #5A606B; }
        /* ordem: primeiro a cadeira, depois a pessoa */
        #mg .ord { position: absolute; left: 90px; width: 900px; height: 190px; border-radius: 40px; background: #151A23; border: 3px solid #2C3442; box-shadow: 0 30px 70px rgba(0,0,0,.45); }
        #mg .ord b { position: absolute; left: 40px; top: 45px; width: 100px; height: 100px; border-radius: 50%; background: #F2B705; color: #11141A; font-weight: 800; font-size: 46px; line-height: 100px; text-align: center; }
        #mg .ord .sw { position: absolute; left: 180px; right: 30px; top: 0; height: 190px; }
        #mg .ord .sw span { position: absolute; left: 0; top: 0; height: 190px; line-height: 190px; font-weight: 800; font-size: 76px; color: #fff; white-space: nowrap; }
        #mg .ord .sw span.rd { color: #FF6B5E; }
        /* comenta CADEIRA */
        #mg .cmt { position: absolute; left: 70px; width: 940px; top: 170px; border-radius: 40px; background: #fff; color: #11141A; padding: 34px 40px 36px;
                   box-shadow: 0 30px 80px rgba(0,0,0,.45); }
        #mg .cmt .hd { display: flex; align-items: center; gap: 18px; font-weight: 800; font-size: 30px; letter-spacing: .12em; color: #8C93A1; }
        #mg .cmt .hd i { width: 56px; height: 56px; border-radius: 50%; background: #FF4A1C; display: block; }
        #mg .cmt .in { position: relative; margin-top: 22px; height: 150px; border-radius: 75px; background: #EEF0F3; display: flex; align-items: center; padding: 0 40px; gap: 6px; }
        #mg .cmt .in .ch { font-weight: 800; font-size: 92px; letter-spacing: .02em; color: #11141A; }
        #mg .cmt .in .caret { width: 6px; height: 90px; background: #0095F6; }
        #mg .cmt .in .go { position: absolute; right: 22px; top: 25px; height: 100px; padding: 0 36px; border-radius: 50px; background: #0095F6; color: #fff; font-weight: 800; font-size: 36px; line-height: 100px; }
        /* climax: EMPRESA -> EMPREGO */
        #mg .wd { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; font-size: 178px; letter-spacing: .01em; color: #fff; line-height: 1; white-space: nowrap; }
        #mg .wd .sl { display: inline-block; position: relative; width: 300px; height: 186px; overflow: hidden; vertical-align: top; text-align: left; }
        #mg .wd .sl div { position: absolute; left: 0; top: 0; }
        #mg .wd .sl div span { display: block; height: 186px; line-height: 186px; }
        #mg .wd .og { color: #FF4A1C; }
        #mg .wsub { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; font-size: 46px; letter-spacing: .14em; color: #8C93A1; }
        #mg .follow { position: absolute; left: 340px; top: 330px; width: 400px; height: 112px; border-radius: 26px; background: #0095F6; color: #fff;
                      font-weight: 800; font-size: 50px; line-height: 112px; text-align: center; box-shadow: 0 20px 50px rgba(0,0,0,.4); }
'''
