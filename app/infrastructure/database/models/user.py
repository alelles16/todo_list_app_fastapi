from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.infrastructure.config import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Relationship with tasks
    tasks = relationship("TaskModel", back_populates="assigned_user")

    def __repr__(self):
        return f"<UserModel(id={self.id}, username={self.username}, email={self.email})>"

    def __str__(self):
        return f"UserModel(id={self.id}, username={self.username}, email={self.email})"
