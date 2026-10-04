"""v2 — réplica do padrão da referência (medido quadro a quadro):
gancho Oswald Bold 156 em caixa laranja degradê, topo em vermelho escuro, apresentador em close;
light leak laranja + whoosh nos cortes; frase de impacto Montserrat ExtraBold 127 digitada letra a letra;
legenda Montserrat SemiBold 74; trilha da referência remapeada; censura no palavrão."""
import json, subprocess, os, sys

W, H, FPS = 1080, 1920, 30
SPLIT_H = 840
AROLL = "aroll.mov"
B = "../broll/"
EYE_Y = 985                       # altura dos olhos no A-roll 1080x1920
DUR = float(subprocess.check_output(
    f"ffprobe -v error -show_entries format=duration -of csv=p=0 {AROLL}", shell=True))

# (início, modo, asset/zoom, opções)   modos: split | full | band | talk
SHOTS = [
    (0.00, "split", "stock_5", {"red": True, "fy": 0.25}),
    (3.90, "split", "us_1611974789855-9c2a0a7236a3", {}),
    (8.16, "full", "us_1507679799987-c73779587ccf", {}),
    (11.02, "band", "a4_1", {}),
    (13.18, "full", "a4_3", {"fx": 0.55}),
    (15.06, "full", "hoalo_0", {"fx": 0.62}),
    (17.42, "full", "hoalo_4", {"fx": 0.35}),
    (19.46, "talk", 1.30, {}),
    (21.44, "talk", 1.50, {}),
    (23.94, "talk", 1.30, {}),
    (25.82, "full", "epic_1", {}),
    (31.56, "split", "us_1590283603385-17ffb3a7f29f", {}),
    (33.94, "talk", 1.50, {}),
    (35.84, "band", "us_1542744173-8e7e53415bb0", {}),
    (40.40, "talk", 1.30, {}),
    (42.96, "full", "strel_2", {}),
    (47.94, "full", "us_1554224155-6726b3ff858f", {}),
    (50.72, "talk", 1.30, {}),
    (53.42, "talk", 1.60, {}),
    (53.90, "talk", 1.30, {}),
    (56.58, "full", "stock_4", {}),
    (61.04, "split", "us_1552664730-d307ca884978", {}),
    (66.14, "full", "xmas_1", {}),
    (69.74, "band", "hoalo_2", {}),
    (72.20, "band", "xmas_5", {}),
    (74.74, "full", "xmas_0", {"fx": 0.5}),
    (77.06, "full", "easter_5", {}),
    (80.98, "band", "hoalo_1", {}),
    (82.80, "talk", 1.30, {}),
    (86.68, "talk", 1.50, {}),
    (88.84, "talk", 1.30, {}),
    (91.66, "talk", 1.50, {}),
]
# cortes com light leak + whoosh (como na referência: entrada de B-roll)
LEAKS = [3.90, 8.16, 11.02, 15.06, 25.82, 35.84, 42.96, 47.94, 56.58, 66.14, 72.20, 77.06]
LEAK_CUT_FRAME = 9                # o corte cai no 10º quadro do leak

# frases de impacto (texto, início, fim) — digitadas letra a letra
EMPH = [
    ("O DONO OTIMISTA\\NÉ O PRIMEIRO\\NA QUEBRAR.", 8.16, 11.00),
    ("FORAM 7\\NE MEIO.", 17.96, 19.40),
    ("SEPARA O\\NQUE É SEU.", 24.64, 25.80),
    ("ENCARA O FATO\\NMAIS FEIO.", 41.26, 42.92),
    ("É MEDO.", 53.42, 53.88),
    ("NUNCA PERDE\\NA FÉ NO FINAL.", 54.82, 56.55),
    ("OS OTIMISTAS.", 70.76, 72.15),
    ("MÊS QUE VEM\\NÉ O SEU NATAL.", 86.68, 88.80),
]
TYPE_CPS = 28                     # letras por segundo na digitação
HOOK_LINES = ["ESSE CARA É UM DOS", "MILITARES MAIS", "TORTURADOS E MAIS", "ESTUDADOS DOS", "ESTADOS UNIDOS."]
HOOK_Y = [664, 757, 850, 943, 1036]
HOOK_END = 4.85
CENSOR = ("porra", 38.70)         # palavra e instante do corte do som
FIX = {"partir.": "partido.", "porra": "po---"}


def shots():
    out = []
    for i, (t0, mode, a, o) in enumerate(SHOTS):
        t1 = SHOTS[i + 1][0] if i + 1 < len(SHOTS) else DUR
        out.append((i, t0, t1, mode, a, o))
    return out


def img_src(img, w, h, n, zin, o):
    fx, fy = o.get("fx", 0.5), o.get("fy", 0.5)
    z = f"1.0+0.08*on/{n}" if zin else f"1.08-0.08*on/{n}"
    s = (f"movie={img},scale={w*2}:{h*2}:force_original_aspect_ratio=increase,"
         f"crop={w*2}:{h*2}:(iw-{w*2})*{fx}:(ih-{h*2})*{fy},setsar=1,"
         f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={w}x{h}:fps={FPS}")
    if o.get("red"):  # duotone vermelho-escuro como a imagem do gancho da referência
        s += (",format=gray,curves=all='0/0 0.3/0.04 0.6/0.3 0.85/0.75 1/1',format=rgb24,"
              "colorchannelmixer=rr=1.0:rg=0:rb=0:gr=0.12:gg=0:gb=0:br=0.08:bg=0:bb=0")
    else:
        s += ",eq=contrast=1.05:saturation=1.05"
    return s


def render_shot(i, t0, t1, mode, a, o):
    d = t1 - t0
    n = max(1, round(d * FPS))
    out = f"shots2/{i:02d}.mp4"
    zin = i % 2 == 0
    if mode == "talk":
        z = a
        cw, ch = int(W / z) // 2 * 2, int(H / z) // 2 * 2
        y0 = max(0, min(H - ch, int(EYE_Y - 0.43 * H / z)))
        fc = f"[0:v]crop={cw}:{ch}:(iw-{cw})/2:{y0},scale={W}:{H}:flags=lanczos,setsar=1[v]"
    elif mode == "full":
        fc = img_src(B + a + ".jpg", W, H, n, zin, o) + "[v]"
    elif mode == "band":  # foto larga: faixa central nítida + fundo desfocado
        bh = 1190
        fc = (img_src(B + a + ".jpg", W, H, n, zin, o) + ",boxblur=30:2,eq=brightness=-0.08[bg];"
              + img_src(B + a + ".jpg", W, bh, n, zin, o) + f"[fg];[bg][fg]overlay=0:{(H-bh)//2}[v]")
    else:  # split: imagem em cima, apresentador em close embaixo (zoom 1.25)
        bh = H - SPLIT_H
        z = 1.25
        cs = int(bh / z) // 2 * 2
        y0 = int(EYE_Y - (1357 - SPLIT_H) / z)
        fc = (img_src(B + a + ".jpg", W, SPLIT_H, n, zin, o) + "[top];"
              f"[0:v]crop={cs}:{cs}:(iw-{cs})/2:{y0},scale={W}:{bh}:flags=lanczos,setsar=1[bot];"
              "[top][bot]vstack[v]")
    cmd = (f"ffmpeg -v error -y -ss {t0:.3f} -t {d:.3f} -i {AROLL} -filter_complex \"{fc}\" "
           f"-map [v] -frames:v {n} -r {FPS} -c:v libx264 -preset fast -crf 16 -pix_fmt yuv420p -an {out}")
    subprocess.run(cmd, shell=True, check=True)


def ass_time(t):
    t = max(0, t)
    return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"


def build_ass():
    words = [w for s in json.load(open("aroll.wav.json")) for w in s["words"]]
    for w in words:
        w["w"] = w["w"].strip()
        for k, v in FIX.items():
            if w["w"].lower().startswith(k):
                w["w"] = v + w["w"][len(k):]
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if w["w"][-1] in ".,?!:" or len(cur) == 3 or len(" ".join(x["w"] for x in cur)) > 15:
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    blocked = [(0, HOOK_END)] + [(e[1], e[2]) for e in EMPH]
    sh = shots()
    def mode_at(t):
        return next(m for _, a, b, m, _, _ in sh if a <= t < b) if t < DUR else "talk"
    ev = []
    for k, c in enumerate(chunks):
        s = c[0]["s"]
        e = chunks[k + 1][0]["s"] if k + 1 < len(chunks) else c[-1]["e"] + 0.3
        e = min(e, c[-1]["e"] + 0.6)
        for b0, b1 in blocked:
            if b0 <= s < b1: s = b1
            if s < b0 < e: e = b0
        if e - s < 0.15: continue
        y = 1458 if mode_at(s) == "talk" else 845
        ev.append(f"Dialogue: 0,{ass_time(s)},{ass_time(e)},Sub,,0,0,0,,{{\\pos(540,{y})}}"
                  + " ".join(x["w"] for x in c))
    for txt, s, e in EMPH:
        chars = [ch for ch in txt.replace("\\N", "\n")]
        vis = [i for i, ch in enumerate(chars) if ch not in " \n"]
        for k, idx in enumerate(vis):
            t0 = s + k / TYPE_CPS
            t1 = s + (k + 1) / TYPE_CPS if k + 1 < len(vis) else e
            if t0 >= e: break
            shown = "".join(chars[:idx + 1]).replace("\n", "\\N")
            hidden = "".join(chars[idx + 1:]).replace("\n", "\\N")
            ev.append(f"Dialogue: 1,{ass_time(t0)},{ass_time(min(t1, e))},Emph,,0,0,0,,"
                      f"{{\\pos(540,1190)}}{shown}{{\\alpha&HFF&}}{hidden}")
    for line, y in zip(HOOK_LINES, HOOK_Y):
        ev.append(f"Dialogue: 2,{ass_time(0)},{ass_time(HOOK_END)},Hook,,0,0,0,,{{\\pos(540,{y})}}{line}")
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,MontSemi,74,&H00FFFFFF,&H00FFFFFF,&H70000000,&H90000000,0,0,0,0,100,100,0,0,1,1.5,2,5,30,30,0,1
Style: Emph,MontXBold,127,&H00FFFFFF,&H00FFFFFF,&H00505050,&H90000000,0,0,0,0,100,100,0,0,1,3,4,5,30,30,0,1
Style: Hook,OswBold,156,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,0,0,0,0,100,100,0,0,1,4.5,3,5,30,30,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    open("subs2.ass", "w").write(head + "\n".join(ev) + "\n")


def final_video():
    ins = f"-i video2.mp4 -loop 1 -t {HOOK_END} -i fx/hookbox.png "
    fc = ["[1:v]format=rgba[box]", f"[0:v][box]overlay=0:0:eof_action=pass:enable='lt(t,{HOOK_END})'[v0]"]
    last = "v0"
    for k, t in enumerate(LEAKS):
        off = t - LEAK_CUT_FRAME / FPS
        ins += f"-itsoffset {off:.3f} -i fx/leak.mov "
        fc.append(f"[{last}][{k+2}:v]overlay=0:0:eof_action=pass[v{k+1}]")
        last = f"v{k+1}"
    fc.append(f"[{last}]ass=subs2.ass:fontsdir=fonts[v]")
    cmd = (f"ffmpeg -v error -y {ins} -i mix2.wav -filter_complex \"{';'.join(fc)}\" "
           f"-map [v] -map {len(LEAKS)+2}:a -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p "
           f"-c:a aac -b:a 192k -movflags +faststart -shortest final2.mp4")
    subprocess.run(cmd, shell=True, check=True)


if __name__ == "__main__":
    os.makedirs("shots2", exist_ok=True)
    args = sys.argv[1:]
    if args and args[0] == "final":
        build_ass(); final_video(); sys.exit()
    only = set(int(x) for x in args) if args else None
    build_ass()
    files = []
    for sh in shots():
        if only is None or sh[0] in only:
            render_shot(*sh)
        files.append(f"file '{sh[0]:02d}.mp4'")
    open("shots2/list.txt", "w").write("\n".join(files))
