from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

from application.repositories.canteens_repository import CanteensRepository
from domain.entities.canteen import Canteen
from infrastructure.db.base import get_db


class CanteensRepositoryImpl(CanteensRepository):
    @staticmethod
    def get_all(db: Session = Depends(get_db)) -> List[Canteen]:
        pass

    @staticmethod
    def get(canteen_id: int, db=Depends(get_db)) -> Canteen:
        return db.query(Canteen).filter(Canteen.canteen_id == canteen_id).first()

    @staticmethod
    def save(canteen: Canteen, db: Session = Depends(get_db)) -> None:
        pass