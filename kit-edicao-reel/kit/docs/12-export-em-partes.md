# Export em partes (MacBook Air 8 GB)

O render direto do HyperFrames trava nesta máquina ("Sequential screenshot capture stalled") e, com vários
workers, o Mac chega a reiniciar. O caminho que fecha — 1440×2560 @ 60 fps, ~90–100 s, em ~15–25 min:

```bash
python3 scripts/size_sweep.py                     # 1. tamanho da parte
npx hyperframes preview --stop                    # 2. libera RAM (só o preview deste projeto)
zsh work/render-all.sh <SIZE>                     # 3. partes — COMO TAREFA DE FUNDO DO HARNESS
python3 scripts/finalizar.py renders/<Nome>-reel-final.mp4    # 4. áudio + mux + QC
```

## 1. Tamanho da parte

O render tem um **gate de cobertura**: se uma parte fica com 2–3 quadros de um clipe, ele aborta ("captured 2
of expected 3 frames"). Está certo — evita clipe em branco. **Não desligar**; escolher o tamanho.

`size_sweep.py` mede, para cada tamanho, a menor sobra de `<video>` dentro de qualquer pedaço e lista os
melhores. O que já foi pago:

- varrer **só os `<video>`** — contando as legendas nenhum tamanho passa (falso alarme);
- incluir os **pedaços do `--split`** — 354 era bom sem split e deixava 8 quadros com `--split 3`;
- sobra mínima ≥ ~15 quadros; varrer de 1 em 1 (os números redondos costumam ser piores);
- a 60 fps ficar em ~300–460 por parte.

Tamanhos usados: 320 (IKEA, Chris Voss, Rolex) · 351 (Jocko, Dan Martell) · 354 (Atul, Andy Grove) · 360 (Jeff
Bezos, Munger) · 348 (Marquet) · 441 (Reed) · 449 (Herb) · 390 (Taiichi) · 342 (Vince) · 372 (Mike, Sun Tzu) ·
432 (Kazuo). Não reaproveitar: depende do layout de cada reel.

## 2–3. As partes

`work/render-all.sh` roda uma parte por vez com `--split 3`: cada parte vira 3 pedaços, cada pedaço numa
**sessão nova do Chrome**, unidos sem recodificar. É isso que acabou com as travas — o limite de quadros por
sessão não é fixo (já travou em 318, 530 e 572, sempre no mesmo quadro, enquanto o snapshot naquele instante
funcionava: não era o quadro, era a sessão).

- **Tarefa de fundo do harness**, não `nohup … &` (morre com `render_cancelled_parent_exited`).
- `TMPDIR` dentro do projeto (`renders/tmp/`), limpo a cada parte: o cache de extração e o perfil do Chrome não
  enchem o disco do sistema. Para com menos de 600 MB livres.
- Retoma de onde parou (parte que existe é pulada). Quando uma parte falha, o script apaga o `chunk-KK.mp4`
  dela: uma parte errada deixada no disco seria pulada na rodada seguinte (no Andy Grove isso custou 3 quadros
  de sincronia). O `finalizar.py` também recusa o mux se a soma dos quadros não for a da timeline.
- ~1–1,5 min por parte. "Capture stalled" isolado: relançar sem mudar nada.
- `RENDER_EXTRA="--no-browser-gpu"` passa flags extras ao render (último recurso; não resolveu no Munger).
- Flags fixas do `render-chunks.mjs`: `--sdr` (o pipeline HDR precisa de ~20 GB e falha), `-q delivery`,
  `--workers 1`, `--video-frame-format jpg`, `--no-best-effort`, `--browser-timeout 300`.

## 4. Fechamento

`finalizar.py`:

1. confere que a soma dos quadros das partes é a timeline (a última pode vir com +1);
2. áudio = `amix(voz-mix, bed, normalize=0)` + `alimiter=limit=0.891:level=disabled` — o `level=disabled` é
   obrigatório (com o auto-level o limiter normaliza de volta para 0 dB);
3. mux direto da lista de partes + `_audio.m4a`, vídeo copiado, **sem `-shortest`** (ele decepa o último
   quadro), com `-frames:v`;
4. QC: quadros = timeline · A/V dentro de 2 quadros · pico ~−1 dB · 0 trechos pretos.

Com as faixas pré-renderizadas o áudio entra com offset zero por construção. (O truque antigo — render com
`--debug`, caçar o `audio.m4a` em `~/.npm/_npx/<hash>/` e medir `-itsoffset` — acabou no reel André Esteves.)

Conferir à parte:

- **Bipe no MP4:** energia em 1 kHz na janela (a trilha por baixo deixa ~98–99%).
- **Quadros-chave** iguais ao preview (capa, revelação, split, callouts, clímax, CTA): diferença de poucos /255.
- **Sincronia boca/voz:** `node scripts/sync-check.mjs final16k.wav bruto16k.wav` → lag mediano 0 ms. Takes de
  ~1 s dão medida ruim (a janela atravessa a emenda) — artefato da medição.
- **MD5 do bruto** igual ao do começo.

## Correção sem mudar o tempo

Corrigir → `build-edit.mjs` → `bake.py` dos alvos → apagar só as partes que cobrem o trecho →
`zsh work/render-all.sh <mesmo SIZE>` → `finalizar.py`. Por isso as partes ficam guardadas em
`renders/chunks/` até o Fabio dar o reel por encerrado. (Mike Michalowicz: troca da capa = 1 parte re-renderizada.)

## Depois

O final vai para o servidor (`/Volumes/Company/Equipe/FABIO KENJI/VIDEOS FINAL BACKUP/`, com linha no
`_MD5.txt`); as partes de `renders/chunks/` podem ser apagadas quando não houver mais correção a fazer.
