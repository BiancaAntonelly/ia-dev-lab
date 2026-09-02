# ia-dev-lab

Laboratorio simples para praticar desenvolvimento com apoio de ferramentas de IA. O projeto usa Python para funcionalidades de saudacao, incluindo uma saudacao configuravel por nome, idioma e periodo do dia, alem de registrar contexto, comandos, convencoes e decisoes tecnicas.

## Estrutura

```text
ia-dev-lab/
|-- AGENTS.md
|-- README.md
|-- .mcp.json
|-- docs/
|   |-- adr/
|   |   `-- 0001-escolha-da-ferramenta-de-ia.md
|   |-- escopo.md
|   |-- mcp-tentativa.md
|   |-- prompts-comparacao.md
|   |-- relatorio-final.md
|   |-- revisao-diff-etapa-3.md
|   `-- spec-sdd-saudacoes.md
|-- src/
|   |-- __init__.py
|   `-- hello.py
`-- tests/
    |-- AGENTS.md
    `-- test_hello.py
```

## Funcionalidade principal

O modulo `src.hello` possui uma saudacao simples e uma saudacao configuravel. A funcao `build_configurable_greeting` recebe nome, idioma e periodo do dia, usando valores padrao quando alguma entrada estiver em branco ou nao for suportada.

Exemplos de comportamento:

- `pt-BR` + `manha` -> `Bom dia, Bianca!`
- `pt-BR` + `tarde` -> `Boa tarde, Bianca!`
- `en` + `noite` -> `Good evening, Bianca!`
- idioma desconhecido -> usa `pt-BR`
- periodo desconhecido -> usa saudacao neutra

## Instalacao

Este projeto nao depende de bibliotecas externas. Basta ter Python 3 instalado.

Para conferir a versao:

```bash
python3 --version
```

## Comandos principais

Rodar o script principal:

```bash
python3 -m src.hello
```

Rodar os testes:

```bash
python3 -m unittest discover -s tests
```

Verificar arquivos alterados no Git:

```bash
git status --short
```

Listar arquivos alterados no ultimo commit:

```bash
git show --name-only --oneline --stat HEAD
```

## Ferramentas de IA usadas

- IDE + assistente sugerido para registro: VS Code + GitHub Copilot.
- CLI agent usado nesta pratica: Codex.

## MCP

O arquivo `.mcp.json` configura um servidor MCP simples de filesystem para o projeto. A tentativa e as limitacoes estao documentadas em `docs/mcp-tentativa.md`.
