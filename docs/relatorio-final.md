# Relatorio final: Harness e Arquitetura na Pratica

## 1. Autonomia e guardrail

Comparei um modo guiado com revisao e um modo mais automatico para uma tarefa pequena. O modo automatico foi mais rapido, mas o modo guiado deu mais controle e reduziu risco de aceitar arquivo errado. O guardrail configurado foi um hook de pre-commit em `scripts/hooks/pre-commit`, bloqueando arquivos `__pycache__` e `*.pyc`; o bloqueio foi testado e registrado em `docs/harness-hook-log.md`.

## 2. TDD e enforcement

Usei Red-Green-Refactor para adicionar a classificacao de qualidade no validador de prompts. O historico mostra o teste falhando antes da implementacao, depois a implementacao minima e, por fim, o refactor para constantes. Investiguei TDD Guard pela documentacao oficial e registrei que ele bloquearia implementacoes sem teste previo, mas nao foi instalado porque depende da configuracao especifica do agente. A comparacao com uma tarefa sem TDD mostrou menor rastreabilidade e gerou uma funcao sem teste dedicado.

## 3. Checkpoint humano

O checkpoint definido foi antes de aceitar mudancas no contrato publico de `validate_prompt`. O papel humano foi o de revisora de contrato de modulo. A decisao foi aprovar com edicao: aceitar o campo `quality`, mas refatorar seus valores para constantes nomeadas.

## 4. Arquitetura, ADR e diagrama

A revisao arquitetural concluiu que o projeto esta no tamanho certo para modulos Python simples, sem extrair servico ou framework. A decisao foi registrada no ADR `docs/adr/0002-manter-modulos-python-simples.md`. O diagrama em `docs/arquitetura-diagrama.md` compara uma versao geral e uma versao mais detalhada; a segunda comunica melhor os contratos e responsabilidades.

## 5. Divida tecnica

Escolhi investigar divida tecnica. Como `ruff`, `pylint` e `flake8` nao estavam instalados, criei `scripts/static_analysis.py`, que identifica funcoes publicas sem teste dedicado. A ferramenta apontou `summarize_prompt_validation`, justamente a funcao criada sem TDD. O principal aprendizado foi que o processo sem TDD aumenta chance de deixar comportamento publico sem teste.

## 6. Dificuldade real

A maior dificuldade foi adaptar uma atividade pensada para ferramentas/harness completos a um projeto pequeno e local. Resolvi usando controles equivalentes e verificaveis: hook versionado, commits Red-Green-Refactor, log da sessao, ADR, diagrama e analise estatica simples.
