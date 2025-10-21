# /schemas/assistant_schema.py

from typing import List, Optional

# Nota: Asumo que estás utilizando alguna librería de validación como Pydantic,
# por eso uso la estructura de clase. Si no, ajusta a la estructura de tu proyecto.

class Message(object):
    """Define un único mensaje en el historial (usuario o asistente)."""
    role: str # Debe ser 'user' o 'assistant'
    content: str

class ChatRequest(object):
    """Schema para la petición de entrada al endpoint POST /assistant/chat."""
    id_user: int
    user_context: Optional[str] = None # El contexto que se le da inicialmente a la IA
    messages_history: List[Message] # Historial completo de la conversación

class ChatResponse(object):
    """Schema para la respuesta de salida del endpoint."""
    assistant_reply: str # La respuesta del modelo de IA
    new_messages_history: List[Message] # El historial actualizado, incluyendo la respuesta