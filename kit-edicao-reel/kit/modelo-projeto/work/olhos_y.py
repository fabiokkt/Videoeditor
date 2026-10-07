"""Mede a altura dos olhos do apresentador (FaceMesh 33/133/362/263) em instantes da TIMELINE, na geometria 1080x1920,
para calcular o splitShiftY (docs/05 §12): alvo y=1377; y_zoom = origem + (y - origem) * escala (origem 53% = 1017,6).
uso: python3 work/olhos_y.py t1 t2 ...   (instantes de timeline dentro das janelas de split)"""
import json, sys, cv2, mediapipe as mp, numpy as np
sys.path.insert(0, 'scripts')
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
from _src import SRC
P=json.load(open('assets/edit-plan.json')); RATE=P.get('rate',1.1); F=1/30; LEAD=P.get('jcutLeadFrames',5)*F
segs=[];t=0
for i,s in enumerate(P['segments']):
    sd=round((s['out']-s['in'])/RATE,3); lead=0 if i==0 else min(LEAD,sd-10*F); d=round(sd-lead,3)
    segs.append(dict(i=i,t0=round(t,3),t1=round(t+d,3),lead=lead,**s)); t=round(t+d,3)
def src_of(tl):
    for s in segs:
        if s['t0']<=tl<s['t1']: return s['in']+(s['lead']+tl-s['t0'])*RATE
lmk=vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=mpt.BaseOptions(model_asset_path='.models/face_landmarker.task'),num_faces=1))
cap=cv2.VideoCapture(SRC); ys=[]
for tl in map(float,sys.argv[1:]):
    s=src_of(tl); cap.set(cv2.CAP_PROP_POS_MSEC,s*1000); ok,fr=cap.read()
    r=lmk.detect(mp.Image(image_format=mp.ImageFormat.SRGB,data=cv2.cvtColor(fr,cv2.COLOR_BGR2RGB)))
    if not r.face_landmarks: print(f't={tl:.2f} sem rosto'); continue
    L=r.face_landmarks[0]; y=np.mean([L[k].y for k in (33,133,362,263)])*1920; ys.append(y)
    print(f't={tl:.2f} src={s:.2f} olhos y={y:.0f}')
y=float(np.median(ys)); o=0.53*1920
for z in P['presenterZoom']['scales']+[1.0]:
    yz=o+(y-o)*z; print(f'mediana y={y:.0f} · zoom {z}: y_zoom={yz:.0f} -> splitShiftY={1377-yz:.0f}')
