from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from application.repositories.side_dishes_repository import SideDishesRepository
from domain.entities.side_dish import SideDish
from infrastructure.config.logs_config import log_decorator
from infrastructure.db.base import async_engine, async_session_factory, Base
from infrastructure.db.models.side_dishes_orm import SideDishesOrm
from sqlalchemy import select, delete, text


class SideDishesRepositoryImpl(SideDishesRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    @log_decorator()
    async def get(self, side_dish_id: int) -> SideDish:
        async with self.session.begin():
            query = select(SideDishesOrm).where(SideDishesOrm.side_dish_id == side_dish_id)
            result = await self.session.execute(query)
            side_dish = result.scalars().first()
            return SideDish(
                side_dish_id=side_dish.side_dish_id,
                name=side_dish.name,
                type=side_dish.type,
                price=side_dish.price,
                properties=side_dish.properties,
                canteen_id=side_dish.canteen_id,
                created_at=side_dish.created_at,
                updated_at=side_dish.updated_at,
            )

    @log_decorator()
    async def get_all_from_canteen(self, canteen_id: int) -> list[SideDish]:
        async with self.session.begin():
            query = (
                select(SideDishesOrm)
                .where(SideDishesOrm.canteen_id == int(canteen_id))
            )
            res = await self.session.execute(query)

            return [SideDish(
                side_dish_id=side_dish.side_dish_id,
                name=side_dish.name,
                type=side_dish.type,
                price=side_dish.price,
                properties=side_dish.properties,
                canteen_id=side_dish.canteen_id,
                created_at=side_dish.created_at,
                updated_at=side_dish.updated_at,
            ) for side_dish in res.scalars().all()]

    @log_decorator()
    async def get_all(self) -> list[SideDish]:
        async with self.session.begin():
            query = select(SideDishesOrm)
            res = await self.session.execute(query)

            return [SideDish(
                side_dish_id=side_dish.side_dish_id,
                name=side_dish.name,
                type=side_dish.type,
                price=side_dish.price,
                properties=side_dish.properties,
                canteen_id=side_dish.canteen_id,
                created_at=side_dish.created_at,
                updated_at=side_dish.updated_at,
            ) for side_dish in res.scalars().all()]

    @log_decorator(print_kwargs=False)
    async def save(self, side_dish: SideDish):
        async with self.session.begin():
            side_dish = SideDishesOrm(
                name=side_dish.name,
                type=side_dish.type,
                price=side_dish.price,
                properties=side_dish.properties,
                canteen_id=side_dish.canteen_id
            )
            self.session.add(side_dish)
            await self.session.commit()

    @log_decorator(print_kwargs=False)
    async def save_many(self, side_dishes: List[SideDish]):
        async with self.session.begin():
            for dish in side_dishes:
                main_dish = SideDishesOrm(
                    name=dish.name,
                    type=dish.type,
                    price=dish.price,
                    properties=dish.properties,
                    canteen_id=dish.canteen_id
                )
                self.session.add(main_dish)
            await self.session.commit()

    @log_decorator()
    async def delete_old_dishes(self, canteen_id: int):
        async with self.session.begin():
            query = (
                delete(SideDishesOrm)
                .where(SideDishesOrm.canteen_id == int(canteen_id))
            )
            await self.session.execute(query)
            await self.session.commit()

    @log_decorator()
    async def delete_all(self) -> None:
        async with self.session.begin():
            await self.session.execute(delete(SideDishesOrm))
            await self.session.execute(
                text(f"ALTER SEQUENCE {SideDishesOrm.__tablename__}_side_dish_id_seq RESTART WITH 1;"))

            await self.session.commit()
