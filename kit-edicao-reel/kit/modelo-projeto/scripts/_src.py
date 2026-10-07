"""Resolve o mezanino do projeto: `src` do edit-plan.json, senão o único assets/*-sdr.mp4."""
import json, glob, os
def mezanino():
    if os.path.exists('assets/edit-plan.json'):
        s = json.load(open('assets/edit-plan.json')).get('src')
        if s: return s
    c = glob.glob('assets/*-sdr.mp4')
    if len(c) != 1: raise SystemExit(f'mezanino ambíguo/ausente em assets/: {c}')
    return c[0]
SRC = mezanino()
