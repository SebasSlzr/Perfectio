import pytest
from uuid import uuid4

pytestmark = pytest.mark.asyncio


def _payload(seed: str | None = None):
    u = seed or uuid4().hex[:6]
    return {
        "username": f"user_{u}",
        "name": f"User {u}",
        "email": f"user_{u}@example.com",
        "password": "Pass1234A",
    }


async def test_register_user(async_client):
    payload = _payload()
    resp = await async_client.post("/users/", json=payload)
    assert resp.status_code == 201
    body = resp.json()
    assert body["email"] == payload["email"]


async def test_register_user_invalid_email(async_client):
    payload = _payload("badmail")
    payload["email"] = "no-es-un-email"
    resp = await async_client.post("/users/", json=payload)
    assert resp.status_code == 422
