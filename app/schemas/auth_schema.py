# app/schemas/auth_schema.py
from typing import Optional
from pydantic import BaseModel, field_validator

# Importar las validaciones
from app.middleware import (
    validate_email,
    validate_password_strength,
    validate_username
)

class AuthBase(BaseModel):
    """Base para autenticacion"""
    username: str
    name: str
    email: str
    password: str
    
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
    
class SuccessResponse(BaseModel):
    """Respuesta de éxito"""
    message: str
    data: Optional[dict] = None