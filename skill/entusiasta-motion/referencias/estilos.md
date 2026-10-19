# Banco de estilos de edição

Catálogo dos 17 estilos que a skill oferece ao criador antes de editar. Fonte: os 17 efeitos do Reels do @tenfoldmarc (15/10/2026), recriados no estúdio e testados um a um.

- **Fichas completas** (o que se vê, movimento, gravação, receita): no workspace de conteúdo do criador (no do autor, `conteudo/instagram/banco de insumos/estilos-de-edicao/fichas/NN-nome.md`). Quem não tem as fichas usa esta tabela e a referência original.
- **Teste de cada estilo:** `.../estilos-de-edicao/testes/NN-nome/NN-nome [REVISAO].mp4`, com `NOTAS.md`.
- **Código:** `studio/src/acervo/estilos/NN-nome/Estilo*.tsx`, registrado no `Root.tsx`, no acervo local de quem gravou os testes (as composições usam recorte e quadros com o rosto do criador, então ainda não estão neste repositório). Ponto de partida, não peça pronta: cada vídeo adapta posição, texto e tempo à fala.
- **Status de todos:** testado tecnicamente, sem aprovação estética individual. O criador mantém os 17 no banco e vai dizendo o que gosta e o que não gosta; registrar isso no `MEMORY.md` e na coluna "notas do criador" abaixo.

## A ideia que orienta o banco

Estilo aqui é **efeito de momento**, não tema do vídeo inteiro. Cada um entra num trecho específico da fala (o gancho, um número, um item de lista, uma explicação de tela) e o vídeo volta pra câmera depois. Um Reels bom combina vários. Exemplo aprovado: Reels 13 especial (ver o fim deste arquivo).

## Os 17, em uma linha cada (é esta lista que vai na pergunta)

| Nº | Estilo | O que aparece | Bom pra |
|---|---|---|---|
| 01 | orbit | cartões de vídeo girando em volta do corpo, passando atrás e na frente | gancho, vitrine de repertório |
| 02 | couch wall | parede de miniaturas subindo atrás da pessoa, título enorme; variante **ranking** (cartões numerados acendendo) | portfólio, prova social, ranking |
| 03 | ui world | metade de cima vira interface (upload, prompt digitando) e a cabeça avança sobre ela | processo, fluxo de produto |
| 04 | frame break | o vídeo vira um cartão de post e a cabeça escapa pela borda | gancho, destaque de um item |
| 05 | digital zoom | punch-in no rosto + duas palavras grandes no topo | ênfase de uma frase ou número |
| 06 | phone mockup | celular flutuando ao lado do rosto, com app e toque | mostrar ação num aplicativo |
| 07 | checklist | lista com checks acendendo acima da cabeça | passos, processo, progresso |
| 08 | headline wall | parede de manchetes e busca atrás da pessoa | gancho de notícia, tese sustentada por manchetes |
| 09 | zoom-through cut | transição por zoom e borrão entre dois takes | troca de assunto, esconder corte |
| 10 | chart grow | gráfico crescendo acima da cabeça | número, crescimento, comparação |
| 11 | pull-back reveal | o próprio vídeo encolhe numa janela de app ou editor, com painel de progresso | bastidor, "olha o que eu fiz", fechamento de bloco |
| 12 | green screen | a sala some e a pessoa fica recortada sobre uma tela, cartão ou interface | explicar uma tela, item de lista com cartão |
| 13 | paper cut | colagem de papel: pessoa com borda branca, número montado | gancho com número, tom lúdico |
| 14 | doodle boil | contorno e rabiscos de giz vibrando em volta do corpo | gancho lúdico, ênfase leve |
| 15 | vertigo | dolly zoom: o fundo estica e a pessoa fica parada | tensão numa afirmação forte |
| 16 | cover story | capa de revista, título serifado gigante atrás da cabeça | gancho editorial, abertura de tema |
| 17 | glasstype | palavra de vidro 3D transparente sobre o quadro | gancho, palavra-chave com peso |

## Ficha técnica rápida (pra decidir se o trecho aguenta o estilo)

| Nº | Estilo | Tela dividida? | Recorte da pessoa | O que a gravação precisa | Composição | Notas do criador |
|---|---|---|---|---|---|---|
| 01 | orbit | não, câmera cheia | sim, pra passar atrás | câmera parada, espaço nas laterais do tronco | `EstiloOrbit` | |
| 02 | couch wall | não | sim | área livre atrás da cabeça | `EstiloCouchWall` | Reels 13 v1 usou a variante ranking e ele reclamou (imagem lavada e borrão preto no recorte, causa técnica, ver CLAUDE.md); [hipótese] não é reprovação do estilo em si |
| 03 | ui world | não (é uma divisão própria, a cabeça invade a interface) | cabeça e ombros | pessoa no terço de baixo, espaço acima | `EstiloUiWorld` | |
| 04 | frame break | não | sim | folga em volta da cabeça | `EstiloFrameBreak` | usado no Reels 13 especial |
| 05 | digital zoom | funciona nos dois | não | plano um pouco mais aberto, resolução sobrando | `EstiloDigitalZoom` | usado no Reels 13 especial |
| 06 | phone mockup | não | não | pessoa deslocada pra esquerda | `EstiloPhoneMockup` | |
| 07 | checklist | funciona nos dois (no split, a lista vai no painel) | não | área livre acima da cabeça | `EstiloChecklist` | |
| 08 | headline wall | não | cabeça e ombros | espaço de parede atrás | `EstiloHeadlineWall` | |
| 09 | zoom-through cut | funciona nos dois | não | rosto no mesmo eixo nos dois takes | `EstiloZoomThrough` | sem whoosh: SFX só `ui-*` |
| 10 | chart grow | funciona nos dois (no split, o gráfico vai no painel) | opcional | espaço acima | `EstiloChartGrow` | |
| 11 | pull-back reveal | não | não | take fixo | `EstiloPullBack` | usado no Reels 13 especial |
| 12 | green screen | não | sim | câmera fixa, boa separação do fundo | `EstiloGreenScreen` | base do Reels 13 v2 e do especial |
| 13 | paper cut | não | sim, com borda branca | plano aberto | `EstiloPaperCut` | |
| 14 | doodle boil | não | silhueta | plano aberto, corpo com folga | `EstiloDoodleBoil` | |
| 15 | vertigo | não | sim | fundo com profundidade; placa limpa da sala ajuda | `EstiloVertigo` | versão digital; dolly real exige gravação própria |
| 16 | cover story | não | cabeça | espaço acima da cabeça | `EstiloCoverStory` | usado no gancho do Reels 13 especial |
| 17 | glasstype | não | opcional | fundo com detalhe pra transparência aparecer | `EstiloGlasstype` | |

Regra prática: com **tela dividida**, o motion mora no painel de cima, então só 05, 07, 09 e 10 cabem sem desmontar o padrão (ou um `<TelaCheia>` pontual). **Sem tela dividida** (`ReelsCheio`), todos cabem, e é aí que o criador costuma pedir mais estilos.

## Sinal na fala → estilo sugerido

Usar pra montar as sugestões por trecho. Sugestão é ponto de partida; quem decide é o criador.

| Sinal no trecho | Sugestões, na ordem |
|---|---|
| gancho (primeiros ~3-7 s) | 16 cover story, 17 glasstype, 04 frame break, 01 orbit, 15 vertigo, 08 headline wall (se for notícia) |
| número forte, valor, porcentagem | 05 digital zoom, 10 chart grow, 13 paper cut |
| crescimento ou comparação no tempo | 10 chart grow |
| lista, ranking, "três coisas" | 12 green screen (um cartão por item), 07 checklist, 02 couch wall variante ranking |
| passo a passo, processo | 07 checklist, 03 ui world |
| "abre o app", "clica", ação no celular | 06 phone mockup |
| ferramenta no computador, prompt, upload | 03 ui world, 12 green screen sobre a interface |
| notícia, manchete, "saiu que" | 08 headline wall, 12 green screen com cartão de notícia |
| bastidor, "fiz isso", "olha o resultado", fechamento de bloco | 11 pull-back reveal |
| afirmação tensa, virada, "e aí vem o pior" | 15 vertigo, 05 digital zoom forte |
| mudança de assunto entre takes | 09 zoom-through cut |
| portfólio, repertório, "já fiz vários" | 01 orbit, 02 couch wall |
| tom de brincadeira | 14 doodle boil, 13 paper cut |

Evitar o mesmo estilo em dois trechos seguidos, salvo série (um cartão por item de lista). Depois de cada efeito, voltar à câmera cheia antes do próximo: o respiro é o que faz o efeito aparecer.

Antes de sugerir, conferir no quadro do trecho se a gravação aguenta: espaço acima da cabeça, mãos cortadas, rosto colado na borda. Se não aguenta, dizer e sugerir o próximo da lista.

## Modelo da pergunta ao criador

Mandar depois de assistir o bruto e antes do script de motion. Duas perguntas, sempre com a lista dos 17 (ele não decora os nomes).

```
Assisti o bruto (NN s, X trechos). Duas perguntas antes de montar o script:

1) Tela dividida (motion em cima, câmera embaixo, o padrão) ou câmera cheia com efeitos por trecho?

2) Quais estilos aplicar? Minhas sugestões por trecho:

| tempo | fala | sugestão | por quê |
|---|---|---|---|
| 0,0-5,2 | "..." | 16 cover story | gancho editorial, tem espaço acima da cabeça |
| 12,4-18,0 | "..." | 05 digital zoom | número forte na fala |
| ... | ... | ... | ... |

Lembrete dos 17:
01 orbit: cartões girando em volta do corpo
02 couch wall: parede de miniaturas atrás (ou ranking)
03 ui world: interface em cima, cabeça invade
04 frame break: vídeo vira post, cabeça escapa da borda
05 digital zoom: punch-in + 2 palavras grandes
06 phone mockup: celular flutuando com app
07 checklist: lista com checks acima da cabeça
08 headline wall: parede de manchetes atrás
09 zoom-through cut: transição por zoom entre takes
10 chart grow: gráfico crescendo
11 pull-back reveal: o vídeo encolhe numa janela de app
12 green screen: sala some, pessoa sobre tela ou cartão
13 paper cut: colagem de papel com número
14 doodle boil: rabiscos de giz vibrando
15 vertigo: dolly zoom, fundo estica
16 cover story: capa de revista atrás da cabeça
17 glasstype: palavra de vidro 3D

Responde com "sugestões ok", ou com os números por trecho (ex.: "gancho 17, item 3 com 06, resto ok").
```

Se ele escolher tela dividida, a sugestão por trecho fica restrita ao que cabe no painel (05, 07, 09, 10 e `<TelaCheia>` pontual), e a pergunta avisa isso.

## Exemplo aprovado (criador autor do banco): Reels 13 especial (gancho 3), 19/10/2026

O criador escolheu esta versão como a melhor das cinco. Sem tela dividida em nenhum trecho, base `ReelsCheio`, branding apple, TRILHA: NENHUMA.

| trecho | estilo |
|---|---|
| gancho "nove notícias preocupantes de 2026" | 16 cover story |
| itens 9, 8, 7 e 2 | 12 green screen, um cartão por item |
| itens 6, 5 e 1 | 05 digital zoom (o 1 mais forte) |
| item 4 | 04 frame break |
| item 3 | 12 green screen + 03 ui world (interface de fórum) |
| menção honrosa | 11 pull-back reveal |
| fecho e CTA | volta pra câmera cheia, pílula Seguir |

Script e código ficam no acervo pessoal do autor (fora do Git). Legenda por modo: y 600 na câmera cheia, 1075 sobre o green screen, 1400 embaixo da janela do frame break.

## Objetivo futuro (NÃO ativo)

Quando o `MEMORY.md` tiver aprovações e reprovações suficientes por estilo, a skill passa a escolher sozinha tela dividida ou não e os estilos de cada trecho, e edita sem perguntar. Até o criador dizer que esse modo está ligado, **as duas perguntas são obrigatórias**.
