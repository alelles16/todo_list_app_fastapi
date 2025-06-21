from typing import Optional

class Task:
    def __init__(
        self,
        id: Optional[int],
        title: str,
        description: Optional[str],
        status: str,
        priority: str,
        completed: bool,
        todo_list_id: int
    ):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.completed = completed
        self.todo_list_id = todo_list_id
