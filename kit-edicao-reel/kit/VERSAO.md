# Versões do kit

## v3.1 — 2026-10-07 · otimização de tempo medida (reel Matthew Ridgway)

Pedido: "teria como otimizar esse tempo sem perder qualidade?" (Ridgway: ~2h05 na nuvem). Tudo testado no bruto do Ridgway com
saídas **idênticas byte a byte** ao fluxo v3 (docs/05 §32).
- `fase1.sh` / `mezanino.sh`: voz primeiro (`mezanino.sh … audio|video`) e transcrição ENQUANTO o mezanino codifica — liga só com
  ≥ 8 núcleos e ≥ 12 GB (Mac). No container de 4 núcleos ficou mais lento (953 × ~850 s): série.
- `fase2.sh`: medidores de olhar em paralelo com o bake do aroll (≥ 12 GB): 578 → 539 s no container.
- `work/entregas.sh <Nome>` novo no modelo: cópia do chat < 30 MB e HEVC final < 100 MB com bitrates pela duração, em paralelo com
  ≥ 8 núcleos, + comparação master × final com SSIM.
- Fotos primeiro, no processo principal durante a fase 1 (`wmcat.py` / `wmcatlote.py` → `wmfila.py` em fila priorizada; docs/14).
- Peças prontas: `exemplos/matthew-ridgway/` (parede + bilhete, objeto SVG que rasga, lista FALTA → RESOLVIDO, contador 5.000, conversa
  com carimbo, anel no detalhe da foto) listadas no fim do docs/13.
- `work/olhos_y.py` (splitShiftY medido) e docs/05 §29 e §32.

## v3 — 2026-10-02 · fluxo rápido (o padrão)

Pedido: "o mais rápido que puder, entregando o mesmo resultado ou melhor". Medido no bruto do Alan Mulally.
- `docs/14-fluxo-rapido.md` + comandos de fase: `fase1.sh`, `fase2.sh`, `legendas.sh`, `montar.sh`, `render-par.sh`.
- Whisper `large-v3-turbo` por padrão (2,3x, mesmo texto) · `chunks_from_regions.py` substitui o 2º passe por chunk.
- `bake.py aroll`: VideoToolbox + 3 takes em paralelo (291 s → 102 s, PSNR igual) · sem cena de vídeo = sem broll-full.
- `render-par.sh`: 3 partes em paralelo (~17 → ~8 min); `render-chunks.mjs` com lista de junção por parte (a lista
  compartilhada corrompia partes rodando em paralelo — pego no teste, PSNR 8,8 dB na parte 10).
- Camada de motion como padrão: `compositions/mg.html` no modelo com a biblioteca de componentes que emitem o próprio
  SFX (`cue()` → `mg_cues.mjs` → `mg_sfx.py`); splits desenhados pela camada (`slots.py` com `MG={"*"}`, split sem
  arquivo no `build-edit.mjs`/`bake.py`).
- `gaze_sheet.py`: folha de olhar com o rosto inteiro e recorte automático.
- `bipe.py` do modelo com `JANELAS=[]` (o exemplo do Kazuo seria aplicado num vídeo novo pelo fase2.sh).

## v2.1 — 2026-10-02 · camada de motion graphics (reel Alan Mulally)

Primeiro reel feito do zero com `novo-projeto.sh` (numa máquina nova, 16 GB). Aprovado: "ficou perfeito".
- **Padrão novo de edição**: sub-composição `compositions/mg.html` (skill showreel-interface) por cima do
  apresentador — fotos reais como cards, conceitos como motion, transições feitas pelos elementos, SFX cravados no
  quadro. `docs/13-camada-motion.md` + `exemplos/alan-mulally/`.
- Motor: `build-edit.mjs` monta o host da camada (`plan.mg`); `render-chunks.mjs` desloca a timeline das
  sub-composições por parte (sem isso a camada sumia no MP4); `make_broll.py` ganhou `ease='out'`;
  `slots.py` ganhou o conjunto `MG`; novo `scripts/mg_sfx.py` (kit de som da skill).
- Pesquisa de imagem: navegador na fonte primária + `hyperframes capture` (`docs/11`); `filt.py` barra westend61 e
  stockcake. Busca por API vira último recurso.
- `docs/05` §23 com as lições.

## v2 — 2026-10-01 · consolidação

Objetivo: parar de depender dos projetos já editados. Até aqui cada reel novo copiava os scripts do anterior e
as lições ficavam espalhadas em 27 `EDICAO.md` e 26 notas de memória; o kit estava parado em 16/09.

- **`modelo-projeto/`**: os 50 scripts na versão mais nova (projeto `kazuo-inamori`), `index.html` como template
  (1440×2560, capa Oswald), plano-esqueleto, `EDICAO.md` modelo, ferramentas de `work/` (render e pesquisa),
  `CLAUDE.md` apontando para o kit. Caminhos fixos de projeto removidos de 6 arquivos.
- **Três scripts novos**, para passos que eram digitados a cada reel: `mezanino.sh`, `size_sweep.py`,
  `finalizar.py`. Os dois últimos reproduzem os números registrados do reel Kazuo Inamori; o primeiro foi
  testado em clipe sintético SDR full-range (o ramo HDR não foi exercitado).
- **`novo-projeto.sh`**: cria o projeto sem copiar de projeto antigo.
- **`docs/`**: `05` reescrito a partir de todos os `EDICAO.md` e das notas de memória; `01`, `02`, `04`, `06`,
  `07`, `09` reescritos para o fluxo atual; `10`, `11`, `12` novos.
- **`assets-fixos/`**: + Oswald 700, + modelo FaceLandmarker.
- **`exemplos/kazuo-inamori/`** e **`arquivo-projetos/`** (texto dos 31 projetos).
- **`legado/`**: gerador e skill da v1, prompts antigos.
- Teste: o `build-edit.mjs` do modelo, com o plano do Kazuo, gera o mesmo `index.html` do projeto
  (`verificar-instalacao.sh`).

Não verificado nesta versão: um reel inteiro feito do zero com `novo-projeto.sh`. O primeiro reel depois desta
data é o teste real — anotar aqui o que precisou de ajuste.

## v1 — 2026-08-21 a 2026-09-16

Formato 1080×1920 @30, um elemento por take, J-cut em duas faixas com crossfade de 5 quadros, export direto.
Gerador de 308 linhas, 13 scripts. Reels Natura e Nubank como exemplos. Está em `legado/v1-2026-09-16/`.

---

## Rotina de manutenção

```bash
cd ~/Claude/KIT-EDICAO-REEL
git add -A && git commit -m "<reel>: <o que mudou>"
# cópia de segurança no servidor (share Company montado) — vai com o histórico do git:
rsync -rt --delete --exclude .DS_Store ./ "/Volumes/Company/Equipe/FABIO KENJI/KIT-EDICAO-REEL/"
```

## v3.1 — 2026-10-02 (reel Deming)
- Dosagem foto × motion (docs/05 §24) a pedido do usuário: abertura só com fotos, motion só onde carrega a história.
- `exemplos/deming/` (camada gerada por `gen.py`; `gen-v1.py` = versão reprovada por excesso de motion).
- Modelo: `.light` com chão escuro (legenda legível) e `.tag` sem quebra. docs/14: refazer depois de ajuste (render-par retoma).
- Portabilidade: `COMECE-AQUI.md`, `instalar.sh` (venv 3.12, Whisper turbo, skills), `skill/showreel-interface` dentro do kit,
  `verificar-instalacao.sh` confere venv, modelo turbo e a skill da camada.
