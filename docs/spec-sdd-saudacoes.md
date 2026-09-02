# Especificacao SDD: gerador de saudacoes configuravel

## Abordagem usada

Esta especificacao foi estruturada em Markdown manual. A escolha foi feita porque o projeto e pequeno, a atividade aceita especificacao manual como entregavel, e essa abordagem evita depender de ferramentas externas como OpenSpec ou Traycer.ai para uma funcionalidade de escopo reduzido.

## Prompt inicial em formato de user story

Como pessoa usuaria do laboratorio `ia-dev-lab`, quero gerar uma saudacao personalizada considerando meu nome, idioma e periodo do dia, para receber uma mensagem adequada ao contexto informado mesmo quando alguma entrada estiver ausente ou invalida.

## PRD: requisitos da funcionalidade

### Objetivo

Permitir que o projeto gere saudacoes personalizadas de forma previsivel, validavel e preparada para diferentes cenarios de entrada.

### Publico-alvo

Pessoas desenvolvedoras ou estudantes usando o `ia-dev-lab` para praticar desenvolvimento guiado por especificacao com apoio de IA.

### Requisitos funcionais

- A funcionalidade deve receber nome, idioma e periodo do dia.
- A funcionalidade deve remover espacos extras antes e depois do nome informado.
- Quando o nome estiver vazio, ausente ou invalido, a funcionalidade deve usar o nome padrao `IA`.
- A funcionalidade deve oferecer suporte inicial aos idiomas `pt-BR` e `en`.
- Quando o idioma informado nao for suportado, a funcionalidade deve usar `pt-BR` como padrao.
- A funcionalidade deve reconhecer pelo menos os periodos `manha`, `tarde` e `noite`.
- Quando o periodo informado nao for suportado, a funcionalidade deve usar uma saudacao neutra.
- A mensagem retornada deve ser uma string simples, sem depender de entrada interativa.
- O script principal deve continuar executavel por linha de comando.
- A funcionalidade deve ter testes automatizados cobrindo cenarios principais e casos de borda.

### Requisitos nao funcionais

- A implementacao deve usar Python 3.
- A implementacao nao deve adicionar dependencias externas.
- O codigo deve permanecer simples, legivel e organizado em `src/`.
- Os testes devem usar `unittest` e ficar em `tests/`.
- A validacao deve ser feita com `python3 -m unittest discover -s tests`.

### Fora de escopo

- Interface grafica.
- Persistencia em arquivo ou banco de dados.
- Suporte a mais idiomas alem de `pt-BR` e `en` nesta primeira versao.
- Deteccao automatica do horario real do sistema.
- Traducao dinamica usando servicos externos.

## Criterios de aceite

### Cenario 1: saudacao em portugues pela manha

Given que a pessoa usuaria informa o nome `Bianca`, o idioma `pt-BR` e o periodo `manha`  
When a saudacao configuravel e gerada  
Then o sistema deve retornar uma mensagem em portugues com referencia ao periodo da manha e ao nome `Bianca`.

### Cenario 2: nome em branco

Given que a pessoa usuaria informa um nome vazio ou composto apenas por espacos  
When a saudacao configuravel e gerada  
Then o sistema deve usar o nome padrao `IA` na mensagem.

### Cenario 3: idioma nao suportado

Given que a pessoa usuaria informa um idioma nao suportado, como `es`  
When a saudacao configuravel e gerada  
Then o sistema deve usar `pt-BR` como idioma padrao e retornar uma mensagem valida.

### Cenario 4: periodo nao suportado

Given que a pessoa usuaria informa um periodo nao suportado, como `madrugada`  
When a saudacao configuravel e gerada  
Then o sistema deve retornar uma saudacao neutra, sem quebrar a execucao.

## Plano de tarefas proposto por agente de IA

- Criar uma funcao `build_configurable_greeting` em `src/hello.py`.
- Definir valores padrao para nome, idioma e periodo.
- Criar uma estrutura simples de mensagens por idioma e periodo.
- Normalizar entradas de texto, removendo espacos extras e tratando valores invalidos.
- Atualizar `main()` para demonstrar o uso da nova funcao.
- Criar testes em `tests/test_hello.py` para os cenarios de aceite.
- Atualizar o `README.md` com o novo comportamento e comandos de validacao.
- Rodar `python3 -m unittest discover -s tests`.

## Revisao humana do plano

O plano proposto foi mantido em sua maior parte, mas a ordem foi ajustada para priorizar primeiro os criterios de teste e depois a implementacao. Essa mudanca reduz o risco de implementar uma solucao que pareca correta, mas nao cubra os casos de borda definidos na especificacao. Tambem foi decidido nao adicionar leitura de argumentos de linha de comando nesta etapa, porque isso aumentaria o escopo e nao e necessario para validar a regra principal da funcionalidade.

## Plano revisado

- Revisar os criterios de aceite e transformar cada um em pelo menos um teste automatizado.
- Atualizar `tests/test_hello.py` com casos para nome valido, nome em branco, idioma nao suportado e periodo nao suportado.
- Implementar `build_configurable_greeting` em `src/hello.py` usando valores padrao previsiveis.
- Manter `build_greeting` existente compativel para nao quebrar testes anteriores.
- Atualizar `main()` apenas para demonstrar o comportamento padrao.
- Atualizar `README.md` com a descricao da funcionalidade.
- Executar `python3 -m unittest discover -s tests`.
- Revisar o diff antes de commitar.
