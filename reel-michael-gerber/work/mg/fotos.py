"""POR VIDEO — reel MICHAEL GERBER. Prepara as fotos da camada: work/pesq/raw/<arquivo> -> assets/mg/<papel>.jpg
(recorte em fracao da imagem; tira a borda do negativo e o codigo de borda das fotos da Library of Congress). A capa (gerada a pedido
no Codex) sai de work/capa/capa.png. Nada que identifique o Michael antes de "Michael": a pre-revelacao usa so a capa, a dona do
armazem (NARA, 1973) e o relogio de ponto (British Library).
uso: python3 work/mg/fotos.py"""
import os
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
R = 'work/pesq/raw/'
# papel -> ([candidatos em ordem], recorte (x0, y0, x1, y1) em fracao, substituta)
FOTOS = {
    'capa.jpg': (['../../capa/capa.png'], (0, 0, 1, 1), None),
    'capa-perto.jpg': (['../../capa/capa.png'], (0.16, 0.0, 0.84, 0.72), None),           # a mulher e o forno, mais perto
    'dona-armazem.jpg': (['fl_grocery.jpg'], (0, 0, 1, 1), None),                         # NARA/DOCUMERICA 1973: dona do armazem em Leakey, Texas
    'relogio-ponto.jpg': (['fl_clock.jpg'], (0, 0, 1, 1), None),                          # British Library: relogio de ponto de fabrica
    'gerber.jpg': (['fl_gerber_mic_k.jpg', 'fl_gerber_mic.jpg'], (0, 0, 1, 1), None),     # Infusionsoft 2009 (CC BY-SA 2.0)
    'gerber-2.jpg': (['fl_gerber_ouve_k.jpg', 'fl_gerber_ouve.jpg'], (0, 0, 1, 1), None),  # Infusionsoft 2009 (CC BY-SA 2.0): ele na reuniao
    'moca-torta.jpg': (['loc_hec26939.jpg'], (0.05, 0.04, 0.985, 0.97), None),            # Harris & Ewing (LOC): moca de touca com uma torta
    'mesa-tortas.jpg': (['loc_8b23573.jpg'], (0.04, 0.03, 0.975, 0.90), None),            # FSA 1939, padaria de San Angelo: massa nas formas
    'mesa-tortas-v.jpg': (['loc_8b23598.jpg'], (0.03, 0.055, 0.92, 0.985), None),         # idem, vertical: a mesa cheia de formas
    'forno.jpg': (['loc_8b23597.jpg'], (0.01, 0.02, 0.94, 0.92), None),                   # idem: formas entrando no forno
    'carrinho.jpg': (['loc_8b23584.jpg'], (0.04, 0.07, 0.99, 0.97), None),                # idem: o carrinho cheio na frente do forno
}
os.makedirs('assets/mg', exist_ok=True)
for out, (cands, box, sub) in FOTOS.items():
    src = next((c for c in cands if os.path.exists(R + c)), None); tag = ''
    if src is None:
        src = sub; box = (0, 0, 1, 1); tag = '  << SUBSTITUTA'
    im = ImageOps.exif_transpose(Image.open(R + src)).convert('RGB')
    W, H = im.size
    im = im.crop((int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)))
    if max(im.size) > 2400: im.thumbnail((2400, 2400), Image.LANCZOS)
    im.save('assets/mg/' + out, quality=92)
    print(f'{out:<22} <- {src:<24} {im.size[0]}x{im.size[1]}{tag}')
