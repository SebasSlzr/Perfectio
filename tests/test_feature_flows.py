import pytest
from datetime import date, datetime, timedelta
from uuid import uuid4

pytestmark = pytest.mark.asyncio


def _user_payload(prefix: str) -> dict:
    unique = uuid4().hex[:6]
    return {
        "username": f"{prefix}_{unique}",
        "name": f"{prefix.title()} User",
        "email": f"{prefix}_{unique}@example.com",
        "password": "Pass1234A",
    }


async def _create_user(async_client, prefix: str):
    payload = _user_payload(prefix)
    response = await async_client.post("/users/", json=payload)
    assert response.status_code == 201
    return response.json()


async def test_habit_and_reminder_flow(async_client):
    user = await _create_user(async_client, "habit")
    habit_payload = {
        "title": "Leer diariamente",
        "tag": "Productividad",
        "start_date": date.today().isoformat(),
        "frequency": "daily",
        "color": "#FFAA00",
        "icon": "book",
        "state": "activo",
        "user_id": user["id_user"],
    }
    habit_response = await async_client.post("/habits/", json=habit_payload)
    assert habit_response.status_code == 201
    habit = habit_response.json()

    reminder_payload = {
        "title": "Leer 20 minutos",
        "description": "Mantén el ritmo de lectura.",
        "date": datetime.utcnow().isoformat(),
        "shouldRepeat": True,
        "habit_id": habit["id_habit"],
    }
    reminder_response = await async_client.post("/reminders/", json=reminder_payload)
    assert reminder_response.status_code == 201

    reminders = await async_client.get("/reminders/")
    assert reminder_payload["title"] in [item["title"] for item in reminders.json()]


async def test_goal_lifecycle(async_client):
    user = await _create_user(async_client, "goal")
    goal_payload = {
        "title": "Entrenar maratón",
        "description": "Plan de 30 días",
        "start_date": date.today().isoformat(),
        "end_date": (date.today() + timedelta(days=30)).isoformat(),
        "progress": 0.0,
        "user_id": user["id_user"],
    }
    goal_response = await async_client.post("/goals/", json=goal_payload)
    assert goal_response.status_code == 201
    goal = goal_response.json()

    fetched = await async_client.get(f"/goals/{goal['id_goal']}")
    assert fetched.status_code == 200
    assert fetched.json()["title"] == goal_payload["title"]


async def test_diary_flow(async_client):
    user = await _create_user(async_client, "diary")
    diary_response = await async_client.post("/diary/", json={"user_id": user["id_user"]})
    assert diary_response.status_code == 201
    diary = diary_response.json()

    entry_payload = {
        "date": datetime.utcnow().isoformat(),
        "content": "Primer registro del diario.",
    }
    entry_response = await async_client.post(f"/diary/{diary['id_diary']}/entries", json=entry_payload)
    assert entry_response.status_code == 201

    entries = await async_client.get(f"/diary/{diary['id_diary']}/entries")
    assert len(entries.json()) == 1
