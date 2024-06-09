from application.interfaces.parser_interface import CanteenParserInterface
from application.providers.canteens_provider import CanteensDependencyProvider
from infrastructure.interfaces_impl.giessen_parsers_impl.giessen_thm_parser_interface_impl import GiessenTHMParserInterfaceImpl
from infrastructure.interfaces_impl.marburg_parsers_impl.marburg_bistro_parser_interface_impl import MarburgBistroParserInterfaceImpl
from infrastructure.interfaces_impl.marburg_parsers_impl.marburg_cafeteria_parser_interface_impl import MarburgCafeteriaParserInterfaceImpl
from infrastructure.interfaces_impl.marburg_parsers_impl.marburg_erlenring_parser_interface_impl import MarburgErlenringParserInterfaceImpl
from infrastructure.interfaces_impl.marburg_parsers_impl.marburg_lahnberge_parser_interface_impl import MarburgLahnbergeParserInterfaceImpl
from infrastructure.interfaces_impl.marburg_parsers_impl.marburg_mo_diner_parser_interface_impl import MarburgMoDinerParserInterfaceImpl


class CanteensDependencyProviderImpl(CanteensDependencyProvider):
    def __init__(self,
                 marburg_erlenring: MarburgErlenringParserInterfaceImpl,
                 marburg_lahnberge: MarburgLahnbergeParserInterfaceImpl,
                 marburg_bistro: MarburgBistroParserInterfaceImpl,
                 marburg_cafeteria: MarburgCafeteriaParserInterfaceImpl,
                 marburg_mo_diner: MarburgMoDinerParserInterfaceImpl,
                 giessen_thm: GiessenTHMParserInterfaceImpl
                 ):
        self.marburg_erlenring = marburg_erlenring
        self.marburg_lahnberge = marburg_lahnberge
        self.marburg_bistro = marburg_bistro
        self.marburg_cafeteria = marburg_cafeteria
        self.marburg_mo_diner = marburg_mo_diner
        self.giessen_thm = giessen_thm

    def get_marburg_erlenring_parser_interface(self) -> CanteenParserInterface:
        return self.marburg_erlenring

    def get_marburg_lahnberge_parser_interface(self) -> CanteenParserInterface:
        return self.marburg_lahnberge

    def get_marburg_bistro_parser_interface(self) -> CanteenParserInterface:
        return self.marburg_bistro

    def get_marburg_cafeteria_parser_interface(self) -> CanteenParserInterface:
        return self.marburg_cafeteria

    def get_marburg_mo_diner_parser_interface(self) -> CanteenParserInterface:
        return self.marburg_mo_diner

    def get_giessen_thm_parser_interface(self) -> CanteenParserInterface:
        return self.giessen_thm

