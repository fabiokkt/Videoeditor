"""POR VIDEO — reel DEMING. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Grafia do roteiro onde o whisper erra so grafia/pontuacao ("pras", "pra", numeros por extenso, "Seu melhor", "que ensinou").
Vale o audio onde ele diz outra coisa: "dar aulas", "esconde O cliente", "vermelhO era O defeito" (roteiro: "Vermelha era defeito").
ch08: "porra" -> P**** (bipe de censura na palavra inteira, scripts/bipe.py, 51,13-51,645 s do source)."""
DROP=None
FIX={
 2:{4:"pras",5:DROP},
 3:{3:"imperador,",4:DROP},
 4:{0:"e até"},
 5:{5:"pra"},
 6:{0:"Primeiro,",1:"troca",2:"o",3:"culpado."},
 7:{2:"três"},
 8:{6:"P****."},
 9:{2:"que",4:"cem",6:"noventa e quatro"},
 13:{0:"Seu",1:DROP},
 14:{3:"que"},
 16:{0:"Aquele",1:"“Aqui",8:"vez.”"},
 18:{6:"almoço,",8:"gafanhoto."},
 21:{6:"pá."},
 22:{0:"Vermelho",3:"defeito."},
 23:{3:"chefe:"},
 24:{0:"Depois,"},
 25:{0:"E",4:"diminuía."},
 27:{5:"amigo?"},
 28:{0:"Olha",2:"caixa."},
 29:{8:"continua,",9:"me",10:"segue,",11:"porque"},
}
FIXT={8:{6:51.13}}  # legenda P**** entra junto com o bipe
