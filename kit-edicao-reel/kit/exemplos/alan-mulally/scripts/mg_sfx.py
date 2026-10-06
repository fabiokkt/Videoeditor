"""SFX da camada de motion graphics (compositions/mg.html) — kit sintetizado da skill showreel-interface
(~/.claude/skills/showreel-interface/scripts/sfx.py). Cada cue marca o PICO do som no quadro do evento visual.
Mistura POR CIMA do bed do formato (trilha + SFX fixos, que continuam todos): rodar SEMPRE depois de `bake.py bed`.
uso: python3 scripts/mg_sfx.py            (le assets/bed.m4a recem-assado, guarda copia em work/bed-base.wav, regrava assets/bed.m4a)"""
import sys, os, json, subprocess, shutil
import numpy as np
sys.path.insert(0, os.path.expanduser('~/.claude/skills/showreel-interface/scripts'))
import sfx as K

SR = K.SR
TOTAL = json.load(open('work/mix-plan.json'))['total']

def tiques(t0, n, passo=2/30, g=-26):
    return [(round(t0 + k * passo, 3), 'tique', g, {}) for k in range(n)]

C = [
 # S1 revelacao
 (13.23, 'whoosh', -17, {}), (13.62, 'pop', -21, {}), (15.62, 'whoosh', -14, {}), (16.51, 'impacto', -18, {'dur': 0.9}),
 (16.51, 'clique', -18, {}), (16.87, 'pop', -23, {}), (17.93, 'whoosh', -15, {}), (18.35, 'pop', -20, {}),
 (19.33, 'impacto', -17, {'dur': 1.2}), (19.33, 'subdrop', -21, {}), (20.5, 'swish', -18, {}),
 # S2 passo 1
 (24.87, 'whoosh', -17, {}), (25.07, 'cacaniquel', -20, {}), *[(t, 'tique', -24, {}) for t in (25.07, 25.44, 25.94, 26.37)],
 (26.8, 'clique', -20, {}), (27.72, 'whoosh', -14, {}), (28.96, 'pop', -18, {}), (28.98, 'ding', -24, {}),
 (30.67, 'clique', -17, {}), (30.67, 'pop', -20, {'f0': 420, 'f1': 160, 'dur': 0.14}), (31.4, 'swish', -18, {}),
 # S3 passo 2
 (36.2, 'whoosh', -17, {}), (36.42, 'pop', -21, {}), (37.57, 'cacaniquel', -20, {}), (38.27, 'swish', -18, {}),
 (38.59, 'clique', -18, {'freq': 2400}), (38.75, 'clique', -18, {'freq': 3000}), (38.91, 'clique', -18, {'freq': 3700}),
 *tiques(39.13, 7, g=-27), (39.6, 'ding', -20, {}), (40.4, 'swish', -18, {}),
 # S4 o quadro
 (45.13, 'whoosh', -17, {}), *tiques(45.2, 5, g=-27), (45.61, 'clique', -18, {}), (45.62, 'ding', -25, {}),
 (46.59, 'clique', -18, {}), (49.2, 'clique', -16, {}), (50.03, 'subdrop', -21, {}), (51.9, 'swish', -18, {}),
 # S5 passo 3
 (56.03, 'whoosh', -17, {}), (56.12, 'pop', -21, {}), (56.5, 'cacaniquel', -20, {}), (57.14, 'tique', -24, {}),
 (57.54, 'tique', -24, {}), (58.12, 'pop', -18, {}), (58.72, 'swish', -17, {}), (59.13, 'swish', -18, {}),
 # S6 zoou -> gafanhoto
 (63.22, 'whoosh', -17, {}), (64.91, 'pop', -18, {'f0': 900}), (65.18, 'pop', -18, {'f0': 1100}), (65.45, 'pop', -18, {'f0': 1300}),
 (65.65, 'clique', -19, {}), (66.94, 'whoosh', -14, {}), (68.84, 'pop', -20, {}), (69.58, 'swish', -18, {}),
 # S7 17 bi (split)
 (72.5, 'whoosh', -15, {}), (73.6, 'cacaniquel', -18, {'dur': 0.85, 'n_tiques': 11}), (74.48, 'impacto', -18, {'dur': 1.2}),
 *tiques(74.5, 5, g=-26),
 # S8 Mark -> producao parada
 (75.95, 'whoosh', -17, {}), (76.25, 'pop', -20, {}), (78.35, 'whoosh', -15, {}), (78.87, 'clique', -16, {}),
 (78.87, 'impacto', -22, {'dur': 0.7}), (80.54, 'pop', -21, {}), (81.24, 'swish', -18, {}),
 # S9 primeiro vermelho -> palma -> arco-iris (88,12: riser + impact do formato ja estao no bed)
 (84.66, 'whoosh', -17, {}), *tiques(84.72, 6, g=-27), (86.06, 'clique', -14, {}), (86.06, 'impacto', -20, {'dur': 0.9}),
 (88.29, 'impacto', -19, {'dur': 0.6}), (88.29, 'swish', -20, {}), (91.1, 'whoosh', -14, {}),
 *tiques(91.62, 5, passo=0.08, g=-24), *[(round(92.25 + k * 2/30, 3), 'pop', -24, {'f0': 700 + 120 * k}) for k in range(6)],
 (93.16, 'ding', -16, {}), (94.45, 'swish', -18, {}),
]

N = int((TOTAL + 1) * SR)
bus = np.zeros((N, 2))
for t, som, g, args in C:
    s, pico = K.SONS[som](**args)
    if s.ndim == 1: s = np.stack([s, s], 1)
    k = int(round(t * SR)) - pico
    i0, j0 = max(0, k), max(0, -k); m = min(len(s) - j0, N - i0)
    if m > 0: bus[i0:i0 + m] += s[j0:j0 + m] * K.db(g)
bus = bus[:int(TOTAL * SR)]

base = 'work/bed-base.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'assets/bed.m4a', '-ar', str(SR), '-ac', '2', base], check=True)
b = K.le_audio(base)
n = min(len(b), len(bus)); out = b[:n] + bus[:n]
pk = np.abs(out).max(); print(f'{len(C)} cues · pico do bed+mg {20*np.log10(pk):.1f} dBFS')
K.grava('work/bed-mg.wav', out)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'work/bed-mg.wav', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', 'assets/bed.m4a'], check=True)
json.dump([dict(t=t, som=s, ganho=g, args=a) for t, s, g, a in C], open('work/mg-cues.json', 'w'), indent=0)
print('assets/bed.m4a = bed do formato + SFX do motion')
