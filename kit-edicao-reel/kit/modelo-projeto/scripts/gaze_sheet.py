"""MOTOR (kit v3). Folhas de conferencia do olhar com o ROSTO INTEIRO (o recorte do gaze_review.py corta a testa e
precisava ser medido por bruto). O recorte sai sozinho: FaceLandmarker em 9 quadros do aroll -> caixa mediana do rosto.
Junta as janelas de gaze/pose-windows.json (P) e gaze/tl-windows.json (T, so as que nao cruzam uma P); 4 quadros por
janela (antes, 1/3, 2/3, depois), 12 janelas por folha -> gaze/me/gNN.jpg. Ler as folhas e listar as NITIDAS.
uso: python3 scripts/gaze_sheet.py      (depois de gaze_tl.py, gaze_windows.py e gaze_pose.py)"""
import json, subprocess, os, cv2, numpy as np, mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
from PIL import Image, ImageDraw, ImageFont
V = 'assets/aroll.mp4'
lm = vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=BaseOptions(model_asset_path='.models/face_landmarker.task')))
cap = cv2.VideoCapture(V); n = int(cap.get(7)); W = int(cap.get(3)); H = int(cap.get(4)); boxes = []
for f in np.linspace(n * 0.05, n * 0.95, 9).astype(int):
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(f)); ok, im = cap.read()
    if not ok: continue
    r = lm.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(im, cv2.COLOR_BGR2RGB)))
    if r.face_landmarks:
        xs = [p.x for p in r.face_landmarks[0]]; ys = [p.y for p in r.face_landmarks[0]]
        boxes.append((min(xs) * W, min(ys) * H, max(xs) * W, max(ys) * H))
x0, y0, x1, y1 = np.median(np.array(boxes), 0)
fw = (x1 - x0) * 1.25; fh = fw * 0.72                       # testa ate a boca, com folga
cx, cy = (x0 + x1) / 2, y0 + (y1 - y0) * 0.30
cw, ch = int(fw) // 2 * 2, int(fh) // 2 * 2
cx0 = int(max(0, min(W - cw, cx - cw / 2))); cy0 = int(max(0, min(H - ch, cy - ch / 2)))
print(f'recorte do rosto: {cw}x{ch} em ({cx0},{cy0}) de {W}x{H}')
P = json.load(open('gaze/pose-windows.json')) if os.path.exists('gaze/pose-windows.json') else []
T = json.load(open('gaze/tl-windows.json'))
Wn = [(w['t0'], w['t1'], 'P') for w in P]
for w in T:
    a, b = w['t0'], w['t1']
    if not any(min(b, x[1]) - max(a, x[0]) > 0 for x in Wn): Wn.append((a, b, 'T'))
Wn.sort()
TW, TH = 300, int(300 * ch / cw)
F = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 22)
os.makedirs('gaze/me', exist_ok=True)
def frame(t):
    d = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{max(0,t):.3f}', '-i', V, '-frames:v', '1', '-vf', f'crop={cw}:{ch}:{cx0}:{cy0},scale={TW}:{TH}',
                        '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
    return Image.frombytes('RGB', (TW, TH), d) if len(d) == TW * TH * 3 else Image.new('RGB', (TW, TH))
rows = [(k, a, b, s, [a - 0.15, a + (b - a) / 3, a + 2 * (b - a) / 3, b + 0.1]) for k, (a, b, s) in enumerate(Wn)]
per = 12
for p in range(0, len(rows), per):
    S = Image.new('RGB', (160 + 4 * (TW + 2), per * (TH + 2)), 'black'); d = ImageDraw.Draw(S)
    for r, (k, a, b, s, ts) in enumerate(rows[p:p + per]):
        y = r * (TH + 2); d.text((4, y + TH // 3), f'#{k} {s}\n{a:.2f}\n{b:.2f}', fill='yellow', font=F)
        for j, t in enumerate(ts):
            S.paste(frame(t), (160 + j * (TW + 2), y)); d.text((164 + j * (TW + 2), y + 2), f'{t:.2f}', fill='yellow', font=F)
    S.save(f'gaze/me/g{p // per:02d}.jpg', quality=85)
print(f'{len(rows)} janelas -> gaze/me/g00..g{(len(rows) - 1) // per:02d}.jpg')
