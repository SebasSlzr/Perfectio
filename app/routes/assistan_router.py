# /app/routers/assistant_router.py

from fastapi import APIRouter
# Ajustamos la importación del esquema para usar la ruta completa de tu proyecto
from ..schemas.assistant_schema import ChatRequest, ChatResponse

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
    # En la implementación real, esta lógica se movería al controller.

    # Simulación de respuesta para pruebas
    new_message = {
        "role": "assistant",
        "content": f"Mensaje recibido de ID {request.id_user}. El contexto inicial es: {request.user_context}. Preparando respuesta IA..."
    }

    # Devuelve una respuesta que cumple con el ChatResponse Schema
    return ChatResponse(
        assistant_reply=new_message['content'],
        new_messages_history=request.messages_history + [new_message]
    )