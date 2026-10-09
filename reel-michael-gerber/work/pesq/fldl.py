# uso (de work/pesq): fldl.py <tag> <photo_id> <owner_nsid_ou_alias>  -> raw/fl_<tag>.jpg  (maior tamanho de pagina sizes: k > h > b)
import sys,re,urllib.request,subprocess
tag,pid,own=sys.argv[1:4]
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'}
for s in ('k','h','b'):
    try:
        t=urllib.request.urlopen(urllib.request.Request(f'https://www.flickr.com/photos/{own}/{pid}/sizes/{s}/',headers=UA),timeout=60).read().decode('utf8','ignore')
    except Exception as e: continue
    m=re.search(r'https://live\.staticflickr\.com/[^"\']+_'+s+r'\.jpg',t)
    if not m: continue
    d=urllib.request.urlopen(urllib.request.Request(m.group(0),headers=UA),timeout=120).read()
    if d[:2]!=b'\xff\xd8': continue
    open(f'raw/fl_{tag}.jpg','wb').write(d); print(tag,s,len(d)); break
else: print(tag,'FALHOU')
