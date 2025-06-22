# tests/infrastructure/api/routes/test_task_routes.py

import pytest
from fastapi.testclient import TestClient
from app.infrastructure.api.main import app

client = TestClient(app)


@pytest.fixture
def sample_todo_list(client):
    response = client.post(
        "/todo_lists/", json={"title": "List A", "description": "description A"}
    )
    return response.json()


@pytest.fixture
def sample_task_data(sample_todo_list):
    return {
        "title": "Test Task",
        "description": "Task description",
        "status": "pending",
        "priority": "normal",
        "todo_list_id": sample_todo_list["id"],
    }


def test_create_task(client, sample_task_data):
    response = client.post("/tasks/", json=sample_task_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == sample_task_data["title"]
    assert data["status"] == "pending"


def test_get_task(client, sample_task_data):
    create_response = client.post("/tasks/", json=sample_task_data)
    task_id = create_response.json()["id"]

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == task_id


def test_update_task(client, sample_task_data):
    create_response = client.post("/tasks/", json=sample_task_data)
    task_id = create_response.json()["id"]

    updated = {
        "title": "Updated Task",
        "description": "Updated description",
        "status": "in_progress",
        "priority": "high",
        "completed": True,
    }

    response = client.put(f"/tasks/{task_id}", json=updated)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["priority"] == "high"


def test_update_task_status(client, sample_task_data):
    create_response = client.post("/tasks/", json=sample_task_data)
    task_id = create_response.json()["id"]

    response = client.patch(f"/tasks/{task_id}/status", json={"status": "done"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "done"
    assert data["completed"] is True


def test_delete_task(client, sample_task_data):
    create_response = client.post("/tasks/", json=sample_task_data)
    task_id = create_response.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404


def test_get_tasks_by_list(client, sample_task_data):
    client.post("/tasks/", json=sample_task_data)
    response = client.get(f"/tasks/by_list/{sample_task_data['todo_list_id']}")
    assert response.status_code == 200
    data = response.json()
    assert "tasks" in data
    assert "completion_percentage" in data


def test_failed_get_invalid_task(client):
    response = client.get("/tasks/999999")
    assert response.status_code == 404


def test_failed_update_nonexistent_task(client):
    updated = {
        "title": "Fake",
        "description": "Fake desc",
        "status": "done",
        "priority": "low",
        "completed": True,
    }
    response = client.put("/tasks/999999", json=updated)
    assert response.status_code == 404


def test_failed_delete_nonexistent_task(client):
    response = client.delete("/tasks/999999")
    assert response.status_code == 404


def test_failed_create_task_invalid_status(client, sample_todo_list):
    task = {
        "title": "Invalid Task",
        "description": "desc",
        "status": "wrong_status",
        "priority": "normal",
        "todo_list_id": sample_todo_list["id"],
    }
    response = client.post("/tasks/", json=task)
    assert response.status_code == 422


def test_failed_update_status_invalid_value(client, sample_task_data):
    create_response = client.post("/tasks/", json=sample_task_data)
    task_id = create_response.json()["id"]

    response = client.patch(f"/tasks/{task_id}/status", json={"status": "banana"})
    assert response.status_code == 422
