from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from app.config2 import SessionLocal
#from app.config import db
from sqlalchemy.orm import Session
from app.schema import OrderSchema, Request, Response, RequestOrder, AddOrderSchema, RequestAddOrder
from sqlalchemy.dialects.mysql import VARCHAR

import app.repository.add_order as order

router = APIRouter(
    prefix="/add_orders",
    tags=['add_orders']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
async def create_add_order(request: RequestAddOrder, db: Session = Depends(get_db)):
    order.create_add_order(db, add_order=request.parameter)
    return ResponseAdd(status="Ok",
                    code="200",
                    message="Order created successfully").dict(exclude_none=True)

@router.get("/")
async def get_add_order(skip: int = 0, limit: int = 99999, db: Session = Depends(get_db)):
    _addOrder = order.get_add_order(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_addOrder)

