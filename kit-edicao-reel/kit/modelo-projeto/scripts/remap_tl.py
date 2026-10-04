"""Converte tempos de timeline de uma versao antiga do plano para a atual, passando pelo tempo de SOURCE
(o mesmo quadro do bruto). Uso como modulo: from remap_tl import remap; remap(t). Planos: $REMAP_OLD (padrao work/v1/edit-plan.json) -> assets/edit-plan.json"""
import json, os
def _segs(P):
    R=P['rate']; F=1/30; LEAD=P.get('jcutLeadFrames',5)*F; t=0; out=[]
    for i,s in enumerate(P['segments']):
        sd=round((s['out']-s['in'])/R,3); lead=0 if i==0 else min(LEAD,sd-10*F); d=round(sd-lead,3)
        out.append(dict(t0=round(t,3),t1=round(t+d,3),m0=round(s['in']+lead*R,3),R=R)); t=round(t+d,3)
    return out
OLD=_segs(json.load(open(os.environ.get('REMAP_OLD','work/v1/edit-plan.json')))); NEW=_segs(json.load(open('assets/edit-plan.json')))
def src_of(t,S=OLD):
    for s in S:
        if s['t0']-1e-6<=t<s['t1']+1e-6: return s['m0']+(t-s['t0'])*s['R']
    s=S[-1]; return s['m0']+(t-s['t0'])*s['R']
def tl_of(src,S=NEW):
    best=None
    for s in S:
        m1=s['m0']+(s['t1']-s['t0'])*s['R']
        if s['m0']-1e-6<=src<=m1+1e-6: return round(s['t0']+(src-s['m0'])/s['R'],3)
        d=min(abs(src-s['m0']),abs(src-m1))
        if best is None or d<best[0]: best=(d,s)
    s=best[1]; return round(min(max(s['t0']+(src-s['m0'])/s['R'],s['t0']),s['t1']),3)
def remap(t): return tl_of(src_of(t))
if __name__=='__main__':
    import sys
    for x in sys.argv[1:]: print(x,'->',remap(float(x)))
