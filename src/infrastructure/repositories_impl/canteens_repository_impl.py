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
            # ic(session)
            # print('---------------------')
            query = select(CanteensOrm)
            # ic(query)
            result = session.execute(query)
            canteens = result.scalars().all()
            ic(canteens)

            # querry = select()

    def get(self, canteen_id: int) -> Canteen:
        pass
        # return self.db_connection.query(Canteen).filter(Canteen.canteen_id == canteen_id).first()

    def update(self, canteen_id: int, canteen_name: str):
        with session_factory() as session:
            canteen = session.get(CanteensOrm, canteen_id)
            canteen.name = canteen_name
            session.commit()


    def save(self, canteen: Canteen = None) -> None:
        pass
        # with sync_engine.connect() as conn:
        #     stmt = insert(canteens_table).values(
        #         {
        #             "name": "тестовая столовая"
        #         }
        #     )
        #     conn.execute(stmt)
        #     conn.commit()


canteen_repository = CanteensRepositoryImpl()
# canteen_repository.save()
# canteen_repository.get_all()
canteen_repository.update(canteen_id=7, canteen_name='тестовая столовая_1')
