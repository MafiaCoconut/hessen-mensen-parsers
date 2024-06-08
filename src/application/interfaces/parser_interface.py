from abc import ABC, abstractmethod

from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish


class CanteenParserInterface(ABC):
    @abstractmethod
    def parse(self) -> dict:
        pass
