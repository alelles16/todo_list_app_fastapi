from abc import ABC, abstractmethod
from typing import Optional
from app.domain.models.user import User


class UserRepository(ABC):

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        """Retrieve a user by their email."""
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        """Create a new user."""
        pass
