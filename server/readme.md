# Server

This folder contains the **API layer** for the project.

## Responsibilities
- HTTP routing
- Request validation
- File uploads
- Response formatting

## What this does NOT contain
- AI logic
- Embeddings
- Vector databases
- Model inference

All intelligence lives in the `/ai` service.

## Running locally

```bash

cd server

# create virtual environment
python -m venv venv

# activate virtual environment (macOS / Linux)
source venv/bin/activate

# activate virtual environment (Windows)
venv\Scripts\activate

pip install -r requirements.txt
gunicorn wsgi:app
