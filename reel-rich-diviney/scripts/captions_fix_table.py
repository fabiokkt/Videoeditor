"""POR VIDEO — reel RICH DIVINEY. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Sem roteiro escrito: o texto segue o AUDIO, com a grafia do formato ("pra"). Correcoes: "CEOs"/"CIUS" -> SEALs (o audio diz
"SEALs", confirmado pelo passe large-v3); "so" de "So os melhores" caiu no take anterior (ch02) e vai para o ch03;
ch12: "merda" -> M**** (bipe de censura na palavra inteira, scripts/bipe.py), entrando junto com o bipe."""
DROP=None
FIX={
 1:{6:"pra"},
 2:{8:"dos",9:"SEALs.",10:DROP},
 3:{0:"Só os",2:"SEALs"},
 4:{0:"E",5:"pra",12:"currículo."},
 5:{5:"pra",6:"ensinar.",7:"Pra",13:"pede",15:"pergunta:"},
 6:{1:"pra"},
 7:{0:"Paciência",2:"dá.",3:"Ele",12:"pra",13:"ensinar."},
 10:{0:"pergunta"},
 12:{2:"M****."},
 17:{2:"cadeira."},
 23:{8:"dos",9:"SEALs",10:"pro",11:DROP},
 30:{5:"currículo,",7:"segue,",8:"porque",11:"demais."},
}
FIXT={12:{2:60.255}}  # legenda M**** entra junto com o bipe (60,255 s do source)
