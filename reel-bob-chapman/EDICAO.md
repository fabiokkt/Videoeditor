# EDICAO.md — mapa do projeto (reel Bob Chapman)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
**Estado (2026-10-08): RENDERIZADO** — ver "Export final" no fim. Comando único sem parada, numa sessão do Claude Code **na nuvem**
(Linux, 4 núcleos, 16 GB).
Duração **90,107 s** · 31 takes · 1 bipe · 94 legendas · 5 callouts · 3 seções (virada, clímax, CTA) · 12 SFX fixos + 89 da camada ·
10 slots (2 splits + 8 cenas de tela cheia na camada de motion, `work/mg/gen.py`) + o botão "Seguir".

## Bruto e roteiro
`~/Claude/videos-brutos/bob-chapman-bruto.mov` (iCloud `051bJhkxfEiL51vMO_8l4TEqQ`) — **não alterado**, MD5 `f1247c47b04519b1123a9e9150751092`.
HEVC 1440x2560 @60, 138,33 s, SDR full-range → mezanino full→limited; cor bruto × mezanino (13,83/69,17/124,5 s): 111,11/111,11 ·
110,55/110,71 · 112,02/112,03, desvio 63,99/63,98 · 63,14/63,13 · 62,37/62,36 — não lavou. Roteiro: ClickUp > Cronograma > "Bob Chapman"
(v1 07/10/2026, seção "Roteiro"; a "Nota de gravação" valeu para a edição: pausa antes de "É o filho de alguém" com o callout de digitação no
rosto dele, o conselheiro impaciente com o apresentador na tela, "você demitiu ou dividiu" olhando pra câmera).
Onde o áudio diverge do roteiro (vale o áudio; passe por região + whisper em recorte sem prompt concordam):
- **"E na última crise, você demitiu ou dividiu, meu amigo?"** (roteiro: "Na última crise…"): o "E" está no áudio.
Grafia/homófonos (vale o roteiro): "pra" (whisper: "para") · "já **tá** respondendo" (whisper: "está"; não há /s/ entre o "já" e o "tá", 49,98–50,25 s) ·
"se você trata **gente** como despesa" (whisper: "trata a gente"; o "a" funde com o fim de "trata") · números por extenso ("três", "quarenta por cento").
"mais **bobos**" é o que o roteiro e o áudio dizem (a nota de gravação fala em "bonzinhos"; ele gravou "bobos").
**CTA de palavra-chave ("Comenta PALAVRA…"): não existe neste roteiro** ("sem palavra-chave falada e sem pergunta de comentário"); nada foi gravado.

## Takes descartados (mantido o ÚLTIMO válido)
r01 "Bob herdou … três bilhões e meio…" (parou) → r02 · r02 parte 3 "Primeiro, escuta de verdade. Ele pagava um curso…" → r03 "Primeiro" + r04 ·
r06 "Segundo, faz o teste do pai." + r07 "Ele viu um pai entregando a filha no **alto mar**" (tropeçou) → r08 + r09 · r12 parte 2 "Ele dizia que o jeito…"
→ r13 · r14 "Ele pensou, o que eu…" → r15 · r16 "Todo mundo!" → r17 · r17 parte 2 "E teve o funcion…" → r18.
Divisões nos vales: r00 em 6,60 e 11,415 · r02 em 25,99 e 30,06 · r04 em 44,50 · r10 em 68,00 · r12 em 76,35 · r13 em 86,83 / 90,30 / 93,25 / 95,30 / 99,13 ·
r17 em 116,45 · r19 em 125,475 · r21 em 131,69. `WFIX`: "E ele" (6,57 → 6,80) e "O conselho" (98,94 → 99,27) caíam no pedaço errado.

## Bipe
"porra" ("Você deu a porra de um esporro na frente de todo mundo?"): "eu a" 87,29–87,50 · oclusão /p/ 87,52–87,71 · explosão 87,72 · "o" 87,73–87,92 ·
"rr" 87,93–87,96 · "a" 87,97–88,07 · /d/ de "de" 88,08. O whisper pôs a palavra ~0,4 s adiantada (87,29–87,54). Recortes cumulativos: até 87,53
"Você deu a…"; de 88,08 "Um esporro na frente de todo mundo". Bipe **87,52–88,08** do source. Legenda `P****`. Apresentador em tela cheia no bipe, com o
callout "NA FRENTE DE / TODO MUNDO?".

## J-cut
30 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9 quadros (4,9–5,4) · respiro mediano 0,245 s (5 pausas curtas emendadas no silêncio).

## Olhar
`gaze_pose.py 2.0`: 17 janelas / 4,2 s; `gaze_windows`: 23 / 8,7 s. Folhas `gaze/me/g00-g02`: o apresentador olha para a câmera o tempo todo — piscadas,
sobrancelha e expressão. Varredura do `gaze/tl.json` nos trechos com ele VISÍVEL (docs/05 §33): só 84,33–84,75 (ele se inclina para a lente no "demitiu ou
dividiu", olho na câmera: gesto). **Leitura exposta: 0 s.**

## Split
`splitShiftY` **400** (olhos y≈980 no mezanino em 12 pontos das janelas de split → 1377−978/975; `work/olhos_y.py`). Splits: capa 0–5,74 · virada 57,29–62,36.

## Marca só depois do nome
"Bob" em 11,01 s → revelação em 11,08 (a capa: ele de costas diante da parede de crachás + "BOB CHAPMAN · BARRY-WEHMILLER · DESDE 1975").
Pré-revelação: a capa (silhueta genérica) e dois operários de 1942 — nada do Bob nem da Barry-Wehmiller. Sem retrato livre dele e sem logotipo (pedido
da tarefa: nada de logotipo nem referência à morte dele).

## Camada de motion (work/mg/gen.py + work/mg/parts.py + work/mg/fotos.py) — dosagem Deming v2
Chip "PASSO N". Motion só em: PASSO 1/2/3 (chip + título) · o contador US$ 3,5 BILHÕES · a frase dele ("CHEFE FALA. LÍDER ESCUTA.", sobre o curso) ·
FUNCIONÁRIO riscado → O FILHO QUERIDO DE ALGUÉM (sobre o rapaz do torno) · o gráfico da crise no split (pedidos 2008 × 2009, −40%) · as semanas sem salário
(ELE × O COLEGA: a semana do colega que não ia aguentar passa pra ele, a do colega vira PAGA) · o botão "Seguir". O resto é foto real da Library of Congress
(FSA/OWI e Matson, domínio público — LICENCAS-FOTOS.txt). ~37% da cobertura em UI.
Clímax = callback da capa: a parede de crachás todos no lugar + "0 DEMITIDOS" + "2010 · RECORDE DE LUCRO".
Callouts: 1º digitado "É O FILHO / DE ALGUÉM." (seg 2, no rosto dele: o primeiro pico da nota) · "VOCÊ JÁ TÁ / RESPONDENDO." (8) · "NA FRENTE DE /
TODO MUNDO?" (16, bipe) · "NÃO VAI DEMITIR / NINGUÉM?" (20, o conselheiro impaciente) · "VOCÊ DEMITIU / OU DIVIDIU?" (27).
`ritmo.py`: maior intervalo sem evento 4,08 s (o apresentador em "pequeno gafanhoto", 39,95–44,03).

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
| fotos / recortes | `work/mg/fotos.py` (papel → arquivo + recorte; a capa vem de `work/capa/capa.png`) |
| cenas da camada | `work/mg/gen.py` (F = foto por papel, OP = enquadramento, CENAS) e `work/mg/parts.py` (CSS) |
| enquadramento do split | `splitShiftY` (medido: 400 — `work/olhos_y.py`) |
| transições | `sections` (após os segs 17, 23, 27) e `leakMinGap` (3,5) no plano |
| bipe | `scripts/bipe.py` (JANELAS 87,52–88,08 s do source) → `bake.py voz` |
| tempos de timeline / palavra | `python3 scripts/tl.py [--words]` |

## Export final

`size_sweep.py`: `--size` **451** (12 partes, sobra mínima 147 quadros) · `render-par.sh 451 … 2` (2 em paralelo, 4 núcleos) · 0 falhas · **1246 s**.
**Master:** `renders/Bob-Chapman-reel-final.mp4` — 1440×2560 · 60 fps · 90,11 s · 5407 quadros (= timeline) · 236 MB (fora do git).
QC (`finalizar.py` + `work/qc_final.sh`): quadros = timeline OK · pico −0,8 dB / média −15,9 dB · trechos pretos 0 · bipe achado na voz-mix em 52,04–52,55 s:
no MP4 99,5% em 950–1050 Hz e 0,5% fora de 900–1100 Hz (na `voz-mix.m4a` 100%) · sincronia boca/voz lag mediano 10 ms (26/27 pontos com r > 0,6; faixa 0..10 ms)
· bruto intacto (MD5 antes e depois `f1247c47b04519b1123a9e9150751092`). Quadro a quadro: 90 quadros do MP4 (um por cena/transição, `work/qc/folha-1..4.jpg`)
conferidos + um quadro de cada parte durante o render; quadro 0 = capa; revelação 2 quadros depois de "Bob".
**Entregas (a partir do master, `work/entregas.sh`):** `entrega/Bob-Chapman-reel-chat.mp4` (x264 dois passes 2,3 Mbps, AAC 160k; **28,1 MB**, mandado no chat) ·
`entrega/Bob-Chapman-reel-final.mp4` (HEVC libx265 dois passes **8,0 Mbps** — reel de 90,1 s < 95 s —, `hvc1`, AAC 256k 48 kHz, `+faststart`) ·
`entrega/comparacao-master-x-hevc.jpg` (quadro 719 = 11,98 s, a revelação com o nome, master × HEVC). Final: **92,9 MB**, 7,96 Mbps de vídeo, 5407 quadros,
`moov` antes do `mdat`; SSIM do vídeo inteiro **0,993**.

## Lições para o kit (entraram em docs/05 §35)

- Library of Congress (FSA/OWI, domínio público, sem 429) como fonte primária de tema sem acervo próprio; TIF mestre (o `v.jpg` tem 1024 px); TIF de 16 bits
  escalado antes de converter. `work/pesq/loc.py` / `locsheet.py` / `locmaster.py` / `locdl.py` (novos no modelo).
- Pessoa-tema sem retrato livre: revelação = a capa (de costas) + etiqueta; clímax = callback da capa.
- iCloud vazio ~20 min (laço de 30 s por até 75 min + push para deixar o Fotos aberto) · `pip install` do setup travado num socket (`--timeout 60 --retries 2`).
