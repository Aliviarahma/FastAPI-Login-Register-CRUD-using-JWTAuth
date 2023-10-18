from fastapi import HTTPException
import logging
import re
from typing import TypeVar, Optional, List, Optional, Generic

from pydantic import BaseModel, validator, Field
from pydantic.generics import GenericModel
from sqlalchemy import false
from app.model.person import role
from datetime import date


T = TypeVar('T')

# get root logger
logger = logging.getLogger(__name__)


class RegisterSchema(BaseModel):

    username: str
    email: str
    name: str
    password: str
    role: str
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


#CRUD system
class OrderSchema(BaseModel):
    id: Optional[str] = None
    order_id: Optional[str] = None
    customer: Optional[str] = None
    product: Optional[str] = None	


    class Config:
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)
    
class RequestOrder(BaseModel):
    parameter: OrderSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

