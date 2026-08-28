# ia-dev-lab

Laboratorio simples para praticar desenvolvimento com apoio de ferramentas de IA. O projeto usa Python para uma pequena funcionalidade de saudacao e registra contexto, comandos, convencoes e decisoes tecnicas.

## Estrutura

```text
ia-dev-lab/
|-- AGENTS.md
|-- README.md
|-- docs/
|   |-- adr/
|   |   `-- 0001-escolha-da-ferramenta-de-ia.md
|   `-- prompts-comparacao.md
|-- src/
|   |-- __init__.py
|   `-- hello.py
`-- tests/
    |-- AGENTS.md
    `-- test_hello.py
```

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

## Ferramentas de IA usadas

- IDE + assistente sugerido para registro: VS Code + GitHub Copilot.
- CLI agent usado nesta pratica: Codex.
