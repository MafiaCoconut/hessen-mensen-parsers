from typing import List, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete, text
from application.repositories.canteens_repository import CanteensRepository
from domain.entities.canteen import Canteen
from infrastructure.db.base import async_engine, async_session_factory
from infrastructure.db.models.canteens_orm import CanteensOrm
from icecream import ic
from application.exceptions.repositories_exceptions import CanteenWrongDataException, CanteenNotFoundException


class CanteensRepositoryImpl(CanteensRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> Sequence[Canteen]:
        async with self.session.begin():
            query = select(CanteensOrm)
            result = await self.session.execute(query)
            canteens = result.scalars().all()
            return [Canteen(
                canteen_id=canteen.canteen_id,
                name=canteen.name,
                description=canteen.description,
                opened_time=canteen.opened_time,
                closed_time=canteen.closed_time,
                created_at=canteen.created_at,
            ) for canteen in canteens]

    async def get(self, canteen_id: int) -> Canteen:
        async with self.session.begin():
            query = select(CanteensOrm).where(CanteensOrm.canteen_id == canteen_id)
            res = await self.session.execute(query)
            canteen = res.scalars().first()
            if canteen is None:
                raise CanteenNotFoundException()
            try:
                return Canteen(
                    canteen_id=canteen.canteen_id,
                    name=canteen.name,
                    description=canteen.description,
                    opened_time=canteen.opened_time,
                    closed_time=canteen.closed_time,
                    created_at=canteen.created_at,
                )
            except:
                raise CanteenWrongDataException()

    async def save(self, canteen: Canteen = None) -> None:
        async with self.session.begin():
            canteen_orm = CanteensOrm(
                canteen_id=canteen.canteen_id,
                name=canteen.name,
                opened_time=canteen.opened_time,
                closed_time=canteen.closed_time,
                description=canteen.description,
                created_at=canteen.created_at
            )
            self.session.add(canteen_orm)
            await self.session.commit()

    async def delete_all(self) -> None:
        async with self.session.begin():
            await self.session.execute(delete(CanteensOrm))
            await self.session.execute(text(f"ALTER SEQUENCE {CanteensOrm.__tablename__}_canteen_id_seq RESTART WITH 1;"))

            await self.session.commit()

    async def delete(self, canteen_id: int) -> None:
        async with self.session.begin():
            query = (
                delete(CanteensOrm)
                .filter(CanteensOrm.canteen_id == int(canteen_id))
            )
            await self.session.execute(query)
            await self.session.commit()


