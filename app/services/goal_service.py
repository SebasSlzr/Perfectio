from sqlalchemy.orm import Session
from app.models.goal_model import Goal
from app.schemas.goal_schemas import GoalCreate, GoalUpdate

def get_all_goals(db: Session):
    return db.query(Goal).all()

def get_goal_by_id(db: Session, goal_id: int):
    return db.query(Goal).filter(Goal.id_goal == goal_id).first()

def create_goal(db: Session, goal: GoalCreate):
    db_goal = Goal(**goal.dict())
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

def update_goal(db: Session, db_goal: Goal, goal_update: GoalUpdate):
    for field, value in goal_update.dict(exclude_unset=True).items():
        setattr(db_goal, field, value)
    db.commit()
    db.refresh(db_goal)
    return db_goal

def delete_goal(db: Session, db_goal: Goal):
    db.delete(db_goal)
    db.commit()
