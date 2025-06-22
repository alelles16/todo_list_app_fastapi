import pytest
from app.domain.models.todo_list import TodoList
from app.application.uses_cases.todo_list import (
    create_todo_list,
    get_all_todo_lists,
    get_todo_list_by_id,
    update_todo_list,
    delete_todo_list,
)


class FakeTodoListRepository:
    def __init__(self):
        self.todo_lists = []
        self.counter = 1

    def create(self, todo_list: TodoList) -> TodoList:
        todo_list.id = self.counter
        self.counter += 1
        self.todo_lists.append(todo_list)
        return todo_list

    def get_all(self) -> list[TodoList]:
        return self.todo_lists

    def get_by_id(self, todo_list_id: int) -> TodoList | None:
        return next((t for t in self.todo_lists if t.id == todo_list_id), None)

    def update(self, todo_list_id: int, updated_list: TodoList) -> TodoList | None:
        for idx, t in enumerate(self.todo_lists):
            if t.id == todo_list_id:
                self.todo_lists[idx] = updated_list
                updated_list.id = todo_list_id
                return updated_list
        return None

    def delete(self, todo_list_id: int) -> bool:
        for t in self.todo_lists:
            if t.id == todo_list_id:
                self.todo_lists.remove(t)
                return True
        return False


@pytest.fixture
def repo():
    return FakeTodoListRepository()


def test_create_todo_list(repo):
    result = create_todo_list(repo, title="Comprar", description="Comprar verduras")
    assert result.id == 1
    assert result.title == "Comprar"
    assert result.description == "Comprar verduras"


def test_get_all_todo_lists(repo):
    create_todo_list(repo, "Tarea 1")
    create_todo_list(repo, "Tarea 2")
    results = get_all_todo_lists(repo)
    assert len(results) == 2
    assert results[0].title == "Tarea 1"


def test_get_todo_list_by_id(repo):
    todo = create_todo_list(repo, "Buscar llaves")
    found = get_todo_list_by_id(repo, todo.id)
    assert found is not None
    assert found.id == todo.id
    assert found.title == "Buscar llaves"


def test_update_todo_list(repo):
    todo = create_todo_list(repo, "Viejo título", "Vieja desc")
    updated = update_todo_list(
        repo, todo.id, title="Nuevo título", description="Nueva desc"
    )
    assert updated is not None
    assert updated.title == "Nuevo título"
    assert updated.description == "Nueva desc"


def test_delete_todo_list(repo):
    todo = create_todo_list(repo, "Eliminar esto")
    success = delete_todo_list(repo, todo.id)
    assert success
    assert get_todo_list_by_id(repo, todo.id) is None
