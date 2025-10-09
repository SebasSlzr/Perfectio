from typing import Union
from app.routes import goal_routes
from fastapi import FastAPI

app = FastAPI(
    title="Perfectio")

app.include_router(goal_routes.router, prefix="/goals", tags=["Goals"])


@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Bienvenido a Perfectio",
        "version": "1.0.0"
    }