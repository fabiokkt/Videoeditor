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
