# D:\UAM\ing software II\Perfectio\tests\conftest.py

import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db  # ajusta si tienen otro nombre/ruta

# BD de pruebas en memoria (solo para tests)
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async_engine = create_async_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
AsyncTestingSessionLocal = async_sessionmaker(bind=async_engine, expire_on_commit=False)


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


@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_database():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


def override_get_db():
    """Sustituye la dependencia get_db de la app para usar la BD de tests."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


async def async_override_get_db():
    async with AsyncTestingSessionLocal() as session:
        try:
            yield session
        finally:
            await session.rollback()


# 👇 ESTO es lo correcto: asignar el override
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    """Cliente de pruebas para llamar a los endpoints."""
    return TestClient(app)


@pytest_asyncio.fixture
async def async_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client
