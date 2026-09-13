# Diagramas de arquitetura

## Versao 1: gerada com prompt simples

```mermaid
C4Container
title ia-dev-lab - Arquitetura atual

Person(user, "Pessoa desenvolvedora", "Executa comandos e revisa artefatos")
System_Boundary(project, "ia-dev-lab") {
  Container(src, "src", "Python", "Codigo de aplicacao")
  Container(tests, "tests", "unittest", "Testes automatizados")
  Container(docs, "docs", "Markdown", "Documentacao e decisoes")
}

Rel(user, src, "Executa", "python3 -m src.hello")
Rel(tests, src, "Valida comportamento")
Rel(user, docs, "Consulta especificacoes e relatorios")
```

## Versao 2: ajustada manualmente com mais contexto

```mermaid
C4Container
title ia-dev-lab - Containers e contratos

Person(dev, "Pessoa desenvolvedora", "Usa IA, Git e testes para evoluir o laboratorio")

System_Boundary(lab, "ia-dev-lab") {
  Container(hello, "src/hello.py", "Python", "Gera saudacoes simples e configuraveis")
  Container(validator, "src/prompt_validator.py", "Python", "Avalia prompts e retorna contrato com is_valid, found, missing e quality")
  Container(test_suite, "tests/", "unittest", "Valida contratos dos modulos Python")
  Container(documentation, "docs/", "Markdown", "Guarda specs, ADRs, logs, checkpoints e relatorios")
  Container(hook, "scripts/hooks/pre-commit", "Shell", "Bloqueia versionamento de caches Python")
}

Rel(dev, hello, "Executa saudacao")
Rel(dev, validator, "Usa para avaliar prompts")
Rel(test_suite, hello, "Testa comportamento")
Rel(test_suite, validator, "Testa contrato de validacao")
Rel(dev, documentation, "Revisa decisoes")
Rel(dev, hook, "Usa antes de commitar")
```

## Comparacao

A primeira versao comunica a divisao geral entre codigo, testes e documentacao, mas agrupa todo o codigo em um unico container `src`, escondendo os contratos dos modulos. A segunda versao comunica melhor a arquitetura atual porque mostra os modulos reais, o hook de harness e o contrato principal do validador de prompts. Para este projeto, a segunda versao e mais util em revisoes porque ajuda a localizar responsabilidades e pontos de acoplamento.
