import logging
import time

from domain.entities.canteen import Canteen
from domain.entities.main_dish import MainDish
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
def set_test_canteens(test_canteens, canteens_repository):
    logging.info("Тестовые столовые инициализированы в бд")
    for canteen in test_canteens:
        canteens_repository.save(canteen)

    yield

    time.sleep(3)
    canteens_repository.delete_all()
    logging.info("Тестовые столовые удалены из бд")


@pytest.fixture
def set_real_canteens(real_canteens, canteens_repository):
    logging.info("Реальные столовые инициализированы в бд")
    for canteen in real_canteens:
        canteens_repository.save(canteen)

    yield

    # time.sleep(3)
    canteens_repository.delete_all()
    logging.info("Реальные столовые удалены из бд")


@pytest.fixture
def set_test_main_dishes(main_dishes, main_dishes_repository):
    print("\nДобавлены главные блюда\n")
    for main_dish in main_dishes:
        main_dishes_repository.save(main_dish)

    yield

    # time.sleep(3)
    main_dishes_repository.delete_all()
    print("\nДанные удалены\n")

