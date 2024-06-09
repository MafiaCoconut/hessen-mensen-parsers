from application.providers.canteens_provider import CanteensDependencyProvider
from application.repositories.canteens_repository import CanteensRepository
from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from application.services.translation_service import TranslationService
from application.use_cases.get_canteen_use_case import GetCanteenUseCase
from application.use_cases.get_canteens_menu_use_case import GetCanteensMenuUseCase
from application.use_cases.parse_menu_use_case import ParseCanteensMenuUseCase
from application.use_cases.save_menu_use_case import SaveMenuUseCase


class CanteenService:
    def __init__(self,
                 canteens_repository: CanteensRepository,
                 main_dishes_repository: MainDishesRepository,
                 side_dishes_repository: SideDishesRepository,
                 canteens_provider: CanteensDependencyProvider,
                 translation_service: TranslationService
                 ):
        self.canteens_repository = canteens_repository
        self.main_dishes_repository = main_dishes_repository
        self.side_dishes_repository = side_dishes_repository
        self.canteens_provider = canteens_provider
        self.translation_service = translation_service

        self.get_canteen_use_case = GetCanteenUseCase(canteens_repository=canteens_repository)
        self.get_canteens_menu_use_case = GetCanteensMenuUseCase(
            canteens_repository=canteens_repository,
            main_dishes_repository=self.main_dishes_repository,
            side_dishes_repository=self.side_dishes_repository,
            translation_service=translation_service
        )
        self.save_canteens_menu_use_case = SaveMenuUseCase(
            main_dishes_repository=self.main_dishes_repository,
            side_dishes_repository=self.side_dishes_repository
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

    def get_canteen(self, canteen_id: int):
        return self.get_canteen_use_case.get(canteen_id)

    def get_menu(self, canteen_id: int, locale: str):
        return self.get_canteens_menu_use_case.execute(canteen_id, locale=locale)

    def parse_canteen(self, canteen_id: int):
        self.main_dishes_repository.delete_old_dishes(canteen_id)
        self.side_dishes_repository.delete_old_dishes(canteen_id)

        canteen = None
        print(canteen_id)
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

        self.save_canteens_menu_use_case.execute(
            main_dishes=result['main_dishes'], side_dishes=result['side_dishes']
        )

        return result

    def parse_all_canteens(self):
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
        print(result)
        return result




