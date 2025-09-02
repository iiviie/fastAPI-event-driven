#!/bin/bash

set -e

echo "🚀 Starting Auth Service..."

# Wait for database to be ready
echo "⏳ Waiting for database to be ready..."
while ! pg_isready -h ${DATABASE_HOST:-postgres} -p ${DATABASE_PORT:-5432} -U ${DATABASE_USER:-auth_user} -d ${DATABASE_NAME:-auth_db}; do
    echo "Database is unavailable - sleeping"
    sleep 2
done

echo "✅ Database is ready!"

# Wait for Redis to be ready
echo "⏳ Waiting for Redis to be ready..."
while ! redis-cli -h ${REDIS_HOST:-redis} -p ${REDIS_PORT:-6379} ping | grep -q PONG; do
    echo "Redis is unavailable - sleeping"
    sleep 2
done

echo "✅ Redis is ready!"

# Run database migrations
echo "🔄 Running database migrations..."
alembic upgrade head

echo "✅ Migrations completed!"

# Start the application
echo "🌟 Starting FastAPI application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
