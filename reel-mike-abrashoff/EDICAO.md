# EDICAO.md — mapa do projeto (reel Mike Abrashoff)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
**Estado (2026-10-04): RENDERIZADO** — entrega: `entrega/Mike-Abrashoff-reel-final.mp4` (HEVC 2 passes, 7,5 Mbps, hvc1, AAC 256k, 93,9 MB) · cópia chat `entrega/Mike-Abrashoff-reel-chat.mp4` (x264, 27 MB) · master 260 MB fora do git. QC: 5800 quadros = timeline · pico −0,6 dB · 0 pretos · bipe 100% em 1 kHz na voz · sync lag mediano 10 ms · MD5 do bruto igual. Render: 13 partes, 2 em paralelo, 24 min + parte 0 refeita com a capa (3 min)., comando único sem parada, numa sessão do Claude Code **na nuvem** (Linux, 4 núcleos).
Duração **96,654 s** · 34 takes · 1 bipe · 110 legendas · 4 callouts · 4 light-leaks (virada, clímax, CTA + gancho) · 11 SFX fixos + 62 da camada ·
11 slots (2 splits + 9 cenas de tela cheia na camada de motion, `work/mg/gen.py`).

## Bruto e roteiro
`~/Claude/videos-brutos/mike-abrashoff-bruto.mov` (iCloud `037Cud67uM3JcRLUlxyOQd84w`) — **não alterado**, MD5 `02e36a2698bcc8b125204b5f030f20f9`.
HEVC 1440x2560 @60, 139,05 s, SDR full-range → mezanino full→limited; cor bruto × mezanino (13,9/69,5/125,2 s): 150,26/150,37 ·
145,94/146,03 · 146,43/146,56, desvio igual — não lavou. Roteiro: ClickUp > Cronograma > "Mike Abrashoff" (roteiro curto).
Onde o áudio diverge do roteiro (vale o áudio): "E o protocolo…" (sem "esse é": o take com "esse é" tropeçou em "quer **parar de** trabalhar"),
"O primeiro **não era ser** tratado com respeito", "pinta **nesse** navio", "soltava **um** rojão".

## Takes descartados (mantido o ÚLTIMO válido)
r04 "com o mesmo atributo" → r05 · r07 (tropeço) → fica r06 · r13+r14+r15 → r16+r17 · r18 "310 pessoas" → r19 · r30 → r31 "É leilão." ·
r32 fim "no dia que ele assumiu o cap…" → r33 · r36 "Ele…" · r38 falso início → r39+r40 (um take, "porque você… é demais").

## Bipe
"porra" ("olhando a porra do celular"): oclusão /p/ 51,28–51,46 · explosão 51,46 · "orra" 51,47–51,67 · /d/ 51,68 · /s/ 51,72.
Whisper em recortes cumulativos: até 51,46 "…olhando a"; até 51,68 "…a porra". Bipe **51,42–51,68** do source. Legenda `P****`.
Apresentador em tela cheia no bipe (36,05–39,40) — ele olha o celular de propósito (nota de gravação).

## J-cut
33 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9 quadros · respiro mediano 0,245 s.

## Olhar
`gaze_pose.py 2.0`: 19 janelas / 3,8 s (quase todas piscada). Nítidas, cobertas por tela cheia: 8,05–8,32 · 54,15–54,30.
94,49–94,88 (cabeça mexendo no "me segue") coberta pela tripulação. 37,7–38,9 olha o celular (intencional). **Leitura exposta: ~0 s.**

## Split
`splitShiftY` **420** (olhos y≈957 no aroll em 12 pontos das janelas de split). Splits: capa 0–7,22 · virada 70,75–78,55.

## Marca só depois do nome
"Mike" em 12,71 s → revelação em 12,78 (USS Benfold + nome). Pré-revelação: capa gerada, canhão de destróier à noite (USS Oscar Austin),
proa de destróier furando onda (USS Barry), sem número legível. Não existe retrato do Abrashoff com licença livre: a revelação é o navio + o nome.
Capa = **gerada a pedido** no Codex (`gpt-5.6-sol`, conta ChatGPT do Fabio por login de dispositivo; logout no fim): oficial de farda branca
de costas na prancha com a esposa e a filha, tripulação comemorando em silhueta no convés, cais à noite (`work/capa/prompt.txt`).

## Camada de motion (work/mg/gen.py) — dosagem Deming v2
Chip "PASSO N". Motion só em: ranking da frota (pior → 1º em 7 meses) · PASSO 1/2/3 · ranking dos motivos (5º salário, 1º respeito) ·
contador 0 → 310 · pedido de demissão + TARDE DEMAIS (≈35% da cobertura). O resto é foto real (Marinha dos EUA, domínio público).
Callouts: 1º digitado "VAI EMBORA / POR SUA CAUSA." (seg 2) · "NINGUÉM MAIS / QUER TRABALHAR." (6) · "É LEILÃO." (25) · "CHORAVA OU / SOLTAVA ROJÃO?" (32).

> **Regra de ouro: nunca editar `index.html` à mão.**
```
editar assets/edit-plan.json (ou scripts/slots.py para B-roll)  ->  node scripts/build-edit.mjs  ->  python3 scripts/bake.py <alvos>  ->  npm run check
(bake.py sem argumento = cenas, brollfull, leaks, voz, bed, aroll; mudou só B-roll: bake.py cenas brollfull leaks bed)
```

## Onde mexer em cada coisa

| Quero mudar… | Arquivo |
|---|---|
| cortes / takes (in/out) | `scripts/mkcut.py` (divisões/descartes) → `scripts/cuts.py` (lista TAKES, FORCE_IN/FORCE_OFF) → `work/segs.json` → `python3 scripts/plan_segments.py` |
| texto de legenda | `scripts/captions_fix_table.py` (FIX por chunk e índice de palavra) → `python3 scripts/fix_captions.py` (idempotente) |
| callouts | `impacts` no plano (frase, seg, linhas, hold, `top` opcional; o 1º com `style: typing`) |
| B-roll (janela, modo, arquivo) | `scripts/slots.py` (lista S, tempos absolutos) → `python3 scripts/slots.py --real` (ou `--placeholders`) |
| foto / movimento de câmera do B-roll | `scripts/entrega.py` (foto e recorte por slot) → `scripts/make_broll.py` (zoom/pan por slot) |
| legenda baixa sobre B-roll | `capLowSegs` no plano |
| enquadramento do split | `splitShiftY` (medido: ___) |
| zoom do apresentador | `presenterZoom` (1,06/1,14, uma troca por aparição; `sceneMax` 4,5) |
| volumes de trilha/SFX | `trilhaVol` no plano / seção SFX de `scripts/build-edit.mjs` → `bake.py bed` |
| transições | `sections` e `leakMinGap` (3,5) no plano |
| bipe | `scripts/bipe.py` (JANELAS ___ s do source) → `bake.py voz` |
| respiro / lead do J-cut | `TA`/`HH` em `scripts/cuts.py`; `jcutLeadFrames` (9) / `jcutCrossfadeFrames` (3) |
| tempos de timeline / palavra | `python3 scripts/tl.py [--words]` |

## Bruto original

`~/Claude/videos-brutos/___` — **não alterado**. MD5 `___` (`work/md5-bruto.txt`).
Codec/resolução/fps/duração: ___ · HDR ou SDR full-range: ___

## Mezanino

`assets/mike-abrashoff-2560-sdr.mp4` — conversão usada: ___ · conferência de cor (média/desvio bruto × mezanino): ___
Voz: `assets/mike-abrashoff-voz.m4a` (com bipe). Voz limpa: `work/mike-abrashoff-voz-limpa.m4a`.

## Transcrição

Regiões: ___ · divisões nos vales: ___ · chunks: ___ · chunks reconstruídos do passe por região: ___
Mantido o que o áudio diz (≠ roteiro): ___ · Grafia do roteiro: ___

## Takes descartados (mantido sempre o ÚLTIMO)

- ___

## J-cut

`python3 scripts/jcut_check.py`: ___ emendas · buracos ___ · crossfade sobre fala ___ · lead de FALA ___ quadros · respiro mediano ___ s

## Bipe

Varredura da transcrição INTEIRA (inclusive takes descartados): ___ palavrão(ões).
Mapa de sílabas: ___ · **Bipe ___–___ s** do source · timeline ___ · aceite por medição na `voz-mix.m4a`: ___ · legenda `___`

## Varredura de olhar

1ª passada (B-roll em placeholder): ___ janelas / ___ s · nítidas: ___ · **leitura exposta: ___ s**
2ª passada (com os B-rolls reais): ___ · **leitura exposta: ___ s**

## Split-screen

`splitShiftY` ___ — olhos medidos em ___ · janelas de split: ___

## Marca só depois do áudio

1ª vez que o áudio diz "___": ___ s · pré-revelação: slots ___ · revelação entra em ___ s (2 quadros depois) ·
último quadro limpo ___ s / primeiro com marca ___ s

## Callouts

___

## Pesquisa e B-roll

`PESQUISAS-BROLL-___.md` · imagens geradas a pedido: ___ · `capLowSegs` ___ · callouts com `top`: ___

## Export final

`size_sweep.py`: `--size` ___ (sobra mínima ___ quadros) · partes ___ · falhas ___
**Resultado:** `renders/___-reel-final.mp4` — 1440×2560 · 60 fps · ___ s · ___ quadros · ___ MB
QC (`finalizar.py`): quadros = timeline ___ · pico ___ dB / média ___ dB · trechos pretos ___ · bipe no MP4 ___ ·
quadros-chave × preview ___ · bruto intacto (MD5 antes e depois) ___

## Correções depois do render

- ___

## Lições para o kit

O que este reel ensinou que vale para os próximos (número novo, armadilha, pedido do Fabio, script corrigido).
Cada item daqui tem que ser levado para `KIT-EDICAO-REEL` (docs/05 e, se mexeu em script, `modelo-projeto/scripts/`) antes de fechar o projeto.

- ___
