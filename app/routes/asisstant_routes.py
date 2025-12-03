# app/routes/asisstant_routes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import IAAssistant, IAAssistantCreate, ChatRequest, ChatResponse
from app.controllers import assistant_controller

router = APIRouter(
    prefix="/assistant",
    tags=["Assistant"],
    responses={
        401: {"description": "No autorizado"},
        404: {"description": "Asistente no encontrado"},
    },
)


@router.get(
    "/{user_id}",
    response_model=IAAssistant,
    summary="Obtener asistente de un usuario",
    description="Devuelve la configuración y estado del asistente IA asignado al usuario.",
    response_description="Información del asistente IA.",
)
async def get_assistant(user_id: int, db: AsyncSession = Depends(get_db)):
    """Consulta el asistente IA asociado a un usuario."""
    return await assistant_controller.get_assistant(user_id, db)


@router.post(
    "/",
    response_model=IAAssistant,
    status_code=status.HTTP_201_CREATED,
    summary="Crear asistente IA",
    description="Inicializa un asistente IA para un usuario específico.",
    response_description="Asistente creado correctamente.",
)
async def create_assistant(assistant: IAAssistantCreate, db: AsyncSession = Depends(get_db)):
    """Crea un asistente IA."""
    return await assistant_controller.create_assistant(assistant, db)


@router.post(
    "/chat",
    response_model=ChatResponse,
    summary="Conversar con el asistente",
    description="Envía un mensaje al asistente IA y recibe una respuesta contextual.",
    response_description="Respuesta generada por el asistente.",
)
async def chat_with_assistant(chat_request: ChatRequest, db: AsyncSession = Depends(get_db)):
    """Gestiona una interacción con el asistente IA."""
    return await assistant_controller.chat_with_assistant(chat_request, db)