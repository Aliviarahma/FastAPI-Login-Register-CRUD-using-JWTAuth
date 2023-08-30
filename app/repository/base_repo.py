from multiprocessing import synchronize
from statistics import mode
from typing import Generic, TypeVar
from sqlalchemy import update as sql_update, delete as sql_delete, desc
from sqlalchemy.future import select
from app.config import db, commit_rollback

T = TypeVar('T')


class BaseRepo:
    model = Generic[T]

    @classmethod
    async def create(cls, **kwargs):
        model = cls.model(**kwargs)
        db.add(model)
        await commit_rollback()
        return model

    @classmethod
    async def get_all(cls):
        query = select(cls.model)
        return(await db.execute(query)).scalars().all()


    @classmethod
    async def get_by_progress(cls, model_order_closing_date: str, model_treg: str):
        query = select(cls.model).where((cls.model.order_closing_date.is_(None)) & (cls.model.treg == model_treg))
        return (await db.execute(query)).scalar().all()


    @classmethod
    async def get_by_nullvalue(cls, model_crm_order_type: str, order_created_date: str):
        query = select(cls.model).where(
            (cls.model.crm_order_type == None) | (cls.model.order_created_date == model_order_created_date)
        )
        return [result.id for result in (await db.execute(query)).scalars().all()]

    @classmethod
    async def get_by_id(cls, model_id: str):
        query = select(cls.model).where(cls.model.id == model_id)
        return (await db.execute(query)).scalar_one_or_none()

    @classmethod
    async def update(cls, model_id: str, **kwargs):
        query = sql_update(cls.model).where(cls.model.id == model_id).values(
            **kwargs).execution_options(synchronize_session="fetch")
        await db.execute(query)
        await commit_rollback()

    @classmethod
    async def delete(cls, model_id: str):
        query = sql_delete(cls.model).where(cls.model.id == model_id)
        await db.execute(query)
        await commit_rollback()
