from datetime import date
from typing import Optional
from sqlalchemy import Enum, table
from sqlmodel import SQLModel, Field, Relationship
from app.model.mixins import TimeMixin


class role(str, Enum):
    Admin = "Admin"
    Business = "Business"
    DBS = "DBS"
    Marketing = "Marketing"
    Tech = "Tech"


class Person(SQLModel, TimeMixin, table=True):
    __tablename__ = "person"

    id: Optional[str] = Field(None, primary_key=True, nullable=False)
    name: str
    role: str

    users: Optional["Users"] = Relationship(
        sa_relationship_kwargs={'uselist': False}, back_populates="person")