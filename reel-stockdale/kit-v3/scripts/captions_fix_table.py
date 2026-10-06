"""POR VIDEO — reel JAMES STOCKDALE. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Sem roteiro escrito neste reel: vale o audio; grafia do formato para numeros ("cinco", "sete e meio") e nomes ("Jim").
Chunks do passe por REGIAO (chunks_from_regions.py). ch11: "porra" -> P**** (bipe de censura na palavra inteira, scripts/bipe.py,
51,72-52,07 s do source)."""
DROP=None
FIX={
 3:{0:"Jim"},
 4:{5:"cinco"},
 5:{2:"sete e meio."},
 11:{8:"P****"},
 15:{6:"gafanhoto,"},
 16:{0:"É",1:"medo."},
 18:{0:"nunca",5:"final."},
 22:{0:"Perguntaram",5:"respondeu:",7:"otimistas."},
 24:{0:"O",13:"passava."},
 25:{0:"E"},
}
FIXT={11:{8:51.72}}  # legenda P**** entra junto com o bipe
