# Reel "por que eu sou assim?" — 15 s sobre o YouTube · @dra.jessicamartani

**Brief:** marca = YouTube (UI nativa, modo escuro e claro) · canal = BRILHANTEMENTE dra.Jéssica Martani
(@dra.jessicamartani, dados públicos coletados em 02/10/2026) · 15,0 s · 1920×1080 · 30 fps · PT-BR ·
CTA = Inscrever-se.

**As três respostas (§0 da skill showreel-interface):**
- **Chip** = os átomos reais do canal: os chips de filtro ("Mais recentes", "Em alta", "Mais antigos") e as
  abas do canal ("Vídeos" → "Shorts").
- **Prova** = o conteúdo real do canal: capas dos vídeos mais vistos, 72 capas de Shorts reais, o contador
  **359 vídeos** e **2,16 mil inscritos** (cabeçalho do canal em 02/10/2026).
- **Frase do começo → fim**: a pergunta digitada na busca, "por que eu sou assim?", é respondida por
  "A psiquiatra explica." e fecha no imperativo "Aperte o play." + Inscrever-se → Inscrito.

**Mecanismo:** a interface do YouTube conta a história. Alguém digita a própria dúvida na busca, a
psiquiatra responde com o acervo do canal, a pessoa maratona ("só mais um vídeo…") e se inscreve.

**Grade:** 120 BPM · 1 tempo = 0,5 s = 15 q · compasso = 2 s = 60 q · drop = 3.1 = 4,00 s.

| Frame | Janela | Mundo | O que acontece | Enquadramento | Emenda de saída |
|---|---|---|---|---|---|
| **f01-busca** | 0,00–2,10 | escuro | logo YouTube (110 px) + busca; push 2× para o close; digita **por · que · eu · sou · assim?** (0,50/0,75/1,00/1,25/1,375); a barra de progresso corre sob "assim?" | UI em close | **T1 zoom-through em 2,00** pela palavra "assim?" |
| **f02-porque** | 1,90–4,00 | escuro | "A psiquiatra explica." assenta; chips entram; a roleta trava em **Em alta** no clique de 3,00; baralho 3D com as capas mais vistas | tipografia → leque 3D | **T3**: a capa da frente ("É possível não sentir nada?") vira a tela cheia **no drop (4,00)** |
| **f03-player** | 4,00–6,00 | footage | player do YouTube; cortes duros na grade 4,00 · 4,50 · 5,00 · 5,25 · 5,50, cada um com título e duração reais | tela cheia | cromo some; **T4 em 6,00** |
| **f04-shorts** | 6,00–10,00 | claro | a tela cheia vira card na aba **Vídeos / Em alta** (títulos, visualizações e datas reais); clique na aba **Shorts** (7,00): as colunas rolam como caça-níquel e os Shorts 9:16 entram; **8,00** a câmera recua para a parede de Shorts e o contador soca **359 vídeos** | grade → parede de 9:16 | **T6 chicote** em 9,77–10,00 |
| **f05-so-mais-um** | 10,00–12,00 | escuro | "só mais um vídeo…" + card nativo **A seguir** ("Os SEGREDOS Ocultos Sobre a Insônia"), música abafada | tipografia | encolhe → **T8 soco em 12,00** |
| **f06-aperte** | 12,00–15,00 | escuro | **"Aperte o play."** soca com a barra cheia; cabeçalho real do canal; Inscrever-se → **Inscrito** + sino (13,30); assinatura **ícone + /@dra.jessicamartani** | cabeçalho do canal | fim |

## Pendências (ver o relatório final)
- **Trechos de vídeo**: o YouTube bloqueou o download neste ambiente ("confirme que não é um robô").
  O beat do player usa as capas reais. Para trocar por vídeo: em `compositions/frames/03-player.html`,
  troque cada `<img id="f03-vN">` por `<video … data-start data-duration data-media-start muted>`.
- **Trilha**: gerada localmente (MusicGen, sem licença de terceiros), esticada para 120 BPM. Se quiser
  outra, troque `assets/audio/trilha-base-120.wav` e rode de novo o `sfx.py mix`.
- **Uso de marca**: as diretrizes do YouTube pedem aprovação (Brand Use Request Form) para usar logo e
  elementos de UI em mídia, e o vídeo não pode sugerir parceria ou endosso.
