"""POR VIDEO — reel GENE KRANZ. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Roteiro do ClickUp (Cronograma > "Gene Kranz", v2 FINAL de 07/10/2026): vale a grafia do roteiro ("pra", "tá", pontuacao, "Gene", "Apollo");
onde o AUDIO diz outra coisa (passe por regiao + whisper em recorte SEM prompt concordam), vale o audio:
  ch11 "e pelo que VOCE deixa de fazer" (roteiro: "e pelo que deixa de fazer") ·
  ch26 "Seu time ta vendo alguma coisa, meu amigo." (roteiro: "...alguma coisa AGORA, meu amigo." — nem com o roteiro no --prompt o whisper ouve "agora").
  Homofonos -> roteiro: ch03 "em toda (a) missao" · ch08 "promete (e) entrega pra sexta" (whisper: "para a cesta") · ch27 "Se (o) seu time".
  ch17: o whisper ouve "juta"; o /ch/ e surdo (ver mkcut.py) -> "chuta".
ch21: "porra" -> P**** (bipe de censura na palavra inteira, scripts/bipe.py, 115,97-116,75 s do source)."""
DROP=None
FIX={
 1:{0:"E",6:"pra"},
 3:{0:"Gene",10:DROP},
 4:{11:"Lua."},
 5:{5:"pra"},
 6:{4:"desculpa."},
 7:{7:"pra"},
 8:{2:DROP,4:"pra",5:DROP,6:"sexta",10:"dá,"},
 12:{7:"nada?"},
 13:{0:"Pergunta",9:"avisou."},
 15:{1:"problema,",2:"ele",3:"falou:"},
 17:{1:"chuta"},
 19:{8:"nave,"},
 20:{3:"problema.",5:"parou."},
 21:{11:"gritou:",12:"P****,"},
 22:{3:"nossa."},
 23:{4:"Apollo"},
 27:{1:"o seu"},
}
FIXT={21:{12:115.97}}  # legenda P**** entra junto com o bipe
