from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.api.schemas.user import UserCreate, UserLogin, UserRead
from app.infrastructure.database.repositories.user_repo_impl import UserRepositoryImpl
from app.infrastructure.config import get_db
from app.application.services.auth_service import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.domain.models.user import User


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)) -> UserRead:
    user_repo = UserRepositoryImpl(db)
    if user_repo.get_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hash_password(user.password)
    new_user = user_repo.create(
        User(
            id=None,
            username=user.email,
            email=user.email,
            password=hashed_password,
        )
    )
    return UserRead(
        id=new_user.id,
        username=new_user.email,
        email=new_user.email,
    )


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    user_repo = UserRepositoryImpl(db)
    db_user = user_repo.get_by_email(user.email)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(db_user)
    return {"access_token": token, "token_type": "bearer", "user": UserRead(
        id=db_user.id,
        username=db_user.email,
        email=db_user.email,
    )}
