from application.interfaces.scheduler_interface import SchedulerInterface
from application.providers.canteens_provider import CanteensDependencyProvider
from application.repositories.canteens_repository import CanteensRepository
from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from application.services.translation_service import TranslationService
from application.use_cases.deactivate_parsing_use_case import DeactivateParsingUseCase
from application.use_cases.delete_jobs_by_canteen_use_case import DeleteJobsByCanteenUseCase
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
                 canteens_repository: CanteensRepository,
                 main_dishes_repository: MainDishesRepository,
                 side_dishes_repository: SideDishesRepository,
                 canteens_provider: CanteensDependencyProvider,
                 translation_service: TranslationService,
                 dishes_validator: DishesValidator,
                 scheduler_interface: SchedulerInterface
                 ):
        self.canteens_repository = canteens_repository
        self.main_dishes_repository = main_dishes_repository
        self.side_dishes_repository = side_dishes_repository
        self.canteens_provider = canteens_provider
        self.translation_service = translation_service
        self.dishes_validator = dishes_validator

        self.get_canteen_use_case = GetCanteenUseCase(
            canteens_repository=canteens_repository,
            main_dishes_repository=self.main_dishes_repository,
            side_dishes_repository=self.side_dishes_repository
        )
        self.get_canteens_menu_use_case = GetCanteensMenuUseCase(
            canteens_repository=canteens_repository,
            main_dishes_repository=self.main_dishes_repository,
            side_dishes_repository=self.side_dishes_repository,
            translation_service=translation_service
        )
        self.save_canteens_menu_use_case = SaveMenuUseCase(
            main_dishes_repository=self.main_dishes_repository,
            side_dishes_repository=self.side_dishes_repository,
            dishes_validator=self.dishes_validator
        )
        self.delete_jobs_by_canteen_use_case = DeleteJobsByCanteenUseCase(
            scheduler_interface=scheduler_interface
        )
        self.set_jobs_use_case = SetJobsByCanteenUseCase(
            scheduler_interface=scheduler_interface,
        )

        self.deactivate_canteen_use_case = DeactivateParsingUseCase(
            canteens_repository=canteens_repository,
            scheduler_interface=scheduler_interface,
            delete_jobs_use_case=self.delete_jobs_by_canteen_use_case
        )

    @property
    def marburg_erlenring_parser(self):
        return self.canteens_provider.get_marburg_erlenring_parser_interface()

    @property
    def marburg_lahnberge_parser(self):
        return self.canteens_provider.get_marburg_lahnberge_parser_interface()

    @property
    def marburg_bistro_parser(self):
        return self.canteens_provider.get_marburg_bistro_parser_interface()

    @property
    def marburg_cafeteria_parser(self):
        return self.canteens_provider.get_marburg_cafeteria_parser_interface()

    @property
    def marburg_mo_diner_parser(self):
        return self.canteens_provider.get_marburg_mo_diner_parser_interface()

    @property
    def giessen_thm_parser(self):
        return self.canteens_provider.get_giessen_thm_parser_interface()

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

    async def parse_canteen(self, canteen_id: int):
        await self.main_dishes_repository.delete_old_dishes(canteen_id)
        await self.side_dishes_repository.delete_old_dishes(canteen_id)

        canteen = None
        match canteen_id:
            case 1:
                canteen = self.marburg_erlenring_parser
            case 2:
                canteen = self.marburg_lahnberge_parser
            case 3:
                canteen = self.marburg_bistro_parser
            case 4:
                canteen = self.marburg_cafeteria_parser
            case 5:
                canteen = self.marburg_mo_diner_parser
            case 6:
                canteen = self.giessen_thm_parser

        parse_canteen_menu_use_case = ParseCanteensMenuUseCase(canteen)
        result = parse_canteen_menu_use_case.execute()

        await self.save_canteens_menu_use_case.execute(
            main_dishes=result['main_dishes'], side_dishes=result['side_dishes']
        )

        return result

    async def parse_all_canteens(self):
        canteens = {
            '1': "erlenring",
            '2': "lahnberge",
            '3': "bistro",
            '4': "cafeteria",
            '5': "mo_diner",
            '6': "thm",
        }

        result = {}
        for i in canteens.keys():
            result[canteens[i]] = self.parse_canteen(int(i))
        return result

    async def delele_menu(self, canteen_id: int):
        await self.delete_main_dishes(canteen_id)
        await self.delete_side_dishes(canteen_id)

    async def delete_main_dishes(self, canteen_id):
        await self.main_dishes_repository.delete_old_dishes(canteen_id)

    async def delete_side_dishes(self, canteen_id):
        await self.side_dishes_repository.delete_old_dishes(canteen_id)

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
