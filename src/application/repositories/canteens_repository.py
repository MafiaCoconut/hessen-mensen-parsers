from abc import abstractmethod, ABC
from typing import List
from sqlalchemy.orm import Session

from domain.entities.canteen import Canteen


class CanteensRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Canteen]:
        pass

    @abstractmethod
    def get(self, canteen_id: int) -> Canteen:
        pass

    @abstractmethod
    def save(self, canteen: Canteen) -> None:
        pass

    @abstractmethod
    def delete_all(self) -> None:
        pass

    @abstractmethod
    def delete(self, canteen_id: int) -> None:
        pass

