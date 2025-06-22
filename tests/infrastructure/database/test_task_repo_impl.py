import pytest
from app.infrastructure.database.repositories.task_repo_impl import TaskRepositoryImpl
from app.infrastructure.database.models.todo_list import TodoListModel
from app.domain.models.task import Task


@pytest.fixture
def repository(db_session):
    return TaskRepositoryImpl(db_session)


@pytest.fixture
def sample_todo_list(db_session):
    todo = TodoListModel(title="Lista Test", description="Lista de prueba")
    db_session.add(todo)
    db_session.commit()
    db_session.refresh(todo)
    return todo


def test_create_task(repository, sample_todo_list):
    task = Task(
        None,
        "Test Task",
        "Descripción",
        "pending",
        "normal",
        False,
        sample_todo_list.id,
    )
    created = repository.create(task)
    assert created.id is not None
    assert created.title == "Test Task"


def test_get_by_id(repository, sample_todo_list):
    created = repository.create(
        Task(None, "Buscar", "...", "pending", "low", False, sample_todo_list.id)
    )
    found = repository.get_by_id(created.id)
    assert found is not None
    assert found.title == "Buscar"


def test_get_by_id_not_found(repository):
    result = repository.get_by_id(999999)
    assert result is None


def test_get_all_by_todo_list(repository, sample_todo_list):
    repository.create(
        Task(None, "T1", "...", "pending", "low", False, sample_todo_list.id)
    )
    repository.create(
        Task(None, "T2", "...", "done", "high", True, sample_todo_list.id)
    )
    tasks = repository.get_all_by_todo_list(sample_todo_list.id)
    assert len(tasks) == 2
    assert any(t.title == "T2" for t in tasks)


def test_update_task(repository, sample_todo_list):
    task = repository.create(
        Task(None, "T-Old", "...", "pending", "normal", False, sample_todo_list.id)
    )
    updated = Task(
        task.id, "T-New", "New desc", "done", "high", True, sample_todo_list.id
    )
    result = repository.update(task.id, updated)
    assert result.title == "T-New"
    assert result.completed is True


def test_update_task_not_found(repository, sample_todo_list):
    fake = Task(9999, "X", "Y", "pending", "low", False, sample_todo_list.id)
    assert repository.update(9999, fake) is None


def test_delete_task(repository, sample_todo_list):
    task = repository.create(
        Task(None, "ToDelete", "...", "pending", "normal", False, sample_todo_list.id)
    )
    result = repository.delete(task.id)
    assert result is True


def test_delete_task_not_found(repository):
    assert repository.delete(123456) is False
