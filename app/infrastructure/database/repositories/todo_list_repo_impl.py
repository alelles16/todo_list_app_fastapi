from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.repositories.todo_list_repo import TodoListRepository
from app.domain.models.todo_list import TodoList
from app.infrastructure.database.models.todo_list import TodoListModel


class TodoListRepositoryImpl(TodoListRepository):
    def __init__(self, db: Session):
        self.db = db

    def _to_domain(self, model: TodoListModel) -> TodoList:
        return TodoList(
            id=model.id,
            title=model.title,
            description=model.description
        )

    def get_all(self) -> List[TodoList]:
        results = self.db.query(TodoListModel).all()
        return [self._to_domain(todo) for todo in results]

    def get_by_id(self, todo_list_id: int) -> Optional[TodoList]:
        todo = self.db.query(TodoListModel).filter(TodoListModel.id == todo_list_id).first()
        return self._to_domain(todo) if todo else None

    def create(self, todo_list: TodoList) -> TodoList:
        db_model = TodoListModel(
            title=todo_list.title,
            description=todo_list.description
        )
        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)
        return self._to_domain(db_model)

    def update(self, todo_list_id: int, updated_list: TodoList) -> Optional[TodoList]:
        db_model = self.db.query(TodoListModel).filter(TodoListModel.id == todo_list_id).first()
        if not db_model:
            return None
        db_model.title = updated_list.title
        db_model.description = updated_list.description
        self.db.commit()
        self.db.refresh(db_model)
        return self._to_domain(db_model)

    def delete(self, todo_list_id: int) -> bool:
        db_model = self.db.query(TodoListModel).filter(TodoListModel.id == todo_list_id).first()
        if not db_model:
            return False
        self.db.delete(db_model)
        self.db.commit()
        return True
