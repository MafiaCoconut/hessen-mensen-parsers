import time

from domain.entities.canteen import Canteen
from infrastructure.repositories_impl.canteens_repository_impl import CanteensRepositoryImpl
from infrastructure.repositories_impl.side_dishes_repository_impl import SideDishesRepositoryImpl
from infrastructure.repositories_impl.main_dishes_repository_impl import MainDishesRepositoryImpl

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


@pytest.fixture
def canteens():
    canteens = [
        Canteen(name="Тестовая столовая 1", description="Qwerty", opened_time=123, closed_time=345),
        Canteen(name="Тестовая столовая 2", description="Ytrewq", opened_time=456, closed_time=857),
        Canteen(name="Тестовая столовая 3", description="asdfgh", opened_time=987, closed_time=258),
    ]
    return canteens


@pytest.fixture
def set_test_canteens(canteens, canteens_repository):
    print('\nДобавлены столовые\n')
    for canteen in canteens:
        canteens_repository.save(canteen)

    # print(canteens_repository.get_all())
    yield
    time.sleep(3)
    canteens_repository.delete_all()
    print('\nДанные удалены\n')
