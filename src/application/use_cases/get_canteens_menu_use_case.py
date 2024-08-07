import logging

from application.repositories.canteens_repository import CanteensRepository
from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from application.services.translation_service import TranslationService
from datetime import datetime
from icecream import ic

from application.use_cases.errors import MenuErrorCodes
from domain.entities.canteen import Canteen


class GetCanteensMenuUseCase:
    def __init__(self,
                 canteens_repository: CanteensRepository,
                 main_dishes_repository: MainDishesRepository,
                 side_dishes_repository: SideDishesRepository,
                 translation_service: TranslationService
                 ):
        self.canteens_repository = canteens_repository
        self.main_dishes_repository = main_dishes_repository
        self.side_dishes_repository = side_dishes_repository
        self.translation_service = translation_service

    async def execute(self, canteen_id: int):
        """
        Функция берёт из репозиториев данные о запрашиваемой столовой и её текущих блюдах
        :param canteen_id: ID столовой в базе данных
        :return: :return: {
            'main_dishes': list[MainDish],
            'side_dishes': side_dishes[SideDishes],
            'canteen': Canteen
        }
        """
        main_dishes = await self.main_dishes_repository.get_all_from_canteen(canteen_id=canteen_id)
        side_dishes = await self.side_dishes_repository.get_all_from_canteen(canteen_id=canteen_id)
        canteen = await self.canteens_repository.get(canteen_id)
        result = {
            'main_dishes': main_dishes,
            'side_dishes': side_dishes,
            'canteen': canteen
        }
        return result

    # async def execute(self, canteen_id: int, locale: str, test_time=None, test_day=None) -> dict:

    #     canteen = await self.canteens_repository.get(canteen_id)
    #
    #     result = {'menu': None,
    #               'error': await self.check_menu_errors(canteen=canteen, locale=locale,
    #                                                     main_dishes=main_dishes,
    #                                                     test_time=test_time, test_day=test_day)}
    #     logging.info(result)
    #     try:
    #         menu_text = ""
    #         menu_text += await self.get_header(canteen=canteen, locale=locale, created_at=main_dishes[0].created_at)
    #         menu_text += await self.get_main_dishes_text(main_dishes=main_dishes, locale=locale)
    #         menu_text += await self.get_side_dishes_text(side_dishes=side_dishes, locale=locale)
    #
    #         print(menu_text)
    #         result['menu'] = menu_text
    #     except:
    #         pass
    #     return result
    #
    # async def check_menu_errors(self, canteen: Canteen, locale: str, main_dishes: list,
    #                             test_time: int | None, test_day: int | None):
    #     weekday = int(datetime.now().isoweekday())
    #     error_text = ""
    #     error_type = ""
    #
    #     if test_time is not None:
    #         if not (canteen.opened_time <= test_time <= canteen.closed_time):
    #             error_type = MenuErrorCodes.CANTEEN_IS_CLOSED
    #             error_text += await self.translation_service.translate(
    #                 message_id='canteens-open-time',
    #                 locale=locale,
    #                 canteen_name=canteen.name)
    #             error_text += '\n' + canteen.description
    #
    #         elif test_day is not None:
    #             if not (1 <= test_day <= 5):
    #                 error_type = MenuErrorCodes.CANTEEN_IS_CLOSED
    #                 error_text += await self.translation_service.translate(
    #                     message_id='canteens-open-time',
    #                     locale=locale,
    #                     canteen_name=canteen.name)
    #                 error_text += '\n' + canteen.description
    #
    #     elif not (canteen.opened_time <= datetime.now().hour * 60 + datetime.now().minute <= canteen.closed_time) or \
    #             not (1 <= weekday <= 5):
    #         error_type = MenuErrorCodes.CANTEEN_IS_CLOSED
    #         error_text += await self.translation_service.translate(
    #             message_id='canteens-open-time',
    #             locale=locale,
    #             canteen_name=canteen.name)
    #         error_text += '\n' + canteen.description
    #
    #     if not main_dishes:
    #         error_type = MenuErrorCodes.MENU_IS_NONE
    #         error_text += await self.translation_service.translate(
    #             message_id='no-menu-for-today',
    #             locale=locale,
    #             canteen_name=canteen.name)
    #         error_text += '\n\n'
    #         error_text += await self.translation_service.translate(
    #             message_id='canteens-open-time',
    #             locale=locale,
    #             canteen_name=canteen.name)
    #         error_text += '\n' + canteen.description
    #
    #     return {'type': error_type, 'text': error_text}
    #
    # async def get_header(self, created_at: datetime, locale: str, canteen: Canteen):
    #     time_parser = created_at
    #     day = f"{str(time_parser.day).zfill(2)}.{str(time_parser.month).zfill(2)}"
    #     time_last_parser = f"{str(time_parser.hour).zfill(2)}:{str(time_parser.minute).zfill(2)}"
    #
    #     text = await self.translation_service.translate(
    #         message_id='dishes-header',
    #         locale=locale,
    #         canteen_name=canteen.name,
    #         day=day,
    #         time_last_parser=time_last_parser
    #     ) + '\n\n\n'
    #     return text
    #
    # async def get_main_dishes_text(self, main_dishes: list, locale: str):
    #
    #     text = await self.translation_service.translate(
    #         message_id='main-dishes-title',
    #         locale=locale) + '\n'
    #
    #     last_type_of_dish = ""
    #     for dish in main_dishes:
    #         if dish.name == "" or dish.name is None or dish.name == " ":
    #             continue
    #
    #         dish_text = ""
    #         if dish.type != last_type_of_dish:
    #             dish_text += f"<u>{dish.type}</u>\n"
    #             last_type_of_dish = dish.type
    #
    #         dish_text += f"* {dish.name}\n"
    #         if dish.properties != '-':
    #             dish_text += f"- {dish.properties}\n"
    #         dish_text += f"= {dish.price}\n\n"
    #
    #         text += dish_text
    #
    #     return text
    #
    # async def get_side_dishes_text(self, side_dishes: list, locale: str):
    #     if not side_dishes:
    #         return ""
    #
    #     text = await self.translation_service.translate(
    #         message_id='beilagen-title',
    #         locale=locale) + '\n'
    #
    #     for side_dish in side_dishes:
    #         if side_dish.name == "" or side_dish.name is None or side_dish.name == " ":
    #             continue
    #         else:
    #             # name_dish = side_dish[1]
    #             # properties = side_dish[2]
    #             side_dish_text = f"* {side_dish.name}\n"
    #             if side_dish.properties != '-':
    #                 side_dish_text += f"- {side_dish.properties}\n"
    #             if side_dish.price != '-':
    #                 side_dish_text += f"= {side_dish.price}\n"
    #
    #             text += side_dish_text + '\n'
    #     return text


# if __name__ == "__main__":
#     obj = GetCanteensMenuUseCase()
"""

{
    'menu': 'text',
    'error': 
    {
        'type': 'canteen-closed',
        'text': 'text'
    }
}
Меню столовой Mensa Erlenring
Время последнего обновления: 07.05 - 11:45


Empore Fleisch
* Lahnbergburger mit Pommes frites  
= 4,65 €

Menü 1
* Kottbülar mit Preiselbeerrahm  
= 4,35 €

Menü 2
* Paprika-Zucchinipfanne mit Bulgur und Soja-Streifen, dazu Tomaten-Chili-Dip Tomaten-Chili-Dip  
- vegan
= 4,05 €

Tagesgericht
* Käsespätzle mit gebräunten Zwiebeln , dazu Salat  
= 3,35 €


Дополнительные блюда
* Currysuppe mit Bohnen (16, 24, 25)

* Karottengemüse (1)

* Pommes frites Reis (1) Salzkartoffeln (1)

* verschiedene Frucht Quark / Joghurt (1, 22) Sojajoghur mit Brombeeren (3, 21)  Wackelpudding Zitrone (12, 45) Mandelpudding (22, 23)

* Weißkrautsalat (3, 25, 27) Karottensalat (3, 27) Paprika-Gurkensalat (3, 25, 27) Italienisches Dressing (3, 24, 25, 27)
"""
