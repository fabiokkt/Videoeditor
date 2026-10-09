#!/bin/bash
# Script de configuração do ambiente na nuvem (Claude Code) para o KIT-EDICAO-REEL.
# Colar em: menu do ambiente → Edit → "Script de configuração". Roda antes de cada sessão nova.
# Deixa o container Linux igual ao Mac do kit: ferramentas, venv, whisper, HyperFrames, Codex e adaptadores do macOS.
# Idempotente: o que já existe é pulado. Log em /tmp/reel-setup.log.
exec > >(tee -a /tmp/reel-setup.log) 2>&1
echo "== reel-setup $(date -u +%FT%TZ)"
export DEBIAN_FRONTEND=noninteractive

# 1. pacotes do sistema (zsh dos scripts do kit, EGL do mediapipe, certutil, git-lfs)
APT="apt-get install -y -q -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold"
dpkg --configure -a --force-confdef --force-confold >/dev/null 2>&1
$APT zsh libegl1 libgles2 libgl1 libnss3-tools git-lfs >/dev/null 2>&1 \
  || { apt-get update -q >/dev/null 2>&1; $APT zsh libegl1 libgles2 libgl1 libnss3-tools git-lfs >/dev/null 2>&1; } \
  || echo "AVISO: apt falhou"

# 2. venv do kit (~/Claude/.venv-reel): numpy, opencv, Pillow, mediapipe, scipy (o sfx.py da skill importa)
V=$HOME/Claude/.venv-reel
[ -x $V/bin/python ] || python3 -m venv $V
$V/bin/pip install -q --disable-pip-version-check --timeout 60 --retries 2 numpy opencv-python-headless Pillow mediapipe scipy fonttools brotli || echo "AVISO: pip falhou"

# 3. whisper.cpp + modelo large-v3-turbo (~1,6 GB)
if ! command -v whisper-cli >/dev/null; then
  mkdir -p $HOME/src && cd $HOME/src
  [ -d whisper.cpp ] || git clone -q --depth 1 https://github.com/ggml-org/whisper.cpp
  cd whisper.cpp && cmake -B build -DCMAKE_BUILD_TYPE=Release -DWHISPER_BUILD_TESTS=OFF >/dev/null \
    && cmake --build build -j"$(nproc)" --target whisper-cli >/dev/null \
    && ln -sf $HOME/src/whisper.cpp/build/bin/whisper-cli /usr/local/bin/whisper-cli || echo "AVISO: whisper.cpp falhou"
fi
M=$HOME/.cache/whisper/ggml-large-v3-turbo.bin
[ -s $M ] || { mkdir -p $(dirname $M); curl -sSL -o $M https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin || echo "AVISO: modelo falhou"; }

# 4. HyperFrames (0.8.64 no projeto, 0.8.48 no render-chunks.mjs) + Chrome do render; Codex CLI
cd /tmp
npx --yes hyperframes@0.8.64 --version >/dev/null 2>&1 || echo "AVISO: hyperframes 0.8.64"
npx --yes hyperframes@0.8.48 --version >/dev/null 2>&1 || echo "AVISO: hyperframes 0.8.48"
npx --yes hyperframes@0.8.64 browser ensure >/dev/null 2>&1 || echo "AVISO: chrome do hyperframes"
command -v codex >/dev/null || npm i -g @openai/codex >/dev/null 2>&1 || echo "AVISO: codex"

# 5. CA do proxy no NSS do Chrome (sem isso o GSAP não carrega: "gsap is not defined" no check)
if [ -f /root/.ccr/agent-proxy-ca.crt ]; then
  mkdir -p $HOME/.pki/nssdb
  [ -f $HOME/.pki/nssdb/cert9.db ] || certutil -N -d sql:$HOME/.pki/nssdb --empty-password
  certutil -L -d sql:$HOME/.pki/nssdb 2>/dev/null | grep -q ccr-agent-proxy \
    || certutil -A -d sql:$HOME/.pki/nssdb -n ccr-agent-proxy -t "C,," -i /root/.ccr/agent-proxy-ca.crt
fi

# 6. adaptadores do macOS (o motor do kit fica intacto)
mkdir -p /opt/homebrew/bin /System/Library/Fonts/Supplemental /System/Volumes/Data
ln -sf /usr/bin/ffmpeg /opt/homebrew/bin/ffmpeg; ln -sf /usr/bin/ffprobe /opt/homebrew/bin/ffprobe
ln -sf /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf /System/Library/Fonts/Helvetica.ttc
ln -sf /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
ln -sf /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf /System/Library/Fonts/Supplemental/Arial.ttf
cat > /usr/local/bin/md5 <<'EOS'
#!/bin/sh
# macOS md5 -> md5sum. "md5 -q arq" imprime só o hash.
[ "$1" = "-q" ] && shift && exec sh -c 'md5sum "$1" | cut -d" " -f1' _ "$1"
for f in "$@"; do echo "MD5 ($f) = $(md5sum "$f" | cut -d' ' -f1)"; done
EOS
cat > /usr/local/bin/sed <<'EOS'
#!/bin/bash
# BSD "sed -i '' ..." -> GNU "sed -i ..."; o resto passa direto para /usr/bin/sed
a=(); skip=0
for x in "$@"; do if [ $skip = 1 ]; then skip=0; [ -z "$x" ] && continue; fi; [ "$x" = "-i" ] && skip=1; a+=("$x"); done
exec /usr/bin/sed "${a[@]}"
EOS
chmod +x /usr/local/bin/md5 /usr/local/bin/sed
# bake.py sem VideoToolbox (Mac) -> x264
grep -q BAKE_X264 /etc/environment 2>/dev/null || echo "BAKE_X264=1" >> /etc/environment
for rc in $HOME/.zshenv $HOME/.bashrc; do grep -q BAKE_X264 $rc 2>/dev/null || echo "export BAKE_X264=1" >> $rc; done

# 7. caminhos do kit: ~/Claude/KIT-EDICAO-REEL e a skill showreel-interface (o mg_sfx.py importa o sfx.py dela)
KIT=$(ls -d /home/user/*/kit-edicao-reel/kit 2>/dev/null | head -1)
if [ -n "$KIT" ]; then
  mkdir -p $HOME/Claude/reel-auto $HOME/Claude/videos-brutos $HOME/.claude/skills
  ln -sfn "$KIT" $HOME/Claude/KIT-EDICAO-REEL
  [ -e $HOME/.claude/skills/showreel-interface ] || ln -s "$KIT/skill/showreel-interface" $HOME/.claude/skills/showreel-interface
else
  echo "AVISO: kit-edicao-reel não encontrado (o repositório ainda não foi clonado?) — o Claude cria os links no início da sessão"
fi
echo "== reel-setup OK"
