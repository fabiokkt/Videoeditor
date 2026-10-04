"""MOTOR (kit v3) + lista EXTRA por video. SFX da camada de motion graphics, com o kit sintetizado da skill
showreel-interface (~/.claude/skills/showreel-interface/scripts/sfx.py). Cada cue marca o PICO do som no quadro do evento.
Os cues vem SOZINHOS dos componentes do compositions/mg.html (cue() -> scripts/mg_cues.mjs -> work/mg-cues-auto.json);
EXTRA abaixo e so para som que nenhum componente dispara (ex.: ding no arco-iris).
Mistura POR CIMA do bed do formato (trilha + SFX fixos, que continuam todos): rodar SEMPRE depois de `bake.py bed`.
uso: node scripts/mg_cues.mjs && python3 scripts/mg_sfx.py"""
import sys, os, json, subprocess
import numpy as np
sys.path.insert(0, os.path.expanduser('~/.claude/skills/showreel-interface/scripts'))
import sfx as K

# POR VIDEO: (t_pico, som, ganho_dB, args). Sons: whoosh swish impacto subdrop clique tique cacaniquel pop riser ding reverso digitar
EXTRA = [
]

SR = K.SR
TOTAL = json.load(open('work/mix-plan.json'))['total']
auto = json.load(open('work/mg-cues-auto.json')) if os.path.exists('work/mg-cues-auto.json') else []
C = [(c['t'], c['som'], c['ganho'], c.get('args', {})) for c in auto] + list(EXTRA)

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
print(f'{len(C)} cues ({len(auto)} automaticos + {len(EXTRA)} extras) · pico do bed+mg {20*np.log10(np.abs(out).max()):.1f} dBFS')
K.grava('work/bed-mg.wav', out)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'work/bed-mg.wav', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', 'assets/bed.m4a'], check=True)
json.dump([dict(t=t, som=s, ganho=g, args=a) for t, s, g, a in C], open('work/mg-cues.json', 'w'), indent=0)
print('assets/bed.m4a = bed do formato + SFX do motion')
