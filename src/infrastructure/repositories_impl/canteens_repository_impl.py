from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

from application.repositories.canteens_repository import CanteensRepository
from domain.entities.canteen import Canteen
from infrastructure.db.base import get_db


class CanteensRepositoryImpl(CanteensRepository):
    def __init__(self, db_connection: Session):
        self.db_connection = db_connection

    def get_all(self) -> List[Canteen]:
        pass

    def get(self, canteen_id: int) -> Canteen:
        return self.db_connection.query(Canteen).filter(Canteen.canteen_id == canteen_id).first()

    def save(canteen: Canteen, db: Session = Depends(get_db)) -> None:
        pass