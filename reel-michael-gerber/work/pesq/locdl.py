#!/usr/bin/env python3
# (reel Michael Gerber, 2026-10-08) uso (de work/pesq): locdl.py <colecao> <id> [largura=2600]   ex.: locdl.py fsa 8b23573 · locdl.py hec 26939 · locdl.py mrg 00126
# Library of Congress em ALTA sem passar pelo loc.gov (Cloudflare "Just a moment...") nem pelo original do Flickr (429 "CIDR range blocked"):
# baixa o TIFF master de tile.loc.gov/storage-services/master/pnp/<colecao>/<milhar>/<centena>/<id>u.tif (FSA 1939: ~142 MB, 13 600 px),
# reduz para JPEG (raw/loc_<id>.jpg) e apaga o TIFF. O id vem da descricao da foto da LOC no Flickr ("fsa.8b23573", "hec.26939").
# O IIIF do master devolve 500 (arquivo grande demais); o "v.jpg" de servico tem so 1024 px.
import sys, os, re, urllib.request
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
col, id_ = sys.argv[1], sys.argv[2]; W = int(sys.argv[3]) if len(sys.argv) > 3 else 2600
m = re.match(r'(.*?)(\d+)$', id_); pre, num = m.group(1), int(m.group(2)); n = len(m.group(2))
d1 = f'{pre}{num // 1000 * 1000:0{n}d}'; d2 = f'{pre}{num // 100 * 100:0{n}d}'
# fsa: dois niveis (8b23000/8b23500); hec, mrg e as outras: um nivel (26900, 00100) — conferido nas fotos deste reel
dirs = f'{d1}/{d2}' if col == 'fsa' else d2
u = f'https://tile.loc.gov/storage-services/master/pnp/{col}/{dirs}/{id_}u.tif'
os.makedirs('tif', exist_ok=True); os.makedirs('raw', exist_ok=True); t = f'tif/{id_}.tif'
req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=600) as r, open(t, 'wb') as f:
    while True:
        b = r.read(1 << 20)
        if not b: break
        f.write(b)
im = Image.open(t); print(id_, im.size, im.mode)
im = im.convert('L') if im.mode not in ('L', 'RGB') else im
im.thumbnail((W, W), Image.LANCZOS); im.convert('RGB').save(f'raw/loc_{id_}.jpg', quality=93); os.remove(t)
print(f'raw/loc_{id_}.jpg', im.size)
