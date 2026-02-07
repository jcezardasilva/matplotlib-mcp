# Matplotlib MCP (FastMCP)

Servidor MCP em Python com FastMCP, transport streamable HTTP e tools para múltiplos tipos de gráficos.

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

- `render_line_chart` (linha)
- `render_bar_chart` (barras)
- `render_scatter_chart` (dispersão)
- `render_area_chart` (área)
- `render_histogram_chart` (histograma)
- `render_boxplot_chart` (boxplot)
- `render_heatmap_chart` (heatmap)
- `render_stacked_bar_chart` (barras empilhadas)
- `render_line_markers_chart` (linha com marcadores)
- `render_pie_chart` (pizza)
- `render_donut_chart` (rosca)

## Examples (Resources)

Cada gráfico possui um resource com exemplo em JSON (mimeType application/json):

- `examples://charts/line`
- `examples://charts/bar`
- `examples://charts/scatter`
- `examples://charts/area`
- `examples://charts/histogram`
- `examples://charts/boxplot`
- `examples://charts/heatmap`
- `examples://charts/stacked-bar`
- `examples://charts/line-markers`
- `examples://charts/pie`
- `examples://charts/donut`
