# app/schemas/user_schema.py
from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    """Base para usuario"""
    username: str
    name: str
    email: str

class UserCreate(UserBase):
    """Crear usuario"""
    password: str

class UserUpdate(BaseModel):
    """Actualizar usuario"""
    username: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class User(UserBase):
    """Usuario completo"""
    id_user: int

    class Config:
        from_attributes = True