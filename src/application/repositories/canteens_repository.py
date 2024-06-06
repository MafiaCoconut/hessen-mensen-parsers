from abc import abstractmethod
from typing import List
from sqlalchemy.orm import Session

from domain.entities.canteen import Canteen


class CanteensRepository:
    @staticmethod
    @abstractmethod
    def get_all(db: Session) -> List[Canteen]:
        pass

    @staticmethod
    @abstractmethod
    def get(canteen_id: int, db: Session) -> Canteen:
        pass

    @staticmethod
    @abstractmethod
    def save(canteen: Canteen, db: Session) -> None:
        pass
