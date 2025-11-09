# app/routes/auth_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas import AuthRegister, AuthLogin, AuthUser, AuthToken

router = APIRouter()

@router.post("/register", response_model=AuthUser)
async def register(user: AuthRegister, db: AsyncSession = Depends(get_db)):
    return {"msg": "Usuario registrado correctamente"}

@router.post("/login", response_model=AuthToken)
async def login(credentials: AuthLogin, db: AsyncSession = Depends(get_db)):
    return {"msg": "Login exitoso", "access_token": "fake_token", "token_type": "bearer"}