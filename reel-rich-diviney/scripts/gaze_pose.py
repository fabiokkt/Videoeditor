"""Varredura de olhar COMPENSADA pela pose da cabeca (reel KAZUO INAMORI).
Motivo: os blendshapes eyeLook* medem o olho DENTRO da cabeca. Este apresentador grava de perto e mexe muito a cabeca
sem tirar o olho da lente — o gaze_windows.py marcava 40 janelas / 19,5 s que eram quase todas giro de cabeca.
Aqui: yaw/pitch da cabeca (matriz de transformacao facial) + centro do rosto no quadro; regressao robusta
side ~ yaw + cx e vert(down-up) ~ pitch + cy (quem olha para a lente compensa o giro com o olho). O RESIDUO e o desvio real.
Saida: gaze/pose.json (amostras com rs, rv) e gaze/pose-windows.json (janelas |residuo| > K sigma, >= 0,15 s, sem piscada).
Uso: gaze_pose.py [K=3.0]"""
import json, sys, cv2, numpy as np, mediapipe as mp, os
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
from _src import SRC
K=float(sys.argv[1]) if len(sys.argv)>1 else 3.0
if not os.path.exists('gaze/pose-raw.json') or '--remeasure' in sys.argv:
    T=json.load(open('gaze/tl.json'))
    bysrc={}
    for o in T: bysrc.setdefault(round(o['src'],3),[]).append(o)
    opt=vision.FaceLandmarkerOptions(base_options=mpt.BaseOptions(model_asset_path='.models/face_landmarker.task'),
        output_face_blendshapes=True,output_facial_transformation_matrixes=True,num_faces=1,running_mode=vision.RunningMode.IMAGE)
    lmk=vision.FaceLandmarker.create_from_options(opt)
    cap=cv2.VideoCapture(SRC); fps=cap.get(cv2.CAP_PROP_FPS); n=0; out=[]
    while True:
        if not cap.grab(): break
        src=round(n/fps,3); n+=1
        if src not in bysrc: continue
        ok,fr=cap.retrieve()
        r=lmk.detect(mp.Image(image_format=mp.ImageFormat.SRGB,data=cv2.cvtColor(cv2.resize(fr,(540,960)),cv2.COLOR_BGR2RGB)))
        if not r.face_blendshapes: continue
        d={c.category_name:c.score for c in r.face_blendshapes[0]}
        M=np.array(r.facial_transformation_matrixes[0])[:3,:3]
        yaw=float(np.degrees(np.arctan2(M[0,2],M[2,2]))); pitch=float(np.degrees(np.arcsin(-M[1,2])))
        L=r.face_landmarks[0]; cx=float(np.mean([L[i].x for i in (33,133,362,263)])); cy=float(np.mean([L[i].y for i in (33,133,362,263)]))
        side=((d['eyeLookOutLeft']+d['eyeLookInRight'])-(d['eyeLookInLeft']+d['eyeLookOutRight']))/2
        vert=((d['eyeLookDownLeft']+d['eyeLookDownRight'])-(d['eyeLookUpLeft']+d['eyeLookUpRight']))/2
        blink=(d['eyeBlinkLeft']+d['eyeBlinkRight'])/2
        for o in bysrc[src]: out.append(dict(t=o['t'],seg=o['seg'],src=src,yaw=round(yaw,2),pitch=round(pitch,2),cx=round(cx,4),cy=round(cy,4),side=round(side,3),vert=round(vert,3),blink=round(blink,3)))
    out.sort(key=lambda o:o['t']); json.dump(out,open('gaze/pose-raw.json','w'))
S=json.load(open('gaze/pose-raw.json'))
def fit(y,X):
    w=np.ones(len(y))
    for _ in range(8):
        A=np.c_[X,np.ones(len(y))]*w[:,None]; c=np.linalg.lstsq(A,y*w,rcond=None)[0]
        r=y-np.c_[X,np.ones(len(y))]@c; s=1.4826*np.median(np.abs(r-np.median(r)))
        w=(np.abs(r)<2.5*s).astype(float)
    return c,r,s
nb=np.array([o['blink']<0.4 for o in S])
side=np.array([o['side'] for o in S]); vert=np.array([o['vert'] for o in S])
Xs=np.array([[o['yaw'],o['cx']] for o in S]); Xv=np.array([[o['pitch'],o['cy']] for o in S])
cs,_,ss=fit(side[nb],Xs[nb]); cv_,_,sv=fit(vert[nb],Xv[nb])
rs=side-np.c_[Xs,np.ones(len(S))]@cs; rv=vert-np.c_[Xv,np.ones(len(S))]@cv_
print(f"side ~ {cs[0]:+.4f}*yaw {cs[1]:+.3f}*cx  sigma {ss:.3f} | vert ~ {cv_[0]:+.4f}*pitch {cv_[1]:+.3f}*cy  sigma {sv:.3f}  ({len(S)} amostras)")
for o,a,b in zip(S,rs,rv): o['rs']=round(float(a/ss),2); o['rv']=round(float(b/sv),2)
json.dump(S,open('gaze/pose.json','w'))
W=[];cur=None
for o in S:
    f=o['blink']<0.4 and (abs(o['rs'])>K or o['rv']>K)
    if f:
        if cur and o['t']-cur[1]<=0.1: cur[1]=o['t']; cur[2].append(o)
        else:
            if cur: W.append(cur)
            cur=[o['t'],o['t'],[o]]
if cur: W.append(cur)
res=[]
for a,b,os_ in W:
    if b-a+0.033<0.15: continue
    m=max(os_,key=lambda o:max(abs(o['rs']),o['rv']))
    res.append(dict(t0=round(a,2),t1=round(b+0.033,2),seg=os_[0]['seg'],rs=float(np.mean([o['rs'] for o in os_])),rv=float(np.mean([o['rv'] for o in os_])),pico=max(abs(m['rs']),m['rv'])))
    print(f"{a:6.2f}-{b+0.033:6.2f} ({b-a+0.033:.2f}s) seg{os_[0]['seg']:>2}  lado {res[-1]['rs']:+.1f}σ  baixo {res[-1]['rv']:+.1f}σ  pico {res[-1]['pico']:.1f}σ")
json.dump(res,open('gaze/pose-windows.json','w'),indent=1)
print(f"{len(res)} janelas, {sum(r['t1']-r['t0'] for r in res):.1f}s (K={K})")
