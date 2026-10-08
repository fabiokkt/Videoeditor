# EDICAO.md — mapa do projeto (reel Gene Kranz)

> Modelo do kit (`KIT-EDICAO-REEL/modelo-projeto/EDICAO.md`). Preencher ao longo da edição: é o que permite
> retomar o projeto meses depois e o que alimenta `docs/05` do kit quando aparecer uma lição nova.
> Tudo que for **regra geral** vai para o kit, não fica só aqui (ver "Lições para o kit" no fim).

Projeto HyperFrames 9:16, palco **1440x2560** (geometria calibrada 1080x1920 escalada por `#stage`), timeline a 30 fps,
saída final **1440x2560 @ 60 fps**. Velocidade **1,1x**.
**Estado (2026-10-07): RENDERIZADO** — ver "Export final" no fim. Comando único sem parada, numa sessão do Claude Code **na nuvem**
(Linux, 4 núcleos, 16 GB).
Duração **93,25 s** · 28 takes · 1 bipe · 100 legendas · 5 callouts · 4 light-leaks (virada, clímax, CTA + gancho) · 10 SFX fixos + 77 da camada ·
9 slots (2 splits + 7 cenas de tela cheia na camada de motion, `work/mg/gen.py`).

## Bruto e roteiro
`~/Claude/videos-brutos/gene-kranz-bruto.mov` (iCloud `0e5x-xcddwsPZCLGnKBQ1RBjg`) — **não alterado**, MD5 `7be4c0dc2d6909d92cefa8883bb274db`.
HEVC 1440x2560 @60, 159,0 s, SDR full-range → mezanino full→limited; cor bruto × mezanino (15,9/79,5/143,1 s): 122,87/122,88 · 124,85/124,86 ·
124,47/124,61, desvio 55,25/55,26 · 55,22/55,22 · 55,28/55,37 — não lavou. O link do iCloud ficou vazio por ~8 min depois de criado (o vídeo ainda subia
do iPhone): laço de 30 s no `ic.py` até o asset aparecer.
Roteiro: ClickUp > Cronograma > "Gene Kranz" (v2 FINAL, 07/10/2026), seção "Roteiro" + "Nota de gravação".
Onde o áudio diverge do roteiro (vale o áudio; passe por região + whisper em recorte SEM prompt concordam):
"pelo que **você** deixa de fazer" (a mais) · "Seu time tá vendo alguma coisa, meu amigo." (**sem o "agora"**; nem com o roteiro no `--prompt` o whisper
ouve "agora"). Homófonos → roteiro: "em toda (a) missão", "promete (e) entrega pra sexta" (whisper: "para a cesta"), "Se (o) seu time".
**Sem CTA de palavra-chave** (o roteiro não tem: é o controle do teste — "Sem palavra-chave falada e sem pergunta no fim"); nada de "Comenta …" no bruto.

## Takes descartados (mantido o ÚLTIMO válido)
r04 "e comandava a sala no dia de o homem..." → r05 · r19 "...pequeno agaf..." + r20 → r21 (o whisper ouve "juta", mas o /ch/ é surdo: 91,30–91,36 com 2–4%
da energia < 500 Hz, igual ao "chuta" do r20) · r24 "Ele juntou o time e disse..." + r25 "...gritou, porra..." → r26 · **o fim refeito a partir de "A culpa é nossa"**:
r27–r33 (A culpa é nossa / Três anos depois... / Mesma sala... / Os três voltaram vivos / Seu time tá vendo... (parou) / A culpa é nossa / Três anos depois, o ap... (parou))
→ r34–r39. Divisões nos vales: r22 em 97,34 ("segunda-feira." | "Em 1967") · r34 em 140,665 ("A culpa é nossa!" | "Três anos depois"; o whisper punha "nossa!"
até 141,11 dentro do vale real 140,59–140,74 → `WFIX`). "Primeiro, [pausa] pressa não é desculpa" e "...meu amigo. [pausa] Pergunta." ficam como um take só (pausa dramática).

## Bipe
"porra" ("...nenhum de nós levantou e gritou: porra, para!"): fim do "gritou" 115,80–115,94 · oclusão /p/ 115,96–116,02 (−48 dB) · "po" 116,04–116,22 ·
vão 116,24–116,36 · "rra" 116,38–116,72 (vogal gritada) · oclusão do /p/ de "para" 116,74–116,90 · "para!" 116,92–117,26. Whisper em recortes do áudio limpo:
até 116,03 e até 116,30 "...levantou e gritou..." (sem a palavra); até 116,74 "...gritou, porra,"; de 116,74 só "Para...". Bipe **115,97–116,75** do source
(palavra inteira; o /p/ de "para" fica limpo). Legenda `P****,`. Apresentador em tela cheia no bipe (72,72–78,62). Aceite no MP4: ver "Export final".

## J-cut
27 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9 quadros (4,9–5,1) · respiro mediano 0,245 s (1 pausa curta emendada no silêncio:
"nossa | Três", 0,26 s).

## Olhar
`gaze_pose.py 2.0`: 20 janelas / 5,1 s; `gaze_windows`: 20 / 7,0 s. Folhas `gaze/me/g00-g02` + recortes grandes (`work/qc/eyes*.jpg`): o apresentador olha
para a câmera quase o tempo todo. Desvios reais e o que foi feito:
- 10,36–10,56 (fim de "esconder", olho baixo): a revelação começa em 10,36 com a capa de costas e troca para o rosto do Kranz 2 quadros depois de "Gene".
- 34,35–34,75 ("meu querido", pálpebra baixa) e 35,02–35,38 (olhos fechados/baixos na pausa antes de "É roleta." — os medidores de janela NÃO pegaram;
  achado num quadro da parte 4 renderizada e confirmado pela varredura de `gaze/tl.json` nos trechos com o apresentador visível): a semana do PASSO 1 fica
  na tela até 35,50 (re-render só das partes 1 e 4).
- 62,85–63,26 (olha para baixo antes de "Em 1967", dentro do split da virada): split encurtado para 61,64–62,80 e a mesma foto abre em tela cheia (§29).
- Ficam (não é leitura): 88,40–88,64 aceno de cabeça no "Pergunta." · 90,7–92,4 o gesto de apontar no "me segue" (olho na mão, §30).
**Leitura exposta: 0 s.**

## Split
`splitShiftY` **393** (olhos y≈985 no mezanino em 11 pontos das janelas de split → 1377−984; `work/olhos_y.py`). Splits: capa 0–4,86 · virada 61,64–62,80.

## Marca só depois do nome
"Gene" em 10,85 s → rosto em 10,92 (Kranz de colete branco no console, 1972 + "GENE KRANZ · DIRETOR DE VOO DA NASA"). "NASA" é dito no gancho (4,01 s): a sala
de 1965 entra no split em 2,38 sem logo (recortada sem a bolsa com o logo). Pré-revelação: capa gerada (homem de costas), a sala de 1965, o time da Apollo 13 —
nada do rosto do Kranz. Capa = **gerada a pedido** no Codex (`gpt-5.6-sol`, conta ChatGPT do Fabio por login de dispositivo; 1º código aceito; logout logo depois
de gerar) a partir da cena da seção "Capa" da tarefa: sala de controle no escuro, fileiras de telas verdes, alarme vermelho estourando, homem de pé de costas,
colete branco e cabelo raspado (`work/capa/prompt.txt`). Sem texto, rosto, logotipo ou bandeira. Assunto entre 5% e 48% da altura (acima da caixa do gancho).

## Camada de motion (work/mg/gen.py + work/mg/parts.py + work/mg/fotos.py + work/mg/tempos.py) — dosagem Deming v2
Chip "PASSO N". Motion só em: PASSO 1/2/3 (chip + título) · a semana com a SEXTA prometida (ENTREGA → X, NÃO DÁ) · os AVISOS DO SEU TIME: 0 · a ordem
1 DESCOBRE (PRIMEIRO) / 2 MEXE (DEPOIS) / CHUTAR (NUNCA) · a virada: PROBLEMA VISTO ×3 · ALGUÉM PAROU? NINGUÉM (≈28% da cobertura: 19 de 67 s).
O resto é foto real da NASA (domínio público, LICENCAS-FOTOS.txt): revelação com anel no colete, a sala da Apollo 11, Aldrin na Lua, a nave da Apollo 1 na montagem
e no Pad 34 (callback na virada: "num teste no chão"), Kranz no console em 1965 com O QUE VOCÊ FAZ / O QUE DEIXA DE FAZER, a sala na crise da Apollo 13 com a fala
do Kranz em balão, a tripulação da Apollo 1 (sem imagem do incêndio).
Clímax: o módulo de serviço da Apollo 13 sem o painel (anel no rombo) → "Mesma sala, mesmo chefe": a foto da 4ª transmissão de TV (13 abr 1970, minutos antes da
explosão) com o anel no Kranz de costas → "Os três voltaram vivos": a tripulação descendo no USS Iwo Jima.
Callouts: 1º digitado "FOI VOCÊ QUE / ENSINOU." (seg 2) · "É ROLETA." (9) · "COM O ÚLTIMO / QUE AVISOU?" (13) · "A CULPA / É NOSSA." (22) · "PERGUNTA." (26).
`ritmo.py`: maior intervalo sem evento 4,58 s (72,52–77,10, o apresentador no bipe).

> **Regra de ouro: nunca editar `index.html` à mão.**
```
editar assets/edit-plan.json (ou work/mg/tempos.py) -> python3 work/mg/fotos.py && python3 work/mg/gen.py -> zsh scripts/montar.sh <instantes>
(cortes: scripts/mkcut.py / cuts.py -> zsh scripts/fase2.sh · legendas: scripts/captions_fix_table.py -> zsh scripts/legendas.sh)
```

## Onde mexer em cada coisa

| Quero mudar… | Arquivo |
|---|---|
| cortes / takes (in/out) | `scripts/mkcut.py` (divisões/descartes/WFIX) → `scripts/cuts.py` (lista TAKES) → `work/segs.json` → `python3 scripts/plan_segments.py` |
| texto de legenda | `scripts/captions_fix_table.py` (FIX/FIXT por chunk e índice de palavra) → `zsh scripts/legendas.sh` |
| callouts | `impacts` no plano (frase, seg, linhas, hold; o 1º com `style: typing`) |
| janelas de cobertura | `work/mg/tempos.py` (lido por `scripts/slots.py` e `work/mg/gen.py`) → `zsh scripts/montar.sh` |
| fotos / recortes | `work/mg/fotos.py` (papel → arquivo da NASA + recorte) |
| cenas da camada | `work/mg/gen.py` (F = foto por papel, OP = enquadramento, CENAS) e `work/mg/parts.py` (CSS) |
| enquadramento do split | `splitShiftY` (medido: 393 — `work/olhos_y.py`) |
| transições | `sections` (após os segs 17, 22, 26) e `leakMinGap` (3,5) no plano |
| bipe | `scripts/bipe.py` (JANELAS 115,97–116,75 s do source) → `bake.py voz` |
| tempos de timeline / palavra | `python3 scripts/tl.py [--words]` |

## Export final

`size_sweep.py`: `--size` **431** (13 partes, sobra mínima 141 quadros) · `render-par.sh 431 … 2` (2 em paralelo, 4 núcleos) · 0 falhas · **1489 s** (~3,7 min por par)
+ re-render só das partes 1 (173 s) e 4 (198 s): a semana do PASSO 1 estendida até 35,50 (olhada 35,02–35,38 achada num quadro da parte 4) e o anel do colete
descido para a cava do colete. O processo da sessão reiniciou no meio desse re-render: o `render-par.sh` retomou e refez só a parte que faltava.
**Master:** `renders/Gene-Kranz-reel-final.mp4` — 1440×2560 · 60 fps · 93,25 s · 5595 quadros (= timeline) · 239 MB (fora do git).
QC (`finalizar.py` + `work/qc_final.sh`): quadros = timeline OK · pico −0,7 dB / média −19,1 dB · trechos pretos 0 · bipe no MP4 98,8% em 950–1050 Hz e 1,2% fora
de 900–1100 Hz (75,54–76,19 s; o resto é a trilha por baixo; na `voz-mix.m4a` 100%) · sincronia boca/voz lag mediano 10 ms (28/28 pontos com r > 0,6; 27 entre 0 e
10 ms; o −80 ms do seg 14 "E terceiro, não chuta." (1,83 s) é a janela de 1,2 s do medidor invadindo o take seguinte, §30 — e o trecho fica sob o chip do PASSO 3)
· bruto intacto (MD5 antes e depois `7be4c0dc2d6909d92cefa8883bb274db`). Quadro a quadro: 60 quadros do MP4 (um por cena/transição, `work/qc/folha-1..3.jpg`)
conferidos; quadro 0 = capa; rosto do Kranz 2 quadros depois de "Gene".
**Entregas (a partir do master, `work/entregas.sh`):** `entrega/Gene-Kranz-reel-chat.mp4` (x264 dois passes 2,2 Mbps, AAC 160k; **27,9 MB**) ·
`entrega/Gene-Kranz-reel-final.mp4` (HEVC libx265 dois passes **7,9 Mbps** — reel de 93,25 s < ~95 s; teto pelo alvo de 96 MB —, `hvc1`, AAC 256k, `+faststart`) ·
`entrega/comparacao-master-x-hevc.jpg` (quadro 744 = 12,40 s, o Kranz de colete com a etiqueta de nome, master × HEVC). Final: **95,6 MB**, 7,92 Mbps de vídeo,
5595 quadros, `moov` antes do `mdat`; SSIM do vídeo inteiro **0,993**.

## Correções depois do render

- (nenhuma)

## Lições para o kit

- **Link do iCloud recém-criado pode vir vazio** (`resolve` responde `videosCount: 1`, mas a consulta de assets volta `records: []` — o iPhone ainda está subindo):
  não é erro do `ic.py`; repetir a cada 30 s em tarefa de fundo (aqui ~8 min) e seguir com a pesquisa de fotos e o login do Codex.
- **NASA Image and Video Library (`images-api.nasa.gov`) é a fonte primária para tema da NASA**: busca por texto que funciona, descrição completa com data e
  nomes, original `~orig.jpg` sem 429 e domínio público — 16 fotos em ~2 min, sem a fila do Commons (§30/§31). `work/pesq/nasa.py` (busca), `nasadesc.py`
  (descrição) e `nasadl.py` (download + licenças) neste projeto.
- Revelação que precisa cobrir uma olhada logo antes do nome: a cena de revelação começa com a capa de costas e troca para o rosto 2 quadros depois do nome.
- Janela de cena compartilhada entre `slots.py` e `gen.py` num só arquivo (`work/mg/tempos.py`): mudar um tempo de cena num lugar só.
