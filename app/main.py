from fastapi import FastAPI
from app.routes import goal_routes
from app.routes import habit_routes
from app.routes import reminder_routes
from app.routes import auth_routes
from app.routes import asisstant_routes
from app.routes import diary_routes


app = FastAPI(
    title="Perfectio"
    )

app.include_router(goal_routes.router, prefix="/goals", tags=["Goals"])
app.include_router(habit_routes.router, prefix="/habits", tags=["Habits"])
app.include_router(reminder_routes.router, prefix="/reminders", tags=["Reminders"])
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(asisstant_routes.router, prefix="/assistant", tags=["Assistant"])
app.include_router(diary_routes.router, prefix="/diary", tags=["Diary"])



@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Bienvenido a Perfectio"
    }
    