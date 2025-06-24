from sqlalchemy import Column, Integer, String
from app.infrastructure.config import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"<UserModel(id={self.id}, username={self.username}, email={self.email})>"
