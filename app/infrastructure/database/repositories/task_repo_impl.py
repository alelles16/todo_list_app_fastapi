from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.repositories.task_repo import TaskRepository
from app.domain.models.task import Task
from app.infrastructure.database.models.task import TaskModel


class TaskRepositoryImpl(TaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def _to_domain(self, model: TaskModel) -> Task:
        return Task(
            id=model.id,
            title=model.title,
            description=model.description,
            status=model.status,
            priority=model.priority,
            completed=model.completed,
            assigned_user_id=model.assigned_user_id,
            todo_list_id=model.todo_list_id
        )

    def get_by_id(self, task_id: int) -> Optional[Task]:
        task_model = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        return self._to_domain(task_model) if task_model else None

    def get_all_by_todo_list(self, todo_list_id: int) -> List[Task]:
        tasks_model = self.db.query(TaskModel).filter(TaskModel.todo_list_id == todo_list_id).all()
        return [self._to_domain(task) for task in tasks_model]

    def create(self, task: Task) -> Task:
        task_model = TaskModel(
            title=task.title,
            description=task.description,
            status=task.status,
            priority=task.priority,
            completed=task.completed,
            assigned_user_id=task.assigned_user_id,
            todo_list_id=task.todo_list_id
        )
        self.db.add(task_model)
        self.db.commit()
        self.db.refresh(task_model)
        return self._to_domain(task_model)

    def update(self, task_id: int, updated_task: Task) -> Optional[Task]:
        task_model = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if not task_model:
            return None
        task_model.title = updated_task.title
        task_model.description = updated_task.description
        task_model.status = updated_task.status
        task_model.priority = updated_task.priority
        task_model.completed = updated_task.completed
        task_model.assigned_user_id = updated_task.assigned_user_id
        task_model.todo_list_id = updated_task.todo_list_id

        self.db.commit()
        self.db.refresh(task_model)
        return self._to_domain(task_model)

    def delete(self, task_id: int) -> bool:
        task_model = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if not task_model:
            return False
        self.db.delete(task_model)
        self.db.commit()
        return True
