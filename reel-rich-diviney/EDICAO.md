# EDICAO.md — mapa do projeto (reel Rich Diviney)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
**Estado (2026-10-04): EM EDIÇÃO.**
Duração ___ s · ___ takes · ___ bipe(s) · ___ legendas · ___ callouts · ___ light-leaks · ___ SFX · ___ slots de B-roll.

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

`assets/reel-rich-diviney-2560-sdr.mp4` — conversão usada: ___ · conferência de cor (média/desvio bruto × mezanino): ___
Voz: `assets/reel-rich-diviney-voz.m4a` (com bipe). Voz limpa: `work/reel-rich-diviney-voz-limpa.m4a`.

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
