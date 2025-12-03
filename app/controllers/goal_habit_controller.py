from fastapi import HTTPException, status
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.goal_habit import GoalHabit
from app.models.goal import Goal
from app.models.habits import Habit
from app.schemas.goal_habit_schemas import GoalHabitCreate


async def _ensure_goal(goal_id: int, db: AsyncSession):
    if await db.get(Goal, goal_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meta no encontrada")


async def _ensure_habit(habit_id: int, db: AsyncSession):
    if await db.get(Habit, habit_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hábito no encontrado")


async def associate_goal_habit(payload: GoalHabitCreate, db: AsyncSession):
    await _ensure_goal(payload.id_goal, db)
    await _ensure_habit(payload.id_habit, db)
    exists = await db.execute(
        select(GoalHabit).where(
            and_(
                GoalHabit.id_goal == payload.id_goal,
                GoalHabit.id_habit == payload.id_habit,
            )
        )
    )
    if exists.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La asociación meta-hábito ya existe",
        )
    relation = GoalHabit(**payload.model_dump())
    db.add(relation)
    await db.commit()
    await db.refresh(relation)
    return relation


async def remove_goal_habit(goal_id: int, habit_id: int, db: AsyncSession):
    result = await db.execute(
        select(GoalHabit).where(
            and_(GoalHabit.id_goal == goal_id, GoalHabit.id_habit == habit_id)
        )
    )
    relation = result.scalar_one_or_none()
    if relation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asociación no encontrada")
    await db.delete(relation)
    await db.commit()
    return {"detail": f"Asociación meta {goal_id} - hábito {habit_id} eliminada"}
