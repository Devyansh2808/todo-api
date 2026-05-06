from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False
    
class TodoItem(TodoCreate):
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True
    