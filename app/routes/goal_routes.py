# app/routes/goal_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import Goal, GoalCreate, GoalUpdate #, GoalWithHabits

router = APIRouter()

@router.get("/", response_model=list[Goal])
async def list_goals(db: AsyncSession = Depends(get_db)):
    return {"msg": "Lista de todas las metas"}

#@router.get("/{goal_id}", response_model=GoalWithHabits)
#async def get_goal(goal_id: int, db: AsyncSession = Depends(get_db)):
#    return {"msg": f"Información de la meta {goal_id} con sus hábitos"}

@router.post("/", response_model=Goal)
async def create_goal(goal: GoalCreate, db: AsyncSession = Depends(get_db)):
    return {"msg": "Meta creada correctamente"}

@router.put("/{goal_id}", response_model=Goal)
async def update_goal(goal_id: int, goal: GoalUpdate, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Meta {goal_id} actualizada"}

@router.delete("/{goal_id}")
async def delete_goal(goal_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Meta {goal_id} eliminada"}

@router.get("/{goal_id}/habits")
async def get_goal_habits(goal_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Hábitos de la meta {goal_id}"}