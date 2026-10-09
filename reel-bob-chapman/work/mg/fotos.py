"""POR VIDEO — reel BOB CHAPMAN. Prepara as fotos da camada: work/pesq/loc/<arquivo> -> assets/mg/<papel>.jpg
(recorte em fracao da imagem, tirando a borda do negativo/cromo e as marcacoes do filme). A capa (gerada a pedido no Codex,
work/capa/capa.png) e a unica imagem gerada. Fotos: Library of Congress, Prints & Photographs Division (FSA/OWI e Matson),
dominio publico — LICENCAS-FOTOS.txt. Nada que identifique o Bob antes de "Bob" (o nome; nao ha retrato livre dele).
uso: python3 work/mg/fotos.py"""
import os
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
R = 'work/pesq/loc/'
# papel -> (arquivo, recorte (x0, y0, x1, y1) em fracao)
FOTOS = {
    'capa.jpg': ('../../capa/capa.png', (0, 0, 1, 1)),
    'capa-crachas.jpg': ('../../capa/capa.png', (0.05, 0.0, 0.83, 0.62)),     # detalhe: a parede de cracha, todos no lugar
    'furadeira.jpg': ('pre_fsac-1a35306.jpg', (0.035, 0.04, 0.965, 0.965)),   # North American Aviation, 1942 (Palmer)
    'torno-moca.jpg': ('pre_fsac-1a34951.jpg', (0.03, 0.03, 0.975, 0.955)),   # Consolidated Aircraft, 1942 (Palmer)
    'torno-rapaz.jpg': ('pre_fsac-1a35308.jpg', (0.02, 0.03, 0.96, 0.955)),   # North American Aviation, 1942 (Palmer)
    'beulah.jpg': ('pre_fsac-1a34938.jpg', (0.03, 0.03, 0.975, 0.95)),        # Beulah Faith, 20, Consolidated, 1942 (Palmer)
    'curso.jpg': ('treino_fsa-8c28613.jpg', (0.06, 0.05, 0.985, 0.965)),      # Detroit, 1942: jovens ouvindo os palestrantes
    'curso2.jpg': ('treino_fsa-8c28602.jpg', (0.03, 0.06, 0.985, 0.96)),
    'altar.jpg': ('pai_matpc-18885.jpg', (0.085, 0.07, 0.93, 0.955)),         # 1938: a noiva entra escoltada pelo pai
    'volta-casa.jpg': ('casa_fsa-8c04489.jpg', (0.03, 0.08, 0.93, 0.95)),     # Midland, PA, 1940: indo pra casa depois da usina
    'jantar-casal.jpg': ('casa_fsa-8c02378.jpg', (0.03, 0.04, 0.975, 0.93)),  # Shenandoah, PA, 1938: o mineiro e a mulher no jantar
    'filhos.jpg': ('casa_fsa-8b22682.jpg', (0.05, 0.06, 0.98, 0.96)),         # Seminole, OK, 1939: os filhos no jantar
    'familia.jpg': ('fam_fsa-8b20145.jpg', (0.03, 0.04, 0.92, 0.93)),         # 1937: uma familia inteira
    'diretoria.jpg': ('dir_fsa-8d25355.jpg', (0.15, 0.06, 0.96, 0.95)),       # Detroit, 1941: executivos na sala da diretoria
}
os.makedirs('assets/mg', exist_ok=True)
for out, (src, box) in FOTOS.items():
    im = ImageOps.exif_transpose(Image.open(R + src)).convert('RGB')
    W, H = im.size
    im = im.crop((int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)))
    if max(im.size) > 2400: im.thumbnail((2400, 2400), Image.LANCZOS)
    im.save('assets/mg/' + out, quality=92)
    print(f'{out:<22} <- {src:<26} {im.size[0]}x{im.size[1]}')
