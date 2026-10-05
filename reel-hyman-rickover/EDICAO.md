# EDICAO.md — mapa do projeto (reel Hyman Rickover)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
**Estado (2026-10-05): RENDERIZADO** — ver "Export final" no fim. Comando único sem parada, numa sessão do Claude Code **na nuvem**
(Linux, 4 núcleos, 16 GB).
Duração **91,088 s** · 28 takes · 1 bipe · ~100 legendas · 5 callouts · 5 light-leaks (virada, clímax, CTA + gancho) · 12 SFX fixos + 62 da camada ·
10 slots (2 splits + 8 cenas de tela cheia na camada de motion, `work/mg/gen.py`).

## Bruto e roteiro
`~/Claude/videos-brutos/hyman-rickover-bruto.mov` (iCloud `03cghLJEoHe7zNeh56NzQo2lw`) — **não alterado**, MD5 `bfc5ad9bf193e444218b1216588791b5`.
HEVC 1440x2560 @60, 124,58 s, SDR full-range → mezanino full→limited; cor bruto × mezanino (12,5/62,3/112,1 s): 154,11/154,13 ·
152,86/152,96 · 152,86/152,89, desvio 71,74/71,76 · 73,04/73,04 · 74,06/74,07 — não lavou. Roteiro: ClickUp > Cronograma > "Hyman Rickover" (v2 curto).
Onde o áudio diverge do roteiro (vale o áudio): "que seu time" (sem "o") · "**ele** nunca foi de ninguém" · "ele diz que **o chefe que** não liga" ·
"virou **o** presidente". **O CTA do meio ("Comenta ALMIRANTE que eu te mando o protocolo completo no direct") não foi gravado**: 80,8–88,2 s do
bruto é silêncio puro (−50 dB) — sem callout de ALMIRANTE. "Primeiro," existe (30,16–30,55 s, whisper em recorte; o passe por região fundiu com "Toda").

## Takes descartados (mantido o ÚLTIMO válido)
r00 parte 3 "Iman serrava a cadeira do candidato Iman." (falso início) → r01 · r14 parte 5 "Seu time deu o melhor essa semana, meu amiguinho." →
r15 "…meu amigo?" · r16 parte 2 "Se você…" (falso início) → r17.

## Bipe
"porra" ("Você tá torcendo, porra!"): oclusão /p/ 80,26–80,35 · explosão 80,36 · "o" 80,38–80,52 · "rr" 80,54–80,56 · "a" 80,58–80,72 · decai até 80,76.
Whisper em recortes cumulativos (de 76,80): até 80,25 "…torcendo"; até 80,45 "…torcendo, pô."; até 80,57 "…porra.". Bipe **80,30–80,80** do source.
Aceite na `voz-mix.m4a`: 64,36–64,81 s da timeline, 99,6% da energia em 950–1050 Hz, 0,12% fora de 900–1100 Hz. Legenda `P****!`.
Apresentador em tela cheia no bipe (61,37–65,23), com o callout "VOCÊ TÁ TORCENDO.".

## J-cut
27 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9 quadros (4,9–5,4) · respiro mediano 0,245 s.

## Olhar
`gaze_pose.py 2.0`: 23 janelas / 4,7 s; `gaze_windows`: 28 / 13,3 s. Nítidas, todas cobertas por tela cheia: 9,82–10,40 · 13,20–13,54 · 29,26–29,51 ·
31,73–32,28 · 33,49–34,34 · 41,42–42,03 · 46,07–46,62 · 48,87–50,33 · 52,33–52,91 · 60,53–60,72 · 72,31–72,74 · 85,81–86,51 · 87,98–88,23.
Expostas (sutis/piscada): capa 2,4–2,8 (dentro do split) · 10,88–11,04 · 12,00–12,17 · 21,81–22,00 · 34,72–34,90 · 61,70–61,92 · split da virada
66,38–66,66 e 67,32–67,53 · 74,29–74,44 · 83,09–83,73 · 89,62–90,47 (cabeça e olhar no "porque você é demais"). **Leitura exposta: ~1,1 s** (quase tudo
piscada/olhar sutil; o mais visível é o fim, 89,9–90,2). 2ª passada nos quadros da composição (bordas de cada aparição do apresentador): todas olhando a câmera.

## Split
`splitShiftY` **400** (olhos y≈982 no aroll em 13 pontos das janelas de split → 1377−979). Splits: capa 0–5,52 · virada 65,23–71,41.

## Marca só depois do nome
"Hyman" em 12,03 s → revelação em 12,13 (retrato de 1965 + "HYMAN RICKOVER · ALMIRANTE · MARINHA DOS EUA"). Pré-revelação: capa gerada (velho de costas,
sem rosto), Nautilus em construção (1953) e operário no casco (Electric Boat) — nada do Rickover. O presidente (Carter) só ganha nome no clímax ("presidente"
80,44); antes ele aparece só como o guarda-marinha anônimo da formatura de 1946 (split da virada).
Capa = **gerada a pedido** no Codex (`gpt-5.6-sol`, conta ChatGPT do Fabio por login de dispositivo; logout no fim): sala escura, uma lâmpada, cadeira de
madeira vazia com os pés da frente serrados e inclinada, velho de terno de costas na mesa de papéis, preto e âmbar (`work/capa/prompt.txt`). A mesma imagem
volta duas vezes: a cadeira vazia em "E a virada foi uma entrevista" e o velho de costas em "E virou a cadeira".

## Camada de motion (work/mg/gen.py) — dosagem Deming v2
Chip "PASSO N". Motion só em: a cadeira serrada (corta, o pedaço cai, ela inclina) · PASSO 1/2/3 · a tarefa com responsável (O COMERCIAL e O PESSOAL riscados,
JOÃO ✓ DONO) · 99% DO TEMPO + carimbo BESTEIRA · vendas zeradas por 6 meses (≈30% da cobertura). O resto é foto real (Marinha dos EUA/NARA, domínio público).
Callouts: 1º digitado "VOCÊ ACEITA / MAIS OU MENOS." (seg 1) · "TAREFA DE / NINGUÉM." (8) · "VOCÊ TÁ / TORCENDO." (17) · "POR QUE NÃO?" (22, curto: 0,64 s,
a fala seguinte entra logo — aviso de tweens sobrepostos no check) · "E VOCÊ? / POR QUE NÃO?" (26, `top` 57 sobre o Rickover encarando).

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
| enquadramento do split | `splitShiftY` (medido: 400) |
| zoom do apresentador | `presenterZoom` (1,06/1,14, uma troca por aparição; `sceneMax` 4,5) |
| volumes de trilha/SFX | `trilhaVol` no plano / seção SFX de `scripts/build-edit.mjs` → `bake.py bed` |
| transições | `sections` e `leakMinGap` (3,5) no plano |
| bipe | `scripts/bipe.py` (JANELAS ___ s do source) → `bake.py voz` |
| respiro / lead do J-cut | `TA`/`HH` em `scripts/cuts.py`; `jcutLeadFrames` (9) / `jcutCrossfadeFrames` (3) |
| tempos de timeline / palavra | `python3 scripts/tl.py [--words]` |

## Export final

`size_sweep.py`: `--size` **456** (12 partes, sobra mínima 149 quadros) · `render-par.sh 456 … 2` (2 em paralelo, 4 núcleos) · 0 falhas · **1446 s** (~4 min por par).
**Master:** `renders/Hyman-Rickover-reel-final.mp4` — 1440×2560 · 60 fps · 91,10 s · 5466 quadros (= timeline) · 256 MB (fora do git).
QC (`finalizar.py`): quadros = timeline OK · pico −0,5 dB / média −15,9 dB · trechos pretos 0 · bipe no MP4 99,1% em 1 kHz (64,40–64,78) ·
sincronia boca/voz lag mediano 10 ms (26/26 pontos, r > 0,6; −90 ms só em "E virou a cadeira", coberto pela capa) · bruto intacto (MD5 antes e depois
`bfc5ad9bf193e444218b1216588791b5`). Quadro a quadro: 56 quadros do MP4 (um por cena/transição) conferidos; quadro 0 = capa.
**Entregas (a partir do master):** `entrega/Hyman-Rickover-reel-chat.mp4` (x264 dois passes 2,2 Mbps, AAC 160k, 27,4 MB) ·
`entrega/Hyman-Rickover-reel-final.mp4` (HEVC libx265 dois passes 8 Mbps, `hvc1`, AAC 256k, `+faststart`; ver tamanho no commit) ·
`entrega/comparacao-master-x-hevc.jpg` (mesmo quadro, master × HEVC). Script: `work/entregas.sh`.

## Correções depois do render

- (nenhuma)

## Lições para o kit

Levadas para `KIT-EDICAO-REEL/docs/05` §27 (+ `ritmo.py` e `work/pesq/wmthumb.py` no modelo):
- `codex exec` em tarefa de fundo precisa de `< /dev/null` (senão espera stdin para sempre).
- Commons no container: original dá 429; baixar a miniatura padrão pela API (`wmthumb.py`).
- `mezanino.sh` direto não tem o venv no PATH: rodar pelo `fase1.sh`.
- Trecho do roteiro não gravado (CTA do meio): vale o áudio, avisar na entrega.
- Palavra curta no começo de região some no passe por região ("Primeiro,"): FIX + FIXT com whisper em recorte.
- Bandeira drapeada recortada em 9:16 pode parecer outra bandeira: trocar a foto.
- `ritmo.py` passa a contar os `cue()` da camada de motion.
