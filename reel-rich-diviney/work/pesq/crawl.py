#!/usr/bin/env python3
# BFS serial em www.kyocera.co.jp/inamori (limite de paginas); grava crawl.json {img_url: [page, alt]}
import urllib.request, re, json, sys, time, urllib.parse
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
base=sys.argv[1]; pref=sys.argv[2]; lim=int(sys.argv[3]); out=sys.argv[4]
seen=set([base]); q=[base]; imgs={}
n=0
while q and n<lim:
    u=q.pop(0); n+=1
    try: h=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=25).read().decode('utf-8','ignore')
    except Exception as e: print('ERR',u,e); continue
    for m in re.finditer(r'<img[^>]+>',h):
        t=m.group(0); s=re.search(r'src="([^"]+)"',t); a=re.search(r'alt="([^"]*)"',t)
        if not s: continue
        iu=urllib.parse.urljoin(u,s.group(1))
        if re.search(r'assets/img|\.svg|\.gif',iu): continue
        imgs.setdefault(iu,[u,a.group(1) if a else ''])
    for m in re.finditer(r'href="([^"#]+)"',h):
        l=urllib.parse.urljoin(u,m.group(1)).split('#')[0]
        if re.search(r'\.(jpg|jpeg|png)$',l,re.I) and pref in l: imgs.setdefault(l,[u,'link'])
        if l.startswith(pref) and l not in seen and not re.search(r'\.(css|js|png|jpg|jpeg|pdf|ico|svg|mp4)$',l):
            seen.add(l); q.append(l)
    time.sleep(0.3)
json.dump(imgs,open(out,'w'),ensure_ascii=False,indent=0); print(n,'pages',len(imgs),'imgs', len(q),'left')
