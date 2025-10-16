# /schemas/auth_schema.py

from typing import Optional
from pydantic import BaseModel, EmailStr


# --- BASE SCHEMAS ---
# Estructuras de datos para registro, login y respuestas.


class UserBase(BaseModel):
    """Campos base del usuario."""
    username: str
    email: EmailStr


# --- REGISTER SCHEMA ---
class UserRegister(UserBase):
    """Datos necesarios para registrar un nuevo usuario."""
    password: str  # Contraseña en texto plano, se encripta antes de guardar


# --- LOGIN SCHEMA ---
class UserLogin(BaseModel):
    """Datos requeridos para iniciar sesión."""
    email: EmailStr
    password: str


# --- RESPONSE SCHEMAS ---
class UserPublic(UserBase):
    """Datos públicos del usuario (se devuelven al cliente)."""
    id_user: int

    class Config:
        from_attributes = True  # Permite mapear desde modelos ORM


class TokenResponse(BaseModel):
    """Respuesta al hacer login (contiene el token JWT)."""
    access_token: str
    token_type: str = "bearer"
    msg: Optional[str] = "Login exitoso"


class LogoutResponse(BaseModel):
    """Respuesta al cerrar sesión."""
    msg: str = "Logout exitoso"
