"""Olhar para baixo/lado por blendshapes do FaceLandmarker (.models/face_landmarker.task),
quadro a quadro nas bordas de cada take (últimos 1,6 s e primeiros 0,6 s) + meio do take.
Saída gaze/blend.json: {seg: [{t, down, out, inn, blink}]}; down = média eyeLookDown L/R,
side = max(eyeLookOut/In) com sinal (+ = direita da tela)."""
import json, cv2, mediapipe as mp, numpy as np, sys
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
from _src import SRC
P=json.load(open('assets/edit-plan.json'))
opt=vision.FaceLandmarkerOptions(base_options=mpt.BaseOptions(model_asset_path='.models/face_landmarker.task'),
    output_face_blendshapes=True,num_faces=1,running_mode=vision.RunningMode.IMAGE)
lmk=vision.FaceLandmarker.create_from_options(opt)
cap=cv2.VideoCapture(SRC); FPS=30
segs=[int(x) for x in sys.argv[1:]] or range(len(P['segments']))
out={}
for i in segs:
    s=P['segments'][i]; mid=(s['in']+s['out'])/2
    wins=[(s['in']-0.5,s['in']+0.6),(mid-0.5,mid+0.5),(s['out']-1.6,s['out']+0.3)]
    rows=[]
    for a,b in wins:
        f0=int(round(max(0,a)*FPS)); cap.set(cv2.CAP_PROP_POS_FRAMES,f0)
        for f in range(f0,int(round(b*FPS))+1):
            ok,fr=cap.read()
            if not ok: break
            img=mp.Image(image_format=mp.ImageFormat.SRGB,data=cv2.cvtColor(cv2.resize(fr,(540,960)),cv2.COLOR_BGR2RGB))
            r=lmk.detect(img)
            if not r.face_blendshapes: continue
            d={c.category_name:c.score for c in r.face_blendshapes[0]}
            rows.append({"t":round(f/FPS,3),"down":round((d['eyeLookDownLeft']+d['eyeLookDownRight'])/2,3),
              "up":round((d['eyeLookUpLeft']+d['eyeLookUpRight'])/2,3),
              "blink":round((d['eyeBlinkLeft']+d['eyeBlinkRight'])/2,3),
              "side":round(((d['eyeLookOutLeft']+d['eyeLookInRight'])-(d['eyeLookInLeft']+d['eyeLookOutRight']))/2,3)})
    out[i]=rows; print(i, len(rows), flush=True)
json.dump(out,open('gaze/blend.json','w'))
