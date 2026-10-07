# EDICAO.md — mapa do projeto (reel Ernest Shackleton)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
**Estado (2026-10-07): RENDERIZADO** — ver "Export final" no fim. Comando único sem parada, numa sessão do Claude Code **na nuvem**
(Linux, 4 núcleos, 16 GB).
Duração **93,272 s** · 27 takes · 1 bipe · 94 legendas · 6 callouts · 4 light-leaks (virada, clímax, CTA + gancho) · 11 SFX fixos + 66 da camada ·
9 slots (2 splits + 7 cenas de tela cheia na camada de motion, `work/mg/gen.py`).

## Bruto e roteiro
`~/Claude/videos-brutos/ernest-shackleton-bruto.mov` (iCloud `0731QXwj3AyvGh3ALwj6UxN2w`) — **não alterado**, MD5 `8573f5f8ae69f1b8097c350a0c90ea0e`.
HEVC 1440x2560 @60, 134,13 s, SDR full-range → mezanino full→limited; cor bruto × mezanino (13,41/67,07/120,72 s): 127,66/127,71 ·
128,62/128,69 · 129,45/129,50, desvio 67,49/67,47 · 65,44/65,41 · 65,10/65,08 — não lavou. Roteiro: ClickUp > Cronograma > "Ernest Shackleton" (v1, 04/10/2026).
Onde o áudio diverge do roteiro (vale o áudio; passe por região + whisper em recorte com e sem o roteiro no `--prompt` concordam):
"o funcionário **que reclama**" (sem "mais") · "preso no gelo **na** Antártida" (roteiro: "da") · "e até **o** futebol no gelo".
**O CTA do meio "Comenta GELO que eu te mando o protocolo completo no direct." não foi gravado** (entre "pequeno gafanhoto" e "E a virada" só há 1,5 s
de silêncio) — sem callout COMENTA GELO (4º reel seguido sem o CTA de palavra-chave).

## Takes descartados (mantido o ÚLTIMO válido)
r03 "E não perdeu um..." → r04 · r05 "...um reclamão contamin..." → r06 · r10 "Ele sai..." → r11 · r13 "Segundo" → r14 · r17 "Então tinha tarefa todo dia,
até o..." → r18 · r23 "Ernest leu conta..." → r24 · r28 "Quem mais reclama na sua empresa" + r29 "Quem mais reclama nas..." → r30.
Divisões nos vales: r01 em 14,00 (antes de "Ernest") · r14 em 58,06 e 61,29 · r16 em 74,45. Duas palavras do r14 vinham ~0,3 s adiantadas pelo whisper,
dentro do silêncio real ("Ele" 57,80 e "E" 61,18): `WFIX` no `mkcut.py` põe as duas no pedaço certo antes de dividir.

## Bipe
"merda" ("Time sem meta da semana fala merda no corredor"): /f/ de "fala" 87,53–87,61 · "fala" 87,62–87,84 · /m/ nasal (60% da energia < 400 Hz) 87,85–87,99 ·
"e(r)" 88,00–88,13 · oclusão /d/ 88,14–88,23 · "a" 88,24–88,31 · /n/ de "no" 88,32. Whisper em recortes do áudio limpo: até 87,99 "...semana fala..." (sem a
palavra); a partir de 88,33 "no corredor, pequeno gafanhoto". Bipe **87,85–88,32** do source. Legenda `M****`. Apresentador em tela cheia no bipe (59,63–63,42).
Aceite no MP4: ver "Export final".

## J-cut
26 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9 quadros (4,9–5,1) · respiro mediano 0,245 s (1 pausa curta emendada no silêncio).

## Olhar
`gaze_pose.py 2.0`: 13 janelas / 2,7 s; `gaze_windows`: 31 / 12,8 s. Folhas `gaze/me/g00-g02`: o apresentador olha para a câmera o tempo todo —
só piscadas e desvios mínimos (o maior, 16,19–16,50, fica sob a foto do Ocean Camp). **Leitura exposta: 0 s.**

## Split
`splitShiftY` **346** (olhos y≈1030 no mezanino em 13 pontos das janelas de split → 1377−1031; `work/olhos_y.py`). Splits: capa 0–5,52 · virada 63,42–66,30.

## Marca só depois do nome
"Ernest" em 12,06 s → revelação em 12,13 (retrato do Shackleton na expedição, c. 1915 + "ERNEST SHACKLETON · EXPLORADOR · ANTÁRTIDA, 1914–1916").
Pré-revelação: capa gerada (Shackleton de costas, sem rosto), o Endurance de velas abertas no gelo, o Endurance à noite e o navio preso — nada do rosto dele.
Capa = **gerada a pedido** no Codex (`gpt-5.6-sol`, conta ChatGPT do Fabio por login de dispositivo; 1º código aceito; logout logo depois de gerar):
mar de Weddell à noite, o Endurance esmagado pelo gelo com uma lanterna acesa no convés, Shackleton estritamente de costas numa crista de gelo, dois homens
puxando um bote num trenó à direita (`work/capa/prompt.txt`). Sem texto, rosto, logotipo ou bandeira. Assunto entre 5% e 53% da altura (acima da caixa do gancho).

## Camada de motion (work/mg/gen.py + work/mg/parts.py + work/mg/fotos.py) — dosagem Deming v2
Chip "PASSO N". Motion só em: PASSO 1/2/3 (chip + título) · a torcida (o RECLAMÃO longe do CHEFE junta gente; anel JUNTA TORCIDA) · as moedas de ouro caindo
na neve (O 1º A LARGAR: O CHEFE.) · a bola de couro no gelo (ATÉ FUTEBOL NO GELO: a foto do jogo não está no Commons — etiqueta honesta sobre a foto real
do trabalho no gelo) · a virada (fala do carpinteiro, o CONTRATO DE BORDO com O SALÁRIO CONTINUA ATÉ O PORTO marcado, carimbo FIM DO MOTIM, MEDO × NÃO REBELDIA)
(≈38% da cobertura). O resto é foto real do Frank Hurley (domínio público, LICENCAS-FOTOS.txt).
Clímax: "Launching the James Caird" (24 abr 1916) inteiro na largura da tela sobre a própria foto desfocada + ABRIL DE 1916 · O BOTE DO SOCORRO · O CARPINTEIRO FOI JUNTO.
Callouts: 1º digitado "VOCÊ TRAZ / PRA PERTO." (seg 1) · "NÃO PERDEU / UM HOMEM." (4) · "CONTAMINAR / O SEU TIME." (5) · "SENTA DO / SEU LADO." (9) ·
"E MANTER O / SEU CARRO?" (13) · "TÁ COM MEDO / DE QUÊ?" (25).

> **Regra de ouro: nunca editar `index.html` à mão.**
```
editar assets/edit-plan.json (ou scripts/slots.py) -> python3 work/mg/fotos.py && python3 work/mg/gen.py -> zsh scripts/montar.sh <instantes>
(cortes: scripts/mkcut.py / cuts.py -> zsh scripts/fase2.sh · legendas: scripts/captions_fix_table.py -> zsh scripts/legendas.sh)
```

## Onde mexer em cada coisa

| Quero mudar… | Arquivo |
|---|---|
| cortes / takes (in/out) | `scripts/mkcut.py` (divisões/descartes/WFIX) → `scripts/cuts.py` (lista TAKES) → `work/segs.json` → `python3 scripts/plan_segments.py` |
| texto de legenda | `scripts/captions_fix_table.py` (FIX/FIXT por chunk e índice de palavra) → `zsh scripts/legendas.sh` |
| callouts | `impacts` no plano (frase, seg, linhas, hold; o 1º com `style: typing`) |
| janelas de cobertura | `scripts/slots.py` (lista S, tempos absolutos; MG="*") → `zsh scripts/montar.sh` |
| fotos / recortes | `work/mg/fotos.py` (papel → arquivo bruto + recorte sem selo) |
| cenas da camada | `work/mg/gen.py` (F = foto por papel, OP = enquadramento, CENAS) e `work/mg/parts.py` (CSS) |
| enquadramento do split | `splitShiftY` (medido: 346 — `work/olhos_y.py`) |
| transições | `sections` (após os segs 17, 23, 25) e `leakMinGap` (3,5) no plano |
| bipe | `scripts/bipe.py` (JANELAS 87,85–88,32 s do source) → `bake.py voz` |
| tempos de timeline / palavra | `python3 scripts/tl.py [--words]` |

## Export final

`size_sweep.py`: `--size` **431** (13 partes, sobra mínima 140 quadros) · `render-par.sh 431 … 2` (2 em paralelo, 4 núcleos) · 0 falhas · **1214 s** (~3,1 min por par)
+ re-render das partes 0 e 1 (210 s) depois de pôr fundo escuro nas cenas A, P e L: no chicote entre fotos (`whip`, expo.out) a foto que entra deixava uma
faixa de 1–2 quadros na borda esquerda onde aparecia o apresentador (cenas sem `.world`).
**Master:** `renders/Ernest-Shackleton-reel-final.mp4` — 1440×2560 · 60 fps · 93,28 s · 5597 quadros (= timeline) · 200 MB (fora do git).
QC (`finalizar.py` + `work/qc_final.sh`): quadros = timeline OK · pico −0,8 dB / média −17,5 dB · trechos pretos 0 · bipe no MP4 99,0% em 950–1050 Hz e 1,0% fora
de 900–1100 Hz (61,14–61,51 s; o resto é a trilha por baixo; na `voz-mix.m4a` 100%) · sincronia boca/voz lag mediano 10 ms (26/27 pontos com r > 0,6; faixa −20..10 ms)
· bruto intacto (MD5 antes e depois `8573f5f8ae69f1b8097c350a0c90ea0e`). Quadro a quadro: 78 quadros do MP4 (um por cena/transição, `work/qc/folha-1..4.jpg`)
conferidos; quadro 0 = capa; revelação 2 quadros depois de "Ernest".
**Entregas (a partir do master, `work/entregas.sh`):** `entrega/Ernest-Shackleton-reel-chat.mp4` (x264 dois passes 2,0 Mbps, AAC 160k; **25,4 MB**) ·
`entrega/Ernest-Shackleton-reel-final.mp4` (HEVC libx265 dois passes **8 Mbps** — reel de 93,3 s < ~95 s —, `hvc1`, AAC 256k, `+faststart`) ·
`entrega/comparacao-master-x-hevc.jpg` (quadro 780 = 13,00 s, o retrato com a etiqueta de nome, master × HEVC). Final: **95,5 MB**, 7,91 Mbps de vídeo, 5597 quadros,
`moov` antes do `mdat`; SSIM do vídeo inteiro **0,995**.

## Correções depois do render

- (nenhuma)

## Lições para o kit

- Commons no container com 429 em tudo (API e miniaturas) por horas: listar as categorias com espera honrando o `retry-after` (1 chamada por categoria +
  1 por lote de 50 arquivos) e baixar só a fila priorizada; Flickr Commons da SLNSW responde sem chave pela página de busca (tamanho `l`, 1024 px).
- Pranchas do livro "South" no Commons (digitalização Cornell) trazem o selo da biblioteca num canto: recortar e conferir os 4 cantos de cada foto.
- Foto horizontal pequena que não aguenta o recorte 9:16: card de foto inteira sobre o mundo escuro, ou a foto inteira na largura da tela sobre ela mesma desfocada (clímax).
- Palavra que o whisper põe dentro do silêncio real cai no pedaço errado da divisão: `WFIX` no `mkcut.py` (tempo real antes de atribuir).
- Cena da camada sem `.world` de fundo: no `whip` a borda da foto que entra deixa ver o apresentador por 1–2 quadros — toda cena de tela cheia (e split) com fundo.
- CTA de palavra-chave não gravado pelo 4º reel seguido.
