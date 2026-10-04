# J-cut — como é feito hoje (emenda ponta a ponta)

O J-cut faz a **fala seguinte entrar antes do corte de imagem**. Este documento é o modelo mental do que
`scripts/cuts.py`, `scripts/build-edit.mjs` (`mixVoice`) e `scripts/bake.py voz` produzem — e de como validar.
A versão anterior (duas faixas de voz em pingue-pongue, sobrepostas, com crossfade de 5 quadros por tween de
volume) foi aposentada no reel Atul Gawande; o texto antigo está em `legado/v1-2026-09-16/` e no git.

## O que mudou e por quê

| Antes | Problema medido | Agora |
|---|---|---|
| duas vozes **somadas** durante o lead | respiro irregular, 0,00–0,20 s; "empresa.Primeiro" colado | voz emendada **ponta a ponta**, sem sobreposição |
| crossfade de 5 quadros | comia até 76 ms da palavra final | crossfade de **3 quadros**, inteiro no silêncio |
| lead contado do início do clipe de voz | a 1ª palavra entrava só 0,9 quadro antes do corte | lead contado da **1ª palavra**: `jcutLeadFrames` 9 |
| folgas 0,12 / 0,10 | respiro de 33 ms entre frases | `HEAD_PAD` 0,20 · `TAIL_PAD` 0,13 · `TA` 0,12 · `HH` 0,15 |
| um `<audio>` por take + tweens | 160 players, preview preto | uma faixa pronta `assets/voz-mix.m4a` |

## Os três tempos de cada take (`work/segs.json` → `segments` do plano)

Para cada take, o `cuts.py` mede `on` (início da fala) e `off` (fim da fala) no envelope e grava:

- **`in`** = `on − HH` (0,15 s de source antes da fala; no 1º take, `on − HEAD_PAD`) — onde a **voz** do take começa
- **`aout`** = `off + TA` (0,12 s depois da fala) — onde a **voz** do take termina
- **`out`** = `aout + lead × rate` — onde o **vídeo** do take termina (no último take, `out = aout = off + TAIL_PAD`)

Ou seja: a voz do take *k* vai de `in` a `aout`; a do take *k+1* entra em seguida; e a **imagem** do take *k*
continua na tela por mais `lead` enquanto a voz nova já está tocando. Isso é o J-cut.

Respiro entre falas = `(TA + HH) / rate` ≈ 0,245 s a 1,1x.

### Pausa curta
Se a pausa real entre duas falas é menor que `TA + HH`, a emenda vai dentro do silêncio real (45% para o tail,
55% para a cabeça). Se com isso o fade-in de 3 quadros invadiria a palavra seguinte e o crossfade **cabe** na
pausa, a emenda vai logo antes da fala nova: `in = on − XF − 5 ms`, `aout = in` (Herb Kelleher, "piloto | foi
grosso", pausa de 0,14 s).

## Na timeline (`build-edit.mjs`)

- `sourceDur = (out − in) / rate` · `lead = min(jcutLeadFrames/30, sourceDur − 10 quadros)` (0 no 1º take)
- janela visual do take: `dur = sourceDur − lead`; a voz começa em `audioStart = tStart − lead`
- vídeo: `data-media-start = in + lead × rate` — quando a imagem entra, ela já avançou o mesmo que a voz
  (**lip-sync preservado**)
- voz (`mixVoice`): cada clipe dura até o `audioStart` do seguinte + `XFADE`; o `bake.py voz` aplica `atempo`
  (tom preservado), fade-in/out de `XFADE` e `adelay`, e soma tudo em `voz-mix.m4a` com `normalize=0`

## Por que `jcutLeadFrames` é 9 e não 5

O clipe de voz começa `HH` = 0,15 s de source **antes** da 1ª palavra (respiração). A 1,1x isso são ~4 quadros
de timeline. Com lead 5 a palavra entrava ~1 quadro antes do corte de imagem — J-cut invisível. Com **9**
(= 5 + `HH`/rate em quadros) a 1ª palavra entra **~5 quadros** antes do corte. Se a velocidade mudar, refazer a
conta e conferir com o `jcut_check.py`.

## Validação por dados (obrigatória)

```bash
python3 scripts/jcut_check.py
```
Tem que sair: `buracos 0` · `crossfade sobre fala: nenhum` · lead de FALA com mediana ~5 quadros (4,9–5,9) ·
respiro mediano ~0,245 s. Qualquer "crossfade sobre fala" se resolve no `cuts.py` (pausa curta, `FORCE_IN`,
`FORCE_OFF`), nunca aumentando o crossfade.

O `mkchunks.py` **não** pode cortar o `out` no `in` do take seguinte: em takes contíguos o `out` passa do `in`
seguinte de propósito (é o lead do vídeo).

## L-cut (`videoTail`)

Campo opcional do segmento, em segundos de source: o **vídeo** do take corta antes do fim e o do take seguinte
entra adiantado. Só serve quando o pré-rolo do take seguinte já está falando (mudo por mais de ~0,3 s lê como
imagem congelada) e é inútil quando os takes são contíguos no source. Na prática dos reels atuais não é usado:
desvio de olhar se cobre com B-roll.
