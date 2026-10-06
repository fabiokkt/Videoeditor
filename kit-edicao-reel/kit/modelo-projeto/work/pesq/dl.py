#!/usr/bin/env python3
# uso: dl.py <tag> <img_url> <page_url> <dom>  -> raw/<tag>.jpg (converte com Pillow), registra em g_index.json
import sys, json, os, io, urllib.request
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
tag, img, page, dom = sys.argv[1:5]
if 'images.pexels.com' in img: img=img.split('?')[0]+'?auto=compress&cs=tinysrgb&w=3000'
req = urllib.request.Request(img, headers={'User-Agent': UA, 'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8', 'Referer': page})
try: data = urllib.request.urlopen(req, timeout=40).read()
except Exception as e: print(tag, 'FAIL', e); sys.exit(1)
out = f'raw/{tag}.jpg'
try:
    im = Image.open(io.BytesIO(data)); w, h = im.size
    if data[:3] == b'\xff\xd8\xff': open(out, 'wb').write(data)
    else:
        if im.mode in ('RGBA','LA','P'):
            im = im.convert('RGBA'); bg = Image.new('RGB', im.size, 'white'); bg.paste(im, mask=im.split()[3]); im = bg
        im.convert('RGB').save(out, quality=95)
except Exception as e: print(tag, 'CONVFAIL', e); sys.exit(1)
idx = json.load(open('g_index.json')) if os.path.exists('g_index.json') else {}
idx[tag] = dict(file=out, w=w, h=h, img=img, page=page, dom=dom)
json.dump(idx, open('g_index.json', 'w'), indent=1)
print(tag, w, h)
