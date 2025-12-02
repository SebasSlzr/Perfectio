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
    user_achievement_routes,
)
from app.database import create_tables
from app import models
from app.middleware import setup_validations

origins = [
    "http://localhost:3000",
]

tags_metadata = [
    {"name": "Authentication", "description": "Registro y autenticación de usuarios."},
    {"name": "Users", "description": "Administración de perfiles y datos de usuario."},
    {"name": "Habits", "description": "CRUD de hábitos diarios del usuario."},
    {"name": "Goals", "description": "Gestión de metas y su progreso."},
    {"name": "Reminders", "description": "Recordatorios vinculados a hábitos y metas."},
    {"name": "Assistant", "description": "Operaciones del asistente de IA y chat contextual."},
    {"name": "Diary", "description": "Entradas del diario y reflexiones del usuario."},
    {"name": "Achievements", "description": "Logros, insignias y sistema de gamificación."},
    {"name": "Goal-Habits", "description": "Asociaciones entre metas e indicadores diarios."},
    {"name": "User-Achievements", "description": "Asignación y consulta de logros por usuario."},
    {"name": "Metadata", "description": "Healthchecks y utilidades de la plataforma."},
]

# Crear instancia de FastAPI
app = FastAPI(
    title="Perfectio",
    description="API para la gestión de desarrollo personal",
    version="1.0.0",
    openapi_tags=tags_metadata,
    contact={"name": "Equipo Perfectio", "email": "perfectio-team@example.com"},
    license_info={"name": "MIT"},
)

setup_validations(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# INCLUIR ROUTERS

app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(habit_routes.router)
app.include_router(goal_routes.router)
app.include_router(reminder_routes.router)
app.include_router(asisstant_routes.router)
app.include_router(diary_routes.router)
app.include_router(achievement_routes.router)
app.include_router(goal_habit_routes.router)
app.include_router(user_achievement_routes.router)



@app.on_event("startup")
async def on_startup():
    """Evento que se ejecuta al iniciar la aplicación"""
    await create_tables()




@app.get(
    "/health",
    tags=["Metadata"],
    summary="Verificar el estado del servicio",
    description="Confirma que la API está respondiendo correctamente.",
    responses={200: {"description": "El servicio está operativo."}},
)
def health_check():
    """Endpoint para verificar el estado de la API"""
    return {
        "status": "healthy",
        "service": "Perfectio API",
        "version": "1.0.0"
    }
    
@app.get(
    "/",
    tags=["Metadata"],
    summary="Mensaje de bienvenida",
    description="Permite comprobar que la API está desplegada y lista para usarse.",
)
def read_root():
    return {"message": "Bienvenido a Perfectio"}
