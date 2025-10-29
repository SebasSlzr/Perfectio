# /schemas/assistant_schema.py

from typing import List, Optional
from pydantic import BaseModel

class Message(BaseModel):
    """Define un único mensaje en el historial (usuario o asistente)."""
    role: str  # Debe ser 'user' o 'assistant'
    content: str

class ChatRequest(BaseModel):
    """Schema para la petición de entrada al endpoint POST /assistant/chat."""
    id_user: int
    user_context: Optional[str] = None  # Contexto inicial opcional para la IA
    messages_history: List[Message]  # Historial completo de la conversación

class ChatResponse(BaseModel):
    """Schema para la respuesta de salida del endpoint."""
    assistant_reply: str  # Respuesta generada por la IA
    new_messages_history: List[Message]  # Historial actualizado con la nueva respuesta
