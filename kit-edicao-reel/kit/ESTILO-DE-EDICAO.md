# Estilo de edição — Reel Viral

Como é um reel editado hoje: o que aparece na tela, o que se ouve, em que ritmo, e as regras que não mudam.
Estado de 2 de outubro de 2026, depois de 32 reels. O exemplo no fim é o mais recente (Kelly Johnson).

O formato é "engenharia reversa de uma história de sucesso": um apresentador falando para a câmera, coberto por
fotos reais do tema, com o nome da pessoa ou empresa guardado até a narração revelar.

---

## 1. Ficha do formato

| | |
|---|---|
| Quadro | vertical 9:16, 1440×2560, 60 fps |
| Duração | a do roteiro, hoje entre 90 e 100 s. O roteiro nunca é cortado por conta própria |
| Velocidade | 1,1x no vídeo todo, com o tom da voz preservado |
| Cenas | 3 a 5 s cada. Quatro segundos é o alvo e também o teto |
| Transição | em todo corte: light-leak com um whoosh |
| Legenda | até 3 palavras por vez, branca, sem contorno |
| B-roll | fotos reais do tema, com movimento só de câmera |

---

## 2. A estrutura de um reel

Todo reel segue a mesma sequência de seis blocos.

| Bloco | O que está na tela |
|---|---|
| 1. Capa e intro | Tela dividida: B-roll em cima, apresentador embaixo, caixa laranja com o gancho. Nenhuma marca ainda |
| 2. Revelação | O áudio diz o nome pela primeira vez e a imagem do tema entra em tela cheia |
| 3. Corpo | Alternância entre B-roll de tela cheia e o apresentador em tela cheia |
| 4. Virada | A tela dividida volta, uma segunda vez |
| 5. Clímax | B-roll de tela cheia, com riser antes e impacto na entrada |
| 6. CTA | Apresentador em tela cheia, com um push-in lento (1 → 1,05) |

---

## 3. O que aparece na tela

### Tela dividida

```
┌───────────────────────┐
│                       │
│        B-ROLL         │  44% da altura
│                       │
├──── legenda (44%) ────┤
│                       │
│     APRESENTADOR      │  56% da altura
│   olhos a ~49% desta  │
│        faixa          │
└───────────────────────┘
```

A tela dividida entra e sai com uma transição de arrastar de 0,55 s. A altura do apresentador dentro da faixa é
medida em cada gravação, porque o enquadramento muda de um vídeo para outro.

### A capa (quadro 0)

O primeiro quadro do vídeo é a capa do reel. A frase inteira do gancho já está na tela, sem animação de entrada.

- Caixa laranja `#FF4A1C`, com borda branca e brilho.
- Texto em Oswald 700, caixa alta, 90 px, branco com contorno escuro e sombra dura.
- A caixa pulsa de leve (1,018) e um brilho atravessa duas vezes.
- A primeira cena é sempre a tela dividida, mesmo que o apresentador desvie o olhar no gancho. Nesse caso a
  capa fica curta e um B-roll de tela cheia cobre o desvio.

### Legendas

- Montserrat 600, 47 px, brancas, sem contorno, com um halo de sombra.
- Até 3 palavras por vez, quebrando na pontuação.
- Ficam a 44% da altura sobre B-roll e na tela dividida, e a 76% quando o apresentador está sozinho.
- Sobre um B-roll de tela cheia, descem para 76% quando cairiam em cima de um rosto, logotipo ou título.
- Em fundo claro, o B-roll é escurecido. A legenda não muda.
- O texto segue a grafia do roteiro ("pra", "tá", nomes próprios). Onde a fala diz outra coisa, vale a fala.

### Callouts

São as frases de impacto em destaque, cerca de 5 a 9 por reel.

- Montserrat 800, 76 px, caixa alta, contorno de 10 px, a 30% da altura.
- O primeiro entra com efeito de digitação e um drum-fill. Os demais entram com um "pop" e leve rotação.
- Mudam de posição quando cobririam um rosto. Se taparem os olhos de um retrato, saem.

### O apresentador

- Aparece sempre olhando para a câmera. Os trechos em que ele lê o roteiro são medidos quadro a quadro e
  cobertos com B-roll de tela cheia. O que sobra exposto é informado em segundos.
- Em tela cheia leva um zoom que troca uma vez por aparição (1,06 e 1,14).

### B-roll

- Fotos reais do tema, que mostrem o que a fala daquele trecho diz. A ordem de busca é: site oficial ou sala
  de imprensa, Wikimedia Commons, Google Imagens em tamanho grande. Banco de imagens fica de fora.
- Só a câmera se move sobre a foto (aproximação, afastamento, travelling). Texto e logotipo ficam idênticos ao
  original.
- Duas fotos parecidas em sequência contam como "parado": alterna-se assunto, escala e luminosidade.
- Imagem gerada por IA só entra quando o Fabio descreve a cena, e é marcada como "gerada a pedido".
- Vídeo entregue pelo Fabio entra em velocidade normal e mudo.

### Marca só depois do áudio

Nada que identifique a pessoa ou a empresa aparece antes de a narração dizer o nome: nem logo, nem letreiro,
nem rosto, nem produto. A imagem da revelação entra 2 quadros depois do início da palavra. Antes disso usa-se
material real do tema sem marca (interior, detalhe, recorte abaixo do letreiro) ou uma cena genérica do assunto.

---

## 4. O que se ouve

### Cortes

- De frase repetida fica sempre o último take válido. Falso início sai inteiro.
- Nenhuma palavra é cortada no meio. O corte cai no silêncio real entre as falas.
- Falas longas são divididas nas pausas naturais, o que dá ritmo e abre janela para B-roll.

### J-cut

A fala seguinte começa antes de a imagem cortar. A voz nova entra 5 quadros antes do corte de imagem, a emenda
das duas vozes é ponta a ponta (nunca somadas) e o crossfade de 3 quadros cabe inteiro no silêncio. O respiro
entre falas fica em torno de 0,245 s. Tudo isso é conferido por medição em cada reel, emenda por emenda.

### Bipe de censura

Palavrão é bipado inteiro, da primeira consoante ao fim do som, com um tom de 1 kHz. A legenda vira `P****` e
entra junto com o bipe. De preferência o apresentador fica em tela cheia nesse momento, porque a boca sob o bipe
é o que se lê como censura. O bipe é aceito por medição de energia na faixa de 1 kHz, e a transcrição inteira é
varrida atrás de palavrão antes de qualquer aprovação.

### Trilha e efeitos

| Elemento | Onde | Volume |
|---|---|---|
| Trilha | o reel todo, baixando nos últimos ~9 s e sumindo no fim | 0,079 → 0,045 → 0 |
| Abertura + riser | de 0 a 3,2 s | 0,25 e 0,22 |
| Boom | 4,8 s | 0,12 |
| Drum-fill | no primeiro callout | 0,3 |
| Whoosh / swoosh | um por transição, alternados | 0,18 |
| Riser | 3 s antes do clímax | 0,2 |
| Impacto | na entrada do clímax | 0,3 |

Efeito sonoro é sempre um toque curto no corte. Não entra batida ou tique contínuo por baixo da fala. O áudio
final passa por um limitador a −1 dB.

---

## 5. Ritmo

- A cada 4 s, no máximo, acontece algo: troca de cena, zoom, callout ou transição.
- Cenas com menos de 3 s também não servem: muitas tomadas curtas seguidas já foram reprovadas.
- Todo corte tem transição, inclusive os cortes entre duas fotos dentro da mesma sequência.
- O light-leak dura 0,7 s e começa 10 quadros antes do corte. Um reel de 90 s tem de 17 a 20.

---

## 6. Como o trabalho anda

1. **Montagem.** Cortes, velocidade, J-cuts, bipe, legendas, callouts, medição do olhar e pesquisa de fotos,
   com o B-roll ainda em cartões provisórios.
2. **Parada única.** O Fabio recebe o link do preview e a lista de tudo que mexe no tempo: duração, cortes,
   velocidade, J-cuts, palavrões, olhar, primeira cena e a foto prevista para cada trecho.
3. **Depois do "pode gerar as brolls".** Os B-rolls reais são gerados e encaixados, o olhar é medido de novo e
   o vídeo é renderizado direto, sem nova revisão.
4. **Correção depois do render.** Se não muda o tempo (foto, texto, cor, volume), refaz-se só o trecho, em
   5 a 10 min. Se muda o tempo (corte, velocidade), é render inteiro, de 25 a 40 min.

A gravação original nunca é alterada, e isso é conferido por MD5 no começo e no fim.

---

## 7. Exemplo: reel Kelly Johnson

Gravação de 140,8 s que virou um reel de **97,3 s**, a 1,1x.

| | |
|---|---|
| Takes | 35 (8 trechos repetidos ou falsos inícios descartados) |
| Legendas | 91 |
| Callouts | 9 |
| B-rolls | 20 (5 em tela dividida, 15 em tela cheia) |
| Transições | 18 light-leaks |
| Efeitos sonoros | 25 |
| Maior intervalo sem evento | 3,85 s |
| Bipe | 1 |
| Leitura de roteiro exposta | 0 s |

### Linha do tempo

| Tempo (s) | Tela | Fala |
|---|---|---|
| 0,00 – 3,60 | **Capa**, tela dividida: tenda de circo + caixa laranja | "Esse cara é um dos engenheiros mais mal-humorados e mais…" |
| 3,60 – 7,49 | B-roll cheio: avião espião em voo, sem marca | "…secretos dos Estados Unidos. E ele criou um protocolo polêmico" |
| 7,49 – 10,20 | Tela dividida: escritório cheio | "pra provar que a sua empresa não é lenta" |
| 10,20 – 12,72 | Tela dividida: reunião lotada. Callout com digitação: **É LENTA POR GENTE DEMAIS.** | "por falta de gente. É lenta por gente demais." |
| 12,72 – 16,03 | **Revelação**: retrato de Kelly Johnson | "Kelly quebrou a perna do menino…" |
| 16,03 – 19,00 | B-roll cheio: Área 51 vista do ar | "achou a Área 51 pra CIA e devolveu" |
| 19,00 – 21,85 | B-roll cheio: Kelly com o U-2. Callout: **PORQUE SOBROU.** | "dois milhões de dólares pro governo. Porque sobrou." |
| 21,85 – 27,90 | Apresentador | "E esse é o protocolo… Primeiro, corta gente." |
| 27,90 – 31,00 | B-roll cheio: Kelly e o piloto sobre a asa | "Ele diz que número de pessoas encostando no projeto" |
| 31,00 – 36,60 | Apresentador. Callout: **QUASE VIOLENTO.** | "tem que ser cortado de um jeito quase violento…" |
| 36,60 – 39,12 | B-roll cheio: gente em volta de um papel | "Oito pessoas pra aprovar um panfleto?" |
| 39,12 – 44,31 | Apresentador. Callout: **SEIS TÃO SOBRANDO.** | "Seis tão sobrando… Segundo, nunca pague ninguém pelo tamanho da equipe." |
| 44,31 – 50,50 | Dois B-rolls cheios: Kelly com o F-104, aperto de mão | "Ele diz que aumento vem do resultado…" |
| 50,50 – 55,99 | Apresentador, **bipe** em 51,47–51,82 | "E você paga pra P**** da empresa engordar…" |
| 55,99 – 64,04 | Dois B-rolls cheios: papelada, planilha | "corta o relatório que ninguém lê…" |
| 64,04 – 67,91 | Apresentador. Callout: **MANTÉM SIMPLES, ESTÚPIDO.** | "Mantém simples, estúpido. Era o lembrete dele pro time." |
| 67,91 – 70,40 | B-roll cheio: a tenda e o caça | "E a virada foi uma tenda de circo." |
| 70,40 – 76,74 | **Virada**, tela dividida em duas tomadas: o caça na pista, o protótipo no pátio | "Na guerra, o exército pediu um caça a jato…" |
| 76,74 – 79,74 | B-roll cheio: chaminé de fábrica | "do lado de uma fábrica de plástico, que fedia tanto" |
| 79,74 – 83,93 | Apresentador | "…atendia o telefone: 'Fábrica do Gambá, pois não?'" |
| 83,93 – 87,59 | **Clímax**: o caça voando, riser + impacto. Callout: **MENOS DE CINCO.** | "Prometeram em seis meses. Entregaram em menos de cinco." |
| 87,59 – 94,04 | Dois B-rolls cheios: escritório cheio, o gambá na cauda | "Projeto atrasado e a sua solução é contratar…" |
| 94,04 – 97,34 | **CTA**: apresentador com push-in | "…me segue, porque você é demais." |

### O que este exemplo mostra

- **Marca depois do áudio.** O nome "Kelly" é dito em 12,65 s e o retrato entra em 12,72 s. Os quatro B-rolls
  anteriores não mostram a pessoa nem a Lockheed.
- **Último take.** "Oito pessoas pra apro… / Oito pessoas pra aprovar um panfleto?" ficou só com a segunda.
- **J-cut medido.** 34 emendas, nenhum crossfade sobre fala, voz entrando de 4,9 a 5,4 quadros antes do corte.
- **Bipe medido.** 100% da energia da janela em torno de 1 kHz, sem resíduo de fala.
- **Imagem a pedido.** A tenda de circo da capa foi gerada por IA a partir da cena descrita pelo Fabio. As
  demais são fotos reais.

---

## 8. O que não entra

- Abrir o vídeo em B-roll de tela cheia em vez da tela dividida.
- Marca, rosto ou produto antes de o áudio dizer o nome.
- Apresentador lendo o roteiro com o olhar fora da câmera.
- Foto parada por mais de 5 s, ou corte sem transição.
- Batida ou tique contínuo por baixo da fala.
- Palavrão audível, mesmo que parcialmente.
- Foto de banco de imagens ou com marca d'água; IA sem pedido.
- Vídeo do Fabio esticado ou em câmera lenta.

---

Os números completos, os motivos de cada regra e os scripts estão em
[KIT-EDICAO-REEL/docs/05-calibracoes-e-armadilhas.md](KIT-EDICAO-REEL/docs/05-calibracoes-e-armadilhas.md).
