from pydantic import BaseModel, EmailStr,Field
from datetime import datetime


class UserCreate(BaseModel):

    username: str
    email: EmailStr
    password: str =Field(
    min_length=8,
    max_length=72
)


class UserResponse(BaseModel):

    id: int
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime

class LoginRequest(BaseModel):

    email: EmailStr
    password: str


class TokenResponse(BaseModel):

    access_token: str
    token_type: str

    class Config:
        from_attributes = True