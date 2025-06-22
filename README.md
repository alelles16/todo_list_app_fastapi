# 📝 Todo List App - FastAPI

This project is a simple **Todo List App** built with **FastAPI**, following **Clean Architecture** principles. It includes full CRUD operations for todo lists and tasks, along with filtering and completion tracking.

---

## 📌 Features

- ✅ Create, read, update and delete todo lists.
- ✅ Add tasks to a list with status, priority, and completion tracking.
- ✅ Filter tasks by `status` or `priority`.
- ✅ Calculate completion percentage per list.
- ✅ FastAPI + Pydantic validations + SQLite.
- ✅ Clean architecture with domain, use cases, and infrastructure layers.
- ✅ Unit tests with Pytest.
- ✅ Code linting with flake8 and formatting with black.

---

## ⚙️ Requirements

- Python 3.10+
- Docker + Docker Compose
- Poetry

---

## ⚙️ Local Setup

1. **Clone the repository:**

```bash
git clone https://github.com/your-user/todo-list-fastapi.git
cd todo-list-fastapi
```

2. **Create a virtual environment and activate it:**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

4. **Run the app with the provided entrypoint:**

```bash
sh entrypoint.sh
```

This script will:
- Set up the SQLite database
- Start the FastAPI app with Uvicorn

The API will be available at: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Running with Docker

1. **Build and Run the Docker image:**

```bash
docker build .
docker-compose build
docker-compose up
```

---

## 🧪 Testing the API

Swagger/OpenAPI documentation available at:

🔗 [http://localhost:8000/docs](http://localhost:8000/docs)

You can interact with all endpoints directly from the Swagger UI.

---

## 📬 Available Endpoints

### Todo Lists

| Method | Endpoint             | Description                  |
|--------|----------------------|------------------------------|
| GET    | `/todo_lists/`       | Get all todo lists           |
| POST   | `/todo_lists/`       | Create a new todo list       |
| GET    | `/todo_lists/{id}`   | Get a todo list by ID        |
| PUT    | `/todo_lists/{id}`   | Update a todo list           |
| DELETE | `/todo_lists/{id}`   | Delete a todo list           |

### Tasks

| Method | Endpoint                           | Description                            |
|--------|------------------------------------|----------------------------------------|
| GET    | `/tasks/{id}`                      | Get a task by ID                       |
| POST   | `/tasks/`                          | Create a new task                      |
| PUT    | `/tasks/{id}`                      | Update a task                          |
| PATCH  | `/tasks/{id}/status`               | Update task status                     |
| DELETE | `/tasks/{id}`                      | Delete a task                          |
| GET    | `/tasks/by_list/{todo_list_id}`    | Get tasks by list, with filters        |

Supports query filters: `?status=pending&priority=high`

---

## 🧹 Code Style & Formatting

### Run flake8 (linting):

```bash
flake8 .
```

### Run black (code formatter):

```bash
black .
```

---

## 🧪 Running Tests

Make sure your test DB is set up via `tests/conftest.py`. Then:

```bash
pytest
```

To run tests with coverage report:

```bash
pytest --cov
```

---

## 📁 Project Structure

```
app/
├── application/
│   └── use_cases/
├── domain/
│   └── models/
│   └── repositories/
├── infrastructure/
│   ├── api/
│   └── database/
├── config.py
tests/
│   ├── application/
│   ├── infrastructure/
│   └── conftest.py
entrypoint.sh
```

---

## 🧾 License

MIT © Your Name
