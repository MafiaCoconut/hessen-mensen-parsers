
from src.domain.entities.main_dish import *
from src.domain.entities.side_dish import *
from src.domain.entities.canteen import *
import pytest


@pytest.fixture()
def canteen():
    return Canteen