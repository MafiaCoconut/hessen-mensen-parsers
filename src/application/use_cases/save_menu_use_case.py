from typing import List

from application.providers.repositories_provider import RepositoriesProvider
from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from application.validators.dishes_validator import DishesValidator
from domain.entities.canteen import Canteen
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish
from infrastructure.config.logs_config import log_decorator


class SaveMenuUseCase:
    def __init__(self,
                 repositories_provider: RepositoriesProvider,
                 dishes_validator: DishesValidator,
                 ):
        self.repositories_provider = repositories_provider
        self.dishes_validator = dishes_validator

    @log_decorator(print_args=False, print_kwargs=False)
    async def execute(self, main_dishes: List[MainDish], side_dishes: List[SideDish]):
        if all(dish.canteen_id == main_dishes[0].canteen_id for dish in main_dishes) if main_dishes else True:
            await self.check_on_none_values_main_dishes(main_dishes=main_dishes)
        else:
            raise ValueError("Переданы предметы main_dishes из разных столовых")

        if all(dish.canteen_id == side_dishes[0].canteen_id for dish in side_dishes) if side_dishes else True:
            await self.check_on_none_values_side_dishes(side_dishes=side_dishes)
        else:
            raise ValueError("Переданы предметы side_dishes из разных столовых")

    @log_decorator(print_args=False, print_kwargs=False)
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
                main_dish_repository = self.repositories_provider.get_main_dishes_repository()
                await main_dish_repository.save(main_dish)
            else:
                continue

    @log_decorator(print_args=False, print_kwargs=False)
    async def check_on_none_values_side_dishes(self, side_dishes: List[SideDish]):
        for side_dish in side_dishes:
            flag = True
            while True:
                # print(side_dish)
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
                side_dish_repository = self.repositories_provider.get_side_dishes_repository()
                await side_dish_repository.save(side_dish)
            else:
                continue





