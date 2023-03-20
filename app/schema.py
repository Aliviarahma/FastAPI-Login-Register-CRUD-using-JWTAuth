from fastapi import HTTPException
import logging
import re
from typing import TypeVar, Optional

from pydantic import BaseModel, validator
from sqlalchemy import false
from app.model.person import role


T = TypeVar('T')

# get root logger
logger = logging.getLogger(__name__)


class RegisterSchema(BaseModel):

    username: str
    email: str
    name: str
    password: str
    role: role
    # profile: str = "base64"


class LoginSchema(BaseModel):
    username: str
    password: str


class ForgotPasswordSchema(BaseModel):
    email: str
    new_password: str


class DetailSchema(BaseModel):
    status: str
    message: str
    result: Optional[T] = None


class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None