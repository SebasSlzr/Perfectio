# app/schemas/asisstant_schema.py
from typing import List, Optional
from pydantic import BaseModel

class Message(BaseModel):
    """Mensaje individual en el historial de chat"""
    role: str
    content: str

class ChatRequest(BaseModel):
    """Peticion para chat con el asistente IA"""
    user_id: int
    user_context: Optional[str] = None
    messages_history: List[Message]

class ChatResponse(BaseModel):
    """Respuesta del asistente IA"""
    assistant_reply: str
    new_messages_history: List[Message]

class IAAssistantBase(BaseModel):
    """Base para el asistente IA"""
    user_context: Optional[str] = None
    messages_history: Optional[str] = None

class IAAssistantCreate(IAAssistantBase):
    """Crear asistente IA"""
    user_id: int

class IAAssistant(IAAssistantBase):
    """Asistente IA completo"""
    id_ia: int
    user_id: int

    class Config:
        from_attributes = True