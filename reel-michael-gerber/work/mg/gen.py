"""POR VIDEO — reel MICHAEL GERBER. Gera compositions/mg.html = modelo do kit (work/mg/template.html, biblioteca intacta)
+ CSS/markup/CENAS deste reel. Os tempos saem de work/tl-words.txt pela FRASE (T("frase") = inicio da 1a palavra; w = indice da
palavra dentro da frase; k = ocorrencia), entao um ajuste de corte so pede rodar este gerador de novo.
Dosagem (docs/05 §24, Deming v2): abertura so com imagem (capa gerada + a dona do armazem + o relogio de ponto; nada do Michael antes de
"Michael"); no corpo foto real e o padrao (o Michael em 2009; a padaria de San Angelo, 1939; a moca com a torta, Harris & Ewing);
motion so nos capitulos (PASSO 1/2/3), no organograma com o seu nome em cada cadeira, na franquia (a mesma loja em todo lugar), no passo a
passo, no contrato da cadeira, na ordem cadeira -> pessoa (e o sobrinho), no COMENTA CADEIRA, no EMPRESA -> EMPREGO e no "Seguir".
uso: python3 work/mg/gen.py"""
import sys, re, unicodedata
sys.path.insert(0, 'work/mg')
from parts import CSS
T_ = open('work/mg/template.html').read()

# ---------- tempos pela frase (work/tl-words.txt) ----------
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return re.sub(r'[^a-z0-9]', '', ''.join(c for c in s if unicodedata.category(c) != 'Mn'))
ENT = []; SEG = {}
for line in open('work/tl-words.txt'):
    m = re.match(r'\s*(\d+)\s+(\S+)\s+([\d.]+)-\s*([\d.]+)\s+\([\d.]+\)\s*(.*)$', line.rstrip('\n'))
    if not m: continue
    SEG[m.group(2)] = (float(m.group(3)), float(m.group(4)))
    parts_ = re.split(r'@(\d+\.\d+)\s*', m.group(5))
    for k in range(0, len(parts_) - 1, 2):
        ENT.append((norm(parts_[k]), float(parts_[k + 1])))
BIG = ''; START = []
for n, t in ENT: START.append(len(BIG)); BIG += n
def _ent(ci):
    for e in range(len(START) - 1, -1, -1):
        if START[e] <= ci: return e
def T(phrase, w=0, k=1, after=0.0):
    toks = [norm(x) for x in phrase.split() if norm(x)]; p = ''.join(toks); pos = -1; found = 0
    while True:
        pos = BIG.find(p, pos + 1)
        if pos < 0: raise SystemExit(f'frase nao achada no tl-words: {phrase!r} (k={k}, after={after})')
        e = _ent(pos)
        if START[e] != pos or ENT[e][1] < after: continue
        found += 1
        if found == k: return ENT[_ent(pos + len(''.join(toks[:w])))][1]
def S0(lab): return SEG[lab][0]
def S1(lab): return SEG[lab][1]

F = dict(  # foto por papel (assets/mg/, preparadas por work/mg/fotos.py)
    capa='capa.jpg', perto='capa-perto.jpg', dona='dona-armazem.jpg', relogio='relogio-ponto.jpg', gerber='gerber.jpg', gerber2='gerber-2.jpg',
    moca='moca-torta.jpg', mesa='mesa-tortas.jpg', mesav='mesa-tortas-v.jpg', forno='forno.jpg', carrinho='carrinho.jpg')
OP = dict(  # object-position de cada foto (medido no snapshot)
    capa_split='50% 30%', perto_split='50% 30%', capa='44% 50%', perto='42% 50%', dona='30% 50%', relogio='38% 50%', gerber='62% 50%',
    moca='50% 50%', mesa_split='50% 45%', mesav='40% 50%', forno='46% 50%', carrinho='62% 50%')
def img(k, cls=''):
    return f'<img id="{{id}}" class="{cls}" src="assets/mg/{F[k]}" style="object-position:{OP.get(k, "50% 50%")}" />'
def full(id_, k, cls='', extra='', op=None):
    s = img(k, cls).replace('{id}', id_ + 'img')
    if op: s = s.replace(OP.get(k, '50% 50%'), op)
    return f'<div class="full" id="{id_}">' + s + extra + '</div>'
def fit(id_, k, top, h, cls='', extra=''):  # foto horizontal: inteira na largura sobre ela mesma desfocada (docs/05 §31)
    return (f'<div class="full" id="{id_}"><img class="bgblur {cls}" src="assets/mg/{F[k]}" />'
            f'<div class="fitimg" style="top:{top}px;height:{h}px"><img id="{id_}img" class="{cls}" src="assets/mg/{F[k]}" /></div>{extra}</div>')
def chip(b, n, dot):
    rolls = {1: ('PASSO 3', 'PASSO 2', 'PASSO 1'), 2: ('PASSO 1', 'PASSO 3', 'PASSO 2'), 3: ('PASSO 2', 'PASSO 1', 'PASSO 3')}[n]
    return (f'<div class="chip" id="{b}-chip" style="top:300px;background:#fff;color:#11141A"><span class="dot" style="background:{dot}"></span>'
            f'<div class="win"><div class="roll" id="{b}-roll">' + ''.join(f'<span>{r}</span>' for r in rolls)
            + f'</div></div><div class="plus" id="{b}-plus" style="background:#fff;color:#11141A">+</div></div>')
def title(b, l1, l2, color='#fff', size=None):
    w = l1 + l2; n = len(w)
    sp = [f'<span id="{b}-w{k+1}">{x}</span>' for k, x in enumerate(w)]
    sel = f'<span class="sel" id="{b}-sel">{sp[-1]}<i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i></span>'
    fs = f';font-size:{size}px' if size else ''
    return (f'<div class="title" id="{b}-title" style="top:520px;color:{color}{fs}">' + ' '.join(sp[:len(l1)]) + '<br />'
            + ' '.join(sp[len(l1):n - 1] + [sel]) + '</div>')

# organograma: 6 cadeiras em 2 colunas x 3 linhas, presas a uma espinha central
SEATS = [('VENDAS', 0, 0), ('FINANCEIRO', 1, 0), ('COMPRAS', 0, 1), ('ENTREGA', 1, 1), ('ATENDIMENTO', 0, 2), ('MARKETING', 1, 2)]
SX = {0: 58, 1: 512}; SY = {0: 210, 1: 470, 2: 730}
ORG = ''.join(f'<div class="seat" id="D-s{k}" style="left:{SX[c]}px;top:{SY[r]}px"><span class="k">CADEIRA</span><span class="d">{nm}</span>'
              f'<span class="ln"></span><span class="you" id="D-y{k}">VOCÊ</span><span class="red" id="D-r{k}"></span></div>'
              for k, (nm, c, r) in enumerate(SEATS))
ARMS = ''.join(f'<div class="arm" style="left:{468 if c == 0 else 492}px;top:{SY[r] + 105}px"></div>' for nm, c, r in SEATS)
# franquia: 1 loja -> 9 iguais
def shop(id_, x, y, s=1.0):
    return (f'<div class="shop" id="{id_}" style="left:{x}px;top:{y}px;transform:scale({s})"><div class="roof"></div><div class="body"></div>'
            f'<div class="win" style="left:34px"></div><div class="win" style="left:164px"></div><div class="door"></div></div>')
GRID = ''.join(shop(f'F-g{k}', 75 + (k % 3) * 335, 330 + (k // 3) * 300) for k in range(9))
STEPS = ''.join(f'<div class="st"><b>{k+1}</b><i id="F-l{k}" style="width:{w}px"></i></div>' for k, w in enumerate([560, 470, 520, 430, 500]))
SIG = ('<svg width="640" height="170" viewBox="0 0 640 170"><path id="H-sig" d="M20 120 C 60 40, 90 40, 100 110 S 150 150, 170 80 S 220 20, 240 100 '
       'S 300 140, 330 70 C 350 30, 380 40, 370 100 C 365 130, 420 120, 450 80 S 520 60, 600 90" fill="none" stroke="#1E3A8A" stroke-width="9" '
       'stroke-linecap="round" stroke-linejoin="round" /></svg>')
CADEIRA = ''.join(f'<span class="ch" id="M-c{k}">{c}</span>' for k, c in enumerate('CADEIRA'))

def build():
    t = {}
    # ---------- tempos (pela frase) ----------
    t['hook_copiados'] = T('mais copiados', 1)
    t['P_in'] = S0('PROTOCOLO-POLEMICO'); t['P_emprego'] = T('você não tem uma empresa', 0)
    t['P_out'] = S1('PROTOCOLO-POLEMICO')
    t['michael'] = T('Michael') + 2 / 30
    t['B_nome'] = T('ensinava'); t['B_socio'] = T('até o sócio'); t['B_quebrado'] = T('a gente tá quebrando')
    t['B_ocup'] = S0('OCUPADO'); t['B_out'] = S1('OCUPADO')
    # PASSO 1
    t['D_in'] = S0('P1-PRIMEIRO'); t['D_chip'] = T('Primeiro'); t['D_w'] = [T('desenha o organograma', i) for i in range(3)]
    t['D_org'] = T('Cada cadeira'); t['D_dep'] = [T('vendas, financeiro, compras, entrega', i) for i in range(4)]
    t['D_nome'] = T('escrever o seu nome', 1); t['D_cada'] = T('em cada cadeira que é sua')
    t['D_seis'] = T('seis cadeiras'); t['D_out'] = T('Você não é o dono') - 0.15  # sai antes do callout "VOCE NAO E O DONO."
    # PASSO 2
    t['F_in'] = S0('P2-SEGUNDO'); t['F_chip'] = T('Segundo'); t['F_w'] = [T('monta a empresa', 0), T('como se fosse vender', 0), T('como se fosse vender', 2)]; t['F_sel'] = T('vender franquia', 0)
    t['F_fr'] = T('vender franquia', 1) + 0.1; t['F_pp0'] = T('escreve passo a passo') - 0.2; t['F_pp'] = T('passo a passo')
    t['F_comum'] = T('gente comum'); t['F_genio'] = T('não com gênio', 2); t['F_out'] = S1('P2-GENTE-COMUM')
    # PASSO 3
    t['H_in'] = T('ela não funciona', 2) + 0.38; t['H_chip'] = T('E terceiro'); t['H_w'] = [T('assina o contrato', i) for i in range(3)]
    t['H_folha'] = T('Escreve numa folha'); t['H_entrega'] = T('aquela cadeira entrega', 2); t['H_assina'] = T('você assina como se fosse funcionário', 1)
    t['H_func'] = T('como se fosse funcionário', 3)
    t['H_ordem'] = T('primeiro a cadeira'); t['H_pessoa'] = T('depois a pessoa'); t['H_sobrinho'] = T('primeiro veio o sobrinho', 3)
    t['H_out'] = S1('P3-SOBRINHO')
    # CTA do meio
    t['M_in'] = T('Comenta'); t['M_cad'] = T('cadeira que eu te mando'); t['M_out'] = S1('CTA-COMENTA')
    # virada
    t['L_in'] = S0('VIRADA-TORTA'); t['L_out'] = S1('VIRADA-TORTA')
    t['N_in'] = S0('VIRADA-SARAH'); t['N_loja'] = T('abriu a própria loja'); t['N_tres'] = T('Três anos depois'); t['N_cheiro'] = T('cheirando a torta')
    t['N_odeio'] = T('odeio fazer torta'); t['N_aguento'] = T('Não aguento'); t['N_out'] = S0('CLIMAX-EMPRESA')
    # climax
    t['C_in'] = S0('CLIMAX-EMPRESA'); t['C_nao'] = T('não abriu uma empresa', 0); t['C_empresa'] = T('não abriu uma empresa', 3)
    t['C_emprego'] = T('Abriu um emprego', 2); t['C_out'] = S1('CLIMAX-EMPREGO')
    t['G_seg'] = T('segunda-feira'); t['G_out'] = T('meu amigo') + 0.45
    t['S_segue'] = T('me segue'); t['S_out'] = T('você é demais', 2) - 0.25
    return t
t = build()
import json as _json
_json.dump({k: v for k, v in t.items()}, open('work/mg/tempos.json', 'w'), indent=0)  # lido por scripts/slots.py
for k, v in t.items(): print(f'  {k:<14} {v}')

HTML = f'''
        <!-- A · SPLIT DA CAPA (o gancho): CAPA GERADA A PEDIDO (Codex: padaria as 4 h, forno aberto, a mulher de avental de costas, cabeca
             entre as maos) -> em "e mais copiados" a mesma cena mais perto. Nada do Michael. -->
        <div class="scene" id="A" style="height:845px"><div class="world dark"></div>{full('A-capa', 'capa', op=OP['capa_split'])}
          {full('A-perto', 'perto', op=OP['perto_split'])}</div>

        <!-- P · PRE-REVELACAO: o relogio de ponto (British Library) -> a dona do armazem (NARA, 1973) em "voce nao tem uma empresa" -->
        <div class="scene" id="P"><div class="world dark"></div>
          {full('P-rel', 'relogio', '', '<div class="floor"></div>')}
          {full('P-dona', 'dona', 'dim', '<div class="floor"></div>')}
        </div>

        <!-- B · REVELACAO ("Michael" + 2 quadros): o Michael em 2009 + nome -> o socio: "a gente ta quebrando." (1985) -->
        <div class="scene" id="B"><div class="world dark"></div>
          {fit('B-ger', 'gerber', 250, 810)}
          <div class="name" id="B-name" style="top:1100px"><b>MICHAEL E. GERBER</b><i>AUTOR DE “O MITO DO EMPREENDEDOR”</i></div>
          <div class="full" id="B-chat"><div class="world dark"></div>
            <div class="yr" id="B-yr" style="top:380px">1985</div>
            <div class="who" id="B-wa" style="left:90px;top:640px"><i style="background:#5A606B">S</i>O SÓCIO</div>
            <div class="dots" id="B-dots" style="left:90px;top:730px"><i></i><i></i><i></i></div>
            <div class="bubble big" id="B-b1" style="left:90px;top:730px">A gente tá quebrando.</div>
          </div>
          {fit('B-ger2', 'gerber2', 300, 810)}
        </div>

        <!-- D · PASSO 1: chip + titulo -> o organograma: as cadeiras nas palavras, VOCE escrito em cada uma, SEU NOME EM 6 CADEIRAS -->
        <div class="scene" id="D"><div class="world dark"><div class="band" id="D-band"></div></div>
          {chip('D', 1, '#E5322D')}
          {title('D', ['DESENHA', 'O'], ['ORGANOGRAMA.'], size=104)}
          <div class="full" id="D-org"><div class="world dark"></div>
            <div class="paper org" style="top:150px;height:1010px">
              <div class="hdr" id="D-hdr">SUA EMPRESA</div><div class="spine" id="D-spine"></div>{ARMS}{ORG}
            </div>
            <div class="cnt" id="D-cnt" style="top:1190px"><span>SEU NOME EM 6 CADEIRAS</span></div>
          </div>
        </div>

        <!-- F · PASSO 2: chip + titulo -> a franquia (a mesma loja 9 vezes) -> o passo a passo -> gente comum x genio -->
        <div class="scene" id="F"><div class="world dark"><div class="band" id="F-band"></div></div>
          {chip('F', 2, '#F2B705')}
          {title('F', ['MONTA', 'COMO'], ['FRANQUIA.'])}
          <div class="full" id="F-fr"><div class="world dark"></div>
            {shop('F-one', 415, 600, 1.0)}{GRID}
            <div class="lbl2" id="F-igual" style="top:1240px;font-size:44px;color:#F2B705">A MESMA LOJA EM TODO LUGAR</div>
          </div>
          <div class="full" id="F-pp"><div class="world dark"></div>
            <div class="sheet" style="top:230px"><div class="hd">TUDO QUE VOCÊ FAZ DE CABEÇA</div><div class="tt">Passo a passo</div>{STEPS}</div>
          </div>
          <div class="full" id="F-vs"><div class="world dark"></div>
            <div class="vcard" id="F-com" style="left:70px"><div class="ppl3"><i style="left:0"></i><i style="left:104px"></i><i style="left:208px"></i></div>
              <div class="dp">GENTE COMUM</div><div class="mk" id="F-ok" style="background:#1FB45A">✓</div></div>
            <div class="vcard" id="F-gen" style="left:560px"><div class="bulb"></div><div class="dp">GÊNIO</div>
              <div class="mk" id="F-no" style="background:#E5322D">✕</div></div>
          </div>
        </div>

        <!-- H · PASSO 3: chip + titulo -> o contrato da cadeira (assinado como funcionario) -> 1o a cadeira, 2o a pessoa -> o sobrinho -->
        <div class="scene" id="H"><div class="world dark"><div class="band" id="H-band"></div></div>
          {chip('H', 3, '#1FB45A')}
          {title('H', ['ASSINA', 'O'], ['CONTRATO.'])}
          <div class="full" id="H-ct"><div class="world dark"></div>
            <div class="ctt" id="H-doc" style="top:200px"><div class="hd">CONTRATO DA CADEIRA</div><div class="tt">Vendas</div>
              <div class="rw" id="H-r1"><span>O QUE ENTREGA</span><i style="width:380px"></i></div>
              <div class="rw" id="H-r2"><span></span><i style="width:300px"></i></div>
              <div class="rw" id="H-r3"><span>COMO SE MEDE</span><i style="width:340px"></i></div>
              <div class="sg">{SIG}<div class="bl"></div><div class="nm" id="H-nm">VOCÊ · FUNCIONÁRIO</div></div>
            </div>
          </div>
          <div class="full" id="H-or"><div class="world dark"></div>
            <div class="ord" id="H-o1" style="top:420px"><b>1º</b><div class="sw"><span id="H-a1">A CADEIRA</span><span class="rd" id="H-b1">O SOBRINHO</span></div></div>
            <div class="ord" id="H-o2" style="top:650px"><b>2º</b><div class="sw"><span id="H-a2">A PESSOA</span><span class="rd" id="H-b2">A CADEIRA</span></div></div>
          </div>
        </div>

        <!-- M · CTA DO MEIO (nota de gravacao: "COMENTA CADEIRA" na tela durante a frase), por cima do apresentador -->
        <div class="scene" id="M">
          <div class="cmt" id="M-box"><div class="hd"><i></i>COMENTA AQUI EMBAIXO</div>
            <div class="in">{CADEIRA}<span class="caret" id="M-caret"></span><span class="go" id="M-go">Publicar</span></div></div>
        </div>

        <!-- L · SPLIT DA VIRADA: a padaria de San Angelo, 1939 (as formas de torta na mesa) -->
        <div class="scene" id="L" style="height:845px"><div class="world dark"></div>
          {full('L-mesa', 'mesa', 'bw', op=OP['mesa_split'])}
        </div>

        <!-- N · A VIRADA: a moca com a torta -> a mesa cheia de formas (a propria loja) -> 3 ANOS DEPOIS: o forno -> "eu odeio fazer torta": a capa -->
        <div class="scene" id="N"><div class="world dark"></div>
          {full('N-moca', 'moca', 'bw', '<div class="floor"></div>')}
          {full('N-mesa', 'mesav', 'bw', '<div class="floor"></div>')}
          {full('N-forno', 'forno', 'bw', '<div class="floor"></div>')}
          <div class="tag" id="N-tres" style="left:90px;top:1150px;background:#11141A">3 ANOS DEPOIS</div>
          {full('N-capa', 'capa', '', '<div class="floor"></div>')}
        </div>

        <!-- C · CLIMAX: EMPRESA -> EMPREGO (as duas ultimas letras rolam) -->
        <div class="scene" id="C"><div class="world dark"><div class="band" id="C-band"></div></div>
          <div class="wsub" id="C-nao" style="top:480px">ELA NÃO ABRIU UMA</div>
          <div class="wd" id="C-wd" style="top:600px">EMPRE<span class="sl"><div id="C-roll"><span>SA</span><span class="og">GO</span></div></span></div>
          <div class="strike" id="C-x" style="left:150px;top:690px;width:780px"></div>
          <div class="wsub" id="C-abr" style="top:860px;color:#FF4A1C">ABRIU UM EMPREGO.</div>
        </div>

        <!-- G · "hoje odeia segunda-feira": a pilula vermelha sobre o apresentador -->
        <div class="scene" id="G"><div class="cnt" id="G-seg" style="top:300px"><span>SEGUNDA-FEIRA</span></div></div>

        <!-- S · "me segue": o botao de seguir sobre o apresentador -->
        <div class="scene" id="S"><div class="follow" id="S-btn">Seguir</div></div>
'''

def JS(t):
    D = t['D_dep']; DW = t['D_w']; FW = t['F_w']; HW = t['H_w']
    return f'''
          gsap.set(["#A-perto", "#P-dona", "#B-name", "#B-chat", "#B-ger2", "#B-yr", "#B-wa", "#B-dots", "#B-b1",
                    "#D-chip", "#D-w1", "#D-w2", "#D-w3", "#D-org", "#D-hdr", "#D-s0", "#D-s1", "#D-s2", "#D-s3", "#D-s4", "#D-s5",
                    "#D-y0", "#D-y1", "#D-y2", "#D-y3", "#D-y4", "#D-y5", "#D-cnt",
                    "#F-chip", "#F-w1", "#F-w2", "#F-w3", "#F-fr", "#F-g0", "#F-g1", "#F-g2", "#F-g3", "#F-g4", "#F-g5", "#F-g6", "#F-g7", "#F-g8", "#F-igual",
                    "#F-pp", "#F-vs", "#F-com", "#F-gen", "#F-ok", "#F-no",
                    "#H-chip", "#H-w1", "#H-w2", "#H-w3", "#H-ct", "#H-nm", "#H-or", "#H-o1", "#H-o2", "#H-b1", "#H-b2",
                    "#M-box", "#M-c0", "#M-c1", "#M-c2", "#M-c3", "#M-c4", "#M-c5", "#M-c6", "#M-go",
                    "#N-mesa", "#N-forno", "#N-tres", "#N-capa", "#C-nao", "#C-wd", "#C-abr", "#G-seg", "#S-btn"], {{ autoAlpha: 0 }});
          gsap.set(["#D-sel", "#F-sel", "#H-sel"], {{ borderColor: "rgba(242,183,5,0)", backgroundColor: "rgba(242,183,5,0)" }});
          gsap.set(["#D-sel .h", "#F-sel .h", "#H-sel .h"], {{ scale: 0 }});
          gsap.set(["#C-x"], {{ scaleX: 0 }});
          gsap.set(["#D-spine"], {{ scaleY: 0 }});
          gsap.set(["#F-l0", "#F-l1", "#F-l2", "#F-l3", "#F-l4"], {{ scaleX: 0 }});
          var sigLen = 1400; gsap.set("#H-sig", {{ strokeDasharray: sigLen, strokeDashoffset: sigLen }});
          function sel(base, t) {{
            tl.to("#" + base + "-sel", {{ borderColor: "rgba(242,183,5,1)", backgroundColor: "rgba(242,183,5,.16)", duration: 4 * q, ease: "none" }}, Q(t));
            tl.to("#" + base + "-sel .h", {{ scale: 1, duration: 6 * q, ease: "back.out(3)", stagger: q }}, Q(t) + q);
          }}
          function out(sel_, t) {{ tl.to(sel_, {{ scale: 0.3, autoAlpha: 0, filter: "blur(12px)", duration: 5 * q, ease: "power4.in" }}, Q(t) - 5 * q); }}
          function cap(b, tChip, tAp, ws, tSel, tOut, entra) {{
            chip(b, tChip, tAp);
            for (var k = 0; k < ws.length; k++) {{ rise("#" + b + "-w" + (k + 1), ws[k]); cue(ws[k], "tique", -24); }}
            sel(b, tSel); smear("#" + b + "-chip", tOut); out("#" + b + "-title", tOut); zoomIn(entra, tOut);
          }}

          // ===== A · CAPA (quadro 0 = capa) =====
          splitIn("#A", 0, true);
          kenburns("#A-capaimg", 0, {t['hook_copiados']:.2f}, 1.0, 1.06);
          whip("#A-capa", "#A-perto", {t['hook_copiados']:.2f});
          kenburns("#A-pertoimg", {t['hook_copiados']:.2f}, {t['P_in']:.2f}, 1.0, 1.07);
          splitOut("#A", {t['P_in']:.2f});

          // ===== P · PRÉ-REVELAÇÃO (só imagem, nada do Michael) =====
          sceneIn("#P", {t['P_in']:.2f});
          kenburns("#P-relimg", {t['P_in']:.2f}, {t['P_emprego']:.2f}, 1.0, 1.1);
          whip("#P-rel", "#P-dona", {t['P_emprego']:.2f});
          kenburns("#P-donaimg", {t['P_emprego']:.2f}, {t['P_out']:.2f}, 1.08, 1.0);
          sceneOut("#P", {t['P_out']:.2f});

          // ===== B · REVELAÇÃO ("Michael") → O SÓCIO =====
          sceneIn("#B", {t['michael']:.2f});
          kenburns("#B-gerimg", {t['michael']:.2f}, {t['B_socio']:.2f}, 1.0, 1.06);
          rise("#B-name", {t['B_nome']:.2f});
          whip(["#B-ger", "#B-name"], "#B-chat", {t['B_socio']:.2f});
          rise("#B-yr", {t['B_socio']:.2f} + 0.05);
          rise("#B-wa", {t['B_socio']:.2f} + 0.15);
          tl.fromTo("#B-dots", {{ autoAlpha: 0 }}, {{ autoAlpha: 1, duration: 3 * q }}, Q({t['B_socio']:.2f} + 0.3));
          tl.to("#B-dots i", {{ y: -14, duration: 4 * q, ease: "power1.inOut", stagger: 2 * q, yoyo: true, repeat: 3 }}, Q({t['B_socio']:.2f} + 0.35));
          tl.set("#B-dots", {{ autoAlpha: 0 }}, Q({t['B_quebrado']:.2f}));
          pop("#B-b1", {t['B_quebrado']:.2f}, {{ scale: 0.5, autoAlpha: 0, y: 30 }});
          // "E ele tava ocupado demais trabalhando pra olhar o dinheiro." (a olhada no fim do take fica coberta)
          whip("#B-chat", "#B-ger2", {t['B_ocup']:.2f});
          kenburns("#B-ger2img", {t['B_ocup']:.2f}, {t['B_out']:.2f}, 1.0, 1.08);
          sceneOut("#B", {t['B_out']:.2f});

          // ===== D · PASSO 1 → O ORGANOGRAMA =====
          sceneIn("#D", {t['D_in']:.2f}); drift("#D-band", {t['D_in']:.2f}, {t['D_out']:.2f});
          cap("D", {t['D_chip'] + 0.25:.2f}, {t['D_in']:.2f}, [{DW[0]:.2f}, {DW[1]:.2f}, {DW[2]:.2f}], {DW[2] + 0.35:.2f}, {t['D_org']:.2f}, "#D-org");
          rise("#D-hdr", {t['D_org']:.2f});
          tl.to("#D-spine", {{ scaleY: 1, duration: 10 * q, ease: "power3.out" }}, Q({t['D_org']:.2f}) + 3 * q);
          pop("#D-s0", {D[0]:.2f}); pop("#D-s1", {D[1]:.2f}); pop("#D-s2", {D[2]:.2f}); pop("#D-s3", {D[3]:.2f});
          pop("#D-s4", {D[3] + 0.35:.2f}); pop("#D-s5", {D[3] + 0.5:.2f});
          // "Ele manda escrever o seu nome em cada cadeira que é sua."
          for (var k = 0; k < 6; k++) {{
            tl.fromTo("#D-y" + k, {{ autoAlpha: 0, scale: 1.8, rotation: -14 }}, {{ autoAlpha: 1, scale: 1, rotation: -5, duration: 4 * q, ease: "power4.in" }}, Q({t['D_nome']:.2f}) + k * 5 * q);
            cue({t['D_nome']:.2f} + k * 5 / 30, "clique", -20);
          }}
          // "Seu nome tá em seis cadeiras?"
          tl.to(["#D-r0", "#D-r1", "#D-r2", "#D-r3", "#D-r4", "#D-r5"], {{ opacity: 1, duration: 3 * q, stagger: q }}, Q({t['D_seis']:.2f}));
          pop("#D-cnt", {t['D_seis']:.2f} + 0.1, {{ y: 60, autoAlpha: 0, scale: 0.7 }});
          cue({t['D_seis']:.2f} + 0.1, "impacto", -20, {{ dur: 0.5 }});
          sceneOut("#D", {t['D_out']:.2f});

          // ===== F · PASSO 2 → A FRANQUIA → O PASSO A PASSO → GENTE COMUM × GÊNIO =====
          sceneIn("#F", {t['F_in']:.2f}); drift("#F-band", {t['F_in']:.2f}, {t['F_out']:.2f});
          cap("F", {t['F_chip'] + 0.25:.2f}, {t['F_in']:.2f}, [{FW[0]:.2f}, {FW[1]:.2f}, {FW[2]:.2f}], {t['F_sel']:.2f}, {t['F_fr']:.2f}, "#F-fr");
          // "vender franquia": a loja vira nove iguais
          tl.to("#F-one", {{ scale: 0.6, autoAlpha: 0, duration: 5 * q, ease: "power3.in" }}, Q({t['F_fr'] + 0.35:.2f}));
          tl.fromTo(["#F-g4", "#F-g1", "#F-g3", "#F-g5", "#F-g7", "#F-g0", "#F-g2", "#F-g6", "#F-g8"], {{ scale: 0.3, autoAlpha: 0 }},
                    {{ scale: 1, autoAlpha: 1, duration: 8 * q, ease: "back.out(2.2)", stagger: 1.5 * q }}, Q({t['F_fr'] + 0.35:.2f}) + 2 * q);
          for (var k = 0; k < 9; k++) cue({t['F_fr'] + 0.35:.2f} + 0.07 + k * 0.05, "pop", -24, {{ f0: 700 + 60 * k }});
          rise("#F-igual", {t['F_fr'] + 0.95:.2f});
          // "Tudo que você faz de cabeça, escreve o passo a passo."
          drop(["#F-fr"], "#F-pp", {t['F_pp0']:.2f});
          tl.to(["#F-l0", "#F-l1", "#F-l2", "#F-l3", "#F-l4"], {{ scaleX: 1, duration: 8 * q, ease: "power2.out", stagger: 4 * q }}, Q({t['F_pp']:.2f}));
          for (var k = 0; k < 5; k++) cue({t['F_pp']:.2f} + k * 4 / 30, "tique", -25);
          // "gente comum, não com gênio"
          whip("#F-pp", "#F-vs", {t['F_comum'] - 0.25:.2f});
          pop("#F-com", {t['F_comum'] - 0.2:.2f}); pop("#F-ok", {t['F_comum'] + 0.25:.2f}, {{ scale: 0.3, autoAlpha: 0 }}, "clique");
          pop("#F-gen", {t['F_genio'] - 0.35:.2f}); pop("#F-no", {t['F_genio']:.2f}, {{ scale: 0.3, autoAlpha: 0 }}, "clique");
          tl.to("#F-gen", {{ opacity: 0.45, duration: 6 * q }}, Q({t['F_genio']:.2f}) + 3 * q);
          sceneOut("#F", {t['F_out']:.2f});

          // ===== H · PASSO 3 → O CONTRATO DA CADEIRA → 1º A CADEIRA, 2º A PESSOA → O SOBRINHO =====
          sceneIn("#H", {t['H_in']:.2f}); drift("#H-band", {t['H_in']:.2f}, {t['H_out']:.2f});
          cap("H", {t['H_chip'] + 0.3:.2f}, {max(t['H_in'], t['H_chip'] - 0.3):.2f}, [{HW[0]:.2f}, {HW[1]:.2f}, {HW[2]:.2f}], {HW[2] + 0.35:.2f}, {t['H_folha']:.2f}, "#H-ct");
          stagger(["#H-r1", "#H-r2", "#H-r3"], {t['H_entrega']:.2f}, 3, 3);
          tl.to("#H-sig", {{ strokeDashoffset: 0, duration: 0.9, ease: "power1.inOut" }}, Q({t['H_assina']:.2f}));
          cue({t['H_assina']:.2f}, "swish", -21);
          pop("#H-nm", {t['H_func']:.2f}, {{ y: 30, autoAlpha: 0 }});
          // "primeiro a cadeira, depois a pessoa."
          whip("#H-ct", "#H-or", {t['H_ordem'] - 0.15:.2f});
          pop("#H-o1", {t['H_ordem']:.2f}, {{ x: -120, autoAlpha: 0 }});
          pop("#H-o2", {t['H_pessoa']:.2f}, {{ x: -120, autoAlpha: 0 }});
          // "Na sua, primeiro veio o sobrinho. Depois inventaram a cadeira."
          tl.to("#H-a1", {{ y: -190, autoAlpha: 0, duration: 6 * q, ease: "power3.in" }}, Q({t['H_sobrinho']:.2f}) - 2 * q);
          tl.fromTo("#H-b1", {{ y: 190, autoAlpha: 0 }}, {{ y: 0, autoAlpha: 1, immediateRender: false, duration: 8 * q, ease: "expo.out" }}, Q({t['H_sobrinho']:.2f}) + 2 * q);
          cue({t['H_sobrinho']:.2f}, "clique", -19);
          tl.to("#H-a2", {{ y: -190, autoAlpha: 0, duration: 6 * q, ease: "power3.in" }}, Q({t['H_sobrinho'] + 0.15:.2f}) - 2 * q);
          tl.fromTo("#H-b2", {{ y: 190, autoAlpha: 0 }}, {{ y: 0, autoAlpha: 1, immediateRender: false, duration: 8 * q, ease: "expo.out" }}, Q({t['H_sobrinho'] + 0.15:.2f}) + 2 * q);
          cue({t['H_sobrinho'] + 0.15:.2f}, "clique", -19);
          sceneOut("#H", {t['H_out']:.2f});

          // ===== M · COMENTA CADEIRA (por cima do apresentador) =====
          tl.set("#M", {{ autoAlpha: 1 }}, Q({t['M_in']:.2f}));
          pop("#M-box", {t['M_in']:.2f}, {{ y: -60, autoAlpha: 0, scale: 0.92 }});
          for (var k = 0; k < 7; k++) {{ tl.set("#M-c" + k, {{ autoAlpha: 1 }}, Q({t['M_cad']:.2f}) + k * 2 * q); cue({t['M_cad']:.2f} + k * 2 / 30, "tique", -23); }}
          tl.to("#M-caret", {{ opacity: 0, duration: 2 * q, yoyo: true, repeat: 9, ease: "steps(1)" }}, Q({t['M_cad']:.2f}) + 14 * q);
          pop("#M-go", {t['M_cad']:.2f} + 0.55, {{ scale: 0.4, autoAlpha: 0 }}, "clique");
          tl.to("#M-box", {{ autoAlpha: 0, y: -40, duration: 6 * q, ease: "power3.in" }}, Q({t['M_out']:.2f}) - 6 * q);
          tl.set("#M", {{ autoAlpha: 0 }}, Q({t['M_out']:.2f}));

          // ===== L · SPLIT DA VIRADA =====
          splitIn("#L", {t['L_in']:.2f});
          kenburns("#L-mesaimg", {t['L_in']:.2f}, {t['L_out']:.2f}, 1.0, 1.08);
          splitOut("#L", {t['L_out']:.2f});

          // ===== N · A VIRADA =====
          sceneIn("#N", {t['N_in']:.2f});
          kenburns("#N-mocaimg", {t['N_in']:.2f}, {t['N_loja']:.2f}, 1.0, 1.06);
          whip("#N-moca", "#N-mesa", {t['N_loja']:.2f});
          kenburns("#N-mesaimg", {t['N_loja']:.2f}, {t['N_tres']:.2f}, 1.08, 1.0);
          drop(["#N-mesa"], "#N-forno", {t['N_tres']:.2f});
          pop("#N-tres", {t['N_tres']:.2f} + 0.1);
          kenburns("#N-fornoimg", {t['N_tres']:.2f}, {t['N_odeio']:.2f}, 1.0, 1.08);
          whip(["#N-forno", "#N-tres"], "#N-capa", {t['N_odeio']:.2f});
          kenburns("#N-capaimg", {t['N_odeio']:.2f}, {t['N_out']:.2f}, 1.0, 1.16);
          sceneOut("#N", {t['N_out']:.2f});

          // ===== C · CLÍMAX: EMPRESA → EMPREGO =====
          sceneIn("#C", {t['C_in']:.2f}); drift("#C-band", {t['C_in']:.2f}, {t['C_out']:.2f});
          rise("#C-nao", {t['C_nao']:.2f});
          pop("#C-wd", {t['C_empresa']:.2f}, {{ scale: 0.7, autoAlpha: 0 }});
          tl.to("#C-x", {{ scaleX: 1, duration: 6 * q, ease: "power3.out" }}, Q({t['C_empresa']:.2f}) + 8 * q);
          cue({t['C_empresa']:.2f} + 8 / 30, "swish", -19);
          tl.to("#C-x", {{ autoAlpha: 0, duration: 3 * q }}, Q({t['C_emprego']:.2f}) - 3 * q);
          tl.to("#C-roll", {{ y: -186, duration: 10 * q, ease: "power4.out" }}, Q({t['C_emprego']:.2f}) - 2 * q);
          cue({t['C_emprego']:.2f}, "cacaniquel", -19);
          tl.fromTo("#C-wd", {{ scale: 1 }}, {{ scale: 1.06, duration: 4 * q, ease: "power2.out", yoyo: true, repeat: 1 }}, Q({t['C_emprego']:.2f}) + 6 * q);
          rise("#C-abr", {t['C_emprego']:.2f} + 0.15);
          sceneOut("#C", {t['C_out']:.2f});

          // ===== G · SEGUNDA-FEIRA =====
          tl.set("#G", {{ autoAlpha: 1 }}, Q({t['G_seg'] - 0.1:.2f}));
          pop("#G-seg", {t['G_seg']:.2f}, {{ scale: 0.4, autoAlpha: 0, y: -30, rotation: -6 }});
          tl.to("#G-seg", {{ autoAlpha: 0, y: -40, duration: 6 * q, ease: "power3.in" }}, Q({t['G_out']:.2f}) - 6 * q);
          tl.set("#G", {{ autoAlpha: 0 }}, Q({t['G_out']:.2f}));

          // ===== S · "me segue" =====
          tl.set("#S", {{ autoAlpha: 1 }}, Q({t['S_segue'] - 0.1:.2f}));
          pop("#S-btn", {t['S_segue']:.2f}, {{ scale: 0.4, autoAlpha: 0, y: 40 }});
          tl.fromTo("#S-btn", {{ scale: 1 }}, {{ scale: 0.94, duration: 3 * q, ease: "power2.out", yoyo: true, repeat: 1 }}, Q({t['S_segue'] + 0.9:.2f}));
          cue({t['S_segue'] + 0.92:.2f}, "clique", -20);
          tl.to("#S-btn", {{ autoAlpha: 0, y: -40, duration: 6 * q, ease: "power3.in" }}, Q({t['S_out']:.2f}) - 6 * q);
          tl.set("#S", {{ autoAlpha: 0 }}, Q({t['S_out']:.2f}));
'''

Tt = T_.replace('            </style>', CSS + '            </style>', 1)
i = Tt.index('-->', Tt.index('CENAS (por video)')) + 3
Tt = Tt[:i] + HTML + Tt[i:]
Tt = Tt.replace('          // (vazio = camada transparente)', JS(t), 1)
open('compositions/mg.html', 'w').write(Tt)
print('compositions/mg.html', len(Tt), 'bytes')
