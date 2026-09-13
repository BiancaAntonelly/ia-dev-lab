# Evidencia do hook de pre-commit

## Acao de risco testada

Foi simulada a tentativa de versionar um arquivo de cache Python em `tmp_hook_test/__pycache__/blocked.pyc`.

## Comando executado

```bash
mkdir -p tmp_hook_test/__pycache__
printf 'cache' > tmp_hook_test/__pycache__/blocked.pyc
git add tmp_hook_test/__pycache__/blocked.pyc
scripts/hooks/pre-commit
```

## Resultado esperado

O hook deve bloquear a acao e retornar erro.

## Log observado

```text
Commit bloqueado: arquivos de cache Python nao devem ser versionados.
tmp_hook_test/__pycache__/blocked.pyc
Remova esses arquivos do stage antes de commitar.
```

## Limpeza apos o teste

O arquivo de cache usado na simulacao foi removido do stage e apagado do diretorio local.
