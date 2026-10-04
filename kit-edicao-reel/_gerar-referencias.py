#!/usr/bin/env python3
"""Regenera os arquivos 2 a 5 desta pasta a partir do kit (~/Claude/KIT-EDICAO-REEL).
Os arquivos 0 e 1 são escritos à mão e não são tocados. NÃO subir este script no projeto.
uso: python3 _gerar-referencias.py
"""
import glob, os, subprocess, datetime

KIT = os.path.expanduser("~/Claude/KIT-EDICAO-REEL")
OUT = os.path.dirname(os.path.abspath(__file__))
LANG = {".py": "python", ".mjs": "javascript", ".sh": "bash", ".json": "json", ".html": "html",
        ".txt": "text", ".css": "css"}


def versao():
    try:
        h = subprocess.check_output(["git", "-C", KIT, "log", "-1", "--format=%h · %s"], text=True).strip()
    except Exception:
        h = "sem git"
    return f"kit em {h} · gerado em {datetime.date.today().isoformat()}"


def expandir(itens):
    """Cada item é um caminho relativo ao kit (aceita glob). Devolve a lista ordenada, sem repetição."""
    vistos, saida = set(), []
    for it in itens:
        achados = sorted(glob.glob(os.path.join(KIT, it))) if any(c in it for c in "*?[") else [os.path.join(KIT, it)]
        for p in achados:
            p = os.path.normpath(p)
            if os.path.isfile(p) and p not in vistos:
                vistos.add(p); saida.append(p)
    return saida


def bloco(p):
    rel = os.path.relpath(p, os.path.dirname(KIT)) if not p.startswith(KIT) else os.path.relpath(p, KIT)
    txt = open(p, encoding="utf-8", errors="replace").read().rstrip("\n")
    ext = os.path.splitext(p)[1]
    cab = f"\n\n---\n\n# ARQUIVO: `{rel}`\n\n"
    if ext == ".md":
        return rel, cab + txt + "\n"
    cerca = "````" if "```" in txt else "```"
    return rel, cab + f"{cerca}{LANG.get(ext, '')}\n{txt}\n{cerca}\n"


def gravar(nome, titulo, intro, itens):
    arquivos = expandir(itens)
    blocos = [bloco(p) for p in arquivos]
    indice = "\n".join(f"- `{rel}`" for rel, _ in blocos)
    corpo = f"# {titulo}\n\n{intro}\n\n_{versao()}_\n\n## Índice\n\n{indice}\n" + "".join(b for _, b in blocos)
    open(os.path.join(OUT, nome), "w", encoding="utf-8").write(corpo)
    print(f"{nome:45s} {len(blocos):3d} arquivos  {len(corpo):7d} caracteres  ~{len(corpo) // 3300:3d} mil tokens")


gravar("2-REFERENCIA-DOCS-DO-KIT.md", "Referência — os docs do kit, na íntegra",
       "Cópia fiel dos documentos do `KIT-EDICAO-REEL`, na ordem de leitura do kit. Cada bloco começa com "
       "`# ARQUIVO: <caminho>`. Entre docs que se contradizem vale o mais novo: `docs/14` e `docs/05` §23–24 "
       "(o resumo coerente está em `1-MANUAL-DO-FORMATO.md`).",
       ["README.md", "docs/14-fluxo-rapido.md", "docs/05-calibracoes-e-armadilhas.md", "docs/13-camada-motion.md",
        "docs/01-pipeline-hyperframes.md", "docs/02-jcut-algoritmo.md", "docs/06-checklist-execucao.md",
        "docs/10-scripts.md", "docs/11-pesquisa-broll.md", "docs/12-export-em-partes.md",
        "docs/04-prompt-comando-unico.md", "docs/07-mapa-de-arquivos.md", "docs/09-instalacao-outra-maquina.md",
        "COMECE-AQUI.md", "VERSAO.md", "skill/edicao-reel-viral/SKILL.md", "modelo-projeto/EDICAO.md",
        "../ESTILO-DE-EDICAO.md", "docs/03-blueprint-casas-bahia.md", "docs/08-storyboard-opcional.md"])

gravar("3-CODIGO-DO-MOTOR.md", "Código do motor — `modelo-projeto/` na íntegra",
       "O esqueleto que todo reel novo copia: template da composição, biblioteca da camada de motion, plano-"
       "esqueleto e todos os scripts. Catálogo (MOTOR × POR VÍDEO) em `docs/10-scripts.md`. Os scripts POR VÍDEO "
       "trazem dados de outro reel como exemplo.",
       ["novo-projeto.sh", "instalar.sh", "verificar-instalacao.sh",
        "modelo-projeto/CLAUDE.md", "modelo-projeto/package.json", "modelo-projeto/hyperframes.json",
        "modelo-projeto/meta.json", "modelo-projeto/assets/edit-plan.json", "modelo-projeto/index.html",
        "modelo-projeto/compositions/mg.html",
        "modelo-projeto/scripts/fase1.sh", "modelo-projeto/scripts/fase2.sh", "modelo-projeto/scripts/legendas.sh",
        "modelo-projeto/scripts/montar.sh", "modelo-projeto/scripts/render-par.sh",
        "modelo-projeto/scripts/build-edit.mjs", "modelo-projeto/scripts/bake.py",
        "modelo-projeto/scripts/render-chunks.mjs", "modelo-projeto/scripts/finalizar.py",
        "modelo-projeto/scripts/*", "modelo-projeto/work/*", "modelo-projeto/work/pesq/*"])

S = "skill/showreel-interface/"
gravar("4-CAMADA-MOTION-showreel-interface.md", "Camada de motion — skill `showreel-interface`",
       "O método de design e movimento usado na camada `compositions/mg.html`: a skill, as referências e os "
       "scripts (o `mg_sfx.py` do kit depende do `sfx.py`). Ficaram de fora o exemplo `youtube-15s` e o "
       "`INSTALAR.md` (instalador gerado).",
       [S + "SKILL.md", S + "referencias/transicoes.md", S + "referencias/componentes.md",
        S + "referencias/ritmo-e-audio.md", S + "referencias/traducao-de-marca.md",
        S + "referencias/pericia-showreel-2025.md", S + "referencias/caso-youtube.md",
        S + "referencias/pericia/movimento.json", S + "scripts/sfx.py", S + "scripts/batida.py",
        S + "scripts/aceite.py", S + "scripts/grade.py", S + "scripts/harness.html", S + "scripts/shoot.sh"])

D, A = "exemplos/deming/", "exemplos/alan-mulally/"
gravar("5-EXEMPLOS-DEMING-E-MULALLY.md", "Exemplos — reels Deming (padrão atual) e Alan Mulally",
       "Dois reels reais como molde de preenchimento. **Deming v2** é o padrão atual (dosagem foto × motion; "
       "camada gerada por `gen.py`). **Alan Mulally** tem o `mg.html` escrito à mão, com o markup de todas as "
       "peças da biblioteca. Ficaram de fora o `mg.html` gerado do Deming e o `gen-v1.py` (versão reprovada por "
       "excesso de motion).",
       [D + "EDICAO.md", D + "LICENCAS-FOTOS.txt", D + "regioes.txt", D + "scripts/mkcut.py", D + "scripts/cuts.py",
        D + "scripts/bipe.py", D + "chunks.txt", D + "scripts/captions_fix_table.py", D + "tl-words.txt",
        D + "assets/edit-plan.json", D + "scripts/slots.py", D + "assets/broll-slots.json", D + "gen.py",
        A + "EDICAO.md", A + "mg.html", A + "scripts/mg_sfx.py", A + "scripts/slots.py",
        A + "PESQUISAS-BROLL-ALAN-MULALLY.md"])

for f in ("0-INSTRUCOES-DO-PROJETO.md", "1-MANUAL-DO-FORMATO.md"):
    n = os.path.getsize(os.path.join(OUT, f))
    print(f"{f:45s}  (à mão)    {n:7d} bytes       ~{n // 3500:3d} mil tokens")
