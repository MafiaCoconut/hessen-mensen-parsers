from application.interfaces.scheduler_interface import SchedulerInterface
from application.providers.canteens_provider import CanteensDependencyProvider
from application.providers.repositories_provider import RepositoriesProvider
from application.repositories.canteens_repository import CanteensRepository
from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from application.services.translation_service import TranslationService
from application.use_cases.deactivate_parsing_use_case import DeactivateParsingUseCase
from application.use_cases.delete_jobs_by_canteen_use_case import DeleteJobsByCanteenUseCase
from application.use_cases.reactivate_parsing_use_case import ReactivateParsingUseCase
from application.use_cases.set_jobs_by_canteen_use_case import SetJobsByCanteenUseCase
from application.use_cases.get_canteen_use_case import GetCanteenUseCase
from application.use_cases.get_canteens_menu_use_case import GetCanteensMenuUseCase
from application.use_cases.parse_menu_use_case import ParseCanteensMenuUseCase
from application.use_cases.save_menu_use_case import SaveMenuUseCase
from application.validators.dishes_validator import DishesValidator
from domain.entities.canteen import Canteen
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish


class CanteensService:
    def __init__(self,
                 repositories_provider: RepositoriesProvider,
                 canteens_provider: CanteensDependencyProvider,
                 translation_service: TranslationService,
                 dishes_validator: DishesValidator,
                 scheduler_interface: SchedulerInterface
                 ):
        self.repositories_provider = repositories_provider
        self.canteens_provider = canteens_provider
        self.translation_service = translation_service
        self.dishes_validator = dishes_validator

        self.get_canteen_use_case = GetCanteenUseCase(
            repositories_provider=repositories_provider,
        )
        self.get_canteens_menu_use_case = GetCanteensMenuUseCase(
            repositories_provider=repositories_provider,
            translation_service=translation_service
        )
        self.save_canteens_menu_use_case = SaveMenuUseCase(
            repositories_provider=repositories_provider,
            dishes_validator=self.dishes_validator
        )
        self.delete_jobs_by_canteen_use_case = DeleteJobsByCanteenUseCase(
            scheduler_interface=scheduler_interface
        )
        self.set_jobs_use_case = SetJobsByCanteenUseCase(
            scheduler_interface=scheduler_interface,
        )
        self.deactivate_canteen_use_case = DeactivateParsingUseCase(
            repositories_provider=repositories_provider,
            scheduler_interface=scheduler_interface,
            delete_jobs_use_case=self.delete_jobs_by_canteen_use_case
        )
        self.reactivate_canteen_use_case = ReactivateParsingUseCase(
            repositories_provider=repositories_provider,
            scheduler_interface=scheduler_interface,
            set_jobs_use_case=self.set_jobs_use_case
        )
        self.parse_menu_use_case = ParseCanteensMenuUseCase(
            repositories_provider=repositories_provider,
            canteens_provider=canteens_provider,
            save_canteens_menu_use_case=self.save_canteens_menu_use_case,
        )

    async def parse_all_canteens(self):
        return await self.parse_menu_use_case.parse_all_canteens()

    async def parse_canteen(self, canteen_id: int):
        return await self.parse_menu_use_case.parse_canteen(canteen_id=canteen_id)

    async def get_canteen_text(self, canteen_id: int) -> str:
        return await self.get_canteen_use_case.get_text(canteen_id=canteen_id)

    async def get_canteen_obj(self, canteen_id: int) -> Canteen:
        return await self.get_canteen_use_case.get_object(canteen_id=canteen_id)

    async def get_canteens_data(self, canteen_id: int) -> dict:
        """
        Функция возвращает информацию о запрашиваемой столовой и её текущих блюдах
        :param canteen_id: Id столовой в базе данных
        :return: {
            'main_dishes': list[MainDish],
            'side_dishes': side_dishes[SideDishes],
            'canteen': Canteen
        }
       """
        return await self.get_canteens_menu_use_case.execute(canteen_id=canteen_id)

    async def delele_menu(self, canteen_id: int):
        await self.delete_main_dishes(canteen_id)
        await self.delete_side_dishes(canteen_id)

    async def delete_main_dishes(self, canteen_id):
        main_dishes_repository = self.repositories_provider.get_main_dishes_repository()
        await main_dishes_repository.delete_old_dishes(canteen_id)

    async def delete_side_dishes(self, canteen_id):
        side_dishes_repository = self.repositories_provider.get_side_dishes_repository()
        await side_dishes_repository.delete_old_dishes(canteen_id)

    async def get_main_dishes_obj(self, canteen_id):
        main_dishes = await self.get_canteen_use_case.get_main_dishes_obj(canteen_id)
        return main_dishes

    async def get_side_dishes_obj(self, canteen_id):
        side_dishes = await self.get_canteen_use_case.get_side_dishes_obj(canteen_id)
        return side_dishes

    async def save_menu(self, main_dishes: list[MainDish], side_dishes: list[SideDish]):
        await self.save_canteens_menu_use_case.execute(main_dishes=main_dishes, side_dishes=side_dishes)

    async def deactivate_canteen(self, canteen_id: int):
        await self.deactivate_canteen_use_case.execute(canteen_id=canteen_id)

    async def reactivate_canteen(self, canteen_id: int):
        await self.reactivate_canteen_use_case.execute(canteen_id=canteen_id, func=self.parse_canteen)


