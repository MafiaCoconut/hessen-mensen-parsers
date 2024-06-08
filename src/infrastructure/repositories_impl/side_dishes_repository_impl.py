from application.repositories.side_dishes_repository import SideDishesRepository
from domain.entities.side_dish import SideDish
from infrastructure.db.base import sync_engine, session_factory, Base
from infrastructure.db.models.side_dishes_orm import SideDishesOrm
from sqlalchemy import select

class SideDishesRepositoryImpl(SideDishesRepository):
    @staticmethod
    def get(side_dish_id: int):
        with session_factory() as session:
            side_dish = session.query(SideDishesOrm, side_dish_id).first()
            return side_dish

    @staticmethod
    def get_all_from_canteen(canteen_id: int):
        with session_factory() as session:
            query = (
                select(SideDishesOrm)
                .filter(SideDishesOrm.canteen_id == canteen_id)
            )
            res = session.execute(query)
            side_dishes = res.scalars().all()
            return side_dishes

    @staticmethod
    def get_all():
        with session_factory() as session:
            query = select(SideDishesOrm)
            res = session.execute(query)
            side_dishes = res.scalars().all()
            return side_dishes

    @staticmethod
    def save(side_dish: SideDish):
        with session_factory() as session:
            side_dish = SideDish(
                name=side_dish.name,
                type=side_dish.type,
                price=side_dish.price,
                properties=side_dish.properties,
                canteen_id=side_dish.canteen_id
            )
            session.add(side_dish)
            session.commit()

