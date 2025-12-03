from typing import Optional
from pydantic import BaseModel, field_validator

# Importar las validaciones
from app.middleware import (
    validate_email,
    validate_password_strength,
    validate_username,
)


class UserCreate(BaseModel):
    """Schema para crear usuario (entrada)"""
    username: str
    name: str
    email: str
    password: str

    @field_validator('username')
    def username_must_be_valid(cls, v):
        if not validate_username(v):
            raise ValueError('Username inválido. Solo letras, números y guiones bajos')
        return v

    @field_validator('email')
    def email_must_be_valid(cls, v):
        if not validate_email(v):
            raise ValueError('Email inválido')
        return v

    @field_validator('password')
    def password_must_be_strong(cls, v):
        if not validate_password_strength(v):
            raise ValueError('Contraseña débil. Debe tener mínimo 8 caracteres, una mayúscula, una minúscula y un número')
        return v


class UserUpdate(BaseModel):
    """Schema para actualizar usuario (entrada)"""
    username: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    @field_validator('username')
    def username_must_be_valid(cls, v):
        if v is not None and not validate_username(v):
            raise ValueError('Username inválido. Solo letras, números y guiones bajos')
        return v

    @field_validator('email')
    def email_must_be_valid(cls, v):
        if v is not None and not validate_email(v):
            raise ValueError('Email inválido')
        return v

    @field_validator('password')
    def password_must_be_strong(cls, v):
        if v is not None and not validate_password_strength(v):
            raise ValueError('Contraseña débil. Debe tener mínimo 8 caracteres, una mayúscula, una minúscula y un número')
        return v



# SCHEMAS DE SALIDA 

class User(BaseModel):
    """Schema para devolver usuario (salida)"""
    id_user: int
    username: str
    name: str
    email: str

    class Config:
        from_attributes = True
