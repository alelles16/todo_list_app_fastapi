from pydantic import BaseModel
from typing import Optional, List
from .task import TaskRead


# Data allowed when creating a new todo list
class TodoListCreate(BaseModel):
    title: str
    description: Optional[str] = None


# Data allowed when updating an existing todo list
class TodoListUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Allowed data when reading a todo list
class TodoListRead(BaseModel):
    id: int
    title: str
    description: Optional[str]

    class Config:
        # Enable ORM mode to read data from ORM models
        orm_mode = True


# Allowed data when reading a todo list with its tasks
class TodoListWithTasks(TodoListRead):
    tasks: List[TaskRead] = []
