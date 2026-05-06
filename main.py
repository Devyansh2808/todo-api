from fastapi import Depends, FastAPI, HTTPException
from models import *
from datetime import datetime
from database import Base, engine, SessionLocal
from database_models import ToDoItem
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "hello"}

@app.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    print(f"Creating todo: {todo}")  # ADD THIS
    todo_item = ToDoItem(
        title=todo.title,
        description=todo.description,
        completed=todo.done
    )
    print(f"Before commit: {todo_item}")  # ADD THIS
    db.add(todo_item)
    db.commit()
    print(f"After commit: {todo_item}")  # ADD THIS
    db.refresh(todo_item)
    return todo_item

@app.get("/todos")
def read_todos(db: Session = Depends(get_db)):
    return db.query(ToDoItem).all()

@app.get("/todos/{todo_id}")
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_item = db.query(ToDoItem).filter(ToDoItem.id == todo_id).first()
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo_item

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_item = db.query(ToDoItem).filter(ToDoItem.id == todo_id).first()
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo_item)
    db.commit()
    return todo_item

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    todo_item = db.query(ToDoItem).filter(ToDoItem.id == todo_id).first()
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo_item.title = todo.title
    todo_item.description = todo.description
    todo_item.completed = todo.done
    todo_item.updated_at = datetime.now()
    db.commit()
    db.refresh(todo_item)
    return todo_item