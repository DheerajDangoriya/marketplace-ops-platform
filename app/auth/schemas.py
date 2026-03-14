"""Data schemas for authentication payloads."""
from pydantic import BaseModel
from typing import Optional


class LoginRequest(BaseModel):
    """Login request schema."""
    username: str
    password: str


class TokenResponse(BaseModel):
    """Token response schema."""
    access_token: str
    token_type: str = "bearer"


class UserSchema(BaseModel):
    """User schema."""
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None