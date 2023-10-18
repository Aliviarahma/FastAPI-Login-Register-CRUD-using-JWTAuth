from sqlalchemy.orm import Session
from app.model.crud import Order
from app.schema import OrderSchema


from sqlalchemy.dialects.mysql import VARCHAR


def get_order(db: Session, skip: int = 0, limit: int = 99999):
    return db.query(Order).offset(skip).limit(limit).all()


def create_order(db: Session, order: OrderSchema):
    _order = Order(id=order.id, order_id = order.subs_id, customer = order.nama_customer, product = order.product)
    db.add(_order)
    db.commit()
    db.refresh(_order)
    return _order


def remove_order(db: Session, id: str):
    _order = get_order_by_id(db=db, id=id)
    db.delete(_order)
    db.commit()


def update_order(db: Session, id: str, order_id: str, customer: str, product: str,):

    _order = get_order_by_id(db=db, id=id)
    _order.id = id
    _order.order_id = order_id
    _order.customer = nama_customer	
    _order.product = product


    db.commit()
    db.refresh(_order)
    return _order






