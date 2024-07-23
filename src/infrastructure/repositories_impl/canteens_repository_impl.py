from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete, text
from application.repositories.canteens_repository import CanteensRepository
from domain.entities.canteen import Canteen
from infrastructure.db.base import async_engine, async_session_factory
from infrastructure.db.models.canteens_orm import CanteensOrm
from icecream import ic


class CanteensRepositoryImpl(CanteensRepository):
    async def get_all(self) -> List[Canteen]:
        async with async_session_factory() as session:
            query = select(CanteensOrm)
            result = await session.execute(query)
            canteens = result.scalars().all()

            return canteens

    async def get(self, canteen_id: int) -> Canteen:
        async with async_session_factory() as session:
            canteen = await session.get(CanteensOrm, canteen_id)
            return canteen

    async def save(self, canteen: Canteen = None) -> None:
        async with async_session_factory() as session:

            canteen_orm = CanteensOrm(
                canteen_id=canteen.canteen_id,
                name=canteen.name,
                opened_time=canteen.opened_time,
                closed_time=canteen.closed_time,
                description=canteen.description,
                created_at=canteen.created_at
            )
            session.add(canteen_orm)
            await session.commit()

    async def delete_all(self) -> None:
        async with async_session_factory() as session:
            await session.execute(delete(CanteensOrm))
            await session.execute(text(f"ALTER SEQUENCE {CanteensOrm.__tablename__}_canteen_id_seq RESTART WITH 1;"))

            await session.commit()

    async def delete(self, canteen_id: int) -> None:
        async with async_session_factory() as session:
            query = (
                delete(CanteensOrm)
                .filter(CanteensOrm.canteen_id == int(canteen_id))
            )
            await session.execute(query)
            await session.commit()


