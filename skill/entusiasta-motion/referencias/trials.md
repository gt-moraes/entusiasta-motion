# Trial reels: variações de gancho do vídeo aprovado

Trial reel é a versão do Reels que o Instagram mostra só pra quem não segue o perfil. A ideia: soltar várias versões do MESMO vídeo, cada uma com um começo diferente, e a que performar melhor vai pro perfil. Usado pela primeira vez num vídeo de vitrine dos 17 estilos (21/10/2026).

## Quando entra no fluxo

Depois que o criador APROVA a edição. Nunca antes: a variação herda tudo do vídeo aprovado, então mexer no corpo depois obriga a refazer as variações.

Pergunta padrão: **"Edição aprovada. Quer as variações pra trial reels?"** Se ele já pediu ("faz as versões de teste", "muda o gancho de cada uma"), não perguntar de novo: fazer.

## A regra que não muda

- **Só os primeiros ~3 s mudam.** Do primeiro item/fala do corpo em diante, é o vídeo aprovado quadro a quadro. Se mudar o corpo, o teste deixa de medir o gancho.
- **Uma hipótese por versão**, escrita no `trials.md` da pasta. Duas versões testando a mesma coisa não ensinam nada.
- **Padrão: 5 versões.** De 4 a 6 funciona.
- O vídeo aprovado não entra como trial: ele é o controle e vai pro perfil.
- Postar é sempre do criador. A skill só gera arquivo.

## Banco de ganchos (escolher 5 que o bruto aguenta)

| gancho | como faz | o que testa | precisa |
|---|---|---|---|
| **frase forte de outro trecho** | puxa pra frente a frase mais provocativa do vídeo (ex.: "Nenhum desses efeitos foi feito com o editor", que estava no CTA) e tira ela do lugar original | provocação × anúncio | uma frase que se sustente sozinha |
| **montagem** | tela cheia em corte rápido (5 frames cada) das peças do vídeo, título branco sobre escurecimento no topo, contador | movimento no primeiro quadro | material visual próprio (previews, telas) |
| **zoom com número** | punch-in de ~1,3 no rosto, número gigante na cor de destaque + 2-3 palavras | rosto perto + número | número na primeira fala |
| **pergunta na tela** | texto de pergunta no lugar do título ("qual desses tu usaria primeiro?"), fala normal por baixo | comentário | assunto com escolha |
| **direto no conteúdo** | corta a frase de abertura; começa no primeiro item com título e peças já na tela | ritmo desde o frame 0 | corpo que se entende sem introdução |
| **outro take** | usa um take descartado do gancho (se tiver um bom) | entrega da fala | retake aproveitável no bruto |
| **estilo do banco no gancho** | aplica um dos 17 estilos (`estilos.md`) só no gancho: 16 cover story, 17 glasstype, 04 frame break | efeito visual × câmera limpa | a gravação aguentar o estilo |
| **capa/legenda** | mesma abertura, outra capa e outra primeira linha de legenda | clique no feed | nada além do vídeo |

Evitar duas versões com a mesma mecânica (ex.: duas de texto na tela com a câmera parada).

## Como montar no estúdio

- `studio/src/edicao/variacoes.ts`: `reordena(ed, ordem)` monta a edição na ordem nova (puxar frase pra frente, cortar a abertura) e `posicao(ordem, original)` traduz o índice ORIGINAL da fala pro novo, pra `momento()` continuar recebendo o índice do json.
- Transformar a composição aprovada numa **fábrica** `fabrica(gancho, ordem)` que devolve `{Comp, duracao}`; a aprovada é `fabrica('aprovado', todas(n))` e precisa continuar idêntica (conferir um still lado a lado antes e depois).
- Registrar `<Id>Trial1Editado` ... no `Root.tsx` (o "Editado" no id faz o `render.sh` sair .mp4).
- Conferir com uma folha só dos primeiros 4 s de cada versão (`folha.sh <Id> <png> 8 30 55 80 100 125`), render um por vez, `loudnorm` em -14 LUFS, decode inteiro.

## Entrega

- `<pasta de entrega do perfil.md>/trials/trial-0N-<gancho>.mp4`
- `trials.md` na mesma pasta: tabela `trial | gancho | hipótese`, pra anotar o resultado depois de postar.
- Render leva ~5 min por versão nesta máquina; a montagem é a mais pesada (muitos vídeos por segundo).
