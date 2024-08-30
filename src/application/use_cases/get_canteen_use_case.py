from application.providers.repositories_provider import RepositoriesProvider
from application.repositories.canteens_repository import CanteensRepository
from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from domain.entities.canteen import Canteen
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish
from infrastructure.config.logs_config import log_decorator


class GetCanteenUseCase:
    def __init__(self,
                 repositories_provider: RepositoriesProvider
                 ):
        self.repositories_provider = repositories_provider

    @log_decorator(print_args=False)
    async def get_text(self, canteen_id: int) -> str:
        canteens_repository = self.repositories_provider.get_canteens_repository()

        canteen = await canteens_repository.get(canteen_id=canteen_id)
        if canteen is None:
            raise ValueError(f"Canteen with ID {canteen_id} does not exist.")

        text = "ID:{}\nНазвание: {}\n".format(
            canteen.canteen_id,
            canteen.name,
        )
        return text

    @log_decorator(print_args=False)
    async def get_object(self, canteen_id: int) -> Canteen:
        canteens_repository = self.repositories_provider.get_canteens_repository()

        canteen = await canteens_repository.get(canteen_id=canteen_id)
        if canteen is None:
            raise ValueError(f"Canteen with ID {canteen_id} does not exist.")

        return canteen

    @log_decorator(print_args=False)
    async def get_main_dishes_obj(self, canteen_id: int) -> list[MainDish]:
        main_dishes_repository = self.repositories_provider.get_main_dishes_repository()
        main_dishes = await main_dishes_repository.get_all_from_canteen(canteen_id=canteen_id)
        new_main_dishes = []
        for i, main_dish in enumerate(main_dishes):
            new_main_dishes.append(
                MainDish(
                    name=main_dish.name,
                    type=main_dish.type,
                    price=main_dish.price,
                    properties=main_dish.properties,
                    canteen_id=main_dish.canteen_id,
                )
            )
        return new_main_dishes

    @log_decorator(print_args=False)
    async def get_side_dishes_obj(self, canteen_id: int) -> list[SideDish]:
        side_dishes_repository = self.repositories_provider.get_side_dishes_repository()
        side_dishes = await side_dishes_repository.get_all_from_canteen(canteen_id=canteen_id)
        new_side_dishes = []
        for i, side_dish in enumerate(side_dishes):
            new_side_dishes.append(
                SideDish(
                    name=side_dish.name,
                    type=side_dish.type,
                    price=side_dish.price,
                    properties=side_dish.properties,
                    canteen_id=side_dish.canteen_id,
                )
            )
        return new_side_dishes


