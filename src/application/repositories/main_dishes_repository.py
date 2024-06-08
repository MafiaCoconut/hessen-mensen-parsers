from abc import ABC, abstractmethod

from domain.entities.main_dish import MainDish


class MainDishesRepository(ABC):
    @staticmethod
    @abstractmethod
    def get(main_dish_id: int):
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
    def save(main_dish: MainDish):
        pass

