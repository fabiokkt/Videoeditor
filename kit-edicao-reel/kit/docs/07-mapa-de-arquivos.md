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
