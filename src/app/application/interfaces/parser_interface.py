from abc import ABC, abstractmethod


class CanteenParser(ABC):
    @abstractmethod
    def parse(self):
        pass
