from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.todo_list import TodoList


class TodoListRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TodoList]:
        """Retrieve all todo lists."""
        pass

    @abstractmethod
    def get_by_id(self, todo_list_id: int) -> Optional[TodoList]:
        """Retrieve a todo list by its ID."""
        pass

    @abstractmethod
    def create(self, todo_list: TodoList) -> TodoList:
        """Create a new todo list."""
        pass

    @abstractmethod
    def update(self, todo_list_id: int, updated_list: TodoList) -> Optional[TodoList]:
        """Update an existing todo list."""
        pass

    @abstractmethod
    def delete(self, todo_list_id: int) -> bool:
        """Delete a todo list by its ID."""
        pass
