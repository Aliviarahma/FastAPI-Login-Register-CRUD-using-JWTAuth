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
    tags=['orders']
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


@router.get("/progress")
async def get_order_by_progress(order_closing_date: str, treg: str, db: Session = Depends(get_db)):
    _orders = crud.get_order_by_progress(db, order_closing_date, treg)
    return Response(status="Ok", code="200", message="Success fetch data", result=_orders)


@router.get("/nullvalue")
async def get_order_by_nullvalue(pic_am: str, li_milestone: str, db: Session = Depends(get_db)):
    _orders = crud.get_order_by_nullvalue(db, pic_am, li_milestone)
    return Response(status="Ok", code="200", message="Success fetch data", result=_orders)


@router.get("/{id}")
async def get_order_by_id(id: str, db: Session = Depends(get_db)):
    _orders = crud.get_order_by_id(db, wfm_id=id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_orders)


@router.put("/update")
async def update_order(request: RequestOrder, db: Session = Depends(get_db)):
    _order = crud.update_order(db, wfm_id=request.parameter.id,
                             subs_id = request.parameter.subs_id, account_name = request.parameter.account_name, produk = request.parameter.produk, pic_am = request.parameter.pic_am, sid = request.parameter.sid, witel = request.parameter.witel, durasi_berlangganan = request.parameter.durasi_berlangganan, nilai_revenue = request.parameter.nilai_revenue, revenue_per_bulan = request.parameter.revenue_per_bulan, no_order_astinet = request.parameter.no_order_astinet, upload_dokumen = request.parameter.upload_dokumen, document = request.parameter.document, activate_account = request.parameter.activate_account, activation_date = request.parameter.activation_date, input_ip = request.parameter.input_ip, link_dashboard = request.parameter.link_dashboard, username = request.parameter.username, password = request.parameter.password, auth_netmonk_hi = request.parameter.auth_netmonk_hi, draft_bast = request.parameter.draft_bast, bast_upload_date = request.parameter.bast_upload_date, status_bast = request.parameter.status_bast, status_internal_netmonk_teknis = request.parameter.status_internal_netmonk_teknis, status_internal_netmonk_admin = request.parameter.status_internal_netmonk_admin, order_closing_date = request.parameter.order_closing_date)
    return Response(status="Ok", code="200", message="Success update data", result=_order)


@router.delete("/{id}")
async def delete_order(id: str,  db: Session = Depends(get_db)):
    crud.remove_order(db, wfm_id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)

