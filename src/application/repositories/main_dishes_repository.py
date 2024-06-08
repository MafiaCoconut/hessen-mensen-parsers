from abc import ABC, abstractmethod
from typing import List

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

    @staticmethod
    @abstractmethod
    def save_many(main_dishes: List[MainDish]):
        pass


    @staticmethod
    @abstractmethod
    def delete_old_dishes(canteen_id: int):
        pass

