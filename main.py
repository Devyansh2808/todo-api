from fastapi import FastAPI
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