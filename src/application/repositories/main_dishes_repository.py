from abc import ABC, abstractmethod
from typing import List

from domain.entities.main_dish import MainDish


class MainDishesRepository(ABC):
    @staticmethod
    @abstractmethod
    async def get(main_dish_id: int) -> MainDish:
        pass

    @staticmethod
    @abstractmethod
    async def get_all_from_canteen(canteen_id: int) -> List[MainDish]:
        pass

    @staticmethod
    @abstractmethod
    async def get_all() -> List[MainDish]:
        pass

    @staticmethod
    @abstractmethod
    async def save(main_dish: MainDish):
        pass

    @staticmethod
    @abstractmethod
    async def save_many(main_dishes: List[MainDish]):
        pass


    @staticmethod
    @abstractmethod
    async def delete_old_dishes(canteen_id: int):
        pass

