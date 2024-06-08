from application.repositories.main_dishes_repository import MainDishesRepository
from domain.entities.main_dish import MainDish


class MainDishesRepositoryImpl(MainDishesRepository):
    @staticmethod
    def get(main_dish_id: int):
        pass

    @staticmethod
    def get_all_from_canteen(main_dish_id: int):
        pass

    @staticmethod
    def get_all():
        pass

    @staticmethod
    def save(main_dish: MainDish):
        pass

