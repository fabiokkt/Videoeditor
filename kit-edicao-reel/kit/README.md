# KIT DE EDIÇÃO — Reel Viral (HyperFrames) · v3.1

> **Outro computador? Leia `COMECE-AQUI.md` e rode `zsh instalar.sh`.**

**A fonte única do formato.** Tudo que foi aprendido em 31 reels — números, armadilhas, scripts, prompts — está
aqui. Um reel novo nasce deste kit e não consulta nenhum projeto antigo; por isso os projetos antigos podem
sair do Mac.

Formato: 9:16, 1440×2560 @ 60 fps, 1,1x, ~90–100 s. Motor: HyperFrames. Máquina: MacBook Air 8 GB.

---

## Começar um reel

```bash
zsh ~/Claude/KIT-EDICAO-REEL/novo-projeto.sh <slug> "Título"
```
Cria `~/Claude/reel-auto/<slug>` com scripts, template, fontes, SFX, trilha, light-leak e modelo de olhar.
Depois é seguir `docs/06-checklist-execucao.md`. O prompt que o Fabio envia está em `docs/04`.

## O que tem dentro

| Pasta | Conteúdo |
|---|---|
| **`docs/`** | O conhecimento. `05` é o mais importante |
| **`modelo-projeto/`** | O esqueleto de um projeto: 53 scripts, `index.html` (template), plano-esqueleto, `EDICAO.md` modelo, ferramentas de pesquisa e de render |
| **`novo-projeto.sh`** | Cria o projeto a partir do modelo + assets fixos |
| **`assets-fixos/`** | Trilha, 9 SFX, light-leak, fontes (Montserrat 600/800, Oswald 700), modelo FaceLandmarker |
| **`exemplos/kazuo-inamori/`** | O reel mais recente como referência: plano, `index.html`, `EDICAO.md`, pesquisa, chunks |
| **`arquivo-projetos/`** | Só o texto dos 31 projetos (EDICAO, pesquisas, scripts de cada época, planos) — consulta histórica |
| **`broll-prompts/`** | Pesquisas/prompts de B-roll dos primeiros reels |
| **`legado/`** | Kit v1 (gerador e skill de 16/09), prompts antigos, backup |
| **`COMECE-AQUI.md` · `instalar.sh`** | Levar o kit para outro Mac: guia simples + instalador de um comando |
| **`exemplos/deming/`** | **O reel mais recente e o padrão atual** (dosagem foto × motion, camada gerada por script) |
| **`skill/`** | `edicao-reel-viral` (porta de entrada) + `showreel-interface` (método da camada; o `mg_sfx.py` depende dela) |
| **`verificar-instalacao.sh`** | Confere o ambiente e reconstrói o reel de referência |
| `exemplos/natura`, `exemplos/nubank`, `bruto/` | do kit v1 (formato antigo, 1080×1920 @30) |

### Ordem de leitura
0. **`docs/14-fluxo-rapido.md` — o fluxo PADRÃO (kit v3): ~1 h do bruto ao MP4, com a camada de motion**
1. `docs/05-calibracoes-e-armadilhas.md` — todo número travado e todo erro já pago
2. `docs/01-pipeline-hyperframes.md` — o fluxo fase a fase, com comandos e o contrato do `edit-plan.json`
3. `docs/06-checklist-execucao.md` — checklist
4. `docs/10-scripts.md` — o que cada script faz; quais são motor e quais são dados do vídeo
5. `docs/02-jcut-algoritmo.md` · `docs/11-pesquisa-broll.md` · `docs/12-export-em-partes.md`
5b. **`docs/05` §24 — dosagem: abertura só com fotos, motion só onde conta a história**
6. **`docs/13-camada-motion.md` — o padrão atual (motion graphics da skill showreel-interface), exemplo em `exemplos/alan-mulally/`**
7. `docs/04-prompt-comando-unico.md` — o prompt
8. `docs/09-instalacao-outra-maquina.md` · `docs/07-mapa-de-arquivos.md`
9. Histórico: `docs/03-blueprint-casas-bahia.md`, `docs/08-storyboard-opcional.md`

---

## As regras que não se negociam

1. **Nunca editar o `index.html` à mão.** Plano → `build-edit.mjs` → `bake.py` → `npm run check`.
2. **Mezanino com a conversão de cor certa antes de tudo** (quase todo bruto é SDR *full-range*; sem converter, lava).
3. **Uma tarefa pesada por vez.** Whisper junto com encode derruba o Mac.
4. **O apresentador aparece olhando para a câmera.** Varredura de olhar duas vezes; leitura exposta reportada em segundos.
5. **Primeira cena em split, capa laranja no quadro 0.** Nada da marca antes de o áudio dizer o nome.
6. **Último take válido; palavra inteira; palavrão bipado inteiro e conferido por medição.**
7. **J-cut validado por dados** (`jcut_check.py`): fala 5 quadros antes do corte, crossfade no silêncio.
8. **Troca de cena ou efeito a cada ~4 s, com transição em todo corte.**
9. **Kit v3: comando único sem parada** (docs/14), MP4 mandado no chat. Parada só a pedido.
10. **Composição leve** (≤ ~10 elementos de mídia) e **export em partes**.

---

## Como o kit se mantém

- Todo reel fecha levando as "Lições para o kit" do seu `EDICAO.md` para `docs/05` e, se mexeu em script, para
  `modelo-projeto/scripts/`.
- O kit é um repositório git (`git log` mostra o que mudou e quando). `VERSAO.md` resume as versões.
- Cópia de segurança no servidor: `/Volumes/Company/Equipe/FABIO KENJI/KIT-EDICAO-REEL/` (atualizar depois de
  cada commit: comando em `VERSAO.md`).
- **Fora do kit, de propósito:** as chaves de API (`~/Claude/reel-auto/.env`), o modelo do Whisper (3 GB, em
  `~/.cache/whisper/`), as skills do HyperFrames (vêm com a ferramenta) e toda mídia de projeto.

## Histórico do formato

Casas Bahia (referência, CapCut → formato extraído quadro a quadro) → Ambev (Palmier) → Natura (1º em
HyperFrames) → Nubank → Bariloche (export em partes) → Localiza, O Boticário (capa laranja) → iPhone Duo (Oswald)
→ André Esteves (faixas pré-renderizadas, ritmo de 4 s) → Costco → Localiza2 (2K/60, marca só depois do áudio)
→ Jeff Bezos (bipe) → IKEA, Chris Voss, Rolex, Jocko Willink → Dan Martell (cenas de 3–5 s, B-roll e leaks numa
faixa) → Charlie Munger (olhar na timeline) → David Marquet → Atul Gawande (J-cut ponta a ponta) → Andy Grove,
Reed Hastings (lead da fala, `--split 3`) → Herb Kelleher → Taiichi Ohno (parada única) → Vince Lombardi → Mike
Michalowicz (layout à mão, imagem-conceito) → Sun Tzu → Kazuo Inamori (olhar compensado pela pose).
