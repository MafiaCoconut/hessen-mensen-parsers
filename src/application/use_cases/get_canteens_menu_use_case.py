from application.repositories.canteens_repository import CanteensRepository
from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from application.services.translation_service import TranslationService


class GetCanteensMenuUseCase:
    def __init__(self,
                 main_dishes_repository: MainDishesRepository,
                 side_dishes_repository: SideDishesRepository,
                 translation_service: TranslationService
                 ):
        self.main_dishes_repository = main_dishes_repository
        self.side_dishes_repository = side_dishes_repository
        self.translation_service = translation_service

    def execute(self, canteen_id):
        main_dishes = self.main_dishes_repository.get_all_from_canteen(canteen_id=canteen_id)
        side_dishes = self.side_dishes_repository.get_all_from_canteen(canteen_id=canteen_id)

        print(main_dishes)
        print(side_dishes)
        # TODO  добавить красивый вывод текста через форматирование и translation_service
        # return {"main_dishes": main_dishes, "side_dishes": side_dishes}