from application.providers.canteens_provider import CanteensDependencyProvider
from application.repositories.canteens_repository import CanteensRepository
from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from application.use_cases.get_canteen_use_case import GetCanteenUseCase
from application.use_cases.get_canteens_menu_use_case import GetCanteensMenuUseCase


class CanteenService:
    def __init__(self,
                 canteens_repository: CanteensRepository,
                 main_dishes_repository: MainDishesRepository,
                 side_dishes_repository: SideDishesRepository,
                 canteens_provider: CanteensDependencyProvider,
                 ):
        self.canteens_repository = canteens_repository
        self.main_dishes_repository = main_dishes_repository
        self.side_dishes_repository = side_dishes_repository
        self.canteens_provider = canteens_provider

        self.get_canteen_use_case = GetCanteenUseCase(canteens_repository=canteens_repository)
        self.get_canteens_menu_use_case = GetCanteensMenuUseCase(
            main_dishes_repository=self.main_dishes_repository,
            side_dishes_repository=self.side_dishes_repository
        )

    def get_canteen(self, canteen_id: int):
        return self.get_canteen_use_case.get(canteen_id)

    def get_menu(self, canteen_id: int):
        return self.get_canteens_menu_use_case.execute(canteen_id)

    def parse_canteen(self, canteen_id: int):
        pass

    def parse_all_canteens(self):
        pass
