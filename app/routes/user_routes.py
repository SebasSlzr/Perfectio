# app/routes/user_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas import User, UserCreate, UserUpdate

router = APIRouter()

@router.get("/", response_model=list[User])
async def list_users(db: AsyncSession = Depends(get_db)):
    return {"msg": "Lista de todos los usuarios"}

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Información del usuario {user_id}"}

@router.post("/", response_model=User)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return {"msg": "Usuario creado correctamente"}

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Usuario {user_id} actualizado"}

@router.delete("/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Usuario {user_id} eliminado"}