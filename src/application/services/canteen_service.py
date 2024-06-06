from application.repositories.canteens_repository import CanteensRepository
from application.use_cases.get_canteen_use_case import GetCanteenUseCase


class CanteenService:
    def __init__(self, canteens_repository: CanteensRepository):
        self.canteens_repository = canteens_repository
        self.canteen_name = canteen_name
        self.get_canteen_use_case = GetCanteenUseCase(canteens_repository=canteens_repository)

    def get(self):
        return self.get_canteen_use_case.execute()
