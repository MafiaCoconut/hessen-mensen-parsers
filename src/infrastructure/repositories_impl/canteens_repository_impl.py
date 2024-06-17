from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete, text
from application.repositories.canteens_repository import CanteensRepository
from domain.entities.canteen import Canteen
from infrastructure.db.base import sync_engine, session_factory
from infrastructure.db.models.canteens_orm import CanteensOrm
from icecream import ic


class CanteensRepositoryImpl(CanteensRepository):
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

    def save(self, canteen: Canteen = None) -> None:
        with session_factory() as session:

            canteen_orm = CanteensOrm(
                canteen_id=canteen.canteen_id,
                name=canteen.name,
                description=canteen.description,
                created_at=canteen.created_at
            )
            session.add(canteen_orm)
            session.commit()

    def delete_all(self) -> None:
        with session_factory() as session:
            session.execute(delete(CanteensOrm))
            session.execute(text(f"ALTER SEQUENCE {CanteensOrm.__tablename__}_canteen_id_seq RESTART WITH 1;"))

            session.commit()


    def delete(self, canteen_id: int) -> None:
        with session_factory() as session:
            query = (
                delete(CanteensOrm)
                .filter(CanteensOrm.canteen_id == int(canteen_id))
            )
            session.execute(query)
            session.commit()


