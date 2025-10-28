from fastapi import FastAPI
from app.routes import goal_routes
from app.routes import habit_routes
from app.routes import reminder_routes
from app.routes import auth_routes

app = FastAPI(
    title="Perfectio"
    )

app.include_router(goal_routes.router, prefix="/goals", tags=["Goals"])
app.include_router(habit_routes.router, prefix="/habits", tags=["Habits"])
app.include_router(reminder_routes.router, prefix="/reminders", tags=["Reminders"])
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Bienvenido a Perfectio"
    }

