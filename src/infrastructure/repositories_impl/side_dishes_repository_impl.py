from application.repositories.side_dishes_repository import SideDishesRepository
from domain.entities.side_dish import SideDish


class SideDishesRepositoryImpl(SideDishesRepository):
    @staticmethod
    def get(side_dish_id: int):
        pass

    @staticmethod
    def get_all_from_canteen(side_dish_id: int):
        pass

    @staticmethod
    def get_all():
        pass

    @staticmethod
    def save(side_dish: SideDish):
        pass

