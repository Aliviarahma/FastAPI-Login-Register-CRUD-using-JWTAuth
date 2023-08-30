from sqlalchemy.orm import Session
from app.model.add_order import addOrder
from app.schema import AddOrderSchema

from sqlalchemy.dialects.mysql import VARCHAR


def create_add_order(db: Session, add_order: AddOrderSchema):
    _addOrder = addOrder(order_id = add_order.order_id, nama_pelanggan = add_order.nama_pelanggan, nomor_internet = add_order.nomor_internet, nomor_hp = add_order.nomor_hp, email_pelanggan = add_order.email_pelanggan, witel = add_order.witel, pic = add_order.pic, source_order = add_order.source_order)
    db.add(_addOrder)
    db.commit()
    db.refresh(_addOrder)
    return _addOrder

def get_add_order(db: Session, skip: int = 0, limit: int = 99999):
    return db.query(addOrder).offset(skip).limit(limit).all()




