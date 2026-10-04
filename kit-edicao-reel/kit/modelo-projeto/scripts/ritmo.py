"""Ritmo visual: nenhum trecho pode passar de MAX s sem algo mudar na tela.
Conta como evento: entrada/saída de B-roll, corte do apresentador com troca de zoom,
callout, light-leak e transição de split. Lê o index.html gerado."""
import re, sys, json, os
MAX=float(sys.argv[1]) if len(sys.argv)>1 else 4.0
h=open('index.html').read()
T=float(re.search(r'id="root"[^>]*data-duration="([\d.]+)"',h)[1])
attr=lambda tag,k: (re.search(k+r'="([^"]*)"',tag) or [None,None])[1]
ev=[(0.0,'inicio')]
full=[(g['t0'],g['t1']) for g in json.load(open('work/broll-groups.json')) if g['mode']!='split']
hidden=lambda x: any(a-0.01<=x<b-0.01 for a,b in full)
prev=None
# corte com zoom: tl.set("#presenter-zoom", { scale: X }, T)
for m in re.finditer(r'tl\.set\("#presenter-zoom", \{ scale: ([\d.]+) \}, ([\d.]+)\)',h):
    sc=float(m[1]); t=float(m[2])
    if (prev is None or sc!=prev) and not hidden(t): ev.append((t,f'zoom {sc}'))
    prev=sc
# entradas/saidas de B-roll pelas cenas (com bakedBroll as cenas de tela cheia sao uma faixa so)
for g in json.load(open('work/broll-groups.json')):
    ev+= [(g['t0'],'broll in '+g['file'].split('/')[-1][:22]),(g['t1'],'broll out')]
full=[(g['t0'],g['t1']) for g in json.load(open('work/broll-groups.json')) if g['mode']!='split']
# cortes DENTRO de uma cena concatenada (várias tomadas num arquivo só)
if os.path.exists('work/broll-groups.json'):
    for g in json.load(open('work/broll-groups.json')):
        t=g['t0']
        for sh in g['shots'][:-1]:
            t+=sh['dur']; ev.append((round(t,2),'tomada '+sh['file'].split('/')[-1][:18]))
for tag in re.findall(r'<div[^>]*class="clip cap-big"[^>]*>',h): ev.append((float(attr(tag,'data-start')),'callout'))
for x in json.load(open('work/leaks.json'))['leaks']: ev.append((x['start'],'leak'))
ev=sorted(set((round(t,2),n) for t,n in ev if t<=T)); ev.append((T,'fim'))
gaps=[(a[0],b[0],b[0]-a[0],a[1]) for a,b in zip(ev,ev[1:]) if b[0]-a[0]>MAX]
print(f"duração {T:.2f}s · {len(ev)} eventos · maior intervalo {max(b[0]-a[0] for a,b in zip(ev,ev[1:])):.2f}s")
for a,b,d,n in gaps: print(f"  SEM EVENTO {a:7.2f} -> {b:7.2f} ({d:.2f}s) depois de: {n}")
print("OK" if not gaps else f"{len(gaps)} trechos acima de {MAX}s")
