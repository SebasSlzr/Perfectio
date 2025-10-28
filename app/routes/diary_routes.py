# /routers/diary_routes.py

from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas import Diary, DiaryCreate, DiaryEntry, DiaryEntryCreate

router = APIRouter(
    prefix="/diary",
    tags=["Diary"]
)


# --- Implementacion de endpoints---


# GET /diary  → Obtener todos los diarios
@router.get("/", response_model=List[Diary])
def get_all_diaries():
    """Obtiene la lista de todos los diarios."""
    # Lógica DB aquí
    return []


# POST /diary/entries → Crear nueva entrada
@router.post("/entries", response_model=DiaryEntry, status_code=status.HTTP_201_CREATED)
def create_entry(entry_data: DiaryEntryCreate):
    """Crea una nueva entrada en el diario."""
    # Lógica DB aquí
    new_id = 1  # Simula ID generado por DB
    return DiaryEntry(id_entry=new_id, diary_id=1, **entry_data.model_dump())


# GET /diary/entries/{entry_id} → Obtener entrada por ID
@router.get("/entries/{entry_id}", response_model=DiaryEntry)
def get_entry(entry_id: int):
    """Obtiene una entrada del diario por su ID."""
    # Lógica DB: Buscar en base de datos
    if entry_id != 1:  # Simulación de inexistente
        raise HTTPException(status_code=404, detail="Entrada no encontrada")

    return DiaryEntry(id_entry=entry_id, diary_id=1, date="2025-01-01T08:00:00", content="Día productivo")


# PUT /diary/entries/{entry_id} → Actualizar una entrada existente
@router.put("/entries/{entry_id}", response_model=DiaryEntry)
def update_entry(entry_id: int, entry_data: DiaryEntryCreate):
    """Actualiza el contenido de una entrada existente."""
    # Lógica DB aquí
    return DiaryEntry(id_entry=entry_id, diary_id=1, **entry_data.model_dump())


# DELETE /diary/entries/{entry_id} → Eliminar una entrada
@router.delete("/entries/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_entry(entry_id: int):
    """Elimina una entrada del diario por su ID."""
    # Lógica DB aquí
    return
