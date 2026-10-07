"""POR VIDEO — reel ERNEST SHACKLETON. CSS das pecas da camada (importado por work/mg/gen.py)."""

CSS = r'''
        /* ===== reel ERNEST SHACKLETON ===== */
        #mg .full img.dim { filter: brightness(.8); }
        #mg .full img.cold, #mg .card img.cold { filter: grayscale(.15) brightness(.82) contrast(1.06); }
        #mg .full .vig { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,10,14,0) 52%, rgba(8,10,14,.72) 82%); }
        #mg .lbl2 { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; letter-spacing: .1em; }
        /* a torcida: o reclamao longe do chefe junta gente */
        #mg .pt { position: absolute; width: 96px; height: 96px; margin: -48px 0 0 -48px; border-radius: 50%; background: #5A606B;
                  box-shadow: 0 10px 24px rgba(0,0,0,.4); }
        #mg .pt.boss { width: 150px; height: 150px; margin: -75px 0 0 -75px; background: #F2B705; }
        #mg .pt.bad { width: 120px; height: 120px; margin: -60px 0 0 -60px; background: #E5322D; }
        #mg .pt b { position: absolute; left: 50%; top: 100%; margin-top: 14px; transform: translateX(-50%); white-space: nowrap;
                    font-weight: 800; font-size: 30px; letter-spacing: .1em; color: #E9ECF2; }
        #mg .halo { position: absolute; width: 520px; height: 520px; margin: -260px 0 0 -260px; border-radius: 50%;
                    border: 6px dashed rgba(229,50,45,.75); background: rgba(229,50,45,.08); }
        /* linha tracejada chefe -> reclamao ("longe") */
        #mg .lnk { position: absolute; left: 780px; top: 330px; width: 880px; height: 0; border-top: 8px dashed rgba(233,236,242,.55);
                   transform-origin: 0 50%; }
        /* moedas de ouro caindo na neve */
        #mg .snow { position: absolute; inset: 0; background: radial-gradient(120% 70% at 50% 18%, #2B3A4E 0%, #0D121A 70%); }
        #mg .snow::after { content: ""; position: absolute; left: -60px; right: -60px; top: 880px; height: 300px; border-radius: 50% 50% 0 0 / 60px 60px 0 0;
                    background: linear-gradient(180deg, #E8EEF5 0%, #B9C6D4 60%, #0D121A 100%); }
        #mg .coin { position: absolute; width: 170px; height: 170px; margin: -85px 0 0 -85px; border-radius: 50%;
                    background: radial-gradient(circle at 35% 30%, #FFF3B0 0%, #F2C94C 30%, #C9952A 70%, #8A5E14 100%);
                    box-shadow: inset 0 0 0 10px rgba(138,94,20,.55), inset 0 0 0 16px rgba(255,236,160,.6), 0 18px 34px rgba(0,0,0,.55); }
        #mg .coin::after { content: ""; position: absolute; left: 50px; top: 38px; width: 70px; height: 92px; border-radius: 46% 46% 40% 40%;
                    background: rgba(138,94,20,.35); }
        /* a bola de couro de 1915 (gomos costurados + cadarco), quicando no gelo */
        #mg .ball { position: absolute; width: 150px; height: 150px; margin: -75px 0 0 -75px; border-radius: 50%; overflow: hidden;
                    background: radial-gradient(circle at 34% 28%, #E2AE76 0%, #B07238 50%, #6A3C19 100%);
                    box-shadow: 0 22px 30px rgba(0,0,0,.55); }
        #mg .ball::before { content: ""; position: absolute; left: 34px; top: -20px; width: 82px; height: 190px; border-radius: 50%;
                    border: 5px solid rgba(70,38,14,.7); border-top-color: transparent; border-bottom-color: transparent; }
        #mg .ball::after { content: ""; position: absolute; left: 62px; top: 24px; width: 26px; height: 46px; border-radius: 4px;
                    background: repeating-linear-gradient(180deg, #F1E3C8 0 5px, rgba(0,0,0,0) 5px 10px); }
        /* o contrato lido no gelo */
        #mg .paper { position: absolute; left: 130px; width: 820px; padding: 50px 56px 46px; background: #F1E8D2; color: #2A2118; border-radius: 12px;
                     box-shadow: 0 30px 80px rgba(0,0,0,.6); transform: rotate(-2deg); }
        #mg .paper .hd { font-weight: 800; font-size: 30px; letter-spacing: .16em; color: #7A6A52; }
        #mg .paper .tt { font-weight: 800; font-size: 60px; margin: 8px 0 26px; }
        #mg .paper .ln { height: 18px; border-radius: 9px; background: rgba(42,33,24,.18); margin: 20px 0; }
        #mg .paper .hl { position: relative; margin: 26px -14px; padding: 10px 14px; font-weight: 800; font-size: 56px; }
        #mg .paper .hl i { position: absolute; left: 0; top: 0; bottom: 0; width: 100%; background: #F2B705; border-radius: 8px; transform-origin: 0 50%; z-index: 0; }
        #mg .paper .hl span { position: relative; z-index: 1; }
        /* fala do carpinteiro */
        #mg .who { position: absolute; display: flex; align-items: center; gap: 18px; font-weight: 800; font-size: 30px; letter-spacing: .1em; color: #8C93A1; }
        #mg .who i { width: 64px; height: 64px; border-radius: 50%; display: block; font-style: normal; color: #fff; font-size: 32px; line-height: 64px; text-align: center; }
        #mg .bubble.big { font-size: 62px; padding: 28px 44px; line-height: 1.15; }
        /* foto inteira na largura da tela sobre a propria foto desfocada (climax) */
        #mg .full img.bgblur { filter: blur(30px) brightness(.42); transform: scale(1.2); }
        #mg .fitimg { position: absolute; left: 0; width: 1080px; height: 666px; overflow: hidden; box-shadow: 0 30px 80px rgba(0,0,0,.6); }
        #mg .fitimg img { width: 100%; height: 100%; object-fit: cover; display: block; }
        /* medo x rebeldia */
        #mg .word { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; letter-spacing: .02em; }
'''
