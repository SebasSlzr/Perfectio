# app/schemas/auth_schema.py
from typing import Optional
from pydantic import BaseModel

class AuthBase(BaseModel):
    """Base para autenticacion"""
    username: str
    name: str
    email: str
    password: str

class AuthRegister(AuthBase):
    """Registro de usuario"""
    pass

class AuthLogin(BaseModel):
    """Login de usuario"""
    username: str
    password: str

class AuthUser(BaseModel):
    """Usuario para respuesta"""
    id_user: int
    username: str
    name: str
    email: str

    class Config:
        from_attributes = True

class AuthToken(BaseModel):
    """Token de autenticacion"""
    access_token: str
    token_type: str = "bearer"