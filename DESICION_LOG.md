# DECISION_LOG.md

## 📌 Project Overview

This project is a **Todo List API** implemented in **FastAPI** following the principles of **Clean Architecture**, with a clear separation between domain models, use cases, repositories, and infrastructure. The project supports CRUD operations for Todo Lists and Tasks, including advanced features like filtered retrieval and completion percentage calculations.

---

## ✅ Major Technical Decisions

### 1. **Use of Clean Architecture**
- **Why**: To maintain separation of concerns, enhance testability, and support scalability.
- **Impact**: Logic is distributed into:
  - `domain`: business rules (models, repository interfaces).
  - `application`: use cases.
  - `infrastructure`: database models, repository implementations, API routes.

---


### 3. **Repository Pattern**
- Abstract repositories were defined in `domain.repositories`.
- Implemented using SQLAlchemy in `infrastructure.database.repositories`.

🔄 This allows swapping data sources (e.g., switch to NoSQL) without touching business logic.

---

### 4. **Validation Logic in Pydantic Schemas**
- Fields like `status` and `priority` use **regex pattern validation**.
- Custom logic added, such as:
  - `title` minimum length of 3 characters.
  - `description` optional but validated if provided.

📎 This avoids repetitive validation code in routes or use cases.

---

### 5. **Swagger UI (OpenAPI)**
- Enabled by FastAPI by default.
- Available at: `http://localhost:8000/docs` for testing endpoints.
- This enhances **developer experience** and facilitates integration testing.

---

### 6. **Error Handling with HTTPException**
- Consistent error handling using FastAPI’s `HTTPException`.
- Custom status codes for 404 (not found) and 422 (validation errors).
- Planned: add global exception handlers for business rule violations.

---

### 7. **Testing Strategy**
- **Unit tests** for use cases with **fake repositories** (no DB dependency).
- **Integration tests** for API routes using FastAPI `TestClient`.
- Database is spun up with SQLite in `tests/conftest.py` to keep tests isolated.

---

### 8. **Formatting & Linting**
- Code style enforced with:
  - `black`: autoformatter for consistent style.
  - `flake8`: linter to catch bad patterns or unused code.
- A `.flake8` config was added to ignore specific warnings like `E501` (line too long).

---

### 9. **Docker & Entrypoint**
- A `Dockerfile` and `entrypoint.sh` simplify setup:
  - Automatic DB migration (`create_all`)
  - App startup via `uvicorn`.
- `docker-compose` support can be added for DB services if scaling up.

---

### 10. **Advanced Features Implemented**
- Endpoint to get tasks by list with optional filters by `status` and `priority`.
- Completion percentage is calculated based on how many tasks are marked as "done".
- This logic is encapsulated in `get_tasks_by_list` use case.

---

## 📅 Future Improvements

- Add authentication/authorization (e.g., JWT).
- Add pagination for large data sets.
- Enhance logging and monitoring.
- Add Celery (e.g., recurring task reminders).
- Add pre-commit hooks for enforcing formatting and linting before commits.
- Migrate to PostgreSQL for better performance and scalability in production.
- Use Poetry as a dependency manager with Docker for clean reproducible builds.
- Improve OpenAPI documentation with detailed schemas and response examples.
- Add .envs files to store credentials.

---

_Last updated: 2025-06-22_
