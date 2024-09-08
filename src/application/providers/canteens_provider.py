from abc import ABC, abstractmethod

from application.interfaces.parser_interface import CanteenParserInterface


class CanteensDependencyProvider(ABC):
    @abstractmethod
    def get_marburg_erlenring_parser_interface(self) -> CanteenParserInterface:
        pass

    @abstractmethod
    def get_marburg_lahnberge_parser_interface(self) -> CanteenParserInterface:
        pass

    @abstractmethod
    def get_marburg_bistro_parser_interface(self) -> CanteenParserInterface:
        pass

    @abstractmethod
    def get_marburg_cafeteria_parser_interface(self) -> CanteenParserInterface:
        pass

    @abstractmethod
    def get_marburg_mo_diner_parser_interface(self) -> CanteenParserInterface:
        pass

    @abstractmethod
    def get_giessen_thm_parser_interface(self) -> CanteenParserInterface:
        pass

    @abstractmethod
    def get_giessen_cafeteria_campus_tor_parser_interface(self) -> CanteenParserInterface:
        pass
