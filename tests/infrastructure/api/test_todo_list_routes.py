import pytest

from fastapi.testclient import TestClient
from app.infrastructure.api.main import app

client = TestClient(app)


@pytest.fixture
def sample_todo_data():
    return {"title": "My List", "description": "Sample description"}


def test_create_todo_list(client, sample_todo_data):
    response = client.post("/todo_lists/", json=sample_todo_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == sample_todo_data["title"]
    assert data["description"] == sample_todo_data["description"]
    assert "id" in data


def test_get_all_todo_lists(client, sample_todo_data):
    client.post("/todo_lists/", json=sample_todo_data)
    response = client.get("/todo_lists/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert all("title" in item for item in data)


def test_get_todo_list_by_id(client, sample_todo_data):
    post_response = client.post("/todo_lists/", json=sample_todo_data)
    todo_id = post_response.json()["id"]

    response = client.get(f"/todo_lists/{todo_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == todo_id
    assert data["title"] == sample_todo_data["title"]


def test_update_todo_list(client, sample_todo_data):
    post_response = client.post("/todo_lists/", json=sample_todo_data)
    todo_id = post_response.json()["id"]

    updated_data = {"title": "Updated Title", "description": "Updated description"}
    response = client.put(f"/todo_lists/{todo_id}", json=updated_data)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["description"] == "Updated description"


def test_delete_todo_list(client, sample_todo_data):
    post_response = client.post("/todo_lists/", json=sample_todo_data)
    todo_id = post_response.json()["id"]

    delete_response = client.delete(f"/todo_lists/{todo_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/todo_lists/{todo_id}")
    assert get_response.status_code == 404
