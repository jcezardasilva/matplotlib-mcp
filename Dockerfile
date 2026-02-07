FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

WORKDIR /app

# Instala uv
RUN pip install --no-cache-dir uv

# Copia apenas arquivos de dependência primeiro
COPY pyproject.toml README.md /app/

# Cria venv e instala dependências
RUN uv venv /opt/venv \
	&& /opt/venv/bin/uv sync --project /app

ENV PATH="/opt/venv/bin:$PATH"

# Copia o código
COPY src/ /app/src/

EXPOSE 8000

CMD ["python", "-m", "matplotlib_mcp.server", "--transport", "streamable-http"]
