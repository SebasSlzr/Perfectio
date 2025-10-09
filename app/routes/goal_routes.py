from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from app.schemas.goal import GoalCreate, GoalUpdate 

router = APIRouter()

# GET /goals/list
@router.get("/list")
async def list_goals(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Listar metas (skip={skip}, limit={limit})"}

# GET /goals/{goal_id}
@router.get("/{goal_id}")
async def get_goal(goal_id: int = Path(..., description="ID de la meta"), db: AsyncSession = Depends(get_db)):
    return {"msg": f"Información de la meta {goal_id}"}

# POST /goals/
@router.post("/", response_model=GoalCreate)
async def create_goal(db: AsyncSession = Depends(get_db)):
    return {"msg": "Meta creada correctamente"}

# PUT /goals/{goal_id}
@router.put("/{goal_id}")
async def update_goal(goal_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Meta {goal_id} actualizada"}

# DELETE /goals/{goal_id}
@router.delete("/{goal_id}")
async def delete_goal(goal_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Meta {goal_id} eliminada"}