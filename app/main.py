# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import (
    user_routes, 
    habit_routes, 
    goal_routes, 
    reminder_routes, 
    auth_routes, 
    asisstant_routes, 
    diary_routes, 
    achievement_routes,
    goal_habit_routes,
    user_achievement_routes
)
from app.database import create_tables
from app import models

app = FastAPI(title="Perfectio")

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(habit_routes.router, prefix="/habits", tags=["Habits"])
app.include_router(goal_routes.router, prefix="/goals", tags=["Goals"])
app.include_router(reminder_routes.router, prefix="/reminders", tags=["Reminders"])
app.include_router(asisstant_routes.router, prefix="/assistant", tags=["Assistant"])
app.include_router(diary_routes.router, prefix="/diary", tags=["Diary"])
app.include_router(achievement_routes.router, prefix="/achievements", tags=["Achievements"])
app.include_router(goal_habit_routes.router, prefix="/goal-habits", tags=["Goal-Habits"])
app.include_router(user_achievement_routes.router, prefix="/user-achievements", tags=["User-Achievements"])

@app.on_event("startup")
async def on_startup():
    await create_tables()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Perfectio"}