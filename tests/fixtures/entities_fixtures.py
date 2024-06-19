
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish
from domain.entities.canteen import Canteen
from contextlib import nullcontext as does_not_raise

import pytest


@pytest.fixture
def canteen():
    return Canteen

@pytest.fixture
def canteens_menu_normal():
    return (
        [
            MainDish(canteen_id=1, name="Блинчики", type="Ausgabe1", price="4.53", properties=None),
            MainDish(canteen_id=1, name="Котлеты", type="Ausgabe1", price="3.99", properties=None),
            MainDish(canteen_id=1, name="Нагетсы", type="Ausgabe2", price="3.99", properties="vegan"),
        ],
        [
            SideDish(canteen_id=1, name="Картошка фри", type=None, price=None, properties=None),
            SideDish(canteen_id=1, name="Десерт", type=None, price=None, properties="vegan"),
        ],
        does_not_raise()
    )


@pytest.fixture
def canteens_menu_without_side_dishes():
    return (
        [
            MainDish(canteen_id=2, name="Блинчики", type="Ausgabe1", price="4.53", properties=None),
            MainDish(canteen_id=3, name="Котлеты", type="Ausgabe1", price="3.99", properties=None),
            MainDish(canteen_id=2, name="Нагетсы", type="Ausgabe2", price="3.99", properties="vegan"),
        ],
        [],
        does_not_raise()
    )


@pytest.fixture
def canteens_menu_without_main_dishes():
    return (
        [],
        [
            SideDish(canteen_id=2, name="Картошка фри", type=None, price=None, properties=None),
            SideDish(canteen_id=2, name="Десерт", type=None, price=None, properties="vegan"),
        ],
        does_not_raise()
    )


@pytest.fixture
def canteens_menu_with_different_canteens_id():
    return (
        [
            MainDish(canteen_id=2, name="Блинчики", type="Ausgabe1", price="4.53", properties=None),
            MainDish(canteen_id=3, name="Котлеты", type="Ausgabe1", price="3.99", properties=None),
            MainDish(canteen_id=2, name="Нагетсы", type="Ausgabe2", price="3.99", properties="vegan"),
        ],
        [
            SideDish(canteen_id=2, name="Картошка фри", type=None, price=None, properties=None),
            SideDish(canteen_id=2, name="Десерт", type=None, price=None, properties="vegan"),
        ],
        pytest.raises(ValueError)
    )




