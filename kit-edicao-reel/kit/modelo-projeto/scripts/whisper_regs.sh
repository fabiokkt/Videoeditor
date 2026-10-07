#!/bin/zsh
# Transcricao por REGIAO, palavra a palavra. Kit v3: large-v3-TURBO por padrao (2,3x mais rapido, mesmo texto em PT
# medido no reel Alan Mulally: 11 s x 26 s em 5 regioes). WHISPER_MODEL=<caminho> troca o modelo; sem o turbo cai no large-v3.
# Serial: nunca junto com encode pesado.
M=${WHISPER_MODEL:-$HOME/.cache/whisper/ggml-large-v3-turbo.bin}
[ -f "$M" ] || M=$HOME/.cache/whisper/ggml-large-v3.bin
echo "whisper: ${M:t}"
for w in work/reg/r*.wav; do
  b=${w%.wav}; n=${b:t}
  whisper-cli -m $M -l pt --max-context 0 -ml 1 -sow -oj -of $b -f $w > work/wh-$n.log 2>&1 || echo "FALHOU $n"
done
echo "json: $(ls work/reg/r*.json | wc -l) / wav: $(ls work/reg/r*.wav | wc -l)"
