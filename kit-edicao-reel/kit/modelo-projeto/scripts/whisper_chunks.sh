#!/bin/zsh
M=$HOME/.cache/whisper/ggml-large-v3.bin
for w in assets/chunks/ch*.wav; do
  b=${w%.wav}
  whisper-cli -m $M -l pt --max-context 0 -ml 1 -sow -oj -of ${b}-words -f $w > work/whc-${b:t}.log 2>&1 || echo "FALHOU $b"
done
echo "json: $(ls assets/chunks/ch*-words.json | wc -l) / wav: $(ls assets/chunks/ch*.wav | wc -l)"
