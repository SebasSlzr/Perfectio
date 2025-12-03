# app/routes/user_routes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import User, UserCreate, UserUpdate
from app.controllers import user_controller as controller

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Usuario no encontrado"}},
)


@router.get(
    "/",
    response_model=list[User],
    summary="Listar usuarios",
    description="Devuelve todos los usuarios registrados.",
    response_description="Colección de usuarios.",
)
async def list_users(db: AsyncSession = Depends(get_db)):
    return await controller.get_all_users(db)


@router.get(
    "/{user_id}",
    response_model=User,
    summary="Obtener usuario",
    description="Devuelve la información de un usuario específico.",
    response_description="Datos del usuario solicitado.",
)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await controller.get_user_by_id(user_id, db)


@router.post(
    "/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Crear usuario",
    description="Registra un usuario con sus credenciales y perfil.",
    response_description="Usuario creado correctamente.",
)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await controller.create_user(user, db)


@router.put(
    "/{user_id}",
    response_model=User,
    summary="Actualizar usuario",
    description="Modifica los datos de un usuario existente.",
    response_description="Usuario actualizado.",
)
async def update_user(user_id: int, user: UserUpdate, db: AsyncSession = Depends(get_db)):
    return await controller.update_user(user_id, user, db)


@router.delete(
    "/{user_id}",
    summary="Eliminar usuario",
    description="Elimina al usuario indicado.",
    responses={200: {"description": "Usuario eliminado correctamente."}},
)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await controller.delete_user(user_id, db)
