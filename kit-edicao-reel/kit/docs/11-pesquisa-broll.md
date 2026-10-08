# Pesquisa de B-roll

O que procurar, onde, com que ferramenta, e o que entregar na parada. Regras de uso da imagem em `docs/05` §14
(marca só depois do áudio) e §16 (geração).

## Método atual (2026-10-02): navegador na fonte primária, não busca por API

**Ir à fonte, não a um buscador.** Busca de imagens por API (Serper/Google, Bing) devolve repostagens: banco de
imagem disfarçado, resolução baixa, marca d'água. No reel Alan Mulally, 3 de 22 fotos assim tiveram de ser
trocadas no QC. O método que deu o melhor resultado (vídeos Vê.la e Joyce, sessão "Opus 5.5 Showreel"):

1. **Abrir as fontes no navegador do app** (`mcp__Claude_Browser__navigate` + `get_page_text`): sala de imprensa
   (ex.: media.ford.com), site oficial, RI, Instagram/LinkedIn da pessoa, página da Wikipedia, matérias. Ler o
   texto real — **todo número e fato do vídeo sai de uma página aberta**, com a URL registrada.
2. **Site inteiro de uma vez:** `npx hyperframes capture "<url>" -o ./capture --json` → imagens, SVGs, fontes,
   tokens de cor e screenshots em `capture/`.
3. **Imagem na maior resolução**: JavaScript na própria página (`javascript_tool`) listando
   `img.currentSrc || img.dataset.src || maior entrada do srcset`; quando o site serve por CDN com tamanho na URL,
   pedir o maior (ex.: `cdn.awsli.com.br/1920x1920/...`). Baixar com `curl -sSL -A "Mozilla/5.0"` (UA genérico,
   **nunca** dado do usuário) e medir com `sips`.
4. **Instagram:** abrir o perfil, rolar (`window.scrollTo` + espera) e extrair `a[href*="/p/"] img` → URLs dos
   posts; montar uma grade na própria aba para escolher pela captura de tela.
5. **Prova no formato do próprio conteúdo** (skill showreel-interface): screenshot real da manchete/matéria
   (ex.: "Ford penhora o logotipo", "GM pede falência") vale mais que foto genérica do assunto.
6. **Logos:** SVG oficial (Commons/site); se só houver PNG pequeno, vetorizar (OpenCV → SVG) e separar as partes
   para animar. Logo só sofre corte, fade, deslocamento e escala uniforme.
7. **Folha de contato** (`work/pesq/sheet.py`) → escolher → recortar tirando texto sobreposto.

Tema da NASA (programa espacial, astronautas, controle de missão): **NASA Image and Video Library primeiro** (`work/pesq/nasa.py` → `nasadl.py`, docs/05 §33).
Fallback: Wikimedia Commons (`work/pesq/wm.py` / `wmpick.py`, licença registrada; no container, `wmstd.py` — docs/05 §28). Busca por API só se não houver
fonte primária, e passando pelo `filt.py`. (`scripts/bimg.py` do projeto alan-mulally foi um remendo para
máquina sem chave Serper: **aposentado**, não usar.)

## O que procurar

Uma foto **real** por slot, que mostre o que a fala daquele trecho diz. Em ordem de preferência:

1. Sala de imprensa / site oficial / RI da empresa (ou o site oficial da pessoa, da editora, do evento) — pelo navegador, acima.
2. Wikimedia Commons (alta resolução, licença registrada).
3. Busca de imagens em tamanho grande (`gimg.mjs` pede `isz:l`) — último recurso.

**Trecho conceitual** (processo, número, gráfico, "semáforo", "arco-íris"…) sem imagem real que o represente:
**não vira foto genérica, vira motion graphics** na camada `compositions/mg.html` (docs/13).

Critérios: lado menor ≥ ~900 px (abaixo disso só com `fill`); sem marca d'água; assunto que caiba no 9:16 (tela
cheia) ou na faixa 16:9 do split; **variedade** — duas fotos parecidas em sequência leem como "parado".
`filt.py` já descarta bancos de imagem (Shutterstock, Getty, Alamy, iStock, Pinterest…).

**Pré-revelação** (antes de o áudio dizer o nome): é o gargalo. Funciona interior/detalhe do material oficial
sem logo, recorte abaixo do letreiro, ou cena genérica do assunto. Foto de fachada e de protesto trazem o nome.

**IA generativa: nunca por conta própria.** Só quando o Fabio descreve a cena — aí é `fal_img.mjs` com
`fal-ai/nano-banana-pro`, 4:3 (serve para split e para tela cheia com fundo borrado), mostrada na parada e
marcada "gerada a pedido" no arquivo de pesquisas. O flux errou mãos; o nano-banana-pro acertou. Não usar
`dry_run` para testar modelo no fal: enfileira job de verdade.

## Ferramentas (`work/pesq/`, rodar de dentro dela ou pelos caminhos indicados)

| Ferramenta | Uso |
|---|---|
| `s.sh <qid> "consulta" [n]` | Google Imagens → `q/<qid>.txt` (já filtrado por `filt.py`) |
| `pick.sh <qid> <idx…>` | baixa os escolhidos em `raw/<qid>_<idx>.jpg` e registra em `g_index.json` |
| `wm.py "consulta" [n]` | busca no Commons → `q/wm_<slug>.json` (título, tamanho, licença) |
| `wmpick.py <slug> <idx…>` | baixa do Commons e grava a licença em `wm_lic.json` |
| `wmcat.py "Category:<nome>" [n]` | lista os arquivos de uma CATEGORIA do Commons → `q/wm_<slug>.json` (licença, data, descrição; pagina de 50 em 50) — melhor que a busca por texto (docs/05 §29/§30) |
| `wmstd.py <largura> <slug>:<idx,…>` | idem, pela miniatura de tamanho padrão montada da URL (sem API por arquivo: não toma 429 no container) |
| `wmcatlote.py q/wm_<slug>.json "Category:A" …` | várias categorias de uma vez honrando o `retry-after` do 429 (1 chamada por categoria + 1 por lote de 50) — docs/05 §31 |
| `nasa.py "consulta" [n]` · `nasadesc.py <id…>` · `nasadl.py <id…>` | **tema da NASA:** busca na NASA Image and Video Library (`images-api.nasa.gov`, fonte primária, domínio público), descrição completa (data, nomes) e download do `~orig.jpg` → `nasa/<id>.jpg` + `licencas.tsv`. Sem 429: 16 fotos em ~2 min (docs/05 §33) |
| `wmfila.py <slug> <idx,…>` | baixa a fila priorizada na largura padrão 1920/1280/960 com espera crescente (429) — docs/05 §31 |
| `crawl.py <base> <prefixo> <limite> <saida.json>` | varre um site oficial e lista as imagens |
| `dl.py <tag> <img> <page> <dom>` | download com UA genérico de Chrome e Referer; converte para JPG |
| `sheet.py <saida.jpg> <glob…>` | folha de miniaturas rotuladas para escolher |

Convenção de nome: o prefixo do arquivo é o trecho do roteiro (`b03a_9`, `c18a_15`…), para montar folha por
trecho. Escolhidas vão para `cand/`, com `candidates.json` e `picks.json` (escolha + alternativa por slot).

As chaves (`SERPER_API_KEY`, `FAL_KEY`) ficam em `~/Claude/reel-auto/.env` — fora do kit, do git e do servidor.

## Se delegar a um subagente

Pôr no prompt, textualmente:

- "Use um User-Agent genérico de Chrome. **Nunca** coloque e-mail, nome ou qualquer dado do usuário em headers,
  URLs ou payloads." (No Andy Grove o subagente pôs o e-mail do Fabio no UA para o Wikimedia.)
- "No máximo ~3 consultas por trecho. Entregue `candidates.json` e `picks.json` **antes** de ampliar a busca."
  (No Kazuo ele travou duas vezes, 600 s sem progresso, com 331 fotos baixadas e nenhum pick.)
- O que já está decidido: slots, tempos, o que é pré-revelação, o que o Fabio entregou.

Se travar: **não retomar**. Montar as folhas por trecho a partir do `g_index.json` e fechar à mão.

## O que sai da pesquisa

`PESQUISAS-BROLL-<TEMA>.md` (gerado por `scripts/pesquisa_md.py`), por slot: trecho da fala · tipo de
enquadramento (split 16:9 / tela cheia 9:16) · imagem recomendada · link e fonte · **prompt de animação** ·
duração necessária · nome do arquivo.

O prompt de animação descreve **só o movimento de câmera** (aproximação, travelling, tilt, pull-out), nunca
redescreve a imagem, e sempre diz que textos, logotipos e elementos de marca ficam parados, legíveis e nítidos.
Mesmo quando o B-roll é gerado localmente pelo `make_broll.py`, o movimento usado é o do prompt.

Exemplo completo: `exemplos/kazuo-inamori/PESQUISAS-BROLL-KAZUO-INAMORI.md`. Mais antigos em `broll-prompts/`
e em `arquivo-projetos/*/PESQUISAS-BROLL-*.md`.

## Da foto ao arquivo

`entrega.py` (tabela `PK`: candidata, âncora `ax/ay`, `fill`, pré-recorte) → `assets/broll-src/entrega/<slot>-9x16.jpg`
ou `-16x9.jpg` + folha `work/pesq/sheet_entrega.jpg` → `make_broll.py` (lista `S`: `z0/z1`, `dx/dy`, `dim`).
Decisões de enquadramento que já custaram iteração estão em `docs/05` §16.
