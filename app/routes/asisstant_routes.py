# /app/routers/assistant_router.py

from fastapi import APIRouter
from ..schemas.asisstant_schema import ChatRequest, ChatResponse
from ..controllers import assistant_controller


# Definición del router
router = APIRouter(
    prefix="/assistant",
    tags=["AI Assistant"],
)


@router.post("/chat", response_model=ChatResponse)
def chat_with_assistant(request: ChatRequest):
    """
    Endpoint para enviar un mensaje al asistente IA y recibir una respuesta.
    """
    # Devuelve una respuesta que cumple con el ChatResponse Schema
    return assistant_controller.process_chat_request(request)