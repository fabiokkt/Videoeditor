"""POR VIDEO — reel MATTHEW RIDGWAY. CSS e SVG das pecas da camada (importado por work/mg/gen.py)."""

CSS = r'''
        /* ===== reel MATTHEW RIDGWAY ===== */
        #mg .full img.dim { filter: brightness(.8); }
        #mg .full img.bw { filter: grayscale(1) contrast(1.05) brightness(.9); }
        /* anel que marca um detalhe da foto (a granada) */
        #mg .mark { position: absolute; width: 230px; height: 230px; margin: -115px 0 0 -115px; border-radius: 50%; border: 9px solid #F2B705;
                    box-shadow: 0 0 0 6px rgba(0,0,0,.35), 0 0 40px rgba(242,183,5,.55); }
        /* a parede de madeira sob a lanterna */
        #mg .wall { position: absolute; inset: 0;
                    background: repeating-linear-gradient(90deg, #4B3020 0px, #5A3A26 70px, #4A2F1F 150px, #26170E 150px, #26170E 156px); }
        #mg .wall::after { content: ""; position: absolute; inset: 0;
                    background: radial-gradient(48% 34% at 50% 40%, rgba(255,214,140,.30) 0%, rgba(0,0,0,0) 62%),
                                radial-gradient(120% 90% at 50% 40%, rgba(0,0,0,0) 35%, rgba(0,0,0,.82) 78%),
                                linear-gradient(180deg, rgba(0,0,0,0) 62%, rgba(10,8,6,.92) 74%); }
        #mg .note { position: absolute; left: 150px; top: 190px; width: 780px; padding: 46px 52px 40px; background: #F1E8D2; color: #2A2118;
                    border-radius: 10px; box-shadow: 0 30px 70px rgba(0,0,0,.55); transform: rotate(-2.5deg); }
        #mg .note p { margin: 0; font-weight: 700; font-size: 40px; line-height: 1.22; letter-spacing: .01em; }
        #mg .note p + p { margin-top: 18px; font-weight: 600; font-size: 34px; color: #5A4B38; }
        #mg .tack { position: absolute; width: 46px; height: 46px; border-radius: 50%; background: radial-gradient(circle at 35% 35%, #FF7A6B, #C4231B 70%);
                    box-shadow: 0 8px 14px rgba(0,0,0,.5); }
        #mg .pants { position: absolute; left: 290px; top: 600px; width: 500px; height: 700px; }
        #mg .pants svg { position: absolute; left: 0; top: 0; overflow: visible; }
        /* lista do que faltava na linha de frente */
        #mg .req { position: absolute; left: 90px; width: 900px; border-radius: 44px; background: #fff; color: #11141A; padding: 38px 46px 26px;
                   box-shadow: 0 34px 90px rgba(0,0,0,.35); }
        #mg .req .hd { font-weight: 800; font-size: 28px; letter-spacing: .14em; color: #8C93A1; }
        #mg .req .tt { font-weight: 800; font-size: 64px; margin: 10px 0 22px; }
        #mg .req .it { position: relative; height: 128px; display: flex; align-items: center; justify-content: space-between; font-weight: 800; font-size: 54px;
                       border-top: 2px solid rgba(128,136,150,.2); }
        #mg .req .it .pill { width: 300px; height: 74px; }
        #mg .req .it.later { color: #B5BAC4; }
        /* contador de rostos */
        #mg .ctr { position: absolute; left: 0; width: 1080px; text-align: center; color: #fff; font-weight: 800; }
        #mg .ctr .col { display: inline-block; height: 300px; overflow: hidden; vertical-align: top; }
        #mg .ctr .col div span { display: block; height: 300px; line-height: 300px; font-size: 300px; width: 190px; text-align: center; }
        #mg .ctr .pt { display: inline-block; height: 300px; line-height: 300px; font-size: 300px; vertical-align: top; width: 70px; }
        #mg .lbl2 { position: absolute; left: 0; width: 1080px; text-align: center; font-weight: 800; letter-spacing: .1em; }
        /* conversa da virada */
        #mg .who { position: absolute; display: flex; align-items: center; gap: 18px; font-weight: 800; font-size: 30px; letter-spacing: .1em; color: #8C93A1; }
        #mg .who i { width: 64px; height: 64px; border-radius: 50%; display: block; font-style: normal; color: #fff; font-size: 32px; line-height: 64px; text-align: center; }
        #mg .bubble.big { font-size: 62px; padding: 28px 44px; line-height: 1.15; }
        #mg .doc { position: absolute; left: 230px; width: 620px; height: 128px; border-radius: 30px; background: #151A23; border: 3px solid #2C3442;
                   display: flex; align-items: center; gap: 26px; padding: 0 34px; color: #E9ECF2; font-weight: 800; font-size: 40px; letter-spacing: .05em; }
        #mg .doc .fi { width: 58px; height: 72px; border-radius: 8px; background: #E9ECF2; position: relative; flex: none; }
        #mg .doc .fi::after { content: ""; position: absolute; left: 12px; right: 12px; top: 18px; height: 34px;
                              background: repeating-linear-gradient(180deg, #8C93A1 0 5px, transparent 5px 11px); }
        #mg .doc.empty { background: transparent; border: 4px dashed #F2B705; color: #F2B705; }
        #mg .doc.empty .fi { background: transparent; border: 4px dashed #F2B705; }
        #mg .doc.empty .fi::after { display: none; }
        #mg .divd { position: absolute; left: 0; width: 1080px; text-align: center; }
        #mg .divd span { display: inline-block; padding: 14px 34px; border-radius: 999px; background: #252C39; color: #E9ECF2; font-weight: 800; font-size: 32px; letter-spacing: .12em; }
'''

# calca de pijama listrada vista de costas (500x700), com o rasgo no fundilho (#PJ-rasgo) que abre na fala
PANTS = '''<svg width="500" height="700" viewBox="0 0 500 700">
              <defs>
                <pattern id="pj-str" width="56" height="56" patternUnits="userSpaceOnUse" patternTransform="rotate(4)">
                  <rect width="56" height="56" fill="#E9EDF3" /><rect width="20" height="56" fill="#4C6FA8" /><rect x="30" width="6" height="56" fill="#9DB1D3" />
                </pattern>
                <linearGradient id="pj-sh" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".28" /><stop offset=".5" stop-color="#000" stop-opacity="0" /><stop offset="1" stop-color="#000" stop-opacity=".32" /></linearGradient>
              </defs>
              <path d="M58 40 L442 40 L470 680 L300 690 L252 300 L206 690 L34 680 Z" fill="url(#pj-str)" />
              <path d="M58 40 L442 40 L470 680 L300 690 L252 300 L206 690 L34 680 Z" fill="url(#pj-sh)" />
              <rect x="50" y="18" width="400" height="56" rx="10" fill="#DCE3EE" />
              <path d="M70 46 Q250 70 430 46" stroke="#A8B4C8" stroke-width="5" fill="none" />
              <path d="M252 300 L252 120" stroke="rgba(0,0,0,.22)" stroke-width="5" />
              <g id="PJ-rasgo">
                <path d="M170 140 L204 116 L222 150 L250 108 L276 146 L306 118 L330 156 L352 150 L338 196 L362 228 L330 248 L340 290 L300 282 L276 312 L250 280 L222 314 L200 280 L160 292 L172 252 L144 226 L170 196 L150 160 Z"
                      fill="#3B2617" stroke="#F4F6FA" stroke-width="7" stroke-linejoin="round" />
                <path d="M182 168 Q250 150 322 172 M176 214 Q250 196 330 218 M190 258 Q250 240 316 262" stroke="#26170E" stroke-width="10" fill="none" opacity=".55" />
                <path d="M190 150 L214 186 M314 150 L292 190 M236 292 L252 262 M326 268 L300 250 M160 236 L190 226" stroke="#F4F6FA" stroke-width="6" stroke-linecap="round" />
              </g>
            </svg>'''
