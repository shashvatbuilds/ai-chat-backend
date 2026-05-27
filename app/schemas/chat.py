from pydantic import BaseModel
from datetime import datetime


class ChatRequest(BaseModel):
    conversation_id: int
    message: str


class ChatResponse(BaseModel):
    user_message: str
    ai_response: str