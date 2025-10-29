# /app/routes/asisstant_routes.py

from fastapi import APIRouter
from ..schemas.asisstant_schema import ChatRequest, ChatResponse

router = APIRouter(
    prefix="/assistant",
    tags=["AI Assistant"],
)

@router.post("/chat", response_model=ChatResponse)
def chat_with_assistant(request: ChatRequest):
    """
    Endpoint para enviar un mensaje al asistente IA y recibir una respuesta simulada.
    """
    # Aquí devuelves una respuesta estática o simulada
    return ChatResponse(
        user_message=request.message,
        assistant_reply=f"Hola! Soy tu asistente. Me dijiste: '{request.message}'"
    )
