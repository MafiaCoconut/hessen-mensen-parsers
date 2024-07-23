from typing import List

from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from application.validators.dishes_validator import DishesValidator
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish


class SaveMenuUseCase:
    def __init__(self,
                 main_dishes_repository: MainDishesRepository,
                 side_dishes_repository: SideDishesRepository,
                 dishes_validator: DishesValidator,
                 ):
        self.main_dish_repository = main_dishes_repository
        self.side_dish_repository = side_dishes_repository
        self.dishes_validator = dishes_validator

    async def execute(self, main_dishes: List[MainDish], side_dishes: List[SideDish]):
        if all(dish.canteen_id == main_dishes[0].canteen_id for dish in main_dishes) if main_dishes else True:
            await self.check_on_none_values_main_dishes(main_dishes=main_dishes)
            # self.main_dish_repository.save_many(main_dishes)
        else:
            raise ValueError("Переданы предметы main_dishes из разных столовых")

        if all(dish.canteen_id == side_dishes[0].canteen_id for dish in side_dishes) if side_dishes else True:
            # self.side_dish_repository.save_many(side_dishes)
            await self.check_on_none_values_side_dishes(side_dishes=side_dishes)
        else:
            raise ValueError("Переданы предметы side_dishes из разных столовых")

    async def check_on_none_values_main_dishes(self, main_dishes: List[MainDish]):
        for main_dish in main_dishes:
            flag = True
            while True:
                try:
                    self.dishes_validator.main_dish(main_dish)
                except Exception as e:

                    match e:
                        case "name":
                            flag = False
                            break
                        case "type":
                            flag = False
                            break
                        case "canteen_id":
                            flag = False
                            break
                        case "price":
                            main_dish.price = "-"
                        case "properties":
                            main_dish.properties = "-"
                else:
                    break

            if flag:
                await self.main_dish_repository.save(main_dish)
            else:
                continue

    async def check_on_none_values_side_dishes(self, side_dishes: List[SideDish]):
        for side_dish in side_dishes:
            flag = True
            while True:
                print(side_dish)
                try:
                    self.dishes_validator.side_dish(side_dish)

                except Exception as e:
                    match e:
                        case "name":
                            flag = False
                            break
                        case "type":
                            flag = False
                            break
                        case "canteen_id":
                            flag = False
                            break
                        case "price":
                            side_dish.price = "-"
                        case "properties":
                            side_dish.properties = "-"
                else:
                    break

            if flag:
                await self.side_dish_repository.save(side_dish)
            else:
                continue





