# EDICAO.md — mapa do projeto (reel Gordon Bethune)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
**Estado (2026-10-08): RENDERIZADO** — ver "Export final" no fim. Comando único sem parada, numa sessão do Claude Code **na nuvem**
(Linux, 4 núcleos, 16 GB).
Duração **96,324 s** · 35 takes · 1 bipe · 99 legendas · 5 callouts · 4 light-leaks (virada, clímax, CTA + gancho) · 11 SFX fixos + 93 da camada ·
9 slots (2 splits + 7 cenas de tela cheia na camada de motion, `work/mg/gen.py`) + o botão "Seguir" e a pergunta escrita no fim.

## Bruto e roteiro
`~/Claude/videos-brutos/gordon-bethune-bruto.mov` (iCloud `0d9U0mbEh4sLzCy9AfdkTE82Q`) — **não alterado**, MD5 `315a7609a78e94be2aba79493b4aa2aa`.
HEVC 1440x2560 @60, 143,17 s, SDR full-range → mezanino full→limited; cor bruto × mezanino (14,32/71,58/128,85 s): 121,68/121,68 ·
121,36/121,51 · 123,57/123,72, desvio 58,90/58,92 · 58,89/58,97 · 58,90/59,01 — não lavou. Roteiro: ClickUp > Cronograma > "Gordon Bethune"
(FINAL 07/10/2026, seção "Roteiro"; a "Nota de gravação" valeu para a edição).
Onde o áudio diverge do roteiro (vale o áudio; passe por região + whisper em recorte concordam, e o espectro confirma):
- **"por SETENTA E CINCO dólares"** (roteiro: "sessenta e cinco"; **o fato é US$ 65**). Nos dois takes (r27 e r28) há oclusão de /t/ e nenhum /s/ entre o
  "se" e o "enta" (108,11–108,25 e 113,46–113,58 s). Legenda "setenta e cinco" (o áudio); o valor NÃO aparece na camada de motion (a nota de dólar sem número).
- **"E COMENTA aqui embaixo: qual a regra…"** (roteiro: "E me conta aqui embaixo:"). Ordem /k/ → /m/ → /t/ no espectro (136,51 / 136,59 / 136,79 s) = "comenta".
- "Seu time **já fez** besteira, meu amigo?" (roteiro: "só faz") · "Se você paga **pro** seu time fazer besteira" (roteiro: "paga o seu time pra fazer") ·
  "parar de pagar seu time" (roteiro: "pagar o seu time").
- Homófonos (vale o roteiro): "amados dos" (whisper: "amado dos") · "queima o manual" ("Queimo manual") · "Seu atendente" ("Se o atendente").
**CTA de palavra-chave ("Comenta PALAVRA…"): não existe neste roteiro** (modelo v2.2: pergunta aberta no fim, sem palavra-chave). A pergunta foi gravada
inteira (r35), mas com "comenta" no lugar de "me conta".

## Takes descartados (mantido o ÚLTIMO válido)
r06 "Primeiro, premia que..." + r07 parte 2 "ele diz que o que você mede" (parou) → r07 parte 1 + r08 · r09 "Paga comissão só por venda..." → r10 ·
r12 "E porra do ca..." → r13 · r17 "Seu comercial ganha por venda, seu financeiro ganha por..." → r18 · r25 parte 2 "Gordon trocou" + r26 "Gordon trocou esse
bônus" + r27 "por setenta e cinco dólares pra..." → r28. Divisões nos vales: r07 em 34,97 · r18 em 72,78 · r21 em 82,22 · r24 em 93,45 e 97,38 · r25 em 102,69 ·
r34 em 132,18. "Gordon..." (r03) e "pegou a pior..." (r04) ficaram em takes separados (pausa de 0,24 s fala a fala, emendada no silêncio).

## Bipe
"porra" ("E a porra do calote fica com você, meu querido."): "E a" 53,78–53,93 · oclusão /p/ 53,94–54,09 · explosão 54,10 · "o" 54,11–54,28 · "rr" 54,29–54,33 ·
"a" 54,34–54,41 · /d/ de "do" 54,42. O whisper pôs a palavra ~0,3 s adiantada. Recortes cumulativos: de 54,42 em diante "do calote e fica com você" (nada da
palavra). Bipe **53,95–54,42** do source. Legenda `P****`. Apresentador em tela cheia no bipe (34,45–37,47), com o callout "O CALOTE FICA COM VOCÊ.".

## J-cut
34 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9 quadros (4,9–5,4) · respiro mediano 0,245 s (3 pausas curtas emendadas no silêncio).

## Olhar
`gaze_pose.py 2.0`: 16 janelas / 3,6 s; `gaze_windows`: 20 / 7,3 s. Folhas `gaze/me/g00-g02`: o apresentador olha para a câmera o tempo todo — só piscadas e
pálpebra baixando em fim de frase (a maior, 59,96–60,32 no "pequeno gafanhoto", é expressão). **Leitura exposta: 0 s.**

## Split
`splitShiftY` **385** (olhos y≈993 no mezanino em 12 pontos das janelas de split → 1377−992; `work/olhos_y.py`). Splits: capa 0–5,55 · virada 61,47–63,99.

## Marca só depois do nome
"Gordon" em 11,49 s → revelação em 11,56 (o 777 da Continental batizado "Gordon M. Bethune", com o anel no nome pintado no nariz + "GORDON BETHUNE ·
CEO · CONTINENTAL AIRLINES · 1994–2004"). Pré-revelação: a capa gerada e a cabine de um 767 com os pilotos de costas (sem marca visível) — nada da Continental.
"Bethune" não é falado (nota de gravação): aparece só na etiqueta.

## Camada de motion (work/mg/gen.py + work/mg/parts.py + work/mg/fotos.py) — dosagem Deming v2
Chip "PASSO N". Motion só em: PASSO 1/2/3 (chip + título) · a frase exata dele ("O QUE VOCÊ MEDE E PREMIA É O QUE VOCÊ RECEBE.", sobre a frota de 1994) ·
comissão por venda fechada × o cliente que não paga · COMERCIAL × FINANCEIRO · o manual riscado + "É POLÍTICA DA EMPRESA." · o painel da cabine (AR DESLIGADO,
DEVAGAR) · o bônus antigo (só o piloto) × o novo (a nota de dólar, PRA TODO MUNDO — sem o valor) · o ranking de pontualidade (TOP 5 = BÔNUS; a Continental sai
da última posição para o TOP 5) · o botão "Seguir" e a pergunta do fim. O resto é foto real (Commons, LICENCAS-FOTOS.txt).
Revelação: FALÊNCIA 1983 / FALÊNCIA 1990 carimbados sobre o 727 em Miami, 1994. Clímax: um DC-10 da Continental em 1996, inteiro na largura sobre ele mesmo
desfocado + "1996 · COMPANHIA AÉREA DO ANO" (Air Transport World).
Callouts: 1º digitado "FAZ O QUE / VOCÊ PAGA." (seg 2) · "PRA FAZER / BESTEIRA." (5) · "O CALOTE FICA / COM VOCÊ." (10) · "QUEM ESCREVEU / FOI VOCÊ." (21) ·
"OLHA O QUE / VOCÊ TÁ PAGANDO." (30). A pergunta escrita na tela de 91,60 ao fim (nota de gravação: "nos últimos 5 segundos").

> **Regra de ouro: nunca editar `index.html` à mão.**
```
editar assets/edit-plan.json (ou scripts/slots.py) -> python3 work/mg/fotos.py && python3 work/mg/gen.py -> zsh scripts/montar.sh <instantes>
(cortes: scripts/mkcut.py / cuts.py -> zsh scripts/fase2.sh · legendas: scripts/captions_fix_table.py -> zsh scripts/legendas.sh)
```

## Onde mexer em cada coisa

| Quero mudar… | Arquivo |
|---|---|
| cortes / takes (in/out) | `scripts/mkcut.py` (divisões/descartes) → `scripts/cuts.py` (lista TAKES) → `work/segs.json` → `python3 scripts/plan_segments.py` |
| texto de legenda | `scripts/captions_fix_table.py` (FIX/FIXT por chunk e índice de palavra) → `zsh scripts/legendas.sh` |
| callouts | `impacts` no plano (frase, seg, linhas, hold; o 1º com `style: typing`) |
| janelas de cobertura | `scripts/slots.py` (lista S, tempos absolutos; MG="*") → `zsh scripts/montar.sh` |
| fotos / recortes | `work/mg/fotos.py` (papel → arquivo bruto + recorte; a capa vem de `work/capa/capa.png`) |
| cenas da camada | `work/mg/gen.py` (F = foto por papel, OP = enquadramento, `fit()` = foto inteira sobre ela desfocada, CENAS) e `work/mg/parts.py` (CSS) |
| enquadramento do split | `splitShiftY` (medido: 385 — `work/olhos_y.py`) |
| transições | `sections` (após os segs 21, 27, 30) e `leakMinGap` (3,5) no plano |
| bipe | `scripts/bipe.py` (JANELAS 53,95–54,42 s do source) → `bake.py voz` |
| tempos de timeline / palavra | `python3 scripts/tl.py [--words]` |

## Export final

`size_sweep.py`: `--size` **445** (13 partes, sobra mínima 145 quadros) · `render-par.sh 445 … 2` (2 em paralelo, 4 núcleos) · 0 falhas · **1533 s** (~4 min por par)
com a capa provisória (o login do Codex só saiu no 5º código) + re-render só das partes 0–2 (431 s) com a capa gerada (a capa aparece de 0 a 10,2 s e em 16,3–18,7 s).
**Master:** `renders/Gordon-Bethune-reel-final.mp4` — 1440×2560 · 60 fps · 96,33 s · 5780 quadros (= timeline) · 239 MB (fora do git).
QC (`finalizar.py` + `work/qc_final.sh`): quadros = timeline OK · pico −0,9 dB / média −19,2 dB · trechos pretos 0 · bipe achado na voz-mix em 34,49–34,92 s:
no MP4 99,6% em 950–1050 Hz e 0,4% fora de 900–1100 Hz (na `voz-mix.m4a` 100%) · sincronia boca/voz lag mediano 10 ms (30/31 pontos com r > 0,6; faixa −30..10 ms)
· bruto intacto (MD5 antes e depois `315a7609a78e94be2aba79493b4aa2aa`). Quadro a quadro: 80 quadros do MP4 (um por cena/transição, `work/qc/folha-1..4.jpg`)
conferidos; quadro 0 = capa; revelação 2 quadros depois de "Gordon".
**Entregas (a partir do master, `work/entregas.sh`):** `entrega/Gordon-Bethune-reel-chat.mp4` (x264 dois passes 2,1 Mbps, AAC 160k; **27,7 MB**) ·
`entrega/Gordon-Bethune-reel-final.mp4` (HEVC libx265 dois passes **7,7 Mbps** — reel de 96,3 s > ~95 s, o bitrate desceu para caber —, `hvc1`, AAC 256k 48 kHz,
`+faststart`) · `entrega/comparacao-master-x-hevc.jpg` (quadro 769 = 12,82 s, o 777 com o nome dele + etiqueta, master × HEVC). Final: **96,4 MB**, 7,73 Mbps de vídeo,
5780 quadros, `moov` antes do `mdat`; SSIM do vídeo inteiro **0,994**.

## Correções depois do render

- Capa provisória → capa gerada (partes 0–2 refeitas; `render-par.sh` retomou as outras 10).

## Lições para o kit (entraram em docs/05 §34)

- Número falado diferente do roteiro e do fato ("setenta e cinco" × US$ 65): legenda com o áudio, valor fora da camada de motion, aviso na entrega.
- "me conta" × "comenta": decidir pela ordem /k/ → /m/ no espectro; card da pergunta com cabeçalho neutro.
- Pessoa-tema sem retrato livre: o avião batizado com o nome dele + anel no nome (Ken Burns no container).
- Foto horizontal ≤ 1280 px: `fit()` (inteira na largura sobre ela mesma desfocada).
- `wmq.py` e `wmtitles.py` (novos no modelo) · link do iCloud recém-criado vem vazio por alguns minutos (laço de 20 s) · GSAP 3 sem `className`.
