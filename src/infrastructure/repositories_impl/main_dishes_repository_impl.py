from typing import List

from application.repositories.main_dishes_repository import MainDishesRepository
from domain.entities.main_dish import MainDish
from infrastructure.db.base import async_engine, async_session_factory, Base
from infrastructure.db.models.main_dishes_orm import MainDishesOrm
from sqlalchemy import select, delete, text

from infrastructure.db.models.canteens_orm import CanteensOrm
from infrastructure.db.models.side_dishes_orm import SideDishesOrm


class MainDishesRepositoryImpl(MainDishesRepository):
    @staticmethod
    async def get(main_dish_id: int) -> MainDish:
        async with async_session_factory() as session:
            main_dish = await session.get(MainDishesOrm, main_dish_id).first()
            return main_dish

    @staticmethod
    async def get_all_from_canteen(canteen_id: int) -> List[MainDish]:
        async with async_session_factory() as session:
            query = (
                select(MainDishesOrm)
                .filter(MainDishesOrm.canteen_id == int(canteen_id))
            )

            res = await session.execute(query)
            main_dishes = res.scalars().all()
            # print(main_dishes)
            return main_dishes

    @staticmethod
    async def get_all() -> List[MainDish]:
        async with async_session_factory() as session:
            query = (select(MainDishesOrm))
            res = await session.execute(query)
            main_dishes = res.scalars().all()
            return main_dishes

    @staticmethod
    async def save(main_dish: MainDish):
        async with async_session_factory() as session:
            main_dish = MainDishesOrm(
                name=main_dish.name,
                type=main_dish.type,
                price=main_dish.price,
                properties=main_dish.properties,
                canteen_id=main_dish.canteen_id
            )
            session.add(main_dish)
            await session.commit()

    @staticmethod
    async def save_many(main_dishes: List[MainDish]):
        async with async_session_factory() as session:
            for dish in main_dishes:
                main_dish = MainDishesOrm(
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
                delete(MainDishesOrm)
                .filter(MainDishesOrm.canteen_id == int(canteen_id))
            )
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def delete_all() -> None:
        async with async_session_factory() as session:
            await session.execute(delete(MainDishesOrm))
            await session.execute(text(f"ALTER SEQUENCE {MainDishesOrm.__tablename__}_main_dish_id_seq RESTART WITH 1;"))

            await session.commit()


