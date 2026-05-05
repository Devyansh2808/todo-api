# Todo API

A simple REST API for managing todos built with FastAPI.

## Setup

1. Clone the repo and navigate to the project directory
2. Create a virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

## Running the server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

Interactive docs: `http://127.0.0.1:8000/docs`

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check |
| GET | `/todos` | Get all todos |
| GET | `/todos/{id}` | Get a specific todo |
| POST | `/todos` | Create a new todo |
| PUT | `/todos/{id}` | Update a todo |
| DELETE | `/todos/{id}` | Delete a todo |

## Creating a todo

Send a POST request to `/todos` with:
```json
{
  "title": "Buy groceries",
  "description": "milk, eggs",
  "done": false
}
```

All fields except `id`, `created_at`, and `updated_at` are user-provided. The API auto-generates timestamps.
