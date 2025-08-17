# syntax=docker/dockerfile:1
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:${PATH}"

WORKDIR /app

# Install curl for uv install
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Copy dependency manifests first for better layer caching
COPY pyproject.toml uv.lock* ./

# Sync dependencies (creates .venv in /app)
RUN uv sync --frozen --no-dev

# Copy application code
COPY app ./app
COPY run.sh ./run.sh

EXPOSE 8001

# Default command: run the API server
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"] 