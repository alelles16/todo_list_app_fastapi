from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.config import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    status = Column(String, default="pending")  # pending, in_progress, done
    priority = Column(String, default="normal")  # low, normal, high
    completed = Column(Boolean, default=False)

    # Foreign key relationships
    # The user assigned to the task
    assigned_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    assigned_user = relationship("UserModel", back_populates="tasks")

    # The todo list this task belongs to
    todo_list_id = Column(Integer, ForeignKey("todo_lists.id"), nullable=False)
    todo_list = relationship("TodoListModel", back_populates="tasks")

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, status={self.status}, priority={self.priority})>"

    def __str__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status}, priority={self.priority})"
