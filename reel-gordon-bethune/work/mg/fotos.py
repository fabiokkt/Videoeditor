"""POR VIDEO — reel GORDON BETHUNE. Prepara as fotos da camada: work/pesq/raw/<arquivo> -> assets/mg/<papel>.jpg
(recorte em fracao da imagem). A capa (gerada a pedido no Codex) sai de work/capa/capa.png; enquanto nao chega, entra a SUBSTITUTA
(marcada no print). Nada que identifique a Continental antes de "Gordon" (11,49 s): a pre-revelacao usa so a capa e a cabine sem marca.
uso: python3 work/mg/fotos.py"""
import os
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
R = 'work/pesq/raw/'
# papel -> ([candidatos em ordem], recorte (x0, y0, x1, y1) em fracao, substituta)
FOTOS = {
    'capa-gordon.jpg': (['../../capa/capa.png'], (0, 0, 1, 1), 'wm_t1_5.jpg'),
    'capa-fogo.jpg': (['../../capa/capa.png'], (0.22, 0.0, 0.78, 0.62), 'wm_t1_5.jpg'),      # detalhe: o manual pegando fogo
    'cabine-767-b.jpg': (['wm_t1_5.jpg'], (0, 0, 1, 1), None),                             # pilotos de costas, sem marca (pre-revelacao)
    'gordon-777.jpg': (['wm_t1_0.jpg'], (0, 0, 1, 1), None),                               # 777 N78001 batizado "Gordon M. Bethune"
    'continental-727-1994.jpg': (['wm_t1_1.jpg'], (0, 0, 1, 1), None),                     # Miami, marco de 1994
    'continental-737-1994.jpg': (['wm_t1_15.jpg'], (0, 0, 1, 1), None),                    # Cleveland, out/1994
    'hangar-iah.jpg': (['wm_t1_9.jpg', 'wm_t1_8.jpg'], (0, 0, 1, 1), None),                # hangar da Continental em Houston
    'tripulacao.jpg': (['wm_t1_7.jpg'], (0, 0, 1, 1), None),                               # comissarias da Continental com os passageiros (2001)
    'a300-miami-1994.jpg': (['wm_t1_3.jpg'], (0, 0, 1, 1), None),                          # Miami, marco de 1994
    'cabine-767.jpg': (['wm_t1_4.jpg'], (0, 0, 1, 1), None),                               # os pilotos na cabine
    'cabine-passageiros.jpg': (['wm_t1_6.jpg'], (0, 0, 1, 1), None),                       # passageiros na cabine
    'dc10-1996.jpg': (['wm_t1_16.jpg'], (0, 0, 1, 1), None),                               # DC-10 da Continental, 1996 (clímax)
}
os.makedirs('assets/mg', exist_ok=True)
for out, (cands, box, sub) in FOTOS.items():
    src = next((c for c in cands if os.path.exists(R + c)), None); tag = ''
    if src is None:
        src = sub; box = (0, 0, 1, 1); tag = '  << SUBSTITUTA (capa pendente)'
    im = ImageOps.exif_transpose(Image.open(R + src)).convert('RGB')
    W, H = im.size
    im = im.crop((int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)))
    if max(im.size) > 2400: im.thumbnail((2400, 2400), Image.LANCZOS)
    im.save('assets/mg/' + out, quality=92)
    print(f'{out:<28} <- {src:<22} {im.size[0]}x{im.size[1]}{tag}')
