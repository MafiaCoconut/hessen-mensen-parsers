from typing import List

from icecream import ic
from sqlalchemy.ext.asyncio import AsyncSession

from application.repositories.main_dishes_repository import MainDishesRepository
from domain.entities.main_dish import MainDish
from infrastructure.db.base import async_engine, async_session_factory, Base
from infrastructure.db.models.main_dishes_orm import MainDishesOrm
from sqlalchemy import select, delete, text

from infrastructure.db.models.canteens_orm import CanteensOrm
from infrastructure.db.models.side_dishes_orm import SideDishesOrm


class MainDishesRepositoryImpl(MainDishesRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, main_dish_id: int) -> MainDish:
        async with self.session.begin():
            query = (
                select(MainDishesOrm)
                .where(MainDishesOrm.main_dish_id == int(main_dish_id))
                .first()
            )
            res = await self.session.execute(query)
            main_dish = res.scalars().first()

            return MainDish(
                main_dish_id=main_dish.main_dish_id,
                name=main_dish.name,
                type=main_dish.type,
                price=main_dish.price,
                properties=main_dish.properties,
                canteen_id=main_dish.canteen_id,
            )

    async def get_all_from_canteen(self, canteen_id: int) -> List[MainDish]:
        async with self.session.begin():
            query = (
                select(MainDishesOrm)
                .filter(MainDishesOrm.canteen_id == int(canteen_id))
            )
            res = await self.session.execute(query)
            main_dishes = res.scalars().all()

            return [MainDish(
                main_dish_id=main_dish.main_dish_id,
                name=main_dish.name,
                type=main_dish.type,
                price=main_dish.price,
                properties=main_dish.properties,
                canteen_id=main_dish.canteen_id,
            ) for main_dish in main_dishes]

    async def get_all(self) -> List[MainDish]:
        async with self.session.begin():
            query = (select(MainDishesOrm))
            res = await self.session.execute(query)
            main_dishes = res.scalars().all()

            return [MainDish(
                main_dish_id=main_dish.main_dish_id,
                name=main_dish.name,
                type=main_dish.type,
                price=main_dish.price,
                properties=main_dish.properties,
                canteen_id=main_dish.canteen_id,
            ) for main_dish in main_dishes]

    async def save(self, main_dish: MainDish):
        async with self.session.begin():
            main_dish = MainDishesOrm(
                name=main_dish.name,
                type=main_dish.type,
                price=main_dish.price,
                properties=main_dish.properties,
                canteen_id=main_dish.canteen_id
            )
            self.session.add(main_dish)
            await self.session.commit()

    async def save_many(self, main_dishes: List[MainDish]):
        async with self.session.begin():
            for dish in main_dishes:
                main_dish = MainDishesOrm(
                    name=dish.name,
                    type=dish.type,
                    price=dish.price,
                    properties=dish.properties,
                    canteen_id=dish.canteen_id
                )
                self.session.add(main_dish)
            await self.session.commit()

    async def delete_old_dishes(self, canteen_id: int):
        async with self.session.begin():
            query = (
                delete(MainDishesOrm)
                .filter(MainDishesOrm.canteen_id == int(canteen_id))
            )
            await self.session.execute(query)
            await self.session.commit()

    async def delete_all(self) -> None:
        async with self.session.begin():
            await self.session.execute(delete(MainDishesOrm))
            await self.session.execute(
                text(f"ALTER SEQUENCE {MainDishesOrm.__tablename__}_main_dish_id_seq RESTART WITH 1;"))

            await self.session.commit()
