"""Mede desvio de olhar quadro a quadro no mezanino (FaceMesh + iris refinada).
gx > 0 => iris deslocada para a DIREITA DA TELA ; yaw > 0 => cabeca virada p/ direita da tela."""
import cv2, json, numpy as np, mediapipe as mp
from _src import SRC
STEP=0.08
fm=mp.solutions.face_mesh.FaceMesh(static_image_mode=False,max_num_faces=1,
    refine_landmarks=True,min_detection_confidence=0.5,min_tracking_confidence=0.5)
R_OUT,R_IN=33,133; L_IN,L_OUT=362,263
RIRIS=[469,470,471,472]; LIRIS=[474,475,476,477]
cap=cv2.VideoCapture(SRC); fps=cap.get(cv2.CAP_PROP_FPS)
out=[]; nxt=0.0; i=0
while True:
    ok,frame=cap.read()
    if not ok: break
    t=i/fps; i+=1
    if t+1e-9<nxt: continue
    nxt+=STEP
    small=cv2.resize(frame,(540,960))
    res=fm.process(cv2.cvtColor(small,cv2.COLOR_BGR2RGB))
    if not res.multi_face_landmarks:
        out.append({"t":round(t,3),"ok":0}); continue
    lm=res.multi_face_landmarks[0].landmark
    def ratio(inn,outr,iris):
        xi,xo=lm[inn].x,lm[outr].x
        cx=sum(lm[k].x for k in iris)/len(iris); w=xo-xi
        return (cx-xi)/w if abs(w)>1e-6 else 0.5
    rr=ratio(R_IN,R_OUT,RIRIS); lr=ratio(L_IN,L_OUT,LIRIS)
    gx=((0.5-rr)+(lr-0.5))/2
    x33,x263,xn=lm[33].x,lm[263].x,lm[1].x
    yaw=(xn-(x33+x263)/2)/abs(x263-x33) if abs(x263-x33)>1e-6 else 0
    op=((lm[145].y-lm[159].y)+(lm[374].y-lm[386].y))/2
    # gy: altura da íris em relação à linha dos cantos do olho, normalizada pela largura do olho
    # (gy maior => olhar para BAIXO — leitura do roteiro abaixo da câmera, reel André Esteves)
    def vy(a,b,iris):
        cy=sum(lm[k].y for k in iris)/len(iris); return (cy-(lm[a].y+lm[b].y)/2)/max(1e-6,abs(lm[b].x-lm[a].x))
    gy=(vy(33,133,RIRIS)+vy(362,263,LIRIS))/2
    out.append({"t":round(t,3),"ok":1,"gx":round(gx,4),"yaw":round(yaw,4),"op":round(op,5),"gy":round(gy,4)})
cap.release()
json.dump(out,open('gaze/measure.json','w'))
g=[o for o in out if o.get("ok")]
print(f"{len(out)} amostras, {len(g)} com rosto")
for k in ("gx","yaw","op","gy"):
    v=np.array([o[k] for o in g])
    print(f"  {k}: mediana {np.median(v):+.4f}  p2 {np.percentile(v,2):+.4f}  p98 {np.percentile(v,98):+.4f}  sd {v.std():.4f}")
