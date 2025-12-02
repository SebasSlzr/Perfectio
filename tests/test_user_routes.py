# D:\UAM\ing software II\Perfectio\tests\test_user_routes.py

def test_register_user(client):
    # Datos de ejemplo para crear un usuario
    payload = {
        "email": "newuser@example.com",
        "password": "Aads12345678"
    }

    # Ajusta la ruta según tu proyecto, por ejemplo "/users/register" o similar
    response = client.post("/users", json=payload)

    assert response.status_code in (200, 201)
    data = response.json()
    assert data["email"] == payload["email"]


def test_register_user_invalid_email(client):
    payload = {
        "email": "no-es-un-email",
        "password": "12345678"
    }

    response = client.post("/users", json=payload)

    # Debería fallar por validación (400 normalmente)
    assert response.status_code in (400, 422)
