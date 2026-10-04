# EDICAO.md — mapa do projeto (reel Rich Diviney)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
Kit v3 (fluxo rápido, docs/14) + camada de motion (showreel-interface), na dosagem do Deming v2.
Editado numa sessão do Claude Code **na nuvem** (Linux, 4 núcleos, sem GPU), com o kit da branch `claude/reel-stockdale-protocolo`.
**Estado (2026-10-04): RENDERIZANDO** (`renders/Rich-Diviney-reel-final.mp4`), comando único sem parada.
Duração **92,944 s** · 31 takes · 1 bipe · 95 legendas · 5 callouts · 3 seções com light-leak · 11 SFX fixos + 68 SFX da camada ·
14 slots (2 splits + 12 cenas de tela cheia na camada de motion).

> A camada sai de `work/mg/gen.py` (`python3 work/mg/gen.py`), depois `zsh scripts/montar.sh`. Nunca editar `compositions/mg.html` à mão.

> **Regra de ouro: nunca editar `index.html` à mão.**
```
editar assets/edit-plan.json (ou scripts/slots.py para B-roll)  ->  node scripts/build-edit.mjs  ->  python3 scripts/bake.py <alvos>  ->  npm run check
(bake.py sem argumento = cenas, brollfull, leaks, voz, bed, aroll; mudou só B-roll: bake.py cenas brollfull leaks bed)
```

## Bruto
`~/Claude/videos-brutos/rich-diviney-bruto.mov` (link iCloud `038ip7G-fEJqsd-2nSBhMoDbQ`) — **não alterado**.
MD5 `5446f98bed1fd3a63c8248bacd1a85ee`. HEVC 1440x2560 @60, 132,7 s, **SDR full-range** (`yuvj420p`/`pc`) → mezanino full→limited.
Cor bruto × mezanino (13,3/66,3/119,4 s): 150,96/151,05 · 151,30/151,41 · 151,04/151,05; desvio igual (73,00/72,99…) — não lavou.

## Sem roteiro escrito
Legendas seguem o áudio, com a grafia do formato ("pra"). Whisper ouviu "CEOs"/"CIUS": o áudio diz **SEALs** (confirmado no large-v3).

## Takes descartados (mantido o ÚLTIMO)
r00 fim "Rick." + r01 "Rich escolhia quem entrava na elite da…" → r02 · r02 fim "E esse é o protocolo… de apaixonar" → r03 (com o "se") ·
r03 fim "primeiro" + r04 "Se você…" → r05 · r07 "E só isso que você…" → r08 · r13 "Na entrevista, me conta." → r14 ·
r17 fim "ele tinha uma marinheira" → r18 · r21 "Ele conta que um moleque…" → r22 · r28 "Se você se ia…" → r29.
Ficam (não são retake): "Coragem. Coragem de aparecer ali…" (ênfase) e o 2º "Nadar, a gente ensina." (fecho do roteiro).

## Bipe
"merda" ("quando dá merda"): nasal /m/ 60,26–60,34 · "er" 60,35–60,49 · /d/ 60,50 · "a" até 60,68 · decaimento até 60,74.
Whisper em recortes cumulativos: até 60,25 "…quando dá"; até 60,36 "…quando dá medo"; até 60,75 "…quando dá merda".
Bipe **60,255–60,745** do source. Medido na voz-mix: **99,8% em 950–1050 Hz, 0,05% fora de 900–1100**. Legenda `M****`.
Apresentador em tela cheia no bipe (40,40–42,30).

## J-cut
30 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9–5,1 quadros · respiro mediano 0,245 s (min 0,236).

## Olhar
`gaze_pose.py 2.0`: 16 janelas / 4,2 s; folhas `gaze/me/g00–g02` (28 janelas). Nítidas (todas cobertas por tela cheia):
20,8–21,9 · 30,5–30,9 · 74,3–74,8 · 75,6–75,8 · 87,6–87,8. Sutis expostas: 63,3–63,5 e 89,0–89,8 (começo do CTA).
**Leitura exposta: ~0,9 s.**

## Split
`splitShiftY` **345** (olhos y≈1031 no aroll em 561 amostras das janelas de split → 1377−1032). Splits: capa 0–10,97 · virada 65,15–71,19.

## Marca só depois do nome
"Rich" em 10,90 s → revelação em 10,97. Antes: só fotos de treino BUD/S sem o Rich (onda, arrebentação, sino).

## Camada de motion (work/mg/gen.py)
Chip = "PASSO N" (verde/amarelo/vermelho). Prova = fotos da Marinha dos EUA como card/tela cheia + retrato do Rich.
Frase que o final inverte: a capa (bote furando a onda) volta em "Nadar a gente ensina".
Motion só em: 10 candidatos/metade reprovava · currículo apaixonado → PASSO 1 · "a vaga pede" (planilha dá / paciência não dá) ·
PASSO 2 · pergunta da entrevista · PASSO 3 · ficha do candidato no clímax (≈40% da cobertura).
Callouts: 1º digitado "PODE SER O QUE / NÃO SABE FAZER / O TRABALHO." (seg 1) · "CURRÍCULO / SÓ MOSTRA O QUE / DÁ PRA ENSINAR." (7) ·
"VOCÊ PRECISA / VER O PIOR." (16) · "TÁ NA CADEIRA / ERRADA." (21) · "VOCÊ REPROVA / ESSE MOLEQUE?" (28).

## Imagens (LICENCAS-FOTOS.txt)
15 fotos da U.S. Navy/DoD via Wikimedia Commons (domínio público). **Pendência:** `rich-retrato.jpg` é foto de divulgação
(direitos reservados) — decidir com o Fabio. Nenhuma de banco, nenhuma com marca d'água, nenhuma gerada por IA.

## Ambiente (container Linux, não o Mac)
Adaptadores: `~/Claude/mac-compat/bin` (`md5`, `sed -i ''`, `whisper-cli`), `/opt/homebrew/bin/ff*` → `/usr/bin`, fontes do macOS →
DejaVu, `/System/Volumes/Data`, `BAKE_X264=1`, CA do proxy no NSS do Chrome (`~/.pki/nssdb`, `certutil`), skill showreel-interface
copiada para `~/.claude/skills/` (o `mg_sfx.py` importa o `sfx.py` dela).

## Lições para o kit
- `montar.sh`: `mg_sfx.py | head -1` dá BrokenPipe no print final (a mistura já foi gravada) → trocado por `tail -1` neste projeto.
- Os splits saem pela camada, mas o `ritmo.py` não conta os eventos dela (acusa "SEM EVENTO" em trechos cobertos pela camada).
