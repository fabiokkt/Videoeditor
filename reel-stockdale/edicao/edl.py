import re,json,subprocess
P=[(0.55,5.40),(5.62,7.70),(10.80,14.75),(15.10,25.80),(26.0,30.90),(31.45,33.45),(37.45,43.0),(44.0,53.42),
(58.05,60.62),(60.9,65.9),(68.95,71.66),(72.1,75.7),(81.0,83.7),(89.55,93.97),(94.3,99.42),(101.35,105.25),
(105.45,111.2),(117.15,119.46),(119.85,126.4),(126.85,132.8),(133.1,137.75)]
out=subprocess.run("ffmpeg -i bruto.wav -af silencedetect=noise=-35dB:d=0.25 -f null -",shell=True,capture_output=True,text=True).stderr
st=[float(x) for x in re.findall(r"silence_start: ([\d.]+)",out)];en=[float(x) for x in re.findall(r"silence_end: ([\d.]+)",out)]
S=list(zip(st,en));PAD=0.09
segs=[]
for a,b in P:
    cur=a
    for s,e in S:
        if s>a and e<b and e-s>0.30:
            segs.append((cur,s+PAD));cur=e-PAD
    segs.append((cur,b))
segs=[(round(a,3),round(b,3)) for a,b in segs if b-a>0.12]
json.dump(segs,open("segs.json","w"))
print(len(segs),"segs, total",round(sum(b-a for a,b in segs),2))
