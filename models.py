from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False
    
class TodoItem(TodoCreate):
    id:int 
    created_at: datetime
    updated_at: Optional[datetime] = None
    