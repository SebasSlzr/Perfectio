# app/middleware/validation.py
"""
Middleware simple para validaciones básicas de datos
"""
import re


def validate_email(email: str) -> bool:
    """Validar formato de email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_username(username: str) -> bool:
    """Validar username: solo letras, números y guiones bajos"""
    pattern = r'^[a-zA-Z0-9_-]{3,20}$'
    return re.match(pattern, username) is not None


def validate_password_strength(password: str) -> bool:
    """Validar contraseña: mín 8 caracteres, mayúscula, minúscula, número"""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True


def validate_no_special_chars(text: str) -> bool:
    """Validar que no tenga caracteres especiales"""
    return re.match(r'^[a-zA-Z0-9\s-]+$', text) is not None


def validate_age(age: int) -> bool:
    """Validar que la edad sea válida"""
    return 13 <= age <= 120


