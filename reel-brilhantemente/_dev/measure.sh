#!/bin/bash
# uso: _dev/measure.sh FRAME T "sel1,sel2"  → JSON com [left,top,width,height] no instante T
cd "$(dirname "$0")/.." || exit 1
curl -s -o /dev/null http://127.0.0.1:8765/ || (python3 -m http.server 8765 --bind 127.0.0.1 >/dev/null 2>&1 &) ; sleep 0.6
"/root/.cache/hyperframes/chrome/chrome-headless-shell/linux-152.0.7977.30/chrome-headless-shell-linux64/chrome-headless-shell" --no-sandbox --disable-gpu --window-size=1920,1080 --virtual-time-budget=5000 --dump-dom "http://127.0.0.1:8765/_dev/harness.html?frame=$1&t=$2&measure=$3" 2>/dev/null | grep -o '<pre id="measure">[^<]*' | sed 's/<pre id="measure">//;s/&quot;/"/g'
