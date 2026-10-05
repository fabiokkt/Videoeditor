#!/bin/bash
cd "$(dirname "$0")"   # uso: bash work/cxlogin.sh (tarefa de fundo); o codigo atual fica em work/codex-login3.log
for i in 1 2 3 4 5 6; do
  codex login --device-auth > codex-login3.log 2>&1
  codex login status 2>&1 | grep -qi "logged in" && ! codex login status 2>&1 | grep -qi "not logged" && break
done
codex login status
