from pydantic import BaseModel, Field
from typing import Optional, List
from .task import TaskRead


class TodoListCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=10)


class TodoListUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=10)


class TodoListRead(BaseModel):
    id: int
    title: str
    description: Optional[str]


class TodoListWithTasks(TodoListRead):
    tasks: List[TaskRead] = []
