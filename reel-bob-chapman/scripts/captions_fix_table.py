"""POR VIDEO — reel BOB CHAPMAN. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Roteiro do ClickUp (Cronograma > "Bob Chapman", v1 07/10/2026, secao "Roteiro"): vale a grafia do roteiro ("pra", "tá", numeros por
extenso, pontuacao). Conferido no audio (whisper em recorte sem prompt + espectro):
  "mais BOBOS" (o roteiro diz "bobos"; a nota de gravacao fala em "bonzinhos") — o audio diz "bobos".
  ch08 "já TÁ respondendo": o whisper escreve "está", mas nao ha /s/ entre o "já" e o "tá" (49,98-50,25 s sem sibilante) -> roteiro.
  ch28 "trata A gente" (whisper) x "trata gente" (roteiro): o "a" de "trata" e o "a" de "a gente" se fundem (homofono) -> roteiro.
Onde o AUDIO diz outra coisa, vale o audio: ch27 "E na ultima crise" (roteiro: "Na ultima crise").
ch16: "porra" -> P**** (bipe de censura na palavra inteira, scripts/bipe.py, 87,52-88,08 s do source)."""
DROP=None
FIX={
 1:{6:"pra",14:"custo."},
 2:{0:"É"},
 3:{13:"três"},
 4:{5:"pra"},
 5:{0:"Primeiro,"},
 6:{2:"verdade.",8:"três",10:"só",11:"pra",16:"escutar."},
 7:{1:"dizia:",2:"chefe",5:"escuta."},
 8:{9:"tá"},
 10:{10:"entendeu:"},
 12:{12:"amigo,"},
 13:{1:"terceiro,"},
 14:{4:"pra"},
 15:{10:"trabalho",12:"pra"},
 16:{3:"P****"},
 19:{5:"quarenta por cento."},
 20:{2:"perguntou:"},
 21:{2:"o",6:"faria?"},
 28:{3:DROP},
 29:{0:"me"},
 30:{0:"é",1:"demais."},
}
FIXT={16:{3:87.52}}  # legenda P**** entra junto com o bipe
