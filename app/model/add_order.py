from sqlalchemy import  Column, Integer, String, Numeric, Date, VARCHAR, Boolean
from app.config2 import Base
import app.model.crud as models
from app.config2 import engine
from sqlalchemy.dialects.mysql import VARCHAR
from sqlmodel import SQLModel
from app.model.mixins import TimeMixin, TimestampMixin

models.Base.metadata.create_all(bind=engine)


class addOrder(TimestampMixin, Base):
    __tablename__ ="add_order"

    order_id = Column(VARCHAR, primary_key=True, index=True)	
    nama_pelanggan = Column(VARCHAR)
    nomor_internet = Column(VARCHAR)
    nomor_hp = Column(VARCHAR)
    email_pelanggan = Column(VARCHAR)
    witel = Column(VARCHAR)
    pic = Column(VARCHAR)
    source_order = Column(VARCHAR)