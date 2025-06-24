from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.infrastructure.config import get_db
from app.infrastructure.database.repositories.user_repo_impl import UserRepositoryImpl
from app.application.services.auth_service import SECRET_KEY, ALGORITHM
from app.domain.models.user import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user_repo = UserRepositoryImpl(db)
    user = user_repo.get_by_email(email=email)
    if user is None:
        raise credentials_exception
    return user
