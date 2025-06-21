#!/bin/sh

echo "🚀 Running DB init script..."
python app/scripts/init_db.py

echo "🚀 Starting FastAPI server..."
uvicorn app.infrastructure.api.main:app --host 0.0.0.0 --port 8000 --reload
