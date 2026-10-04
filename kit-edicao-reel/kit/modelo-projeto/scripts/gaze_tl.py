"""Olhar quadro a quadro NA TIMELINE (30 amostras/s), so onde o apresentador aparece em algum take.
FaceLandmarker (.models/face_landmarker.task) com blendshapes: down/up (eyeLookDown/Up), side (+ = direita
da tela), blink. Le o mezanino em sequencia (rapido) e converte source->timeline pela mesma conta do
build-edit.mjs (lead do J-cut, videoTail). Saida: gaze/tl.json [{t, seg, src, down, up, side, blink}].
Depois: scripts/gaze_windows.py transforma em janelas de leitura."""
import json, cv2, mediapipe as mp
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
from _src import SRC
P=json.load(open('assets/edit-plan.json')); RATE=P.get('rate',1.1); F=1/30; LEAD=P.get('jcutLeadFrames',5)*F
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/RATE,3); lead=0 if i==0 else min(LEAD,sd-10*F); d=round(sd-lead,3)
    segs.append(dict(i=i,t0=round(t,3),t1=round(t+d,3),lead=lead,**s)); t=round(t+d,3)
ed=[round((s['out']-s['videoTail'])/RATE,3) if s.get('videoTail') else 0 for s in segs]
R=[]  # (src0, src1, vStart, seg)
for k,s in enumerate(segs):
    dPrev=ed[k-1] if k>0 else 0
    vS=round(s['t0']-dPrev,3); vE=round(s['t1']-ed[k],3); vM=round(s['in']+(s['lead']-dPrev)*RATE,3)
    R.append((vM, vM+(vE-vS)*RATE, vS, k))
opt=vision.FaceLandmarkerOptions(base_options=mpt.BaseOptions(model_asset_path='.models/face_landmarker.task'),
    output_face_blendshapes=True,num_faces=1,running_mode=vision.RunningMode.IMAGE)
lmk=vision.FaceLandmarker.create_from_options(opt)
cap=cv2.VideoCapture(SRC); fps=cap.get(cv2.CAP_PROP_FPS); n=0; out=[]
while True:
    ok=cap.grab()
    if not ok: break
    src=n/fps; n+=1
    hit=[r for r in R if r[0]-1e-6<=src<r[1]]
    if not hit: continue
    # 30 amostras por segundo de TIMELINE ~ 33 por segundo de source: pega 1 quadro a cada 2 (60 fps)
    if (n-1)%2: continue
    ok,fr=cap.retrieve()
    img=mp.Image(image_format=mp.ImageFormat.SRGB,data=cv2.cvtColor(cv2.resize(fr,(540,960)),cv2.COLOR_BGR2RGB))
    r=lmk.detect(img)
    for s0,s1,vS,k in hit:
        tl=round(vS+(src-s0)/RATE,3)
        if not r.face_blendshapes: out.append({"t":tl,"seg":k,"src":round(src,3),"ok":0}); continue
        d={c.category_name:c.score for c in r.face_blendshapes[0]}
        out.append({"t":tl,"seg":k,"src":round(src,3),"ok":1,
            "down":round((d['eyeLookDownLeft']+d['eyeLookDownRight'])/2,3),
            "up":round((d['eyeLookUpLeft']+d['eyeLookUpRight'])/2,3),
            "blink":round((d['eyeBlinkLeft']+d['eyeBlinkRight'])/2,3),
            "side":round(((d['eyeLookOutLeft']+d['eyeLookInRight'])-(d['eyeLookInLeft']+d['eyeLookOutRight']))/2,3)})
out.sort(key=lambda o:o['t'])
json.dump(out,open('gaze/tl.json','w'))
print(f"{len(out)} amostras na timeline ({sum(o['ok'] for o in out)} com rosto)")
