"""POR VIDEO — reel MATTHEW RIDGWAY. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Roteiro do ClickUp (Cronograma > "Matthew Ridgway", v1 curto): vale a grafia do roteiro ("paizões", "pra", "pro", "tá", "três", "cinco mil",
pontuação); onde o AUDIO diz outra coisa (passe por regiao + whisper em recorte, com e sem o roteiro no --prompt, concordam), vale o audio:
  ch11 "rodou tres dias NA linha de frente" (roteiro: "a linha") · ch18 "E voce nao sabe..." (com "E") · ch20 "mostrou pra ele UM plano de recuar"
  (roteiro: "o plano") · ch21 "Ele perguntou: o plano de ataque?" (sem o "e"; 3 passes) · ch24 "o exercito que fugia" (sem "mesmo").
  Os passes discordam (vale o roteiro): ch06 "Ele DIZ que teve que arrancar" (sem prompt "disse") · ch12 "passando O MESMO frio" (sem prompt "mesmo o").
  ch04: o passe por regiao fundiu "Primeiro," com "Resolve" (whisper em recorte 34,75-37,60: Primeiro 35,16 · resolve 36,03 · a 36,93 · luva 37,04).
  Nao gravado: o CTA "E comenta GENERAL que eu te mando o PDF." (sem callout de GENERAL).
ch09: "porra" -> P**** (bipe de censura na palavra inteira, scripts/bipe.py, 64,03-64,53 s do source)."""
DROP=None
FIX={
 0:{10:"paizões"},
 1:{6:"pra",13:"tá",14:"desmotivado.",15:"Tá"},
 2:{10:"parede,",13:"pro",14:DROP,16:"inimigo,"},
 3:{5:"pra",12:"pro",13:DROP},
 4:{0:"Primeiro,",1:"resolve a",2:"luva."},
 5:{4:"mais."},
 6:{0:"Ele",1:"diz",5:"arrancar:"},
 7:{6:"pra",8:"pra"},
 8:{0:"Resolveu",5:"atacar."},
 9:{6:"presta,",11:"P****",16:"querido."},
 11:{0:"Ele",2:"três",10:"aberto,",12:"neve."},
 12:{10:"o",11:"mesmo"},
 13:{12:"chefe.",13:"É"},
 15:{3:"cinco",7:"cara,"},
 16:{7:"bom",8:"trabalho."},
 19:{5:"pergunta."},
 20:{3:"pra"},
 21:{2:"o",5:"ataque?"},
 22:{2:"gaguejou:",3:"senhor,"},
 25:{4:"pra"},
 27:{6:"pro",7:DROP},
}
FIXT={9:{11:64.03},  # legenda P**** entra junto com o bipe
      4:{0:35.16,1:36.03,2:37.04}}  # ch04: tempos do whisper em recorte (o passe por regiao fundiu "Primeiro," com "Resolve")
