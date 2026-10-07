"""POR VIDEO — reel ERNEST SHACKLETON. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Roteiro do ClickUp (Cronograma > "Ernest Shackleton", v1 de 04/10/2026): vale a grafia do roteiro ("pra", "tá", pontuacao); onde o AUDIO
diz outra coisa (passe por regiao + whisper em recorte, com e sem o roteiro no --prompt, concordam), vale o audio:
  ch01 "o funcionario que reclama" (roteiro: "que MAIS reclama") · ch02 "preso no gelo NA Antartida" (roteiro: "da") ·
  ch16 "e ate O futebol no gelo" (roteiro: "e ate futebol").
  ch08: o passe por regiao ouviu "reclamam ... junto a torcida": e "reclamao ... junta torcida" (roteiro; o "a" sai).
  Nao gravado: o CTA do meio "Comenta GELO que eu te mando o protocolo completo no direct." (sem callout COMENTA GELO).
ch17: "merda" -> M**** (bipe de censura na palavra inteira, scripts/bipe.py, 87,85-88,32 s do source)."""
DROP=None
FIX={
 1:{15:"afasta.",16:"Você"},
 3:{2:"pra"},
 5:{5:"pra"},
 6:{0:"Primeiro,",1:"põe"},
 7:{8:"pra"},
 8:{3:"reclamão",7:"junta",8:DROP},
 9:{5:"empresa"},
 10:{3:"primeiro."},
 11:{8:"gelo."},
 12:{7:"ele:",8:"as",11:"ouro."},
 17:{4:"semana",6:"M****"},
 19:{2:"afundou,",15:"bote:"},
 20:{5:"mim."},
 21:{4:"pra",8:"avisou:"},
 22:{0:"Acabou",2:"motim."},
 23:{3:"rebeldia."},
 26:{13:"demais."},
}
FIXT={17:{6:87.85}}  # legenda M**** entra junto com o bipe
