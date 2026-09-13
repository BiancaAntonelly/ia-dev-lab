# TDD como guard-rail

## Ciclo Red-Green-Refactor

A tarefa escolhida foi adicionar uma classificacao de qualidade ao validador de prompts.

## Evidencia do ciclo

- Red: commit `2bd146b` adicionou testes esperando o campo `quality` antes da implementacao. A suite falhou com `KeyError: 'quality'`.
- Green: commit `ecf08c6` implementou a classificacao minima para os testes passarem.
- Refactor: commit `3a1bbb6` substituiu strings soltas por constantes nomeadas sem alterar comportamento.

## Ferramenta investigada

A ferramenta investigada foi TDD Guard. A documentacao oficial informa que ela funciona como enforcement de TDD para agentes, bloqueando implementacao sem testes falhando antes, evitando implementacao alem do necessario e podendo integrar lint. A propria documentacao tambem informa que novos projetos devem considerar Probity, enquanto TDD Guard permanece mantido para projetos existentes.

Fonte consultada:

- https://github.com/nizos/tdd-guard
- https://www.npmjs.com/package/tdd-guard

## Instalacao no contexto deste projeto

Nao instalei a ferramenta no projeto porque ela e voltada principalmente para hooks/plugin de agentes como Claude Code e depende de configuracao especifica do ambiente do agente. No nosso contexto, simulei o comportamento central com commits separados Red-Green-Refactor e com revisao explicita do historico.

## Tarefa sem TDD

Como comparacao, foi adicionada a funcao `summarize_prompt_validation` diretamente em `src/prompt_validator.py`, sem escrever um teste antes. Ela reutiliza `validate_prompt` e retorna um resumo textual da avaliacao.

## Comparacao

O fluxo com TDD deixou claro o comportamento esperado antes da implementacao e protegeu casos de borda por meio de testes. A tarefa sem TDD foi mais rapida, mas ficou menos rastreavel: nao houve falha inicial comprovando a necessidade da mudanca, e a nova funcao depende indiretamente dos testes de `validate_prompt`, sem testes dedicados para o formato do resumo. A diferenca principal foi a confianca: com TDD, a revisao verifica um contrato explicito; sem TDD, a revisao depende mais de leitura manual do codigo.
