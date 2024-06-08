from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update
from application.repositories.canteens_repository import CanteensRepository
from domain.entities.canteen import Canteen
from infrastructure.db.base import sync_engine, session_factory
from infrastructure.db.models.canteens_orm import CanteensOrm
from icecream import ic

class CanteensRepositoryImpl(CanteensRepository):
    # def __init__(self, db_connection: Session):
    #     self.db_connection = db_connection

    def get_all(self) -> List[Canteen]:
        with session_factory() as session:
            query = select(CanteensOrm)
            result = session.execute(query)
            canteens = result.scalars().all()

            return canteens

    def get(self, canteen_id: int) -> Canteen:
        with session_factory() as session:
            canteen = session.get(CanteensOrm, canteen_id)

            return canteen

    # def update(self, canteen_id: int, canteen_name: str):
    #     with session_factory() as session:
    #         canteen = session.get(CanteensOrm, canteen_id)
    #         canteen.name = canteen_name
    #         session.commit()


    def save(self, canteen: Canteen = None) -> None:
        with session_factory() as session:

            canteen_orm = CanteensOrm(
                canteen_id=canteen.canteen_id,
                name=canteen.name,
                created_at=canteen.created_at
            )
            session.add(canteen_orm)
            session.commit()



canteen_repository = CanteensRepositoryImpl()
canteen = Canteen(canteen_id=8, name="dsfdsffs")
canteen_repository.save(canteen=canteen)
# canteen_repository.get_all()
# canteen_repository.get(canteen_id=1)
# canteen_repository.update(canteen_id=7, canteen_name='тестовая столовая_1')
