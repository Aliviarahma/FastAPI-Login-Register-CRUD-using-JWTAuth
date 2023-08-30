from sqlalchemy import  Column, Integer, String, Numeric, Date, VARCHAR, Boolean
from app.config2 import Base
import app.model.crud as models
from app.config2 import engine
from sqlalchemy.dialects.mysql import VARCHAR
from sqlmodel import SQLModel
from app.model.mixins import TimeMixin, TimestampMixin

models.Base.metadata.create_all(bind=engine)

class Order(TimestampMixin, Base):
    __tablename__ ="netmonk_fulfillment"

    id = Column(VARCHAR, primary_key=True, index=True)	
    subs_id = Column(VARCHAR)
    nama_customer = Column(VARCHAR)	
    account_name = Column(VARCHAR)	
    produk = Column(VARCHAR)	
    order_id = Column(VARCHAR)	
    crm_order_type = Column(VARCHAR)
    agreement_name = Column(VARCHAR)	
    location = Column(VARCHAR)	
    pic_am = Column(VARCHAR)	
    sid = Column(Integer)	
    treg = Column(VARCHAR)	
    witel = Column(VARCHAR)	
    divisi = Column(VARCHAR)	
    segment = Column(VARCHAR)	
    durasi_berlangganan = Column(VARCHAR)	
    nilai_revenue = Column(Numeric)	
    revenue_per_bulan = Column(Numeric)	
    order_created_date = Column(Date)	
    no_order_astinet = Column(VARCHAR)	
    upload_dokumen = Column(VARCHAR)	
    document = Column(Boolean)	
    activate_account = Column(Boolean)	
    activation_date = Column(Date)	
    input_ip = Column(Boolean)	
    link_dashboard = Column(VARCHAR)	
    username = Column(VARCHAR)	
    password = Column(VARCHAR)	
    auth_netmonk_hi = Column(VARCHAR)	
    draft_bast = Column(VARCHAR)	
    bast_upload_date = Column(Date)	
    status_bast = Column(VARCHAR)	
    status_internal_netmonk_teknis = Column(VARCHAR)	
    status_internal_netmonk_admin = Column(VARCHAR)	
    order_closing_date = Column(Date)
    order_status = Column(VARCHAR)
    li_milestone = Column(VARCHAR)
    tgl_fbc = Column(Date)


