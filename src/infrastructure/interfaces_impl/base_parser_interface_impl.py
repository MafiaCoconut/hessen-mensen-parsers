from application.interfaces.parser_interface import CanteenParserInterface
import re
from datetime import datetime

class BaseParser(CanteenParserInterface):
    def __init__(self):
        self.canteens_open_time = None

    def parse(self) -> dict:
        raise NotImplementedError("This method should be overridden in a subclass")

    @staticmethod
    def format_title(data: str):
        data = re.sub(r'\([^)]*\)', '', data)
        data = re.sub(r'\s{2,}', ' ', data)
        return data + " "

    @staticmethod
    def is_vegan_or_is_sweet(item: str):
        if "vegan" in item or "vegetarisch" in item:
            return 'vegan'
        elif "süß" in item:
            return 'süß'
        else:
            return 'None'

    def check_opening_time(self, canteen):
        time_now = datetime.now().hour * 60 + datetime.now().minute
        # time_now = 11 * 60 + 56
        # time_now = 20 * 60 + 59
        open_time, close_time = self.canteens_open_time
        if (time_now < open_time or close_time < time_now) or not self.is_weekday():
            return False
        return True

    @staticmethod
    def is_weekday():
        weekday = int(datetime.now().isoweekday())
        if 1 <= weekday <= 5:
            return True
        return False

