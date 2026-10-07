"""POR VIDEO — reel ERNEST SHACKLETON. Prepara as fotos da camada: work/pesq/raw/<arquivo> -> assets/mg/<papel>.jpg
(recorte em fracao da imagem: tira a borda arredondada das laminas de lanterna e o selo "Cornell University Library" das pranchas do
livro South, 1919). Foto que ainda nao baixou entra com a SUBSTITUTA (marcada no print) ate o download chegar.
uso: python3 work/mg/fotos.py"""
import os
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
R = 'work/pesq/raw/'
# papel -> ([candidatos em ordem], recorte (x0, y0, x1, y1) em fracao, substituta)
FOTOS = {
    'endurance-noite-1915.jpg': (['wm_endurance_158.jpg'], (0, 0, 1, 1), None),
    'endurance-vela-gelo-1915.jpg': (['wm_endurance_25.jpg'], (0.03, 0.02, 0.97, 0.98), 'wm_endurance_158.jpg'),
    'shackleton-expedicao-1915.jpg': (['wm_endurance_171.jpg'], (0, 0, 1, 1), None),
    'endurance-preso-1915.jpg': (['wm_endurance_105.jpg', 'wm_endurance_93.jpg'], (0.02, 0.02, 0.98, 0.98), 'wm_endurance_158.jpg'),
    'pinguins-1915.jpg': (['wm_endurance_461.jpg'], (0.45, 0.10, 0.90, 0.95), 'fl_elephant_yelcho_8725111406.jpg'),
    'hurley-shackleton-acampamento.jpg': (['wm_endurance_36.jpg'], (0, 0, 1, 1), 'wm_endurance_180.jpg'),
    'acampamento-gelo-1915.jpg': (['wm_endurance_404.jpg'], (0.06, 0.03, 0.90, 0.93), 'wm_endurance_99.jpg'),
    'trenos-prontos-1915.jpg': (['wm_endurance_433.jpg'], (0.02, 0.12, 0.84, 0.97), 'wm_endurance_404.jpg'),
    'solidao-gelo-1915.jpg': (['wm_endurance_399.jpg'], (0.02, 0.03, 0.88, 0.97), 'wm_endurance_158.jpg'),
    'abrindo-caminho-gelo-1915.jpg': (['wm_endurance_438.jpg'], (0.06, 0.03, 0.90, 0.93), 'wm_endurance_99.jpg'),
    'endurance-adernado-1915.jpg': (['wm_endurance_415.jpg'], (0.20, 0.0, 1.0, 0.93), None),
    'endurance-afundando-1915.jpg': (['wm_endurance_99.jpg'], (0.04, 0.03, 0.96, 0.97), None),
    'puxando-bote-1915.jpg': (['wm_endurance_411.jpg', 'wm_endurance_304.jpg'], (0.02, 0.03, 0.90, 0.95), 'wm_endurance_415.jpg'),
    'james-caird-partida-1916.jpg': (['wm_endurance_398.jpg', 'wm_endurance_4.jpg'], (0.02, 0.03, 0.84, 0.97), 'wm_endurance_99.jpg'),
}
os.makedirs('assets/mg', exist_ok=True)
for out, (cands, box, sub) in FOTOS.items():
    src = next((c for c in cands if os.path.exists(R + c)), None); tag = ''
    if src is None:
        src = sub; box = (0, 0, 1, 1); tag = '  << SUBSTITUTA (download pendente)'
    im = ImageOps.exif_transpose(Image.open(R + src)).convert('RGB')
    W, H = im.size
    im = im.crop((int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)))
    if max(im.size) > 2400: im.thumbnail((2400, 2400), Image.LANCZOS)
    im.save('assets/mg/' + out, quality=92)
    print(f'{out:<36} <- {src:<36} {im.size[0]}x{im.size[1]}{tag}')
