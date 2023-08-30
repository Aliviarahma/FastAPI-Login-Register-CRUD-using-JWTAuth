from sqlalchemy.orm import Session
from app.model.crud import Order
from app.schema import OrderSchema


from sqlalchemy.dialects.mysql import VARCHAR


def get_order(db: Session, skip: int = 0, limit: int = 99999):
    return db.query(Order).offset(skip).limit(limit).all()


def get_order_by_progress(db: Session, order_closing_date: str, treg: str):
    return db.query(Order).filter((Order.order_closing_date.is_(None)) & (Order.treg == treg)).all()


def get_order_by_id(db: Session, wfm_id: str):
    return db.query(Order).filter(Order.id == wfm_id).first()


def get_order_by_nullvalue(db: Session, pic_am: str, li_milestone: str):
    return db.query(Order.order_id).filter((Order.pic_am == None) | (Order.li_milestone == None)).all()


def create_order(db: Session, order: OrderSchema):
    _order = Order(id=order.id, subs_id = order.subs_id, nama_customer = order.nama_customer, account_name = order.account_name, produk = order.produk, order_id = order.order_id, crm_order_type= order.crm_order_type, agreement_name = order.agreement_name, location = order.location, pic_am = order.pic_am, sid = order.sid, treg = order.treg, witel = order.witel, divisi = order.divisi, segment = order.segment, durasi_berlangganan = order.durasi_berlangganan, nilai_revenue = order.nilai_revenue, revenue_per_bulan = order.revenue_per_bulan, order_created_date = order.order_created_date, no_order_astinet = order.no_order_astinet, upload_dokumen = order.upload_dokumen, document = order.document, activate_account = order.activate_account, activation_date = order.activation_date, input_ip = order.input_ip, link_dashboard = order.link_dashboard, username = order.username, password = order.password, auth_netmonk_hi = order.auth_netmonk_hi, draft_bast = order.draft_bast, bast_upload_date = order.bast_upload_date, status_bast = order.status_bast, status_internal_netmonk_teknis = order.status_internal_netmonk_teknis, status_internal_netmonk_admin = order.status_internal_netmonk_admin, order_closing_date = order.order_closing_date, order_status = order.order_status, li_milestone = order.li_milestone, tgl_fbc = order.tgl_fbc)
    db.add(_order)
    db.commit()
    db.refresh(_order)
    return _order


def remove_order(db: Session, wfm_id: str):
    _order = get_order_by_id(db=db, wfm_id=wfm_id)
    db.delete(_order)
    db.commit()


def update_order(db: Session, wfm_id: str, subs_id: str, account_name: str, produk: str, pic_am: str, sid: int, witel: str, durasi_berlangganan: str, nilai_revenue: int, revenue_per_bulan: int, no_order_astinet: str, upload_dokumen: str, document: bool, activate_account: bool, activation_date: int, input_ip: bool, link_dashboard: str, username: str, password: str, auth_netmonk_hi: str, draft_bast: str, bast_upload_date: int, status_bast: str, status_internal_netmonk_teknis: str, status_internal_netmonk_admin: str, order_closing_date: int):

    _order = get_order_by_id(db=db, wfm_id=wfm_id)
    _order.subs_id = subs_id
    #_order.nama_customer = nama_customer	
    _order.account_name = account_name	
    _order.produk = produk
    #_order.order_id = order_id 	
    #_order.crm_order_type = crm_order_type
    #_order.agreement_name = agreement_name	
    #_order.location = location	
    _order.pic_am = pic_am
    _order.sid = sid	
    #_order.treg = treg	
    _order.witel = witel
    #_order.divisi = divisi
    #_order.segment = segment	
    _order.durasi_berlangganan = durasi_berlangganan	
    _order.nilai_revenue = nilai_revenue	
    _order.revenue_per_bulan = revenue_per_bulan	
    #_order.order_created_date = order_created_date	
    _order.no_order_astinet = no_order_astinet	
    _order.upload_dokumen = upload_dokumen
    _order.document = document	
    _order.activate_account = activate_account	
    _order.activation_date = activation_date	
    _order.input_ip = input_ip	
    _order.link_dashboard = link_dashboard
    _order.username = username	
    _order.password = password	
    _order.auth_netmonk_hi = auth_netmonk_hi	
    _order.draft_bast = draft_bast 	
    _order.bast_upload_date = bast_upload_date
    _order.status_bast = status_bast	
    _order.status_internal_netmonk_teknis = status_internal_netmonk_teknis	
    _order.status_internal_netmonk_admin = status_internal_netmonk_admin	
    _order.order_closing_date = order_closing_date
    #_order.order_status = order_status
    #_order.li_milestone = li_milestone
    #_order.tgl_fbc = tgl_fbc
    #_order.id_update = id_update

    db.commit()
    db.refresh(_order)
    return _order






