from pydantic import BaseModel
from datetime import datetime


class MessageCreate(BaseModel):

    role: str
    content: str
    conversation_id: int


class MessageResponse(BaseModel):

    id: int
    role: str
    content: str
    conversation_id: int
    created_at: datetime

    class Config:
        from_attributes = True