# Start with slim Python image
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies FIRST (this rarely changes, so it gets cached)
RUN apt-get update && apt-get install -y \
    postgresql-client \
    redis-tools \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv (also rarely changes)
RUN pip install --no-cache-dir uv

# Copy ONLY dependency files (this layer only rebuilds when deps change)
COPY pyproject.toml uv.lock ./

# Install Python dependencies
RUN uv sync --frozen --no-dev

# Copy the rest of the application (this rebuilds on code changes)
COPY ./app ./app
COPY ./alembic ./alembic
COPY ./alembic.ini ./alembic.ini
COPY ./entrypoint.sh ./entrypoint.sh

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Set Python path to use uv's virtual environment
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]