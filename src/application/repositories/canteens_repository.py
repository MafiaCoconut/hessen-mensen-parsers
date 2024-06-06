from abc import abstractmethod, ABC
from typing import List
from sqlalchemy.orm import Session

from domain.entities.canteen import Canteen


class CanteensRepository(ABC):

    @abstractmethod
    def get_all(self, db: Session) -> List[Canteen]:
        pass

    @abstractmethod
    def get(self, canteen_id: int, db: Session) -> Canteen:
        pass

    @abstractmethod
    def save(self, canteen: Canteen, db: Session) -> None:
        pass
