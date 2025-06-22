from typing import List, Optional
from app.domain.models.task import Task
from app.domain.repositories.task_repo import TaskRepository


def create_task(
    repository: TaskRepository,
    title: str,
    description: Optional[str],
    todo_list_id: int,
    status: str = "pending",
    priority: str = "normal",
    completed: bool = False,
) -> Task:
    task = Task(
        id=None,
        title=title,
        description=description,
        status=status,
        priority=priority,
        completed=completed,
        todo_list_id=todo_list_id,
    )
    return repository.create(task)


def get_task(repository: TaskRepository, task_id: int) -> Optional[Task]:
    return repository.get_by_id(task_id)


def get_tasks_by_list(repository: TaskRepository, todo_list_id: int) -> List[Task]:
    return repository.get_all_by_todo_list(todo_list_id)


def update_task(
    repository: TaskRepository,
    task_id: int,
    title: Optional[str],
    description: Optional[str],
    status: Optional[str],
    priority: Optional[str],
    completed: Optional[bool],
) -> Optional[Task]:
    existing_task = repository.get_by_id(task_id)
    if not existing_task:
        return None
    updated = Task(
        id=existing_task.id,
        title=title or existing_task.title,
        description=description or existing_task.description,
        status=status or existing_task.status,
        priority=priority or existing_task.priority,
        completed=completed if completed is not None else existing_task.completed,
        todo_list_id=existing_task.todo_list_id,
    )
    return repository.update(task_id, updated)


def delete_task(repository: TaskRepository, task_id: int) -> bool:
    return repository.delete(task_id)
