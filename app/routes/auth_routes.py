# app/routes/auth_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import AuthRegister, AuthLogin, AuthUser, AuthToken
from app.controllers.user_controller import create_user
from app.schemas.user_schema import UserCreate

router = APIRouter()

@router.post("/register", response_model=AuthUser)
async def register(user: AuthRegister, db: AsyncSession = Depends(get_db)):
    # Convertir AuthRegister a UserCreate
    user_data = UserCreate(
        username=user.username,
        name=user.name,
        email=user.email,
        password=user.password
    )
    # Crear usuario usando el controller
    created_user = await create_user(user_data, db)
    return created_user


@router.post("/login", response_model=AuthToken)
async def login(credentials: AuthLogin, db: AsyncSession = Depends(get_db)):

    return {"access_token": "fake_token", "token_type": "bearer"}