# D:\UAM\ing software II\Perfectio\tests\conftest.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db  # ajusta si tienen otro nombre/ruta

# BD de pruebas en memoria (solo para tests)
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session")
def db_engine():
    # Crear las tablas una vez para toda la sesión de tests
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session(db_engine):
    # Transacción por test
    connection = db_engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


def override_get_db():
    """Sustituye la dependencia get_db de la app para usar la BD de tests."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# 👇 ESTO es lo correcto: asignar el override
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    """Cliente de pruebas para llamar a los endpoints."""
    return TestClient(app)
