# EDICAO.md — mapa do projeto (reel Deming)

Kit v3 (fluxo rápido, docs/14) + camada de motion (showreel-interface). Palco 1440x2560, timeline 30 fps, saída 1440x2560 @ 60 fps, 1,1x.
**Estado (2026-10-02): RENDERIZADO** (`renders/Deming-reel-final.mp4`), comando único sem parada.
Duração **101,31 s** · 30 takes · 1 bipe · 102 legendas · 4 callouts · 3 light-leaks (virada, clímax, CTA) · 11 cenas de motion · 2 splits.

> Regra de ouro: nunca editar `index.html` nem `compositions/mg.html` à mão. A camada sai de `work/mg/gen.py` (`python3 work/mg/gen.py`), depois `zsh scripts/montar.sh`.

## Bruto
`~/Claude/videos-brutos/deming-bruto.MP4` (cópia de ~/Downloads/89D5923E-….MP4) — MD5 `85706cdb154fce6e15e6209f03e42339`. HEVC 1440x2560 @60, 137,5 s, SDR full-range → mezanino full→limited.

## Takes descartados (mantido o ÚLTIMO)
r01 "Demi foi dar aulas…" e r02 "…medalha do empre…" → r03 · r09 "E quem montou…" → r10 · r11 fim "foi o ranking que…" → r12 · r16 "…no almoço biquen…" → r17. CTA r25–r27 = um take.

## Áudio ≠ roteiro (vale o áudio)
"dar aulas", "esconde O cliente", "Vermelho era O defeito". Grafia do roteiro: "pras", "pra", "cem", "noventa e quatro", "três", "Seu melhor", "que ensinou".
Não dá para ouvir o "de" em "de cada cem" (legenda: "Ele diz que cada cem problemas").

## Bipe
"porra" (51,13–51,645 s do source): /p/ 51,14 · decaimento até 51,64. Medido na voz-mix: 99,9% em 950–1050 Hz, 0% fora de 900–1100. Legenda `P****`. Apresentador em tela cheia.

## J-cut
29 emendas · 0 buracos · nenhum crossfade sobre fala · lead 4,9 quadros · respiro 0,245 s.

## Olhar
70 janelas nas folhas (gaze/me). Nítidas: 11,58 · 14,04 · 30,46–30,70 · 33,38–33,59 · 45,20 · 84,02–84,55 · 95,17–95,41 — todas sob motion. Leitura exposta: 0 s.

## Split
`splitShiftY` 520 (olhos medidos ~1213–1282 com 400 → ~1371). Splits: capa 0–11,37 · virada 71,34–75,99.

## Marca só depois do nome
"Deming" em 11,30 s → revelação em 11,37 (capa = professor de costas, sem rosto).

## Imagens
Capa: Codex gpt-5.6-sol (gerada a pedido — cena escolhida por mim, o pedido veio com o placeholder "[DESCRIÇÃO DA CENA]"): aula numa fábrica japonesa em 1950, professor de costas.
Retrato: Wikimedia `W. Edwards Deming.jpg` (domínio público, 393 px). Aula em Tóquio 1950, Deming com a Ordem do Tesouro Sagrado, medalha do Prêmio Deming: JUSE (juse.or.jp/deming_en/award, 200 px — usadas como cartões pequenos, ampliadas 4x).
Insígnia da Ordem do Tesouro Sagrado (2ª classe): Wikimedia CC BY 4.0. Mestre Po: reaproveitado do reel Alan Mulally.
deming.org bloqueou com verificação anti-robô (não contornada).

## Lições para o kit
- Fundo `.light` da camada precisa de "chão" escuro abaixo de ~64% da tela: legenda branca a 76% sobre cena clara reprova no contraste (check) e some.
- `.tag` com `white-space: nowrap` (tag longa quebrava em 2 linhas).
- Fonte primária com Cloudflare (deming.org) bloqueia o navegador do app: cair para site institucional (JUSE) + Commons.

## v2 (2026-10-02) — pedido: "diminuir os motion graphics, mais imagens; o início só com imagens"
- Abertura (split 0–11,37) só com fotos: capa (Codex) → operário na fábrica (LOC/FSA, domínio público) → desempregado encostado na vitrine "TO LEASE"
  (Dorothea Lange, NARA, domínio público). Saíram as etiquetas EUA/JAPÃO, os crachás e o DEMITIDO. O callout de digitação continua.
- Corpo: saíram o loop de crachás, os 3 crachás de vendedor + gráfico de vendas, os balões "kkkk", a fileira de voluntários e o gráfico "não diminui".
  Entraram fotos: linha de montagem A-20 (NARA, DP) · vendedor 1958 (Commons, CC BY 4.0) · mural "Employee of the Month" (Commons, CC BY-SA 4.0) ·
  operários rindo no almoço (NARA, DP). "E a vermelha não diminuía" (87,94–90,00) passou para o apresentador.
- Motion ficou nos capítulos (PASSO 1/2/3), nos 94 de 100, no ranking (só o trecho do cliente escondido), no cartaz, na caixa de bolinhas, na pá, no placar e no clímax.
- Licenças: work/pesq/q2/licencas.txt. Camada v1 guardada em work/mg/gen-v1.py.
- Render v2: `renders/Deming-reel-final-v2.mp4` (QC OK). Lição para o kit: `render-par.sh` RETOMA — pula toda `renders/chunks/chunk-NN.mp4` que já existe.
  Depois de mudar a camada, apagar as partes afetadas antes (na 1ª tentativa ele reaproveitou as 14 partes da v1 e o MP4 saiu igual à v1).
