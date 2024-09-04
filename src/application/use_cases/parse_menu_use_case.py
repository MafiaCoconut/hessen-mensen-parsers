from datetime import datetime

from application.interfaces.parser_interface import CanteenParserInterface
from application.providers.canteens_provider import CanteensDependencyProvider
from application.providers.repositories_provider import RepositoriesProvider
from application.repositories.canteens_repository import CanteensRepository
from application.use_cases.save_menu_use_case import SaveMenuUseCase
from infrastructure.config.logs_config import log_decorator


class ParseCanteensMenuUseCase:
    def __init__(
            self,
            canteens_provider: CanteensDependencyProvider,
            repositories_provider: RepositoriesProvider,
            save_canteens_menu_use_case: SaveMenuUseCase,
    ):
        self.canteens_provider = canteens_provider
        self.repositories_provider = repositories_provider
        self.save_canteens_menu_use_case = save_canteens_menu_use_case

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

    @log_decorator(print_args=False)
    async def parse_canteen(self, canteen_id: int):
        canteens_repository = self.repositories_provider.get_canteens_repository()
        main_dishes_repository = self.repositories_provider.get_main_dishes_repository()
        side_dishes_repository = self.repositories_provider.get_side_dishes_repository()

        await main_dishes_repository.delete_old_dishes(canteen_id=canteen_id)
        await side_dishes_repository.delete_old_dishes(canteen_id=canteen_id)

        result = None
        if await self.check_is_active(canteen_id=canteen_id, canteens_repository=canteens_repository):
            match canteen_id:
                case 1:
                    if await self.check_is_active(canteen_id=canteen_id, canteens_repository=canteens_repository):
                        result = self.marburg_erlenring_parser.parse()
                case 2:
                    if await self.check_is_active(canteen_id=canteen_id, canteens_repository=canteens_repository):
                        result = self.marburg_lahnberge_parser.parse()
                case 3:
                    if await self.check_is_active(canteen_id=canteen_id, canteens_repository=canteens_repository):
                        result = self.marburg_bistro_parser.parse()
                case 4:
                    if await self.check_is_active(canteen_id=canteen_id, canteens_repository=canteens_repository):
                        result = self.marburg_cafeteria_parser.parse()
                case 5:
                    if await self.check_is_active(canteen_id=canteen_id, canteens_repository=canteens_repository):
                        result = self.marburg_mo_diner_parser.parse()
                case 6:
                        result = self.giessen_thm_parser.parse()

            await canteens_repository.update_last_parsing_time(canteen_id=canteen_id, new_last_parsing_time=datetime.now())
            await self.save_canteens_menu_use_case.execute(
                main_dishes=result['main_dishes'], side_dishes=result['side_dishes']
            )
            return result

        else:
            return {"text": "Canteen is deactivated"}

    @log_decorator(print_args=False, print_kwargs=False)
    async def parse_all_canteens(self):
        canteens = {
            1: "erlenring",
            2: "lahnberge",
            3: "bistro",
            # '4': "cafeteria",
            # '5': "mo_diner",
            6: "thm",
        }

        result = {}
        for i in canteens.keys():
            result[canteens[i]] = await self.parse_canteen(canteen_id=i)
        return result

    @log_decorator(print_args=False)
    async def check_is_active(self, canteen_id: int, canteens_repository: CanteensRepository):
        canteen = await canteens_repository.get(canteen_id=canteen_id)
        if canteen.status == "active":
            return True
        return False


