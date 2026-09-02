# Design: add-prompt-validator

## Overview

O validador sera implementado em um novo modulo `src/prompt_validator.py`. A funcao principal recebera uma string e retornara um dicionario com tres informacoes: elementos encontrados, elementos ausentes e status final.

## Behavior

Os elementos obrigatorios sao `contexto`, `tarefa`, `restricoes` e `validacao`. Como o projeto deve permanecer simples e sem dependencias externas, a primeira versao usara palavras-chave para identificar cada elemento.

## Data shape

```python
{
    "is_valid": False,
    "found": ["contexto", "tarefa"],
    "missing": ["restricoes", "validacao"],
}
```

## Trade-offs

O uso de palavras-chave e simples, previsivel e facil de testar, mas pode nao reconhecer prompts bem escritos que usem sinonimos. Essa limitacao foi aceita para manter o escopo pequeno e adequado ao laboratorio.
