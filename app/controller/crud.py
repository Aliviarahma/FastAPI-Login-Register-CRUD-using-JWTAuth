from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from app.config2 import SessionLocal
#from app.config import db
from sqlalchemy.orm import Session
from app.schema import OrderSchema, Request, Response, RequestOrder, AddOrderSchema, RequestAddOrder
from sqlalchemy.dialects.mysql import VARCHAR

import app.repository.crud as crud

router = APIRouter(
    prefix="/orders",
    tags=['Orders']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
async def create_order_service(request: RequestOrder, db: Session = Depends(get_db)):
    crud.create_order(db, order=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Order created successfully").dict(exclude_none=True)


@router.get("/")
async def get_orders(skip: int = 0, limit: int = 99999, db: Session = Depends(get_db)):
    _orders = crud.get_order(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_orders)


@router.get("/{id}")
async def get_order_by_id(id: str, db: Session = Depends(get_db)):
    _orders = crud.get_order_by_id(db, id=id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_orders)


@router.put("/update")
async def update_order(request: RequestOrder, db: Session = Depends(get_db)):
    _order = crud.update_order(db, id=request.parameter.id,
                             order_id = request.parameter.order_id, customer = request.parameter.customer, product = request.parameter.product)
    return Response(status="Ok", code="200", message="Success update data", result=_order)


@router.delete("/{id}")
async def delete_order(id: str,  db: Session = Depends(get_db)):
    crud.remove_order(db, id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)

