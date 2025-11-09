# app/routes/__init__.py
from .user_routes import router as user_router
from .habit_routes import router as habit_router
from .goal_routes import router as goal_router
from .reminder_routes import router as reminder_router
from .auth_routes import router as auth_router
from .asisstant_routes import router as asisstant_router
from .diary_routes import router as diary_router
from .achievement_routes import router as achievement_router
from .goal_habit_routes import router as goal_habit_router
from .user_achievement_routes import router as user_achievement_router

__all__ = [
    "user_router",
    "habit_router", 
    "goal_router",
    "reminder_router",
    "auth_router",
    "asisstant_router",
    "diary_router",
    "achievement_router",
    "goal_habit_router",
    "user_achievement_router"
]