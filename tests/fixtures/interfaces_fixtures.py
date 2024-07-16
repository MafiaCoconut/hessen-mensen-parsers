from application.services.translation_service import TranslationService
from infrastructure.interfaces_impl.marburg_parsers_impl.marburg_bistro_parser_interface_impl import MarburgBistroParserInterfaceImpl
from infrastructure.interfaces_impl.marburg_parsers_impl.marburg_erlenring_parser_interface_impl import MarburgErlenringParserInterfaceImpl
from infrastructure.interfaces_impl.marburg_parsers_impl.marburg_cafeteria_parser_interface_impl import MarburgCafeteriaParserInterfaceImpl
from infrastructure.interfaces_impl.marburg_parsers_impl.marburg_lahnberge_parser_interface_impl import MarburgLahnbergeParserInterfaceImpl
from infrastructure.interfaces_impl.marburg_parsers_impl.marburg_mo_diner_parser_interface_impl import MarburgMoDinerParserInterfaceImpl

from infrastructure.interfaces_impl.giessen_parsers_impl.giessen_thm_parser_interface_impl import GiessenTHMParserInterfaceImpl

from infrastructure.providers_impl.canteens_provider_impl import CanteensDependencyProviderImpl

import pytest


@pytest.fixture
def giessen_thm_interface():
    return GiessenTHMParserInterfaceImpl()


@pytest.fixture
def marburg_erlenring_interface():
    return MarburgErlenringParserInterfaceImpl()


@pytest.fixture
def marburg_lahnberge_interface():
    return MarburgLahnbergeParserInterfaceImpl()


@pytest.fixture
def marburg_cafeteria_interface():
    return MarburgCafeteriaParserInterfaceImpl()


@pytest.fixture
def marburg_bistro_interface():
    return MarburgBistroParserInterfaceImpl()


@pytest.fixture
def marburg_mo_diner_interface():
    return MarburgMoDinerParserInterfaceImpl()


@pytest.fixture
def canteens_provider(
        marburg_erlenring_interface,
        marburg_lahnberge_interface,
        marburg_bistro_interface,
        marburg_cafeteria_interface,
        marburg_mo_diner_interface,
        giessen_thm_interface
):
    provider = CanteensDependencyProviderImpl(
        marburg_erlenring=marburg_erlenring_interface,
        marburg_lahnberge=marburg_lahnberge_interface,
        marburg_bistro=marburg_bistro_interface,
        marburg_cafeteria=marburg_cafeteria_interface,
        marburg_mo_diner=marburg_mo_diner_interface,
        giessen_thm=giessen_thm_interface
    )
    return provider


@pytest.fixture
def translation_service():
    return TranslationService(status="Tests")


