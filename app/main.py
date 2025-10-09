from fastapi import FastAPI
from app.routes import reminder_routes

app = FastAPI(title="PerfectioAPI")

app.include_router(reminder_routes.router)
