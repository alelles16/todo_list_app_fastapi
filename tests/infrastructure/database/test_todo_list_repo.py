import pytest
from app.infrastructure.database.repositories.todo_list_repo_impl import (
    TodoListRepositoryImpl,
)
from app.domain.models.todo_list import TodoList


@pytest.fixture
def repository(db_session):
    return TodoListRepositoryImpl(db_session)


def test_create_todo_list(repository):
    todo = TodoList(id=None, title="Mi Lista", description="Descripción de prueba")
    created = repository.create(todo)
    assert created.id is not None
    assert created.title == "Mi Lista"
    assert created.description == "Descripción de prueba"


def test_get_all(repository):
    repository.create(TodoList(None, "Lista 1", "Desc 1"))
    repository.create(TodoList(None, "Lista 2", "Desc 2"))
    result = repository.get_all()
    assert len(result) >= 2
    titles = [todo.title for todo in result]
    assert "Lista 1" in titles
    assert "Lista 2" in titles


def test_get_by_id(repository):
    todo = repository.create(TodoList(None, "Buscar", "Desc"))
    fetched = repository.get_by_id(todo.id)
    assert fetched is not None
    assert fetched.title == "Buscar"


def test_get_by_id_not_found(repository):
    assert repository.get_by_id(99999) is None


def test_update_todo_list(repository):
    original = repository.create(TodoList(None, "Original", "Old desc"))
    updated_data = TodoList(id=original.id, title="Actualizado", description="New desc")
    updated = repository.update(original.id, updated_data)
    assert updated.title == "Actualizado"
    assert updated.description == "New desc"


def test_update_not_found(repository):
    fake = TodoList(id=99999, title="X", description="Y")
    assert repository.update(99999, fake) is None


def test_delete_todo_list(repository):
    todo = repository.create(TodoList(None, "Borrar", "Eliminar esto"))
    success = repository.delete(todo.id)
    assert success is True
    assert repository.get_by_id(todo.id) is None


def test_delete_not_found(repository):
    assert repository.delete(123456) is False
