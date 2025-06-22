from pydantic import BaseModel, Field
from typing import Optional, List


class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=8)
    status: Optional[str] = Field(
        default="pending", pattern="^(pending|in_progress|done)$"
    )
    priority: Optional[str] = Field(default="normal", pattern="^(low|normal|high)$")


class TaskCreate(TaskBase):
    todo_list_id: int


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=8)
    status: Optional[str] = Field(None, pattern="^(pending|in_progress|done)$")
    priority: Optional[str] = Field(None, pattern="^(low|normal|high)$")
    completed: Optional[bool] = None


class TaskStatusUpdate(BaseModel):
    status: str = Field(..., pattern="^(pending|in_progress|done)$")


class TaskRead(TaskBase):
    id: int
    completed: bool
    todo_list_id: int


class TaskListWithCompletion(BaseModel):
    tasks: List[TaskRead]
    completion_percentage: float
