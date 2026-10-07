# Prompt de comando único — kit v3 (fluxo rápido, padrão atual)

```
Edita o reel do [TEMA] com o bruto [CAMINHO DO BRUTO] e este roteiro:
[ROTEIRO]

Segue o fluxo rápido do kit (~/Claude/KIT-EDICAO-REEL/docs/14-fluxo-rapido.md): formato do kit + camada de
motion graphics da skill showreel-interface, na dosagem do reel Deming v2: abertura só com fotos, no corpo foto
real como padrão e motion só onde conta a história. Comando único, sem parada: pesquisa as imagens na fonte
primária pelo navegador, gera a capa no Codex com esta cena: [CENA], monta, confere quadro a quadro e me manda o
MP4 aqui no chat.
```
Se a [CENA] não for preenchida, o Claude escolhe uma (assunto na metade de cima; a pessoa-tema de costas antes de o
nome ser dito) e avisa no resumo.

O que vem junto sem precisar escrever: último take, palavra inteira, bipe da palavra inteira, J-cut medido, olhar
coberto, marca só depois do nome, capa laranja no quadro 0, trilha + SFX do formato, SFX do motion, QC, MD5.

---

# (histórico) Prompt de comando único — kit v2

# Prompt de comando único — parada única

Copiar, preencher as lacunas, colar o roteiro e enviar. É o prompt usado desde 2026-09-29
(`reel-auto/PROMPT-COMANDO-UNICO-1-PARADA.md`), com três acertos e cinco regras permanentes do Fabio que estavam só na memória e passaram a constar no texto:

| No prompt antigo | Aqui | Motivo |
|---|---|---|
| "usando a skill edicao-reel-viral" | "usando o kit em `~/Claude/KIT-EDICAO-REEL`" | o kit é a fonte única; nenhum projeto antigo é consultado |
| "legendas amarelas dentro de uma caixa no gancho" | capa laranja | era texto do template antigo; o padrão desde o O Boticário é a caixa laranja |
| "J-cut de 5 frames com crossfade" | "J-cut com a fala entrando 5 quadros antes do corte" | o lead de fala é 5; o crossfade é 3, dentro do silêncio |

Regras acrescentadas ao texto (todas pedidas por ele em reels anteriores, ver `docs/05`): primeira cena sempre em
split · troca de cena ou efeito a cada ~4 s com transição em todo corte · bipe na palavra **inteira** · nada que
identifique a empresa antes de o áudio dizer o nome · registrar no kit, no fim, o que o reel ensinou.
**Fabio: se alguma dessas linhas não for mais o que você quer, é só tirar do prompt.**

A versão com duas paradas (B-roll e depois "APROVADO — PODE EXPORTAR") e a versão automática de agosto estão
em `legado/` e no git; não são mais usadas.

**Por que uma parada só:** correção de tempo (corte, velocidade, J-cut, palavrão) depois do render custa
~25–40 min de render inteiro; correção só visual (B-roll, texto, cor, volume) custa ~5–10 min.

---

## O PROMPT

```
Edita o vídeo [NOME_DO_ARQUIVO_BRUTO] no meu formato de reel viral, usando o kit em ~/Claude/KIT-EDICAO-REEL (README e docs) e o pipeline HyperFrames. A empresa/tema é [NOME_DA_EMPRESA].
Crie o projeto com o novo-projeto.sh do kit. Não consulte projetos antigos: o kit é a fonte única.
Faça toda a edição sem me perguntar sobre ajustes durante a montagem inicial. Siga os padrões já calibrados:
Crie um mezanino com correção de cor. O vídeo bruto pode ser HDR do iPhone ou SDR full-range: converta corretamente e não deixe as cores lavadas.
Preserve o arquivo bruto original sem alterações.
Faça a transcrição por regiões e por chunks.
Quando houver frases ou takes repetidos, mantenha sempre o ÚLTIMO take válido.
Corte os tails somente depois da palavra completa. Nunca corte uma palavra no meio.
Faça a varredura de olhar obrigatória: eu costumo olhar para o lado para ler o roteiro antes de falar e ao terminar cada take. Revise os frames e corte ou cubra todos esses desvios. Nos trechos em que eu estiver visível, quero aparecer olhando para a câmera.
Use J-cut com a fala seguinte entrando 5 quadros antes do corte de imagem, com crossfade dentro do silêncio.
Aplique velocidade de 1.1x ao vídeo.
A primeira cena é sempre a tela dividida. Use split-screen 44/56 com a transição de arrastar, em que o B-roll desce revelando o apresentador.
Gancho inteiro no primeiro quadro, como capa: caixa laranja com letras brancas em caixa alta. No restante, legendas sincronizadas brancas sem contorno.
Posicione as legendas mais abaixo quando eu estiver sozinho na tela e ajuste a posição quando houver B-roll para não cobrir informações importantes.
Adicione callouts nas frases de impacto. O primeiro callout deve usar efeito de digitação acompanhado de drum-fill.
Troque de cena ou coloque um efeito a cada ~4 segundos (cenas de 3 a 5 segundos), com transição em todo corte.
Adicione light-leaks, efeitos sonoros e a trilha do formato.
Bipe em TODO palavrão, na palavra inteira: antes da parada, varra a transcrição inteira atrás de palavrão e confira ouvindo o trecho que nenhum ficou audível.
O vídeo original do apresentador e todos os B-rolls devem ficar sem o áudio próprio. Use apenas a faixa de voz tratada, a trilha e os efeitos sonoros definidos na edição.
Organize o projeto HyperFrames de forma clara para permitir alterações posteriores em cortes, textos, legendas, B-rolls, volumes, efeitos e timings.

Mantenha os slots de B-roll do formato:
Intro em split-screen
Cutaways durante o corpo do vídeo
Segundo split-screen
Clímax emocional
Não mostre nada que identifique [NOME_DA_EMPRESA] antes de o áudio dizer o nome pela primeira vez.
Para cada slot:
Pesquise no Google Imagens fotos reais de [NOME_DA_EMPRESA] que combinem diretamente com a fala daquele trecho. Considere fábrica, produto, loja, equipe, clientes, bastidores, sede, eventos ou qualquer outro assunto adequado ao roteiro.
Priorize imagens provenientes da sala de imprensa oficial ou do site oficial da empresa. Se não houver material adequado, use resultados do Google Imagens com tamanho grande.
Para cada imagem escolhida, escreva um prompt de animação que mova somente a câmera sobre a imagem. Não redescreva a imagem. Textos, logotipos e elementos da marca devem permanecer parados, legíveis e nítidos, sem deformação, morphing ou alteração.
Salve todas as pesquisas no arquivo PESQUISAS-BROLL-[NOME_DA_EMPRESA].md, registrando por slot: trecho da fala, tipo de enquadramento, imagem recomendada, link e fonte, prompt de animação, duração necessária e nome sugerido do arquivo.

PARADA ÚNICA — TEMPO TRAVADO:
Com a montagem pronta e o arquivo de pesquisas salvo, abra o preview local do HyperFrames, me dê o link e PARE. Esta é a ÚNICA parada do fluxo.
Nessa mensagem, mostre tudo que mexe no tempo do vídeo, para eu aprovar de uma vez:
Duração total
Lista de cortes
Velocidade aplicada
J-cuts (quantidade e leads)
Palavrões encontrados e confirmação de que cada um está bipado
Resultado da varredura de olhar
Primeira cena
Lista de B-rolls planejados por slot
Não gere os B-rolls antes da minha resposta.

DEPOIS DA PARADA — DIRETO ATÉ O FINAL:
Quando eu disser "pode gerar as brolls" (com ou sem correções):
Aplique as correções pedidas.
Gere os B-rolls, encaixe nos slots e ajuste duração, enquadramento e sincronização.
Rode novamente a varredura de olhar, pois os B-rolls podem alterar os pontos de cobertura e de corte, e corrija todos os desvios.
Verifique legendas, callouts, split-screens, transições, light-leaks, trilha, voz e efeitos sonoros.
Execute a validação do projeto HyperFrames até zero erros e confira snapshots dos pontos-chave.
Em seguida RENDERIZE O VÍDEO FINAL SEM PARAR para nova revisão.
Só pare antes do render se surgir uma decisão que precise de mim (slot sem imagem aceitável, mudança de corte que não seja de olhar).

EXPORTAÇÃO FINAL:
Renderize o vídeo final completo em MP4, em resolução vertical 1440×2560, 60 fps, qualidade alta.
Inclua a voz tratada, a trilha e todos os efeitos sonoros.
Salve em renders/[NOME_DA_EMPRESA]-reel-final.mp4.
Confira se o arquivo foi criado corretamente, se tem áudio e se a duração bate com o preview.
Entregue o link do preview (o projeto continua editável) e um resumo com: nome do arquivo, duração, resolução, taxa de quadros, resultado da validação, confirmação de áudio, B-roll usado em cada slot e callouts aplicados.
No fim, registre no kit o que este reel ensinou de novo.

CORREÇÕES DEPOIS DO RENDER:
Se eu pedir alteração depois do render:
Se ela não muda o tempo do vídeo (trocar B-roll, texto, legenda, cor, volume, efeito), renderize de novo só as partes afetadas e junte.
Se ela muda o tempo (corte, velocidade, J-cut, ordem), me avise que o render será inteiro e faça.
Em ambos os casos, valide, atualize o preview e o MP4 final e me diga o que mudou.

Esse é o roteiro:

[COLE O ROTEIRO AQUI]
```

---

## O que trocar

- `[NOME_DO_ARQUIVO_BRUTO]` — nome do .mov/.mp4 gravado (em `~/Claude/videos-brutos/`)
- `[NOME_DA_EMPRESA]` — nome real da empresa/pessoa analisada (3 ocorrências + o nome do arquivo final)
- `[COLE O ROTEIRO AQUI]` — o roteiro falado

## Pedidos que o Fabio costuma acrescentar

- "use `broll1.jpg` / `broll1.mp4` para a primeira cena" — arquivo dele na capa; vídeo dele vai em velocidade
  normal, mudo, sem esticar.
- Uma cena descrita em texto para a capa ("mesa de jantar, cofrinho remendado…") — é pedido de imagem-conceito
  (`fal_img.mjs`, nano-banana-pro, 4:3); mostrar na parada.
- "acelere 1.1" depois de ver o preview — multiplica a velocidade atual (1,1 → 1,21); "só um pouquinho" → 1,15.
