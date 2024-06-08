from abc import ABC, abstractmethod

from domain.entities.side_dish import SideDish


class SideDishesRepository(ABC):
    @staticmethod
    @abstractmethod
    def get(side_dish_id: int):
        pass

    @staticmethod
    @abstractmethod
    def get_all_from_canteen(canteen_id: int):
        pass

    @staticmethod
    @abstractmethod
    def get_all():
        pass

    @staticmethod
    @abstractmethod
    def save(side_dish: SideDish):
        pass

