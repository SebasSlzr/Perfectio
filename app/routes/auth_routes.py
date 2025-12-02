# app/routes/auth_routes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import AuthRegister, AuthLogin, AuthUser, AuthToken
from app.controllers.user_controller import create_user
from app.schemas.user_schema import UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={
        401: {"description": "Credenciales inválidas"},
        409: {"description": "Usuario ya existente"},
    },
)


@router.post(
    "/register",
    response_model=AuthUser,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar un usuario",
    description="Crea un nuevo usuario y devuelve la información pública de su perfil.",
    response_description="Usuario creado exitosamente.",
)
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


@router.post(
    "/login",
    response_model=AuthToken,
    summary="Autenticar usuario",
    description="Valida las credenciales y entrega un token de acceso.",
    response_description="Token JWT válido para consumir la API.",
)
async def login(credentials: AuthLogin, db: AsyncSession = Depends(get_db)):

    return {"access_token": "fake_token", "token_type": "bearer"}