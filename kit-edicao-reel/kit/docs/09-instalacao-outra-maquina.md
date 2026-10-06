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
