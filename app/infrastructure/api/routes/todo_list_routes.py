from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.infrastructure.api.schemas.todo_list import TodoListCreate, TodoListRead
from app.infrastructure.database.repositories.todo_list_repo_impl import TodoListRepositoryImpl
from app.application.uses_cases.todo_list import (
    create_todo_list, get_all_todo_lists, get_todo_list_by_id,
    update_todo_list, delete_todo_list,
)
from app.infrastructure.config import get_db

router = APIRouter(prefix="/todo_lists", tags=["Todo Lists"])


@router.post("/", response_model=TodoListRead)
def create_todo_list_route(todo_list: TodoListCreate, db: Session = Depends(get_db)) -> TodoListRead:
    repository = TodoListRepositoryImpl(db)
    created = create_todo_list(
        repository=repository,
        title=todo_list.title,
        description=todo_list.description,
    )
    return TodoListRead(**created.__dict__)


@router.get("/", response_model=List[TodoListRead])
def get_all_todo_lists_route(db: Session = Depends(get_db)):
    repository = TodoListRepositoryImpl(db)
    todos = get_all_todo_lists(
        repository=repository
    )
    return [TodoListRead(**todo.__dict__) for todo in todos]


@router.get("/{todo_list_id}", response_model=TodoListRead)
def get_todo_list_route(todo_list_id: int, db: Session = Depends(get_db)):
    repository = TodoListRepositoryImpl(db)
    todo = get_todo_list_by_id(
        repository=repository,
        todo_list_id=todo_list_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo list not found")
    return TodoListRead(**todo.__dict__)


@router.put("/{todo_list_id}", response_model=TodoListRead)
def update_todo_list_route(todo_list_id: int, todo_list: TodoListCreate, db: Session = Depends(get_db)):
    repository = TodoListRepositoryImpl(db)
    updated = update_todo_list(
        repository=repository,
        todo_list_id=todo_list_id,
        title=todo_list.title,
        description=todo_list.description)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo list not found")
    return TodoListRead(**updated.__dict__)


@router.delete("/{todo_list_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_list_route(todo_list_id: int, db: Session = Depends(get_db)):
    repository = TodoListRepositoryImpl(db)
    success = delete_todo_list(
        repository=repository,
        todo_list_id=todo_list_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo list not found")
