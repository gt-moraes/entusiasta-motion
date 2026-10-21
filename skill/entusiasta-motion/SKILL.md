---
name: entusiasta-motion
description: Edita reels inteiros e cria motion design em código (Remotion) no padrão premium Apple, sincronizado com a fala do criador. Recebe o vídeo bruto (com retakes), escolhe o último take de cada fala, corta, põe a câmera embaixo e o motion em cima (interfaces reais, logos oficiais, mola física, zoom na ação), legenda no estilo do criador e efeitos de interface, e entrega o .mp4 pronto. Também faz só o motion por cima (.mov com transparência) pra juntar no editor. Use quando o criador disser "edita esse vídeo inteiro", "faz a edição completa", "a IA edita esse bruto", "edita igual a referência", "faz o motion desse vídeo", "cria os motions desse reels", "monta um motion de app", "anima isso", "quero um motion igual a esse", "motion pro YouTube", "motion pra publi", mandar um vídeo gravado ou um roteiro pedindo motion, ou mandar uma referência ("olha esse motion", "aprende com esse"). Antes de editar, assiste o bruto, sugere estilos do banco de 17 estilos de edição por trecho e pergunta se o vídeo fica em tela dividida e quais estilos aplicar. Também para reaproveitar um motion do acervo e para trocar atualizações da skill com o time ("manda pro <nome>", "manda essa melhoria pro time", "o que o <nome> mandou?", "puxa a atualização da skill"). NÃO use para vídeo realista gerado por IA, thumbnail, carrossel de imagens, nem para mandar bruto pra um editor humano.
---

# Skill: entusiasta-motion

## Setup (leia antes de executar)
0. **`perfil.md` desta pasta.** Se NÃO existir, é a primeira vez: rode o questionário de `referencias/onboarding.md` antes de qualquer coisa e grave as respostas em `perfil.md` (é pessoal, não vai pro Git). É o perfil que diz de onde vem o roteiro, onde fica o acervo, qual a cor/branding, o estilo de legenda, etc.
1. `HANDOFF.md` se existir trabalho em andamento (retomada depois de limpar a conversa).
2. `CLAUDE.md` desta skill: arquitetura, regras de ouro e pegadinhas.
3. `MEMORY.md`: o que ESTE criador aprovou e reprovou (pessoal). Crie a partir de `MEMORY.exemplo.md` se não existir.
4. `referencias/doutrina-movimento.md`: **OBRIGATÓRIO antes de montar qualquer cena.** Pular a doutrina é o que deixa o resultado genérico.
5. `referencias/estilos.md`: **OBRIGATÓRIO no modo editado inteiro.** O banco dos 17 estilos, o guia de sugestão por trecho e o modelo da pergunta.
6. `referencias/trials.md`: **OBRIGATÓRIO depois da aprovação**, quando entram as variações pra trial reels.
7. Sob demanda em `referencias/`: `formatos.md`, `brandings.md`, `logos-e-simbolos.md`, `som.md`, `retroalimentacao.md`, `apple-hig-para-motion.md`.

## Como o criador trabalha com a skill (padrão de fábrica; o `perfil.md` ajusta)
1. **Roteiro:** o criador já tem o roteiro (num gerenciador de conteúdo, arquivo ou colado na conversa). A skill lê o roteiro e o texto exato de cada fala.
2. **Referência OU briefing:** normalmente ele manda um vídeo de referência ("edita igual a esse"). Sem referência, a skill conduz um briefing curto (ver abaixo).
3. **Bruto:** ele manda o arquivo gravado, com retakes. A skill escolhe os takes e corta.
4. **Assistir e perguntar o estilo (obrigatório no editado):** a skill assiste o bruto, identifica que estilos cabem em cada trecho e faz duas perguntas: tela dividida ou não, e quais estilos aplicar, sempre relembrando os 17 com a descrição curta e trazendo sugestão por trecho (`referencias/estilos.md`).
5. **Portão:** a skill mostra o script de motion ANTES de construir e só renderiza depois do OK.
6. **Trial reels:** com o vídeo aprovado, a skill oferece as variações de gancho pra testar com quem não segue (`referencias/trials.md`).

## Dois modos
- **Editado inteiro** (padrão para reels): a skill entrega o reels pronto (cortes + câmera + motion + legenda + SFX).
  1. `motor/takes.sh <bruto>`: mapa de trechos falados com texto. Regra: **o ÚLTIMO take de cada fala** (murmúrio ensaiando a próxima fala não é take; ouvir na dúvida).
  2. Escrever `cortes.json` (`[[inicio, fim, "texto exato falado"], ...]`, folga ~0,08s antes e ~0,1s depois) e rodar `motor/preparar.py <id> <bruto> <cortes.json>` → `studio/public/brutos/<id>.mp4` (proxy leve) + `studio/public/edicoes/<id>.json` (falas + tempo de cada palavra).
  3. **Assistir e sugerir estilos.** Com o `edicoes/<id>.json` (fala e tempo de cada palavra) e quadros do proxy (`ffmpeg -ss <t> -i studio/public/brutos/<id>.mp4 -frames:v 1 q-<t>.png`, um por trecho, olhando espaço acima da cabeça, mãos e enquadramento), mapear cada trecho contra o guia "sinal na fala → estilo" de `referencias/estilos.md`. Sem visão de imagem, sugerir só pela fala e avisar que o enquadramento não foi conferido.
  4. **Perguntar (PORTÃO DE ESTILO, obrigatório):** mandar o modelo de `referencias/estilos.md`: (a) tela dividida ou câmera cheia; (b) quais estilos, com a tabela `tempo | fala | sugestão | por quê` e a lista dos 17 com uma linha cada. Esperar a resposta. Não pular, mesmo com referência ou briefing: o modo autônomo ainda não está ligado.
  5. Montar conforme a resposta. **Tela dividida:** copiar `studio/src/acervo/_modelos/modelo-editado/` pra `studio/src/acervo/<topico>/<slug>/`, registrar em `studio/src/Root.tsx` (id com "Editado") e montar as cenas dentro de `<ReelsEditado>`: painel de motion no topo (0-900px), câmera deslocada embaixo, `<TelaCheia>` (até 2), `momento(ed, "palavra", fala)` pra ação cair NA palavra. Legenda e som já vêm prontos. **Câmera cheia:** base `studio/src/edicao/ReelsCheio.tsx` (motion `sobre` a câmera, `<TelaCheia>` quando a cena pede), e cada estilo escolhido montado a partir da ficha em `referencias/estilos.md` (ou adaptado da composição `Estilo*` em `studio/src/acervo/estilos/NN-nome/`, quando ela existir no acervo local), entrando na palavra do trecho. Exemplo aprovado descrito em `estilos.md`.
  6. `motor/render.sh <Id> <saida>` → `.mp4`.
  7. **Trial reels (depois do OK do criador):** perguntar "Edição aprovada. Quer as variações pra trial reels?" (se ele já pediu, só fazer). Padrão 5 versões, cada uma com um gancho do banco de `referencias/trials.md`, mudando só os ~3 s iniciais: o corpo é o vídeo aprovado. Montar com `studio/src/edicao/variacoes.ts`, entregar como `trials/trial-0N-<gancho>.mp4` na pasta de entrega do `perfil.md` + `trials.md` com a hipótese de cada uma.
- **Overlay** (só o motion, o criador junta no editor dele): composição com `<Reels>`, render `.mov` ProRes 4444 com transparência, duração exata do vídeo gravado.

## Fluxo
1. **Briefing curto** (só o que faltar e não estiver no `perfil.md`): destino (reels, YouTube, publi), modo (editado inteiro ou overlay), referência (se houver), branding, som.
   Sem referência, pergunte também: qual a ação principal de cada trecho, que telas/apps aparecem (o que citar precisa aparecer de verdade), tom (sério, divertido, técnico).
2. **Transcrever** (overlay) ou **mapear takes** (editado). Sem vídeo (só roteiro): estimar ~2,6 palavras/s e avisar que o tempo final vem do vídeo.
2b. **Estilos (editado, PORTÃO):** assistir, sugerir por trecho e perguntar tela dividida + estilos (ver "Dois modos", passos 3 e 4). Só seguir com a resposta.
3. **Script de motion (PORTÃO, obrigatório):** tabela `| tempo | fala | modo (topo/cheio/green/janela) | estilo | ação herói | peça |`, já com os estilos que ele escolheu + 1 linha com branding, som, **trilha** (slug do acervo, `referencias/som.md`, ou nenhuma se o criador vetou música) e duração. Esperar o OK. Referência de motion: analisar a gramática (ver `retroalimentacao.md`) e dizer o que vai copiar dela.
4. **Construir:** reaproveitar acervo e primitivas antes de criar; peça nova nasce genérica em `studio/src/primitivas/`.
5. **Conferir:** `motor/folha.sh <Id> <saida.png> <frames...>` e OLHAR a folha contra o **checklist "cara de premium"** (fim da doutrina) + área segura + nada sobreposto. Corrigir antes de mostrar.
6. **Renderizar** só com OK: `motor/render.sh <Id> <saida>`.
7. **Acervo:** vídeo + `ficha.md` (modelo em `formatos.md`) na pasta de acervo do `perfil.md` + linha no catálogo.
7b. **Trial reels:** com o OK, variações de gancho (`referencias/trials.md`).
8. **Retroalimentar:** `MEMORY.md` (pessoal), incluindo que estilos ele escolheu, aprovou ou reprovou, e a coluna "notas do criador" de `referencias/estilos.md`. É esse histórico que um dia libera o modo autônomo. Aprendizado que vale pra todo criador sobe pra doutrina/código e pode ser mandado pro time (`COLABORACAO.md`).

## Colaboração (trocar melhorias com o time)
Protocolo completo em `COLABORACAO.md` (raiz do repositório). Resumo:
- **"manda pro <nome>" / "manda essa melhoria pro time":** separar o compartilhável (doutrina, primitivas, motor, referências) do pessoal (perfil, MEMORY, brutos, edições, acervo pessoal), criar branch `<autor>/<assunto>`, commit, push e abrir PR no formato do template (o que mudou, por quê, antes/depois, como testar, regras novas). Devolver o link do PR.
- **"o que o <nome> mandou?" / "puxa a atualização":** listar PRs abertos, resumir cada um, testar (tipos + folha da demo) e só fazer merge com OK do criador. Depois `git pull`.

## Regras
- Script antes de gerar, sempre. Nada de render sem OK. Exceção: quando o criador manda editar sem portão ("só edita e me apresenta a final"), vale pra aquele vídeo.
- Trial reels só depois da aprovação, e só o gancho muda.
- No editado inteiro, as duas perguntas de estilo (tela dividida? quais estilos?) vêm antes do script, sempre com a lista dos 17. Estilo é efeito de trecho, não do vídeo inteiro.
- **Modo autônomo (futuro, NÃO ativo):** a skill escolher sozinha tela dividida e estilos e editar sem perguntar. Só liga quando o criador disser.
- Checklist "cara de premium" conferido na folha ANTES de mostrar.
- **Interface real e fiel** em vez de símbolo; **toda ferramenta citada com a logo oficial**; mascote do Claude (Clawd) **só no gancho**, junto da logo.
- **Trilha de fundo em todo reels editado**, bem baixa (acervo pessoal em `studio/public/trilhas/`, ver `som.md`).
- **Som só de interface** (banco `ui-*`), baixo. Laser, whoosh, impacto e riser ficam mudos.
- **Área segura do Reels:** nada a menos de ~90px das laterais nem colado no topo, zoom incluído.
- Legenda do modo editado: estilo do `perfil.md` (padrão: Geist 600, minúscula, branca, sem caixa, 2-3 palavras, altura variável, escura em fundo claro). No overlay, a legenda é do editor do criador.
- Logo de terceiro na cor original, do pacote de logos ou do press kit oficial, nunca redesenhada nem gerada por IA.
- Nunca usar marca, logo ou fonte licenciada de empresa real como se fosse do app mostrado (app de demonstração = fictício).
- Regras de estilo de texto do criador (palavras proibidas, pontuação, tom): `perfil.md`.
