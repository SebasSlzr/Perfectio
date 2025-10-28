# /routers/achievement_routes.py

from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime

from app.schemas.achievement_schema import Achievement, AchievementCreate

# --- Inicialización del router ---
router = APIRouter(
    prefix="/achievements",
    tags=["Achievements (Gamificación)"]
)


# --- ENDPOINTS ---


#GET /achievements  → Lista todos los logros
@router.get("/", response_model=List[Achievement])
def get_all_achievements():
    """Obtiene todos los logros registrados en el sistema."""
    # Aquí irá la lógica de consulta a la base de datos
    return []


# GET /achievements/{id}  → Obtiene un logro por su ID
@router.get("/{id_achievement}", response_model=Achievement)
def get_achievement_by_id(id_achievement: int):
    """Obtiene la información de un logro específico."""
    # Lógica de búsqueda. Si no se encuentra:
    # raise HTTPException(status_code=404, detail="Logro no encontrado")

    # Placeholder temporal
    return Achievement(
        id_achievement=id_achievement,
        title="Primer Hábito Completado",
        description="Logro otorgado por completar tu primer hábito",
        date=datetime.now(),
        user_id=1,
        emblem="Estrella Dorada"
    )


#POST /achievements  → Crea un nuevo logro
@router.post("/", response_model=Achievement, status_code=status.HTTP_201_CREATED)
def create_achievement(achievement_data: AchievementCreate):
    """Crea un nuevo logro asociado a un usuario."""
    # Lógica para guardar el logro y obtener su ID
    new_id = 1  # Simulación de ID generado por la BD

    return Achievement(id_achievement=new_id, **achievement_data.model_dump())


# DELETE /achievements/{id}  → Elimina un logro
@router.delete("/{id_achievement}", status_code=status.HTTP_204_NO_CONTENT)
def delete_achievement(id_achievement: int):
    """Elimina un logro existente por su ID."""
    # Lógica para eliminar de la BD
    # Si no se encuentra, lanzar excepción:
    # raise HTTPException(status_code=404, detail="Logro no encontrado")
    return
