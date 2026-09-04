# Relatorio final: De Spec a Codigo

## 1. Funcionalidades escolhidas

As funcionalidades escolhidas foram um gerador de saudacoes configuravel e um validador simples de prompts. Elas foram bons casos para SDD porque possuem regras claras, entradas variadas e casos de borda, como nome em branco, idioma nao suportado, periodo invalido e prompts incompletos. Tambem exigiram alteracoes em mais de um arquivo, incluindo codigo em `src/`, testes em `tests/` e documentacao em `docs/`.

## 2. Abordagens de especificacao usadas

A primeira abordagem foi Markdown manual, usada em `docs/spec-sdd-saudacoes.md` para registrar user story, PRD, criterios de aceite e plano revisado. Ela funcionou bem por ser direta e simples para uma funcionalidade pequena. A segunda abordagem foi OpenSpec manual, registrada em `openspec/changes/add-prompt-validator/`, com `proposal.md`, `design.md`, `tasks.md` e `specs/`. Como o CLI `openspec` nao estava instalado, os artefatos foram criados manualmente, mas a separacao por proposta, design, tarefas e requisitos ajudou a deixar a mudanca mais rastreavel.

## 3. Dificuldade enfrentada

A principal dificuldade foi equilibrar simplicidade e especificacao real em um projeto pequeno. Para resolver isso, mantive as funcionalidades pequenas, mas com regras verificaveis e testes automatizados. Tambem registrei um checkpoint humano antes do merge, revisando se a implementacao atendia a especificacao e se o diff nao quebrava comportamento existente.

## Checklist final

- [x] `docs/escopo.md` com funcionalidades escolhidas e justificativa.
- [x] Especificacao completa com requisitos, criterios de aceite e plano revisado.
- [x] Registro das abordagens de spec usadas e justificativa.
- [x] Tarefas implementadas com testes automatizados.
- [x] Registro de revisao de diff.
- [x] Registro de checkpoint humano.
- [x] Comparacao entre abordagens de especificacao e codigo gerado.
- [x] Repositorio no GitHub com historico de commits.
- [x] Relatorio final em Markdown.
