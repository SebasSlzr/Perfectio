# app/routes/goal_routes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.controllers import goal_controller
from app.schemas import Goal, GoalCreate, GoalUpdate, GoalHabit

router = APIRouter(
    prefix="/goals",
    tags=["Goals"],
    responses={404: {"description": "Meta no encontrada"}},
)


@router.get(
    "/",
    response_model=list[Goal],
    summary="Listar metas",
    description="Devuelve todas las metas registradas por los usuarios.",
    response_description="Colección de metas.",
)
async def list_goals(db: AsyncSession = Depends(get_db)):
    return await goal_controller.get_all_goals(db)


@router.get(
    "/{goal_id}",
    response_model=Goal,
    summary="Obtener meta",
    description="Recupera la meta solicitada por su identificador.",
    response_description="Meta solicitada.",
)
async def get_goal(goal_id: int, db: AsyncSession = Depends(get_db)):
    return await goal_controller.get_goal_by_id(goal_id, db)


@router.post(
    "/",
    response_model=Goal,
    status_code=status.HTTP_201_CREATED,
    summary="Crear meta",
    description="Crea una nueva meta con su información principal.",
    response_description="Meta creada correctamente.",
)
async def create_goal(goal: GoalCreate, db: AsyncSession = Depends(get_db)):
    return await goal_controller.create_goal(goal, db)


@router.put(
    "/{goal_id}",
    response_model=Goal,
    summary="Actualizar meta",
    description="Actualiza los datos de una meta existente.",
    response_description="Meta actualizada.",
)
async def update_goal(goal_id: int, goal: GoalUpdate, db: AsyncSession = Depends(get_db)):
    return await goal_controller.update_goal(goal_id, goal, db)


@router.delete(
    "/{goal_id}",
    summary="Eliminar meta",
    description="Elimina la meta indicada.",
    responses={200: {"description": "Meta eliminada correctamente."}},
)
async def delete_goal(goal_id: int, db: AsyncSession = Depends(get_db)):
    return await goal_controller.delete_goal(goal_id, db)


@router.get(
    "/{goal_id}/habits",
    response_model=list[GoalHabit],
    summary="Listar hábitos de una meta",
    description="Recupera los hábitos asociados a la meta seleccionada.",
    responses={200: {"description": "Listado de hábitos asociados."}},
)
async def get_goal_habits(goal_id: int, db: AsyncSession = Depends(get_db)):
    return await goal_controller.get_goal_habits(goal_id, db)