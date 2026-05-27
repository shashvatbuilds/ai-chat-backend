from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.chat import (
    ChatRequest,
    ChatResponse
)

from app.models.conversation import Conversation
from app.models.message import Message
from app.models.user import User

from app.utils.security import get_current_user

from app.services.gemini_service import (
    generate_ai_response
)

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)


@router.post(
    "/",
    response_model=ChatResponse
)
def chat_with_ai(
    chat_data: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    conversation = db.query(
        Conversation
    ).filter(
        Conversation.id == chat_data.conversation_id,
        Conversation.user_id == current_user.id
    ).first()

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    user_message = Message(
        conversation_id=chat_data.conversation_id,
        role="user",
        content=chat_data.message
    )

    db.add(user_message)
    db.commit()

    previous_messages = db.query(
        Message
    ).filter(
        Message.conversation_id == chat_data.conversation_id
    ).order_by(
        Message.created_at.asc()
    ).all()

    conversation_history = ""

    for msg in previous_messages:

        conversation_history += (
            f"{msg.role}: {msg.content}\n"
        )

    full_prompt = f"""
You are a helpful AI assistant.

Conversation History:
{conversation_history}

User: {chat_data.message}
"""

    ai_reply = generate_ai_response(
        full_prompt
    )

    ai_message = Message(
        conversation_id=chat_data.conversation_id,
        role="assistant",
        content=ai_reply
    )

    db.add(ai_message)
    db.commit()

    return {
        "user_message": chat_data.message,
        "ai_response": ai_reply
    }