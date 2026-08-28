# Regras para tests/

## Convencao customizada por escopo
Arquivos dentro desta pasta devem ser testes automatizados em Python usando `unittest`.

## Comandos
- `python3 -m unittest discover -s tests` -> roda todos os testes deste escopo.

## Convencoes de codigo
- Nomeie arquivos de teste como `test_*.py`.
- Nomeie metodos de teste como `test_*`.
- Cada teste deve validar um comportamento pequeno e objetivo.

## Nao fazer
- Nao criar testes que dependam de rede.
- Nao depender de ordem de execucao entre testes.
