# /routers/habit_router.py

from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas import Habit, HabitCreate
from app.database import get_db


# Asegúrate de que esta importación apunte correctamente a tus schemas

# Inicializa el Router para este módulo
router = APIRouter(
    prefix="/habits",  # Todas las rutas aquí comenzarán con /habits
    tags=["Habits"]  # Etiqueta para la documentación de la API
)


# --- Implementación de Endpoints ---

# 1. GET /habits (Obtener todos los hábitos)
@router.get("/", response_model=List[Habit])
def get_all_habits():
    """Obtiene una lista de todos los hábitos."""
    # Nota: Aquí irá la lógica para consultar la base de datos (DB)
    # Por ahora, devolvemos una lista vacía como placeholder
    return []


# 2. GET /habits/{habit_id} (Obtener un hábito por ID)
@router.get("/{habit_id}", response_model=Habit)
def get_habit(habit_id: int):
    """Obtiene un hábito específico por su ID."""
    # Lógica de búsqueda en la DB. Si no se encuentra:
    # raise HTTPException(status_code=404, detail="Hábito no encontrado")

    # Placeholder: simula un hábito encontrado
    return Habit(id_habit=habit_id, title="Leer 20 mins", tag="Desarrollo", start_date="2024-01-01", frequency="diario",
                 reminders=["08:00"], color="#00ff00", icon="book")


# 3. POST /habits (Crear un nuevo hábito)
@router.post("/", response_model=Habit, status_code=status.HTTP_201_CREATED)
def create_habit(habit_data: HabitCreate):
    """Crea un nuevo hábito en la base de datos."""
    # Lógica para guardar habit_data en la DB y obtener el ID
    new_id = 1  # Simulación de ID generado por la DB

    # Combina los datos de entrada con el ID y devuelve el Schema completo
    return Habit(id_habit=new_id, **habit_data.model_dump())


# 4. PUT /habits/{habit_id} (Actualizar un hábito)
@router.put("/{habit_id}", response_model=Habit)
def update_habit(habit_id: int, habit_data: HabitCreate):
    """Actualiza completamente un hábito existente."""
    # Lógica para buscar el hábito en la DB y actualizarlo con habit_data

    # Placeholder: simula el objeto actualizado
    return Habit(id_habit=habit_id, **habit_data.model_dump())


# 5. DELETE /habits/{habit_id} (Eliminar un hábito)
@router.delete("/{habit_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_habit(habit_id: int):
    """Elimina un hábito por su ID."""
    # Lógica para eliminar el hábito de la DB
    # Si la eliminación fue exitosa, devuelve un 204 No Content (no necesita cuerpo de respuesta)
    return