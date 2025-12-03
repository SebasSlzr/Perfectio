import json
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ia_assistant import IAAssistant as AssistantModel
from app.schemas.asisstant_schema import (
    IAAssistantCreate,
    ChatRequest,
    ChatResponse,
    Message,
)


async def _get_assistant_or_404(user_id: int, db: AsyncSession) -> AssistantModel:
    result = await db.execute(select(AssistantModel).where(AssistantModel.user_id == user_id))
    assistant = result.scalar_one_or_none()
    if assistant is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asistente no encontrado")
    return assistant


async def get_assistant(user_id: int, db: AsyncSession):
    return await _get_assistant_or_404(user_id, db)


async def create_assistant(payload: IAAssistantCreate, db: AsyncSession):
    existing = await db.execute(select(AssistantModel).where(AssistantModel.user_id == payload.user_id))
    if existing.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya cuenta con un asistente configurado",
        )
    assistant = AssistantModel(**payload.model_dump())
    assistant.messages_history = assistant.messages_history or "[]"
    db.add(assistant)
    await db.commit()
    await db.refresh(assistant)
    return assistant


def _load_history(raw_history: str | None) -> list[dict]:
    if not raw_history:
        return []
    try:
        parsed = json.loads(raw_history)
        return parsed if isinstance(parsed, list) else []
    except json.JSONDecodeError:
        return []


def _dump_history(history: list[dict]) -> str:
    return json.dumps(history)


async def chat_with_assistant(payload: ChatRequest, db: AsyncSession) -> ChatResponse:
    assistant = await _get_assistant_or_404(payload.user_id, db)
    history = _load_history(assistant.messages_history)
    history.extend([msg.model_dump() for msg in payload.messages_history])
    reply_content = payload.user_context or "Continúa avanzando con tus metas."
    if payload.messages_history:
        reply_content = f"{reply_content} | Recibido: {payload.messages_history[-1].content}"
    history.append({"role": "assistant", "content": reply_content})
    assistant.messages_history = _dump_history(history)
    if payload.user_context:
        assistant.user_context = payload.user_context
    await db.commit()
    await db.refresh(assistant)
    return ChatResponse(
        assistant_reply=reply_content,
        new_messages_history=[Message(**msg) for msg in history],
    )
