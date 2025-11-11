# app/routes/user_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import User, UserCreate, UserUpdate
from app.controllers import user_controller as controller

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[User])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await controller.get_all_users(db)

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await controller.get_user_by_id(user_id, db)

@router.post("/", response_model=User)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await controller.create_user(user, db)

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate, db: AsyncSession = Depends(get_db)):
    return await controller.update_user(user_id, user, db)

@router.delete("/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await controller.delete_user(user_id, db)
