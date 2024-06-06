from abc import abstractmethod
from typing import List

from domain.entities.canteen import Canteen


class CanteensRepository:
    @staticmethod
    @abstractmethod
    def get_all() -> List[Canteen]:
        pass

    @staticmethod
    @abstractmethod
    def get() -> Canteen:
        pass

    @staticmethod
    @abstractmethod
    def save() -> None:
        pass