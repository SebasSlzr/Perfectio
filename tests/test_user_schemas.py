# D:\UAM\ing software II\Perfectio\tests\test_user_schemas.py

import pytest
from pydantic import ValidationError

from app.schemas.user_schema import UserCreate


def test_user_create_schema_ok():
    data = {
        "email": "user@example.com",
        "password": "Password123",  # 1 mayúscula, 1 minúscula, 1 número
        "username": "user123",
        "name": "User Name",
    }
    user = UserCreate(**data)
    assert user.email == "user@example.com"
    assert user.username == "user123"
    assert user.name == "User Name"


def test_user_create_schema_invalid_email():
    data = {
        "email": "no-es-un-email",
        "password": "Password123",
        "username": "user123",
        "name": "User Name",
    }
    with pytest.raises(ValidationError):
        UserCreate(**data)
