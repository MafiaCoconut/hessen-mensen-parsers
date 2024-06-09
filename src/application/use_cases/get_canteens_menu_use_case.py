from application.repositories.canteens_repository import CanteensRepository
from application.repositories.main_dishes_repository import MainDishesRepository
from application.repositories.side_dishes_repository import SideDishesRepository
from application.services.translation_service import TranslationService
from datetime import datetime
from icecream import ic

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

    def execute(self, canteen_id: int, locale: str):
        main_dishes = self.main_dishes_repository.get_all_from_canteen(canteen_id=canteen_id)
        side_dishes = self.side_dishes_repository.get_all_from_canteen(canteen_id=canteen_id)
        canteen = self.canteens_repository.get(canteen_id)

        print(main_dishes)
        print(side_dishes)
        # TODO  добавить красивый вывод текста через форматирование и translation_service
        # return {"main_dishes": main_dishes, "side_dishes": side_dishes}
        result = {'menu': None,
                  'error': self.check_menu_errors(canteen=canteen, locale=locale, main_dishes=main_dishes)}
        ic(result)

        menu_text = ""
        menu_text += self.get_main_dishes_text(canteen=canteen, main_dishes=main_dishes, locale=locale)
        print(menu_text)


    def check_menu_errors(self, canteen: Canteen, locale: str, main_dishes: list):
        weekday = int(datetime.now().isoweekday())
        error_text = ""
        error_type = ""

        if not (canteen.opened_time <= datetime.now().hour * 60 + datetime.now().minute <= canteen.closed_time) or \
           not (1 <= weekday <= 5):
            error_type = 'canteen-closed'
            error_text += self.translation_service.translate(
                message_id='canteens-open-time',
                locale=locale,
                canteen_name=canteen.name)
            error_text += '\n' + canteen.description

        elif not main_dishes:
            error_type = 'menu-is-None'
            error_text += self.translation_service.translate(
                message_id='no-menu-for-today',
                locale=locale,
                canteen_name=canteen.name)
            error_text += '\n\n'
            error_text += self.translation_service.translate(
                message_id='canteens-open-time',
                locale=locale,
                canteen_name=canteen.name)
            error_text += '\n' + canteen.description

        return {'type': error_type, 'text': error_text}

    def get_main_dishes_text(self, main_dishes: list, locale: str, canteen: Canteen):
        text = ""
        time_parser = main_dishes[0].created_at
        ic(time_parser)
        day = f"{str(time_parser.day).zfill(2)}.{str(time_parser.month).zfill(2)}"
        time_last_parser = f"{str(time_parser.hour).zfill(2)}:{str(time_parser.minute).zfill(2)}"

        text += self.translation_service.translate(
            message_id='dishes-header',
            locale=locale,
            canteen_name=canteen.name,
            day=day,
            time_last_parser=time_last_parser
        ) + '\n\n\n'
        # --------------------------------------
        last_type_of_dish = ""
        for dish in main_dishes:
            if dish.name == "" or dish.name is None or dish.name == " ":
                continue

            dish_text = ""
            if dish.type != last_type_of_dish:
                dish_text += f"<u>{dish.type}</u>\n"
                last_type_of_dish = dish.type

            dish_text += f"* {dish.name}\n"
            if dish.properties != 'None':
                dish_text += f"- {dish.properties}\n"
            # dish_text += f"~ {type_of_dish}\n"
            dish_text += f"= {dish.price}\n\n"

            text += dish_text

        return text

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