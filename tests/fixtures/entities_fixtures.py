
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish
from domain.entities.canteen import Canteen
import pytest


@pytest.fixture()
def canteen():
    return Canteen