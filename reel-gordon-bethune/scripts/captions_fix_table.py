"""POR VIDEO — reel GORDON BETHUNE. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Roteiro do ClickUp (Cronograma > "Gordon Bethune", FINAL 07/10/2026): vale a grafia do roteiro ("pra", "pro", "tá", "boca-suja", pontuacao).
Homofonos (o whisper escreve, o roteiro manda): "amado dos" -> "amados dos" · "Queimo manual" -> "queima o manual" · "Se o atendente" -> "Seu atendente".
Onde o AUDIO diz outra coisa (passe por regiao + whisper em recorte concordam, conferido no espectro), vale o audio:
  ch05 "parar de pagar seu time" (roteiro: "pagar O seu time") · ch26 "SETENTA E CINCO dolares" (roteiro: "sessenta e cinco"; o fato e US$ 65:
  nos dois takes ha oclusao de /t/ e nenhum /s/ entre o "se" e o "enta", 108,11-108,25 e 113,46-113,58 s) · ch29 "Seu time JA FEZ besteira"
  (roteiro: "so faz") · ch32 "paga PRO seu time fazer besteira" (roteiro: "paga o seu time pra fazer") · ch34 "E COMENTA aqui embaixo"
  (roteiro: "E me conta aqui embaixo:"; a ordem /k/ -> /m/ -> /t/ no espectro, 136,51 / 136,59 / 136,79 s, e de "comenta").
ch10: "porra" -> P**** (bipe de censura na palavra inteira, scripts/bipe.py, 53,95-54,42 s do source)."""
DROP=None
FIX={
 0:{7:"boca-suja",8:DROP,11:"amados"},
 1:{6:"pra"},
 3:{0:"Gordon"},
 4:{0:"pegou",12:"vezes.",13:"E"},
 5:{5:"pra",12:"pra"},
 6:{5:"pro",6:DROP},
 8:{0:"Paga",5:"fechada?"},
 9:{4:"pra"},
 10:{2:"P****"},
 12:{0:"todo"},
 14:{12:"custo?"},
 15:{0:"Vão"},
 16:{1:"terceiro,"},
 17:{0:"queima o",1:"manual."},
 18:{9:"pro",10:DROP,13:"pra",14:DROP},
 19:{3:"tá"},
 20:{0:"Seu",1:DROP,4:"“é",7:"empresa”?"},
 22:{5:"ar-condicionado.",6:DROP},
 23:{4:"pra"},
 25:{0:"O",5:"atrasado."},
 26:{5:"setenta e cinco",7:"pra",9:"mundo,"},
 30:{4:"tá"},
 32:{1:"pro",2:DROP,6:"besteira,"},
 33:{0:"me"},
 34:{3:"embaixo:",14:"viu?"},
}
FIXT={10:{2:53.95}}  # legenda P**** entra junto com o bipe
