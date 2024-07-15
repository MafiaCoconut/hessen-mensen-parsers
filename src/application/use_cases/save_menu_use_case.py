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
        if all(dish.canteen_id == main_dishes[0].canteen_id for dish in main_dishes) if main_dishes else True:
            self.main_dish_repository.save_many(main_dishes)
        else:
            ValueError("Переданы предметы main_dishes из разных столовых")

        if all(dish.canteen_id == side_dishes[0].canteen_id for dish in side_dishes) if side_dishes else True:
            self.side_dish_repository.save_many(side_dishes)
        else:
            ValueError("Переданы предметы side_dishes из разных столовых")

