# Escopo da especificacao

## Projeto escolhido

O projeto escolhido foi o `ia-dev-lab`, laboratorio em Python criado para praticar desenvolvimento assistido por IA. A base atual possui uma funcao simples de saudacao, testes automatizados, documentacao de contexto e registros de decisoes.

## Funcionalidade 1: gerador de saudacoes configuravel

Criar uma funcionalidade que gere saudacoes personalizadas a partir de nome, idioma e periodo do dia. A funcao deve lidar com entradas em branco, nomes com espacos extras e idiomas nao suportados, mantendo uma resposta padrao previsivel.

### Cenarios de uso

- Usuario informa nome `Bianca`, idioma `pt-BR` e periodo `manha`; o sistema retorna uma saudacao em portugues adequada ao periodo.
- Usuario informa nome vazio ou apenas espacos; o sistema usa um nome padrao e ainda retorna uma mensagem valida.
- Usuario informa idioma nao suportado; o sistema aplica o idioma padrao sem quebrar a execucao.

## Funcionalidade 2: validador simples de prompts

Criar uma funcionalidade que avalie se um prompt contem os elementos minimos de uma boa solicitacao: contexto, tarefa, restricoes e criterio de validacao. O resultado deve indicar quais elementos foram encontrados e quais estao ausentes.

### Cenarios de uso

- Usuario envia um prompt completo com contexto, tarefa, restricoes e validacao; o sistema classifica o prompt como adequado.
- Usuario envia um prompt generico, como `crie uma funcao`; o sistema aponta os elementos ausentes.
- Usuario envia um prompt com contexto e tarefa, mas sem criterio de validacao; o sistema retorna uma avaliacao parcial e recomenda melhoria.

## Justificativa para SDD

Essas funcionalidades sao boas candidatas para SDD porque possuem regras de negocio claras, entradas variadas e casos de borda que precisam ser definidos antes da implementacao. O gerador de saudacoes exige decisoes sobre valores padrao, idiomas suportados e comportamento para dados invalidos. O validador de prompts precisa de criterios objetivos para classificar uma entrada textual, o que pode gerar ambiguidades se nao houver uma especificacao previa. As duas funcionalidades tambem devem afetar mais de um arquivo, incluindo codigo em `src/`, testes em `tests/` e possivelmente documentacao no `README.md`.
