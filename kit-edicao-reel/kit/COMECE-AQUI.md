# COMECE AQUI — levar a edição de reels para outro computador

Esta pasta é **toda a inteligência** da edição: o formato (números, regras, erros já pagos em 33 reels), os scripts,
o modelo de projeto, a trilha, os SFX, as fontes, os exemplos (Deming é o mais recente e o padrão atual) e as skills
que ensinam o Claude a usar tudo isso. O Claude no outro computador lê esta pasta e edita igual.

## O que precisa no outro computador
- **Mac com Apple Silicon** (M1/M2/M3/M4). 16 GB de RAM é o ideal; 8 GB funciona, mais devagar (ver docs/09).
- **≥ 15 GB livres** (ferramentas + modelo do Whisper + render).
- **Claude Code** — o app Claude (aba Code) ou o `claude` no Terminal, logado na sua conta.
- **Google Chrome** instalado (o render usa).
- Opcional: **Codex CLI** logado na conta ChatGPT (só para gerar a capa com IA).

## Instalar (uma vez, ~15 min)
1. Copie a pasta `KIT-EDICAO-REEL` para o outro Mac (pendrive, AirDrop, Drive — tanto faz onde).
2. Se o Mac ainda não tem o Homebrew, instale pelo comando de https://brew.sh (ele pede a senha do Mac).
3. No Terminal, rode (arraste o `instalar.sh` para a janela do Terminal no lugar do caminho):
   ```
   zsh /caminho/para/KIT-EDICAO-REEL/instalar.sh
   ```
   Ele instala ffmpeg, whisper, node e Python 3.12; copia o kit para `~/Claude/KIT-EDICAO-REEL`; cria o Python do kit;
   baixa o modelo do Whisper (1,6 GB); instala as skills no Claude Code e, no fim, **confere tudo e reconstrói um reel
   de teste**. Tem que terminar com `0 falha(s)`.
4. Feche e abra o Claude Code para ele enxergar as skills novas.

## Usar
1. Coloque o vídeo bruto em `~/Claude/videos-brutos/` (ou em qualquer lugar — você passa o caminho).
2. Abra o Claude Code na pasta `~/Claude` e mande o prompt (modelo em `docs/04-prompt-comando-unico.md`):
   ```
   Edita o reel do [TEMA] com o bruto [CAMINHO DO BRUTO] e este roteiro:
   [ROTEIRO]

   Segue o fluxo rápido do kit (~/Claude/KIT-EDICAO-REEL/docs/14-fluxo-rapido.md): formato do kit + camada de
   motion graphics da skill showreel-interface, na dosagem do reel Deming v2: abertura só com fotos, no corpo foto
   real como padrão e motion só onde conta a história. Comando único, sem parada: pesquisa as imagens na fonte
   primária pelo navegador, gera a capa no Codex com esta cena: [CENA], monta, confere quadro a quadro e me manda o
   MP4 aqui no chat.
   ```
3. Em ~1 h o MP4 chega no chat. Para ajustar, é só pedir ("menos motion", "troca a foto do minuto 0:30"…).

## Onde está cada coisa
| | |
|---|---|
| `docs/14-fluxo-rapido.md` | o fluxo padrão, comando a comando |
| `docs/05-calibracoes-e-armadilhas.md` | **o mais importante**: todos os números e erros já pagos (§24 = dosagem de imagem × motion) |
| `docs/13-camada-motion.md` | como a camada de motion é feita |
| `exemplos/deming/` | o último reel aprovado: gerador da camada (`gen.py`; `gen-v1.py` = versão com motion demais), plano, cortes, legendas |
| `modelo-projeto/` | o esqueleto que todo reel novo copia |
| `assets-fixos/` | trilha, SFX, light-leak, fontes, modelo de rosto |
| `skill/` | as skills que o `instalar.sh` coloca no Claude Code |

## O que NÃO vai nesta pasta (de propósito)
- Chaves de API (`~/Claude/reel-auto/.env`). O fluxo padrão não precisa delas.
- O modelo do Whisper (o `instalar.sh` baixa).
- Vídeos brutos e projetos renderizados (pesados; o kit não depende deles).
- Logins (Codex, Claude) — cada computador faz o seu.

## Manter os dois computadores iguais
O kit é um repositório git. Quando um reel ensinar algo novo, o Claude grava em `docs/05` e dá commit. Para levar a
versão nova ao outro Mac, copie a pasta de novo e rode o `instalar.sh` (ele guarda a versão antiga com outro nome).
