# 0002 Manter modulos Python simples

## Contexto

O projeto `ia-dev-lab` cresceu de um exemplo de saudacao para incluir validacao de prompts, especificacoes SDD, harness, testes e documentacao. Mesmo com esse crescimento, o codigo de aplicacao permanece pequeno e sem dependencias externas.

## Decisao

Manter a arquitetura como modulos Python simples separados por responsabilidade: `hello.py` para saudacoes e `prompt_validator.py` para validacao de prompts. Nao sera extraido um servico, framework ou camada adicional neste momento.

## Consequencias

Ganha-se simplicidade, baixo acoplamento e facilidade de teste com `unittest`. A principal limitacao e que, se o projeto crescer com interfaces, persistencia ou integrações externas, sera necessario revisitar a decisao e talvez introduzir uma camada de aplicacao ou servicos. Por enquanto, a estrutura atual comunica bem os contratos e evita arquitetura desnecessaria.
