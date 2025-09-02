# ---- Base stage ----
FROM python:3.12-slim AS base

WORKDIR /app

RUN pip install --no-cache-dir uv

# Copy dependency files only
COPY pyproject.toml uv.lock ./

# Install deps into /.venv
RUN uv sync --frozen --no-dev --no-cache

# ---- Runtime stage ----
FROM python:3.12-slim AS runtime

WORKDIR /app

# Copy virtual environment from base
COPY --from=base /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy app source
COPY ./app ./app

# Expose port
EXPOSE 8000

# Run Uvicorn with 4 workers + reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--reload-dir", "app"]
