from typing import List

from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish


class SaveMenuUseCase:
    def __init__(self,
                 main_dishes_repository: MainDishesRepository,
                 side_dishes_repository: SideDishesRepository
                 ):
        self.main_dish_repository = main_dishes_repository
        self.side_dish_repository = side_dishes_repository

    def execute(self, main_dishes: List[MainDish], side_dishes: List[SideDish]):
        self.main_dish_repository.save_many(main_dishes)
        self.side_dish_repository.save_many(side_dishes)


