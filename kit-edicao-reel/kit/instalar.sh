#!/bin/zsh
# Instala o kit de edição de reel num Mac novo (Apple Silicon). Rodar no Terminal:
#   zsh /caminho/do/KIT-EDICAO-REEL/instalar.sh
# Pode rodar de novo quantas vezes quiser: o que já existe é pulado.
set -e
KIT_SRC="${0:A:h}"; KIT="$HOME/Claude/KIT-EDICAO-REEL"
echo "== 1/7 Homebrew =="
command -v brew >/dev/null || { echo "Falta o Homebrew. Instale com o comando de https://brew.sh (pede a senha do Mac) e rode este script de novo."; exit 1; }
echo "== 2/7 Ferramentas (ffmpeg, whisper-cpp, node, python 3.12) =="
for p in ffmpeg whisper-cpp node python@3.12; do brew list $p >/dev/null 2>&1 || brew install $p; done
echo "== 3/7 Kit em $KIT =="
mkdir -p "$HOME/Claude" "$HOME/Claude/reel-auto" "$HOME/Claude/videos-brutos"
if [ "$KIT_SRC" != "$KIT" ]; then
  [ -e "$KIT" ] && { echo "Já existe $KIT — renomeando o antigo para KIT-EDICAO-REEL.antigo-$(date +%Y%m%d%H%M)"; mv "$KIT" "$KIT.antigo-$(date +%Y%m%d%H%M)"; }
  cp -R "$KIT_SRC" "$KIT"
fi
echo "== 4/7 Python do kit (~/Claude/.venv-reel: numpy, opencv, Pillow, mediapipe 0.10.14) =="
PY=$(brew --prefix python@3.12)/bin/python3.12
[ -x "$HOME/Claude/.venv-reel/bin/python" ] || "$PY" -m venv "$HOME/Claude/.venv-reel"
"$HOME/Claude/.venv-reel/bin/pip" install -q --upgrade pip
"$HOME/Claude/.venv-reel/bin/pip" install -q numpy opencv-python Pillow mediapipe==0.10.14
echo "== 5/7 Modelo do Whisper (large-v3-turbo, 1,6 GB) =="
mkdir -p "$HOME/.cache/whisper"
M="$HOME/.cache/whisper/ggml-large-v3-turbo.bin"
[ -s "$M" ] || curl -L --fail -o "$M" https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin
echo "== 6/7 Skills do Claude Code =="
mkdir -p "$HOME/.claude/skills"
cp -R "$KIT/skill/edicao-reel-viral" "$KIT/skill/showreel-interface" "$HOME/.claude/skills/"
npx --yes hyperframes@0.8.64 skills update || echo "(skills do HyperFrames: rodar depois 'npx hyperframes skills update')"
echo "== 7/7 Conferência =="
bash "$KIT/verificar-instalacao.sh"
cat <<FIM

Pronto. Opcional:
  - Codex (para gerar a capa): instalar o Codex CLI e fazer login (ver COMECE-AQUI.md).
  - ~/Claude/reel-auto/.env com SERPER_API_KEY= / FAL_KEY= (só para a pesquisa por API e imagem no fal; o fluxo padrão não precisa).
Uso: abrir o Claude Code na pasta ~/Claude e mandar o prompt de docs/04-prompt-comando-unico.md.
FIM
