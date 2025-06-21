from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.task import Task


class TaskRepository(ABC):

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID."""
        pass

    @abstractmethod
    def get_all_by_todo_list(self, todo_list_id: int) -> List[Task]:
        """Retrieve all tasks for a specific todo list."""
        pass

    @abstractmethod
    def create(self, task: Task) -> Task:
        """Create a new task."""
        pass

    @abstractmethod
    def update(self, task_id: int, updated_task: Task) -> Optional[Task]:
        """Update an existing task."""
        pass

    @abstractmethod
    def delete(self, task_id: int) -> bool:
        """Delete a task by its ID."""
        pass
