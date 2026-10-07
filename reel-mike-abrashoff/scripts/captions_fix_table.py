"""POR VIDEO — reel MIKE ABRASHOFF. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Roteiro do ClickUp (Cronograma > "Mike Abrashoff", roteiro curto): vale a grafia do roteiro ("pra", "pros", "trezentos e dez",
"Marinha"); onde o AUDIO diz outra coisa (passe por regiao + whisper em recorte concordam), vale o audio:
  ch06 "E o protocolo..." (sem "esse e": o take com "esse e" tropecou em "quer parar de trabalhar") · ch10 "O primeiro nao era ser
  tratado com respeito" (roteiro: "era nao ser") · ch17 "pinta nesse navio" · ch32 "soltava um rojao".
ch11: "porra" -> P**** (bipe de censura na palavra inteira, scripts/bipe.py, 51,42-51,68 s do source)."""
DROP=None
FIX={
 0:{12:"Marinha",13:"americana."},
 1:{0:"E"},
 2:{0:"pra",10:"salário.",11:"Vai"},
 4:{7:"pra",8:DROP,9:"guerra"},
 5:{0:"Com"},
 6:{0:"E",3:"pra"},
 11:{6:"P****",10:"querido."},
 14:{1:"pros",2:DROP,3:"trezentos e dez",4:"marinheiros,"},
 15:{1:"respondeu:"},
 18:{0:"Trocaram"},
 19:{1:"Marinha",3:"copiou."},
 22:{8:"marinheiro:"},
 23:{0:"O",4:"pra",6:"ficar?"},
 24:{10:"Aí"},
 29:{1:"pensou:",5:"anos,"},
 30:{6:"pra",7:DROP},
 31:{0:"Não",6:"navio."},
 33:{12:"é"},
}
FIXT={11:{6:51.42}}  # legenda P**** entra junto com o bipe
