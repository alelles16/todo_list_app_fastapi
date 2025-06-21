from pydantic import BaseModel, Field
from typing import Optional


# Data model for tasks
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = Field(default="pending", regex="^(pending|in_progress|done)$")
    priority: Optional[str] = Field(default="normal", regex="^(low|normal|high)$")


# Data allowed when creating a new task
class TaskCreate(TaskBase):
    todo_list_id: int
    assigned_user_id: int


# Data allowed when updating an existing task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = Field(default=None, regex="^(pending|in_progress|done)$")
    priority: Optional[str] = Field(default=None, regex="^(low|normal|high)$")
    completed: Optional[bool] = None
    assigned_user_id: Optional[int] = None


# Allowed data when reading a task
class TaskRead(TaskBase):
    id: int
    completed: bool
    todo_list_id: int
    assigned_user_id: int

    class Config:
        orm_mode = True
