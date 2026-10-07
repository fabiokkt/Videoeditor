# EDICAO.md — mapa do projeto (reel John Wooden)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
**Estado (2026-10-06): RENDERIZADO** — ver "Export final" no fim. Comando único sem parada, numa sessão do Claude Code **na nuvem**
(Linux, 4 núcleos, 16 GB).
Duração **89,392 s** · 31 takes · 1 bipe · 94 legendas · 5 callouts · 5 light-leaks (virada, clímax, CTA + gancho) · 12 SFX fixos + 66 da camada ·
10 slots (2 splits + 8 cenas de tela cheia na camada de motion, `work/mg/gen.py`).

## Bruto e roteiro
`~/Claude/videos-brutos/john-wooden-bruto.mov` (iCloud `07aKGfM3o9F5pWaTWtmrxuMfg`) — **não alterado**, MD5 `04028ff1a25b3797c16aaa4f04599996`.
HEVC 1440x2560 @60, 145,50 s, SDR full-range → mezanino full→limited; cor bruto × mezanino (14,55/72,75/130,95 s): 119,60/119,67 ·
119,25/119,32 · 119,47/119,53, desvio 64,17/64,14 · 64,34/64,31 · 63,92/63,90 — não lavou. Roteiro: ClickUp > Cronograma > "John Wooden" (v1, 04/10).
Onde o áudio diverge do roteiro (vale o áudio): "a calçar **a** meia" · "**o** atraso é desrespeito com **todo o** time" (roteiro: "com o tempo do time") ·
"voltou **de** férias" (roteiro: "das férias"). **O CTA do meio ("Comenta ESTRELA que eu te mando o protocolo completo no direct") não foi gravado**
(nenhuma das 34 regiões de fala tem a frase) — sem callout de ESTRELA.

## Takes descartados (mantido o ÚLTIMO válido)
r01/r02 falsos inícios de "E ele criou um protocolo polêmico…" + r03 "Boa droga." → r04 · r06 "E o protocolo pra você…" (sem "esse é") e r07 "E esse é o
protocolo pra…" → r08+r09 · r11 "Se o melhor vendedor chega às 10h," → r12 · r15 "Ele obrigava a quem…" → r16 · r17 "…o parabéns do grupo?" + r18 ruído →
r19 · r21 "Seu treinador…" → r22 · r23 parte 2 "está vendendo a…" (tropeço) → r24 "Tá perdendo a porra do resto do time."

## Bipe
"porra" ("Tá perdendo a porra do resto do time."): "a" 108,69–108,81 · oclusão /p/ 108,83–108,96 · explosão 108,97 · "o" 108,98–109,11 · "rr" 109,12–109,16 ·
"a" 109,17–109,22 · /d/ de "do" a partir de 109,23. Whisper em recortes cumulativos (de 107,90): até 108,95 "…perdendo a"; até 109,05 "…apoio" (o "po");
até 109,12 "…a porra."; até 109,25 "Tá perdendo a porra.". Bipe **108,86–109,23** do source.
Aceite na `voz-mix.m4a`: 60,75–61,08 s da timeline, 100,0% da energia em 950–1050 Hz, 0,00% fora de 900–1100 Hz. Legenda `P****`.
Apresentador em tela cheia no bipe (57,21–62,34), com o callout "DO RESTO / DO TIME.".

## J-cut
30 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9 quadros (4,9–5,4) · respiro mediano 0,245 s.

## Olhar
`gaze_pose.py 2.0`: 17 janelas / 4,2 s; `gaze_windows`: 14 / 5,1 s. Nítidas, todas cobertas por tela cheia: 9,28–9,93 · 23,29–23,87 · 24,11–24,35 ·
27,45–27,75 · 34,25–34,59 · 38,36–39,79 · 44,79–45,19 · 50,65–51,01 · 52,77–53,22 · 53,60–53,81 · 69,78–70,45 · 71,89–73,23 · 84,07–84,28.
Expostas (sutis/piscada): capa 0,67–1,12 (dentro do split) · 9,95–10,00 (fim da olhada, na volta do apresentador) · 20,77–20,93 · 31,69–31,91 (piscada) ·
82,74–82,89. **Leitura exposta: ~0,5 s**, toda sutil. 2ª passada nos quadros do apresentador nas bordas de cada aparição (29 pontos): olhando a câmera.

## Split
`splitShiftY` **344** (olhos y≈1033 no aroll em 13 pontos das janelas de split → 1377−1033). Splits: capa 0–5,19 · virada 62,34–69,70.

## Marca só depois do nome
"John" em 11,28 s → revelação em 11,35 (retrato + "JOHN WOODEN · TÉCNICO DE BASQUETE · UCLA"). Pré-revelação: capa gerada (técnico e gigante de costas,
sem rosto) e dois jogos de basquete genéricos (colégio Worthington, anos 50, e Warriors) — nada do Wooden nem da UCLA. O Bill Walton só ganha nome em
"Bill" (73,90 → 73,97); antes ele aparece anônimo (o barbudo do split da virada e o protesto de 1972).
Capa = **gerada a pedido** no Codex (`gpt-5.6-sol`, conta ChatGPT do Fabio por login de dispositivo; logout no fim): vestiário escuro dos anos 70, uma
lâmpada, o técnico baixinho de terno com a prancheta e o gigante de 2 m de costas, a navalha na pia, preto e azul elétrico (`work/capa/prompt.txt`). A mesma
imagem volta duas vezes: a navalha em "E a virada foi uma barba" e em "Antes do treino, ele tava sem barba".

## Camada de motion (work/mg/gen.py) — dosagem Deming v2
Chip "PASSO N". Motion só em: 10 títulos em 12 temporadas (1966 e 1974 apagadas) · a meia (as dobras somem, ✓ SEM DOBRA) · PASSO 1/2/3 · o relógio das dez
(sob o callout "NA HORA QUE VOCÊ DEIXOU.") · o grupo de vendas (PARABÉNS ×14 pro vendedor, 0 reações pra proposta da pré-venda) · o grupo da empresa (o
vendedor estrela esculacha o financeiro, o dono ri) (≈35% da cobertura). O resto é foto real (anuários da UCLA, LA Times/UCLA Library, DPLA).
Callouts: 1º digitado "NÃO VALE / PRA NINGUÉM." (seg 1) · "NA HORA QUE / VOCÊ DEIXOU." (8, sobre o relógio) · "DO RESTO / DO TIME." (18, bipe) ·
"E O TIME VAI / SENTIR SUA FALTA." (26, clímax) · "E POR QUE ELE AINDA / TÁ DE BARBA?" (29, `top` 62, abaixo do retrato do Walton).

> **Regra de ouro: nunca editar `index.html` à mão.**
```
editar assets/edit-plan.json (ou scripts/slots.py / work/mg/gen.py)  ->  zsh scripts/montar.sh <instantes>  ->  apagar renders/chunks das partes afetadas
->  zsh scripts/render-par.sh 447 renders/John-Wooden-reel-final.mp4 2  ->  bash work/entregas.sh
```

## Onde mexer em cada coisa

| Quero mudar… | Arquivo |
|---|---|
| cortes / takes (in/out) | `scripts/mkcut.py` (divisões/descartes) → `scripts/cuts.py` (lista TAKES, FORCE_IN/FORCE_OFF) → `work/segs.json` → `python3 scripts/plan_segments.py` |
| texto de legenda | `scripts/captions_fix_table.py` (FIX por chunk e índice de palavra) → `zsh scripts/legendas.sh` |
| callouts | `impacts` no plano (frase, seg, linhas, hold, `top` opcional; o 1º com `style: typing`) |
| cenas / fotos / motion | `work/mg/gen.py` (gera `compositions/mg.html`) · janelas em `scripts/slots.py` |
| enquadramento do split | `splitShiftY` (medido: 344) |
| zoom do apresentador | `presenterZoom` (1,06/1,14, uma troca por aparição; `sceneMax` 4,5) |
| transições | `sections` e `leakMinGap` (3,5) no plano |
| bipe | `scripts/bipe.py` (JANELAS 108,86–109,23 s do source) → `bake.py voz` |
| respiro / lead do J-cut | `TA`/`HH` em `scripts/cuts.py`; `jcutLeadFrames` (9) / `jcutCrossfadeFrames` (3) |
| tempos de timeline / palavra | `python3 scripts/tl.py [--words]` |

## Export final

`size_sweep.py`: `--size` **447** (12 partes, sobra mínima 149 quadros) · `render-par.sh 447 … 2` (2 em paralelo, 4 núcleos) · 0 falhas · **1289 s** (~4 min por par).
**Master:** `renders/John-Wooden-reel-final.mp4` — 1440×2560 · 60 fps · 89,40 s · 5364 quadros (= timeline) · 213 MB (fora do git).
QC (`finalizar.py`): quadros = timeline OK · pico −1,0 dB / média −19,9 dB · trechos pretos 0 · bipe no MP4 99,4% em 1 kHz (60,76–61,09) ·
sincronia boca/voz lag mediano 10 ms (29/31 pontos com r > 0,6; faixa −30..10 ms) · bruto intacto (MD5 antes e depois `04028ff1a25b3797c16aaa4f04599996`).
Quadro a quadro: 89 quadros do MP4 (1 por segundo) + transições conferidos; quadro 0 = capa; camada de motion presente nas partes.
**Entregas (a partir do master, `work/entregas.sh`):** `entrega/John-Wooden-reel-chat.mp4` (x264 dois passes 2,2 Mbps, AAC 160k, **27,0 MB**) ·
`entrega/John-Wooden-reel-final.mp4` (HEVC libx265 dois passes **8,0 Mbps**, `hvc1`, AAC 256k 48 kHz, `+faststart`, **92,7 MB**) ·
`entrega/comparacao-master-x-hevc.jpg` (quadro 72,70 s, master × HEVC; SSIM do vídeo inteiro 0,995).

## Correções depois do render

- (nenhuma)

## Lições para o kit

Levadas para `KIT-EDICAO-REEL/docs/05` §28 (+ `work/pesq/wmstd.py` no modelo e linha em `docs/11`):
- Commons no container: baixar a miniatura de tamanho padrão montando a URL (`wmstd.py`), sem chamar a API por arquivo (a API passou a dar 429 em tudo e o
  `wmthumb.py` ficou 30 min parado); cortar o `?utm_…` da URL; o `thumb` do `wm.py` vira o original quando a largura pedida passa a do arquivo.
- Arquivo do Los Angeles Times na UCLA Library (CC BY 4.0) no Commons: boa fonte de esporte dos anos 60–70; crédito obrigatório.
- `until ! pgrep -f "<texto do próprio comando>"` nunca termina (o laço se acha).
- `FIX` com duas palavras numa entrada ("por que") vira um token no `impacts[].phrase`: escrever "porque" na frase do callout.
- Retrato com fundo branco / camisa de outro time: card de retrato (`.pcard`) num mundo escuro em vez de tela cheia.
- CTA do meio não gravado pela 2ª vez seguida: vale o áudio, avisar.
