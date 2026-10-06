# Referência — os docs do kit, na íntegra

Cópia fiel dos documentos do `KIT-EDICAO-REEL`, na ordem de leitura do kit. Cada bloco começa com `# ARQUIVO: <caminho>`. Entre docs que se contradizem vale o mais novo: `docs/14` e `docs/05` §23–24 (o resumo coerente está em `1-MANUAL-DO-FORMATO.md`).

_kit em 47e642e · v3.1: dosagem foto x motion (reel Deming), exemplo Deming, instalador e guia para outro computador, showreel-interface no kit · gerado em 2026-10-04_

## Índice

- `README.md`
- `docs/14-fluxo-rapido.md`
- `docs/05-calibracoes-e-armadilhas.md`
- `docs/13-camada-motion.md`
- `docs/01-pipeline-hyperframes.md`
- `docs/02-jcut-algoritmo.md`
- `docs/06-checklist-execucao.md`
- `docs/10-scripts.md`
- `docs/11-pesquisa-broll.md`
- `docs/12-export-em-partes.md`
- `docs/04-prompt-comando-unico.md`
- `docs/07-mapa-de-arquivos.md`
- `docs/09-instalacao-outra-maquina.md`
- `COMECE-AQUI.md`
- `VERSAO.md`
- `skill/edicao-reel-viral/SKILL.md`
- `modelo-projeto/EDICAO.md`
- `ESTILO-DE-EDICAO.md`
- `docs/03-blueprint-casas-bahia.md`
- `docs/08-storyboard-opcional.md`


---

# ARQUIVO: `README.md`

# KIT DE EDIÇÃO — Reel Viral (HyperFrames) · v3.1

> **Outro computador? Leia `COMECE-AQUI.md` e rode `zsh instalar.sh`.**

**A fonte única do formato.** Tudo que foi aprendido em 31 reels — números, armadilhas, scripts, prompts — está
aqui. Um reel novo nasce deste kit e não consulta nenhum projeto antigo; por isso os projetos antigos podem
sair do Mac.

Formato: 9:16, 1440×2560 @ 60 fps, 1,1x, ~90–100 s. Motor: HyperFrames. Máquina: MacBook Air 8 GB.

---

## Começar um reel

```bash
zsh ~/Claude/KIT-EDICAO-REEL/novo-projeto.sh <slug> "Título"
```
Cria `~/Claude/reel-auto/<slug>` com scripts, template, fontes, SFX, trilha, light-leak e modelo de olhar.
Depois é seguir `docs/06-checklist-execucao.md`. O prompt que o Fabio envia está em `docs/04`.

## O que tem dentro

| Pasta | Conteúdo |
|---|---|
| **`docs/`** | O conhecimento. `05` é o mais importante |
| **`modelo-projeto/`** | O esqueleto de um projeto: 53 scripts, `index.html` (template), plano-esqueleto, `EDICAO.md` modelo, ferramentas de pesquisa e de render |
| **`novo-projeto.sh`** | Cria o projeto a partir do modelo + assets fixos |
| **`assets-fixos/`** | Trilha, 9 SFX, light-leak, fontes (Montserrat 600/800, Oswald 700), modelo FaceLandmarker |
| **`exemplos/kazuo-inamori/`** | O reel mais recente como referência: plano, `index.html`, `EDICAO.md`, pesquisa, chunks |
| **`arquivo-projetos/`** | Só o texto dos 31 projetos (EDICAO, pesquisas, scripts de cada época, planos) — consulta histórica |
| **`broll-prompts/`** | Pesquisas/prompts de B-roll dos primeiros reels |
| **`legado/`** | Kit v1 (gerador e skill de 16/09), prompts antigos, backup |
| **`COMECE-AQUI.md` · `instalar.sh`** | Levar o kit para outro Mac: guia simples + instalador de um comando |
| **`exemplos/deming/`** | **O reel mais recente e o padrão atual** (dosagem foto × motion, camada gerada por script) |
| **`skill/`** | `edicao-reel-viral` (porta de entrada) + `showreel-interface` (método da camada; o `mg_sfx.py` depende dela) |
| **`verificar-instalacao.sh`** | Confere o ambiente e reconstrói o reel de referência |
| `exemplos/natura`, `exemplos/nubank`, `bruto/` | do kit v1 (formato antigo, 1080×1920 @30) |

### Ordem de leitura
0. **`docs/14-fluxo-rapido.md` — o fluxo PADRÃO (kit v3): ~1 h do bruto ao MP4, com a camada de motion**
1. `docs/05-calibracoes-e-armadilhas.md` — todo número travado e todo erro já pago
2. `docs/01-pipeline-hyperframes.md` — o fluxo fase a fase, com comandos e o contrato do `edit-plan.json`
3. `docs/06-checklist-execucao.md` — checklist
4. `docs/10-scripts.md` — o que cada script faz; quais são motor e quais são dados do vídeo
5. `docs/02-jcut-algoritmo.md` · `docs/11-pesquisa-broll.md` · `docs/12-export-em-partes.md`
5b. **`docs/05` §24 — dosagem: abertura só com fotos, motion só onde conta a história**
6. **`docs/13-camada-motion.md` — o padrão atual (motion graphics da skill showreel-interface), exemplo em `exemplos/alan-mulally/`**
7. `docs/04-prompt-comando-unico.md` — o prompt
8. `docs/09-instalacao-outra-maquina.md` · `docs/07-mapa-de-arquivos.md`
9. Histórico: `docs/03-blueprint-casas-bahia.md`, `docs/08-storyboard-opcional.md`

---

## As regras que não se negociam

1. **Nunca editar o `index.html` à mão.** Plano → `build-edit.mjs` → `bake.py` → `npm run check`.
2. **Mezanino com a conversão de cor certa antes de tudo** (quase todo bruto é SDR *full-range*; sem converter, lava).
3. **Uma tarefa pesada por vez.** Whisper junto com encode derruba o Mac.
4. **O apresentador aparece olhando para a câmera.** Varredura de olhar duas vezes; leitura exposta reportada em segundos.
5. **Primeira cena em split, capa laranja no quadro 0.** Nada da marca antes de o áudio dizer o nome.
6. **Último take válido; palavra inteira; palavrão bipado inteiro e conferido por medição.**
7. **J-cut validado por dados** (`jcut_check.py`): fala 5 quadros antes do corte, crossfade no silêncio.
8. **Troca de cena ou efeito a cada ~4 s, com transição em todo corte.**
9. **Kit v3: comando único sem parada** (docs/14), MP4 mandado no chat. Parada só a pedido.
10. **Composição leve** (≤ ~10 elementos de mídia) e **export em partes**.

---

## Como o kit se mantém

- Todo reel fecha levando as "Lições para o kit" do seu `EDICAO.md` para `docs/05` e, se mexeu em script, para
  `modelo-projeto/scripts/`.
- O kit é um repositório git (`git log` mostra o que mudou e quando). `VERSAO.md` resume as versões.
- Cópia de segurança no servidor: `/Volumes/Company/Equipe/FABIO KENJI/KIT-EDICAO-REEL/` (atualizar depois de
  cada commit: comando em `VERSAO.md`).
- **Fora do kit, de propósito:** as chaves de API (`~/Claude/reel-auto/.env`), o modelo do Whisper (3 GB, em
  `~/.cache/whisper/`), as skills do HyperFrames (vêm com a ferramenta) e toda mídia de projeto.

## Histórico do formato

Casas Bahia (referência, CapCut → formato extraído quadro a quadro) → Ambev (Palmier) → Natura (1º em
HyperFrames) → Nubank → Bariloche (export em partes) → Localiza, O Boticário (capa laranja) → iPhone Duo (Oswald)
→ André Esteves (faixas pré-renderizadas, ritmo de 4 s) → Costco → Localiza2 (2K/60, marca só depois do áudio)
→ Jeff Bezos (bipe) → IKEA, Chris Voss, Rolex, Jocko Willink → Dan Martell (cenas de 3–5 s, B-roll e leaks numa
faixa) → Charlie Munger (olhar na timeline) → David Marquet → Atul Gawande (J-cut ponta a ponta) → Andy Grove,
Reed Hastings (lead da fala, `--split 3`) → Herb Kelleher → Taiichi Ohno (parada única) → Vince Lombardi → Mike
Michalowicz (layout à mão, imagem-conceito) → Sun Tzu → Kazuo Inamori (olhar compensado pela pose).


---

# ARQUIVO: `docs/14-fluxo-rapido.md`

# Fluxo rápido (kit v3) — do bruto ao MP4 em ~1 hora, com um comando

**Teste de ponta a ponta (2026-10-02, bruto do Alan Mulally):** fase1 77 s (+ mezanino ~2,5 min) · fase2 ~5,5 min
(com o aroll novo) · montar 55 s · render+finalizar 13 min · QC OK, quadros = timeline, sincronia 10 ms. O que sobra
é trabalho de leitura e autoria (cortes, legendas, olhar, cenas da camada): ~30–40 min com a biblioteca.

**Este é o fluxo padrão.** O resultado é o do reel Alan Mulally v2 (aprovado: "ficou perfeito"): o formato do kit
(capa laranja, splits, J-cut, bipe, legendas, marca só depois do nome, trilha + SFX fixos) com a camada de motion
graphics da skill `showreel-interface` por cima. Tudo que existia só para o fluxo antigo de B-roll em vídeo
(entrega.py, make_broll.py, bake de cenas, light-leak em todo corte, 2º passe do whisper por chunk) **saiu do caminho**.
Sem parada no meio: o vídeo pronto vai para o chat no fim.

## Onde o tempo foi ganho (medido no bruto do Alan Mulally, 152 s → reel de 103 s, Mac M4 16 GB)

| Etapa | Antes | Agora | Como |
|---|---|---|---|
| Transcrição por região | ~4 min | **77 s** | `large-v3-turbo` (2,3x; mesmo texto em PT) |
| 2º passe do whisper por chunk + consertos | ~5 min | **0** | `chunks_from_regions.py` usa o passe por região |
| Corte do apresentador (`aroll`) | 291 s | **102 s** | VideoToolbox (hardware) + 3 takes em paralelo; PSNR igual |
| Folha de olhar | manual, recorte errado | **automática** | `gaze_sheet.py`: recorte do rosto pelo FaceLandmarker |
| B-roll em vídeo (recorte, câmera, bake) | ~10 min | **0** | tudo na camada de motion (fotos são `<img>` no GSAP) |
| Pesquisa de imagem | serial, API ruim | **em paralelo** com a fase 1 | navegador na fonte primária (docs/11) |
| SFX do motion | ~100 cues à mão | **automático** | cada componente chama `cue()`; `mg_cues.mjs` extrai |
| Render a 60 fps | ~17 min | **~13 min** | `render-par.sh`: 3 partes em paralelo. Frio rende o dobro (27 s/parte), mas o Air M4 sem ventoinha cai para ~44 s/parte sob carga contínua; 0.8.111 com 3 workers deu o mesmo (764 s × 793 s) |

## Os comandos (de dentro de `~/Claude/reel-auto/<slug>`)

```bash
zsh ~/Claude/KIT-EDICAO-REEL/novo-projeto.sh <slug> "Título"            # 1 s
zsh scripts/fase1.sh "<bruto>" <slug>          # FUNDO · ~5 min: mezanino + whisper turbo -> work/regioes.txt
#   em paralelo: pesquisa no navegador (fonte primária) + imagem a pedido no Codex (docs/11, docs/05 §23)
#   escrever: scripts/mkcut.py (SPLIT/DROP) · scripts/cuts.py (TAKES) · scripts/bipe.py (JANELAS, se houver palavrão)
zsh scripts/fase2.sh                           # FUNDO · ~5 min: cortes, J-cut, chunks, legendas, faixas, olhar
#   ler work/chunks.txt -> scripts/captions_fix_table.py -> zsh scripts/legendas.sh
#   ler gaze/me/g*.jpg -> janelas NÍTIDAS · ler work/tl-words.txt -> tempos de cada palavra
#   plano: sections (virada, CLIMAX, CTA), impacts (≤5; o 1º typing), ctaSeg, splitShiftY (medir)
#   scripts/slots.py (S, cobrindo as nítidas) · compositions/mg.html (CENAS com a biblioteca)
zsh scripts/montar.sh 13.4,16.8,...            # ~1 min: build + leaks + bed + SFX automáticos + check + snapshots
#   ler os snapshots, corrigir, repetir montar.sh
python3 scripts/size_sweep.py | head -3        # escolher o SIZE
zsh scripts/render-par.sh <SIZE> renders/<Nome>-reel-final.mp4    # FUNDO · ~13 min: 3 partes em paralelo + finalizar
#   conferir: quadros-chave, bipe no MP4, MD5 do bruto · mandar o MP4 no chat (SendUserFile)
```

## Escrevendo a camada (`compositions/mg.html`)
O modelo já traz o CSS de todos os componentes e a **biblioteca** (não mexer): `sceneIn/sceneOut`, `splitIn/splitOut`,
`whip`, `drop`, `zoomIn`, `pop`, `flip`, `rise`, `words`, `slam`, `chip`, `smear`, `stagger`, `bars`, `digits`, `rings`,
`kenburns`, `drift`, `cue`. Cada um com som chama `cue()` sozinho. As CENAS vão no fim, com tempos absolutos de
`work/tl-words.txt`. Markup de todas as peças: `exemplos/alan-mulally/mg.html`. Regras e armadilhas: `docs/13`.

- **Splits** (capa, pré-revelação, virada) também são da camada: `.scene` com `style="height:845px"` +
  `splitIn(id, t0, true)` no quadro 0 e `splitIn/splitOut` nas janelas seguintes (sincronizados com o arrasto).
  A caixa do gancho cobre 35–56% da tela: na capa, o assunto fica no terço de cima.
- Faixa das legendas livre (y≈1380–1540). Callout só onde o motion não diz a mesma coisa.

## Imagens: dosagem e capa
- **Abertura só com fotos, motion no meio** (docs/05 §24). Fotos de arquivo: NARA/LOC/Commons (`work/pesq/`), licença registrada.
- Capa a pedido no Codex: `codex exec -m gpt-5.6-sol --skip-git-repo-check --sandbox workspace-write "<cena>"` (~70 s, 1536×1024).
  Assunto na metade de cima (a caixa do gancho cobre 35–56%); pessoa-tema **de costas** se o nome ainda não foi dito.

## Refazer depois de um ajuste
Mudou a camada ou o plano → `zsh scripts/montar.sh <instantes>` → **apagar `renders/chunks/chunk-NN.mp4` das partes afetadas** (o
`render-par.sh` retoma e pula as que existem) → `render-par.sh` → conferir um quadro de cada trecho mudado no MP4.

## O que continua obrigatório (é o que garante o resultado)
Varredura de olhar (folhas) · `jcut_check.py` · bipe medido · QC por snapshot de cada cena · um quadro de cada fase
do render conferido · MD5 do bruto · sem foto de banco/marca d'água. Pular qualquer um = retrabalho.

## Máquina
`render-par.sh` usa P=3 (Mac 16 GB). Mac de 8 GB: `zsh scripts/render-par.sh <SIZE> <saida> 1` (= serial antigo).
`BAKE_X264=1` volta o aroll para x264. Disco: ≥ 6 GB livres antes do render.


---

# ARQUIVO: `docs/05-calibracoes-e-armadilhas.md`

# Calibrações travadas e armadilhas já pagas

Destilado dos 31 reels editados até 2026-10-01 (Casas Bahia → … → Kazuo Inamori): os 27 `EDICAO.md` dos
projetos e as notas de memória. **É a fonte única**: nada aqui precisa ser reconferido num projeto antigo.
Entre parênteses, o reel em que a regra nasceu — só para dar contexto; o texto do projeto está em
`arquivo-projetos/<slug>/`.

**Não recalcular, não re-perguntar, não "melhorar" sem o Fabio pedir.** Pedido explícito dele vence qualquer
número daqui — e vira regra nova (seção 22).

---

## 1. Números do formato

| Parâmetro | Valor | Observação |
|---|---|---|
| Palco | `#root` 1440×2560 com `#stage` 1080×1920 em `scale(4/3)` | toda medida (fonte, caixa, `splitShiftY`) continua na geometria 1080×1920 |
| Timeline / saída | timeline a **30 fps** · export **1440×2560 @ 60 fps** | `bake.py` tem dois fps (seção 17) |
| Velocidade | **1,1x** (`rate`) | "acelere 1.1" sobre o que já está a 1,1 → **1,21**; "só um pouquinho" → **1,15** |
| Duração | o roteiro manda (hoje ~90–100 s; os primeiros eram 50–60 s) | nunca cortar roteiro por conta própria |
| J-cut | `jcutLeadFrames` **9** · `jcutCrossfadeFrames` **3** | 9 = 5 quadros de FALA + ~4 de respiração (seção 7) |
| Folgas do corte | `HEAD_PAD` 0,20 · `TAIL_PAD` 0,13 · `TA` 0,12 · `HH` 0,15 | respiro mediano ~0,245 s entre falas |
| Split-screen | B-roll **44%** em cima / apresentador **56%** embaixo | transição de arrastar 0,55 s `power3.inOut` |
| `splitShiftY` | **medir em todo bruto** (já deu de 260 a 550) | olhos a ~49% da faixa do apresentador (seção 12) |
| Zoom do apresentador | `presenterZoom` 1,06 / 1,14 · `mode: scene` · `sceneMax` 4,5 · `origin` 50% 53% | uma troca por aparição |
| Ritmo | cenas de **3–5 s**; ~4 s é alvo **e** teto | `leakMinGap` **3,5** |
| Legenda | Montserrat **600 / 47 px**, branca, **sem contorno**, halo de 3 sombras | até 3 palavras, quebra em pontuação |
| Legenda — posição | **44%** sobre B-roll e dentro do split · **76%** com o apresentador sozinho | `capLowSegs` só vale sobre B-roll de tela cheia |
| Gancho = capa | frase inteira desde o quadro 0 · caixa **#FF4A1C** · **Oswald 700, caixa alta, 90 px** | seção 13 |
| Callout | Montserrat **800 / 76 px CAPS**, contorno 10 px, a **30%** (ou `top`) | ~5 por reel de 90 s; o 1º com digitação |
| Light-leak | 0,7 s, começa **10 quadros antes** do corte, `screen`, opacidade 0,85 | ~17–20 por reel de 90 s |
| CTA | push-in 1 → 1,05 a partir de `ctaSeg` | |
| Trilha | 0,079 → 0,045 (últimos ~9 s) → 0 (fade 0,7 s) | `trilhaLoop` se o reel passar de 164 s |
| Áudio final | `amix(voz-mix, bed)` + limiter a −1 dBTP · AAC 256 kb/s 48 kHz | `finalizar.py` |
| CLI | `hyperframes@0.8.64` fixo no `package.json` | o `render-chunks.mjs` chama `0.8.48` no render; é a combinação validada — não atualizar no meio de um reel |

### SFX (volumes exatos, todos no `bed.m4a`)
- intro `opening` **0,25** + `riser` **0,22**, de 0 a 3,2 s
- `boom-cinematic` em 4,8 s, **0,12**
- `drum-fill` em 7,0 s, **0,166** — suprimido quando o callout de digitação cai entre 5,5 e 9,5 s (dois drum-fills embolam)
- `drum-fill` do callout de digitação, **0,3**
- `whoosh` → `swoosh` → `whoosh-transition` alternados, **0,18**, um por light-leak
- `riser` **0,2** 3 s antes do clímax · `impact-hit` **0,3** na entrada do clímax (a seção cujo `name` contém "CLIMAX")

**Regra de ouro do mix:** nunca SFX rítmico contínuo (ticks, loop de batida) sobre fala densa — o Fabio reportou
como "áudio quebrado". One-shot curto nos cortes: sim. Cama rítmica sobre a voz: não.

---

## 2. Fluxo e comunicação com o Fabio

- **Parada única**, antes dos B-rolls. Nela tudo que mexe no tempo tem que estar travado e listado: duração,
  cortes, velocidade, J-cuts, palavrões bipados, varredura de olhar, primeira cena, B-rolls planejados por slot.
  Depois do "pode gerar as brolls" vai direto até o MP4 final, sem nova revisão. Só parar de novo se surgir
  decisão que só ele pode tomar (slot sem imagem aceitável, mudança de corte que não seja de olhar).
  *Por quê:* a 2ª parada só gerava pedido visual ou correção de tempo que devia ter saído na 1ª (Andy Grove,
  Reed Hastings, Herb Kelleher); cortar a 2ª economiza 15–25 min por vídeo.
- **Link do preview em toda parada**, em toda rodada de correção e na entrega do render:
  `http://localhost:<porta>/#project/<slug>`, clicável, no topo da mensagem. Subir com
  `npx hyperframes preview --background` e conferir com `curl` (o `--status` às vezes mente). *("onde está o
  link para eu ver o vídeo até aqui? Toda vez você esquece" — iPhone Duo.)*
- **O texto do prompt antigo está desatualizado em dois pontos** — aplicar o padrão atual e registrar no resumo,
  sem perguntar: "legendas amarelas dentro de uma caixa no gancho" = capa laranja; "J-cut de 5 frames" = 5
  quadros de fala com crossfade de 3. O prompt de `docs/04` já está corrigido.
- **Correção depois do render:** não muda o tempo (B-roll, texto, cor, volume) → refazer só as partes afetadas
  (~5–10 min). Muda o tempo (corte, velocidade, J-cut, ordem) → avisar que é render inteiro (~25–40 min) e fazer.
- Reportar sempre os segundos de leitura de roteiro que ficaram expostos, em vez de trocar o formato para zerar.
- Resumo de entrega: arquivo, duração, resolução, fps, validação, áudio, B-roll por slot, callouts, decisões.

---

## 3. A máquina: MacBook Air 8 GB / 228 GB

- **Serializar tudo que é pesado.** Whisper junto com encode do mezanino derrubou o `opendirectoryd`
  (Jocko Willink): `whoami` devolve `501`, o whisper morre no Metal, o Chrome morre no sandbox. Não há conserto
  por shell — só sessão nova (sair e entrar na conta basta). **Canário:** `sudo -n true` respondendo
  "you do not exist in the passwd database" → parar tudo e pedir relogin.
- Não engolir o stderr do loop de whisper: conferir `ls work/reg/*.json | wc -l` contra o número de regiões.
- **Disco:** ≥ 7 GB livres antes do render é o confortável. O render enche o cache de extração (~2,9 GB).
  `work/render-all.sh` põe o `TMPDIR` dentro do projeto e limpa a cada parte — rodou com ~2 GB livres.
  Apagar cache compartilhado do `$TMPDIR` do sistema foi negado pelo classificador de permissões: não tentar.
- **Render em segundo plano = tarefa de fundo do harness.** `nohup … &` dentro de uma chamada de shell morre com
  `render_cancelled_parent_exited`.
- **Parar o preview deste projeto antes do render** (RAM). Parar preview de *outro* projeto foi negado pelo
  classificador ("Interfere With Workloads"): pedir ao Fabio; com o "pode parar" dele passa.
- Glob no zsh numa pasta vazia aborta a lista `&&` inteira: usar `find … -delete`, não `rm -f pasta/*.mp4`.
- `make_broll.py` trabalha a 1,5x da saída: a 2x com foto de 4000 px o ffmpeg leva SIGKILL.
- O ffmpeg local **não tem `zscale` nem `drawtext`**.
- **Armazenamento:** finais e brutos ficam no servidor (`/Volumes/Company/Equipe/FABIO KENJI/`: `VIDEOS FINAL
  BACKUP/` com `_MD5.txt`, `VIDEOS BRUTOS BACKUP/`). Não estranhar a falta deles no Mac. Mover sempre conferindo
  MD5 antes de apagar o local. O share `Company` precisa estar montado.
- Chaves de API (`SERPER_API_KEY`, `FAL_KEY`) em `~/Claude/reel-auto/.env` — **nunca** vai para o kit, git ou servidor.

---

## 4. Mezanino e cor

- **Mezanino antes de tudo**, na resolução e fps do bruto (hoje 1440×2560 @60), BT.709 limited, `-g 30`.
  `scripts/mezanino.sh` decide o caso pelo `ffprobe`.
- **Quase todo bruto é SDR full-range** (`yuvj420p` / `color_range=pc`), não HDR. Sem converter
  full→limited (`scale=in_range=full:out_range=tv`) a cor **lava** — reclamação real.
- Quando for HDR do iPhone (HLG / `arib-std-b67`, BT.2020 10 bits):
  `colorspace=iall=bt2020:itrc=bt2020-10:all=bt709:format=yuv420p:dither=fsb`.
- **Conferir a cor por número**, bruto × mezanino em 3–4 pontos: média de luminância bate em ~1–1,5/255 e o
  desvio-padrão fica igual. Desvio caindo = lavou.
- **`-g 30 -keyint_min 30 -sc_threshold 0` em TODO arquivo gerado** (mezanino, `aroll`, cenas, B-rolls): sem GOP
  denso o render avisa `sparse keyframes … causes seek failures and frame freezing` e a captura trava (Costco).
- Bruto **nunca** alterado: MD5 antes e depois, registrado no `EDICAO.md`.
- Voz sempre em `.m4a` dedicado: `<audio src="*.mp4">` de vídeo não toca no Studio.

---

## 5. Transcrição

- **Nunca whisper no arquivo inteiro** (alucina em loop). `silencedetect -35dB / 0,35 s` → regiões →
  `whisper-cli large-v3 -l pt --max-context 0 -ml 1 -sow` **por região** → `work/region-words.json`.
- O passe por região serve para escolher takes, achar palavrão e ancorar o tail na última palavra.
- Depois dos cortes: **1 chunk por take** (± 0,3 s) → whisper por chunk, do **áudio limpo** (`full-clean.wav`).
- **O passe por chunk falha nas bordas**: vaza a palavra do take vizinho, alucina ("Obrigado", "E aí",
  "Sensacional!") e às vezes **colapsa** várias palavras no mesmo timestamp (`to <= from`). Conserto:
  `rebuild_chunk.py ch:regiao` reconstrói o chunk a partir do passe por região. Nos reels recentes quase todos
  os chunks foram reconstruídos (Sun Tzu 14, Kazuo 40 de 41). Guardar o passe cru em `work/chunks-raw/`.
- Depois de reconstruir, **rever os DROP daquele chunk**: o chunk vindo da região não tem a palavra vazada e o
  DROP antigo passa a comer palavra boa (IKEA).
- Ordem fixa: whisper → `align.py` → `fix_captions.py`. O `align.py` ignora as palavras DROP e limita o encaixe
  em `aout` (a voz do take): sem isso jogava "Terra." do gancho para fora da voz (Taiichi Ohno).
- `fix_captions.py` é idempotente (parte sempre de `work/chunks-aligned/`). Para refazer do zero depois de novo
  `align.py`: apagar `work/chunks-aligned/chNN-words.json`.
- Palavra fraca pode cair **entre regiões** do `silencedetect` ("perdi **tudo**", Mike Michalowicz): quando os
  passes discordam, conferir de ouvido com whisper em recortes.

### Texto da legenda
- Erro de **grafia/pontuação/maiúscula** do whisper → vale o roteiro ("pra", "pro", "tá", números por extenso
  como no roteiro, nomes como no roteiro: "Jocko", "Herb", "Taiichi").
- Onde o **áudio diz outra coisa** (passe por região, por chunk e com o roteiro no `--prompt` concordam) → vale
  o áudio. Registrar no `EDICAO.md` o que divergiu do roteiro.
- Legenda da palavra bipada: `M****`, `P****` (palavra inteira bipada) — entra junto com o bipe (`FIXT`).

---

## 6. Cortes e takes

- **Frase ou take repetido: fica sempre o ÚLTIMO válido.** Falso início sai inteiro. Varrer a transcrição
  toda, inclusive o que parece ruído.
- "porque você… é demais" com pausa dramática é **um take só**, não repetição.
- Regiões descartadas continuam em `regions_cut.json`: o `cuts.py` usa as vizinhas para achar o silêncio real.
- **Dividir fala longa nos vales reais** (`valleys.py`, −38 dB, ≥ 0,16 s) dá ritmo de corte e janelas de B-roll.
  Não dividir quando o silêncio real é < ~120 ms (o crossfade cairia sobre a palavra — Costco).
- **Head:** onset por RMS (20 ms, −27 dB, 4 de 8 janelas), recuando até o piso, − `HEAD_PAD`.
- **Tail:** `min(fim da última palavra, offset RMS a −45 dB)` + trava: enquanto o nível ≥ −35 dB, avança.
  Nunca por RMS sozinho (decepa "loja", "pessoas") nem por piso sozinho (deixa ~1 s de respiração — IKEA) nem
  por whisper sozinho (estoura além do áudio).
- **Pausa curta** entre dois takes: emenda no silêncio real; se o crossfade de 3 f cabe na pausa, a emenda vai
  logo antes da fala nova (`in = on − XF − 5 ms`, `aout = in`) — "piloto | foi grosso", Herb Kelleher.
- `FORCE_IN` / `FORCE_OFF` no `cuts.py` para a borda em que a respiração seguinte fica acima do piso.
- **Sem clamp no `mkchunks.py`**: com `out = aout + lead`, em takes contíguos o clamp comia o lead e cortava
  14–75 ms da palavra final (Reed Hastings).
- O **gancho** tem que ser a primeira frase inteira: juntar regiões se preciso e, se o take trouxer a 2ª frase,
  dividir no vale para a capa ter só a 1ª.
- `ctaSeg` é o encerramento real: quando o "já me segue" vem no começo do roteiro, o push-in vai para a pergunta final.
- Recuperar palavra engolida colando a sílaba de outro take só sob B-roll (sem lip-sync a respeitar) —
  `se_splice.py` (David Marquet) é o molde.
- Depois de mudar corte ou velocidade com B-rolls já posicionados: remapear os tempos pelo mesmo quadro do
  bruto (`remap_tl.py`, plano antigo em `work/v1/`) e refazer chunks + `fix_captions.py` (os índices mudam).

---

## 7. J-cut

- **Voz emendada ponta a ponta**, nunca duas vozes somadas: a voz do take termina em `aout` (fim da fala +
  0,12) e a do seguinte começa em `in` (início da fala − 0,15), com crossfade de **3 quadros dentro do
  silêncio**. O **vídeo** segura o lead depois do `aout` (`out = aout + lead × rate`). *("as J-cuts não ficaram
  tão boas" — Atul Gawande.)*
- **O lead conta da PRIMEIRA PALAVRA**, não do início do clipe: o clipe de voz começa 0,15 s de source antes da
  fala; com `jcutLeadFrames` 5 a palavra entrava só 0,9 quadro antes do corte — J-cut invisível. Por isso **9**
  (= 5 + `HH`/rate em quadros). *("foque um pouco mais no j-cut" — Reed Hastings.)*
- Crossfade de 5 quadros não cabe no silêncio e come até 76 ms da palavra final: **3** (André Esteves).
- **Sempre validar por dados** antes de fechar: `python3 scripts/jcut_check.py` → 0 buracos, nenhum crossfade
  sobre fala, lead de fala ~5 quadros, respiro mediano ~0,245 s.
- **L-cut (`videoTail`)**: só quando o pré-rolo do próximo take já está **falando**. Pré-rolo mudo > ~0,3 s lê
  como imagem congelada (Localiza). Quando o roteiro é lido de uma tacada (takes contíguos no source) o L-cut é
  **estruturalmente inútil** — recuar o início mostra os mesmos quadros do desvio. Na prática: todo desvio de
  olhar se resolve com cobertura de B-roll.

---

## 8. Legendas na tela

- Branca **sem contorno**: some sobre fundo claro. Escurecer o B-roll (`dim` no `make_broll.py`, 0,08–0,35;
  negativo clareia) em vez de mexer na legenda.
- `capLowSegs` decidido **olhando snapshot por snapshot**: legenda a 44% em cima de rosto, logotipo, título de
  livro, mostrador → desce para 76%. Só vale sobre B-roll de **tela cheia**; dentro do split fica sempre na
  divisa (a 76% cai na boca do apresentador — Herb Kelleher).
- Legenda que cruza o corte para um B-roll: conferir os dois lados.

---

## 9. Bipe de censura

- **Varrer a transcrição INTEIRA atrás de palavrão antes da parada** (inclusive takes descartados) e conferir
  ouvindo. *("a palavra PORRA deu para escutar" — Reed Hastings.)* Bipar também palavra com risco de bloqueio
  no Instagram quando ele pedir ("mortes" — Atul Gawande).
- **Padrão atual: a palavra INTEIRA**, da 1ª consoante ao fim do decaimento. (Os primeiros eram "MER—" + bipe;
  o Fabio passou a pedir a palavra toda: "ainda dá para escutar".)
- **Onde:** gravado dentro de `assets/<slug>-voz.m4a` (`bipe.py`), 1 kHz, fade de 6 ms, ~1 dB acima da frase.
  O filtro `sine` do ffmpeg sai a −18 dBFS, não a 0. `work/full.wav` leva o bipe (senão o tail do take o deixa
  de fora); a transcrição sai de `work/full-clean.wav` (com o bipe o whisper alucina).
- **Achar a janela:** o whisper erra ~0,4 s dentro da região e o envelope sozinho não diz qual sílaba é qual
  (o vale que parecia o /d/ era o /p/ — Mike Michalowicz). Mapear as sílabas com **whisper em recortes
  cumulativos do áudio limpo** e pelo espectro (nasal /m/ = energia < 400 Hz; oclusão = vale).
- **Aceite por medição na `voz-mix.m4a`:** ~100% da energia em 950–1050 Hz e ~0% fora de 900–1100 Hz na janela.
  O "p***" do whisper **não** serve de juiz para palavrão previsível: com a palavra trocada por silêncio puro
  ele ainda escreve "uma merda" (Sun Tzu). Rodar o controle do silêncio antes de confiar nele.
- **Imagem:** de preferência o apresentador em tela cheia (a boca sob o bipe lê como censura). Mas se ele lê o
  roteiro naquele trecho, **a regra do olhar vence** e o bipe fica sob B-roll.

---

## 10. Varredura de olhar

**O apresentador lê o roteiro olhando para o lado ou para baixo** no começo e no fim de quase todo take, e às
vezes no meio. No vídeo final ele tem que aparecer olhando para a câmera. Fase obrigatória, feita **duas
vezes**: com os B-rolls em placeholder e de novo com os B-rolls reais.

1. **Medir na timeline:** `gaze_tl.py` (FaceLandmarker, blendshapes, 30 amostras/s) → `gaze_windows.py`
   (`|side − mediana| > 0,17` ou `down − mediana > 0,11`, sem piscada, ≥ 0,15 s).
2. **Se ele gravou de perto e mexe a cabeça:** os blendshapes medem o olho *dentro da cabeça*, e quem olha para a
   lente compensa o giro com o olho — a maioria das janelas vira falso positivo. Usar `gaze_pose.py` (regressão
   contra yaw/pitch; o resíduo é o desvio real; 2σ). Kazuo: 40 janelas / 19,5 s → 19 / 5,4 s.
3. **Conferir nas folhas**, sempre: `gaze_review.py`, `vw_tl.py`, `vw_eyes.py`, `vw_big.py`. O medidor é pista,
   não veredito — piscada, pálpebra baixando, sorriso e aceno passam do limiar. **O recorte dos olhos tem que
   ser medido por bruto** (o enquadramento muda).
4. **Triar** em nítidas / de fronteira de take × sutis. Desenhar o layout contra as **nítidas**; conferir as
   sutis expostas em tamanho grande.
5. **Cobrir** com B-roll de tela cheia. Desvio dentro de janela de split não tem conserto por corte: vira
   cutaway ou fica. Pálpebra já baixando 2 quadros antes: adiantar a janela do B-roll.
6. **2ª passada com os B-rolls reais**, nos quadros da **composição** (snapshots das bordas de cada aparição do
   apresentador), não só no mezanino.
7. Registrar e reportar: janelas, segundos, **leitura exposta em segundos**.

Histórico dos medidores (ainda no modelo, úteis em casos específicos): `gaze_measure.py` + `gaze_report.py`
(íris, só desvio lateral: `gx ≤ −0,055` = leitura; `gx` positivo com yaw subindo = cabeça virada, olho na
lente) · `gaze_bounds.py` / `gaze_pairs.py` (fronteiras de take) · `gaze_down.py` / `gaze_lids.py` /
`gaze_blend.py` (olhar para baixo).

---

## 11. Layout de cenas e ritmo

- **"A cada 4 segundos no máximo precisa de um efeito ou B-roll"** (André Esteves) — e depois: **"ficaram muitas
  brolls… o intervalo está muito curto"** com tomadas de 0,7–2 s (Dan Martell). Resultado: cenas de **3–5 s**,
  zoom do apresentador **uma vez por aparição**, `leakMinGap` 3,5. Auditar com `ritmo.py` (maior intervalo sem
  evento ~4–4,7 s).
- **Todo corte precisa de transição**: light-leak + whoosh em corte de seção, entrada e saída de cena **e nos
  cortes internos** de cena concatenada. *("só uma broll sem transição, sem nada".)*
- Duas tomadas parecidas (mesma foto reenquadrada, dois interiores iguais) contam como "parado": alternar
  assunto, escala e luminosidade.
- **A primeira cena é sempre split** (capa: B-roll em cima, ele embaixo, caixa laranja), mesmo com olhada no
  gancho: split curto de capa → cutaway de tela cheia cobrindo a olhada → split volta com a transição de
  arrastar. Reportar os décimos expostos dentro da capa. *("a primeira cena precisa ser a tela dividida como em
  todos os outros vídeos" — Reed Hastings.)*
- Estrutura do formato: intro em split (pré-revelação) → revelação → cutaways do corpo → **2º split na virada**
  → clímax emocional → CTA no apresentador.
- O intro split **não precisa** ocupar os ~10 s inteiros. CTA "já me segue" dentro da intro vai com o
  apresentador em tela cheia, sem B-roll — escolha do Fabio (IKEA).
- **`cenas_opt.py`** (DP que minimiza leitura exposta com cenas de 2,5–5 s) é ponto de partida. Com muitas
  janelas ele engole os splits (`WBS` baixo) ou expõe leitura dentro deles (`WBS` alto): nesse caso **desenhar
  o layout à mão** sobre as nítidas (`work/layout-exemplo.py` → `slots.py`). `FIRST=('S',0.0)`; `ONLYP` no bipe
  e no fim do CTA; `ONLYB` na revelação e no clímax.

---

## 12. Split-screen

- `splitShiftY` **se mede, não se copia** — já deu 260, 312, 352, 362, 365, 375, 390, 400, 410, 412, 422, 424,
  432, 435, 436, 438, 439, 442, 470, 535, 550. Com o valor errado os olhos caíam a 29% da faixa (Costco).
- Medir a altura dos olhos no `aroll`/mezanino (FaceMesh: média do `y` dos landmarks 33/133/362/263) em vários
  pontos **dentro das janelas de split**; aplicar o zoom
  (`y_zoom = origem + (y_olhos − origem) × escala`); alvo: olhos a **~49% da faixa do apresentador** (a faixa vai
  de 845 a 1920 → y ≈ 1377 na geometria 1080×1920); `splitShiftY = 1377 − y_zoom`.
- Para medir sem B-roll: `slots.py --placeholders`, build, snapshot. Conferir no snapshot antes de fechar.
- No split o cover-crop mostra só 44% da altura: assunto fora da faixa → `objectPosition`, ou gerar o split da
  foto 4:3 inteira.

---

## 13. Gancho = capa

- O **quadro 0 é a capa do reel**: frase inteira do gancho já na tela, sem animação de entrada. Conferir sempre
  o snapshot em t=0.
- Caixa laranja **#FF4A1C** (gradiente, borda branca, glow), **Oswald 700 em caixa alta, 90 px**, caixa de
  1016 px (margem ~32 px), contorno 12 px + sombra dura, pulso **1,018** (a 1,035 a caixa larga vaza da tela),
  brilho atravessando duas vezes. Sem `text-wrap: balance`.
- A caixa cobre ~35–56% da altura: o assunto do B-roll de capa tem que ficar **acima** dela (gerar o split da
  imagem 4:3 inteira; recompor a foto se a caixa tapar o assunto).
- Para voltar à caixa amarela antiga: `"hookSeg": null` + `"yellowCapSegs": [0]`.

---

## 14. Marca só depois do áudio

- **Nada que identifique a empresa/pessoa antes de o áudio dizer o nome pela 1ª vez** — logo, letreiro, rosto,
  livro, produto. Quando o tema é uma pessoa, o gatilho é o nome dela, e a empresa dela entra junto.
  *("não coloque nenhuma imagem… antes do áudio falar o nome da empresa pela primeira vez" — Localiza2.)*
- Achar o instante pela palavra (`tl.py --words`). A revelação entra **2 quadros depois** do início da palavra:
  no quadro exato a emenda arredonda e a marca vaza 1 quadro antes.
- Pré-revelação: material real do tema **sem marca** (recorte abaixo do totem, interior, detalhe) ou cena
  genérica do assunto. Concessionária/loja genérica não serve se traz logo de outra marca.
- Conferir com snapshots da faixa pré-revelação + fronteira; registrar último quadro limpo e primeiro com marca.

---

## 15. Callouts

- 1º callout: **digitação** (caracteres um a um em ≤ 1,35 s) + drum-fill + pulso de settle. Demais: `popIn`
  `back.out(2.4)`, rotação −5°, grow 1,07, saída 0,22 s. Sempre `tl.set autoAlpha 0` no fim (linter de seek).
- `impacts[].seg` prende o callout ao segmento (sem isso dispara em toda repetição da frase).
- `impacts[].top` quando o B-roll tem rosto/assunto na faixa dos 30%. Callout branco some em fundo branco:
  trocar a imagem. Callout que cobre os olhos de um retrato: tirar o callout.
- Callout estourando com o apresentador em tela cheia leva punch-in 1,07.

---

## 16. B-roll

### Pesquisa (detalhe em `docs/11`)
- Fotos **reais** do tema, que casem com a fala do trecho. Prioridade: sala de imprensa / site oficial →
  Wikimedia Commons → Google Imagens em tamanho grande. Lado menor ≥ ~900 px. Banco de imagens fica de fora.
- **Nunca IA generativa por conta própria.** Imagem encenada só quando o Fabio **descreve** a cena: `fal_img.mjs`,
  `fal-ai/nano-banana-pro`, 4:3, mostrar na parada, marcar "gerada a pedido" no PESQUISAS-BROLL.
- **Subagente de pesquisa:** proibir no prompt e-mail/nome do usuário em User-Agent, headers, URLs ou payloads
  (usar UA genérico de Chrome); limitar a ~3 consultas por trecho e exigir os JSON antes de ampliar. Se travar
  ("stalled"), não retomar: fechar à mão pelas folhas do `g_index.json`.
- Licenças: registrar a fonte de cada foto. CC BY-NC e "direitos reservados" são pendência para o Fabio decidir.

### Geração (`entrega.py` → `make_broll.py`)
- **Só a câmera se move** sobre a foto: texto, logotipo e marca ficam idênticos ao original.
- Tela cheia 1440×2560, split 1440×1128, 60 fps, cada arquivo = janela + 0,1 s (`rate` 1,0 — `< 1` reprova no
  gate de cobertura; câmera lenta se grava no arquivo).
- Foto pequena ou assunto largo demais: `fill` 1 (foto inteira sobre fundo borrado) ou 2 (fundo liso, para foto
  de estúdio); não ampliar mais que ~1,4x. Pré-recorte lateral para a foto ocupar mais tela.
- Letreiro/capa que ocupa a largura: **pull-out** terminando com o texto inteiro, ou estático. Zoom-in decepa.
- Normalizar rotação EXIF antes (o `ffprobe` não aplica, o `ffmpeg` aplica — o recorte sai deitado).
- Vídeo entregue pelo Fabio (`broll1.mp4`): **velocidade normal, mudo**, só normalizado (`norm_broll1.py`).
  Esticar foi reprovado (0,63x — IKEA). Os cortes internos dele dão o ritmo.
- QC com folha início/meio/fim de cada tomada.

---

## 17. Composição leve (faixas pré-renderizadas)

- **Nunca passar de ~10 elementos de mídia; light-leak também conta.** Cada `<video>`/`<audio>` é um player e
  uma sessão de decodificação: com 164 (André Esteves) e depois com 57 (Dan Martell) o B-roll sumia e a tela
  ficava preta **só no Chrome do Fabio**. O headless mostra tudo certo — snapshot OK **não prova** o preview.
- `bake.py` gera: `aroll.mp4` (corte do apresentador), `voz-mix.m4a` (J-cut), `bed.m4a` (trilha + SFX),
  `_cenaNN.mp4` (tomadas seguidas), `broll-full.mp4` (todas as cenas de tela cheia), `leaks.mp4`.
  Flags no plano: `bakedAroll`, `bakedAudio`, `bakedBroll`, `bakedLeaks`.
- **Rodar `bake.py` depois de toda mudança** de corte, velocidade, SFX ou B-roll (só B-roll:
  `bake.py cenas brollfull leaks bed`).
- Armadilhas do bake: `setpts=PTS/rate,fps=N` (com `-r` o conteúdo atrasa 2 quadros dentro do take) · fronteiras
  por **quadro acumulado** · `setsar=1` antes do `concat` · **dois fps**: `TLFPS` = `plan.fps` (30) para a
  matemática da timeline, `FPS` = 60 para os quadros do arquivo (com 60 nos dois: 1,9 s de dessincronia) ·
  conferir a linha `aroll.mp4 N quadros (timeline N)` · estado inicial escondido em **CSS**, não `tl.set` em 0 ·
  conteúdo de cada cena de `floor(t0·60)` a `ceil(t1·60)`.
- Zoom do apresentador por `tl.set` num wrapper, nunca duplicando `<video>`.
- Testar **tocando** no Studio, não só com seek. Servidor serial (`python3 -m http.server`) dá falso positivo.

---

## 18. Export em partes (detalhe em `docs/12`)

- Render direto trava ("Sequential screenshot capture stalled") e com vários workers o Mac reinicia.
  `render-chunks.mjs`: 1 worker, `--no-best-effort`, `--video-frame-format jpg`, **sempre `--sdr`**.
- **Tamanho da parte por varredura** (`size_sweep.py`): só sobre os `<video>`, incluindo os pedaços do
  `--split`; sobra mínima ≥ ~15 quadros. **Não desligar o gate de cobertura.**
- **Todas as partes em `--split 3`** (sessão nova do Chrome por pedaço): zero falha desde o Reed Hastings.
  O limite de quadros por sessão não é fixo (travou em 530, 572, 318).
- `--fps 60` e o mesmo `--size` em tudo. A soma dos quadros das partes tem que ser a timeline.
- Áudio: `amix(normalize=0)` + `alimiter=limit=0.891:level=disabled`. Mux **sem `-shortest`**, com `-frames:v`.
- QC: 0 trechos pretos, pico ~−1 dB, quadros = timeline, bipe presente, quadros-chave iguais ao preview,
  sincronia boca/voz com lag mediano 0 ms (`sync-check.mjs`), MD5 do bruto igual.

---

## 19. Preview

- `npx hyperframes preview --background`; conferir com `curl`; as portas mudam (3002, 3003, 3005…); matar
  zumbi com `lsof` só deste projeto.
- O Studio reescreve o `index.html` ao salvar (`data-hf-id`, `<br>`): normal, o build seguinte regenera.

---

## 20. Regra de ouro do trabalho

**Nunca editar o `index.html` à mão.** Tudo sai de `assets/edit-plan.json` (e dos scripts POR VÍDEO) por
`build-edit.mjs` + `bake.py`. Mudou algo: plano → build → bake → `npm run check` (0 erros; avisos de track
densa são normais).

---

## 21. O que NÃO fazer (lista curta)

Whisper no arquivo inteiro · tail por RMS · crossfade de 5 quadros · duas vozes somadas no J-cut · copiar
`splitShiftY` · L-cut com pré-rolo mudo · abrir em tela cheia · marca antes do nome · esticar vídeo do Fabio ·
IA sem ele pedir · `-shortest` no mux · `alimiter` sem `level=disabled` · desligar o gate de cobertura ·
`nohup &` no render · whisper junto com encode · editar `index.html` à mão · parar sem o link do preview ·
confiar só no snapshot para o preview · confiar no "p***" do whisper · e-mail do Fabio em requisição.

---

## 22. Como este documento cresce

Todo reel termina com a seção "Lições para o kit" do `EDICAO.md` do projeto. Cada item entra **aqui** (regra +
porquê + reel) e, se mexeu em script, em `modelo-projeto/scripts/` — com `git commit` no kit. É isso que
dispensa abrir projeto antigo.

---

## 23. Padrão novo: camada de motion graphics (reel Alan Mulally, 2026-10-02 — "ficou perfeito")

- **O que cobre o apresentador é motion, não foto genérica.** Trecho conceitual (processo, número, gráfico) vira
  UI animada na sub-composição `compositions/mg.html`; foto real entra como card. Light-leak só nas trocas de seção.
  Detalhe, componentes e armadilhas: `docs/13-camada-motion.md`. *(pedido: "mesmo formato, mas com transições,
  imagens e motion graphics melhores, mais dinâmico com a mesma essência".)*
- **Trilha e SFX fixos do formato continuam todos**; os SFX do motion entram por cima (`mg_sfx.py`, depois do
  `bake.py bed`), impactos ≤ −16 dB para a voz ficar na frente. *(pedido explícito do Fabio/usuário.)*
- **Pesquisa de imagem pelo navegador na fonte primária** (sala de imprensa, site, Instagram, Wikipedia,
  `hyperframes capture`), não por API de busca — docs/11. Busca por API trouxe 3 fotos de banco/marca d'água em 22.
- **`render-chunks.mjs` precisa deslocar a timeline das sub-composições** por parte (corrigido no modelo): sem isso
  a camada aparece no preview e some no MP4.
- Capa: a caixa do gancho cobre 35–56% da tela até o fim do gancho também sobre o B-roll de tela cheia que entra
  antes dele terminar (s02 do Alan Mulally) — recompor a foto com o assunto abaixo da caixa.
- Imagem a pedido também pode sair do **Codex**: `codex exec -m gpt-5.6-sol --skip-git-repo-check --sandbox
  workspace-write "<prompt>"` (~70 s, paisagem 1536×1024). O modelo padrão do config pode ser recusado no login
  ChatGPT: passar `-m`.
- Máquina com 16 GB: o render serial em partes continua correto, só conservador; medir antes de afrouxar.
- Entrega: mandar o MP4 no próprio chat (`SendUserFile`), além do caminho.
- **Mundo claro da camada precisa de "chão" escuro** abaixo de ~64% da tela: legenda branca a 76% sobre cena clara reprova no
  contraste do `check` e some no vídeo. Já está no `.light` do modelo (reel Deming).
- **`.tag` sem quebra de linha** (`white-space: nowrap`, no modelo): tag longa quebrava em 2 linhas e cobria o vizinho (reel Deming).
- **Fonte primária atrás de Cloudflare** (deming.org, loc.gov) mostra "Um momento…" no navegador do app: não contornar. Cair para o site
  institucional (ex.: JUSE para o Prêmio Deming) + Wikimedia Commons (API com pausa de ~4 s entre buscas; sem pausa dá HTTP 429).
- **`render-par.sh` retoma**: pula toda `renders/chunks/chunk-NN.mp4` que já existe. Depois de mudar a camada/plano, **apagar as partes
  afetadas antes** (ou todas). No Deming v2 ele reaproveitou as 14 partes da v1 ("partes em 0s") e o MP4 saiu igual à v1 com QC OK —
  só um quadro conferido revelou. Parte k cobre `[k·SIZE, (k+1)·SIZE)` quadros a 60 fps.

## 24. Dosagem: imagem primeiro, motion só onde conta a história (reel Deming v2, 2026-10-02)

Pedido do usuário depois da v1 do Deming (camada com UI em quase todo trecho): *"diminuir um pouco os motion graphics e colocar mais
imagens; os primeiros segundos e o início, o ideal é manter como era, só com imagens, e depois pode animar"*. Virou regra:

- **Abertura (split da capa + pré-revelação) = só fotos.** Capa → fotos reais/de arquivo com Ken Burns e corte por chicote/queda.
  Nada de etiqueta, crachá, carimbo ou UI por cima. O callout de digitação do formato continua.
- **No corpo, foto real é o padrão.** Trecho que *dá* para mostrar com foto (pessoa, lugar, objeto, situação: "três vendedores",
  "ranking de funcionário", "almoço", "linha de montagem") vai de **foto de arquivo** (NARA / Library of Congress / Commons, domínio
  público ou CC) em tela cheia, no máximo uma etiqueta.
- **Motion só onde ele carrega a história:** título de capítulo (chip PASSO N + título), número que precisa ser visto (94 de 100,
  1 em cada 5), o mecanismo do clímax (a caixa, a pá, o placar), o objeto que a fala nomeia e não existe em foto (o cartaz com a
  frase exata). Regra prática: **≤ ~40% do tempo de cobertura em UI animada**; o resto é foto ou apresentador.
- Gráfico que só repete a fala ("não diminuía") → apresentador em tela cheia (respira o ritmo).


---

# ARQUIVO: `docs/13-camada-motion.md`

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


---

# ARQUIVO: `docs/01-pipeline-hyperframes.md`

# Pipeline — do bruto ao MP4 (estado de 2026-10-01)

O fluxo como ele é feito hoje, fase a fase, com os comandos. Os números e os porquês estão em `docs/05`; o
catálogo dos scripts em `docs/10`. Tudo roda de dentro da pasta do projeto (`~/Claude/reel-auto/<slug>`).

```
bruto ─► mezanino + voz ─► transcrição por região ─► bipe ─► takes/cortes ─► chunks + legendas
      ─► plano + build + bake ─► varredura de olhar ─► layout + placeholders ─► pesquisa de B-roll
      ─► ■ PARADA ÚNICA ■ ─► B-rolls reais ─► 2ª varredura + QC ─► render em partes ─► finalizar ─► entrega
```

Três regras que atravessam tudo: **nunca editar `index.html` à mão** · **uma tarefa pesada por vez** (Air de
8 GB) · **o bruto nunca é alterado**.

---

## Fase 0 — Projeto

```bash
zsh ~/Claude/KIT-EDICAO-REEL/novo-projeto.sh <slug> "Título"
cd ~/Claude/reel-auto/<slug>
```
Cria o projeto a partir de `modelo-projeto/` + `assets-fixos/` (scripts, template, fontes, SFX, trilha,
light-leak, modelo do FaceLandmarker). Os scripts **POR VÍDEO** vêm com os dados do reel Kazuo Inamori como
exemplo e são reescritos ao longo das fases (lista em `docs/10`).

## Fase 1 — Mezanino e voz  *(sozinho, sem nada pesado em paralelo)*

```bash
zsh scripts/mezanino.sh "$HOME/Claude/videos-brutos/<Bruto>.MP4" <slug>
```
Gera `assets/<slug>-2560-sdr.mp4`, `assets/<slug>-voz.m4a`, `work/<slug>-voz-limpa.m4a`, `work/full.wav`,
`work/full-clean.wav`, `work/md5-bruto.txt` e imprime a conferência de cor (média/desvio bruto × mezanino).

## Fase 2 — Transcrição por região  *(só depois que o mezanino terminou)*

```bash
python3 scripts/regions.py            # silencedetect -35dB / 0.35 -> work/regions.json
python3 scripts/mkreg.py              # um wav por região -> work/reg/
zsh scripts/whisper_regs.sh           # whisper large-v3 por região; imprime json/wav no fim: os números têm que bater
python3 scripts/regwords.py           # work/region-words.json + o texto de cada região
```
Ler o texto das regiões contra o roteiro: takes repetidos, falsos inícios, palavrões.

## Fase 3 — Bipe  *(se houver palavrão; antes dos cortes)*

Mapear a palavra (whisper em recortes cumulativos + envelope/espectro), preencher `JANELAS` em
`scripts/bipe.py` e rodar. Ele grava o bipe em `assets/<slug>-voz.m4a` e em `work/full.wav`. Aceite por medição
depois do `bake.py voz` (docs/05 §9).

## Fase 4 — Takes e cortes

```bash
python3 scripts/valleys.py 8.2 15.5 …   # vales de silêncio perto dos pontos onde uma região deve ser dividida
python3 scripts/mkcut.py                # SPLIT/DROP  -> work/regions_cut.json + region-words-cut.json
python3 scripts/cuts.py                 # TAKES       -> work/segs.json (in, out, aout de cada take)
python3 scripts/plan_segments.py        # copia os takes para `segments` do edit-plan.json
```
`cuts.py` lê `rate` e `jcutLeadFrames` do plano (o esqueleto já vem com 1,1 / 9 / 3).

## Fase 5 — Chunks e legendas

```bash
python3 scripts/mkchunks.py             # 1 chunk por take -> assets/chunks/chNN.wav + meta.json
zsh scripts/whisper_chunks.sh           # palavra a palavra por chunk
mkdir -p work/chunks-raw && cp assets/chunks/ch*-words.json work/chunks-raw/
python3 scripts/rebuild_chunk.py 3:5 7:9+10 …   # chunk:região_cut — onde o passe por chunk vazou/alucinou/colapsou
python3 scripts/align.py                # reancora os tempos na energia real
python3 scripts/fix_captions.py         # aplica scripts/captions_fix_table.py (FIX / DROP / FIXT)
```

## Fase 6 — Plano, build e faixas

Preencher no `assets/edit-plan.json`: `sections` (cortes de seção; a do clímax com "CLIMAX" no nome), `impacts`
(callouts; o 1º `style: typing`), `ctaSeg`, `hookSeg`.

```bash
node scripts/build-edit.mjs             # index.html + work/mix-plan.json + work/broll-groups.json + work/leaks.json
python3 scripts/bake.py voz bed aroll   # faixas prontas
python3 scripts/jcut_check.py           # 0 buracos · nenhum crossfade sobre fala · lead de fala ~5 quadros
python3 scripts/tl.py --words           # timeline de cada take e de cada palavra (acha a 1ª menção do nome)
```

## Fase 7 — Varredura de olhar (1ª passada) e layout

```bash
python3 scripts/gaze_tl.py && python3 scripts/gaze_windows.py     # janelas de leitura na timeline
python3 scripts/gaze_pose.py 2.0                                  # se ele mexe muito a cabeça: resíduo olho × pose
python3 scripts/gaze_review.py                                    # folhas de conferência -> gaze/rev/
python3 scripts/vw_eyes.py gaze/duvida.jpg 8.27 27.72 …           # zoom nos pontos em dúvida
python3 scripts/cenas_opt.py                                      # ponto de partida do layout (ou à mão)
python3 scripts/slots.py --placeholders                           # S/NOMES -> plan.broll com cartões rotulados
node scripts/build-edit.mjs && python3 scripts/bake.py cenas brollfull leaks bed
```
Depois: medir o `splitShiftY`, conferir a capa em t=0 e o ritmo (`python3 scripts/ritmo.py`), `npm run check`.

## Fase 8 — Pesquisa de B-roll

Ferramentas em `work/pesq/` (docs/11). Saída: candidatas em `work/pesq/cand/`, `candidates.json`,
`picks.json` e o arquivo `PESQUISAS-BROLL-<TEMA>.md` (`scripts/pesquisa_md.py`).

## ■ PARADA ÚNICA

Preview no ar (`npx hyperframes preview --background`), **link no topo da mensagem**, e a lista do que trava o
tempo: duração · cortes · velocidade · J-cuts · palavrões e bipe · varredura de olhar · primeira cena ·
B-rolls por slot. Não gerar B-roll antes da resposta.

## Fase 9 — B-rolls reais

```bash
python3 scripts/entrega.py              # PK: foto por slot + recorte -> assets/broll-src/entrega/
python3 scripts/make_broll.py           # S: movimento de câmera por slot -> assets/broll/   (--only sNN regera um)
python3 scripts/slots.py --real
node scripts/build-edit.mjs && python3 scripts/bake.py cenas brollfull leaks bed
npm run check
```
Com os snapshots: definir `capLowSegs` e `impacts[].top`, conferir a revelação quadro a quadro (último limpo /
primeiro com marca), a capa, o ritmo, e fazer a **2ª varredura de olhar** nos quadros da composição.

## Fase 10 — Export

```bash
python3 scripts/size_sweep.py                         # escolhe o --size (sobra mínima de clipe por pedaço)
npx hyperframes preview --stop                        # libera RAM
zsh work/render-all.sh <SIZE>                         # COMO TAREFA DE FUNDO do harness; retoma de onde parou
python3 scripts/finalizar.py renders/<Nome>-reel-final.mp4
```
`finalizar.py` monta o áudio (limiter a −1 dBTP), faz o mux e o QC básico. À parte: bipe no MP4, quadros-chave
× preview, `sync-check.mjs`, MD5 do bruto.

## Fase 11 — Entrega e fechamento

Mensagem com o link do preview e o resumo (arquivo, duração, resolução, fps, validação, áudio, B-roll por slot,
callouts, decisões). Preencher o `EDICAO.md` do projeto e levar as **"Lições para o kit"** para `docs/05` e para
`modelo-projeto/scripts/` (com `git commit` no kit).

## Correção depois do render

- **Não muda o tempo** (B-roll, texto, cor, volume): corrigir → build → bake dos alvos → apagar só as partes
  afetadas em `renders/chunks/` → `zsh work/render-all.sh <SIZE>` (mesmo SIZE) → `finalizar.py`.
- **Muda o tempo** (corte, velocidade, J-cut, ordem): avisar que é render inteiro; guardar o plano antigo em
  `work/vN/`, remapear os slots com `remap_tl.py`, refazer chunks/legendas, apagar todas as partes.

---

## O contrato: `assets/edit-plan.json`

| Campo | O que faz |
|---|---|
| `fps` | fps da **timeline** (30). O arquivo final sai a 60 |
| `rate` | velocidade global: vídeo por `setpts`, voz por `atempo` (tom preservado) |
| `jcutLeadFrames` / `jcutCrossfadeFrames` | 9 / 3 (docs/05 §7) |
| `src` / `voiceSrc` | mezanino / voz dedicada (com bipe) |
| `segments[]` | `in`, `out`, `aout`, `label`, `chunk` (vêm do `plan_segments.py`); `videoTail` opcional (L-cut) |
| `sections[]` | `afterSegment`, `name` — light-leak no corte; "CLIMAX" no nome dispara riser + impact-hit |
| `broll[]` | `mode` (`split`/`full`), `fromSeg`, `toSeg`, `span` [f0,f1], `file`; opcionais `preStart`, `objectPosition`. Escrito por `slots.py` |
| `impacts[]` | `phrase` (como está na legenda, sem acento/pontuação), `seg`, `lines`, `hold`, `style` (`typing` no 1º), `top` (%) |
| `presenterZoom` | `scales`, `mode: scene`, `sceneMax`, `maxHold`, `origin` |
| `leakMinGap` | intervalo mínimo entre transições (3,5) |
| `hookSeg` | segmento do gancho/capa (0; `null` desliga) |
| `capLowSegs` | segmentos com legenda a 76% sobre B-roll de tela cheia |
| `splitShiftY` | deslocamento vertical do apresentador no split — medir |
| `ctaSeg` | 1º segmento do encerramento (push-in) |
| `trilhaVol`, `trilhaLoop` | volume da trilha (0,079); emenda quando o reel passa de 164 s (`at`, `back`, `xfade`) |
| `bakedAroll`, `bakedAudio`, `bakedBroll`, `bakedLeaks` | faixas pré-renderizadas (sempre `true`) |
| `brollKenBurns` | `false` (o `make_broll.py` já grava a câmera) |
| `yellowCapSegs` | LEGADO — caixa amarela no gancho (só com `hookSeg: null`) |

`build-edit.mjs` lê também `assets/chunks/meta.json` e `assets/chunks/chNN-words.json` — sem eles quebra — e
termina com `OK: N segs, Xs, N cenas de broll (N tomadas), N sfx, N legendas, N callouts, N leaks, J-cut 9f/3f.`


---

# ARQUIVO: `docs/02-jcut-algoritmo.md`

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


---

# ARQUIVO: `docs/06-checklist-execucao.md`

# Checklist de execução — do bruto ao MP4

Ordem fixa. Cada fase só começa quando a anterior fechou. Comandos em `docs/01`; porquês em `docs/05`.

## 0 · Antes de começar
- [ ] `sudo -n true` **não** responde "you do not exist in the passwd database" (se responder: pedir relogin)
- [ ] Disco: `df -h /` — ≥ 7 GB livres é o confortável para chegar ao render
- [ ] Bruto em `~/Claude/videos-brutos/` (se estiver no servidor, pedir de volta; share `Company` montado)
- [ ] `zsh ~/Claude/KIT-EDICAO-REEL/novo-projeto.sh <slug> "Título"` — nada de copiar de projeto antigo

## 1 · Mezanino (sozinho)
- [ ] `zsh scripts/mezanino.sh "<bruto>" <slug>`
- [ ] Média de luminância bate em ~1–1,5/255 e desvio-padrão igual (cor não lavou)
- [ ] MD5 do bruto em `work/md5-bruto.txt`; tipo do bruto (HDR / SDR full-range) anotado no `EDICAO.md`

## 2 · Transcrição por região (depois do mezanino, nunca junto)
- [ ] `regions.py` → `mkreg.py` → `whisper_regs.sh` → `regwords.py`
- [ ] nº de JSON = nº de regiões
- [ ] Texto das regiões lido contra o roteiro: repetições, falsos inícios, **palavrões**

## 3 · Bipe (se houver palavrão)
- [ ] Varredura da transcrição **inteira**, inclusive takes que vão ser descartados
- [ ] Janela mapeada por recortes cumulativos + espectro; palavra **inteira**
- [ ] `bipe.py` → voz do projeto e `work/full.wav` com o bipe; `full-clean.wav` sem

## 4 · Takes e cortes
- [ ] Repetido → fica o **último**; falso início sai
- [ ] `valleys.py` → `mkcut.py` (SPLIT/DROP) → `cuts.py` (TAKES) → `plan_segments.py`
- [ ] Gancho = a 1ª frase inteira, num take só
- [ ] Avisos de "pausa curta" e "tail" do `cuts.py` lidos; `FORCE_IN`/`FORCE_OFF` onde a respiração engana

## 5 · Chunks e legendas
- [ ] `mkchunks.py` → `whisper_chunks.sh` → cópia crua em `work/chunks-raw/`
- [ ] Chunks colapsados/alucinados/vazados reconstruídos (`rebuild_chunk.py`)
- [ ] `align.py` → `captions_fix_table.py` (FIX/DROP/FIXT) → `fix_captions.py`
- [ ] Grafia do roteiro; onde o áudio diz outra coisa, vale o áudio (anotado)

## 6 · Plano, build, faixas
- [ ] `sections` (com a do CLIMAX), `impacts` (1º `typing`), `ctaSeg`, `hookSeg` no plano
- [ ] `node scripts/build-edit.mjs` → linha `OK: …`
- [ ] `python3 scripts/bake.py voz bed aroll` → `aroll.mp4 N quadros (timeline N)` batendo
- [ ] `python3 scripts/jcut_check.py` → 0 buracos · nenhum crossfade sobre fala · lead de fala ~5 quadros
- [ ] Bipe aceito por **medição** na `voz-mix.m4a` (≈100% da energia em 950–1050 Hz na janela)

## 7 · Varredura de olhar (1ª passada) e layout
- [ ] `gaze_tl.py` → `gaze_windows.py` (→ `gaze_pose.py` se ele mexe a cabeça)
- [ ] Folhas conferidas a olho (`gaze_review.py`, `vw_eyes.py`); recorte dos olhos medido para este bruto
- [ ] Triagem: nítidas × sutis; layout cobrindo todas as nítidas
- [ ] **1ª cena em split**; estrutura intro split → revelação → cutaways → 2º split → clímax → CTA
- [ ] Cenas de 3–5 s; `python3 scripts/ritmo.py`
- [ ] `slots.py --placeholders` → build → `bake.py cenas brollfull leaks bed`
- [ ] `splitShiftY` **medido**; capa conferida no snapshot de t=0
- [ ] 1ª menção do nome achada (`tl.py --words`); pré-revelação sem marca; revelação 2 quadros depois
- [ ] `npm run check` → 0 erros

## 8 · Pesquisa de B-roll
- [ ] Fotos reais por slot, fonte registrada; nada de IA sem pedido
- [ ] Subagente (se usar): sem dado do usuário em requisição; ~3 consultas por trecho; JSON antes de ampliar
- [ ] `PESQUISAS-BROLL-<TEMA>.md` salvo

## ■ PARADA ÚNICA
- [ ] Preview no ar e conferido com `curl`; **link no topo da mensagem**
- [ ] Mensagem lista: duração · cortes · velocidade · J-cuts · palavrões/bipe · olhar (leitura exposta em s) ·
      primeira cena · B-rolls por slot · decisões tomadas sem perguntar

## 9 · B-rolls reais (depois do "pode gerar")
- [ ] Correções pedidas aplicadas primeiro (se mexem no tempo: remapear slots, refazer chunks)
- [ ] `entrega.py` → `make_broll.py` → folha de QC início/meio/fim
- [ ] `slots.py --real` → build → `bake.py cenas brollfull leaks bed`
- [ ] `capLowSegs` e `impacts[].top` decididos nos snapshots; fundo claro com `dim`
- [ ] Revelação quadro a quadro: último limpo / primeiro com marca
- [ ] **2ª varredura de olhar** nos quadros da composição → leitura exposta em s
- [ ] `ritmo.py` · `jcut_check.py` · `npm run check` (0 erros)
- [ ] ≤ ~10 elementos de mídia na composição

## 10 · Export
- [ ] `python3 scripts/size_sweep.py` → `--size` com sobra mínima ≥ ~15 quadros
- [ ] `npx hyperframes preview --stop` (só o deste projeto)
- [ ] `zsh work/render-all.sh <SIZE>` como **tarefa de fundo do harness**
- [ ] `python3 scripts/finalizar.py renders/<Nome>-reel-final.mp4` → `QC OK`
- [ ] Bipe presente no MP4 · quadros-chave iguais ao preview · `sync-check.mjs` com lag mediano 0 ms
- [ ] MD5 do bruto igual ao do começo

## 11 · Entrega e fechamento
- [ ] Mensagem: link do preview + arquivo, duração, resolução, fps, validação, áudio, B-roll por slot, callouts
- [ ] `EDICAO.md` do projeto preenchido
- [ ] **"Lições para o kit"** levadas para `docs/05` / `modelo-projeto/scripts/` + `git commit` no kit
- [ ] Nota de memória só para o que é preferência do Fabio ou fato do ambiente — regra de edição vai para o kit


---

# ARQUIVO: `docs/10-scripts.md`

# Catálogo dos scripts (`modelo-projeto/scripts/` e `modelo-projeto/work/`)

Todos rodam de dentro da pasta do projeto. Origem: a cópia mais nova de cada um em 2026-10-01 (projeto
`kazuo-inamori`, que já trazia todas as correções dos reels anteriores), mais três scripts novos escritos para
o kit.

- **MOTOR** — não muda de reel para reel. Correção nele vale para todos: fazer no kit e dar `git commit`.
- **POR VÍDEO** — o código fica, os **dados** são do reel. Vêm com os dados do Kazuo Inamori como exemplo de
  preenchimento e têm que ser reescritos. Não rodar sem trocar.

## Fase 1–2 · mezanino e transcrição

| Script | Tipo | O que faz |
|---|---|---|
| `mezanino.sh` | MOTOR · **novo no kit v2** | mezanino (HDR / SDR full-range / SDR limited), voz limpa, `full.wav`, `full-clean.wav`, MD5, conferência de cor. Testado no caso SDR full-range (o de todos os brutos recentes); o ramo HDR é o comando registrado no kit v1 e não foi exercitado em 2026-10 |
| `_src.py` | MOTOR | resolve o mezanino do projeto (importado pelos scripts de olhar) |
| `regions.py [-35dB] [0.35]` | MOTOR | `silencedetect` → `work/regions.json` |
| `mkreg.py` | MOTOR | um wav por região (± 0,3 s) → `work/reg/` |
| `whisper_regs.sh` | MOTOR | whisper large-v3 por região (`~/.cache/whisper/ggml-large-v3.bin`), serial |
| `regwords.py` | MOTOR | junta em `work/region-words.json` (tempos absolutos) e imprime o texto |

## Fase 3–5 · bipe, cortes, legendas

| Script | Tipo | O que faz |
|---|---|---|
| `bipe.py` | POR VÍDEO (`JANELAS`) | grava o bipe de 1 kHz na voz do projeto e em `work/full.wav`. Lê os nomes de arquivo do plano |
| `se_splice.py` | POR VÍDEO (molde) | cola uma sílaba de outro take na voz (caso David Marquet). Só quando precisar |
| `valleys.py t1 t2 …` | MOTOR | vales de silêncio perto de um instante (para dividir região) |
| `mkcut.py` | POR VÍDEO (`SPLIT`, `DROP`) | divide regiões nos vales e marca descartes → `regions_cut.json`, `region-words-cut.json` |
| `cuts.py` | POR VÍDEO (`TAKES`, `FORCE_IN`, `FORCE_OFF`) + motor | head/tail/aout de cada take → `work/segs.json`. Constantes do formato: `HEAD_PAD`, `TAIL_PAD`, `TA`, `HH` |
| `plan_segments.py` | MOTOR | `work/segs.json` → `segments` do plano (preserva campos postos à mão) |
| `mkchunks.py` | MOTOR | 1 chunk por take do áudio limpo → `assets/chunks/` + `meta.json`. **Sem clamp** |
| `whisper_chunks.sh` | MOTOR | whisper palavra a palavra por chunk |
| `rebuild_chunk.py ch:reg[+reg]` | MOTOR | reconstrói um chunk a partir do passe por região |
| `align.py [chunks]` | MOTOR | reancora os tempos de palavra na energia real; ignora DROP; limita em `aout` |
| `captions_fix_table.py` | POR VÍDEO (`FIX`, `FIXT`) | tabela de correções por chunk e índice de palavra (`DROP` = apagar) |
| `fix_captions.py [chunks]` | MOTOR | aplica a tabela; idempotente (`work/chunks-aligned/`) |
| `tl.py [--words]` | MOTOR | timeline de cada take e de cada palavra |
| `remap_tl.py t…` | MOTOR | converte tempo de timeline de um plano antigo para o atual pelo mesmo quadro do bruto (`REMAP_OLD`) |

## Fase 6 · build e faixas

| Script | Tipo | O que faz |
|---|---|---|
| `build-edit.mjs` | MOTOR | gera a edição inteira no `index.html` a partir do plano; grava `work/mix-plan.json`, `broll-groups.json`, `leaks.json`. `--passes` gera os passes de camada para NLE |
| `bake.py [alvos]` | MOTOR | `aroll`, `voz`, `bed`, `cenas`, `brollfull`, `leaks` (sem argumento = tudo) |
| `jcut_check.py` | MOTOR | valida o J-cut por dados |
| `ritmo.py [4.0]` | MOTOR | lista intervalos sem evento na tela acima do limite |

## Fase 7 · olhar e layout

| Script | Tipo | O que faz |
|---|---|---|
| `gaze_tl.py` | MOTOR | blendshapes quadro a quadro na timeline → `gaze/tl.json` |
| `gaze_windows.py [SIDE] [DOWN]` | MOTOR | janelas de leitura → `gaze/tl-windows.json` |
| `gaze_pose.py [K]` | MOTOR | olhar compensado pela pose da cabeça → `gaze/pose-windows.json` |
| `gaze_review.py [saida]` | MOTOR | folhas grandes das janelas (REF + 5 quadros) |
| `vw_tl.py`, `vw_eyes.py`, `vw_big.py`, `vw_batch.py` | MOTOR* | faixas/zoom dos olhos para conferência. *O recorte dos olhos é do enquadramento: ajustar por bruto |
| `gaze_measure.py`, `gaze_report.py`, `gaze.py`, `grids.py`, `gaze_bounds.py`, `gaze_pairs.py`, `gaze_blend.py`, `gaze_down.py`, `gaze_lids.py` | MOTOR (geração anterior) | medidor de íris e revisões por fronteira de take; úteis em casos específicos |
| `cenas_opt.py` | POR VÍDEO (`SPLIT`, `FORCE`, `ONLYB`, `ONLYP`) + motor | DP do layout de cenas → `work/cenas-opt.json` |
| `work/layout-exemplo.py` | POR VÍDEO (molde) | layout desenhado à mão (S/B/P com tempos) |
| `slots.py [--placeholders] [--real]` | POR VÍDEO (`S`, `NOMES`) + motor | janelas de B-roll em tempo absoluto → `assets/broll-slots.json` e `plan.broll` |

## Fase 8–9 · B-roll

| Script | Tipo | O que faz |
|---|---|---|
| `gimg.mjs "consulta" [n]` | MOTOR | Google Imagens via Serper (chave no `.env`) |
| `fal_img.mjs modelo saida aspect "prompt"` | MOTOR | imagem-conceito no fal.ai — **só a pedido** |
| `work/pesq/*` | MOTOR | pesquisa e download (docs/11) |
| `pesquisa_md.py` | POR VÍDEO (textos) + motor | gera o `PESQUISAS-BROLL-<TEMA>.md` |
| `entrega.py` | POR VÍDEO (`PK`) + motor | foto escolhida por slot → recorte no aspecto do slot + folha |
| `make_broll.py [--only id,…]` | POR VÍDEO (`S`) + motor | anima a foto só com câmera → `assets/broll/` |
| `norm_broll1.py` | POR VÍDEO (molde) | normaliza vídeo entregue pelo Fabio (caso Rolex) |

## Fase 10 · export

| Script | Tipo | O que faz |
|---|---|---|
| `size_sweep.py` | MOTOR · **novo no kit v2** | escolhe o `--size`. Conferido contra o Kazuo: 432 → sobra mínima 92 quadros, como registrado |
| `render-chunks.mjs` | MOTOR | render de uma parte (`--fps --size --only K --split N`); `--join` une |
| `work/render-all.sh <SIZE> [FPS] [SPLIT]` | MOTOR · generalizado no kit v2 | todas as partes, uma por vez, com `TMPDIR` no projeto |
| `finalizar.py <saida.mp4>` | MOTOR · **novo no kit v2** | áudio final + mux + QC. Conferido contra o Kazuo: mesmos 5897 quadros, 98,283 s, 369 MB, pico −1,0 / média −19,1 dB, áudio idêntico byte a byte |
| `sync-check.mjs final16k.wav bruto16k.wav` | MOTOR | lag boca/voz por take |

## Mudanças em relação às cópias dos projetos

Só o que foi necessário para o modelo não depender de pasta ou nome de projeto:
`gimg.mjs` / `fal_img.mjs` (caminho do `.env` por `$REEL_ENV`, padrão `~/Claude/reel-auto/.env`) · `bipe.py` (nomes
de arquivo vindos do plano) · `work/render-all.sh`, `work/pesq/s.sh`, `work/pesq/pick.sh` (caminho relativo ao
script). O resto é byte a byte o que rodou no último reel. O `build-edit.mjs` do modelo, aplicado ao plano do
Kazuo, gera o mesmo `index.html` do projeto (`verificar-instalacao.sh` repete esse teste).

## Dependências

Node ≥ 20 · Python 3.9+ com `numpy`, `opencv-python` (`cv2`), `Pillow`, `mediapipe` · `ffmpeg`/`ffprobe` em
`/opt/homebrew/bin` (o `render-chunks.mjs` usa esse caminho) · `whisper-cli` + `~/.cache/whisper/ggml-large-v3.bin`.

## Scripts antigos

O pipeline `.mjs` dos primeiros reels (Havaianas, Natura, Nubank, Bariloche: `broll-gerar.mjs` com Kling/fal,
`gaze-scan.mjs`, `build-presenter.mjs`…) e variantes pontuais estão em `arquivo-projetos/<slug>/scripts/`.
Não fazem parte do fluxo atual.


---

# ARQUIVO: `docs/11-pesquisa-broll.md`

# Pesquisa de B-roll

O que procurar, onde, com que ferramenta, e o que entregar na parada. Regras de uso da imagem em `docs/05` §14
(marca só depois do áudio) e §16 (geração).

## Método atual (2026-10-02): navegador na fonte primária, não busca por API

**Ir à fonte, não a um buscador.** Busca de imagens por API (Serper/Google, Bing) devolve repostagens: banco de
imagem disfarçado, resolução baixa, marca d'água. No reel Alan Mulally, 3 de 22 fotos assim tiveram de ser
trocadas no QC. O método que deu o melhor resultado (vídeos Vê.la e Joyce, sessão "Opus 5.5 Showreel"):

1. **Abrir as fontes no navegador do app** (`mcp__Claude_Browser__navigate` + `get_page_text`): sala de imprensa
   (ex.: media.ford.com), site oficial, RI, Instagram/LinkedIn da pessoa, página da Wikipedia, matérias. Ler o
   texto real — **todo número e fato do vídeo sai de uma página aberta**, com a URL registrada.
2. **Site inteiro de uma vez:** `npx hyperframes capture "<url>" -o ./capture --json` → imagens, SVGs, fontes,
   tokens de cor e screenshots em `capture/`.
3. **Imagem na maior resolução**: JavaScript na própria página (`javascript_tool`) listando
   `img.currentSrc || img.dataset.src || maior entrada do srcset`; quando o site serve por CDN com tamanho na URL,
   pedir o maior (ex.: `cdn.awsli.com.br/1920x1920/...`). Baixar com `curl -sSL -A "Mozilla/5.0"` (UA genérico,
   **nunca** dado do usuário) e medir com `sips`.
4. **Instagram:** abrir o perfil, rolar (`window.scrollTo` + espera) e extrair `a[href*="/p/"] img` → URLs dos
   posts; montar uma grade na própria aba para escolher pela captura de tela.
5. **Prova no formato do próprio conteúdo** (skill showreel-interface): screenshot real da manchete/matéria
   (ex.: "Ford penhora o logotipo", "GM pede falência") vale mais que foto genérica do assunto.
6. **Logos:** SVG oficial (Commons/site); se só houver PNG pequeno, vetorizar (OpenCV → SVG) e separar as partes
   para animar. Logo só sofre corte, fade, deslocamento e escala uniforme.
7. **Folha de contato** (`work/pesq/sheet.py`) → escolher → recortar tirando texto sobreposto.

Fallback: Wikimedia Commons (`work/pesq/wm.py` / `wmpick.py`, licença registrada). Busca por API só se não houver
fonte primária, e passando pelo `filt.py`. (`scripts/bimg.py` do projeto alan-mulally foi um remendo para
máquina sem chave Serper: **aposentado**, não usar.)

## O que procurar

Uma foto **real** por slot, que mostre o que a fala daquele trecho diz. Em ordem de preferência:

1. Sala de imprensa / site oficial / RI da empresa (ou o site oficial da pessoa, da editora, do evento) — pelo navegador, acima.
2. Wikimedia Commons (alta resolução, licença registrada).
3. Busca de imagens em tamanho grande (`gimg.mjs` pede `isz:l`) — último recurso.

**Trecho conceitual** (processo, número, gráfico, "semáforo", "arco-íris"…) sem imagem real que o represente:
**não vira foto genérica, vira motion graphics** na camada `compositions/mg.html` (docs/13).

Critérios: lado menor ≥ ~900 px (abaixo disso só com `fill`); sem marca d'água; assunto que caiba no 9:16 (tela
cheia) ou na faixa 16:9 do split; **variedade** — duas fotos parecidas em sequência leem como "parado".
`filt.py` já descarta bancos de imagem (Shutterstock, Getty, Alamy, iStock, Pinterest…).

**Pré-revelação** (antes de o áudio dizer o nome): é o gargalo. Funciona interior/detalhe do material oficial
sem logo, recorte abaixo do letreiro, ou cena genérica do assunto. Foto de fachada e de protesto trazem o nome.

**IA generativa: nunca por conta própria.** Só quando o Fabio descreve a cena — aí é `fal_img.mjs` com
`fal-ai/nano-banana-pro`, 4:3 (serve para split e para tela cheia com fundo borrado), mostrada na parada e
marcada "gerada a pedido" no arquivo de pesquisas. O flux errou mãos; o nano-banana-pro acertou. Não usar
`dry_run` para testar modelo no fal: enfileira job de verdade.

## Ferramentas (`work/pesq/`, rodar de dentro dela ou pelos caminhos indicados)

| Ferramenta | Uso |
|---|---|
| `s.sh <qid> "consulta" [n]` | Google Imagens → `q/<qid>.txt` (já filtrado por `filt.py`) |
| `pick.sh <qid> <idx…>` | baixa os escolhidos em `raw/<qid>_<idx>.jpg` e registra em `g_index.json` |
| `wm.py "consulta" [n]` | busca no Commons → `q/wm_<slug>.json` (título, tamanho, licença) |
| `wmpick.py <slug> <idx…>` | baixa do Commons e grava a licença em `wm_lic.json` |
| `crawl.py <base> <prefixo> <limite> <saida.json>` | varre um site oficial e lista as imagens |
| `dl.py <tag> <img> <page> <dom>` | download com UA genérico de Chrome e Referer; converte para JPG |
| `sheet.py <saida.jpg> <glob…>` | folha de miniaturas rotuladas para escolher |

Convenção de nome: o prefixo do arquivo é o trecho do roteiro (`b03a_9`, `c18a_15`…), para montar folha por
trecho. Escolhidas vão para `cand/`, com `candidates.json` e `picks.json` (escolha + alternativa por slot).

As chaves (`SERPER_API_KEY`, `FAL_KEY`) ficam em `~/Claude/reel-auto/.env` — fora do kit, do git e do servidor.

## Se delegar a um subagente

Pôr no prompt, textualmente:

- "Use um User-Agent genérico de Chrome. **Nunca** coloque e-mail, nome ou qualquer dado do usuário em headers,
  URLs ou payloads." (No Andy Grove o subagente pôs o e-mail do Fabio no UA para o Wikimedia.)
- "No máximo ~3 consultas por trecho. Entregue `candidates.json` e `picks.json` **antes** de ampliar a busca."
  (No Kazuo ele travou duas vezes, 600 s sem progresso, com 331 fotos baixadas e nenhum pick.)
- O que já está decidido: slots, tempos, o que é pré-revelação, o que o Fabio entregou.

Se travar: **não retomar**. Montar as folhas por trecho a partir do `g_index.json` e fechar à mão.

## O que sai da pesquisa

`PESQUISAS-BROLL-<TEMA>.md` (gerado por `scripts/pesquisa_md.py`), por slot: trecho da fala · tipo de
enquadramento (split 16:9 / tela cheia 9:16) · imagem recomendada · link e fonte · **prompt de animação** ·
duração necessária · nome do arquivo.

O prompt de animação descreve **só o movimento de câmera** (aproximação, travelling, tilt, pull-out), nunca
redescreve a imagem, e sempre diz que textos, logotipos e elementos de marca ficam parados, legíveis e nítidos.
Mesmo quando o B-roll é gerado localmente pelo `make_broll.py`, o movimento usado é o do prompt.

Exemplo completo: `exemplos/kazuo-inamori/PESQUISAS-BROLL-KAZUO-INAMORI.md`. Mais antigos em `broll-prompts/`
e em `arquivo-projetos/*/PESQUISAS-BROLL-*.md`.

## Da foto ao arquivo

`entrega.py` (tabela `PK`: candidata, âncora `ax/ay`, `fill`, pré-recorte) → `assets/broll-src/entrega/<slot>-9x16.jpg`
ou `-16x9.jpg` + folha `work/pesq/sheet_entrega.jpg` → `make_broll.py` (lista `S`: `z0/z1`, `dx/dy`, `dim`).
Decisões de enquadramento que já custaram iteração estão em `docs/05` §16.


---

# ARQUIVO: `docs/12-export-em-partes.md`

# Export em partes (MacBook Air 8 GB)

O render direto do HyperFrames trava nesta máquina ("Sequential screenshot capture stalled") e, com vários
workers, o Mac chega a reiniciar. O caminho que fecha — 1440×2560 @ 60 fps, ~90–100 s, em ~15–25 min:

```bash
python3 scripts/size_sweep.py                     # 1. tamanho da parte
npx hyperframes preview --stop                    # 2. libera RAM (só o preview deste projeto)
zsh work/render-all.sh <SIZE>                     # 3. partes — COMO TAREFA DE FUNDO DO HARNESS
python3 scripts/finalizar.py renders/<Nome>-reel-final.mp4    # 4. áudio + mux + QC
```

## 1. Tamanho da parte

O render tem um **gate de cobertura**: se uma parte fica com 2–3 quadros de um clipe, ele aborta ("captured 2
of expected 3 frames"). Está certo — evita clipe em branco. **Não desligar**; escolher o tamanho.

`size_sweep.py` mede, para cada tamanho, a menor sobra de `<video>` dentro de qualquer pedaço e lista os
melhores. O que já foi pago:

- varrer **só os `<video>`** — contando as legendas nenhum tamanho passa (falso alarme);
- incluir os **pedaços do `--split`** — 354 era bom sem split e deixava 8 quadros com `--split 3`;
- sobra mínima ≥ ~15 quadros; varrer de 1 em 1 (os números redondos costumam ser piores);
- a 60 fps ficar em ~300–460 por parte.

Tamanhos usados: 320 (IKEA, Chris Voss, Rolex) · 351 (Jocko, Dan Martell) · 354 (Atul, Andy Grove) · 360 (Jeff
Bezos, Munger) · 348 (Marquet) · 441 (Reed) · 449 (Herb) · 390 (Taiichi) · 342 (Vince) · 372 (Mike, Sun Tzu) ·
432 (Kazuo). Não reaproveitar: depende do layout de cada reel.

## 2–3. As partes

`work/render-all.sh` roda uma parte por vez com `--split 3`: cada parte vira 3 pedaços, cada pedaço numa
**sessão nova do Chrome**, unidos sem recodificar. É isso que acabou com as travas — o limite de quadros por
sessão não é fixo (já travou em 318, 530 e 572, sempre no mesmo quadro, enquanto o snapshot naquele instante
funcionava: não era o quadro, era a sessão).

- **Tarefa de fundo do harness**, não `nohup … &` (morre com `render_cancelled_parent_exited`).
- `TMPDIR` dentro do projeto (`renders/tmp/`), limpo a cada parte: o cache de extração e o perfil do Chrome não
  enchem o disco do sistema. Para com menos de 600 MB livres.
- Retoma de onde parou (parte que existe é pulada). Quando uma parte falha, o script apaga o `chunk-KK.mp4`
  dela: uma parte errada deixada no disco seria pulada na rodada seguinte (no Andy Grove isso custou 3 quadros
  de sincronia). O `finalizar.py` também recusa o mux se a soma dos quadros não for a da timeline.
- ~1–1,5 min por parte. "Capture stalled" isolado: relançar sem mudar nada.
- `RENDER_EXTRA="--no-browser-gpu"` passa flags extras ao render (último recurso; não resolveu no Munger).
- Flags fixas do `render-chunks.mjs`: `--sdr` (o pipeline HDR precisa de ~20 GB e falha), `-q delivery`,
  `--workers 1`, `--video-frame-format jpg`, `--no-best-effort`, `--browser-timeout 300`.

## 4. Fechamento

`finalizar.py`:

1. confere que a soma dos quadros das partes é a timeline (a última pode vir com +1);
2. áudio = `amix(voz-mix, bed, normalize=0)` + `alimiter=limit=0.891:level=disabled` — o `level=disabled` é
   obrigatório (com o auto-level o limiter normaliza de volta para 0 dB);
3. mux direto da lista de partes + `_audio.m4a`, vídeo copiado, **sem `-shortest`** (ele decepa o último
   quadro), com `-frames:v`;
4. QC: quadros = timeline · A/V dentro de 2 quadros · pico ~−1 dB · 0 trechos pretos.

Com as faixas pré-renderizadas o áudio entra com offset zero por construção. (O truque antigo — render com
`--debug`, caçar o `audio.m4a` em `~/.npm/_npx/<hash>/` e medir `-itsoffset` — acabou no reel André Esteves.)

Conferir à parte:

- **Bipe no MP4:** energia em 1 kHz na janela (a trilha por baixo deixa ~98–99%).
- **Quadros-chave** iguais ao preview (capa, revelação, split, callouts, clímax, CTA): diferença de poucos /255.
- **Sincronia boca/voz:** `node scripts/sync-check.mjs final16k.wav bruto16k.wav` → lag mediano 0 ms. Takes de
  ~1 s dão medida ruim (a janela atravessa a emenda) — artefato da medição.
- **MD5 do bruto** igual ao do começo.

## Correção sem mudar o tempo

Corrigir → `build-edit.mjs` → `bake.py` dos alvos → apagar só as partes que cobrem o trecho →
`zsh work/render-all.sh <mesmo SIZE>` → `finalizar.py`. Por isso as partes ficam guardadas em
`renders/chunks/` até o Fabio dar o reel por encerrado. (Mike Michalowicz: troca da capa = 1 parte re-renderizada.)

## Depois

O final vai para o servidor (`/Volumes/Company/Equipe/FABIO KENJI/VIDEOS FINAL BACKUP/`, com linha no
`_MD5.txt`); as partes de `renders/chunks/` podem ser apagadas quando não houver mais correção a fazer.


---

# ARQUIVO: `docs/04-prompt-comando-unico.md`

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


---

# ARQUIVO: `docs/07-mapa-de-arquivos.md`

# Mapa — onde está cada coisa

## No Mac

| Caminho | O que é |
|---|---|
| `~/Claude/KIT-EDICAO-REEL/` | **o kit** (este repositório git) — fonte única do formato |
| `~/Claude/reel-auto/<slug>/` | projetos de reel (os em uso; os antigos vão para o servidor) |
| `~/Claude/reel-auto/.env` | chaves `SERPER_API_KEY` e `FAL_KEY` — **fica só aqui** |
| `~/Claude/videos-brutos/` | brutos do reel em edição |
| `~/.cache/whisper/ggml-large-v3.bin` | modelo do Whisper (3 GB) |
| `~/.claude/skills/hyperframes*/`, `media-use/` | skills do HyperFrames |
| `~/.claude/projects/-Users-fabiotakahashi-Claude/memory/` | notas de memória do Claude (preferências e fatos do ambiente) |

## No servidor (`/Volumes/Company/Equipe/FABIO KENJI/`)

| Caminho | O que é |
|---|---|
| `VIDEOS FINAL BACKUP/` | os `*-reel-final.mp4`, com `_MD5.txt` (md5, nome, projeto de origem) |
| `VIDEOS BRUTOS BACKUP/` | brutos |
| `KIT-EDICAO-REEL/` | cópia de segurança do kit |

## Dentro do kit

| Caminho | O que é |
|---|---|
| `README.md`, `VERSAO.md` | entrada e histórico de versões |
| `novo-projeto.sh` | cria um projeto |
| `verificar-instalacao.sh` | teste de fumaça |
| `docs/01…12` | o conhecimento |
| `modelo-projeto/scripts/` | 53 scripts (catálogo em `docs/10`) |
| `modelo-projeto/work/` | `render-all.sh`, `layout-exemplo.py`, `pesq/` (ferramentas de pesquisa) |
| `modelo-projeto/index.html` | template da composição (CSS do formato + blocos gerados vazios) |
| `modelo-projeto/assets/edit-plan.json` | plano-esqueleto com os padrões |
| `modelo-projeto/EDICAO.md`, `CLAUDE.md`, `AGENTS.md`, `package.json`, `hyperframes.json`, `meta.json` | arquivos de projeto |
| `assets-fixos/trilha/`, `sfx/`, `fx/`, `fonts/`, `models/` | o que é igual em todo reel |
| `exemplos/kazuo-inamori/` | reel de referência (texto) |
| `arquivo-projetos/<slug>/` | texto dos 31 projetos |
| `broll-prompts/`, `exemplos/natura`, `exemplos/nubank`, `bruto/`, `legado/` | material da v1 |

## Dentro de um projeto

```
<slug>/
  EDICAO.md                 mapa do projeto (estado, decisões, medidas)
  PESQUISAS-BROLL-<TEMA>.md pesquisa de imagens por slot
  index.html                GERADO — nunca editar à mão
  CLAUDE.md, AGENTS.md, package.json, hyperframes.json, meta.json
  .models/face_landmarker.task
  assets/
    edit-plan.json          O CONTRATO — fonte única da edição
    <slug>-2560-sdr.mp4     mezanino
    <slug>-voz.m4a          voz do projeto (com bipe)
    aroll.mp4  voz-mix.m4a  bed.m4a  broll-full.mp4  leaks.mp4     faixas do bake.py
    broll-slots.json        slots de B-roll (tempos, fala, tema, fonte, prompt)
    broll-src/              fotos escolhidas; broll-src/entrega/ = recortes no aspecto
    broll/                  B-rolls finais + _cenaNN.mp4 + _ph/ (placeholders)
    chunks/                 chNN.wav, chNN-words.json, meta.json
    fonts/ sfx/ trilha-….mp3 transicao-light-leak.mp4
  scripts/                  do modelo; os POR VÍDEO reescritos
  work/
    kit-versao.txt          versão do kit que criou o projeto
    full.wav (com bipe)  full-clean.wav (sem)  <slug>-voz-limpa.m4a  md5-bruto.txt
    regions.json  reg/  region-words.json  regions_cut.json  region-words-cut.json  segs.json
    chunks-raw/  chunks-aligned/
    mix-plan.json  broll-groups.json  leaks.json            gerados pelo build-edit.mjs
    pesq/                   pesquisa (q/, raw/, cand/, g_index.json, candidates.json, picks.json)
    qc/  vN/                conferências; planos de versões anteriores
    render-all.sh
  gaze/                     tl.json, tl-windows.json, pose*.json, folhas de conferência
  snapshots/                quadros da composição
  renders/
    chunks/chunk-NN.mp4     partes do render (guardar até encerrar as correções)
    _audio.m4a  parts.txt   <Nome>-reel-final.mp4
```

## O que pesa e o que pode sair do Mac

| Pasta | Peso típico | Depois de entregue |
|---|---|---|
| `assets/` | ~1 GB | servidor (é o que permite reeditar) |
| `renders/chunks/` | ~0,4 GB | apagar ou servidor (refazível) |
| `work/` | ~0,3 GB | servidor |
| `snapshots/`, `gaze/` | ~0,1 GB | servidor |
| texto (`EDICAO.md`, scripts, planos) | < 2 MB | já está em `arquivo-projetos/` |


---

# ARQUIVO: `docs/09-instalacao-outra-maquina.md`

# Instalar o kit em outra máquina (kit v3)

**Caminho curto: `zsh instalar.sh` na raiz do kit** — faz os passos abaixo e roda o `verificar-instalacao.sh`.
Guia em linguagem simples: `COMECE-AQUI.md`. O que o fluxo v3 usa além do kit: Python 3.12 em `~/Claude/.venv-reel`
(mediapipe 0.10.14 não instala no Python 3.13+), `~/.cache/whisper/ggml-large-v3-turbo.bin` (o `large-v3` é só
reserva), a skill `showreel-interface` em `~/.claude/skills/` (o `mg_sfx.py` importa o `sfx.py` dela), Chrome, e o
Codex CLI logado (opcional, capa a pedido).

---

# Instalar o kit em outra máquina

O kit (~45 MB) carrega tudo que é *do formato*: scripts, template, assets fixos, docs. O resto é ferramenta
pública. No fim, `bash verificar-instalacao.sh` confere item por item e reconstrói o reel de referência.

## 1 · O que copiar

A pasta **`KIT-EDICAO-REEL/`** inteira, para `~/Claude/KIT-EDICAO-REEL` (os docs e o `CLAUDE.md` dos projetos
usam esse caminho). Não precisa de nenhum projeto de `reel-auto/`.

**Não vão no kit e têm que ser providenciados:**
- `~/Claude/reel-auto/.env` com `SERPER_API_KEY=` (Google Imagens) e `FAL_KEY=` (imagem-conceito). Sem ele a
  edição funciona; só a pesquisa automática e a geração de imagem param. Nunca colocar esse arquivo no kit.
- O modelo do Whisper (item 4).

## 2 · Ferramentas

macOS com [Homebrew](https://brew.sh):

```bash
brew install ffmpeg whisper-cpp node
pip3 install numpy opencv-python Pillow mediapipe
```

| Ferramenta | Versão em uso (2026-10) | Para quê |
|---|---|---|
| Node.js | 24.14 (mínimo 20) | `build-edit.mjs`, `render-chunks.mjs`, CLI do HyperFrames |
| ffmpeg / ffprobe | 9.0 | mezanino, bake, B-roll, QC. Os scripts de render chamam `/opt/homebrew/bin/ffmpeg` |
| whisper-cpp (`whisper-cli`) | Homebrew | transcrição |
| Python 3 | 3.9 | scripts `.py` |
| numpy · opencv · Pillow · mediapipe | 2.0 · 5.0 · 11.3 · 0.10.14 | cortes, olhar, B-roll |
| Google Chrome | sistema | render e preview |

O ffmpeg do Homebrew **não tem `zscale` nem `drawtext`**: os comandos do kit usam `colorspace` e `scale`. Não
trocar por receita com `zscale`.

## 3 · HyperFrames

Roda por `npx`, sem instalação nem login para render local. Os projetos fixam `hyperframes@0.8.64` no
`package.json` (o `render-chunks.mjs` chama `0.8.48` no render — combinação validada no Air de 8 GB).

```bash
npx hyperframes skills update     # skills hyperframes-* em ~/.claude/skills
npx hyperframes doctor            # TTS, BGM e Docker podem ficar vermelhos: não são usados
```

## 4 · Modelo do Whisper (3 GB)

`~/.cache/whisper/ggml-large-v3.bin` — é o caminho que `whisper_regs.sh` e `whisper_chunks.sh` usam. Copiar da
máquina antiga ou baixar o `ggml-large-v3.bin` do repositório do whisper.cpp.

## 5 · Verificar

```bash
bash ~/Claude/KIT-EDICAO-REEL/verificar-instalacao.sh
```
Confere ferramentas, filtros do ffmpeg, bibliotecas Python, assets, e reconstrói o reel Kazuo Inamori a partir
de `exemplos/kazuo-inamori/`. Tem que sair:

```
OK: 41 segs, 98.275s, 4 cenas de broll (21 tomadas), 25 sfx, 101 legendas, 9 callouts, 18 leaks, J-cut 9f/3f.
```
e "index.html igual ao de referência".

## 6 · Usar

Claude Code aberto em `~/Claude`, o prompt de `docs/04` com o nome do bruto, o tema e o roteiro.

## Diferenças de máquina que importam

- **Com mais de 8 GB de RAM** muita coisa do kit fica conservadora demais (render em partes com `--split 3`,
  tudo serial), mas continua correta. Não mexer sem medir.
- **Disco:** ≥ 7 GB livres na hora do render.
- **Fontes:** vão dentro do projeto (`assets/fonts/`); nunca depender de fonte instalada no sistema.
- **Fora do macOS:** os scripts usam `zsh`, `md5`, `sed -i ''` e `/opt/homebrew/bin` — precisam de ajuste.


---

# ARQUIVO: `COMECE-AQUI.md`

# COMECE AQUI — levar a edição de reels para outro computador

Esta pasta é **toda a inteligência** da edição: o formato (números, regras, erros já pagos em 33 reels), os scripts,
o modelo de projeto, a trilha, os SFX, as fontes, os exemplos (Deming é o mais recente e o padrão atual) e as skills
que ensinam o Claude a usar tudo isso. O Claude no outro computador lê esta pasta e edita igual.

## O que precisa no outro computador
- **Mac com Apple Silicon** (M1/M2/M3/M4). 16 GB de RAM é o ideal; 8 GB funciona, mais devagar (ver docs/09).
- **≥ 15 GB livres** (ferramentas + modelo do Whisper + render).
- **Claude Code** — o app Claude (aba Code) ou o `claude` no Terminal, logado na sua conta.
- **Google Chrome** instalado (o render usa).
- Opcional: **Codex CLI** logado na conta ChatGPT (só para gerar a capa com IA).

## Instalar (uma vez, ~15 min)
1. Copie a pasta `KIT-EDICAO-REEL` para o outro Mac (pendrive, AirDrop, Drive — tanto faz onde).
2. Se o Mac ainda não tem o Homebrew, instale pelo comando de https://brew.sh (ele pede a senha do Mac).
3. No Terminal, rode (arraste o `instalar.sh` para a janela do Terminal no lugar do caminho):
   ```
   zsh /caminho/para/KIT-EDICAO-REEL/instalar.sh
   ```
   Ele instala ffmpeg, whisper, node e Python 3.12; copia o kit para `~/Claude/KIT-EDICAO-REEL`; cria o Python do kit;
   baixa o modelo do Whisper (1,6 GB); instala as skills no Claude Code e, no fim, **confere tudo e reconstrói um reel
   de teste**. Tem que terminar com `0 falha(s)`.
4. Feche e abra o Claude Code para ele enxergar as skills novas.

## Usar
1. Coloque o vídeo bruto em `~/Claude/videos-brutos/` (ou em qualquer lugar — você passa o caminho).
2. Abra o Claude Code na pasta `~/Claude` e mande o prompt (modelo em `docs/04-prompt-comando-unico.md`):
   ```
   Edita o reel do [TEMA] com o bruto [CAMINHO DO BRUTO] e este roteiro:
   [ROTEIRO]

   Segue o fluxo rápido do kit (~/Claude/KIT-EDICAO-REEL/docs/14-fluxo-rapido.md): formato do kit + camada de
   motion graphics da skill showreel-interface, na dosagem do reel Deming v2: abertura só com fotos, no corpo foto
   real como padrão e motion só onde conta a história. Comando único, sem parada: pesquisa as imagens na fonte
   primária pelo navegador, gera a capa no Codex com esta cena: [CENA], monta, confere quadro a quadro e me manda o
   MP4 aqui no chat.
   ```
3. Em ~1 h o MP4 chega no chat. Para ajustar, é só pedir ("menos motion", "troca a foto do minuto 0:30"…).

## Onde está cada coisa
| | |
|---|---|
| `docs/14-fluxo-rapido.md` | o fluxo padrão, comando a comando |
| `docs/05-calibracoes-e-armadilhas.md` | **o mais importante**: todos os números e erros já pagos (§24 = dosagem de imagem × motion) |
| `docs/13-camada-motion.md` | como a camada de motion é feita |
| `exemplos/deming/` | o último reel aprovado: gerador da camada (`gen.py`; `gen-v1.py` = versão com motion demais), plano, cortes, legendas |
| `modelo-projeto/` | o esqueleto que todo reel novo copia |
| `assets-fixos/` | trilha, SFX, light-leak, fontes, modelo de rosto |
| `skill/` | as skills que o `instalar.sh` coloca no Claude Code |

## O que NÃO vai nesta pasta (de propósito)
- Chaves de API (`~/Claude/reel-auto/.env`). O fluxo padrão não precisa delas.
- O modelo do Whisper (o `instalar.sh` baixa).
- Vídeos brutos e projetos renderizados (pesados; o kit não depende deles).
- Logins (Codex, Claude) — cada computador faz o seu.

## Manter os dois computadores iguais
O kit é um repositório git. Quando um reel ensinar algo novo, o Claude grava em `docs/05` e dá commit. Para levar a
versão nova ao outro Mac, copie a pasta de novo e rode o `instalar.sh` (ele guarda a versão antiga com outro nome).


---

# ARQUIVO: `VERSAO.md`

# Versões do kit

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


---

# ARQUIVO: `skill/edicao-reel-viral/SKILL.md`

---
name: edicao-reel-viral
description: Edita um vídeo bruto de talking-head no formato de reel viral do usuário (9:16 1440x2560 @60, 1,1x, capa laranja no quadro 0, split-screen, J-cut, bipe, legendas Montserrat, trilha e SFX fixos, fotos reais + camada de motion graphics da skill showreel-interface, HyperFrames). USE SEMPRE que o usuário mandar um bruto com roteiro para editar, disser "edita no meu formato", "faz o reel do X", mandar o prompt de comando único do kit, ou pedir correção/render de um reel em ~/Claude/reel-auto.
---

# Edição de reel viral — porta de entrada do kit

**O conhecimento está no kit, fonte única do formato:** `~/Claude/KIT-EDICAO-REEL/`. Esta skill só aponta para ele.

## Antes de qualquer ação, ler
1. `docs/14-fluxo-rapido.md` — **o fluxo padrão (kit v3)**: comando único, sem parada, do bruto ao MP4 no chat
2. `docs/05-calibracoes-e-armadilhas.md` — todo número travado e todo erro já pago (§23 camada de motion, **§24 dosagem**)
3. `docs/13-camada-motion.md` — a camada de motion; exemplos em `exemplos/deming/` (o mais recente) e `exemplos/alan-mulally/`
4. `docs/10-scripts.md` — quais scripts são MOTOR e quais são POR VÍDEO (estes vêm com dados de outro reel: reescrever)

## Fluxo (resumo de docs/14)
```
zsh ~/Claude/KIT-EDICAO-REEL/novo-projeto.sh <slug> "Título"      # cria ~/Claude/reel-auto/<slug>
zsh scripts/fase1.sh "<bruto>" <slug>     # FUNDO: mezanino + whisper por região -> work/regioes.txt
   (enquanto roda: pesquisa de fotos na fonte primária + capa no Codex)
   escrever scripts/mkcut.py (SPLIT/DROP) · scripts/cuts.py (TAKES) · scripts/bipe.py (JANELAS)
zsh scripts/fase2.sh                      # FUNDO: cortes, J-cut, chunks, legendas, faixas, olhar
   scripts/captions_fix_table.py -> zsh scripts/legendas.sh · ler gaze/me/g*.jpg · work/tl-words.txt
   plano: sections, impacts (<=5, 1º typing), ctaSeg, splitShiftY (MEDIR) · scripts/slots.py · camada mg
zsh scripts/montar.sh t1,t2,...           # build + bake + SFX + check + snapshots -> LER as imagens
zsh scripts/render-par.sh <SIZE> renders/<Nome>-reel-final.mp4   # FUNDO, SIZE de size_sweep.py
   conferir quadros do MP4 + bipe + MD5 do bruto -> SendUserFile
```

## Preferências do usuário (não re-perguntar)
- Comando único sem parada; o MP4 vai no chat no fim.
- **Abertura só com fotos; motion só no meio, onde carrega a história; foto real é o padrão** (docs/05 §24).
- O apresentador lê o roteiro olhando para o lado: varredura de olhar é obrigatória; leitura exposta reportada em segundos.
- Último take válido; palavra inteira; palavrão bipado inteiro e medido; nada da marca antes de o áudio dizer o nome.
- IA generativa só para a capa (Codex) ou quando ele descrever a cena.

## Regras
- Nunca editar `index.html` nem `compositions/mg.html` gerado à mão: plano / gerador -> build.
- Uma tarefa pesada por vez; render e whisper como tarefa de fundo do harness.
- Depois de ajuste: apagar as partes afetadas em `renders/chunks/` antes do `render-par.sh` (ele retoma).
- Fim do reel: lições novas para `docs/05` / `modelo-projeto/` + `git commit` no kit.

As skills do HyperFrames (`/hyperframes*`) cobrem a ferramenta; o kit cobre o formato. Onde divergirem, vale o kit.


---

# ARQUIVO: `modelo-projeto/EDICAO.md`

# EDICAO.md — mapa do projeto (reel __TITULO__)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
**Estado (__DATA__): EM EDIÇÃO.**
Duração ___ s · ___ takes · ___ bipe(s) · ___ legendas · ___ callouts · ___ light-leaks · ___ SFX · ___ slots de B-roll.

> **Regra de ouro: nunca editar `index.html` à mão.**
```
editar assets/edit-plan.json (ou scripts/slots.py para B-roll)  ->  node scripts/build-edit.mjs  ->  python3 scripts/bake.py <alvos>  ->  npm run check
(bake.py sem argumento = cenas, brollfull, leaks, voz, bed, aroll; mudou só B-roll: bake.py cenas brollfull leaks bed)
```

## Onde mexer em cada coisa

| Quero mudar… | Arquivo |
|---|---|
| cortes / takes (in/out) | `scripts/mkcut.py` (divisões/descartes) → `scripts/cuts.py` (lista TAKES, FORCE_IN/FORCE_OFF) → `work/segs.json` → `python3 scripts/plan_segments.py` |
| texto de legenda | `scripts/captions_fix_table.py` (FIX por chunk e índice de palavra) → `python3 scripts/fix_captions.py` (idempotente) |
| callouts | `impacts` no plano (frase, seg, linhas, hold, `top` opcional; o 1º com `style: typing`) |
| B-roll (janela, modo, arquivo) | `scripts/slots.py` (lista S, tempos absolutos) → `python3 scripts/slots.py --real` (ou `--placeholders`) |
| foto / movimento de câmera do B-roll | `scripts/entrega.py` (foto e recorte por slot) → `scripts/make_broll.py` (zoom/pan por slot) |
| legenda baixa sobre B-roll | `capLowSegs` no plano |
| enquadramento do split | `splitShiftY` (medido: ___) |
| zoom do apresentador | `presenterZoom` (1,06/1,14, uma troca por aparição; `sceneMax` 4,5) |
| volumes de trilha/SFX | `trilhaVol` no plano / seção SFX de `scripts/build-edit.mjs` → `bake.py bed` |
| transições | `sections` e `leakMinGap` (3,5) no plano |
| bipe | `scripts/bipe.py` (JANELAS ___ s do source) → `bake.py voz` |
| respiro / lead do J-cut | `TA`/`HH` em `scripts/cuts.py`; `jcutLeadFrames` (9) / `jcutCrossfadeFrames` (3) |
| tempos de timeline / palavra | `python3 scripts/tl.py [--words]` |

## Bruto original

`~/Claude/videos-brutos/___` — **não alterado**. MD5 `___` (`work/md5-bruto.txt`).
Codec/resolução/fps/duração: ___ · HDR ou SDR full-range: ___

## Mezanino

`assets/__SLUG__-2560-sdr.mp4` — conversão usada: ___ · conferência de cor (média/desvio bruto × mezanino): ___
Voz: `assets/__SLUG__-voz.m4a` (com bipe). Voz limpa: `work/__SLUG__-voz-limpa.m4a`.

## Transcrição

Regiões: ___ · divisões nos vales: ___ · chunks: ___ · chunks reconstruídos do passe por região: ___
Mantido o que o áudio diz (≠ roteiro): ___ · Grafia do roteiro: ___

## Takes descartados (mantido sempre o ÚLTIMO)

- ___

## J-cut

`python3 scripts/jcut_check.py`: ___ emendas · buracos ___ · crossfade sobre fala ___ · lead de FALA ___ quadros · respiro mediano ___ s

## Bipe

Varredura da transcrição INTEIRA (inclusive takes descartados): ___ palavrão(ões).
Mapa de sílabas: ___ · **Bipe ___–___ s** do source · timeline ___ · aceite por medição na `voz-mix.m4a`: ___ · legenda `___`

## Varredura de olhar

1ª passada (B-roll em placeholder): ___ janelas / ___ s · nítidas: ___ · **leitura exposta: ___ s**
2ª passada (com os B-rolls reais): ___ · **leitura exposta: ___ s**

## Split-screen

`splitShiftY` ___ — olhos medidos em ___ · janelas de split: ___

## Marca só depois do áudio

1ª vez que o áudio diz "___": ___ s · pré-revelação: slots ___ · revelação entra em ___ s (2 quadros depois) ·
último quadro limpo ___ s / primeiro com marca ___ s

## Callouts

___

## Pesquisa e B-roll

`PESQUISAS-BROLL-___.md` · imagens geradas a pedido: ___ · `capLowSegs` ___ · callouts com `top`: ___

## Export final

`size_sweep.py`: `--size` ___ (sobra mínima ___ quadros) · partes ___ · falhas ___
**Resultado:** `renders/___-reel-final.mp4` — 1440×2560 · 60 fps · ___ s · ___ quadros · ___ MB
QC (`finalizar.py`): quadros = timeline ___ · pico ___ dB / média ___ dB · trechos pretos ___ · bipe no MP4 ___ ·
quadros-chave × preview ___ · bruto intacto (MD5 antes e depois) ___

## Correções depois do render

- ___

## Lições para o kit

O que este reel ensinou que vale para os próximos (número novo, armadilha, pedido do Fabio, script corrigido).
Cada item daqui tem que ser levado para `KIT-EDICAO-REEL` (docs/05 e, se mexeu em script, `modelo-projeto/scripts/`) antes de fechar o projeto.

- ___


---

# ARQUIVO: `ESTILO-DE-EDICAO.md`

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


---

# ARQUIVO: `docs/03-blueprint-casas-bahia.md`

# Blueprint numérico — vídeo original "Casas Bahia"

Mapa completo do vídeo de referência, extraído frame a frame do projeto CapCut do usuário. Use como gabarito de **proporções e ritmo** ao montar vídeos novos. Timeline-mestre: **2040 frames @ 30 fps (68s) a 1.0x** → 1.087x → **1877 frames (62.6s)**.

> ⚠️ **Documento histórico.** Os números aqui são os do vídeo-referência original (era CapCut/Palmier, 1.087x, legenda 46pt com contorno). Os valores **em vigor** — 1.1x, legenda 47px sem contorno com sombra-halo, split 44/56, etc. — estão em `calibracoes-e-armadilhas.md` e mandam sobre qualquer coisa deste arquivo.

## Mapa de B-rolls

| Janela (frames) | Conteúdo | Layout |
|---|---|---|
| 0–107 | Fachada de loja atual (tema apresentado) | SPLIT topo |
| 107–236 | Segundo B-roll do tema | SPLIT topo |
| 284–590 | Cena narrativa longa (escritório/burocracia) | TELA CHEIA |
| 686–744 | Continuação da cena narrativa (outro trim do mesmo vídeo) | TELA CHEIA |
| 922–1020 | Imagem estática histórica (screenshot/foto P&B) | TELA CHEIA |
| 1128–1271 | B-roll tema (vendedor) | SPLIT topo (2ª janela) |
| 1271–1441 | B-roll tema (banco) | SPLIT topo (2ª janela) |
| 1602–1864 | B-roll emocional (família feliz em casa) | TELA CHEIA (clímax) |

Fora dessas janelas: apresentador em tela cheia.

- SPLIT: no HyperFrames é `mode: "split"` no `edit-plan.json` — B-roll ocupa os 44% de cima, apresentador os 56% de baixo (`splitShiftY` enquadra o rosto)
- TELA CHEIA: `mode: "full"` — o cover-crop 9:16 é automático; `objectPosition` reenquadra quando o assunto sai da faixa visível
- No CapCut original os B-rolls de split tinham velocidade 0.5–0.8x para preencher a janela; no HyperFrames use `rate` (= duração_source / janela). **Atenção:** `rate < 1` reprova no gate de frames do `hyperframes render` — gerar a câmera lenta no próprio arquivo (`setpts`+`minterpolate`) e usar rate 1.0

## Transições light-leak (7)

Frames de início: **217, 363, 572, 724, 1000, 1422, 1844** — cada uma 21 frames, começando ~10 frames antes do ponto de corte que ela cobre. `blendMode screen`, áudio vinculado volume 0. Ficam em faixa própria acima do B-roll.

## Legendas (85 chunks no original)

Estilo (todos iguais):
```json
{"fontName": "Montserrat", "fontSize": 46, "color": "#FFFFFF",
 "borderColor": "#000000", "alignment": "center", "animation": "fadeIn",
 "transform": {"centerX": 0.5, "centerY": 0.44}}
```
Chunks de 1–4 palavras, sentence case, duração = janela da fala (5–64 frames). Exemplos reais: "O Carnê" / "que enxergou o" / "A Casas Bahia" / "pagava," / "não enxergava."

## Callouts (do original)

| Frame | Dur | Texto | Estilo |
|---|---|---|---|
| 594 | 46 | "MILHÕES\nDE BRASILEIROS" | 68pt bold, centerY 0.3, popIn |
| 712 | 29 | "CASA\nPRÓPRIA" | 68pt bold, centerY 0.3, popIn |

Colocados quando a voz fala o número/frase de impacto. Sempre na faixa MAIS ALTA.

## Mix de áudio (volumes exatos do original)

| Elemento | Janela (frames) | Volume |
|---|---|---|
| Trilha épica | 0–2040 contínua | automação -22 dB (→ -27 dB no final) |
| Intro: cinematic-opening | 0–95 | 0.25 → 0.19 |
| Intro: when-emphasizing-riser | 0–95 | 0.25 → 0.19 |
| Boom cinematic | 0–76 | 0.06 → 0.16 |
| Whoosh (pós-intro) | 90–121 | 0.35 |
| Drum-fill (virada da intro) | 187–221 | 0.166 |
| Swoosh (corte) | 217–237 | 0.095 |
| Whoosh (corte seção) | 414–427 | 0.35 |
| Swoosh | 560–589 | 0.092 |
| Whoosh (dupla) | 731–763 | 0.143 |
| Impact hit (virada) | 792–842 | 0.5 |
| Swoosh | 926–955 | 0.117 |
| Whoosh (dupla) | 1020–1051 | 0.35 |
| Swoosh | 1257–1286 | 0.056 |
| Whoosh+Swoosh | 1436–1463 | 0.083–0.085 |
| Impact (dupla, clímax) | 1555–1600 | 0.221 |
| Riser (build-up clímax) | 1637–1703 | 0.198 |
| Whoosh (CTA) | 1844–1861 | 0.149 |
| Voz | 0–2040 | 1.0 (com crossfades do J-cut) |
| Áudio original do bruto | — | 0 (mudo) |
| Áudio dos B-rolls | — | 0 (mudo) |

**Removido do formato:** percussion-ticks 0.6 sobre a fala densa (frames 427–506) — causava sensação de "áudio quebrado". Não repetir.

## J-cut (números do original)

- 43 clipes de voz (após remover 6 fillers de 1 frame) em 2 faixas: A=22, B=21
- Leads: 2–5 frames (média 4.8)
- Crossfades: 5 frames lineares em todos (fade-in e fade-out)
- Cobertura da voz: contínua 0→2040, zero buracos

## Export

- Bake mestre: H.264 1080p, 2040 frames
- Projeto final: baked a speed **1.087** → 1877 frames = 00:01:02:17 (bateu exatamente com o CapCut do usuário)
- No CapCut original o usuário usa 1.1x nos clipes; 1.087x no baked produz a mesma duração final


---

# ARQUIVO: `docs/08-storyboard-opcional.md`

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
