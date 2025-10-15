# /app/controllers/assistant_controller.py

from typing import List, Dict
# Ajustamos la importación del esquema usando la ruta correcta
from ..schemas.assistant_schema import ChatRequest, ChatResponse, Message


def process_chat_request(request: ChatRequest) -> ChatResponse:
    """
    Procesa la petición de chat, y genera una respuesta simulada.
    """

    # --- Simulación de Lógica de IA ---
    ai_response_content = (
        f"Tu solicitud sobre '{request.user_context[:20]}...' ha sido procesada por el Controller. "
        "Se necesita integrar una API de IA real (Gemini, etc.) aquí."
    )
    # --- Fin Simulación ---

    # Crear el nuevo mensaje del asistente
    new_assistant_message = Message(
        role="assistant",
        content=ai_response_content
    )

    # Actualizar el historial
    updated_history = request.messages_history + [new_assistant_message]

    return ChatResponse(
        assistant_reply=ai_response_content,
        new_messages_history=updated_history
    )