# Proposal: add-prompt-validator

## Summary

Adicionar um validador simples de prompts ao `ia-dev-lab` para identificar se um prompt contem contexto, tarefa, restricoes e criterio de validacao.

## Motivation

Na atividade anterior, o projeto comparou um prompt fraco com um prompt efetivo. Esta mudanca transforma essa comparacao em uma funcionalidade executavel, permitindo avaliar prompts de forma objetiva e testavel.

## Scope

- Criar uma funcao que analise um texto de prompt.
- Retornar quais elementos obrigatorios foram encontrados.
- Retornar quais elementos estao ausentes.
- Classificar o prompt como adequado apenas quando todos os elementos obrigatorios estiverem presentes.
- Manter a implementacao sem dependencias externas.

## Out of Scope

- Usar modelos de IA para interpretar semanticamente o prompt.
- Criar interface grafica.
- Persistir historico de avaliacoes.
- Criar score numerico complexo.
