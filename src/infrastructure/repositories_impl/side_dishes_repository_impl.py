from typing import List

from application.repositories.side_dishes_repository import SideDishesRepository
from domain.entities.side_dish import SideDish
from infrastructure.db.base import async_engine, async_session_factory, Base
from infrastructure.db.models.side_dishes_orm import SideDishesOrm
from sqlalchemy import select, delete, text


class SideDishesRepositoryImpl(SideDishesRepository):
    @staticmethod
    async def get(side_dish_id: int)-> SideDish:
        async with async_session_factory() as session:
            side_dish = await session.query(SideDishesOrm, side_dish_id).first()
            return side_dish

    @staticmethod
    async def get_all_from_canteen(canteen_id: int) -> list[SideDish]:
        async with async_session_factory() as session:
            query = (
                select(SideDishesOrm)
                .filter(SideDishesOrm.canteen_id == int(canteen_id))
            )
            res = await session.execute(query)
            side_dishes = res.scalars().all()
            return side_dishes

    @staticmethod
    async def get_all() -> list[SideDish]:
        async with async_session_factory() as session:
            query = select(SideDishesOrm)
            res = await session.execute(query)
            side_dishes = res.scalars().all()
            return side_dishes

    @staticmethod
    async def save(side_dish: SideDish):
        async with async_session_factory() as session:
            side_dish = SideDishesOrm(
                name=side_dish.name,
                type=side_dish.type,
                price=side_dish.price,
                properties=side_dish.properties,
                canteen_id=side_dish.canteen_id
            )
            session.add(side_dish)
            await session.commit()

    @staticmethod
    async def save_many(side_dishes: List[SideDish]):
        async with async_session_factory() as session:
            for dish in side_dishes:
                main_dish = SideDishesOrm(
                    name=dish.name,
                    type=dish.type,
                    price=dish.price,
                    properties=dish.properties,
                    canteen_id=dish.canteen_id
                )
                session.add(main_dish)
            await session.commit()

    @staticmethod
    async def delete_old_dishes(canteen_id: int):
        async with async_session_factory() as session:
            query = (
                delete(SideDishesOrm)
                .filter(SideDishesOrm.canteen_id == int(canteen_id))
            )
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def delete_all() -> None:
        async with async_session_factory() as session:
            await session.execute(delete(SideDishesOrm))
            await session.execute(text(f"ALTER SEQUENCE {SideDishesOrm.__tablename__}_side_dish_id_seq RESTART WITH 1;"))

            await session.commit()
