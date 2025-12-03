# app/routes/diary_routes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import Diary, DiaryCreate, DiaryEntry, DiaryEntryCreate
from app.controllers import diary_controller

router = APIRouter(
    prefix="/diary",
    tags=["Diary"],
    responses={404: {"description": "Diario o entrada no encontrada"}},
)


@router.get(
    "/{user_id}",
    response_model=Diary,
    summary="Obtener diario por usuario",
    description="Retorna el diario completo de un usuario.",
    response_description="Diario del usuario solicitado.",
)
async def get_diary(user_id: int, db: AsyncSession = Depends(get_db)):
    """Devuelve el diario asociado a un usuario."""
    return await diary_controller.get_diary_by_user(user_id, db)


@router.post(
    "/",
    response_model=Diary,
    status_code=status.HTTP_201_CREATED,
    summary="Crear diario",
    description="Inicializa un diario digital para el usuario.",
    response_description="Diario creado correctamente.",
)
async def create_diary(diary: DiaryCreate, db: AsyncSession = Depends(get_db)):
    """Crea un diario para un usuario."""
    return await diary_controller.create_diary(diary, db)


@router.get(
    "/{diary_id}/entries",
    response_model=list[DiaryEntry],
    summary="Listar entradas del diario",
    description="Recupera todas las entradas registradas dentro de un diario.",
    response_description="Listado de entradas del diario.",
)
async def list_diary_entries(diary_id: int, db: AsyncSession = Depends(get_db)):
    """Lista las entradas pertenecientes a un diario."""
    return await diary_controller.list_entries(diary_id, db)


@router.post(
    "/{diary_id}/entries",
    response_model=DiaryEntry,
    status_code=status.HTTP_201_CREATED,
    summary="Crear entrada de diario",
    description="Añade una nueva reflexión o apunte al diario seleccionado.",
    response_description="Entrada creada correctamente.",
)
async def create_diary_entry(diary_id: int, entry: DiaryEntryCreate, db: AsyncSession = Depends(get_db)):
    """Crea una entrada dentro del diario especificado."""
    return await diary_controller.create_entry(diary_id, entry, db)