from typing import List

from src.domain.entities.main_dish import MainDish
from src.domain.entities.side_dish import SideDish


class SaveMenuUseCase:
    def __init__(self, main_dishes_repository, side_dishes_repository):
        self.main_dish_repository = main_dishes_repository
        self.side_dish_repository = side_dishes_repository

    def execute(self, main_dishes: List[MainDish], side_dishes: List[SideDish]):
        self.main_dish_repository.save_many(main_dishes)
        self.side_dish_repository.save_meny(side_dishes)


