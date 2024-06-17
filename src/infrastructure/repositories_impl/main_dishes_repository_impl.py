from typing import List

from application.repositories.main_dishes_repository import MainDishesRepository
from domain.entities.main_dish import MainDish
from infrastructure.db.base import sync_engine, session_factory, Base
from infrastructure.db.models.main_dishes_orm import MainDishesOrm
from sqlalchemy import select, delete, text

from infrastructure.db.models.canteens_orm import CanteensOrm
from infrastructure.db.models.side_dishes_orm import SideDishesOrm


class MainDishesRepositoryImpl(MainDishesRepository):
    @staticmethod
    def get(main_dish_id: int) -> MainDish:
        with session_factory() as session:
            main_dish = session.get(MainDishesOrm, main_dish_id).first()
            return main_dish

    @staticmethod
    def get_all_from_canteen(canteen_id: int) -> List[MainDish]:
        with session_factory() as session:
            query = (
                select(MainDishesOrm)
                .filter(MainDishesOrm.canteen_id == int(canteen_id))
            )

            res = session.execute(query)
            main_dishes = res.scalars().all()
            print(main_dishes)
            return main_dishes

    @staticmethod
    def get_all() -> List[MainDish]:
        with session_factory() as session:
            query = (select(MainDishesOrm))
            res = session.execute(query)
            main_dishes = res.scalars().all()
            return main_dishes

    @staticmethod
    def save(main_dish: MainDish):
        with session_factory() as session:
            main_dish = MainDishesOrm(
                name=main_dish.name,
                type=main_dish.type,
                price=main_dish.price,
                properties=main_dish.properties,
                canteen_id=main_dish.canteen_id
            )
            session.add(main_dish)
            session.commit()

    @staticmethod
    def save_many(main_dishes: List[MainDish]):
        with session_factory() as session:
            for dish in main_dishes:
                main_dish = MainDishesOrm(
                    name=dish.name,
                    type=dish.type,
                    price=dish.price,
                    properties=dish.properties,
                    canteen_id=dish.canteen_id
                )
                session.add(main_dish)
            session.commit()

    @staticmethod
    def delete_old_dishes(canteen_id: int):
        with session_factory() as session:
            query = (
                delete(MainDishesOrm)
                .filter(MainDishesOrm.canteen_id == int(canteen_id))
            )
            session.execute(query)
            session.commit()

    @staticmethod
    def delete_all() -> None:
        with session_factory() as session:
            session.execute(delete(MainDishesOrm))
            session.execute(text(f"ALTER SEQUENCE {MainDishesOrm.__tablename__}_main_dish_id_seq RESTART WITH 1;"))

            session.commit()


