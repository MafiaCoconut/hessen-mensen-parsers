from application.providers.repositories_provider import RepositoriesProvider
from application.repositories.canteens_repository import CanteensRepository
from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from infrastructure.config.repositories_config import get_canteens_repository, get_main_dishes_repository, get_side_dishes_repository


class RepositoriesProviderImpl(RepositoriesProvider):
    def get_canteens_repository(self) -> CanteensRepository:
        return get_canteens_repository()

    def get_main_dishes_repository(self) -> MainDishesRepository:
        return get_main_dishes_repository()

    def get_side_dishes_repository(self) -> SideDishesRepository:
        return get_side_dishes_repository()
