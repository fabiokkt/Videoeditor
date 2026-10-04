# STORYBOARD.md — precisa? (e o template)

**Resposta curta: é opcional. Não alimenta o build.**

No HyperFrames "normal", o `STORYBOARD.md` é o plano frame a frame que os frame-workers
consomem: cada `## Frame N` vira um arquivo em `compositions/frames/`. **Este formato não
funciona assim** — a composição inteira sai de `assets/edit-plan.json` +
`scripts/build-edit.mjs`, num `index.html` só, sem `compositions/frames/`. Nada quebra se o
`STORYBOARD.md` não existir: `npm run check`, `preview` e `render` não o leem.

**Ainda assim vale manter uma cópia por projeto**, por dois motivos baratos:

1. **Retomada.** Sem `BRIEF.md`, o HyperFrames identifica um projeto existente por
   `hyperframes.json` / `STORYBOARD.md` e retoma pelo frontmatter em vez de reinterrogar.
2. **Mapa legível.** É a única visão dos 7 beats em texto — útil pro usuário revisar a
   estrutura sem abrir o `edit-plan.json`.

**Regra:** o `edit-plan.json` é a fonte da verdade. O storyboard é descrição, nunca insumo —
se os dois divergirem, o plano ganha. Não gastar tempo mantendo-o em sincronia fina; atualizar
só quando um beat mudar de verdade.

Gabarito preenchido de verdade: `exemplos/natura/STORYBOARD.md` no kit.

---

## Template (copiar para a raiz do projeto e preencher)

```markdown
---
format: 1080x1920
message: <a tese do vídeo em uma frase>
arc: Gancho → Contexto → Virada → Sequência de punches → Clímax emocional → CTA
audience: <público do reel>
---

> Formato "reel viral" do usuário. Todos os frames são gerados por
> `scripts/build-edit.mjs` a partir de `assets/edit-plan.json` — não há
> compositions/frames neste formato. Slots de B-roll nascem VAZIOS.

## Frame 1 — Gancho (split-screen)
- duration: ~10s
- transition_in: SFX de intro (opening + riser), drum-fill fechando
- status: outline | built | animated
- src: index.html (segs 0-1 · B-roll split topo 44%)

Gancho inteiro em caixa laranja desde o frame 0 (capa). 1º callout com digitação + drum-fill.

## Frame 2 — Contexto (cutaway tela cheia)
- duration: ~5.5s
- transition_in: light-leak + whoosh (10f antes do corte)
- status: outline
- src: index.html (seg 2 · B-roll full com Ken Burns 1→1.07)

## Frame 3 — A virada (tela cheia + callout)
- duration: ~5s
- transition_in: light-leak + swoosh
- status: outline
- src: index.html (seg 3 · apresentador solo, legenda cap-low 76%)

## Frame 4 — Desenvolvimento (cutaways alternados)
- duration: ~8s
- transition_in: cutaway antecipado (preStart) sobre o fim da frase anterior
- status: outline
- src: index.html (segs 4-6)

## Frame 5 — Sequência de punches (segundo split)
- duration: ~7s
- transition_in: transição animada 0.55s power3.inOut
- status: outline
- src: index.html (segs 7-9)

## Frame 6 — Tese + Clímax emocional
- duration: ~7.5s
- transition_in: saída animada do split; riser 3s antes + impact-hit na entrada
- status: outline
- src: index.html (segs 10-11)

## Frame 7 — CTA
- duration: ~8.5s
- transition_in: light-leak + whoosh; push-in 1→1.05 até o fim
- status: outline
- src: index.html (segs 12-13)

Pergunta de engajamento + "me segue para não perder a próxima". Trilha cai e faz
fade no último 0.7s.
```
