from abc import ABC, abstractmethod

from application.repositories.canteens_repository import CanteensRepository
from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from infrastructure.config.repositories_config import get_side_dishes_repository, get_main_dishes_repository, \
    get_canteens_repository


class RepositoriesProvider(ABC):
    @abstractmethod
    def get_canteens_repository(self) -> CanteensRepository:
        pass

    @abstractmethod
    def get_main_dishes_repository(self) -> MainDishesRepository:
        pass

    @abstractmethod
    def get_side_dishes_repository(self) -> SideDishesRepository:
        pass
