# EDICAO.md — mapa do projeto (reel Alan Mulally)

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**. Kit v2 (4db7732), 1º reel feito do zero com `novo-projeto.sh`.
**Estado (2026-10-02): EXPORTADO** (`renders/Alan-Mulally-reel-final.mp4`), comando único, sem parada (pedido do usuário).
Duração **103,309 s** · 35 takes · 1 bipe · 96 legendas · 9 callouts · 19 light-leaks · 26 SFX · 22 slots de B-roll.

> **Regra de ouro: nunca editar `index.html` à mão.**
```
editar assets/edit-plan.json (ou scripts/slots.py para B-roll)  ->  node scripts/build-edit.mjs  ->  python3 scripts/bake.py <alvos>  ->  npm run check
```
Python desta máquina: `~/Claude/.venv-reel/bin` (3.12 + mediapipe 0.10.14) na frente do PATH.

## Onde mexer em cada coisa

| Quero mudar… | Arquivo |
|---|---|
| cortes / takes | `scripts/mkcut.py` → `scripts/cuts.py` → `python3 scripts/plan_segments.py` |
| texto de legenda | `scripts/captions_fix_table.py` → `python3 scripts/fix_captions.py` |
| callouts | `impacts` no plano (seg 2 `top` 6, seg 31 `top` 60) |
| B-roll | `scripts/slots.py` → `scripts/entrega.py` → `scripts/make_broll.py` (`ease='out'` novo) → `slots.py --real` |
| legenda baixa sobre B-roll | `capLowSegs` [1, 3, 4, 24, 28, 29, 30, 31] |
| enquadramento do split | `splitShiftY` **469** (olhos medidos em y≈908/1920 nas janelas de split) |
| bipe | `scripts/bipe.py` (49,435–50,005 s do source) |

## Bruto original

`~/Downloads/857F3F29-3490-4046-8493-26C4BAEBA1EA 2.MP4` — **não alterado**. MD5 `ea3ccbeb7a40f5a0ef063091568af7b8`.
HEVC 1440x2560 @60, 152,32 s, **SDR full-range** (`yuvj420p`/`pc`, BT.709), áudio AAC 44,1 kHz.

## Mezanino

full→limited (`mezanino.sh`). Bruto × mezanino (15/76/137 s): 129,59/128,32 · 130,53/129,23 · 130,72/129,43; desvio 70,46→70,41 — não lavou.

## Transcrição

33 regiões → whisper large-v3 por região → `mkcut.py` divide em 6,44 · 12,55 · 15,18 · 22,83 · 25,88 · 27,19 · 30,75 · 41,44 · 61,13 ·
71,20 · 78,72 · 82,52 · 97,83 · 107,49 → 35 chunks. Passe por chunk mantido, vazamentos de borda apagados com DROP; ch33 com o
passe cru (o `align.py` jogou "gerente" 3 s para frente) + FIXT do "Seu" no início da fala (140,44).
Áudio ≠ roteiro (vale o áudio): "proíbe A piada", "dezessete bilhões" (sem "de dólares"), "um novo carro", "Na reunião SOBRE o primeiro
vermelho" (3 passes, inclusive com `--prompt` "sobe"), "O Alan bate palma E PERGUNTA". Grafia do roteiro: "pra", "pro", "Seu gerente", "com carro".

**O bruto não tem estas frases do roteiro** (não gravadas — nada a cortar ou recuperar): "Antes, era o engenheiro-chefe do Boeing 777. E em
quatro anos… a mais lucrativa do mundo." · "Na sua empresa: o vendedor sabe no dia dez… no dia trinta." · "Não tô falando de você… meu
amiguinho." · "Ele parou a reunião e perguntou… Todo mundo olhou pro chão." · "Todo mundo achou que iam entrar dois seguranças…" ·
"E o Mark? Anos depois, virou o CEO da Ford."

## Takes descartados (mantido sempre o ÚLTIMO)

r00 fim "Alan nunca tinha trabalho…" → r01 · r02 fim "Primeiro, aceita" → r03 · r05 "…quando dá merda." → r06 · r07/r08 "Segundo,…" → r09 ·
r12 → r13 · r14 fim "E a virada foi uma pal…" → r15 · r17 fim "Aí o Mark…" · r18 (igual ao r19) → r19 · r21 "Boa sorte!" → r22.
CTA r30–r32 = um take só.

## J-cut

34 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9–5,4 quadros · respiro mediano 0,245 s.

## Bipe

"…quando a M**** já tá feita": nasal /m/ 49,44 · "er" · /d/ 49,82–49,87 · "a" até 50,00 · /ʒ/ de "já" em 50,02. Bipe **49,435–50,005**.
Timeline 35,30–35,82: 100% da energia em 950–1050 Hz, 0% fora de 900–1100 Hz. Apresentador em tela cheia no bipe. Legenda `M****`.

## Varredura de olhar

`gaze_tl` 52 janelas/23,7 s → `gaze_pose` 22/5,7 s. Recorte do `gaze_review` corta a testa neste bruto: folhas próprias com rosto inteiro
(`work/gzsheet.py` → `gaze/me/g*.jpg`, 62 janelas). Nítidas: 36,2–37,1 · 66,3–66,8 · 68,1–68,5 · 77,0–77,2 · 86,4–86,7 — todas cobertas por
B-roll. 2ª passada nos quadros da composição (`snapshots/g2/`): olhando para a lente. **Leitura exposta: 0 s** (piscadela expressiva de
~0,2 s em 83,0 s, "foi um prazer te conhecer", não é leitura).

## Marca só depois do áudio

1ª vez que o áudio diz "Alan": **13,16 s**. s01–s04 sem Mulally/Ford/GM. Revelação (s05) em **13,23 s**.

## Capa / imagem gerada a pedido

Codex `gpt-5.6-sol` (o `gpt-6.1-sol` do config é recusado no login ChatGPT): diretoria à noite, telão todo verde, executivos olhando para a
mesa (`work/conceito/capa-diretoria-verde.png`, 1536x1024). Reusada no s16 (a virada "Tudo verde") como callback.

## B-roll

`PESQUISAS-BROLL-ALAN-MULALLY.md`. Busca por Bing Imagens (`scripts/bimg.py`, sem chave Serper nesta máquina) + Wikimedia.
s02 e s20 trocados depois do QC (westend61 e stockcake são bancos de imagem) por Wikimedia CC0 / domínio público.

## Lições para o kit

- `bimg.py`: busca de imagens sem chave (Bing) no mesmo formato do `gimg.mjs`; `work/pesq/s.sh` aponta para ele.
- `make_broll.py`: `ease='out'` (1-(1-p)^2,2) — câmera chega depois do leak e assenta (lei 1 da skill showreel-interface).
- `filt.py` não barra westend61 e stockcake: acrescentar à lista de bancos.
- `align.py` pode deslocar palavras em chunk cuja 1ª palavra tem duração zero ("Faz[500-500]"): conferir `tl.py --words`.
- Codex como gerador da imagem a pedido: `codex exec -m gpt-5.6-sol …` (~70 s, sai 1536x1024 em paisagem).
