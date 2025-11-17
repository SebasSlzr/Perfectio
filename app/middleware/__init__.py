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

__all__ = [
   
    # Validaciones simples
    "validate_email",
    "validate_no_special_chars",
    "validate_age",
    "validate_password_strength",
    "validate_username",
]

def setup_validations(app):
    """Configurar validaciones globales de la aplicación"""
    pass
