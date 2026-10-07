"""Monta o reel no padrão da referência: split no gancho, B-roll em tela cheia com
movimento, talking head com punch-in, flash laranja, legenda pequena + frases de impacto."""
import json, subprocess, os, sys

W, H, FPS = 1080, 1920, 30
SPLIT_H = 880                      # altura da imagem no topo da tela dividida
AROLL = "aroll.mov"
B = "../broll/"
DUR = float(subprocess.check_output(
    f"ffprobe -v error -show_entries format=duration -of csv=p=0 {AROLL}", shell=True))

# (início, modo, asset/zoom, opções)
SHOTS = [
    (0.00, "split", "stock_5", {"hook": True}),
    (4.92, "split", "us_1611974789855-9c2a0a7236a3", {}),
    (8.16, "full", "us_1507679799987-c73779587ccf", {}),
    (11.02, "full", "a4_1", {"flash": True, "fx": 0.45}),
    (13.18, "full", "a4_3", {"fx": 0.55}),
    (15.06, "full", "hoalo_0", {"fx": 0.62}),
    (17.42, "full", "hoalo_4", {"fx": 0.35}),
    (19.46, "talk", 1.00, {}),
    (21.44, "talk", 1.18, {}),
    (23.94, "talk", 1.32, {}),
    (25.82, "full", "epic_1", {"flash": True}),
    (31.56, "split", "us_1590283603385-17ffb3a7f29f", {}),
    (33.94, "talk", 1.15, {}),
    (35.84, "full", "us_1542744173-8e7e53415bb0", {}),
    (40.40, "talk", 1.32, {}),
    (42.96, "full", "strel_2", {"flash": True}),
    (47.94, "full", "us_1554224155-6726b3ff858f", {}),
    (50.72, "talk", 1.00, {}),
    (53.42, "talk", 1.38, {}),
    (53.90, "talk", 1.15, {}),
    (56.58, "full", "stock_4", {"flash": True}),
    (61.04, "split", "us_1552664730-d307ca884978", {}),
    (66.14, "full", "xmas_1", {"flash": True}),
    (69.74, "full", "hoalo_2", {"fx": 0.5}),
    (72.20, "full", "xmas_5", {"fx": 0.5}),
    (74.74, "full", "xmas_0", {"fx": 0.5}),
    (77.06, "full", "easter_5", {}),
    (80.98, "full", "hoalo_1", {}),
    (82.80, "talk", 1.00, {}),
    (86.68, "talk", 1.32, {}),
    (88.84, "talk", 1.00, {}),
    (91.66, "talk", 1.20, {}),
]

# frases de impacto: (texto, início, fim)
EMPH = [
    ("O DONO OTIMISTA\\NÉ O PRIMEIRO\\NA QUEBRAR.", 8.16, 11.00),
    ("7 ANOS E MEIO.", 17.96, 19.40),
    ("PRIMEIRO:\\NSEPARA O QUE É SEU.", 23.94, 25.80),
    ("SEGUNDO:\\NENCARA O FATO\\NMAIS FEIO.", 40.40, 42.90),
    ("É MEDO.", 53.42, 53.88),
    ("TERCEIRO:\\NNUNCA PERDE A FÉ\\NNO FINAL.", 53.90, 56.55),
    ("OS OTIMISTAS.", 70.76, 72.15),
    ("MÊS QUE VEM\\NÉ O SEU NATAL.", 86.68, 88.80),
]
HOOK = ("ESSE CARA É UM DOS\\NMILITARES MAIS\\NTORTURADOS E MAIS\\NESTUDADOS DOS\\NESTADOS UNIDOS.", 0.0, 4.90)
HOOK_BOX = (50, 380, 980, 650)     # x, y, w, h da caixa laranja
FIX = {"partir.": "partido."}


def shots():
    out = []
    for i, (t0, mode, a, o) in enumerate(SHOTS):
        t1 = SHOTS[i + 1][0] if i + 1 < len(SHOTS) else DUR
        out.append((i, t0, t1, mode, a, o))
    return out


def kenburns(img, w, h, n, zin, fx):
    z = f"1.0+0.10*on/{n}" if zin else f"1.10-0.10*on/{n}"
    return (f"movie={img},scale={w*2}:{h*2}:force_original_aspect_ratio=increase,"
            f"crop={w*2}:{h*2}:(iw-{w*2})*{fx}:(ih-{h*2})/2,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={w}x{h}:fps={FPS},"
            f"eq=contrast=1.06:saturation=1.08,vignette=PI/6")


def render_shot(i, t0, t1, mode, a, o):
    d = t1 - t0
    n = max(1, round(d * FPS))
    out = f"shots/{i:02d}.mp4"
    zin = i % 2 == 0
    fx = o.get("fx", 0.5)
    if mode == "talk":
        z = a
        cw, ch = int(W / z) // 2 * 2, int(H / z) // 2 * 2
        # punch-in centrado um pouco acima do meio (rosto)
        fc = f"[0:v]crop={cw}:{ch}:(iw-{cw})/2:(ih-{ch})*0.38,scale={W}:{H}:flags=lanczos,setsar=1[v]"
    elif mode == "full":
        fc = kenburns(B + a + ".jpg", W, H, n, zin, fx) + "[v]"
    else:  # split: imagem em cima, apresentador embaixo
        bh = H - SPLIT_H
        fc = (kenburns(B + a + ".jpg", W, SPLIT_H, n, zin, fx) + "[top];"
              f"[0:v]crop={W}:{bh}:0:300[bot];[top][bot]vstack[v]")
        if o.get("hook"):
            x, y, w, h = HOOK_BOX
            fc = fc[:-3] + (f"[st];[st]drawbox={x}:{y}:{w}:{h}:color=0xE4471C:t=fill,"
                            f"drawbox={x}:{y}:{w}:{h}:color=white@0.9:t=4[v]")
    if o.get("flash"):
        fc = fc[:-3] + ("[pre];color=c=0xFF6A1A:s=1080x1920:d=0.45:r=30,format=rgba,"
                        "fade=t=out:st=0:d=0.45:alpha=1[fl];[pre][fl]overlay=eof_action=pass[v]")
    cmd = (f"ffmpeg -v error -y -ss {t0:.3f} -t {d:.3f} -i {AROLL} -filter_complex \"{fc}\" "
           f"-map [v] -frames:v {n} -r {FPS} -c:v libx264 -preset fast -crf 17 -pix_fmt yuv420p -an {out}")
    subprocess.run(cmd, shell=True, check=True)
    return out


def ass_time(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def build_ass():
    words = [w for s in json.load(open("aroll.wav.json")) for w in s["words"]]
    for w in words:
        w["w"] = FIX.get(w["w"].strip(), w["w"].strip())
    # blocos de até 3 palavras / 18 caracteres, quebrando na pontuação
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        txt = " ".join(x["w"] for x in cur)
        if w["w"][-1] in ".,?!:" or len(cur) == 3 or len(txt) > 16:
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    blocked = [(HOOK[1], HOOK[2])] + [(e[1], e[2]) for e in EMPH]
    split_ranges = [(t0, t1) for _, t0, t1, m, _, _ in shots() if m == "split"]
    ev = []
    for k, c in enumerate(chunks):
        s = c[0]["s"]
        e = chunks[k + 1][0]["s"] if k + 1 < len(chunks) else c[-1]["e"] + 0.3
        e = min(e, c[-1]["e"] + 0.6)
        if any(s < b1 and e > b0 for b0, b1 in blocked):
            # recorta o bloco fora da janela da frase de impacto
            for b0, b1 in blocked:
                if s >= b0 and s < b1: s = b1
                if e > b0 and s < b0: e = b0
            if e - s < 0.15: continue
        y = SPLIT_H - 40 if any(a <= s < b for a, b in split_ranges) else 1440
        txt = " ".join(x["w"] for x in c)
        ev.append(f"Dialogue: 0,{ass_time(s)},{ass_time(e)},Sub,,0,0,0,,{{\\pos(540,{y})}}{txt}")
    talk_ranges = [(t0, t1) for _, t0, t1, m, _, _ in shots() if m == "talk"]
    for txt, s, e in EMPH:
        ey = 1480 if any(a <= s + 0.01 < b for a, b in talk_ranges) else 1060
        ev.append(f"Dialogue: 1,{ass_time(s)},{ass_time(e)},Emph,,0,0,0,,"
                  f"{{\\pos(540,{ey})\\fscx80\\fscy80\\t(0,90,\\fscx100\\fscy100)}}{txt}")
    x, y, w, h = HOOK_BOX
    ev.append(f"Dialogue: 2,{ass_time(HOOK[1])},{ass_time(HOOK[2])},Hook,,0,0,0,,"
              f"{{\\pos({x + w // 2},{y + h // 2})}}{HOOK[0]}")
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,MontSemi,44,&H00FFFFFF,&H00FFFFFF,&H80000000,&H80000000,0,0,0,0,100,100,0,0,1,1.6,1.5,5,40,40,0,1
Style: Emph,MontBlack,90,&H00FFFFFF,&H00FFFFFF,&H00000000,&HA0000000,0,0,0,0,100,100,0,0,1,3,4,5,60,60,0,1
Style: Hook,Anton,112,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,4,3,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    open("subs.ass", "w").write(head + "\n".join(ev) + "\n")


if __name__ == "__main__":
    os.makedirs("shots", exist_ok=True)
    only = set(int(x) for x in sys.argv[1:]) if len(sys.argv) > 1 else None
    build_ass()
    files = []
    for sh in shots():
        if only is None or sh[0] in only:
            render_shot(*sh)
        files.append(f"file '{sh[0]:02d}.mp4'")
    open("shots/list.txt", "w").write("\n".join(files))
