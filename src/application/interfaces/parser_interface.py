from abc import ABC, abstractmethod


class CanteenParserInterface(ABC):
    @abstractmethod
    def parse(self):
        pass
