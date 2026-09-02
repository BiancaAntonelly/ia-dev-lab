# Revisao de diff da Etapa 3

## Diff revisado

Revisei o diff da implementacao do gerador de saudacoes configuravel antes de aceitar as alteracoes. A revisao incluiu `src/hello.py`, `tests/test_hello.py` e `README.md`.

## Observacao concreta

Um ponto que eu poderia ter deixado passar sem a revisao era quebrar a compatibilidade da funcao `build_greeting`, que ja existia e ja era testada. Na revisao, confirmei que `build_greeting` continuou retornando a mensagem original usada nos testes antigos, enquanto a nova regra ficou isolada em `build_configurable_greeting`.

## Resultado da revisao

O diff foi aceito porque os cenarios principais da especificacao foram cobertos por testes, a implementacao nao adicionou dependencias externas e a documentacao foi atualizada com o novo comportamento.
