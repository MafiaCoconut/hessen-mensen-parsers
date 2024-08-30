import logging

from application.providers.repositories_provider import RepositoriesProvider
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
                 repositories_provider: RepositoriesProvider,
                 translation_service: TranslationService
                 ):
        self.repositories_provider = repositories_provider
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
        canteens_repository = self.repositories_provider.get_canteens_repository()
        main_dishes_repository = self.repositories_provider.get_main_dishes_repository()
        side_dishes_repository = self.repositories_provider.get_side_dishes_repository()

        canteen = await canteens_repository.get(canteen_id)
        main_dishes = await main_dishes_repository.get_all_from_canteen(canteen_id=canteen_id)
        side_dishes = await side_dishes_repository.get_all_from_canteen(canteen_id=canteen_id)
        result = {
            'main_dishes': main_dishes,
            'side_dishes': side_dishes,
            'canteen': canteen
        }
        return result


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
