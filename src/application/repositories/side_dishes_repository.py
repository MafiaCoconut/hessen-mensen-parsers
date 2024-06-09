from abc import ABC, abstractmethod
from typing import List

from domain.entities.side_dish import SideDish


class SideDishesRepository(ABC):
    @staticmethod
    @abstractmethod
    def get(side_dish_id: int) -> SideDish:
        pass

    @staticmethod
    @abstractmethod
    def get_all_from_canteen(canteen_id: int) -> list[SideDish]:
        pass

    @staticmethod
    @abstractmethod
    def get_all() -> list[SideDish]:
        pass

    @staticmethod
    @abstractmethod
    def save(side_dish: SideDish):
        pass

    @staticmethod
    @abstractmethod
    def save_many(main_dishes: List[SideDish]):
        pass

    @staticmethod
    @abstractmethod
    def delete_old_dishes(canteen_id: int):
        pass

