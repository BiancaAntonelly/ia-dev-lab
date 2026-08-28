# Relatorio final

## 1. Ferramentas de IA configuradas

Usei Codex como agente de desenvolvimento para criar arquivos, reorganizar o projeto, gerar testes e validar comandos. Para a categoria IDE + assistente, registrei VS Code + GitHub Copilot como opcao recomendada, porque e uma combinacao comum para edicao assistida no fluxo diario de desenvolvimento.

## 2. Trecho mais util do AGENTS.md

O trecho mais util foi a secao de comandos:

```md
- `python3 -m src.hello` -> roda o script principal e valida a saudacao.
- `python3 -m unittest discover -s tests` -> roda os testes automatizados quando a pasta `tests/` existir com casos de teste.
```

Esse trecho e importante porque permite que a IA e a pessoa desenvolvedora saibam rapidamente como executar e validar o projeto sem adivinhar comandos.

## 3. Diferenca entre prompt fraco e prompt eficaz

O prompt fraco, "Crie uma funcao de saudacao", deixa contexto, arquivo-alvo, restricoes e validacao em aberto. O prompt eficaz informa onde alterar, qual padrao seguir, quais restricoes respeitar e como testar. A resposta gerada por um prompt eficaz tende a ser mais alinhada com o projeto, mais facil de revisar e menos sujeita a retrabalho.

## 4. Obstaculo enfrentado

O principal obstaculo foi transformar um exemplo inicial muito simples em uma estrutura organizada com `src/`, `tests/`, `docs/` e ADR sem complicar demais o projeto. Resolvi mantendo o laboratorio pequeno, sem dependencias externas, e usando testes `unittest` para validar a funcionalidade.

Durante a integracao com o GitHub, a publicacao por HTTPS falhou por falta de credenciais no terminal. Resolvi usando o remoto SSH, que ja estava autenticado. A abertura automatica do Pull Request pelo navegador integrado ficou bloqueada porque a sessao do GitHub nao estava logada nesse navegador; o link direto para criacao do PR foi gerado pelo GitHub apos o push da branch.

## Checklist final

- [x] Repositorio no GitHub com historico de commits.
- [x] Arquivo `AGENTS.md` e regra customizada em `tests/AGENTS.md`.
- [x] Estrutura de pastas organizada com `README.md` e ADR em `docs/adr/`.
- [x] Arquivo `docs/prompts-comparacao.md` com comparativo de prompts.
- [x] Arquivo `.mcp.json` e documentacao da tentativa MCP.
- [x] Relatorio final em Markdown.
- [ ] Pull Request aberto no GitHub: pendente de login no navegador integrado.
