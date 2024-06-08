from application.interfaces.parser_interface import CanteenParserInterface
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish
from icecream import ic
import re

from infrastructure.interfaces_impl.base_parser_interface_impl import BaseParser


class MarburgBistroParserInterfaceImpl(BaseParser):
    def __init__(self):
        super().__init__()
        self.canteen_number = "460"
        # self.canteens_open_time = [510, 720]
        # self.canteens_name = "Mo's Dinner"
        self.canteen_id = 3

        self.url = 'https://studierendenwerk-marburg.de/essen-trinken/speisekarte'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

    def parse(self):
        list_of_dishes = self.get_list_of_dishes()
        menu = {'main_dishes': [], 'side_dishes': []}

        for dish in list_of_dishes:
            result = self.refactor_dish_to_entities(dish)
            if result:
                if isinstance(result, MainDish):
                    menu['main_dishes'].append(result)
                elif isinstance(result, SideDish):
                    menu['side_dishes'].append(result)
        ic(menu)
        return menu

    def get_list_of_dishes(self) -> list:
        elements = self.soup.find_all('tr', {
            'data-canteen': self.canteen_number,
            'data-date': "2024-06-10",
            # 'data-date': str(datetime.now())[:10],
        })

        items = []
        # список всех елементов подходящих условию
        for element in elements:
            # print(element.text.strip().split('\n'))
            items.append(element.text.strip())
        return items

    def refactor_dish_to_entities(self, dish: str):
        dishes_list = dish.split('\n')

        dishes_list = [item for item in dishes_list if item != '']

        if not dishes_list:
            return False

        # У объекта main_dish всегда > 2-ух элементов, у side_dish всегда <= 2
        if len(dishes_list) > 2:
            dish_obj = self.rafactor_main_dish(dishes_list)
        else:
            dish_obj = self.refactor_side_dish(dishes_list)

        return dish_obj


    def rafactor_main_dish(self, dish: list):
        main_dish = MainDish(canteen_id=self.canteen_id)

        main_dish.name = self.format_title(dish[0])
        main_dish.type = dish[1]
        main_dish.price = dish[-1]

        properties = main_dish.type[main_dish.type.rfind(' ') + 1:]
        item_properties_in_type = self.is_vegan_or_is_sweet(properties)

        item_properties_in_separate_cell = dish[-2]
        if item_properties_in_separate_cell != main_dish.type:
            main_dish.properties = item_properties_in_separate_cell

        else:
            main_dish.properties = item_properties_in_type

        main_dish.type = main_dish.type[
                         :main_dish.type.rfind(' ')] if item_properties_in_type != 'None' else main_dish.type
        return main_dish

    def refactor_side_dish(self, dish: list):
        side_dish = SideDish(canteen_id=self.canteen_id)

        side_dish.name = self.format_title(dish[0])
        if len(dish) == 2:
            side_dish.properties = dish[1]
        else:
            side_dish.properties = self.is_vegan_or_is_sweet(dish[0])

        return side_dish
