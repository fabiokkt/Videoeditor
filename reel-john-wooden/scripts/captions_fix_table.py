"""POR VIDEO — reel JOHN WOODEN. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Roteiro do ClickUp (Cronograma > "John Wooden", v1): vale a grafia do roteiro ("pra", "pro", "dez", "doze", "ta", "Bill", "por que");
onde o AUDIO diz outra coisa (passe por regiao + whisper em recorte, com e sem o roteiro no --prompt, concordam), vale o audio:
  ch03 "a calcar A meia" (roteiro: "a calcar meia") · ch06 "o atraso e desrespeito com TODO O time" (roteiro: "atraso e desrespeito com o
  tempo do time") · ch20 "voltou DE ferias" (roteiro: "das ferias").
  ch02/ch03: o "e" de "e, no primeiro treino" caiu no take anterior no passe por regiao (recorte de 28,98 s: "E no primeiro treino") -> DROP no ch02
  e "e, no" no ch03.
  Nao gravado: o CTA do meio "Comenta ESTRELA que eu te mando o protocolo completo no direct." (sem callout de ESTRELA).
ch18: "porra" -> P**** (bipe de censura na palavra inteira, scripts/bipe.py, 108,86-109,23 s do source)."""
DROP=None
FIX={
 1:{6:"pra",13:"pro",14:DROP,20:"pra"},
 2:{2:"dez",5:"doze",7:DROP},
 3:{0:"e, no",2:"treino,"},
 4:{5:"pra"},
 5:{3:"atrasado.",4:"Nem"},
 7:{5:"dez",8:"muito?"},
 10:{8:"pro",9:DROP,14:"bola."},
 13:{3:"gafanhoto."},
 14:{6:"colega."},
 15:{0:"Ele"},
 17:{2:"tá",9:"amiguinho."},
 18:{3:"P****"},
 21:{2:"proibida."},
 22:{0:"Ele",5:"dele."},
 25:{0:"Acredito.",8:"acredita."},
 26:{0:"E"},
 29:{1:"por que"},
 30:{14:"demais."},
}
FIXT={18:{2:108.69,3:108.86}}  # legenda P**** entra junto com o bipe
