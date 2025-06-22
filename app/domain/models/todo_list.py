from typing import Optional


class TodoList:

    def __init__(
        self,
        id: Optional[int],
        title: str,
        description: Optional[str],
    ):
        self.id = id
        self.title = title
        self.description = description
