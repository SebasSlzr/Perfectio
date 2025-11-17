# app/schemas/user_schema.py
from typing import Optional
from pydantic import BaseModel, field_validator

# Importar las validaciones
from app.middleware import (
    validate_email,
    validate_password_strength,
    validate_username,
)

class UserBase(BaseModel):
    """Base para usuario"""
    username: str
    name: str
    email: str
    
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

class UserCreate(UserBase):
    """Crear usuario"""
    password: str
    
    @field_validator('password')
    def password_must_be_strong(cls, v):
        if not validate_password_strength(v):
            raise ValueError('Contraseña débil. Debe tener mínimo 8 caracteres, una mayúscula, una minúscula y un número')
        return v

class UserUpdate(BaseModel):
    """Actualizar usuario"""
    username: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    
    # Validador para email
    @field_validator('email')
    def email_must_be_valid(cls, v):
        if not validate_email(v):
            raise ValueError('Email inválido')
        return v
    
    # Validador para username
    @field_validator('username')
    def username_must_be_valid(cls, v):
        if not validate_username(v):
            raise ValueError('Username inválido. Solo letras, números y guiones bajos')
        return v
    
    # Validador para password
    @field_validator('password')
    def password_must_be_strong(cls, v):
        if not validate_password_strength(v):
            raise ValueError('Contraseña débil. Debe tener mínimo 8 caracteres, una mayúscula, una minúscula y un número')
        return v

class User(UserBase):
    """Usuario completo"""
    id_user: int

    class Config:
        from_attributes = True