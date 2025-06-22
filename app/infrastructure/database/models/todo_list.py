from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.infrastructure.config import Base


class TodoListModel(Base):
    __tablename__ = "todo_lists"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    tasks = relationship(
        "TaskModel", back_populates="todo_list", cascade="all, delete-orphan"
    )
