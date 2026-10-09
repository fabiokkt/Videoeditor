# EDICAO.md — mapa do projeto (reel Michael Gerber)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
**Estado (2026-10-08): RENDERIZADO** — ver "Export final" no fim. Comando único sem parada, numa sessão do Claude Code **na nuvem**
(Linux, 4 núcleos, 16 GB).
Duração **99,015 s** · 34 takes · 1 bipe · 104 legendas · 5 callouts · 4 light-leaks (virada, clímax, CTA + gancho) · 10 SFX fixos + 101 da camada ·
9 slots (2 splits + 7 cenas de tela cheia na camada de motion, `work/mg/gen.py`) + COMENTA CADEIRA, SEGUNDA-FEIRA e o botão "Seguir" sobre o apresentador.

## Bruto e roteiro
`~/Claude/videos-brutos/michael-gerber-bruto.mov` (iCloud `09dHezn_Jq85iWjQ0dYuImeCg`) — **não alterado**, MD5 `cddb98c2a6a0f35bb198c38209da6dc9`.
HEVC 1440x2560 @60, 138,12 s, SDR full-range → mezanino full→limited; cor bruto × mezanino (13,81/69,06/124,31 s): média 100,00/100,14 ·
102,48/102,48 · 101,95/102,09, desvio 67,37/67,50 · 68,76/68,78 · 68,74/68,83 — não lavou. O link do iCloud ficou VAZIO por ~28 min
(o iPhone ainda subindo; `ic.py` em laço de 20 s, baixou na ~82ª tentativa, 433 MB).
Roteiro: ClickUp > Cronograma > "Michael Gerber" (v2 06/10/2026, seção "Roteiro (v2)"; a "Nota de gravação" valeu para a edição: "COMENTA CADEIRA"
na tela durante o CTA do meio).
Onde o áudio diverge do roteiro (vale o áudio; passe por região + whisper em recorte concordam, e o espectro confirma):
- **"Tem um emprego."** (roteiro: "Você tem um emprego."): o recorte 12,4–16,4 s ouve "…não tem uma empresa, tem um emprego."
- **"a gente tá QUEBRANDO"** (roteiro: "quebrado"): murmúrio nasal /n/ de 0,08 s (21,10–21,16 s, energia < 400 Hz) entre "quebra" e "do".
- "E ele tava ocupado" (roteiro: "Ele tava") · "escreve passo a passo" (roteiro: "o passo a passo") · "Ele DISSE que ela tem que funcionar"
  (roteiro: "Ele diz") · "ela falou: odeio fazer torta" (roteiro: "eu odeio").
- Homófonos / fala ligada (vale o roteiro): "desenhe o" → "desenha o" · "Montar a" → "monta a" · "Tudo o que" → "Tudo que" · "te mando teste" → "te mando
  o teste" (o recorte ouviu "o teste") · "está" → "tá" e "estava" → "tava" (nenhum /s/ no espectro).
- **CTA de palavra-chave "Comenta CADEIRA…": GRAVADO** (r24, inteiro: "Comenta CADEIRA que eu te mando o teste pra descobrir quantas cadeiras são suas.";
  o r23 "Comenta Cadeira." parou e saiu). Na tela: a caixa de comentário com CADEIRA digitado + "Publicar" durante a frase.
- "E o seu chefe é um louco: você." (só na nota de gravação, não no texto do roteiro v2): não foi gravado.
- "Depois inventaram a cadeira." — a nota pedia "seco, sem sorrir"; ele sorri no take (único take, mantido).

## Takes descartados (mantido o ÚLTIMO válido)
r01 "E ele criou um protocolo polêmico para provar para você..." → r02 · r06 "E ele estava ocupado demais trabalhando para olhar..." → r07 ·
r08 "E esse é o protocolo para você parar de ser o funcionário." (parou antes de "mais explorado") → r09 · r16 "Se..." → r17 · r21 "Na sua..." → r22 ·
r23 "Comenta Cadeira." → r24 · r26 "Três anos depois, a loja..." → r27 · r28 "Você abriu..." → r29.
Divisões nos vales: r11 em 44,52 · r12 em 50,42 e 52,53 · r14 em 58,86 (com `WFIX`: o whisper pôs "Tudo" dentro do vale 58,62–59,10) · r17 em 72,73 ·
r22 em 89,63 · r25 em 104,16 · r27 em 116,90, 118,73 e 120,41 · r30 em 130,62. "porque você... é demais" (r30 + r31, pausa dramática) = um take só.

## Bipe
"porra" ("Você é a porra do organograma."): /s/ de "você" 52,76–52,84 · "é a" 52,85–53,01 · oclusão /p/ 53,02–53,20 (−39 a −59 dB) · explosão 53,21 ·
"o" 53,22–53,35 · "rr" 53,36–53,40 · "a" 53,41–53,48 · /d/ de "do" 53,49. O whisper pôs a palavra em 52,92–53,28 (adiantada). Recortes cumulativos:
até 53,03 "você é a"; de 53,40 e de 53,49 em diante só "do organograma". Bipe **53,03–53,49** do source. Legenda `P****`. Apresentador em tela cheia no bipe.

## J-cut
33 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9 quadros (4,9–5,4) · respiro mediano 0,245 s (6 pausas curtas emendadas no silêncio).

## Olhar
`gaze_pose.py 2.0`: 21 janelas / 5,4 s; `gaze_windows`: 19 / 6,1 s. Folhas `gaze/me/g00-g02` + recortes grandes: o apresentador olha para a câmera quase o tempo
todo — piscadas, pálpebra baixando em fim de frase e o sorriso. **Duas olhadas para baixo nítidas em fim de take**, cobertas: 17,38–17,71 ("dinheiro.") pela
2ª foto do Michael (a cena B foi estendida até o fim do take) e 51,42–51,69 ("funciona.") pela entrada antecipada do PASSO 3 (51,38). Sutil exposta:
71,0–71,2 (pálpebra baixa sorrindo em "cadeiras são suas", sob a caixa do COMENTA) e 97,9–98,1 (a pausa dramática do "porque você... é demais").
**Leitura exposta: 0 s.**

## Split
`splitShiftY` **397** (olhos y≈982 no mezanino em 12 pontos das janelas de split → zoom 1,06: 980 → 1377−980; `work/olhos_y.py`). Splits: capa 0–5,06 · virada 72,57–75,03.

## Marca só depois do nome
"Michael" em 10,55 s → revelação em 10,62 (a foto dele em 2009 + "MICHAEL E. GERBER · AUTOR DE “O MITO DO EMPREENDEDOR”"). Pré-revelação: a capa gerada,
o relógio de ponto e a dona do armazém — nada dele.

## Camada de motion (work/mg/gen.py + work/mg/parts.py + work/mg/fotos.py) — dosagem Deming v2
Os tempos saem das FRASES em `work/tl-words.txt` (`T("frase", w, k)` no gen.py) e vão para `work/mg/tempos.json`, que o `scripts/slots.py` lê: mudou o corte,
roda o gerador de novo. Chip "PASSO N". Motion só em: PASSO 1/2/3 (chip + título) · o sócio "A gente tá quebrando." (1985) · o organograma (as cadeiras nas
palavras, VOCÊ em cada uma, SEU NOME EM 6 CADEIRAS) · a franquia (a mesma loja 9 vezes) · o passo a passo · GENTE COMUM × GÊNIO · o contrato da cadeira
(assinado, VOCÊ · FUNCIONÁRIO) · 1º A CADEIRA / 2º A PESSOA → 1º O SOBRINHO / 2º A CADEIRA · COMENTA CADEIRA · EMPRESA → EMPREGO (clímax) · SEGUNDA-FEIRA ·
o botão "Seguir". O resto é foto real (LICENCAS-FOTOS.txt): capa gerada (Codex) · relógio de ponto (British Library) · dona do armazém (NARA 1973) · o Michael
em 2009 (2 fotos, Flickr/Infusionsoft CC BY-SA 2.0) · a padaria de San Angelo 1939 (Russell Lee, FSA/LOC, do TIFF master) · a moça com a torta (Harris & Ewing,
LOC) · a capa de novo em "odeio fazer torta" (callback). Nenhuma foto de arquivo leva etiqueta dizendo que é a Sarah (nome trocado, segundo o livro).
Callouts: 1º digitado "TEM UM / EMPREGO." (seg 2) · "O FUNCIONÁRIO / MAIS EXPLORADO." (6) · "VOCÊ NÃO É / O DONO." (11) · "ELA NÃO / FUNCIONA." (17) ·
"LOJA DE / TORTA." (32).

> **Regra de ouro: nunca editar `index.html` à mão.**
```
editar assets/edit-plan.json (work/plano.py) ou work/mg/gen.py -> python3 work/mg/fotos.py && python3 work/mg/gen.py -> zsh scripts/montar.sh <instantes>
(cortes: scripts/mkcut.py / cuts.py -> zsh scripts/fase2.sh · legendas: scripts/captions_fix_table.py -> zsh scripts/legendas.sh + tl.py --words)
```

## Onde mexer em cada coisa

| Quero mudar… | Arquivo |
|---|---|
| cortes / takes (in/out) | `scripts/mkcut.py` (divisões/descartes/WFIX) → `scripts/cuts.py` (lista TAKES) → `work/segs.json` → `python3 scripts/plan_segments.py` |
| texto de legenda | `scripts/captions_fix_table.py` (FIX/FIXT por chunk e índice de palavra) → `zsh scripts/legendas.sh` |
| callouts, seções, CTA, splitShiftY | `work/plano.py` (impacts, sections, ctaSeg; `python3 work/plano.py 397`) |
| janelas de cobertura | `work/mg/gen.py` (função `build()`: tempos pela frase) → `work/mg/tempos.json` → `scripts/slots.py` |
| fotos / recortes | `work/mg/fotos.py` (papel → arquivo bruto + recorte; a capa vem de `work/capa/capa.png`) |
| cenas da camada | `work/mg/gen.py` (F = foto por papel, OP = enquadramento, `fit()`, HTML e JS) e `work/mg/parts.py` (CSS) |
| testar a camada sem o vídeo | `work/mg/teste/` (`fake_tl.py` gera um tl-words do roteiro; `harness.html` + `shoot.mjs` fotografam a camada) |
| bipe | `scripts/bipe.py` (JANELAS 53,03–53,49 s do source) → `bake.py voz` |
| tempos de timeline / palavra | `python3 scripts/tl.py [--words]` |

## Export final

`size_sweep.py`: `--size` **457** (13 partes, sobra mínima 151 quadros) · `render-par.sh 457 … 2` (2 em paralelo, 4 núcleos) · 0 falhas · **1428 s**
(~3,7 min por par) + re-render só da parte 4 (146 s) depois do quadro a quadro: o callout "VOCÊ NÃO É O DONO." pulava ~6 quadros sobre o organograma saindo
(33,8–33,95 s) → o organograma passou a sair 0,15 s antes do "Você" (`D_out` no gen.py).
**Master:** `renders/Michael-Gerber-reel-final.mp4` — 1440×2560 · 60 fps · 99,02 s · 5941 quadros (= timeline) · 226 MB (fora do git).
QC (`finalizar.py` + `work/qc_final.sh`): quadros = timeline OK · pico −0,3 dB / média −16,9 dB · trechos pretos 0 · bipe achado na voz-mix em 36,03–36,45 s:
no MP4 99,5% em 950–1050 Hz e 0,5% fora de 900–1100 Hz (na `voz-mix.m4a` 100%) · sincronia boca/voz lag mediano 10 ms (32/32 pontos medindo DENTRO dos
takes curtos — o `sync-check.mjs` padrão dava −70/−120/−150 ms nos takes de 1,1–1,9 s porque a janela de 1,2 s invade o take vizinho, §30)
· bruto intacto (MD5 antes e depois `cddb98c2a6a0f35bb198c38209da6dc9`). Quadro a quadro: 67 quadros do MP4 (um por cena/transição, `work/qc/folha-1..4.jpg`)
+ as emendas da parte refeita conferidos; quadro 0 = capa; revelação 2 quadros depois de "Michael".
**Entregas (a partir do master, `work/entregas.sh`):** `entrega/Michael-Gerber-reel-chat.mp4` (x264 dois passes 2,0 Mbps, AAC 160k; **27,4 MB**) ·
`entrega/Michael-Gerber-reel-final.mp4` (HEVC libx265 dois passes **7,4 Mbps** — reel de 99 s > ~95 s, o bitrate desceu para caber —, `hvc1`, AAC 256k 48 kHz,
`+faststart`) · `entrega/comparacao-master-x-hevc.jpg` (quadro 720 = 12,00 s, o Michael com o nome, master × HEVC). Final: **95,5 MB**, 7,44 Mbps de vídeo,
5941 quadros, `moov` antes do `mdat`; SSIM do vídeo inteiro **0,995**.
As fotos em `assets/mg/` no repositório estão reduzidas a 1600 px (o render usou as de 2400 px geradas pelo `fotos.py` a partir de `work/pesq/raw/`, fora do git).

## Correções depois do render

- Callout "VOCÊ NÃO É O DONO." sobre o organograma saindo (6 quadros) → `D_out` 0,15 s antes do "Você"; parte 4 refeita (`render-par.sh` retomou as outras 12).

## Lições para o kit (entraram em docs/05 §36, docs/11, docs/14 e no modelo)

- Library of Congress em alta pelo TIFF master do `tile.loc.gov` com o id tirado do Flickr (o loc.gov caiu no Cloudflare): `locmaster.py` do modelo agora
  tenta uma pasta só (`hec`, `mrg`); o `work/pesq/locdl.py` deste reel faz o mesmo · Flickr Commons pela página de busca (`flsearch.py`, novo) ·
  Openverse (`ovq.py`, novo) achou a foto CC BY-SA do Michael.
- Camada escrita pela FRASE (`T()` no gen.py → `work/mg/tempos.json` → `slots.py`) e testada antes do bruto (`work/mg/teste/`, novo no modelo).
- `WFIX` no `mkcut.py` do modelo · "quebrado" × "quebrando" pelo murmúrio nasal · CTA de palavra-chave gravado · olhada de fim de take coberta pela cena vizinha.
- Callout que começa logo depois de uma cena de tela cheia: a cena tem que sair ANTES da 1ª palavra do callout (o `sceneOut` leva 12 quadros encolhendo).
