"""POR VIDEO — reel KAZUO INAMORI. Gera PESQUISAS-BROLL-KAZUO-INAMORI.md a partir de assets/broll-slots.json (scripts/slots.py),
work/pesq/candidates.json (pesquisa) e work/pesq/slot-picks.json (foto escolhida por slot, scripts/entrega.py).
Grava tambem img/link/fonte/prompt de cada slot em assets/broll-slots.json. Uso: python3 scripts/pesquisa_md.py"""
import json
S=json.load(open('assets/broll-slots.json'))['slots']
C={c['id']:c for c in json.load(open('work/pesq/candidates.json'))}
PK=json.load(open('work/pesq/slot-picks.json'))
ALT={k:v.get('alt') for k,v in json.load(open('work/pesq/picks.json')).items()}
LOCK=("Os textos, logotipos e elementos de marca da imagem (o logo JAL e o grou vermelho, o letreiro KYOCERA, a caligrafia 敬天愛人, "
"as notas de 10.000 ienes, os números do caderno e da calculadora, as telas do painel do avião, a palavra ACCEPTED) precisam ficar PARADOS, "
"legíveis e nítidos exatamente como na imagem de referência: sem morphing, sem deformar, sem redesenhar, sem inventar letras novas e sem mudar cor. "
"Rostos e mãos não podem mudar de feição, de forma nem de identidade. Nada na cena se move por conta própria — ninguém anda, fala, gesticula ou pisca, "
"nenhum objeto desliza, nenhuma chama ou luz pisca, nenhuma pessoa ou objeto novo aparece. O ÚNICO movimento é o da câmera. Movimento constante e suave, "
"sem aceleração, sem corte, sem tremor.")
DESC={k:C[PK[k]]['desc'] for k in PK}
CAM={
"s01":"Aproximação lenta (~4%) em direção ao monge de costas no centro da pista.",
"s02":"Aproximação lenta (~5%) seguindo o monge de costas, com leve deriva para cima (~2% da altura).",
"s03":"Travelling lateral lento da esquerda para a direita (~4% da largura) com leve aproximação em direção à mão sobre a mesa.",
"s04":"Aproximação lenta (~5%) em direção ao papel que o homem segura contra o peito.",
"s05":"Aproximação muito lenta (~6%) centrada no rosto.",
"s06":"Tilt lento de baixo para cima (~5% da altura), do rosário nas mãos até o rosto, com leve aproximação (~3%).",
"s07":"Tilt lento de cima para baixo (~5% da altura), do logotipo no avião até o homem no púlpito.",
"s08":"Travelling lateral lento da esquerda para a direita (~4% da largura) ao longo do grupo.",
"s09":"Aproximação lenta (~5%) em direção ao centro do grupo.",
"s10":"Tilt lento de baixo para cima (~6% da altura) ao longo da fachada do prédio.",
"s11":"Aproximação lenta (~5%) em direção ao visor da calculadora.",
"s12":"Aproximação lenta (~6%) em direção às telas do painel de instrumentos.",
"s13":"Aproximação muito lenta (~6%) em direção aos olhos do Mestre Po.",
"s14":"Tilt lento de cima para baixo (~5% da altura) ao longo da pilha de papéis até a bandeja.",
"s15":"Aproximação lenta (~5%) em direção à nota em chamas.",
"s16":"Aproximação lenta (~5%) em direção ao homem do centro.",
"s17":"Travelling lateral lento da esquerda para a direita (~5% da largura) sobre os maços de notas.",
"s18":"Travelling lateral lento da direita para a esquerda (~4% da largura) ao longo da fila de diretores.",
"s19":"Aproximação muito lenta (~6%) em direção aos dois funcionários curvados.",
"s20":"Travelling lento acompanhando o avião para a direita e para cima (~4% da largura, ~2% da altura).",
"s21":"Aproximação lenta (~5%) em direção à pessoa sozinha na mesa.",
}
NOTA={
"s01":"CAPA do reel (quadro 0, atrás da caixa laranja do gancho) e PRÉ-REVELAÇÃO. Gerada a seu pedido (fal.ai, nano-banana-pro, 4:3): bateu com a descrição de primeira (monge de costas, avião sem logotipo, luz vermelha no alto, preto/vermelho/âmbar). O split sai da foto 4:3 inteira para o monge e o avião ficarem acima da caixa do gancho.",
"s02":"PRÉ-REVELAÇÃO e cobre a olhada do gancho (1,72–2,24 s). Foto de matéria da revista Chichi (templo zen japonês), 1920x1280: o recorte vertical fica com 720 px de largura — é o slot de menor resolução. Alternativa nítida (3000x4498, Pexels): `d02f_2`, monge de túnica laranja num corredor de templo (não é zen japonês).",
"s03":"PRÉ-REVELAÇÃO. É a sua alternativa de capa (ação × curiosidade), gerada a pedido — fica aqui e disponível como capa B do teste (`work/conceito/c2-reuniao-nb.jpg`). Nenhum texto legível nas folhas.",
"s04":"PRÉ-REVELAÇÃO: callout de digitação \"VOCÊ ESCONDE O NÚMERO.\" + drum-fill sobre esta tomada (9,90 s). Pexels, licença livre.",
"s05":"REVELAÇÃO: entra em 11,25 s, 2 quadros depois de \"Kazuo\" (11,18 s). Retrato publicado pelo jornal Minami-Nippon Shimbun (373news.com), licença não informada — uso editorial.",
"s06":"Foto do jornal Sankei (1997, ordenação no templo Enpuku-ji), 1084x1701 — uso editorial. Alternativa em preto e branco de corpo inteiro: `b04a_0`.",
"s07":"Callout \"SEM SALÁRIO.\" nesta tomada (18,6 s). Foto do Sankei, 1200x1552 — uso editorial. O logo JAL ocupa o terço de cima: `capLowSegs` para a legenda não cobrir.",
"s08":"Foto institucional da Kyocera (kyocera.co.jp). Horizontal: entra inteira (recorte lateral leve) sobre o próprio fundo borrado.",
"s09":"Callout \"BRIGA PELO LUCRO.\" nesta tomada. Evento na Biblioteca Inamori (industry-co-creation.com), 1920x1080, sobre fundo borrado.",
"s10":"Sede da Kyocera em Kyoto (bigcompany.jp), vertical nativa.",
"s11":"Foto de divulgação da Casio (calculadora + kakeibo), 1600x1200, sobre fundo borrado. As alternativas com dinheiro eram em dólar.",
"s12":"Callout \"PILOTAR AVIÃO SEM OLHAR O PAINEL.\" nesta tomada. Foto de usuário (reddit), vertical 2268x4032 — uso editorial. É um 787; a JAL opera o modelo, mas a foto não identifica a companhia.",
"s13":"Mesma foto de divulgação da série Kung Fu (IMDb) usada no reel Sun Tzu — uso editorial. Alternativa: pôster da série (`b11b_12`).",
"s14":"Pexels, licença livre. A palavra ACCEPTED está em inglês.",
"s15":"Pexels, licença livre. É uma nota de dólar (não achei iene queimando em resolução útil). Logo depois o apresentador volta para o bipe (61,61–62,15 s).",
"s16":"Split com a transição de arrastar. Foto da Diamond Online (coletiva da JAL), 4096x2152 — uso editorial.",
"s17":"Split com a transição de arrastar. Foto de site japonês de numismática (kosen-kantei.jp), 5184x3456 — licença não informada.",
"s18":"Foto do JBpress (coletiva da JAL, 2010), 1600x1066, sobre fundo borrado — uso editorial. Riser do clímax começa em 79,28 s, já no apresentador.",
"s19":"CLÍMAX (impact-hit em 82,28 s + callout \"RASTEJANDO NO CHÃO.\"). Foto do site oficial da JAL (trico.jal.com), 1920x1280, sobre fundo borrado. Alternativa mais literal: carregadores agachados na esteira (`c18e_3`).",
"s20":"Unsplash, licença livre. Não achei a foto da relistagem na bolsa (2012) em resolução útil.",
"s21":"Pexels, licença livre. Cobre as duas olhadas do CTA (94,71–95,04 e 95,65–96,11 s); o apresentador volta em 96,15 s para \"me segue, porque você é demais\".",
}
L=[]
L.append("# PESQUISAS-BROLL-KAZUO-INAMORI.md\n")
L.append("Pesquisa de B-roll do reel **Kazuo Inamori** — formato viral, projeto HyperFrames `reel-auto/kazuo-inamori`.\n")
L.append("**21 tomadas em 4 slots.** Prioridade aplicada: (1) **sites oficiais** — Kyocera (`s08`) e Japan Airlines (`s19`); as salas de imprensa não têm o Inamori "
"de monge nem as coletivas de 2010 em tamanho útil; (2) **Google Imagens em tamanho grande**: imprensa japonesa (Sankei, Diamond, JBpress, Minami-Nippon) para o "
"retrato, o monge e a JAL; Pexels/Unsplash (licença livre) para as falas genéricas (esconder o número, orçamento, verba torrada, dono sozinho, decolagem). "
"Nada com marca d'água de banco de imagens. **Duas imagens são conceito gerado por IA a seu pedido** (`s01`, a capa, e `s03`, a alternativa de capa). "
"Todas as outras são fotos reais.\n")
L.append("As fotos originais estão em `assets/broll-src/<slot>.jpg`. **Já recortadas no formato de entrega**: `assets/broll-src/entrega/<slot>-9x16.jpg` "
"(tela cheia) e `<slot>-16x9.jpg` (split). As candidatas escolhidas e as alternativas: `work/pesq/cand/` (metadados em `work/pesq/candidates.json`, escolha e alternativa por slot em "
"`work/pesq/picks.json`); as 331 fotos baixadas na busca estão em `work/pesq/raw/` (índice `work/pesq/g_index.json`, folhas por trecho em `work/pesq/sheets2/`). "
"Mapa técnico: `assets/broll-slots.json`. Folha das escolhidas: `work/pesq/sheet_entrega.jpg`.\n")
L.append("**Geração:** depois do \"pode gerar as brolls\", as tomadas são geradas **localmente** por `scripts/make_broll.py`, que executa exatamente o "
"movimento de câmera de cada prompt sobre a foto (nada de IA generativa na animação): texto, logotipo e rosto ficam idênticos ao original. Os prompts abaixo "
"servem também para Kling/Seedance/Veo, se preferir gerar lá.\n")
L.append("## Regra que vale para TODOS os prompts\n\nO modelo recebe a imagem como referência, então **o prompt não redescreve a imagem**: só o movimento de câmera, e trava os textos e marcas:\n\n> "+LOCK+"\n")
L.append("## Por que as durações importam\n\nTempos a 1,1x. Vários cutaways cobrem um **desvio de olhar** medido no bruto. "
"**Se a tomada encurtar, o desvio reaparece**: a duração pedida é mínima. Gerar **5 s** em todas (a maior janela é 4,02 s); o corte é no quadro exato.\n")
L.append("## Como entregar (se for gerar fora)\n\n- **Split-screen** (`s01`, `s03`, `s04`, `s16`, `s17`): **16:9 horizontal**. No reel aparece a faixa central de ~72% da largura (topo de 44% da tela).\n"
"- **Tela cheia** (os demais): **9:16 vertical**.\n- Nome final de cada tomada na tabela do fim, em `reel-auto/kazuo-inamori/assets/broll/`. O áudio dos vídeos é zerado (só voz tratada + trilha + SFX).\n")
L.append("## Pontos de atenção (decisões e limitações)\n\n"
"- **Nome só depois do áudio:** \"Kazuo\" é dito em 11,18 s. `s01`–`s04` não mostram o Inamori, a Kyocera, a KDDI nem a JAL (o avião da capa não tem logotipo); a revelação (`s05`) entra em 11,25 s.\n"
"- **A capa é o split** (`s01`, quadro 0) com a sua imagem do monge na pista. A alternativa (mão batendo na mesa) está no `s03` e em `work/conceito/c2-reuniao-nb.jpg` para o teste de capa.\n"
"- **Fotos pequenas:** `s02` (720 px de largura no recorte), `s06` (956 px) e `s07` (873 px) são ampliadas para 1440 px — as únicas fotos reais do monge e da posse na JAL que achei em vertical. Seis fotos horizontais entram inteiras sobre fundo borrado (`s08`, `s09`, `s11`, `s18`, `s19`, `s20`).\n"
"- **Não achei em resolução útil:** a relistagem da JAL na bolsa em 2012 (`s20` usa a decolagem), o Inamori pedindo esmola de monge na rua (só miniaturas), iene queimando (`s15` é dólar).\n"
"- **Slots com texto/logo (maior risco se gerar com IA):** `s07`, `s18`, `s19`, `s20` (JAL), `s08`, `s10` (Kyocera), `s09` (caligrafia), `s11`, `s12` (números e telas), `s14` (ACCEPTED), `s17` (cédulas).\n"
"- **Licenças:** Pexels/Unsplash = licença livre (`s04`, `s14`, `s15`, `s20`, `s21`); Kyocera e JAL = material institucional (`s08`, `s19`); imprensa e sites japoneses, IMDb e reddit = "
"licença não informada, uso editorial (`s02`, `s05`, `s06`, `s07`, `s09`, `s10`, `s11`, `s12`, `s13`, `s16`, `s17`, `s18`); `s01`/`s03` gerados a pedido.\n"
"- A pesquisa foi feita com User-Agent genérico de Chrome, sem nenhum dado seu nas requisições.\n\n---\n")
SLOTS=[("SLOT 1 — INTRO EM SPLIT-SCREEN (PRÉ-REVELAÇÃO)","0,00 → 11,25 s. Capa em split no quadro 0 (`s01`), cutaway cobrindo a olhada do gancho (`s02`), e o split voltando com a transição de arrastar (`s03`, `s04` com o callout de digitação). **Nada de Inamori, Kyocera ou JAL** antes de 11,18 s, quando o áudio diz \"Kazuo\".",["s01","s02","s03","s04"]),
("SLOT 2 — CUTAWAYS DURANTE O CORPO DO VÍDEO","11,25 → 61,40 s. Revelação, o monge, a JAL e os três passos do protocolo. Entre os cutaways o apresentador aparece em tela cheia olhando para a câmera (inclusive no bipe, 61,61–62,15 s, e no \"Comenta MONGE\").",["s05","s06","s07","s08","s09","s10","s11","s12","s13","s14","s15"]),
("SLOT 3 — SEGUNDO SPLIT-SCREEN (A VIRADA: A REUNIÃO)","67,30 → 78,28 s. Split com a transição de arrastar (67,30–71,89), \"Ele cortou: pra você não confio nem um centavo\" no seu rosto, e os diretores (`s18`). \"Ele explodiu: de quem é esse dinheiro? Da empresa? Não.\" fica no seu rosto, com o riser subindo.",["s16","s17","s18"]),
("SLOT 4 — CLÍMAX EMOCIONAL","82,28 → 96,15 s. \"É o lucro que o funcionário tirou rastejando no chão\" (riser 3 s antes + impact-hit em 82,28 s), o recorde de lucro e, depois de \"Número escondido.\" no seu rosto, o dono sozinho com as contas. O CTA fecha no seu rosto.",["s19","s20","s21"])]
Sd={s['id']:s for s in S}
fmt=lambda x: f"{x:.2f}".replace('.',',')
for tit,desc,ids in SLOTS:
    L.append(f"## {tit}\n\n{desc}\n")
    for sid in ids:
        s=Sd[sid]; c=C[PK[sid]]; tag='16x9' if s['mode']=='split' else '9x16'
        enq="Split-screen (faixa de 44% do topo) — entregar em **16:9 horizontal**." if s['mode']=='split' else "Tela cheia — entregar em **9:16 vertical**."
        L.append(f"### `{sid}` — {fmt(s['t0'])} → {fmt(s['t1'])} s\n")
        L.append("| | |\n|---|---|")
        L.append(f"| **Trecho da fala** | \"{s['fala']}\" |")
        L.append(f"| **Tipo de enquadramento** | {enq} |")
        L.append(f"| **Imagem recomendada** | {s['tema']} — {DESC[sid]} |")
        L.append(f"| **Arquivo para subir** | `assets/broll-src/entrega/{sid}-{tag}.jpg` (original: `assets/broll-src/{sid}.jpg`, {c['w']}x{c['h']} px) |")
        L.append(f"| **Link da imagem** | {c['img']} |")
        L.append(f"| **Fonte** | {c['dom']} — {c['fonte']} — {c['page']} ({c['licenca']}) |")
        L.append(f"| **Duração necessária** | **{fmt(s['dur'])} s** (gerar 5 s) |")
        L.append(f"| **Nome do arquivo final** | `{s['file'].split('/')[-1]}` |")
        L.append(f"| **Cobre desvio de olhar** | {s['cobre']} |")
        L.append(f"| **Alternativa** | `{ALT.get(sid)}` — {C[ALT[sid]]['desc']} ({C[ALT[sid]]['dom']}, {C[ALT[sid]]['w']}x{C[ALT[sid]]['h']}) — `work/pesq/cand/{ALT[sid]}.jpg` |" if ALT.get(sid) else "| **Alternativa** | — |")
        L.append(f"| **Atenção** | {NOTA[sid]} |\n")
        L.append("**Prompt de animação (Kling / Seedance / Veo):**\n\n```\n"+CAM[sid]+" "+LOCK+"\n```\n")
        s.update(img=c['img'],link=c['page'],fonte=c['dom'],prompt=CAM[sid]+" "+LOCK,foto=PK[sid])
L.append("---\n\n## Resumo — arquivos que eu preciso receber em `assets/broll/`\n\n| Slot | Janela (s) | Duração | Formato | Nome do arquivo |\n|---|---|---|---|---|")
for s in S:
    L.append(f"| `{s['id']}` | {fmt(s['t0'])}–{fmt(s['t1'])} | {fmt(s['dur'])} s | {'16:9 (split)' if s['mode']=='split' else '9:16'} | `{s['file'].split('/')[-1]}` |")
open('PESQUISAS-BROLL-KAZUO-INAMORI.md','w').write('\n'.join(L)+'\n')
d=json.load(open('assets/broll-slots.json')); d['slots']=S; json.dump(d,open('assets/broll-slots.json','w'),ensure_ascii=False,indent=1)
print(f"PESQUISAS-BROLL-KAZUO-INAMORI.md: {len(S)} tomadas")
