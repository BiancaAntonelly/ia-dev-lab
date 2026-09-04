# Spec: prompt-validator

## Requirement: avaliar elementos essenciais de um prompt

O sistema deve avaliar se um prompt contem os elementos essenciais de uma boa solicitacao: contexto, tarefa, restricoes e validacao.

### Scenario: prompt completo

Given um prompt que contem contexto, tarefa, restricoes e validacao  
When o prompt for avaliado  
Then o resultado deve indicar `is_valid` como verdadeiro e nao deve listar elementos ausentes.

### Scenario: prompt generico

Given um prompt generico como `crie uma funcao`  
When o prompt for avaliado  
Then o resultado deve indicar `is_valid` como falso e deve listar os elementos ausentes.

### Scenario: prompt parcial

Given um prompt com contexto e tarefa, mas sem validacao  
When o prompt for avaliado  
Then o resultado deve indicar `is_valid` como falso e deve informar que `validacao` esta ausente.

### Scenario: entrada invalida

Given uma entrada vazia ou que nao seja texto  
When a entrada for avaliada  
Then o resultado deve indicar `is_valid` como falso e deve listar todos os elementos obrigatorios como ausentes.
