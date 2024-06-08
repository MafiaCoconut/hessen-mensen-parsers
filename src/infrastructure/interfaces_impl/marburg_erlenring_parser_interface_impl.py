from src.application.interfaces.parser_interface import CanteenParserInterface
import requests
from bs4 import BeautifulSoup


class MarburgErlenringParserInterfaceImpl(CanteenParserInterface):
    def __init__(self):
        self.canteen_number = "330"
        self.canteens_open_time = [690, 855]
        self.canteens_name = "Mensa Erlenring"

        self.url = 'https://studierendenwerk-marburg.de/essen-trinken/speisekarte'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

    def parse(self):
        pass