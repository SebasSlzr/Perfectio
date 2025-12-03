# app/middleware/__init__.py
"""
Middlewares y validaciones simples de Perfectio
"""

# Importar funciones de validación simples
from app.middleware.validation import (
    validate_email,
    validate_no_special_chars,
    validate_age,
    validate_password_strength,
    validate_username,
)
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

__all__ = [
   
    # Validaciones simples
    "validate_email",
    "validate_no_special_chars",
    "validate_age",
    "validate_password_strength",
    "validate_username",
]

def setup_validations(app: FastAPI):
    """Configurar validaciones globales de la aplicación"""
    # Registra un middleware que convierte ValidationErrors en respuestas JSON uniformes.
    @app.middleware("http")
    async def validation_error_handler(request: Request, call_next):
        try:
            return await call_next(request)
        except ValidationError as exc:
            return JSONResponse(status_code=422, content={"detail": exc.errors()})
