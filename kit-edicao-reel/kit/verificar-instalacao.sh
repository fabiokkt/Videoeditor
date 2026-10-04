#!/usr/bin/env bash
# Teste de fumaça do kit (v3). Confere o ambiente e reconstrói o reel de referência (só o HTML).
# Uso: bash verificar-instalacao.sh
set -uo pipefail
KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ok=0; fail=0; aviso=0
# grep -q + pipefail = SIGPIPE no ffmpeg; ler a saída inteira evita o falso negativo
hasfilter() { ffmpeg -hide_banner -filters 2>/dev/null | grep -w "$1" >/dev/null; }
chk() { if eval "$2" >/dev/null 2>&1; then printf "  ✓ %s\n" "$1"; ok=$((ok+1)); else printf "  ✗ %s  → %s\n" "$1" "$3"; fail=$((fail+1)); fi; }
opc() { if eval "$2" >/dev/null 2>&1; then printf "  ✓ %s\n" "$1"; ok=$((ok+1)); else printf "  ! %s  → %s\n" "$1" "$3"; aviso=$((aviso+1)); fi; }

echo "== Ferramentas =="
chk "node >= 20"        '[ "$(node -p "process.versions.node.split(\".\")[0]")" -ge 20 ]' "instale Node 20+"
chk "ffmpeg em /opt/homebrew/bin" '[ -x /opt/homebrew/bin/ffmpeg ] && [ -x /opt/homebrew/bin/ffprobe ]' "brew install ffmpeg (o render-chunks.mjs usa esse caminho)"
for f in colorspace scale setpts silencedetect volumedetect blackdetect alimiter atempo zoompan; do
  chk "filtro $f" "hasfilter $f" "ffmpeg sem o filtro $f"
done
chk "whisper-cli"       "command -v whisper-cli" "brew install whisper-cpp"
chk "modelo whisper (large-v3-turbo ou large-v3)" '[ -f "$HOME/.cache/whisper/ggml-large-v3-turbo.bin" ] || [ -f "$HOME/.cache/whisper/ggml-large-v3.bin" ]' "zsh instalar.sh (baixa o ggml-large-v3-turbo.bin)"
chk "python do kit (~/Claude/.venv-reel) + numpy, cv2, PIL, mediapipe" '"$HOME/Claude/.venv-reel/bin/python" -c "import numpy, cv2, PIL, mediapipe"' "zsh instalar.sh (cria o venv com python 3.12 + mediapipe 0.10.14)"
chk "zsh"               "command -v zsh" "os scripts .sh do kit são zsh"

echo "== Kit =="
chk "scripts do modelo (>= 53)" '[ "$(ls "$KIT"/modelo-projeto/scripts | wc -l)" -ge 53 ]' "modelo-projeto/scripts incompleto"
chk "fontes (Montserrat 600/800 + Oswald 700)" '[ "$(ls "$KIT"/assets-fixos/fonts/*.woff2 | wc -l)" -ge 6 ]' "faltam fontes em assets-fixos/fonts/"
chk "trilha + 9 SFX + light-leak" '[ -f "$KIT/assets-fixos/trilha/trilha-epic-cinematic-corporate.mp3" ] && [ "$(ls "$KIT"/assets-fixos/sfx/ | wc -l)" -ge 9 ] && [ -f "$KIT/assets-fixos/fx/transicao-light-leak.mp4" ]' "assets-fixos incompleto"
chk "modelo FaceLandmarker" '[ -f "$KIT/assets-fixos/models/face_landmarker.task" ]' "falta assets-fixos/models/face_landmarker.task"
chk "sintaxe dos scripts .py" 'for f in "$KIT"/modelo-projeto/scripts/*.py; do python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" "$f" || exit 1; done' "erro de sintaxe em modelo-projeto/scripts"
chk "sintaxe dos scripts .mjs" 'for f in "$KIT"/modelo-projeto/scripts/*.mjs; do node --check "$f" || exit 1; done' "erro de sintaxe em modelo-projeto/scripts"

echo "== Ambiente (opcional) =="
chk "skill showreel-interface (sfx.py da camada)" '[ -f "$HOME/.claude/skills/showreel-interface/scripts/sfx.py" ]' "cp -R skill/showreel-interface ~/.claude/skills/"
opc "skill edicao-reel-viral" '[ -f "$HOME/.claude/skills/edicao-reel-viral/SKILL.md" ]' "cp -R skill/edicao-reel-viral ~/.claude/skills/"
opc "codex (capa a pedido)" "command -v codex" "opcional: instalar o Codex CLI e fazer login"
opc "skills do HyperFrames" '[ -d "$HOME/.claude/skills/hyperframes-core" ]' "npx hyperframes skills update"
opc "chaves de API (.env)" '[ -f "${REEL_ENV:-$HOME/Claude/reel-auto/.env}" ]' "sem ~/Claude/reel-auto/.env a pesquisa no Google Imagens e a imagem-conceito não rodam"
opc "kit em ~/Claude/KIT-EDICAO-REEL" '[ "$KIT" = "$HOME/Claude/KIT-EDICAO-REEL" ]' "docs e CLAUDE.md dos projetos apontam para ~/Claude/KIT-EDICAO-REEL"
opc "servidor montado" '[ -d "/Volumes/Company/Equipe/FABIO KENJI" ]' "share Company não montado (só para backup e brutos)"

echo "== novo-projeto.sh + build de referência (reel Kazuo Inamori) =="
TMP="$(mktemp -d)"
if REEL_DIR="$TMP" zsh "$KIT/novo-projeto.sh" teste-fumaca "Kazuo Inamori" >/dev/null 2>&1 && [ -f "$TMP/teste-fumaca/scripts/build-edit.mjs" ]; then
  printf "  ✓ novo-projeto.sh criou o projeto\n"; ok=$((ok+1))
  P="$TMP/teste-fumaca"; E="$KIT/exemplos/kazuo-inamori"
  cp "$E/assets/edit-plan.json" "$P/assets/"; cp "$E"/assets/chunks/*.json "$P/assets/chunks/"
  OUT="$(cd "$P" && node scripts/build-edit.mjs 2>&1)"
  ESP="OK: 41 segs, 98.275s, 4 cenas de broll (21 tomadas), 25 sfx, 101 legendas, 9 callouts, 18 leaks, J-cut 9f/3f."
  if [ "$OUT" = "$ESP" ]; then printf "  ✓ gerador: %s\n" "$OUT"; ok=$((ok+1)); else printf "  ✗ build divergiu\n    esperado: %s\n    obtido:   %s\n" "$ESP" "$OUT"; fail=$((fail+1)); fi
  # o Studio reescreve o index.html do projeto ao salvar (data-hf-id, <br>, &#160;): normaliza os dois lados antes de comparar
  norm() { sed -E -e 's/ data-hf-id="[^"]*"//g' -e 's#<br/>#<br>#g' -e 's/&#160;/\&nbsp;/g' "$1"; }
  if diff <(norm "$P/index.html") <(norm "$E/index.html") >/dev/null; then printf "  ✓ index.html igual ao de referência\n"; ok=$((ok+1)); else printf "  ✗ index.html difere do de referência (exemplos/kazuo-inamori/index.html)\n"; fail=$((fail+1)); fi
else
  printf "  ✗ novo-projeto.sh falhou\n"; fail=$((fail+1))
fi
rm -rf "$TMP"

echo
echo "== $ok ok · $aviso aviso(s) · $fail falha(s) =="
[ "$fail" -eq 0 ]
