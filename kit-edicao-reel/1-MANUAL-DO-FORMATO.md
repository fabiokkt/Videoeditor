# Manual do formato — Reel Viral do Fabio (kit v3.1, compactado)

Tudo que o kit `KIT-EDICAO-REEL` sabe, num arquivo só e já reconciliado: o estado **atual** do formato depois de
33 reels. Derivado do kit v3.1 (commit `47e642e`, 2026-10-02); compactado em 2026-10-04.

**Como ler este manual**
- Ele é o resumo coerente. O texto original, com o porquê de cada regra e o reel em que ela nasceu, está em
  `2-REFERENCIA-DOCS-DO-KIT.md`; o código, em `3-CODIGO-DO-MOTOR.md`.
- Os docs originais foram escritos em épocas diferentes e se contradizem em três pontos (parada, light-leak,
  B-roll). **Vale o mais novo: `docs/14` e `docs/05` §23–24.** Este manual já aplica isso.
- **Números travados não se recalculam, não se re-perguntam e não se "melhoram".** Um pedido explícito do Fabio
  vence qualquer número daqui e vira regra nova.
- Convenção: "f" ou "quadros" = quadros da timeline a 30 fps, salvo indicação. Medidas de tela na geometria
  1080×1920.

---

## 1. O que é

Formato "engenharia reversa de uma história de sucesso": o Fabio fala para a câmera (talking-head vertical),
coberto por fotos reais do tema e por motion graphics, com o nome da pessoa ou empresa guardado até a narração
revelar. Ele grava lendo o roteiro, então desvia o olhar no começo e no fim de quase todo take.

- **Motor:** HyperFrames (composição HTML + GSAP, renderizada pelo Chrome). O formato é o do kit; onde as skills
  do HyperFrames divergirem, vale o kit.
- **Onde roda:** Claude Code no Mac, com o kit em `~/Claude/KIT-EDICAO-REEL`, projetos em
  `~/Claude/reel-auto/<slug>`, brutos em `~/Claude/videos-brutos/`. Ferramentas: ffmpeg, whisper-cli, Node ≥ 20,
  Python 3.12 (`~/Claude/.venv-reel`: numpy, opencv, Pillow, mediapipe), Google Chrome.
- **Tempo:** ~1 h do bruto ao MP4 (fluxo rápido, kit v3).

## 2. Ficha do formato (números travados)

| Parâmetro | Valor |
|---|---|
| Quadro | 9:16 · palco `#root` 1440×2560 com `#stage` 1080×1920 em `scale(4/3)` |
| fps | timeline **30** · arquivo final **60** |
| Velocidade | **1,1x** no vídeo todo, tom da voz preservado (`atempo`). "acelere 1.1" sobre 1,1 → 1,21; "só um pouquinho" → 1,15 |
| Duração | a do roteiro (hoje 90–100 s). Nunca cortar roteiro por conta própria |
| Cenas | **3–5 s**; ~4 s é alvo **e** teto. A cada 4 s algo acontece (cena, zoom, callout, transição) |
| Split-screen | B-roll **44%** em cima (845 px) / apresentador **56%** embaixo · arrasto de 0,55 s `power3.inOut` |
| `splitShiftY` | **medir em todo bruto** (já deu de 260 a 550): olhos a ~49% da faixa do apresentador |
| Zoom do apresentador | 1,06 / 1,14 · uma troca por aparição · `mode: scene`, `sceneMax` 4,5, `origin` 50% 53% |
| Legenda | Montserrat **600 / 47 px**, branca, **sem contorno**, halo de 3 sombras · até 3 palavras, quebra na pontuação |
| Legenda, posição | **44%** sobre B-roll e no split · **76%** com o apresentador sozinho e sobre a camada de motion |
| Capa (gancho) | frase inteira no quadro 0 · caixa laranja **#FF4A1C** · **Oswald 700, caixa alta, 90 px** |
| Callout | Montserrat **800 / 76 px CAPS**, contorno 10 px, a **30%** da altura · **≤ 5** por reel; o 1º com digitação |
| J-cut | `jcutLeadFrames` **9** · `jcutCrossfadeFrames` **3** → fala entra ~5 quadros antes do corte de imagem |
| Folgas de corte | `HEAD_PAD` 0,20 · `TAIL_PAD` 0,13 · `TA` 0,12 · `HH` 0,15 → respiro mediano ~0,245 s |
| Light-leak | 0,7 s, começa 10 quadros antes do corte, `screen`, opacidade 0,85 · `leakMinGap` 3,5 |
| CTA | push-in 1 → 1,05 a partir de `ctaSeg` |
| Trilha | 0,079 → 0,045 (últimos ~9 s) → 0 (fade 0,7 s) · `trilhaLoop` se passar de 164 s |
| Áudio final | `amix(voz-mix, bed, normalize=0)` + `alimiter=limit=0.891:level=disabled` (−1 dBTP) · AAC 256 kb/s 48 kHz |
| CLI | `hyperframes@0.8.64` no projeto; `render-chunks.mjs` chama `0.8.48`. Combinação validada: não atualizar no meio de um reel |

**SFX fixos (todos no `bed.m4a`)**
- intro `intro-cinematic-opening` **0,25** + `intro-when-emphasizing-riser` **0,22**, de 0 a 3,2 s
- `boom-cinematic` em 4,8 s, **0,12**
- `drum-fill` em 7,0 s, **0,166** — suprimido se o callout de digitação cai entre 5,5 e 9,5 s
- `drum-fill` do callout de digitação, **0,3**
- `whoosh` → `swoosh` → `whoosh-transition` alternados, **0,18**, um por light-leak
- `riser` **0,2** 3 s antes do clímax · `impact-hit` **0,3** na entrada do clímax (seção com "CLIMAX" no nome)
- SFX da camada de motion por cima (`mg_sfx.py`), impactos ≤ −16 dB: a voz fica ≥ 6 dB acima

**Regra de ouro do mix:** SFX é toque curto no corte. Nunca batida, tique ou loop contínuo sob a fala (foi
reportado como "áudio quebrado").

Assets fixos (em `assets-fixos/`, iguais em todo reel): trilha `trilha-epic-cinematic-corporate.mp3`, 9 SFX,
`transicao-light-leak.mp4`, fontes Montserrat 600/800 e Oswald 700, modelo `face_landmarker.task`.

## 3. Estrutura de um reel

| Bloco | Na tela |
|---|---|
| 1. Capa e intro | **Split desde o quadro 0**: foto em cima, apresentador embaixo, caixa laranja com o gancho. Nenhuma marca |
| 2. Revelação | O áudio diz o nome pela 1ª vez e a imagem do tema entra em tela cheia, 2 quadros depois |
| 3. Corpo | Alterna cobertura de tela cheia (foto ou motion) e apresentador em tela cheia |
| 4. Virada | O split volta, uma segunda vez |
| 5. Clímax | Tela cheia, riser 3 s antes e impacto na entrada |
| 6. CTA | Apresentador em tela cheia, push-in lento |

**Dosagem foto × motion (regra desde o reel Deming v2):**
- **Abertura (capa + pré-revelação) = só fotos**, com Ken Burns e corte por chicote ou queda. Nada de etiqueta,
  crachá, carimbo ou UI por cima. O callout de digitação continua.
- **No corpo, foto real é o padrão.** Tudo que dá para mostrar com foto (pessoa, lugar, objeto, situação) vai de
  foto em tela cheia, no máximo com uma etiqueta.
- **Motion só onde carrega a história:** título de capítulo (chip PASSO N + título), número que precisa ser
  visto, o mecanismo do clímax, objeto que a fala nomeia e não existe em foto. **≤ ~40% do tempo de cobertura em
  UI animada.**
- Gráfico que só repete a fala → apresentador em tela cheia (respira o ritmo).

## 4. O que aparece na tela

### Capa (quadro 0)
- O quadro 0 **é** a capa: frase inteira do gancho já na tela, sem animação de entrada. Conferir o snapshot em t=0.
- Caixa laranja #FF4A1C (gradiente, borda branca, glow), 1016 px de largura, Oswald 700 caixa alta 90 px, contorno
  12 px + sombra dura, pulso **1,018** (1,035 vaza da tela), brilho atravessando duas vezes. Sem `text-wrap: balance`.
- A caixa cobre ~35–56% da altura e fica até o fim do gancho, inclusive sobre a tela cheia que entrar antes: o
  assunto da foto de capa fica **no terço de cima** (gerar o split da imagem 4:3 inteira).
- **A primeira cena é sempre split**, mesmo com olhada no gancho: split curto de capa → cutaway de tela cheia
  cobrindo a olhada → split volta com o arrasto. Reportar os décimos expostos.
- O gancho é a 1ª frase inteira, num take só (juntar regiões ou dividir no vale se preciso).
- Legado: `"hookSeg": null` + `"yellowCapSegs": [0]` volta à caixa amarela antiga.

### Split-screen
- `splitShiftY` se mede: altura dos olhos no `aroll` (FaceMesh, média do `y` dos landmarks 33/133/362/263) em vários
  pontos **dentro das janelas de split**; aplicar o zoom (`y_zoom = origem + (y_olhos − origem) × escala`); alvo
  y ≈ **1377** (49% da faixa 845–1920); `splitShiftY = 1377 − y_zoom`. Conferir no snapshot.
- O cover-crop do split mostra só 44% da altura: assunto fora da faixa → `objectPosition` ou recompor a foto.
- Dentro do split a legenda fica sempre na divisa (44%); a 76% cai na boca do apresentador.

### Legendas
- Branca sem contorno some em fundo claro: **escurecer a imagem**, não mexer na legenda. Na camada de motion, o
  mundo claro (`.light`) tem "chão" escuro abaixo de ~64% da tela.
- Sobre foto/B-roll de tela cheia, desce para 76% (`capLowSegs`) quando cairia em rosto, logotipo ou título.
  Decidir olhando snapshot por snapshot; conferir os dois lados quando a legenda cruza um corte.
- Na camada de motion, deixar livre a faixa **y ≈ 1380–1540**.
- **Texto:** grafia, pontuação e maiúsculas seguem o roteiro ("pra", "tá", números por extenso, nomes próprios).
  Onde o **áudio diz outra coisa**, vale o áudio (registrar a divergência). Palavra bipada: `P****`, `M****`,
  entrando junto com o bipe.

### Callouts
- 1º: digitação (caractere a caractere em ≤ 1,35 s) + drum-fill + pulso de settle. Demais: `popIn`
  `back.out(2.4)`, rotação −5°, grow 1,07, saída 0,22 s. Sempre `tl.set autoAlpha 0` no fim.
- `impacts[].seg` prende ao segmento; `impacts[].top` desloca quando há rosto na faixa dos 30%.
- Callout que cobre os olhos de um retrato: tirar. Callout branco sobre fundo branco: trocar a imagem.
- Só onde o motion não diz a mesma coisa.

### Marca só depois do áudio
- **Nada que identifique a pessoa/empresa antes de o áudio dizer o nome pela 1ª vez**: logo, letreiro, rosto,
  livro, produto. Tema = pessoa → o gatilho é o nome dela, e a empresa entra junto.
- Achar o instante pela palavra (`tl.py --words`). A revelação entra **2 quadros depois** do início da palavra
  (no quadro exato a emenda arredonda e a marca vaza 1 quadro antes).
- Pré-revelação: material real do tema sem marca (interior, detalhe, recorte abaixo do letreiro) ou cena genérica
  do assunto. Capa gerada: pessoa-tema **de costas**.
- Conferir por snapshot: registrar último quadro limpo e primeiro com marca.

### Imagens
- **Fotos reais do tema, que mostrem o que a fala daquele trecho diz.** Sem banco de imagens, sem marca d'água.
- **Só a câmera se move** sobre a foto; texto, logotipo e marca ficam idênticos ao original. Letreiro largo:
  pull-out terminando com o texto inteiro, ou estático (zoom-in decepa).
- Duas fotos parecidas em sequência contam como "parado": alternar assunto, escala e luminosidade.
- **IA generativa só para a capa ou quando o Fabio descreve a cena**, marcada "gerada a pedido". Nunca por conta
  própria para suprir foto que falta.
- Vídeo entregue pelo Fabio (`broll1.mp4`): velocidade normal, mudo, só normalizado. Esticar foi reprovado.
- Licença e fonte de cada foto registradas. CC BY-NC e "direitos reservados" são pendência para ele decidir.

## 5. O que se ouve

### Cortes e takes
- **Frase ou take repetido: fica sempre o ÚLTIMO válido.** Falso início sai inteiro. Varrer a transcrição toda.
- "porque você… é demais" com pausa dramática é um take só, não repetição.
- **Nenhuma palavra cortada no meio.** O corte cai no silêncio real.
- Dividir fala longa nos **vales reais** (`valleys.py`: −38 dB, ≥ 0,16 s): dá ritmo e abre janela de cobertura. Não
  dividir se o silêncio real é < ~120 ms.
- **Head:** onset por RMS (20 ms, −27 dB, 4 de 8 janelas), recuando até o piso, − `HEAD_PAD`.
- **Tail:** `min(fim da última palavra, offset RMS a −45 dB)` + trava: enquanto o nível ≥ −35 dB, avança. Nunca por
  RMS sozinho (decepa), nem por piso sozinho (deixa ~1 s de respiração), nem por whisper sozinho (estoura).
- `FORCE_IN` / `FORCE_OFF` no `cuts.py` onde a respiração engana o piso.
- `mkchunks.py` **sem clamp** (`out` passa do `in` seguinte de propósito: é o lead do vídeo).
- `ctaSeg` é o encerramento real; "já me segue" no começo do roteiro não move o push-in para lá.
- Palavra engolida: colar a sílaba de outro take só sob cobertura (`se_splice.py`).

### J-cut (emenda ponta a ponta)
A fala seguinte começa antes de a imagem cortar. Para cada take, `cuts.py` mede `on`/`off` da fala e grava:
- **`in`** = `on − HH` (no 1º take, `on − HEAD_PAD`) — onde a **voz** começa
- **`aout`** = `off + TA` — onde a **voz** termina
- **`out`** = `aout + lead × rate` — onde o **vídeo** termina (último take: `out = aout = off + TAIL_PAD`)

A voz do take k vai de `in` a `aout`, a do k+1 entra em seguida, e a imagem do take k segura mais `lead`.
- Voz **nunca somada**: emenda ponta a ponta, crossfade de **3 quadros inteiro no silêncio** (5 comia até 76 ms).
- **O lead conta da 1ª palavra:** o clipe de voz começa `HH` = 0,15 s antes da fala (~4 quadros a 1,1x), por isso
  `jcutLeadFrames` **9** = 5 de fala + ~4 de respiração. Mudou a velocidade → refazer a conta.
- Na timeline: `sourceDur = (out − in)/rate` · `lead = min(9/30, sourceDur − 10 quadros)` · vídeo com
  `data-media-start = in + lead × rate` (lip-sync preservado).
- **Pausa curta** (< `TA + HH`): emenda dentro do silêncio real (45% tail / 55% cabeça); se o fade-in invadiria a
  palavra e o crossfade cabe na pausa: `in = on − XF − 5 ms`, `aout = in`.
- **Validar por dados, sempre:** `python3 scripts/jcut_check.py` → `buracos 0` · `crossfade sobre fala: nenhum` ·
  lead de fala mediano ~5 quadros (4,9–5,9) · respiro mediano ~0,245 s. "Crossfade sobre fala" se resolve no
  `cuts.py`, nunca aumentando o crossfade.
- **L-cut (`videoTail`)** só se o pré-rolo do próximo take já está falando; mudo > ~0,3 s lê como imagem
  congelada. Na prática não se usa: desvio de olhar se cobre.

### Bipe de censura
- **Varrer a transcrição INTEIRA atrás de palavrão** (inclusive takes descartados) e conferir ouvindo. Bipar
  também palavra com risco de bloqueio quando ele pedir.
- **Palavra inteira**, da 1ª consoante ao fim do decaimento. Tom de 1 kHz, fade de 6 ms, ~1 dB acima da frase
  (o `sine` do ffmpeg sai a −18 dBFS).
- Gravado dentro de `assets/<slug>-voz.m4a` e de `work/full.wav` (`bipe.py`, `JANELAS` em segundos do source). A
  transcrição sai de `work/full-clean.wav` (com bipe o whisper alucina).
- **Achar a janela:** o whisper erra ~0,4 s e o envelope sozinho confunde sílabas. Mapear com whisper em
  **recortes cumulativos do áudio limpo** + espectro (nasal /m/ = energia < 400 Hz; oclusão = vale).
- **Aceite por medição** na `voz-mix.m4a`: ~100% da energia em 950–1050 Hz e ~0% fora de 900–1100 Hz na janela.
  O "p***" do whisper **não** serve de juiz (ele escreve o palavrão até sobre silêncio).
- Imagem: de preferência apresentador em tela cheia (a boca sob o bipe lê como censura); se ele lê o roteiro
  ali, **a regra do olhar vence** e o bipe fica sob cobertura.

## 6. Varredura de olhar (obrigatória)

O apresentador tem que aparecer olhando para a câmera. Leitura de roteiro é medida e coberta; o que sobrar
exposto é **reportado em segundos**, nunca resolvido trocando o formato.

1. **Medir na timeline:** `gaze_tl.py` (FaceLandmarker, blendshapes, 30 amostras/s) → `gaze_windows.py`
   (`|side − mediana| > 0,17` ou `down − mediana > 0,11`, sem piscada, ≥ 0,15 s).
2. **Se ele gravou de perto e mexe a cabeça:** `gaze_pose.py 2.0` (regressão do olho contra yaw/pitch; o resíduo
   é o desvio real). Sem isso a maioria das janelas é falso positivo (Kazuo: 40 janelas/19,5 s → 19/5,4 s).
3. **Conferir nas folhas**, sempre (`gaze_sheet.py` → `gaze/me/g*.jpg`; `gaze_review.py`, `vw_eyes.py`). O medidor é
   pista, não veredito: piscada, pálpebra, sorriso e aceno passam do limiar. O recorte dos olhos é por bruto.
4. **Triar** nítidas × sutis. Desenhar o layout contra as **nítidas**; conferir as sutis em tamanho grande.
5. **Cobrir** com tela cheia. Desvio dentro de split não tem conserto por corte: vira cutaway ou fica. Pálpebra
   baixando 2 quadros antes: adiantar a janela.
6. **2ª passada com a cobertura real**, nos quadros da **composição** (bordas de cada aparição dele).
7. Registrar: janelas, segundos, **leitura exposta em segundos**.

Layout: `cenas_opt.py` (DP, cenas de 2,5–5 s) é ponto de partida; com muitas janelas ele engole os splits ou expõe
leitura dentro deles → **desenhar à mão** sobre as nítidas (`work/layout-exemplo.py` → `slots.py`).
`FIRST=('S',0.0)`; `ONLYP` no bipe e no fim do CTA; `ONLYB` na revelação e no clímax.

## 7. Ritmo e transições

- Cenas de 3–5 s; zoom do apresentador uma vez por aparição. Tomadas de 0,7–2 s em sequência foram reprovadas
  ("muitas brolls"); mais de ~4 s sem evento também. Auditar com `ritmo.py` (maior intervalo ~4–4,7 s).
- **Todo corte tem transição.** Com a camada de motion (padrão atual) a transição é feita **pelos elementos**
  (chicote, queda, zoom-through, card ↔ tela) e o light-leak fica só nas **trocas de seção** (virada, clímax,
  CTA) — ~3 por reel. No fluxo antigo de B-roll em vídeo era light-leak + whoosh em todo corte (17–20 por reel).
- O intro em split não precisa ocupar os ~10 s inteiros.

## 8. Fluxo de trabalho (kit v3 — padrão)

**Comando único, sem parada.** O MP4 pronto vai para o chat no fim (`SendUserFile`) junto com o caminho. Parada
só se o Fabio pedir ou houver decisão que só ele pode tomar (trecho sem imagem aceitável, mudança de corte que
não seja de olhar). De dentro de `~/Claude/reel-auto/<slug>`:

```bash
zsh ~/Claude/KIT-EDICAO-REEL/novo-projeto.sh <slug> "Título"   # cria o projeto do modelo + assets fixos
zsh scripts/fase1.sh "<bruto>" <slug>     # FUNDO ~5 min: mezanino + whisper turbo por região -> work/regioes.txt
#   em paralelo: pesquisa de fotos no navegador (fonte primária) + capa no Codex
#   escrever: scripts/mkcut.py (SPLIT/DROP) · scripts/cuts.py (TAKES) · scripts/bipe.py (JANELAS, se houver palavrão)
zsh scripts/fase2.sh                      # FUNDO ~5 min: cortes, J-cut, chunks, legendas, faixas, timeline, olhar
#   ler work/chunks.txt -> scripts/captions_fix_table.py -> zsh scripts/legendas.sh
#   ler gaze/me/g*.jpg -> janelas NÍTIDAS · ler work/tl-words.txt -> tempo de cada palavra
#   plano: sections (virada, CLIMAX, CTA), impacts (<=5; 1º typing), ctaSeg, splitShiftY (medir)
#   scripts/slots.py (S, cobrindo as nítidas; MG={"*"}) · compositions/mg.html (CENAS com a biblioteca)
zsh scripts/montar.sh 13.4,16.8,...       # ~1 min: slots + build + leaks + bed + SFX da camada + check + snapshots
#   LER os snapshots, corrigir, repetir
python3 scripts/size_sweep.py | head -3   # escolher o SIZE da parte
zsh scripts/render-par.sh <SIZE> renders/<Nome>-reel-final.mp4   # FUNDO ~13 min: partes em paralelo + finalizar.py
#   conferir quadros-chave no MP4, bipe, MD5 do bruto -> mandar o MP4 no chat
```

**O que continua obrigatório** (pular = retrabalho): varredura de olhar pelas folhas · `jcut_check.py` · bipe
medido · QC por snapshot de cada cena · um quadro de cada fase do render conferido · MD5 do bruto · nenhuma foto
de banco ou com marca d'água.

**Refazer depois de um ajuste:** mudou camada ou plano → `montar.sh <instantes>` → **apagar
`renders/chunks/chunk-NN.mp4` das partes afetadas** → `render-par.sh` → conferir um quadro de cada trecho mudado.
O `render-par.sh` **retoma** e pula o que existe: sem apagar, o MP4 sai igual ao anterior com QC OK. A parte k
cobre os quadros `[k·SIZE, (k+1)·SIZE)` a 60 fps.

**Custo de correção:** não muda o tempo (imagem, texto, cor, volume) → só as partes afetadas, ~5–10 min. Muda o
tempo (corte, velocidade, J-cut, ordem) → avisar que é render inteiro (~25–40 min no fluxo serial); guardar o
plano antigo em `work/vN/`, remapear os tempos com `remap_tl.py`, refazer chunks e legendas (os índices mudam).

**Fim do reel:** preencher o `EDICAO.md` do projeto; levar as "Lições para o kit" para `docs/05` e, se mexeu em
script, para `modelo-projeto/scripts/`; `git commit` no kit; cópia para o servidor.

### Fluxo antigo (kit v2, só a pedido): parada única
Mesma montagem, com B-roll em vídeo (`entrega.py` → `make_broll.py`), light-leak em todo corte e uma parada antes
dos B-rolls, com tudo que mexe no tempo travado e listado: duração · cortes · velocidade · J-cuts · palavrões e
bipe · olhar (leitura exposta em s) · primeira cena · imagem prevista por slot. Depois do "pode gerar as brolls"
vai direto até o MP4. **Em toda parada, rodada de correção e entrega: link do preview clicável no topo**
(`http://localhost:<porta>/#project/<slug>`; subir com `npx hyperframes preview --background` e conferir com
`curl`, porque o `--status` às vezes mente).

### Prompt de comando único (o que o Fabio envia)
```
Edita o reel do [TEMA] com o bruto [CAMINHO DO BRUTO] e este roteiro:
[ROTEIRO]

Segue o fluxo rápido do kit (~/Claude/KIT-EDICAO-REEL/docs/14-fluxo-rapido.md): formato do kit + camada de
motion graphics da skill showreel-interface, na dosagem do reel Deming v2: abertura só com fotos, no corpo foto
real como padrão e motion só onde conta a história. Comando único, sem parada: pesquisa as imagens na fonte
primária pelo navegador, gera a capa no Codex com esta cena: [CENA], monta, confere quadro a quadro e me manda o
MP4 aqui no chat.
```
Sem [CENA], o Claude escolhe (assunto na metade de cima; pessoa-tema de costas) e avisa no resumo. Vem junto sem
precisar escrever: último take, palavra inteira, bipe inteiro, J-cut medido, olhar coberto, marca só depois do
nome, capa laranja no quadro 0, trilha + SFX do formato, SFX do motion, QC, MD5.

## 9. A regra de ouro e o contrato

**Nunca editar `index.html` nem o `compositions/mg.html` gerado à mão.** Tudo sai de `assets/edit-plan.json` e dos
scripts POR VÍDEO: plano → `node scripts/build-edit.mjs` → `python3 scripts/bake.py <alvos>` → `npm run check`
(0 erros; aviso de track densa é normal). O Studio reescreve o `index.html` ao salvar; o build seguinte regenera.

| Campo do `edit-plan.json` | O que faz |
|---|---|
| `fps` / `rate` | 30 (timeline) / 1,1 |
| `jcutLeadFrames` / `jcutCrossfadeFrames` | 9 / 3 |
| `src` / `voiceSrc` | mezanino / voz dedicada `.m4a` (com bipe) |
| `segments[]` | `in`, `out`, `aout`, `label`, `chunk` (de `plan_segments.py`); `videoTail` opcional |
| `sections[]` | `afterSegment`, `name` — light-leak no corte; "CLIMAX" no nome dispara riser + impacto |
| `broll[]` | `mode` (`split`/`full`), `fromSeg`, `toSeg`, `span` [f0,f1], `file`; opcionais `preStart`, `objectPosition`. Escrito por `slots.py` |
| `impacts[]` | `phrase` (como na legenda, sem acento/pontuação), `seg`, `lines`, `hold`, `style` (`typing` no 1º), `top` (%) |
| `presenterZoom` | `scales`, `mode: scene`, `sceneMax`, `maxHold`, `origin` |
| `leakMinGap` | 3,5 |
| `hookSeg` | segmento da capa (0; `null` desliga) |
| `capLowSegs` | segmentos com legenda a 76% sobre tela cheia |
| `splitShiftY` | medido |
| `ctaSeg` | 1º segmento do encerramento |
| `trilhaVol`, `trilhaLoop` | 0,079; emenda se > 164 s (`at`, `back`, `xfade`) |
| `bakedAroll`, `bakedAudio`, `bakedBroll`, `bakedLeaks` | faixas pré-renderizadas — sempre `true` |
| `mg` | `{"src": "compositions/mg.html", "id": "mg"}` — camada de motion |
| `brollKenBurns` | `false` |

`build-edit.mjs` lê também `assets/chunks/meta.json` e `chNN-words.json` e termina com
`OK: N segs, Xs, N cenas de broll (N tomadas), N sfx, N legendas, N callouts, N leaks, J-cut 9f/3f.`

**Onde mexer em cada coisa**

| Quero mudar… | Arquivo |
|---|---|
| cortes / takes | `scripts/mkcut.py` (SPLIT/DROP) → `scripts/cuts.py` (TAKES, FORCE_IN/FORCE_OFF) → `plan_segments.py` |
| texto de legenda | `scripts/captions_fix_table.py` (FIX/DROP/FIXT por chunk e índice) → `zsh scripts/legendas.sh` |
| callouts | `impacts` no plano |
| janelas de cobertura | `scripts/slots.py` (lista `S`, tempos absolutos) |
| cenas de foto e motion | `compositions/mg.html` (bloco CENAS) ou o gerador `work/mg/gen.py` |
| legenda baixa | `capLowSegs` |
| enquadramento do split | `splitShiftY` |
| volumes | `trilhaVol` / seção SFX do `build-edit.mjs` → `bake.py bed` |
| bipe | `scripts/bipe.py` (`JANELAS`) → `bake.py voz` |
| respiro / lead | `TA`/`HH` em `cuts.py`; `jcutLeadFrames` |
| tempos | `python3 scripts/tl.py [--words]` |

## 10. Scripts: MOTOR × POR VÍDEO

- **MOTOR:** não muda de reel para reel. Correção vai no kit, com commit.
- **POR VÍDEO:** o código fica, os **dados** são do reel. Vêm com dados de outro reel como exemplo. **Reescrever
  antes de rodar.** São: `bipe.py` (`JANELAS`), `mkcut.py` (`SPLIT`, `DROP`), `cuts.py` (`TAKES`, `FORCE_*`),
  `captions_fix_table.py` (`FIX`, `FIXT`), `cenas_opt.py`, `slots.py` (`S`, `NOMES`, `MG`), `entrega.py` (`PK`),
  `make_broll.py` (`S`), `pesquisa_md.py`, `se_splice.py`, `norm_broll1.py`, `work/layout-exemplo.py` e as CENAS
  do `mg.html`.

| Fase | Scripts |
|---|---|
| Comandos de fase (v3) | `fase1.sh` · `fase2.sh` · `legendas.sh` · `montar.sh` · `render-par.sh` |
| Mezanino e transcrição | `mezanino.sh` · `regions.py` · `mkreg.py` · `whisper_regs.sh` · `regwords.py` |
| Cortes | `valleys.py` · `mkcut.py` · `cuts.py` · `plan_segments.py` · `bipe.py` · `se_splice.py` |
| Legendas | `mkchunks.py` · `chunks_from_regions.py` · `align.py` · `captions_fix_table.py` · `fix_captions.py` · `rebuild_chunk.py` · `whisper_chunks.sh` (2º passe, só no fluxo antigo) |
| Build e faixas | `build-edit.mjs` · `bake.py [aroll voz bed cenas brollfull leaks]` · `jcut_check.py` · `ritmo.py` · `tl.py` · `remap_tl.py` |
| Olhar e layout | `gaze_tl.py` · `gaze_windows.py` · `gaze_pose.py` · `gaze_sheet.py` · `gaze_review.py` · `vw_*.py` · `cenas_opt.py` · `slots.py` |
| Imagens | `work/pesq/*` (`wm.py`, `wmpick.py`, `crawl.py`, `dl.py`, `sheet.py`, `filt.py`, `s.sh`, `pick.sh`) · `gimg.mjs` · `fal_img.mjs` · `entrega.py` · `make_broll.py` · `pesquisa_md.py` |
| Camada de motion | `compositions/mg.html` · `mg_cues.mjs` · `mg_sfx.py` |
| Export | `size_sweep.py` · `render-chunks.mjs` · `render-par.sh` · `work/render-all.sh` · `finalizar.py` · `sync-check.mjs` |

## 11. Pipeline técnico — armadilhas já pagas

### Mezanino e cor
- **Mezanino antes de tudo**, na resolução e fps do bruto (1440×2560 @60), BT.709 limited. `mezanino.sh` decide
  pelo `ffprobe`.
- **Quase todo bruto é SDR full-range** (`yuvj420p` / `color_range=pc`), não HDR. Sem
  `scale=in_range=full:out_range=tv` a cor **lava**.
- HDR do iPhone (HLG / `arib-std-b67`, BT.2020 10 bits):
  `colorspace=iall=bt2020:itrc=bt2020-10:all=bt709:format=yuv420p:dither=fsb` (ramo pouco exercitado).
- **Conferir a cor por número:** média de luminância bruto × mezanino dentro de ~1–1,5/255 e desvio-padrão igual.
  Desvio caindo = lavou.
- **`-g 30 -keyint_min 30 -sc_threshold 0` em todo arquivo gerado**: sem GOP denso a captura trava.
- **O bruto nunca é alterado:** MD5 antes e depois.
- Voz sempre em `.m4a` dedicado (`<audio src="*.mp4">` não toca no Studio). Vídeo sempre `muted`.

### Transcrição
- **Nunca whisper no arquivo inteiro** (alucina em loop). `silencedetect -35dB / 0,35 s` → regiões → `whisper-cli`
  (`large-v3-turbo` no v3) `-l pt --max-context 0 -ml 1 -sow` **por região** → `work/region-words.json`.
- v3: os chunks de legenda saem do passe por região (`chunks_from_regions.py`), um chunk por take, sem 2º passe.
  O 2º passe por chunk vazava a palavra do take vizinho, alucinava ("Obrigado", "E aí") e colapsava palavras no
  mesmo timestamp.
- Ordem: chunks → `align.py` (reancora na energia real; ignora DROP; limita em `aout`) → `fix_captions.py`
  (idempotente, parte de `work/chunks-aligned/`). `legendas.sh` faz tudo do zero.
- Palavra fraca pode cair **entre regiões** do `silencedetect`: quando os passes discordam, conferir de ouvido
  com whisper em recortes.
- Conferir `ls work/reg/*.json | wc -l` contra o número de regiões; não engolir o stderr do loop.

### Composição leve (faixas pré-renderizadas)
- **Nunca passar de ~10 elementos de mídia; light-leak também conta.** Cada `<video>`/`<audio>` é um player: com
  57 a tela ficava preta **só no Chrome do Fabio**, enquanto o headless mostrava tudo certo. Snapshot OK não
  prova o preview.
- `bake.py` gera `aroll.mp4` (corte do apresentador), `voz-mix.m4a` (J-cut), `bed.m4a` (trilha + SFX),
  `_cenaNN.mp4`, `broll-full.mp4`, `leaks.mp4`. **Rodar depois de toda mudança** de corte, velocidade, SFX ou B-roll.
- Armadilhas do bake: `setpts=PTS/rate,fps=N` (com `-r` atrasa 2 quadros) · fronteiras por quadro acumulado ·
  `setsar=1` antes do `concat` · **dois fps** (`TLFPS` = 30 para a matemática, `FPS` = 60 para os quadros; com 60
  nos dois: 1,9 s de dessincronia) · conferir a linha `aroll.mp4 N quadros (timeline N)` · estado inicial
  escondido em **CSS**, não `tl.set` em 0.
- `aroll` em VideoToolbox + 3 takes em paralelo (`BAKE_X264=1` volta ao x264).
- Zoom do apresentador por `tl.set` num wrapper, nunca duplicando `<video>`.

### Export em partes
- Render direto trava ("Sequential screenshot capture stalled"). `render-chunks.mjs`: `--workers 1`,
  `--no-best-effort`, `--video-frame-format jpg`, `-q delivery`, `--browser-timeout 300`, **sempre `--sdr`**.
- **`--split 3` em todas as partes** (sessão nova do Chrome por pedaço): zero falha desde então.
- **Tamanho da parte por `size_sweep.py`**: só sobre os `<video>`, incluindo os pedaços do split; sobra mínima ≥
  ~15 quadros; ~300–460 quadros a 60 fps. Não reaproveitar de outro reel. **Não desligar o gate de cobertura.**
- `render-par.sh <SIZE> <saida> [P]`: P=3 no Mac de 16 GB; **P=1 no de 8 GB**. Cada parte com seu `TMPDIR` dentro
  do projeto. "Capture stalled" isolado: relançar sem mudar nada.
- A camada de motion é sub-composição: o `render-chunks.mjs` desloca a timeline dela por parte. Sem isso ela
  aparece no preview e some no MP4.
- `finalizar.py`: soma dos quadros = timeline · áudio com limiter (`level=disabled` obrigatório) · mux **sem
  `-shortest`**, com `-frames:v` · QC: quadros = timeline, A/V dentro de 2 quadros, pico ~−1 dB, 0 trechos pretos.
- Conferir à parte: bipe no MP4 (~98–99% em 1 kHz com a trilha por baixo) · quadros-chave iguais ao preview ·
  `sync-check.mjs` com lag mediano 0 ms · MD5 do bruto.

## 12. Camada de motion graphics (`compositions/mg.html`)

Padrão desde o reel Alan Mulally ("ficou perfeito"), na dosagem do Deming v2 (§3). O formato do kit fica
inteiro; muda o que cobre o apresentador: uma **sub-composição** com fotos reais como cards ou tela cheia,
conceitos como UI animada e transições feitas pelos próprios elementos.

**Antes de desenhar, três respostas por escrito** (skill `showreel-interface`):
1. **O chip:** o átomo de UI do próprio assunto, usado como título de capítulo (Mulally → pílula de status
   verde/amarelo/vermelho; Deming → chip "PASSO N").
2. **A prova:** fotos reais como cards + motion nos conceitos.
3. **A frase que o final inverte:** o fim volta à imagem da capa com o sentido trocado.

**Arquitetura**
- Plano: `"mg": {"src": "compositions/mg.html", "id": "mg"}` → o build monta `#mg-host` (track 8, `z-index: 30`:
  acima do apresentador e do B-roll em vídeo, abaixo dos leaks e das legendas).
- Sub-composição 1080×1920 transparente, **uma timeline do reel inteiro**, tempos absolutos (os de
  `work/tl-words.txt`). Cenas = `.scene` escondidas por CSS, ligadas por `tl.set autoAlpha`.
- **Splits também são da camada:** `.scene` com `style="height:845px"` + `splitIn(id, t0, true)` no quadro 0 e
  `splitIn/splitOut` nas janelas seguintes. `slots.py` com `MG={"*"}`.
- `sections` só nas trocas grandes (virada, CLIMAX, CTA).
- SFX automático: cada componente com som chama `cue()` → `mg_cues.mjs` extrai → `mg_sfx.py` sintetiza e mistura
  **depois** do `bake.py bed`.

**Biblioteca do modelo (não mexer; as CENAS vão no fim):** `sceneIn/sceneOut` (card → tela cheia; sai encolhendo
+ chicote para cima) · `splitIn/splitOut` · `whip` (chicote lateral) · `drop` (queda/subida) · `zoomIn` · `pop` ·
`flip` · `rise` · `words` (título palavra a palavra) · `slam` (carimbo) · `chip` ("+" → pílula → rolo trava no
capítulo) · `smear` (chip vira risco → corte) · `stagger` · `bars` · `digits` (rolo de dígitos seek-safe) ·
`rings` · `kenburns` · `drift` · `cue`.

**Leis de física do movimento:** antecipação lenta (6–8 q) → rajada curta (2–3 q) → assentamento longo (10–12 q,
`expo.out`) · motion blur só na rajada · continuidade de vetor (o novo entra na direção em que o velho saiu) · o
elemento vira a transição · deriva ≤ 3% só nas seguras · o soco pousa na batida. Nada de crossfade entre cenas.

**Armadilhas pagas**
- `fromTo` aplica o estado "de" na montagem: usar `immediateRender: false`; e pôr `autoAlpha: 1` também no
  "para" (se o render pula para depois do tween, o elemento some).
- Quem sai "caindo" vai longe (y ≥ 1900), senão espia na borda.
- Pílula ou `.tag` com texto longo quebra em 2 linhas: alargar; `.tag` com `white-space: nowrap`.
- Só lógica determinística: sem `Date.now()`, `Math.random()`, `onUpdate`, fetch. Aleatório = semente fixa.
- Cena com peças repetidas (100 pontos, 112 bolinhas): escrever a camada por **gerador Python**
  (`work/mg/gen.py` lê o modelo, injeta CSS/markup/CENAS e grava `compositions/mg.html`). Editar o gerador.
- Conferir por snapshot em vários instantes de cada cena **e** um quadro de uma parte renderizada antes do
  render inteiro.

## 13. Pesquisa de imagem

- **Ir à fonte, pelo navegador, não a um buscador por API** (API trouxe 3 fotos de banco/marca d'água em 22).
  Ordem: sala de imprensa / site oficial / RI → Wikimedia Commons, NARA, Library of Congress (domínio público ou
  CC) → busca de imagens em tamanho grande (último recurso, passando por `filt.py`).
- Site inteiro: `npx hyperframes capture "<url>" -o ./capture --json`. Maior resolução: listar
  `img.currentSrc`/`srcset` na página; baixar com `curl -sSL -A "Mozilla/5.0"`; medir com `sips`.
- **Todo número e fato do vídeo sai de uma página aberta**, com a URL registrada.
- Prova no formato do conteúdo: screenshot real da manchete vale mais que foto genérica.
- Logos: SVG oficial; só corte, fade, deslocamento e escala uniforme.
- Critérios: lado menor ≥ ~900 px; sem marca d'água; cabe no 9:16 ou na faixa 16:9 do split; variedade.
- **Trecho conceitual sem imagem real não vira foto genérica: vira motion.**
- Fonte atrás de Cloudflare ("Um momento…"): **não contornar**; cair para site institucional + Commons (API do
  Commons com pausa de ~4 s entre buscas; sem pausa dá HTTP 429).
- **Capa a pedido no Codex:** `codex exec -m gpt-5.6-sol --skip-git-repo-check --sandbox workspace-write "<cena>"`
  (~70 s, 1536×1024). Alternativa: `fal_img.mjs` com `fal-ai/nano-banana-pro`, 4:3 (o flux errou mãos). Não usar
  `dry_run` no fal (enfileira job de verdade).
- **Se delegar a um subagente**, escrever no prompt: User-Agent genérico de Chrome e **nunca** e-mail, nome ou
  dado do usuário em headers, URLs ou payloads · no máximo ~3 consultas por trecho · entregar `candidates.json` e
  `picks.json` antes de ampliar. Se travar, não retomar: fechar à mão pelas folhas do `g_index.json`.
- Saída no fluxo antigo: `PESQUISAS-BROLL-<TEMA>.md` por slot (fala, enquadramento, imagem, link e fonte, prompt
  de animação só de câmera, duração, arquivo).

## 14. A máquina e o ambiente

- **Uma tarefa pesada por vez.** Whisper junto com encode derruba o `opendirectoryd` no Mac de 8 GB.
  **Canário:** `sudo -n true` respondendo "you do not exist in the passwd database" → parar tudo e pedir relogin.
- **Render e whisper como tarefa de fundo do harness** (`run_in_background`). `nohup … &` morre com
  `render_cancelled_parent_exited`.
- Disco: ≥ 6–7 GB livres antes do render. Parar o preview **deste** projeto antes do render; preview de outro
  projeto, pedir ao Fabio.
- zsh: glob em pasta vazia aborta a lista `&&` → usar `find … -delete`.
- O ffmpeg local **não tem `zscale` nem `drawtext`**. `make_broll.py` a 1,5x da saída (a 2x leva SIGKILL).
- Chaves (`SERPER_API_KEY`, `FAL_KEY`) em `~/Claude/reel-auto/.env`: nunca no kit, git, servidor ou chat. O fluxo
  padrão não precisa delas.
- Finais, brutos e projetos antigos ficam no servidor (`/Volumes/Company/Equipe/FABIO KENJI/`: `VIDEOS FINAL
  BACKUP/`, `VIDEOS BRUTOS BACKUP/`, `VIDEOS PROJETOS BACKUP/`, com `_MD5.txt`). Mover conferindo MD5; **apagar o
  local é com o Fabio**.
- Outro computador: copiar a pasta do kit e rodar `zsh instalar.sh` (termina com `0 falha(s)`).

## 15. O que NÃO fazer

Whisper no arquivo inteiro · tail por RMS · crossfade de 5 quadros · duas vozes somadas no J-cut · copiar
`splitShiftY` · L-cut com pré-rolo mudo · abrir em tela cheia · marca antes do nome · esticar vídeo do Fabio · IA
sem ele pedir · foto de banco ou com marca d'água · motion na abertura · UI em mais de ~40% da cobertura · batida
contínua sob a fala · palavrão audível, mesmo em parte · `-shortest` no mux · `alimiter` sem `level=disabled` ·
desligar o gate de cobertura · `nohup &` no render · whisper junto com encode · editar `index.html` à mão ·
re-renderizar sem apagar as partes afetadas · confiar só no snapshot para o preview · confiar no "p***" do
whisper · dado do usuário em requisição · consultar projeto antigo para saber "como se faz".

## 16. Resumo de entrega

Arquivo e caminho · duração · resolução · fps · validação (`check`, QC do `finalizar.py`) · áudio · imagem usada
em cada trecho (com fonte e licença; o que foi gerado a pedido) · callouts · takes descartados · onde o áudio
diverge do roteiro · bipe (janela e medição) · J-cut (emendas, lead, respiro) · **leitura exposta em segundos** ·
decisões tomadas sem perguntar.
