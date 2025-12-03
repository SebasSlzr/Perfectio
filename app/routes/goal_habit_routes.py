# app/routes/goal_habit_routes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import GoalHabit, GoalHabitCreate
from app.controllers import goal_habit_controller

router = APIRouter(
    prefix="/goal-habits",
    tags=["Goal-Habits"],
    responses={404: {"description": "Asociación no encontrada"}},
)


@router.post(
    "/",
    response_model=GoalHabit,
    status_code=status.HTTP_201_CREATED,
    summary="Asociar hábito a meta",
    description="Crea la relación entre una meta y un hábito que la soporta.",
    response_description="Asociación registrada.",
)
async def associate_goal_habit(association: GoalHabitCreate, db: AsyncSession = Depends(get_db)):
    """Asocia un hábito existente a una meta."""
    return await goal_habit_controller.associate_goal_habit(association, db)


@router.delete(
    "/{goal_id}/{habit_id}",
    summary="Eliminar asociación meta-hábito",
    description="Rompe la relación entre la meta y el hábito indicados.",
    responses={200: {"description": "Asociación eliminada correctamente."}},
)
async def remove_goal_habit_association(goal_id: int, habit_id: int, db: AsyncSession = Depends(get_db)):
    """Elimina la asociación entre una meta y un hábito."""
    return await goal_habit_controller.remove_goal_habit(goal_id, habit_id, db)