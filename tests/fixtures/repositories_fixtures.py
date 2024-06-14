from src.infrastructure.repositories_impl.canteens_repository_impl import CanteensRepositoryImpl
from src.infrastructure.repositories_impl.side_dishes_repository_impl import SideDishesRepositoryImpl
from src.infrastructure.repositories_impl.main_dishes_repository_impl import MainDishesRepositoryImpl

import pytest

@pytest.fixture
def canteens_repository():
    return CanteensRepositoryImpl()


@pytest.fixture
def side_dishes_repository():
    return SideDishesRepositoryImpl()


@pytest.fixture
def main_dishes_repository():
    return MainDishesRepositoryImpl()
