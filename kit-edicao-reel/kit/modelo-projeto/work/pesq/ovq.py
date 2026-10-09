# (reel Michael Gerber, 2026-10-08) uso: ovq.py "consulta" ["&source=wikimedia"] -> lista da Openverse (API anonima, page_size <= 20), licencas pdm/cc0/by/by-sa.
# Achou a foto CC BY-SA da pessoa-tema (Flickr) quando a Wikipedia nao tinha imagem; com source=wikimedia busca no Commons sem o 429 da API do Commons.
import json,sys,urllib.request,urllib.parse,time
q=sys.argv[1]; extra=sys.argv[2] if len(sys.argv)>2 else ''
u="https://api.openverse.org/v1/images/?"+urllib.parse.urlencode({'q':q,'page_size':20,'license':'pdm,cc0,by,by-sa'})+extra
d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60))
print('##',q,d.get('result_count'))
for r in d.get('results',[]):
    print(f"{r['id'][:8]} {r['width']}x{r['height']} {r['license']} {r['source']} | {r['title'][:90]} | {r['url']}")
