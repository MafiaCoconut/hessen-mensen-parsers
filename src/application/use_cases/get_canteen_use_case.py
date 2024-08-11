from application.repositories.canteens_repository import CanteensRepository
from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from domain.entities.canteen import Canteen
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish


class GetCanteenUseCase:
    def __init__(self,
                 canteens_repository: CanteensRepository,
                 main_dishes_repository: MainDishesRepository,
                 side_dishes_repository: SideDishesRepository,
                 ):
        self.canteens_repository = canteens_repository
        self.main_dishes_repository = main_dishes_repository
        self.side_dishes_repository = side_dishes_repository

    async def get_text(self, canteen_id: int) -> str:
        canteen = await self.canteens_repository.get(canteen_id=canteen_id)
        if canteen is None:
            raise ValueError(f"Canteen with ID {canteen_id} does not exist.")

        text = "ID:{}\nНазвание: {}\n".format(
            canteen.canteen_id,
            canteen.name,
        )
        return text

    async def get_object(self, canteen_id: int) -> Canteen:
        canteen = await self.canteens_repository.get(canteen_id=canteen_id)
        if canteen is None:
            raise ValueError(f"Canteen with ID {canteen_id} does not exist.")

        return canteen

    async def get_main_dishes_obj(self, canteen_id: int) -> list[MainDish]:
        main_dishes = await self.main_dishes_repository.get_all_from_canteen(canteen_id=canteen_id)
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

    async def get_side_dishes_obj(self, canteen_id: int) -> list[SideDish]:
        side_dishes = await self.side_dishes_repository.get_all_from_canteen(canteen_id=canteen_id)
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


