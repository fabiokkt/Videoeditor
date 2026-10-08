"""POR VIDEO — reel GENE KRANZ. Prepara as fotos da camada: work/pesq/nasa/<id>.jpg (NASA Image and Video Library,
dominio publico) -> assets/mg/<papel>.jpg (recorte em fracao da imagem). A capa e gerada a pedido (Codex).
uso: python3 work/mg/fotos.py"""
import os
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
R = 'work/pesq/nasa/'
# papel -> (arquivo, recorte (x0, y0, x1, y1) em fracao)
FOTOS = {
    'capa-gene-kranz.jpg': ('../../capa/capa.png', (0, 0, 1, 1)),                    # gerada a pedido (Codex)
    'sala-gemini-1965.jpg': ('s65-30410.jpg', (0, 0, 1, 0.78)),                       # a sala de controle de Houston, Gemini 4, jun 1965 (sem a bolsa com o logo, embaixo)
    'time-apollo13-console-1970.jpg': ('S70-35014.jpg', (0, 0, 1, 1)),               # controladores em volta do console do Lunney — Apollo 13, 15 abr 1970
    'time-apollo13-monitor-1970.jpg': ('s70-34986.jpg', (0, 0, 1, 1)),               # astronautas e controladores no console — Apollo 13, 14 abr 1970
    'kranz-colete-1972.jpg': ('s72-35188.jpg', (0, 0, 1, 1)),                        # Kranz de colete branco no console — Apollo 16, 16 abr 1972
    'sala-apollo11-1969.jpg': ('S69-40301.jpg', (0, 0, 1, 1)),                       # a sala de controle no fim da Apollo 11, 24 jul 1969
    'aldrin-lua-1969.jpg': ('as11-40-5902.jpg', (0, 0, 1, 1)),                       # Aldrin na Lua, 20 jul 1969
    'nave-012-fabrica-1967.jpg': ('S67-15704.jpg', (0, 0, 1, 1)),                    # a nave 012 (Apollo 1) na montagem, 3 jan 1967
    'nave-012-pad34-1967.jpg': ('S67-17042.jpg', (0, 0, 1, 1)),                      # a nave 012 icada no Pad 34, jan 1967
    'kranz-console-1965.jpg': ('s65-22203.jpg', (0, 0, 1, 1)),                       # Kranz no console de diretor de voo — Gemini 4 (simulacao), abr 1965
    'crise-apollo13-1970.jpg': ('S70-35369.jpg', (0, 0, 1, 1)),                      # discussao na sala no ultimo dia da Apollo 13, 16 abr 1970
    'kranz-imprensa-1966.jpg': ('S66-32629.jpg', (0, 0, 1, 1)),                      # Kranz (3o da esq.) na mesa de imprensa, 1966
    'tripulacao-apollo1-1966.jpg': ('S66-30236.jpg', (0, 0, 1, 1)),                  # White, Grissom e Chaffee (Apollo 1), 1966
    'modulo-servico-apollo13-1970.jpg': ('7010516.jpg', (0, 0, 1, 1)),               # o modulo de servico da Apollo 13 sem o painel (tanque de O2), 17 abr 1970
    'sala-apollo13-kranz-costas-1970.jpg': ('S70-35139.jpg', (0, 0, 1, 1)),          # Kranz de costas (primeiro plano) olhando o telao — Apollo 13, 13 abr 1970
    'tripulacao-apollo13-viva-1970.jpg': ('S70-35614.jpg', (0, 0, 1, 1)),            # Haise, Lovell e Swigert descem no USS Iwo Jima, 17 abr 1970
}
os.makedirs('assets/mg', exist_ok=True)
for out, (src, box) in FOTOS.items():
    im = ImageOps.exif_transpose(Image.open(R + src)).convert('RGB')
    W, H = im.size
    im = im.crop((int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)))
    if max(im.size) > 2400: im.thumbnail((2400, 2400), Image.LANCZOS)
    im.save('assets/mg/' + out, quality=92)
    print(f'{out:<40} <- {src:<22} {im.size[0]}x{im.size[1]}')
