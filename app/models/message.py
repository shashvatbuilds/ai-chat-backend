from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Text
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.sql import func

class Message(Base):
    __tablename__ ="message"
    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    conversation_id = Column(
        Integer,
        ForeignKey("conversations.id")
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )

