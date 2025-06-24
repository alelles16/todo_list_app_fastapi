from sqlalchemy.orm import Session
from app.domain.models.user import User
from app.domain.repositories.user_repo import UserRepository
from app.infrastructure.database.models.user import UserModel


class UserRepositoryImpl(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> User:
        user_model = self.db.query(UserModel).filter(email == email).first()
        if user_model:
            return User(
                id=user_model.id,
                username=user_model.email,
                email=user_model.email,
                password=user_model.password,
            )
        return None

    def create(self, user: User) -> User:
        user_model = UserModel(
            username=user.email, email=user.email, password=user.password
        )
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return User(
            id=user_model.id,
            username=user_model.email,
            email=user_model.email,
            password=user_model.password,
        )
