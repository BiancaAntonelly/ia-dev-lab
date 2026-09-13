# Harness minimo: autonomia e guardrail

## Projeto escolhido

O projeto escolhido foi o `ia-dev-lab`, o mesmo usado nas praticas anteriores.

## Tarefa pequena testada

A tarefa usada para comparar autonomia foi adicionar um documento de entrega no repositorio. A mesma tarefa foi analisada em dois modos: um modo guiado, com planejamento e revisao antes de aceitar alteracoes, e um modo mais automatico, aceitando edicoes com pouca pausa intermediaria.

## Comparacao entre modos de autonomia

| Modo | Tempo gasto | Sensacao de controle | Risco percebido |
| --- | --- | --- | --- |
| Guiado com revisao | Cerca de 8 minutos | Alto, porque cada arquivo e diff foram conferidos antes do commit | Baixo, pois houve validacao antes de publicar |
| Execucao mais automatica | Cerca de 4 minutos | Medio, porque a tarefa avanca mais rapido, mas exige confiar mais no agente | Medio, pois pequenos erros de conteudo ou caminho poderiam passar despercebidos |

## Conclusao

O modo mais automatico e util para tarefas pequenas e reversiveis, como criar um documento simples. Para mudancas que afetam codigo, testes ou fluxo de entrega, o modo guiado oferece melhor equilibrio entre velocidade e seguranca.

## Guardrail configurado

O guardrail escolhido foi um hook de pre-commit que bloqueia arquivos de cache Python, como `__pycache__/` e `*.pyc`. Esse risco e real no projeto porque a execucao dos testes gera caches locais, e versionar esses arquivos polui o historico e pode esconder diferencas irrelevantes em revisoes.

## Como instalar o hook

```bash
cp scripts/hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
