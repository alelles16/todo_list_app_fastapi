from app.domain.models.todo_list import TodoList
from app.domain.repositories.todo_list_repo import TodoListRepository


def create_todo_list(
    repository: TodoListRepository,
    title: str,
    description: str | None = None,
) -> TodoList:
    """
    Create a new todo list.

    Args:
        repository (TodoListRepository): The repository to interact with the database.
        title (str): The title of the todo list.
        description (str | None): An optional description for the todo list.

    Returns:
        TodoList: The created todo list object.
    """
    todo_list = TodoList(id=None, title=title, description=description)
    return repository.create(todo_list)


def get_all_todo_lists(
    repository: TodoListRepository,
) -> list[TodoList]:
    """
    Retrieve all todo lists.

    Args:
        repository (TodoListRepository): The repository to interact with the database.

    Returns:
        list[TodoList]: A list of all todo lists.
    """
    return repository.get_all()


def get_todo_list_by_id(
    repository: TodoListRepository,
    todo_list_id: int,
) -> TodoList | None:
    """
    Retrieve a todo list by its ID.

    Args:
        repository (TodoListRepository): The repository to interact with the database.
        todo_list_id (int): The ID of the todo list to retrieve.

    Returns:
        TodoList | None: The todo list if found, otherwise None.
    """
    return repository.get_by_id(todo_list_id)


def update_todo_list(
    repository: TodoListRepository,
    todo_list_id: int,
    title: str | None = None,
    description: str | None = None,
) -> TodoList | None:
    """
    Update an existing todo list.

    Args:
        repository (TodoListRepository): The repository to interact with the database.
        todo_list_id (int): The ID of the todo list to update.
        title (str | None): The new title for the todo list.
        description (str | None): The new description for the todo list.

    Returns:
        TodoList | None: The updated todo list if found, otherwise None.
    """
    updated_list = TodoList(id=todo_list_id, title=title, description=description)
    return repository.update(todo_list_id, updated_list)


def delete_todo_list(
    repository: TodoListRepository,
    todo_list_id: int,
) -> bool:
    """
    Delete a todo list by its ID.

    Args:
        repository (TodoListRepository): The repository to interact with the database.
        todo_list_id (int): The ID of the todo list to delete.

    Returns:
        bool: True if the deletion was successful, otherwise False.
    """
    return repository.delete(todo_list_id)
