# Investigacao de divida tecnica

## Opcao escolhida

Escolhi a Opcao A: divida tecnica.

## Ferramenta usada

As ferramentas `ruff`, `pylint` e `flake8` nao estavam instaladas no ambiente local. Para ainda executar uma investigacao real, criei uma ferramenta simples de analise estatica em `scripts/static_analysis.py`, usando `ast` da biblioteca padrao do Python.

## O que a ferramenta verifica

A ferramenta percorre os arquivos em `src/`, identifica funcoes publicas e confere se o nome dessas funcoes aparece nos testes em `tests/test_*.py`. O objetivo e localizar funcoes publicas sem teste dedicado.

## Resultado observado

```text
Possiveis sinais de divida tecnica:
- src/prompt_validator.py:summarize_prompt_validation sem teste dedicado
```

## Sinal real de divida tecnica

A funcao `summarize_prompt_validation` foi criada durante a comparacao sem TDD. Ela reutiliza `validate_prompt`, mas nao possui teste proprio para garantir o formato textual retornado.

## Mitigacao proposta

Criar um teste dedicado em `tests/test_prompt_validator.py` verificando o resumo retornado por `summarize_prompt_validation`, ou entao remover a funcao se ela nao for necessaria para nenhum fluxo real. A mitigacao recomendada e adicionar o teste, porque a funcao pode ser util para apresentar o resultado ao usuario.

## Aprendizado

Mesmo em um projeto pequeno, uma ferramenta simples de analise estatica consegue revelar uma divida tecnica criada por uma decisao de processo: a tarefa feita sem TDD gerou codigo sem teste dedicado. Isso reforca o valor do ciclo Red-Green-Refactor como guardrail.
