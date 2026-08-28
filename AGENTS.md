# AGENTS.md

## Sobre o projeto
Este projeto e um laboratorio simples para testar ferramentas de IA aplicadas ao desenvolvimento. Ele contem uma pequena funcionalidade Python de saudacao, testes automatizados e documentos de apoio para registrar decisoes e praticas de prompt.

## Comandos
- `python3 -m src.hello` -> roda o script principal e valida a saudacao.
- `python3 -m unittest discover -s tests` -> roda os testes automatizados quando a pasta `tests/` existir com casos de teste.
- `git status --short` -> confere rapidamente quais arquivos foram criados ou alterados.

## Convencoes de codigo
- Use Python 3.
- Coloque codigo de aplicacao em `src/`.
- Coloque testes automatizados em `tests/`.
- Coloque decisoes de arquitetura em `docs/adr/`.
- Prefira funcoes pequenas e nomes claros.
- Mantenha mensagens de saida simples e faceis de validar.
- Evite dependencias externas sem necessidade para este laboratorio.

## Nao fazer
- Nao adicionar bibliotecas ou frameworks sem uma justificativa clara.
- Nao misturar exemplos de varias linguagens no mesmo teste inicial.
- Nao remover arquivos do laboratorio sem confirmar primeiro.
