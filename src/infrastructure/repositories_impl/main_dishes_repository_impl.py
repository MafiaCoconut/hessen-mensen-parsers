
from application.repositories.main_dishes_repository import MainDishesRepository
from domain.entities.main_dish import MainDish
from infrastructure.db.base import sync_engine, session_factory, Base
from infrastructure.db.models.main_dishes_orm import MainDishesOrm
from sqlalchemy import select

from infrastructure.db.models.canteens_orm import CanteensOrm
from infrastructure.db.models.side_dishes_orm import SideDishesOrm

class MainDishesRepositoryImpl(MainDishesRepository):
    @staticmethod
    def get(main_dish_id: int):
        with session_factory() as session:
            main_dish = session.get(MainDishesOrm, main_dish_id).first()
            return main_dish

    @staticmethod
    def get_all_from_canteen(canteen_id: int):
        with session_factory() as session:
            query = (
                select(MainDishesOrm)
                .filter(MainDishesOrm.canteen_id == canteen_id)
            )

            res = session.execute(query)
            main_dishes = res.scalars().all()
            print(main_dishes)
            return main_dishes

    @staticmethod
    def get_all():
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


# Base.metadata.create_all(sync_engine)
# object_1 = MainDishesRepositoryImpl()
# main_dish = MainDish(
#     name="test",
#     type="test",
#     price="test",
#     properties="test",
#     canteen_id=1
# )
# object_1.save(main_dish)
# print('-----------------------------')
# object_1.get_all_from_canteen(1)
# print('-----------------------')
# object_1.get(1)
