# Camada de motion graphics (skill showreel-interface) — padrão aprovado em 2026-10-02

> **Dosagem (reel Deming v2, pedido do usuário): abertura só com fotos; no corpo, foto real é o padrão e motion só onde carrega a
> história (capítulos, números, o mecanismo do clímax). ≤ ~40% da cobertura em UI. Ver docs/05 §24 e `exemplos/deming/`
> (`gen-v1.py` = versão com motion demais, `gen.py` = versão aprovada).**

Reel Alan Mulally v2: **"ficou perfeito"**. O formato do kit fica inteiro (capa laranja, splits de pré-revelação,
cortes, J-cut, bipe, legendas, marca só depois do nome, trilha + SFX fixos). O que muda é o que cobre o
apresentador: em vez de B-roll de foto genérica com light-leak em todo corte, uma **sub-composição de motion
graphics** com fotos reais como cards, conceitos como UI animada e transições feitas pelos próprios elementos.
Exemplo completo: `exemplos/alan-mulally/` (`mg.html`, `scripts/mg_sfx.py`, `scripts/slots.py`, plano).

## Antes de desenhar: as 3 respostas da skill
- **O chip** (título de capítulo): o átomo de UI do próprio assunto. Mulally → a pílula de status do BPR (● verde /
  amarelo / vermelho), um chip por passo do protocolo.
- **A prova**: fotos reais como cards (pessoa, logo, sede, produto) + motion nos conceitos (quadro de status,
  semáforo, contador de prejuízo, gráficos).
- **A frase que o final inverte**: capa = quadro todo verde (a mentira); fim "tudo verde" volta ao mesmo quadro.

## Arquitetura (motor do kit já suporta)
- `assets/edit-plan.json`: `"mg": {"src": "compositions/mg.html", "id": "mg"}` → `build-edit.mjs` monta o host
  `#mg-host` (track 8, `z-index:30`: acima do apresentador e do B-roll de vídeo, abaixo dos leaks e legendas).
- `compositions/mg.html`: sub-composição 1080×1920 transparente, **uma timeline do reel inteiro** (tempos absolutos,
  os mesmos de `tl.py --words`). Cenas = `.scene` escondidas por CSS, ligadas por `tl.set autoAlpha`.
- `scripts/slots.py`: `MG = {...}` tira do `plan.broll` os slots que viraram motion (continuam no
  `broll-slots.json` como referência de tempo). Splits de pré-revelação e o B-roll de vídeo que fizer sentido ficam.
- `sections`: só as trocas grandes (virada, clímax com "CLIMAX" no nome, CTA) — os leaks deixam de cobrir todo corte.
- Captions: fora das janelas de B-roll de vídeo elas descem para 76% → **a faixa y≈1380–1540 (geometria 1080×1920)
  fica livre** no desenho das cenas. Callout repetido por gráfico sai do plano (o gráfico já diz).
- `scripts/mg_sfx.py`: cues `(t_pico, som, ganho_dB, args)` com o kit sintetizado da skill; rodar **sempre depois de
  `bake.py bed`** (mistura por cima da trilha + SFX fixos). Impactos ≤ −16 dB: a voz fica ≥ 6 dB acima no evento.
- `render-chunks.mjs` (corrigido): cada parte ganha uma cópia da sub-composição com a timeline tocando de A a B.
  **Sem isso a camada some no MP4** (aparece no snapshot e no preview, não no render em partes).

## Componentes que já existem em `exemplos/alan-mulally/mg.html`
`sceneIn/sceneOut` (tela cresce de card → cheia; sai encolhendo para card + chicote para cima revelando o
apresentador) · `chip()` (T2: "+" gira, pílula abre, rolo trava no capítulo) · card de foto com sombra · etiqueta
de nome · carimbo que bate (`slam`) · título palavra a palavra no tempo da palavra (`rise`) com caixa de seleção
com alças · toast de notificação · semáforo + semana · quadro de status com linhas e pílulas (`pop`) · balões de
chat + risco · contador por rolo de dígitos (caça-níquel, seek-safe) · barras · anéis de palma · faixa arco-íris.
Transições internas: chicote lateral com blur (T6), queda/subida no mesmo vetor, smear de chip → corte (T7).

## Armadilhas pagas (todas no Alan Mulally)
- `fromTo` aplica o estado "de" **na montagem**: elemento com `autoAlpha: 1` no "de" aparece antes da hora e o que
  nasce fora da tela fica fora. Usar `immediateRender: false` nesses tweens.
- Com `immediateRender: false`, se o render **pula** para depois do fim do tween, `autoAlpha` que só existe no "de"
  não é aplicado → elemento some. Pôr `autoAlpha: 1` também no "para".
- Elemento que sai "caindo" precisa ir longe o bastante (y ≥ 1900) senão espia na borda.
- Pílula com texto longo quebra em 2 linhas: alargar a pílula (ex.: 470 px para "PRODUÇÃO PARADA").
- Conferir por snapshot em vários instantes de cada cena **e** um quadro de uma parte renderizada antes do render todo.

## Tempo
Montagem da camada + SFX + QC: ~30–40 min. Render a 60 fps em 18 partes: ~18 min (Mac 16 GB).

## Gerar a camada por script (reel Deming)
Quando a cena tem peças repetidas (100 pontos, 112 bolinhas, furos da pá), escrever a camada como gerador Python
(`exemplos/deming/gen.py`): lê o modelo (`compositions/mg.html` copiado para `work/mg/template.html`), injeta CSS, markup e CENAS e grava
`compositions/mg.html`. Aleatório com semente fixa (determinístico). Editar o gerador, nunca o `mg.html` gerado.
