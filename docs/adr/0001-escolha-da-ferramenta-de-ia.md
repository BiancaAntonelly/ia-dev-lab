# ADR 0001: Escolha da ferramenta de IA para o laboratorio

## Status

Aceita

## Contexto

O laboratorio precisa demonstrar o uso de pelo menos uma ferramenta de IA para desenvolvimento, alem de registrar contexto de projeto e regras que orientem respostas futuras. O projeto e pequeno, em Python, e deve ser simples de executar localmente.

## Decisao

Usaremos Codex como agente CLI para criar, modificar e validar arquivos do projeto. Para a categoria IDE + assistente, registramos VS Code + GitHub Copilot como combinacao recomendada para edicao interativa.

## Consequencias

- O arquivo `AGENTS.md` passa a ser a referencia de contexto para o agente.
- Regras especificas podem ser adicionadas por escopo, como `tests/AGENTS.md`.
- O projeto permanece leve, sem dependencias externas.
- As validacoes principais ficam baseadas em comandos locais simples.
