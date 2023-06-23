from fastapi import HTTPException
import logging
import re
from typing import TypeVar, Optional, List, Optional, Generic

from pydantic import BaseModel, validator, Field
from pydantic.generics import GenericModel
from sqlalchemy import false
from app.model.person import role
from datetime import date

#CRUD System



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
    subs_id: Optional[str] = None
    #nama_customer: Optional[str] = None
    account_name: Optional[str] = None
    produk: Optional[str] = None	
    #order_id: Optional[str] = None	
    #crm_order_type: Optional[str] = None
    #agreement_name: Optional[str] = None	
    #location: Optional[str] = None
    pic_am: Optional[str] = None	
    sid: Optional[int] = None
    #treg: Optional[str] = None
    witel: Optional[str] = None
    #divisi: Optional[str] = None
    #segment: Optional[str] = None
    durasi_berlangganan: Optional[str] = None	
    nilai_revenue: Optional[int] = None
    revenue_per_bulan: Optional[int] = None	
    #order_created_date: Optional[date] = None	
    no_order_astinet: Optional[str] = None
    upload_dokumen: Optional[str] = None	
    document: Optional[bool] = None	
    activate_account: Optional[bool] = None	
    activation_date: Optional[date] = None
    input_ip: Optional[bool] = None
    link_dashboard: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    auth_netmonk_hi: Optional[str] = None
    draft_bast: Optional[str] = None
    bast_upload_date: Optional[date] = None
    status_bast: Optional[str] = None
    status_internal_netmonk_teknis: Optional[str] = None	
    status_internal_netmonk_admin: Optional[str] = None
    order_closing_date: Optional[date] = None
    # order_status: Optional[str] = None
    # li_milestone: Optional[str] = None
    # tgl_fbc: Optional[date] = None
    #id_update: Optional[str] = None
    

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
