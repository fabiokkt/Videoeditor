"""POR VIDEO — reel HYMAN RICKOVER. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Roteiro do ClickUp (Cronograma > "Hyman Rickover", v2 curto): vale a grafia do roteiro ("Hyman", "serrava", "pra", "pro",
"oitenta e dois", "noventa e nove por cento"); onde o AUDIO diz outra coisa (passe por regiao + whisper em recorte, com e sem o
roteiro no --prompt, concordam), vale o audio:
  ch01 "que seu time" (sem "o") · ch07 "ELE nunca foi de ninguem" (roteiro: "ela") · ch10 "ele diz que o chefe que nao liga" (roteiro:
  "que se o chefe nao liga") · ch24 "virou O presidente".
  ch05: o whisper engoliu o "Primeiro," (30,16-30,55 s, confirmado em recorte) e juntou com "Toda".
  ch25 "deu o melhor": o "o" funde com o "deu" (elisao) — mantida a grafia do roteiro.
  Nao gravado: o CTA do meio "Comenta ALMIRANTE..." (sem callout de ALMIRANTE).
ch17: "porra" -> P**** (bipe de censura na palavra inteira, scripts/bipe.py, 80,30-80,80 s do source)."""
DROP=None
FIX={
 1:{6:"pra"},
 2:{0:"Hyman",1:"serrava",4:"pro",5:DROP,9:"entrevista."},
 3:{0:"E",7:"demitido.",8:"Aos",9:"oitenta e dois"},
 4:{5:"pra"},
 5:{0:"Primeiro,",1:"toda tarefa",4:"nome.",5:"Não",6:"é"},
 6:{0:"o",5:"pessoal.",6:"É"},
 10:{0:"cuida",2:"detalhe.",3:"Ele",11:"pro",12:DROP},
 11:{2:"noventa e nove por cento"},
 12:{10:"amanhã,",12:"gafanhoto."},
 13:{1:"terceiro,"},
 14:{0:"para"},
 15:{6:"pra"},
 17:{10:"P****!"},
 18:{5:"entrevista."},
 19:{0:"Um",3:"contou,",5:"orgulhoso,"},
 20:{0:"Hyman",1:"perguntou:"},
 21:{3:"seco:"},
 22:{5:"perguntou:"},
 25:{2:"deu o"},
 27:{13:"demais."},
}
FIXT={17:{10:80.30},  # legenda P**** entra junto com o bipe
      5:{1:30.91,2:31.57,3:31.82,4:31.99}}  # ch05: tempos do whisper em recorte (30,7-33,2 s; o passe por regiao adiantou "toda tarefa")
