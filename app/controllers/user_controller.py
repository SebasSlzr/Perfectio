# app/controllers/user_controller.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy import or_

from app.models.users import User
from app.schemas.user_schema import UserCreate, UserUpdate

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


async def _get_user_or_404(user_id: int, db: AsyncSession) -> User:
    result = await db.execute(select(User).where(User.id_user == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


async def _ensure_unique_credentials(
    db: AsyncSession,
    *,
    email: str | None = None,
    username: str | None = None,
    exclude_user_id: int | None = None,
) -> None:
    filters = []
    if email is not None:
        filters.append(User.email == email)
    if username is not None:
        filters.append(User.username == username)
    if not filters:
        return
    query = select(User).where(or_(*filters))
    if exclude_user_id:
        query = query.where(User.id_user != exclude_user_id)
    result = await db.execute(query)
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico o el nombre de usuario ya están en uso",
        )


def _hash_password(password: str) -> str:
    return pwd_context.hash(password)


async def get_all_users(db: AsyncSession):
    """Devuelve todos los usuarios registrados."""
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users


async def get_user_by_id(user_id: int, db: AsyncSession):
    """Obtiene un usuario por ID."""
    return await _get_user_or_404(user_id, db)


async def create_user(user_data: UserCreate, db: AsyncSession):
    """Crea un nuevo usuario con contraseña hasheada y validando duplicados."""
    payload = user_data.model_dump()
    await _ensure_unique_credentials(db, email=payload["email"], username=payload["username"])
    payload["password"] = _hash_password(payload["password"])
    new_user = User(**payload)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def update_user(user_id: int, user_data: UserUpdate, db: AsyncSession):
    """Actualiza datos del usuario respetando unicidad y hashing."""
    user = await _get_user_or_404(user_id, db)
    update_data = user_data.model_dump(exclude_unset=True)
    await _ensure_unique_credentials(
        db,
        email=update_data.get("email"),
        username=update_data.get("username"),
        exclude_user_id=user_id,
    )
    if "password" in update_data:
        update_data["password"] = _hash_password(update_data["password"])
    for key, value in update_data.items():
        setattr(user, key, value)
    await db.commit()
    await db.refresh(user)
    return user


async def delete_user(user_id: int, db: AsyncSession):
    """Elimina un usuario existente."""
    user = await _get_user_or_404(user_id, db)
    await db.delete(user)
    await db.commit()
    return {"detail": f"Usuario {user_id} eliminado correctamente"}
