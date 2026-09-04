# Comparacao de ferramentas SDD

## Opcao escolhida para repeticao

A segunda abordagem escolhida foi OpenSpec, registrada por meio de artefatos manuais no diretorio `openspec/changes/add-prompt-validator/`. O comando `openspec` nao estava instalado no ambiente, entao a estrutura foi criada manualmente seguindo a ideia da ferramenta: proposta, design, tarefas e especificacao por requisito.

## O que foi feito

Repeti o processo de SDD para a funcionalidade `validador simples de prompts`, que havia sido definida no escopo inicial. Foram criados os artefatos `proposal.md`, `design.md`, `tasks.md` e `specs/prompt-validator/spec.md`, depois as tarefas foram executadas com a implementacao de `src/prompt_validator.py` e testes em `tests/test_prompt_validator.py`.

## Comparacao das estrategias de especificacao

A especificacao em Markdown manual usada na funcionalidade de saudacoes foi mais rapida e direta, porque concentrou user story, PRD, criterios de aceite e plano em um unico arquivo. A abordagem inspirada no OpenSpec separou melhor a intencao da mudanca, o desenho tecnico, a lista de tarefas e os requisitos verificaveis. O ponto positivo do Markdown manual foi a simplicidade; o ponto negativo foi que ele depende mais de disciplina para manter tudo organizado. O ponto positivo do OpenSpec foi a rastreabilidade; o ponto negativo foi gerar mais arquivos para uma funcionalidade pequena.

## Comparacao do codigo gerado

Na funcionalidade de saudacoes, o codigo ficou concentrado em `src/hello.py`, reaproveitando a estrutura existente e mantendo compatibilidade com `build_greeting`. Na funcionalidade do validador de prompts, a abordagem OpenSpec favoreceu criar um modulo separado, `src/prompt_validator.py`, deixando a responsabilidade mais isolada. As duas implementacoes atenderam aos requisitos passados e foram cobertas por testes, mas o validador ficou arquiteturalmente mais separado por ter nascido de uma especificacao com design proprio.

## Evidencia

Evidencia local da opcao escolhida:

- `openspec/changes/add-prompt-validator/proposal.md`
- `openspec/changes/add-prompt-validator/design.md`
- `openspec/changes/add-prompt-validator/tasks.md`
- `openspec/changes/add-prompt-validator/specs/prompt-validator/spec.md`

O aprendizado principal foi que uma ferramenta mais estruturada ajuda a separar melhor decisao, requisito e execucao. Para projetos pequenos, Markdown manual pode ser suficiente; para funcionalidades com mais regras, a organizacao por artefatos facilita revisar e evoluir a especificacao antes de codificar.
