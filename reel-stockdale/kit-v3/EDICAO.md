# EDICAO.md — mapa do projeto (reel James Stockdale)

Kit v3 (fluxo rápido, docs/14) + camada de motion (showreel-interface), na dosagem do Deming v2.
Palco 1440x2560 (geometria 1080x1920 por `#stage`), timeline 30 fps, saída **1440x2560 @ 60 fps**, **1,1x**.
Editado numa sessão do Claude Code **na nuvem** (Linux, 4 núcleos, sem GPU), com o kit remontado a partir dos .md enviados.
**Estado (2026-10-04): RENDERIZANDO** (`renders/James-Stockdale-reel-final.mp4`), comando único sem parada.
Duração **91,091 s** · 29 takes · 1 bipe · 99 legendas · 4 callouts · 4 light-leaks (fim do split, virada, clímax, CTA) ·
10 SFX fixos + 56 SFX da camada · 14 slots (2 splits + 12 cenas de tela cheia na camada de motion).

> Regra de ouro: nunca editar `index.html` nem `compositions/mg.html` à mão. A camada sai de `work/mg/gen.py`
> (`python3 work/mg/gen.py`), depois `zsh scripts/montar.sh`.

## Bruto
`~/Claude/videos-brutos/stockdale-bruto.mov` (link iCloud `092Y0PdhgC7ZX35N_Ot9p8zFQ`, gravado no iPad) — **não alterado**.
MD5 `837ae5f0c064234fca6379af4c27538a` (antes e depois). HEVC 1440x2560 @60, 139,3 s, **SDR full-range** (`yuvj420p`/`pc`) →
mezanino full→limited. Cor bruto × mezanino (13,9/69,7/125,4 s): 150,93/151,00 · 152,19/152,33 · 153,32/153,42; desvio igual — não lavou.

## Sem roteiro escrito
O bruto veio sem roteiro: as legendas seguem o áudio, com a grafia do formato ("Jim", "cinco", "sete e meio").

## Takes descartados (mantido o ÚLTIMO)
r01 fim "pra provar que na crise do dono" → r02 · r07 "Ele aprendeu com um filósofo grego" + r08 "que você…" → r09 ·
r13 "Segundo, encara o fato…" → r14 · r15 "Faz quanto tempo que você não abre…" → r16 · r18 fim "e terceiro nunca perda" → r19+r20 ·
r20 fim "Ele diz que nunca duvidou…" → r21 · r23 "E na virada…" → r24 · r25 fim "o que" (falso início) → r26 ·
r27 "O Natal a gente chegava e passava." → r28. CTA r31 = um take.

## Bipe
"porra" ("xingando a porra dos juros"): oclusão /p/ 51,62–51,73 · explosão 51,74 · "orra" até 52,04 · decaimento até 52,06 ·
/d/ de "dos" em 52,06. Whisper em recortes cumulativos: até 51,76 "…xingando a"; até 51,90 "…a porra". Bipe **51,72–52,07** do source.
Medido na voz: **99,6% em 950–1050 Hz, 0,05% fora de 900–1100**. Legenda `P****`. Apresentador em tela cheia no bipe (37,52 s).

## J-cut
28 emendas · 0 buracos · nenhum crossfade sobre fala · lead de FALA 4,9–5,1 quadros · respiro mediano 0,245 s (min 0,236).

## Olhar
`gaze_pose.py 2.0`: 12 janelas / 3,0 s; folhas `gaze/me/g00–g02` (30 janelas do medidor bruto). Nítidas (todas cobertas por
tela cheia): 37,9–38,5 · 63,7–64,7 · 77,0–77,5 · 81,6–82,0 · 86,3–86,8. Sutil exposta: 2,9–3,4 (olhar levemente para baixo,
dentro do split da capa). **Leitura exposta: ~0,5 s** (a sutil do gancho).

## Split
`splitShiftY` **363** (olhos y≈1014 no aroll em 11 pontos das janelas de split → 1377−1014). Splits: capa 0–10,74 · virada 64,82–70,78.

## Marca só depois do nome
"Jim" em 10,67 s → revelação em 10,74. Snapshot: 10,70 sem o Stockdale (apresentador + leak), 10,77 com o retrato.
Capa = Hanoi Hilton visto do alto (sem o Stockdale), depois cela e muro de Hoa Lò.

## Camada de motion (work/mg/gen.py)
Chip = "PASSO N" (pílula verde/amarela/vermelha). Prova = fotos de arquivo como card/tela cheia. Frase que o final inverte:
a árvore de Natal da virada volta em "Mês que vem é o seu Natal."
Motion só em: contador 5 → 7,5 anos · PASSO 1/2/3 · depende × não depende · extrato · calendário do clímax (≈38% da cobertura).
Callouts: 1º digitado "O DONO OTIMISTA / É O PRIMEIRO / A QUEBRAR." (seg 2) · "É MEDO." (16) · "OS OTIMISTAS." (22, `top` 40 para
não cobrir os olhos do retrato) · "MÊS QUE VEM / É O SEU NATAL." (27).

## Imagens (LICENCAS-FOTOS.txt)
Todas de arquivo (Wikimedia Commons: Marinha dos EUA/NARA/DoD em domínio público; Hoa Lò e ovos em CC BY 2.0). Nenhuma de banco.

## Ambiente (container Linux, não o Mac)
Adaptadores sem mexer no motor: `~/Claude/mac-compat/bin` (`md5`, `sed -i ''`), `/opt/homebrew/bin/ffmpeg` → `/usr/bin/ffmpeg`,
fontes do macOS em `/System/Library/Fonts` → DejaVu, `/System/Volumes/Data` (checagem de disco do render-par), `BAKE_X264=1`
(sem VideoToolbox), CA do proxy no NSS do Chrome (sem isso o GSAP não carrega e o `check` acusa `gsap is not defined`),
`libegl1`/`libgles2` para o mediapipe, `scipy` no venv (o `sfx.py` da skill importa). whisper.cpp compilado + `ggml-large-v3-turbo`.

## Lições para o kit
- `mg_sfx.py` → `sfx.py` da skill importa **scipy**: falta na lista de dependências do docs/10 e do `instalar.sh`.
- Conferir a seção "Runtime" do `check`: `gsap is not defined` = o navegador não carregou o CDN e a camada não anima.
