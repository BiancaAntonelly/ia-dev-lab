# Etapa 4: Boas praticas de prompt

## Funcionalidade escolhida

Criar uma funcao Python que gere uma saudacao personalizada, trate nomes em branco e continue compativel com o script principal.

## Prompt fraco

Crie uma funcao de saudacao.

## Resposta esperada para o prompt fraco

Uma resposta provavel criaria apenas uma funcao simples, sem definir onde o arquivo deve ficar, sem testes e sem explicar como validar o resultado. O codigo poderia funcionar, mas ficaria pouco conectado a estrutura do projeto.

## Prompt efetivo

No projeto `ia-dev-lab`, edite `src/hello.py` para criar uma funcao `build_greeting(name="IA")` que retorne uma saudacao personalizada. Siga o contexto do `AGENTS.md`: use Python 3, mantenha funcoes pequenas, nao adicione dependencias externas e preserve uma saida simples. Tambem atualize `tests/test_hello.py` usando `unittest`, conforme `tests/AGENTS.md`, com casos para nome preenchido e nome em branco. Valide com `python3 -m unittest discover -s tests`.

## Resposta esperada para o prompt efetivo

Uma resposta melhor deve alterar o arquivo certo, respeitar a estrutura `src/` e `tests/`, criar testes objetivos e informar o comando de validacao. Tambem deve evitar dependencias externas, porque essa restricao esta registrada no contexto do projeto.

## Comparacao das respostas

O prompt fraco e generico e deixa muitas decisoes em aberto, entao a IA pode produzir codigo correto mas desalinhado da organizacao do projeto. O prompt efetivo informa contexto, arquivo-alvo, padrao de teste, restricoes e forma de validar o resultado. Com isso, a resposta tende a ser mais completa, testavel e consistente com as regras do laboratorio. A diferenca principal esta na qualidade das instrucoes: quanto mais claro o escopo e o criterio de sucesso, menor a chance de retrabalho.

## Modelo usado

Modelo principal usado nesta execucao: Codex nesta sessao.

Modelo de menor performance para repeticao sugerida: uma variante menor/rapida do agente disponivel no ambiente, caso a ferramenta ofereca selecao de modelo.
