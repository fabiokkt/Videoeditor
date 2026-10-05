# Calibrações travadas e armadilhas já pagas

Destilado dos 31 reels editados até 2026-10-01 (Casas Bahia → … → Kazuo Inamori): os 27 `EDICAO.md` dos
projetos e as notas de memória. **É a fonte única**: nada aqui precisa ser reconferido num projeto antigo.
Entre parênteses, o reel em que a regra nasceu — só para dar contexto; o texto do projeto está em
`arquivo-projetos/<slug>/`.

**Não recalcular, não re-perguntar, não "melhorar" sem o Fabio pedir.** Pedido explícito dele vence qualquer
número daqui — e vira regra nova (seção 22).

---

## 1. Números do formato

| Parâmetro | Valor | Observação |
|---|---|---|
| Palco | `#root` 1440×2560 com `#stage` 1080×1920 em `scale(4/3)` | toda medida (fonte, caixa, `splitShiftY`) continua na geometria 1080×1920 |
| Timeline / saída | timeline a **30 fps** · export **1440×2560 @ 60 fps** | `bake.py` tem dois fps (seção 17) |
| Velocidade | **1,1x** (`rate`) | "acelere 1.1" sobre o que já está a 1,1 → **1,21**; "só um pouquinho" → **1,15** |
| Duração | o roteiro manda (hoje ~90–100 s; os primeiros eram 50–60 s) | nunca cortar roteiro por conta própria |
| J-cut | `jcutLeadFrames` **9** · `jcutCrossfadeFrames` **3** | 9 = 5 quadros de FALA + ~4 de respiração (seção 7) |
| Folgas do corte | `HEAD_PAD` 0,20 · `TAIL_PAD` 0,13 · `TA` 0,12 · `HH` 0,15 | respiro mediano ~0,245 s entre falas |
| Split-screen | B-roll **44%** em cima / apresentador **56%** embaixo | transição de arrastar 0,55 s `power3.inOut` |
| `splitShiftY` | **medir em todo bruto** (já deu de 260 a 550) | olhos a ~49% da faixa do apresentador (seção 12) |
| Zoom do apresentador | `presenterZoom` 1,06 / 1,14 · `mode: scene` · `sceneMax` 4,5 · `origin` 50% 53% | uma troca por aparição |
| Ritmo | cenas de **3–5 s**; ~4 s é alvo **e** teto | `leakMinGap` **3,5** |
| Legenda | Montserrat **600 / 47 px**, branca, **sem contorno**, halo de 3 sombras | até 3 palavras, quebra em pontuação |
| Legenda — posição | **44%** sobre B-roll e dentro do split · **76%** com o apresentador sozinho | `capLowSegs` só vale sobre B-roll de tela cheia |
| Gancho = capa | frase inteira desde o quadro 0 · caixa **#FF4A1C** · **Oswald 700, caixa alta, 90 px** | seção 13 |
| Callout | Montserrat **800 / 76 px CAPS**, contorno 10 px, a **30%** (ou `top`) | ~5 por reel de 90 s; o 1º com digitação |
| Light-leak | 0,7 s, começa **10 quadros antes** do corte, `screen`, opacidade 0,85 | ~17–20 por reel de 90 s |
| CTA | push-in 1 → 1,05 a partir de `ctaSeg` | |
| Trilha | 0,079 → 0,045 (últimos ~9 s) → 0 (fade 0,7 s) | `trilhaLoop` se o reel passar de 164 s |
| Áudio final | `amix(voz-mix, bed)` + limiter a −1 dBTP · AAC 256 kb/s 48 kHz | `finalizar.py` |
| CLI | `hyperframes@0.8.64` fixo no `package.json` | o `render-chunks.mjs` chama `0.8.48` no render; é a combinação validada — não atualizar no meio de um reel |

### SFX (volumes exatos, todos no `bed.m4a`)
- intro `opening` **0,25** + `riser` **0,22**, de 0 a 3,2 s
- `boom-cinematic` em 4,8 s, **0,12**
- `drum-fill` em 7,0 s, **0,166** — suprimido quando o callout de digitação cai entre 5,5 e 9,5 s (dois drum-fills embolam)
- `drum-fill` do callout de digitação, **0,3**
- `whoosh` → `swoosh` → `whoosh-transition` alternados, **0,18**, um por light-leak
- `riser` **0,2** 3 s antes do clímax · `impact-hit` **0,3** na entrada do clímax (a seção cujo `name` contém "CLIMAX")

**Regra de ouro do mix:** nunca SFX rítmico contínuo (ticks, loop de batida) sobre fala densa — o Fabio reportou
como "áudio quebrado". One-shot curto nos cortes: sim. Cama rítmica sobre a voz: não.

---

## 2. Fluxo e comunicação com o Fabio

- **Parada única**, antes dos B-rolls. Nela tudo que mexe no tempo tem que estar travado e listado: duração,
  cortes, velocidade, J-cuts, palavrões bipados, varredura de olhar, primeira cena, B-rolls planejados por slot.
  Depois do "pode gerar as brolls" vai direto até o MP4 final, sem nova revisão. Só parar de novo se surgir
  decisão que só ele pode tomar (slot sem imagem aceitável, mudança de corte que não seja de olhar).
  *Por quê:* a 2ª parada só gerava pedido visual ou correção de tempo que devia ter saído na 1ª (Andy Grove,
  Reed Hastings, Herb Kelleher); cortar a 2ª economiza 15–25 min por vídeo.
- **Link do preview em toda parada**, em toda rodada de correção e na entrega do render:
  `http://localhost:<porta>/#project/<slug>`, clicável, no topo da mensagem. Subir com
  `npx hyperframes preview --background` e conferir com `curl` (o `--status` às vezes mente). *("onde está o
  link para eu ver o vídeo até aqui? Toda vez você esquece" — iPhone Duo.)*
- **O texto do prompt antigo está desatualizado em dois pontos** — aplicar o padrão atual e registrar no resumo,
  sem perguntar: "legendas amarelas dentro de uma caixa no gancho" = capa laranja; "J-cut de 5 frames" = 5
  quadros de fala com crossfade de 3. O prompt de `docs/04` já está corrigido.
- **Correção depois do render:** não muda o tempo (B-roll, texto, cor, volume) → refazer só as partes afetadas
  (~5–10 min). Muda o tempo (corte, velocidade, J-cut, ordem) → avisar que é render inteiro (~25–40 min) e fazer.
- Reportar sempre os segundos de leitura de roteiro que ficaram expostos, em vez de trocar o formato para zerar.
- Resumo de entrega: arquivo, duração, resolução, fps, validação, áudio, B-roll por slot, callouts, decisões.

---

## 3. A máquina: MacBook Air 8 GB / 228 GB

- **Serializar tudo que é pesado.** Whisper junto com encode do mezanino derrubou o `opendirectoryd`
  (Jocko Willink): `whoami` devolve `501`, o whisper morre no Metal, o Chrome morre no sandbox. Não há conserto
  por shell — só sessão nova (sair e entrar na conta basta). **Canário:** `sudo -n true` respondendo
  "you do not exist in the passwd database" → parar tudo e pedir relogin.
- Não engolir o stderr do loop de whisper: conferir `ls work/reg/*.json | wc -l` contra o número de regiões.
- **Disco:** ≥ 7 GB livres antes do render é o confortável. O render enche o cache de extração (~2,9 GB).
  `work/render-all.sh` põe o `TMPDIR` dentro do projeto e limpa a cada parte — rodou com ~2 GB livres.
  Apagar cache compartilhado do `$TMPDIR` do sistema foi negado pelo classificador de permissões: não tentar.
- **Render em segundo plano = tarefa de fundo do harness.** `nohup … &` dentro de uma chamada de shell morre com
  `render_cancelled_parent_exited`.
- **Parar o preview deste projeto antes do render** (RAM). Parar preview de *outro* projeto foi negado pelo
  classificador ("Interfere With Workloads"): pedir ao Fabio; com o "pode parar" dele passa.
- Glob no zsh numa pasta vazia aborta a lista `&&` inteira: usar `find … -delete`, não `rm -f pasta/*.mp4`.
- `make_broll.py` trabalha a 1,5x da saída: a 2x com foto de 4000 px o ffmpeg leva SIGKILL.
- O ffmpeg local **não tem `zscale` nem `drawtext`**.
- **Armazenamento:** finais e brutos ficam no servidor (`/Volumes/Company/Equipe/FABIO KENJI/`: `VIDEOS FINAL
  BACKUP/` com `_MD5.txt`, `VIDEOS BRUTOS BACKUP/`). Não estranhar a falta deles no Mac. Mover sempre conferindo
  MD5 antes de apagar o local. O share `Company` precisa estar montado.
- Chaves de API (`SERPER_API_KEY`, `FAL_KEY`) em `~/Claude/reel-auto/.env` — **nunca** vai para o kit, git ou servidor.

---

## 4. Mezanino e cor

- **Mezanino antes de tudo**, na resolução e fps do bruto (hoje 1440×2560 @60), BT.709 limited, `-g 30`.
  `scripts/mezanino.sh` decide o caso pelo `ffprobe`.
- **Quase todo bruto é SDR full-range** (`yuvj420p` / `color_range=pc`), não HDR. Sem converter
  full→limited (`scale=in_range=full:out_range=tv`) a cor **lava** — reclamação real.
- Quando for HDR do iPhone (HLG / `arib-std-b67`, BT.2020 10 bits):
  `colorspace=iall=bt2020:itrc=bt2020-10:all=bt709:format=yuv420p:dither=fsb`.
- **Conferir a cor por número**, bruto × mezanino em 3–4 pontos: média de luminância bate em ~1–1,5/255 e o
  desvio-padrão fica igual. Desvio caindo = lavou.
- **`-g 30 -keyint_min 30 -sc_threshold 0` em TODO arquivo gerado** (mezanino, `aroll`, cenas, B-rolls): sem GOP
  denso o render avisa `sparse keyframes … causes seek failures and frame freezing` e a captura trava (Costco).
- Bruto **nunca** alterado: MD5 antes e depois, registrado no `EDICAO.md`.
- Voz sempre em `.m4a` dedicado: `<audio src="*.mp4">` de vídeo não toca no Studio.

---

## 5. Transcrição

- **Nunca whisper no arquivo inteiro** (alucina em loop). `silencedetect -35dB / 0,35 s` → regiões →
  `whisper-cli large-v3 -l pt --max-context 0 -ml 1 -sow` **por região** → `work/region-words.json`.
- O passe por região serve para escolher takes, achar palavrão e ancorar o tail na última palavra.
- Depois dos cortes: **1 chunk por take** (± 0,3 s) → whisper por chunk, do **áudio limpo** (`full-clean.wav`).
- **O passe por chunk falha nas bordas**: vaza a palavra do take vizinho, alucina ("Obrigado", "E aí",
  "Sensacional!") e às vezes **colapsa** várias palavras no mesmo timestamp (`to <= from`). Conserto:
  `rebuild_chunk.py ch:regiao` reconstrói o chunk a partir do passe por região. Nos reels recentes quase todos
  os chunks foram reconstruídos (Sun Tzu 14, Kazuo 40 de 41). Guardar o passe cru em `work/chunks-raw/`.
- Depois de reconstruir, **rever os DROP daquele chunk**: o chunk vindo da região não tem a palavra vazada e o
  DROP antigo passa a comer palavra boa (IKEA).
- Ordem fixa: whisper → `align.py` → `fix_captions.py`. O `align.py` ignora as palavras DROP e limita o encaixe
  em `aout` (a voz do take): sem isso jogava "Terra." do gancho para fora da voz (Taiichi Ohno).
- `fix_captions.py` é idempotente (parte sempre de `work/chunks-aligned/`). Para refazer do zero depois de novo
  `align.py`: apagar `work/chunks-aligned/chNN-words.json`.
- Palavra fraca pode cair **entre regiões** do `silencedetect` ("perdi **tudo**", Mike Michalowicz): quando os
  passes discordam, conferir de ouvido com whisper em recortes.

### Texto da legenda
- Erro de **grafia/pontuação/maiúscula** do whisper → vale o roteiro ("pra", "pro", "tá", números por extenso
  como no roteiro, nomes como no roteiro: "Jocko", "Herb", "Taiichi").
- Onde o **áudio diz outra coisa** (passe por região, por chunk e com o roteiro no `--prompt` concordam) → vale
  o áudio. Registrar no `EDICAO.md` o que divergiu do roteiro.
- Legenda da palavra bipada: `M****`, `P****` (palavra inteira bipada) — entra junto com o bipe (`FIXT`).

---

## 6. Cortes e takes

- **Frase ou take repetido: fica sempre o ÚLTIMO válido.** Falso início sai inteiro. Varrer a transcrição
  toda, inclusive o que parece ruído.
- "porque você… é demais" com pausa dramática é **um take só**, não repetição.
- Regiões descartadas continuam em `regions_cut.json`: o `cuts.py` usa as vizinhas para achar o silêncio real.
- **Dividir fala longa nos vales reais** (`valleys.py`, −38 dB, ≥ 0,16 s) dá ritmo de corte e janelas de B-roll.
  Não dividir quando o silêncio real é < ~120 ms (o crossfade cairia sobre a palavra — Costco).
- **Head:** onset por RMS (20 ms, −27 dB, 4 de 8 janelas), recuando até o piso, − `HEAD_PAD`.
- **Tail:** `min(fim da última palavra, offset RMS a −45 dB)` + trava: enquanto o nível ≥ −35 dB, avança.
  Nunca por RMS sozinho (decepa "loja", "pessoas") nem por piso sozinho (deixa ~1 s de respiração — IKEA) nem
  por whisper sozinho (estoura além do áudio).
- **Pausa curta** entre dois takes: emenda no silêncio real; se o crossfade de 3 f cabe na pausa, a emenda vai
  logo antes da fala nova (`in = on − XF − 5 ms`, `aout = in`) — "piloto | foi grosso", Herb Kelleher.
- `FORCE_IN` / `FORCE_OFF` no `cuts.py` para a borda em que a respiração seguinte fica acima do piso.
- **Sem clamp no `mkchunks.py`**: com `out = aout + lead`, em takes contíguos o clamp comia o lead e cortava
  14–75 ms da palavra final (Reed Hastings).
- O **gancho** tem que ser a primeira frase inteira: juntar regiões se preciso e, se o take trouxer a 2ª frase,
  dividir no vale para a capa ter só a 1ª.
- `ctaSeg` é o encerramento real: quando o "já me segue" vem no começo do roteiro, o push-in vai para a pergunta final.
- Recuperar palavra engolida colando a sílaba de outro take só sob B-roll (sem lip-sync a respeitar) —
  `se_splice.py` (David Marquet) é o molde.
- Depois de mudar corte ou velocidade com B-rolls já posicionados: remapear os tempos pelo mesmo quadro do
  bruto (`remap_tl.py`, plano antigo em `work/v1/`) e refazer chunks + `fix_captions.py` (os índices mudam).

---

## 7. J-cut

- **Voz emendada ponta a ponta**, nunca duas vozes somadas: a voz do take termina em `aout` (fim da fala +
  0,12) e a do seguinte começa em `in` (início da fala − 0,15), com crossfade de **3 quadros dentro do
  silêncio**. O **vídeo** segura o lead depois do `aout` (`out = aout + lead × rate`). *("as J-cuts não ficaram
  tão boas" — Atul Gawande.)*
- **O lead conta da PRIMEIRA PALAVRA**, não do início do clipe: o clipe de voz começa 0,15 s de source antes da
  fala; com `jcutLeadFrames` 5 a palavra entrava só 0,9 quadro antes do corte — J-cut invisível. Por isso **9**
  (= 5 + `HH`/rate em quadros). *("foque um pouco mais no j-cut" — Reed Hastings.)*
- Crossfade de 5 quadros não cabe no silêncio e come até 76 ms da palavra final: **3** (André Esteves).
- **Sempre validar por dados** antes de fechar: `python3 scripts/jcut_check.py` → 0 buracos, nenhum crossfade
  sobre fala, lead de fala ~5 quadros, respiro mediano ~0,245 s.
- **L-cut (`videoTail`)**: só quando o pré-rolo do próximo take já está **falando**. Pré-rolo mudo > ~0,3 s lê
  como imagem congelada (Localiza). Quando o roteiro é lido de uma tacada (takes contíguos no source) o L-cut é
  **estruturalmente inútil** — recuar o início mostra os mesmos quadros do desvio. Na prática: todo desvio de
  olhar se resolve com cobertura de B-roll.

---

## 8. Legendas na tela

- Branca **sem contorno**: some sobre fundo claro. Escurecer o B-roll (`dim` no `make_broll.py`, 0,08–0,35;
  negativo clareia) em vez de mexer na legenda.
- `capLowSegs` decidido **olhando snapshot por snapshot**: legenda a 44% em cima de rosto, logotipo, título de
  livro, mostrador → desce para 76%. Só vale sobre B-roll de **tela cheia**; dentro do split fica sempre na
  divisa (a 76% cai na boca do apresentador — Herb Kelleher).
- Legenda que cruza o corte para um B-roll: conferir os dois lados.

---

## 9. Bipe de censura

- **Varrer a transcrição INTEIRA atrás de palavrão antes da parada** (inclusive takes descartados) e conferir
  ouvindo. *("a palavra PORRA deu para escutar" — Reed Hastings.)* Bipar também palavra com risco de bloqueio
  no Instagram quando ele pedir ("mortes" — Atul Gawande).
- **Padrão atual: a palavra INTEIRA**, da 1ª consoante ao fim do decaimento. (Os primeiros eram "MER—" + bipe;
  o Fabio passou a pedir a palavra toda: "ainda dá para escutar".)
- **Onde:** gravado dentro de `assets/<slug>-voz.m4a` (`bipe.py`), 1 kHz, fade de 6 ms, ~1 dB acima da frase.
  O filtro `sine` do ffmpeg sai a −18 dBFS, não a 0. `work/full.wav` leva o bipe (senão o tail do take o deixa
  de fora); a transcrição sai de `work/full-clean.wav` (com o bipe o whisper alucina).
- **Achar a janela:** o whisper erra ~0,4 s dentro da região e o envelope sozinho não diz qual sílaba é qual
  (o vale que parecia o /d/ era o /p/ — Mike Michalowicz). Mapear as sílabas com **whisper em recortes
  cumulativos do áudio limpo** e pelo espectro (nasal /m/ = energia < 400 Hz; oclusão = vale).
- **Aceite por medição na `voz-mix.m4a`:** ~100% da energia em 950–1050 Hz e ~0% fora de 900–1100 Hz na janela.
  O "p***" do whisper **não** serve de juiz para palavrão previsível: com a palavra trocada por silêncio puro
  ele ainda escreve "uma merda" (Sun Tzu). Rodar o controle do silêncio antes de confiar nele.
- **Imagem:** de preferência o apresentador em tela cheia (a boca sob o bipe lê como censura). Mas se ele lê o
  roteiro naquele trecho, **a regra do olhar vence** e o bipe fica sob B-roll.

---

## 10. Varredura de olhar

**O apresentador lê o roteiro olhando para o lado ou para baixo** no começo e no fim de quase todo take, e às
vezes no meio. No vídeo final ele tem que aparecer olhando para a câmera. Fase obrigatória, feita **duas
vezes**: com os B-rolls em placeholder e de novo com os B-rolls reais.

1. **Medir na timeline:** `gaze_tl.py` (FaceLandmarker, blendshapes, 30 amostras/s) → `gaze_windows.py`
   (`|side − mediana| > 0,17` ou `down − mediana > 0,11`, sem piscada, ≥ 0,15 s).
2. **Se ele gravou de perto e mexe a cabeça:** os blendshapes medem o olho *dentro da cabeça*, e quem olha para a
   lente compensa o giro com o olho — a maioria das janelas vira falso positivo. Usar `gaze_pose.py` (regressão
   contra yaw/pitch; o resíduo é o desvio real; 2σ). Kazuo: 40 janelas / 19,5 s → 19 / 5,4 s.
3. **Conferir nas folhas**, sempre: `gaze_review.py`, `vw_tl.py`, `vw_eyes.py`, `vw_big.py`. O medidor é pista,
   não veredito — piscada, pálpebra baixando, sorriso e aceno passam do limiar. **O recorte dos olhos tem que
   ser medido por bruto** (o enquadramento muda).
4. **Triar** em nítidas / de fronteira de take × sutis. Desenhar o layout contra as **nítidas**; conferir as
   sutis expostas em tamanho grande.
5. **Cobrir** com B-roll de tela cheia. Desvio dentro de janela de split não tem conserto por corte: vira
   cutaway ou fica. Pálpebra já baixando 2 quadros antes: adiantar a janela do B-roll.
6. **2ª passada com os B-rolls reais**, nos quadros da **composição** (snapshots das bordas de cada aparição do
   apresentador), não só no mezanino.
7. Registrar e reportar: janelas, segundos, **leitura exposta em segundos**.

Histórico dos medidores (ainda no modelo, úteis em casos específicos): `gaze_measure.py` + `gaze_report.py`
(íris, só desvio lateral: `gx ≤ −0,055` = leitura; `gx` positivo com yaw subindo = cabeça virada, olho na
lente) · `gaze_bounds.py` / `gaze_pairs.py` (fronteiras de take) · `gaze_down.py` / `gaze_lids.py` /
`gaze_blend.py` (olhar para baixo).

---

## 11. Layout de cenas e ritmo

- **"A cada 4 segundos no máximo precisa de um efeito ou B-roll"** (André Esteves) — e depois: **"ficaram muitas
  brolls… o intervalo está muito curto"** com tomadas de 0,7–2 s (Dan Martell). Resultado: cenas de **3–5 s**,
  zoom do apresentador **uma vez por aparição**, `leakMinGap` 3,5. Auditar com `ritmo.py` (maior intervalo sem
  evento ~4–4,7 s).
- **Todo corte precisa de transição**: light-leak + whoosh em corte de seção, entrada e saída de cena **e nos
  cortes internos** de cena concatenada. *("só uma broll sem transição, sem nada".)*
- Duas tomadas parecidas (mesma foto reenquadrada, dois interiores iguais) contam como "parado": alternar
  assunto, escala e luminosidade.
- **A primeira cena é sempre split** (capa: B-roll em cima, ele embaixo, caixa laranja), mesmo com olhada no
  gancho: split curto de capa → cutaway de tela cheia cobrindo a olhada → split volta com a transição de
  arrastar. Reportar os décimos expostos dentro da capa. *("a primeira cena precisa ser a tela dividida como em
  todos os outros vídeos" — Reed Hastings.)*
- Estrutura do formato: intro em split (pré-revelação) → revelação → cutaways do corpo → **2º split na virada**
  → clímax emocional → CTA no apresentador.
- O intro split **não precisa** ocupar os ~10 s inteiros. CTA "já me segue" dentro da intro vai com o
  apresentador em tela cheia, sem B-roll — escolha do Fabio (IKEA).
- **`cenas_opt.py`** (DP que minimiza leitura exposta com cenas de 2,5–5 s) é ponto de partida. Com muitas
  janelas ele engole os splits (`WBS` baixo) ou expõe leitura dentro deles (`WBS` alto): nesse caso **desenhar
  o layout à mão** sobre as nítidas (`work/layout-exemplo.py` → `slots.py`). `FIRST=('S',0.0)`; `ONLYP` no bipe
  e no fim do CTA; `ONLYB` na revelação e no clímax.

---

## 12. Split-screen

- `splitShiftY` **se mede, não se copia** — já deu 260, 312, 352, 362, 365, 375, 390, 400, 410, 412, 422, 424,
  432, 435, 436, 438, 439, 442, 470, 535, 550. Com o valor errado os olhos caíam a 29% da faixa (Costco).
- Medir a altura dos olhos no `aroll`/mezanino (FaceMesh: média do `y` dos landmarks 33/133/362/263) em vários
  pontos **dentro das janelas de split**; aplicar o zoom
  (`y_zoom = origem + (y_olhos − origem) × escala`); alvo: olhos a **~49% da faixa do apresentador** (a faixa vai
  de 845 a 1920 → y ≈ 1377 na geometria 1080×1920); `splitShiftY = 1377 − y_zoom`.
- Para medir sem B-roll: `slots.py --placeholders`, build, snapshot. Conferir no snapshot antes de fechar.
- No split o cover-crop mostra só 44% da altura: assunto fora da faixa → `objectPosition`, ou gerar o split da
  foto 4:3 inteira.

---

## 13. Gancho = capa

- O **quadro 0 é a capa do reel**: frase inteira do gancho já na tela, sem animação de entrada. Conferir sempre
  o snapshot em t=0.
- Caixa laranja **#FF4A1C** (gradiente, borda branca, glow), **Oswald 700 em caixa alta, 90 px**, caixa de
  1016 px (margem ~32 px), contorno 12 px + sombra dura, pulso **1,018** (a 1,035 a caixa larga vaza da tela),
  brilho atravessando duas vezes. Sem `text-wrap: balance`.
- A caixa cobre ~35–56% da altura: o assunto do B-roll de capa tem que ficar **acima** dela (gerar o split da
  imagem 4:3 inteira; recompor a foto se a caixa tapar o assunto).
- Para voltar à caixa amarela antiga: `"hookSeg": null` + `"yellowCapSegs": [0]`.

---

## 14. Marca só depois do áudio

- **Nada que identifique a empresa/pessoa antes de o áudio dizer o nome pela 1ª vez** — logo, letreiro, rosto,
  livro, produto. Quando o tema é uma pessoa, o gatilho é o nome dela, e a empresa dela entra junto.
  *("não coloque nenhuma imagem… antes do áudio falar o nome da empresa pela primeira vez" — Localiza2.)*
- Achar o instante pela palavra (`tl.py --words`). A revelação entra **2 quadros depois** do início da palavra:
  no quadro exato a emenda arredonda e a marca vaza 1 quadro antes.
- Pré-revelação: material real do tema **sem marca** (recorte abaixo do totem, interior, detalhe) ou cena
  genérica do assunto. Concessionária/loja genérica não serve se traz logo de outra marca.
- Conferir com snapshots da faixa pré-revelação + fronteira; registrar último quadro limpo e primeiro com marca.

---

## 15. Callouts

- 1º callout: **digitação** (caracteres um a um em ≤ 1,35 s) + drum-fill + pulso de settle. Demais: `popIn`
  `back.out(2.4)`, rotação −5°, grow 1,07, saída 0,22 s. Sempre `tl.set autoAlpha 0` no fim (linter de seek).
- `impacts[].seg` prende o callout ao segmento (sem isso dispara em toda repetição da frase).
- `impacts[].top` quando o B-roll tem rosto/assunto na faixa dos 30%. Callout branco some em fundo branco:
  trocar a imagem. Callout que cobre os olhos de um retrato: tirar o callout.
- Callout estourando com o apresentador em tela cheia leva punch-in 1,07.

---

## 16. B-roll

### Pesquisa (detalhe em `docs/11`)
- Fotos **reais** do tema, que casem com a fala do trecho. Prioridade: sala de imprensa / site oficial →
  Wikimedia Commons → Google Imagens em tamanho grande. Lado menor ≥ ~900 px. Banco de imagens fica de fora.
- **Nunca IA generativa por conta própria.** Imagem encenada só quando o Fabio **descreve** a cena: `fal_img.mjs`,
  `fal-ai/nano-banana-pro`, 4:3, mostrar na parada, marcar "gerada a pedido" no PESQUISAS-BROLL.
- **Subagente de pesquisa:** proibir no prompt e-mail/nome do usuário em User-Agent, headers, URLs ou payloads
  (usar UA genérico de Chrome); limitar a ~3 consultas por trecho e exigir os JSON antes de ampliar. Se travar
  ("stalled"), não retomar: fechar à mão pelas folhas do `g_index.json`.
- Licenças: registrar a fonte de cada foto. CC BY-NC e "direitos reservados" são pendência para o Fabio decidir.

### Geração (`entrega.py` → `make_broll.py`)
- **Só a câmera se move** sobre a foto: texto, logotipo e marca ficam idênticos ao original.
- Tela cheia 1440×2560, split 1440×1128, 60 fps, cada arquivo = janela + 0,1 s (`rate` 1,0 — `< 1` reprova no
  gate de cobertura; câmera lenta se grava no arquivo).
- Foto pequena ou assunto largo demais: `fill` 1 (foto inteira sobre fundo borrado) ou 2 (fundo liso, para foto
  de estúdio); não ampliar mais que ~1,4x. Pré-recorte lateral para a foto ocupar mais tela.
- Letreiro/capa que ocupa a largura: **pull-out** terminando com o texto inteiro, ou estático. Zoom-in decepa.
- Normalizar rotação EXIF antes (o `ffprobe` não aplica, o `ffmpeg` aplica — o recorte sai deitado).
- Vídeo entregue pelo Fabio (`broll1.mp4`): **velocidade normal, mudo**, só normalizado (`norm_broll1.py`).
  Esticar foi reprovado (0,63x — IKEA). Os cortes internos dele dão o ritmo.
- QC com folha início/meio/fim de cada tomada.

---

## 17. Composição leve (faixas pré-renderizadas)

- **Nunca passar de ~10 elementos de mídia; light-leak também conta.** Cada `<video>`/`<audio>` é um player e
  uma sessão de decodificação: com 164 (André Esteves) e depois com 57 (Dan Martell) o B-roll sumia e a tela
  ficava preta **só no Chrome do Fabio**. O headless mostra tudo certo — snapshot OK **não prova** o preview.
- `bake.py` gera: `aroll.mp4` (corte do apresentador), `voz-mix.m4a` (J-cut), `bed.m4a` (trilha + SFX),
  `_cenaNN.mp4` (tomadas seguidas), `broll-full.mp4` (todas as cenas de tela cheia), `leaks.mp4`.
  Flags no plano: `bakedAroll`, `bakedAudio`, `bakedBroll`, `bakedLeaks`.
- **Rodar `bake.py` depois de toda mudança** de corte, velocidade, SFX ou B-roll (só B-roll:
  `bake.py cenas brollfull leaks bed`).
- Armadilhas do bake: `setpts=PTS/rate,fps=N` (com `-r` o conteúdo atrasa 2 quadros dentro do take) · fronteiras
  por **quadro acumulado** · `setsar=1` antes do `concat` · **dois fps**: `TLFPS` = `plan.fps` (30) para a
  matemática da timeline, `FPS` = 60 para os quadros do arquivo (com 60 nos dois: 1,9 s de dessincronia) ·
  conferir a linha `aroll.mp4 N quadros (timeline N)` · estado inicial escondido em **CSS**, não `tl.set` em 0 ·
  conteúdo de cada cena de `floor(t0·60)` a `ceil(t1·60)`.
- Zoom do apresentador por `tl.set` num wrapper, nunca duplicando `<video>`.
- Testar **tocando** no Studio, não só com seek. Servidor serial (`python3 -m http.server`) dá falso positivo.

---

## 18. Export em partes (detalhe em `docs/12`)

- Render direto trava ("Sequential screenshot capture stalled") e com vários workers o Mac reinicia.
  `render-chunks.mjs`: 1 worker, `--no-best-effort`, `--video-frame-format jpg`, **sempre `--sdr`**.
- **Tamanho da parte por varredura** (`size_sweep.py`): só sobre os `<video>`, incluindo os pedaços do
  `--split`; sobra mínima ≥ ~15 quadros. **Não desligar o gate de cobertura.**
- **Todas as partes em `--split 3`** (sessão nova do Chrome por pedaço): zero falha desde o Reed Hastings.
  O limite de quadros por sessão não é fixo (travou em 530, 572, 318).
- `--fps 60` e o mesmo `--size` em tudo. A soma dos quadros das partes tem que ser a timeline.
- Áudio: `amix(normalize=0)` + `alimiter=limit=0.891:level=disabled`. Mux **sem `-shortest`**, com `-frames:v`.
- QC: 0 trechos pretos, pico ~−1 dB, quadros = timeline, bipe presente, quadros-chave iguais ao preview,
  sincronia boca/voz com lag mediano 0 ms (`sync-check.mjs`), MD5 do bruto igual.

---

## 19. Preview

- `npx hyperframes preview --background`; conferir com `curl`; as portas mudam (3002, 3003, 3005…); matar
  zumbi com `lsof` só deste projeto.
- O Studio reescreve o `index.html` ao salvar (`data-hf-id`, `<br>`): normal, o build seguinte regenera.

---

## 20. Regra de ouro do trabalho

**Nunca editar o `index.html` à mão.** Tudo sai de `assets/edit-plan.json` (e dos scripts POR VÍDEO) por
`build-edit.mjs` + `bake.py`. Mudou algo: plano → build → bake → `npm run check` (0 erros; avisos de track
densa são normais).

---

## 21. O que NÃO fazer (lista curta)

Whisper no arquivo inteiro · tail por RMS · crossfade de 5 quadros · duas vozes somadas no J-cut · copiar
`splitShiftY` · L-cut com pré-rolo mudo · abrir em tela cheia · marca antes do nome · esticar vídeo do Fabio ·
IA sem ele pedir · `-shortest` no mux · `alimiter` sem `level=disabled` · desligar o gate de cobertura ·
`nohup &` no render · whisper junto com encode · editar `index.html` à mão · parar sem o link do preview ·
confiar só no snapshot para o preview · confiar no "p***" do whisper · e-mail do Fabio em requisição.

---

## 22. Como este documento cresce

Todo reel termina com a seção "Lições para o kit" do `EDICAO.md` do projeto. Cada item entra **aqui** (regra +
porquê + reel) e, se mexeu em script, em `modelo-projeto/scripts/` — com `git commit` no kit. É isso que
dispensa abrir projeto antigo.

---

## 23. Padrão novo: camada de motion graphics (reel Alan Mulally, 2026-10-02 — "ficou perfeito")

- **O que cobre o apresentador é motion, não foto genérica.** Trecho conceitual (processo, número, gráfico) vira
  UI animada na sub-composição `compositions/mg.html`; foto real entra como card. Light-leak só nas trocas de seção.
  Detalhe, componentes e armadilhas: `docs/13-camada-motion.md`. *(pedido: "mesmo formato, mas com transições,
  imagens e motion graphics melhores, mais dinâmico com a mesma essência".)*
- **Trilha e SFX fixos do formato continuam todos**; os SFX do motion entram por cima (`mg_sfx.py`, depois do
  `bake.py bed`), impactos ≤ −16 dB para a voz ficar na frente. *(pedido explícito do Fabio/usuário.)*
- **Pesquisa de imagem pelo navegador na fonte primária** (sala de imprensa, site, Instagram, Wikipedia,
  `hyperframes capture`), não por API de busca — docs/11. Busca por API trouxe 3 fotos de banco/marca d'água em 22.
- **`render-chunks.mjs` precisa deslocar a timeline das sub-composições** por parte (corrigido no modelo): sem isso
  a camada aparece no preview e some no MP4.
- Capa: a caixa do gancho cobre 35–56% da tela até o fim do gancho também sobre o B-roll de tela cheia que entra
  antes dele terminar (s02 do Alan Mulally) — recompor a foto com o assunto abaixo da caixa.
- Imagem a pedido também pode sair do **Codex**: `codex exec -m gpt-5.6-sol --skip-git-repo-check --sandbox
  workspace-write "<prompt>"` (~70 s, paisagem 1536×1024). O modelo padrão do config pode ser recusado no login
  ChatGPT: passar `-m`.
- Máquina com 16 GB: o render serial em partes continua correto, só conservador; medir antes de afrouxar.
- Entrega: mandar o MP4 no próprio chat (`SendUserFile`), além do caminho.
- **Mundo claro da camada precisa de "chão" escuro** abaixo de ~64% da tela: legenda branca a 76% sobre cena clara reprova no
  contraste do `check` e some no vídeo. Já está no `.light` do modelo (reel Deming).
- **`.tag` sem quebra de linha** (`white-space: nowrap`, no modelo): tag longa quebrava em 2 linhas e cobria o vizinho (reel Deming).
- **Fonte primária atrás de Cloudflare** (deming.org, loc.gov) mostra "Um momento…" no navegador do app: não contornar. Cair para o site
  institucional (ex.: JUSE para o Prêmio Deming) + Wikimedia Commons (API com pausa de ~4 s entre buscas; sem pausa dá HTTP 429).
- **`render-par.sh` retoma**: pula toda `renders/chunks/chunk-NN.mp4` que já existe. Depois de mudar a camada/plano, **apagar as partes
  afetadas antes** (ou todas). No Deming v2 ele reaproveitou as 14 partes da v1 ("partes em 0s") e o MP4 saiu igual à v1 com QC OK —
  só um quadro conferido revelou. Parte k cobre `[k·SIZE, (k+1)·SIZE)` quadros a 60 fps.

## 24. Dosagem: imagem primeiro, motion só onde conta a história (reel Deming v2, 2026-10-02)

Pedido do usuário depois da v1 do Deming (camada com UI em quase todo trecho): *"diminuir um pouco os motion graphics e colocar mais
imagens; os primeiros segundos e o início, o ideal é manter como era, só com imagens, e depois pode animar"*. Virou regra:

- **Abertura (split da capa + pré-revelação) = só fotos.** Capa → fotos reais/de arquivo com Ken Burns e corte por chicote/queda.
  Nada de etiqueta, crachá, carimbo ou UI por cima. O callout de digitação do formato continua.
- **No corpo, foto real é o padrão.** Trecho que *dá* para mostrar com foto (pessoa, lugar, objeto, situação: "três vendedores",
  "ranking de funcionário", "almoço", "linha de montagem") vai de **foto de arquivo** (NARA / Library of Congress / Commons, domínio
  público ou CC) em tela cheia, no máximo uma etiqueta.
- **Motion só onde ele carrega a história:** título de capítulo (chip PASSO N + título), número que precisa ser visto (94 de 100,
  1 em cada 5), o mecanismo do clímax (a caixa, a pá, o placar), o objeto que a fala nomeia e não existe em foto (o cartaz com a
  frase exata). Regra prática: **≤ ~40% do tempo de cobertura em UI animada**; o resto é foto ou apresentador.
- Gráfico que só repete a fala ("não diminuía") → apresentador em tela cheia (respira o ritmo).

## 25. Capa que viraliza + edição numa sessão na nuvem (reel James Stockdale, 2026-10-04)

- **Capa = a pessoa-tema de costas ou em silhueta, numa cena dramática do assunto**, com luz e cor fortes: o padrão das capas
  que viralizaram (Jocko: SEAL em silhueta na visão noturna · Dan Martell: empresário de costas numa cela · David Marquet:
  capitão em silhueta no periscópio, luz vermelha). Prédio, foto aérea ou objeto não serve: a 1ª capa do Stockdale (Hanoi
  Hilton visto do alto) foi reprovada ("precisa ser mais parecida com o vídeo do Jocko, Dan e David… isso influenciou na
  viralização"). Quando a cena não existe em foto real, **gerar** (Codex) e marcar "gerada a pedido".
- **Sessão do Claude Code na nuvem** (container Linux, sem o Mac): o Codex entra pela conta ChatGPT do Fabio com
  `codex login --device-auth` → ele abre `https://auth.openai.com/codex/device` e digita o código. Pré-requisito: ativar
  **"device code sign-in"** em ChatGPT → Settings → Security and login. Sem custo extra (plano do ChatGPT). `codex logout` no fim.
  Gerador público gratuito (pollinations) foi testado e reprovado: 886x665, marca d'água, ignora o prompt.
- **`sfx.py` da skill showreel-interface importa `scipy`** (o `mg_sfx.py` falha sem ele): incluir no venv.
- **Conferir a seção "Runtime" do `check`**: `gsap is not defined` = o Chrome não carregou o GSAP do CDN e a camada de motion
  não anima (no container foi o certificado do proxy fora do NSS do Chrome).
- Adaptadores que o container Linux precisou (sem mexer no motor): `md5`→`md5sum`, `sed -i ''`, `/opt/homebrew/bin/ffmpeg`,
  fontes em `/System/Library/Fonts`, `/System/Volumes/Data` (checagem de disco do `render-par.sh`), `BAKE_X264=1`,
  `libegl1`/`libgles2` para o mediapipe, whisper.cpp compilado. Render: 12 partes, 2 em paralelo, 23 min em 4 núcleos.

## 26. Comando único na nuvem sem esperar a capa (reel Mike Abrashoff, 2026-10-04)

- **O código do `codex login --device-auth` expira em 15 min** e o usuário pode demorar a digitar. Não travar a edição esperando:
  rodar o login num laço (`cxlogin.sh`: até 6 códigos seguidos, sai quando `codex login status` não diz "Not logged") como tarefa de
  fundo, avisar cada código novo no chat e seguir. A capa entra num **placeholder** (`assets/mg/capa-<slug>.jpg` = uma foto da
  pré-revelação); quando o Codex gera a capa: `gen.py` → `montar.sh` → apagar só `renders/chunks/chunk-00.mp4` e o MP4 →
  `render-par.sh` (retoma: refez só a parte 0 em 3 min). `codex logout` logo depois de gerar.
- **`pkill -f "codex login"` dentro de um comando que também contém "codex login" mata o próprio shell** (exit 144). Matar por PID
  ou rodar o laço a partir de um arquivo de script.
- **Sem retrato livre da pessoa-tema** (Abrashoff: zero no Commons, sem Wikipedia): a revelação é o objeto-símbolo real (o navio,
  USS Benfold) + a etiqueta de nome. Não usar foto de palestra com direitos reservados.
- Take refeito que **tropeça na frase-chave** ("ninguém mais quer **parar de** trabalhar") não é o "último válido": fica o take
  anterior limpo, mesmo sem uma palavra do roteiro ("E o protocolo…" sem "esse é"). Conferir com whisper em recorte antes de decidir.
- **`fix_captions.py` não quebra mais com a tabela do modelo** (a do Kazuo, índices de outro reel): avisa e segue. Mesmo assim,
  reescrever `captions_fix_table.py` antes da fase 2.
- **`montar.sh`**: `mg_sfx.py | head -1` dava `BrokenPipeError` no print final (o bed já estava gravado); trocado por `sed -n 1p`.
- **Render no container de 4 núcleos**: 13 partes de 447 quadros, 2 em paralelo, **24 min** (≈ 4 min por par). Entregas pedidas pelo
  usuário a partir do master (260–285 MB): cópia para o chat em x264 dois passes ~2 Mbps (< 30 MB) e versão final HEVC
  (`libx265` dois passes, `-tag:v hvc1`, AAC 256k, `+faststart`) a 8 Mbps — **acima de ~95 s, baixar o vídeo para caber em
  < 100 MB** (96,7 s → 7,5 Mbps).
