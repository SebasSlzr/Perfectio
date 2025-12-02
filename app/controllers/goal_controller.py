from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.goal import Goal
from app.models.goal_habit import GoalHabit
from app.models.users import User
from app.schemas.goal_schemas import GoalCreate, GoalUpdate


async def _ensure_user_exists(user_id: int, db: AsyncSession) -> None:
    if await db.get(User, user_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")


async def _get_goal_or_404(goal_id: int, db: AsyncSession) -> Goal:
    goal = await db.get(Goal, goal_id)
    if goal is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meta no encontrada")
    return goal


async def get_all_goals(db: AsyncSession):
    result = await db.execute(select(Goal))
    return result.scalars().all()


async def get_goal_by_id(goal_id: int, db: AsyncSession):
    return await _get_goal_or_404(goal_id, db)


async def create_goal(goal_data: GoalCreate, db: AsyncSession):
    await _ensure_user_exists(goal_data.user_id, db)
    goal = Goal(**goal_data.model_dump())
    db.add(goal)
    await db.commit()
    await db.refresh(goal)
    return goal


async def update_goal(goal_id: int, goal_data: GoalUpdate, db: AsyncSession):
    goal = await _get_goal_or_404(goal_id, db)
    payload = goal_data.model_dump(exclude_unset=True)
    if "user_id" in payload:
        await _ensure_user_exists(payload["user_id"], db)
    for key, value in payload.items():
        setattr(goal, key, value)
    await db.commit()
    await db.refresh(goal)
    return goal


async def delete_goal(goal_id: int, db: AsyncSession):
    goal = await _get_goal_or_404(goal_id, db)
    await db.delete(goal)
    await db.commit()
    return {"detail": f"Meta {goal_id} eliminada"}


async def get_goal_habits(goal_id: int, db: AsyncSession):
    await _get_goal_or_404(goal_id, db)
    result = await db.execute(select(GoalHabit).where(GoalHabit.id_goal == goal_id))
    return result.scalars().all()
