"""POR VIDEO — reel STANLEY McCHRYSTAL. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Roteiro do ClickUp (Cronograma > "Stanley McChrystal", v1): vale a grafia do roteiro ("pra", "pro", "tá", numeros por extenso:
"quatro", "sete mil", "dezoito", "trezentas"; pontuacao); onde o AUDIO diz outra coisa (passe por regiao e passe por chunk sem prompt
concordam; com o roteiro no --prompt o whisper alucinou em 3 de 6 chunks), vale o audio:
  ch01 "pra provar que SEU comercial e SUA operacao" (roteiro: "o seu ... a sua") · ch05 "parar de ser JUIZ" (roteiro: "o juiz") ·
  ch09 "Reuniao de vendas sem OPERACAO" (roteiro: "sem a operacao").
  Os passes discordam ou o whisper troca homofono (vale o roteiro): ch13 "SEU melhor vendedor" (whisper "Se o") · ch14 "Nao O encostado"
  (regiao "Nao encostado", chunk "Nao um encostado") · ch21 "Ele juntou soldado e analista" (regiao "juntou o soldado", chunk sem o "o").
  Nao gravado: o CTA do meio e o do fim ("Comenta BRIGA que eu te mando o protocolo completo no direct.") — sem callout de BRIGA.
ch17: "porra" -> P**** (bipe de censura na palavra inteira, scripts/bipe.py, 118,44-118,77 s do source)."""
DROP=None
FIX={
 1:{6:"pra"},
 3:{3:"forças",4:"especiais",5:"americanas"},
 4:{0:"dormia",1:"quatro"},
 5:{5:"pra"},
 6:{0:"Primeiro,",5:"reunião."},
 7:{0:"Ele",8:"sete",10:"pessoas."},
 8:{4:"excelente,",6:"separado,",7:"perde."},
 11:{0:"Ele"},
 13:{0:"Seu",1:DROP},
 14:{0:"Não o"},
 16:{9:"tudo,"},
 17:{11:"P****"},
 18:{0:"E",5:"quartinho."},
 19:{7:"pra"},
 20:{0:"Ia"},
 21:{2:DROP,5:"analista,",11:"dezoito",14:"pra",17:"trezentas."},
 23:{0:"Ou"},
 24:{14:"demais."},
}
FIXT={17:{11:118.44}}  # legenda P**** entra junto com o bipe
