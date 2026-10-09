# POR VIDEO (molde, reel Michael Gerber): troque a lista S pelo roteiro do reel novo. uso: python3 work/mg/teste/fake_tl.py (SOBRESCREVE work/tl-words.txt: so antes da fase 2!)
# Timeline PROVISORIA (so para testar a camada antes do bruto): o roteiro a ~2,9 palavras/s, 0,35 s entre takes.
S=[("GANCHO","Esse cara é um dos donos mais atrapalhados e mais copiados do planeta Terra."),
("PROTOCOLO-POLEMICO","E ele criou um protocolo polêmico pra provar que você não tem uma empresa."),
("EMPREGO","Você tem um emprego."),
("MICHAEL","Michael ensinava dono a não quebrar."),
("SOCIO-QUEBRADO","Até o sócio avisar: a gente tá quebrado."),
("OCUPADO","Ele tava ocupado demais trabalhando pra olhar o dinheiro."),
("PROTOCOLO-EXPLORADO","E esse é o protocolo pra você parar de ser o funcionário mais explorado da sua empresa."),
("P1-ORGANOGRAMA","Primeiro, desenha o organograma. Cada cadeira: vendas, financeiro, compras, entrega."),
("P1-NOME","Ele manda escrever o seu nome em cada cadeira que é sua."),
("P1-SEIS-CADEIRAS","Seu nome tá em seis cadeiras?"),
("P1-DONO","Você não é o dono, meu querido."),
("P1-BIPE","Você é a P**** do organograma."),
("P2-FRANQUIA","Segundo, monta a empresa como se fosse vender franquia."),
("P2-PASSO","Tudo que você faz de cabeça, escreve o passo a passo."),
("P2-GENTE-COMUM","Ele diz que ela tem que funcionar com gente comum, não com gênio."),
("P2-GAFANHOTO","Se só funciona com você, pequeno gafanhoto, ela não funciona."),
("P3-CONTRATO","E terceiro, assina o contrato de cada cadeira."),
("P3-FOLHA","Escreve numa folha o que aquela cadeira entrega, e você assina como se fosse funcionário."),
("P3-ORDEM","Ele diz: primeiro a cadeira, depois a pessoa."),
("P3-SOBRINHO","Na sua, primeiro veio o sobrinho."),
("P3-INVENTARAM","Depois inventaram a cadeira."),
("CTA-COMENTA","Comenta CADEIRA que eu te mando o teste pra descobrir quantas cadeiras são suas."),
("VIRADA-TORTA","E a virada foi uma loja de torta."),
("VIRADA-SARAH","Sarah aprendeu a fazer torta com a tia e abriu a própria loja."),
("VIRADA-TRES","Três anos depois, com a loja cheirando a torta, ela falou: eu odeio fazer torta."),
("VIRADA-CHEIRO","Não aguento nem o cheiro."),
("CLIMAX-EMPREGO","Ela não abriu uma empresa. Abriu um emprego."),
("FECHO-SEGUNDA","Você abriu pra fazer o que amava e hoje odeia segunda-feira, meu amigo?"),
("FECHO-LOJA","Loja de torta."),
("CTA-SEGUE","Se você é o funcionário mais explorado da sua empresa, me segue, porque você é demais.")]
t=0.0; out=[]
for i,(lab,txt) in enumerate(S):
    ws=txt.split(); t0=t; parts=[]
    for w in ws: parts.append(f"{w}@{t+0.05:.2f}"); t+=1/2.9
    t1=t+0.35; out.append(f"{i:2d} {lab:<22} {t0:5.2f}- {t1:5.2f} ({t1-t0:.2f})  "+' '.join(parts)); t=t1
open('work/tl-words.txt','w').write('\n'.join(out)+'\n'); print('total',round(t,2))
