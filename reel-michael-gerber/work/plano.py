"""POR VIDEO — reel MICHAEL GERBER. Campos do plano que nao saem do corte (rodar depois do plan_segments.py / fase2.sh):
callouts (impacts), secoes (leaks grandes), ctaSeg, splitShiftY (medido: work/olhos_y.py). uso: python3 work/plano.py [splitShiftY]"""
import json, sys
P = json.load(open('assets/edit-plan.json'))
L = [s['label'] for s in P['segments']]; ix = {l: i for i, l in enumerate(L)}
P['impacts'] = [
    {"phrase": "tem um emprego", "seg": ix['EMPREGO'], "style": "typing", "lines": ["TEM UM", "EMPREGO."], "hold": 0.2},
    {"phrase": "funcionario mais explorado", "seg": ix['PROTOCOLO-EXPLORADO'], "lines": ["O FUNCIONÁRIO", "MAIS EXPLORADO."], "hold": 0.5},
    {"phrase": "voce nao e o dono", "seg": ix['P1-DONO'], "lines": ["VOCÊ NÃO É", "O DONO."], "hold": 0.5},
    {"phrase": "ela nao funciona", "seg": ix['P2-GAFANHOTO'], "lines": ["ELA NÃO", "FUNCIONA."], "hold": 0.2},
    {"phrase": "loja de torta", "seg": ix['FECHO-LOJA'], "lines": ["LOJA DE", "TORTA."], "hold": 0.6},
]
P['sections'] = [
    {"afterSegment": ix['CTA-COMENTA'], "name": "CTA DO MEIO -> VIRADA (a loja de torta)"},
    {"afterSegment": ix['VIRADA-CHEIRO'], "name": "VIRADA -> CLIMAX (empresa -> emprego)"},
    {"afterSegment": ix['FECHO-LOJA'], "name": "FECHO -> CTA"},
]
P['ctaSeg'] = ix['CTA-SEGUE']
if len(sys.argv) > 1: P['splitShiftY'] = int(sys.argv[1])
json.dump(P, open('assets/edit-plan.json', 'w'), ensure_ascii=False, indent=1)
print('impacts', len(P['impacts']), '· sections', [s['afterSegment'] for s in P['sections']], '· ctaSeg', P['ctaSeg'], '· splitShiftY', P['splitShiftY'])
