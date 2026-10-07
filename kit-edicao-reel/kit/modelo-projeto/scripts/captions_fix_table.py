"""POR VIDEO — reel KAZUO INAMORI. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Regra do formato: onde o whisper erra so GRAFIA/PONTUACAO, vale a grafia do roteiro ("pra", "pro", "setenta e oito", "um bilhao", "MONGE");
onde o AUDIO diz outra coisa (passe por regiao, passe por chunk e passe com --prompt do roteiro concordam), vale o audio:
"virou UM monge budista" (roteiro: "virou monge"), "sem olhar numero" (roteiro: "o numero"), "uma reuniao COM O diretor QUE ia gastar"
(roteiro: "uma reuniao. Um diretor ia gastar"), "pra voce nao confio" (roteiro: "eu nao confio"), "ja ESTA aprovado" (roteiro: "ja ta").
Todos os chunks foram reconstruidos do passe por REGIAO (rebuild_chunk.py: o passe por chunk vazava/alucinava nas bordas — "Caso",
"monstro", "Sensacional!", "equilibrio", "importancia"), menos o ch28, que fica com o passe por chunk (o por regiao punha o "com" no take anterior).
Copia do passe por chunk cru: work/chunks-raw/. ch24: "merda" -> M**** (bipe de censura na palavra inteira, scripts/bipe.py)."""
DROP=None
FIX={
 2:{0:"pra"},
 4:{4:"e,",6:"setenta e oito",7:"anos,",12:"falida."},
 5:{0:"Sem"},
 6:{5:"pra",14:"pro",15:DROP},
 8:{0:"quebra"},
 9:{5:"empresinha,"},
 14:{0:"mostra",5:"equipe,"},
 17:{1:"diz"},
 19:{4:"gafanhoto."},
 22:{0:"Ele",4:"plano,"},
 23:{0:"porque"},
 24:{1:DROP,11:"M****?"},
 26:{1:"MONGE"},
 27:{6:DROP},
 28:{6:"um",10:DROP,11:DROP},
 29:{1:"cortou:"},
 30:{0:"“Pra",6:"centavo.”"},
 31:{1:"diretor:"},
 32:{0:"“Mas",6:"orçamento.”"},
 33:{1:"explodiu:"},
 34:{0:"“De"},
 36:{9:"chão.”"},
 39:{1:"escondido."},
 40:{0:"Se",7:"pro",8:DROP,14:"segue,",17:"é",18:"demais."},
}
FIXT={24:{11:75.905}}  # legenda M**** entra junto com o bipe (75,905 s do source)
