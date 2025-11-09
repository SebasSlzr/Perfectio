# app/routes/asisstant_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas import IAAssistant, IAAssistantCreate, ChatRequest, ChatResponse

router = APIRouter()

@router.get("/{user_id}", response_model=IAAssistant)
async def get_assistant(user_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Asistente IA del usuario {user_id}"}

@router.post("/", response_model=IAAssistant)
async def create_assistant(assistant: IAAssistantCreate, db: AsyncSession = Depends(get_db)):
    return {"msg": "Asistente IA creado correctamente"}

@router.post("/chat", response_model=ChatResponse)
async def chat_with_assistant(chat_request: ChatRequest, db: AsyncSession = Depends(get_db)):
    return {"msg": "Chat con asistente IA", "assistant_reply": "Respuesta simulada", "new_messages_history": []}