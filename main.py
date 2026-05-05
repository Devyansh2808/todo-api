from fastapi import FastAPI, HTTPException
from models import *
from datetime import datetime

todos = {}
next_id = 1

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hello"}

@app.post("/todos")
def create_todo(todo: TodoCreate):
    global next_id
    todo_item = TodoItem(**todo.model_dump(), id=next_id, created_at=datetime.now())
    todos[next_id] = todo_item
    next_id += 1
    return todo_item

@app.get("/todos")
def read_todos():
    return list(todos.values())

@app.get("/todos/{todo_id}")
def read_todo(todo_id: int):
    return todos.get(todo_id)

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos.pop(todo_id)

