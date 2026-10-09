"""POR VIDEO — reel MICHAEL GERBER. Tabela de correcoes de legenda por chunk (indice = posicao da palavra no chunk,
ignorando entradas vazias), usada por fix_captions.py (texto) e por align.py (palavras DROP ficam fora do encaixe).
Roteiro do ClickUp (Cronograma > "Michael Gerber", v2 06/10/2026, secao "Roteiro (v2)"): vale a grafia do roteiro ("pra", "ta", pontuacao, CADEIRA).
Homofonos / fala ligada (o whisper escreve, o roteiro manda): "desenhe o" -> "desenha o" · "Montar a" -> "monta a" · "Tudo o que" -> "Tudo que" ·
"te mando teste" -> "te mando o teste" (o recorte ouviu "o teste") · "esta em seis" -> "ta em seis" (sem /s/ no espectro, 48,86-49,30) ·
"estava" -> "tava" (nenhum /s/ entre "ele" e "tava", 25,36-25,80).
Onde o AUDIO diz outra coisa (passe por regiao + whisper em recorte concordam; conferido no espectro), vale o audio:
  ch02 "TEM um emprego." (roteiro: "Voce tem um emprego.") · ch04 "a gente ta QUEBRANDO" (roteiro: "quebrado"; murmurio nasal /n/ 21,10-21,16 s)
  · ch05 "E ele tava" (roteiro: "Ele tava") · ch15 "escreve passo a passo" (roteiro: "o passo a passo") · ch16 "Ele DISSE que" (roteiro: "diz")
  · ch27 "ela falou: odeio fazer torta" (roteiro: "eu odeio").
ch12: "porra" -> P**** (bipe de censura na palavra inteira, scripts/bipe.py, 53,03-53,49 s do source)."""
DROP=None
FIX={
 1:{6:"pra"},
 2:{0:"Tem",2:"emprego."},
 4:{3:"avisar:",7:"quebrando."},
 5:{2:"tava",6:"pra"},
 6:{5:"pra"},
 7:{1:"desenha"},
 8:{1:"cadeira:",2:"vendas,"},
 10:{2:"tá",5:"cadeiras?"},
 11:{0:"Você",6:"querido."},
 12:{0:"Você",3:"P****"},
 14:{0:"monta",7:"franquia."},
 15:{1:DROP,10:"passo."},
 17:{0:"Se",4:"você,",6:"gafanhoto,",9:"funciona."},
 18:{0:"E",1:"terceiro,",7:"cadeira."},
 19:{7:"entrega,"},
 21:{0:"primeiro"},
 22:{5:"sobrinho."},
 23:{0:"Depois"},
 24:{1:"CADEIRA",6:"o teste",7:"pra"},
 27:{10:"falou:",13:"torta."},
 28:{0:"Não",4:"cheiro."},
 29:{0:"Ela",4:"empresa."},
 30:{0:"Abriu"},
 33:{13:"você",14:"é",15:"demais."},
}
FIXT={12:{3:53.03}}  # legenda P**** entra junto com o bipe
