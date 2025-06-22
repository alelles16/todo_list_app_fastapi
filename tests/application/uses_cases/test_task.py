from typing import List, Optional
from app.domain.models.task import Task
from app.application.uses_cases.task import (
    create_task,
    get_task,
    update_task,
    delete_task,
    update_task_status,
    get_tasks_by_list,
)


class FakeTaskRepository:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def create(self, task: Task) -> Task:
        task.id = self.counter
        self.counter += 1
        self.tasks.append(task)
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return next((task for task in self.tasks if task.id == task_id), None)

    def update(self, task_id: int, updated_task: Task) -> Optional[Task]:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks[i] = updated_task
                return updated_task
        return None

    def delete(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def get_all_by_todo_list(self, todo_list_id: int) -> List[Task]:
        return [task for task in self.tasks if task.todo_list_id == todo_list_id]


def test_create_task():
    repo = FakeTaskRepository()
    task = create_task(repo, "Test Task", "Description", 1)
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.status == "pending"


def test_get_task():
    repo = FakeTaskRepository()
    created = create_task(repo, "Another Task", "", 2)
    result = get_task(repo, created.id)
    assert result is not None
    assert result.id == created.id


def test_update_task():
    repo = FakeTaskRepository()
    original = create_task(repo, "Original", "Desc", 1)
    updated = update_task(repo, original.id, "New Title", None, "done", None, True)
    assert updated.title == "New Title"
    assert updated.status == "done"
    assert updated.completed is True


def test_delete_task():
    repo = FakeTaskRepository()
    task = create_task(repo, "Delete me", "", 1)
    result = delete_task(repo, task.id)
    assert result is True
    assert repo.get_by_id(task.id) is None


def test_update_task_status():
    repo = FakeTaskRepository()
    task = create_task(repo, "Status change", "", 1)
    updated = update_task_status(repo, task.id, "done")
    assert updated.status == "done"
    assert updated.completed is True


def test_get_tasks_by_list_with_filters():
    repo = FakeTaskRepository()
    create_task(repo, "T1", "", 1, status="done", completed=True)
    create_task(repo, "T2", "", 1, status="pending")
    create_task(repo, "T3", "", 1, status="in_progress")
    create_task(repo, "T4", "", 2, status="done")

    tasks, percent = get_tasks_by_list(repo, todo_list_id=1)
    assert len(tasks) == 3
    assert percent == 33.33

    done_tasks, _ = get_tasks_by_list(repo, todo_list_id=1, status="done")
    assert len(done_tasks) == 1

    high_priority_tasks, _ = get_tasks_by_list(repo, todo_list_id=1, priority="high")
    assert high_priority_tasks == []
