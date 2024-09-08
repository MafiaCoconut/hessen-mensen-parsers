import time
from application.interfaces.parser_interface import CanteenParserInterface
from infrastructure.config.selenium_config import get_selenium_driver
from infrastructure.interfaces_impl.base_parser_interface_impl import BaseParser
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish

from selenium.webdriver.common.by import By

from infrastructure.interfaces_impl.errors import ParserErrorCodes


class GiessenCafeteriaCampusTorParserInterfaceImpl(BaseParser):
    def __init__(self):
        super().__init__()
        self.url = "https://www.stwgi.de/cafeteria-campustor"
        self.driver = None

        self.waiting_time = 1
        self.canteens_open_time = {"thm": [360, 1140]}
        self.canteens_names = {"cafeteria_campus_tor": "Cafeteria CampusTor"}
        self.canteen_id = 7

    def parse(self):

        self.driver = get_selenium_driver()
        self.driver.get(self.url)

        time.sleep(self.waiting_time)
        self.accept_cookies()

        result = self.get_dishes()

        self.driver.close()

        return result

    def accept_cookies(self):
        item = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[2]/button[1]")
        item.click()
        time.sleep(self.waiting_time)

    def get_dishes(self):
        result = {'main_dishes': [], 'side_dishes': []}
        for container_nummer in range(3, 7+1):
            try:
                container = self.driver.find_element(By.XPATH, f"/html/body/div[2]/main[2]/div[1]/div/div/div/div[5]/div/div/div[3]/div[{container_nummer}]")
            except:
                result['error'] = ParserErrorCodes.NO_DATA_ON_WEBSITE
                break
            items = container.text.split('\n')
            type_of_items = items[0].replace('/', '')
            items = items[2:]

            dishes = self.format_group_items(items=items, type_of_items=type_of_items)

            for dish in dishes:
                result['main_dishes'].append(self.refactor_list_to_main_dish(dish))
        return result

    def format_group_items(self, items: list, type_of_items: str):
        dishes = []
        is_new_item = True
        item_data = ["", ""]

        for item in items:
            try:
                if item == '' or item[0] == '-':
                    continue
            except:
                continue

            if is_new_item:
                is_new_item = False
                item_data[0] = self.format_title(item)
            else:
                if item[0].islower():
                    item_data[0] += self.format_title(item)
                elif item.startswith("Euro"):
                    item_data[1] = item[5:9] + " €"
                    is_new_item = True

                    dishes.append({
                        "name": self.format_title(item_data[0]),
                        "type": type_of_items,
                        "price": item_data[1],
                        "properties": "None"
                    })
                    item_data = ["", ""]
        return dishes

    def refactor_list_to_main_dish(self, item: dict) -> MainDish:
        main_dish = MainDish(canteen_id=self.canteen_id)
        main_dish.name = item['name']
        main_dish.type = item['type']
        main_dish.price = item['price']
        main_dish.properties = item['properties']

        return main_dish
