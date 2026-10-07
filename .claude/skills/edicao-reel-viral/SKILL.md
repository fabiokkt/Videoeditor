---
name: edicao-reel-viral
description: Edita um vídeo bruto de talking-head no formato de reel viral do usuário (9:16 1440x2560 @60, 1,1x, capa laranja no quadro 0, split-screen, J-cut, bipe, legendas Montserrat, trilha e SFX fixos, fotos reais + camada de motion graphics da skill showreel-interface, HyperFrames). USE SEMPRE que o usuário mandar um bruto com roteiro para editar, disser "edita no meu formato", "faz o reel do X", mandar o prompt de comando único do kit, ou pedir correção/render de um reel em ~/Claude/reel-auto.
---


> **Neste repositório (sessão na nuvem):** o kit está em `kit-edicao-reel/kit/` (docs, `modelo-projeto/`, `exemplos/`, `skill/`), remontado a partir de `kit-edicao-reel/0..5-*.md`. Comece por `kit-edicao-reel/1-MANUAL-DO-FORMATO.md`. Os binários de `assets-fixos/` (trilha, SFX, light-leak, fontes, `face_landmarker.task`) não vêm nos .md: já estão em `kit-edicao-reel/kit/assets-fixos/`. O ambiente
> (ferramentas, venv, whisper, HyperFrames, Codex, adaptadores do macOS) sai do script `kit-edicao-reel/ambiente-nuvem.sh`,
> colado no "Script de configuração" do ambiente; se a sessão começar sem ele, rodar `bash kit-edicao-reel/ambiente-nuvem.sh`.
> Imagem a pedido (capa): `codex login --device-auth` (o Fabio digita o código) e `codex logout` no fim.

# Edição de reel viral — porta de entrada do kit

**O conhecimento está no kit, fonte única do formato:** `~/Claude/KIT-EDICAO-REEL/`. Esta skill só aponta para ele.

## Antes de qualquer ação, ler
1. `docs/14-fluxo-rapido.md` — **o fluxo padrão (kit v3)**: comando único, sem parada, do bruto ao MP4 no chat
2. `docs/05-calibracoes-e-armadilhas.md` — todo número travado e todo erro já pago (§23 camada de motion, **§24 dosagem**)
3. `docs/13-camada-motion.md` — a camada de motion; exemplos em `exemplos/deming/` (o mais recente) e `exemplos/alan-mulally/`
4. `docs/10-scripts.md` — quais scripts são MOTOR e quais são POR VÍDEO (estes vêm com dados de outro reel: reescrever)

## Fluxo (resumo de docs/14)
```
zsh ~/Claude/KIT-EDICAO-REEL/novo-projeto.sh <slug> "Título"      # cria ~/Claude/reel-auto/<slug>
zsh scripts/fase1.sh "<bruto>" <slug>     # FUNDO: mezanino + whisper por região -> work/regioes.txt
   (enquanto roda: pesquisa de fotos na fonte primária + capa no Codex)
   escrever scripts/mkcut.py (SPLIT/DROP) · scripts/cuts.py (TAKES) · scripts/bipe.py (JANELAS)
zsh scripts/fase2.sh                      # FUNDO: cortes, J-cut, chunks, legendas, faixas, olhar
   scripts/captions_fix_table.py -> zsh scripts/legendas.sh · ler gaze/me/g*.jpg · work/tl-words.txt
   plano: sections, impacts (<=5, 1º typing), ctaSeg, splitShiftY (MEDIR: work/olhos_y.py) · scripts/slots.py · camada mg
zsh scripts/montar.sh t1,t2,...           # build + bake + SFX + check + snapshots -> LER as imagens
zsh scripts/render-par.sh <SIZE> renders/<Nome>-reel-final.mp4   # FUNDO, SIZE de size_sweep.py
   conferir quadros do MP4 + bipe + MD5 do bruto -> SendUserFile
bash work/entregas.sh <Nome>             # FUNDO: copia do chat < 30 MB + HEVC final < 100 MB + comparacao (kit v3.1)
```

## Preferências do usuário (não re-perguntar)
- Comando único sem parada; o MP4 vai no chat no fim.
- **Abertura só com fotos; motion só no meio, onde carrega a história; foto real é o padrão** (docs/05 §24).
- O apresentador lê o roteiro olhando para o lado: varredura de olhar é obrigatória; leitura exposta reportada em segundos.
- Último take válido; palavra inteira; palavrão bipado inteiro e medido; nada da marca antes de o áudio dizer o nome.
- IA generativa só para a capa (Codex) ou quando ele descrever a cena.

## Regras
- Nunca editar `index.html` nem `compositions/mg.html` gerado à mão: plano / gerador -> build.
- Uma tarefa pesada por vez; render e whisper como tarefa de fundo do harness.
- Depois de ajuste: apagar as partes afetadas em `renders/chunks/` antes do `render-par.sh` (ele retoma).
- Fim do reel: lições novas para `docs/05` / `modelo-projeto/` + `git commit` no kit.

As skills do HyperFrames (`/hyperframes*`) cobrem a ferramenta; o kit cobre o formato. Onde divergirem, vale o kit.
