from pydantic import BaseModel, Field
from typing import Optional, List


# Data model for tasks
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = Field(default="pending", pattern="^(pending|in_progress|done)$")
    priority: Optional[str] = Field(default="normal", pattern="^(low|normal|high)$")


# Data allowed when creating a new task
class TaskCreate(TaskBase):
    todo_list_id: int


# Data allowed when updating an existing task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = Field(default=None, pattern="^(pending|in_progress|done)$")
    priority: Optional[str] = Field(default=None, pattern="^(low|normal|high)$")
    completed: Optional[bool] = None


# Allowed data when reading a task
class TaskRead(TaskBase):
    id: int
    completed: bool
    todo_list_id: int


# Data model for updating task status
class TaskStatusUpdate(BaseModel):
    status: str = Field(..., pattern="^(pending|in_progress|done)$")


# Data model for a list of tasks with completion percentage
class TaskListWithCompletion(BaseModel):
    tasks: List[TaskRead]
    completion_percentage: float
