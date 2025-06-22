from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.infrastructure.api.schemas.task import TaskCreate, TaskRead, TaskUpdate
from app.infrastructure.database.repositories.task_repo_impl import TaskRepositoryImpl
from app.infrastructure.config import get_db
from app.application.uses_cases.task import (
    create_task,
    get_task,
    get_tasks_by_list,
    update_task,
    delete_task,
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskRead)
def create_task_route(task: TaskCreate, db: Session = Depends(get_db)) -> TaskRead:
    repository = TaskRepositoryImpl(db)
    created = create_task(
        repository=repository,
        title=task.title,
        description=task.description,
        todo_list_id=task.todo_list_id,
        status=task.status,
        priority=task.priority,
        completed=False
    )
    return TaskRead(**created.__dict__)


@router.get("/list/{todo_list_id}", response_model=List[TaskRead])
def get_tasks_by_list_route(todo_list_id: int, db: Session = Depends(get_db)) -> List[TaskRead]:
    repository = TaskRepositoryImpl(db)
    tasks = get_tasks_by_list(repository, todo_list_id)
    return [TaskRead(**task.__dict__) for task in tasks]


@router.get("/{task_id}", response_model=TaskRead)
def get_task_route(task_id: int, db: Session = Depends(get_db)) -> TaskRead:
    repository = TaskRepositoryImpl(db)
    task = get_task(repository, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskRead(**task.__dict__)


@router.put("/{task_id}", response_model=TaskRead)
def update_task_route(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)) -> TaskRead:
    repository = TaskRepositoryImpl(db)
    updated = update_task(
        repository=repository,
        task_id=task_id,
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
        completed=task.completed,
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskRead(**updated.__dict__)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_route(task_id: int, db: Session = Depends(get_db)):
    repository = TaskRepositoryImpl(db)
    success = delete_task(repository, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
