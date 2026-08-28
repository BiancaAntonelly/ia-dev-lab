# Tentativa de configuracao MCP

## Servidor escolhido

Servidor MCP de filesystem, configurado no arquivo `.mcp.json`.

## Objetivo

Permitir que a ferramenta de IA acesse os arquivos do projeto por meio de um servidor MCP simples, limitado ao diretorio atual do laboratorio.

## Configuracao criada

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "."
      ]
    }
  }
}
```

## Prompt de validacao

Liste os arquivos alterados no ultimo commit.

## Resultado esperado

Com o servidor conectado, a IA deve conseguir consultar a arvore do projeto e responder com base nos arquivos disponiveis. Caso a ferramenta nao permita iniciar MCP neste ambiente, esta configuracao e a documentacao da tentativa registram o procedimento seguido.

## Limitacao encontrada

A configuracao foi criada no projeto, mas a conexao efetiva depende da ferramenta local carregar o `.mcp.json` e permitir executar o servidor MCP configurado.
