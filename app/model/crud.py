from sqlalchemy import  Column, Integer, String, Numeric, Date, VARCHAR, Boolean
from app.config2 import Base
import app.model.crud as models
from app.config2 import engine
from sqlalchemy.dialects.mysql import VARCHAR
from sqlmodel import SQLModel
from app.model.mixins import TimeMixin, TimestampMixin

models.Base.metadata.create_all(bind=engine)

class Order(TimestampMixin, Base):
    __tablename__ ="orders"

    id = Column(VARCHAR, primary_key=True, index=True)	
    order_id = Column(VARCHAR)
    customer = Column(VARCHAR)	
    product = Column(VARCHAR)	



