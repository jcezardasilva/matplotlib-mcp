# Matplotlib MCP (FastMCP)

Servidor MCP em Python com FastMCP, transport streamable HTTP e uma tool para renderizar gráficos de linha com múltiplas séries.

## UV

- Criar ambiente e sincronizar dependências:
  - `uv venv`
  - `uv sync`
- Executar com uv:
  - `uv run python -m matplotlib_mcp.server --transport streamable-http`

## Executar

- Streamable HTTP (padrão):
  - `python -m matplotlib_mcp.server --transport streamable-http`

- Stdio (para integração local via MCP config):
  - `python -m matplotlib_mcp.server --transport stdio`

## Tools disponíveis

- `render_line_chart`: gera um gráfico de linha com múltiplas séries e retorna uma imagem.
- `render_bar_chart`: gera um gráfico de barras com múltiplas séries e retorna uma imagem.

### Exemplo de entrada

```json
{
  "title": "Vendas por mês",
  "x_label": "Mês",
  "y_label": "Vendas",
  "series": [
    {"label": "Produto A", "y": [10, 20, 18, 25]},
    {"label": "Produto B", "x": [1, 2, 3, 4], "y": [8, 15, 22, 19]}
  ],
  "width": 900,
  "height": 500,
  "dpi": 100,
  "show_grid": true
}
```
