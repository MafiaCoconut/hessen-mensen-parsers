
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish
from domain.entities.canteen import Canteen
from contextlib import nullcontext as does_not_raise

import pytest


@pytest.fixture
def canteens_menu(request):
    match request.param:
        case "normal":
            return canteens_menu_normal()
        case "without_side_dishes":
            return canteens_menu_without_side_dishes()
        case "without_main_dishes":
            return canteens_menu_without_main_dishes()
        case "with_different_canteens_id":
            return canteens_menu_with_different_canteens_id()



def canteens_menu_normal():
    return (
        1,
        [
            MainDish(canteen_id=1, name="Блинчики", type="Ausgabe1", price="4.53", properties="None"),
            MainDish(canteen_id=1, name="Котлеты", type="Ausgabe1", price="3.99", properties="None"),
            MainDish(canteen_id=1, name="Нагетсы", type="Ausgabe2", price="3.99", properties="vegan"),
        ],
        [
            SideDish(canteen_id=1, name="Картошка фри", type="None", price="None", properties="None"),
            SideDish(canteen_id=1, name="Десерт", type="None", price="None", properties="vegan"),
        ],
        does_not_raise()
    )


def canteens_menu_without_side_dishes():
    return (
        2,
        [
            MainDish(canteen_id=2, name="Блинчики", type="Ausgabe1", price="4.53", properties="None"),
            MainDish(canteen_id=2, name="Котлеты", type="Ausgabe1", price="3.99", properties="None"),
            MainDish(canteen_id=2, name="Нагетсы", type="Ausgabe2", price="3.99", properties="vegan"),
        ],
        [],
        does_not_raise()
    )


def canteens_menu_without_main_dishes():
    return (
        2,
        [],
        [
            SideDish(canteen_id=2, name="Картошка фри", type="None", price="None", properties="None"),
            SideDish(canteen_id=2, name="Десерт", type="None", price="None", properties="vegan"),
        ],
        does_not_raise()
    )


def canteens_menu_with_different_canteens_id():
    return (
        2,
        [
            MainDish(canteen_id=2, name="Блинчики", type="Ausgabe1", price="4.53", properties="None"),
            MainDish(canteen_id=3, name="Котлеты", type="Ausgabe1", price="3.99", properties='None'),
            MainDish(canteen_id=2, name="Нагетсы", type="Ausgabe2", price="3.99", properties="vegan"),
        ],
        [
            SideDish(canteen_id=2, name="Картошка фри", type="None", price="None", properties="None"),
            SideDish(canteen_id=2, name="Десерт", type="None", price="None", properties="vegan"),
        ],
        pytest.raises(ValueError)
    )


# @pytest.fixture()
# def canteens():
#     return [
#         Canteen(canteen_id=1, name="Mensa Erlenring", opened_time=690, closed_time=855, description="---"),
#         Canteen(canteen_id=2, name="Mensa Lahnberge", opened_time=690, closed_time=85, description="---"),
#         Canteen(canteen_id=3, name="Bistro", opened_time=540, closed_time=1140, description="---"),
#         Canteen(canteen_id=4, name="Cafeteria Lahnberge", opened_time=480, closed_time=1020, description="---"),
#         Canteen(canteen_id=5, name="Mo's Dinner", opened_time=510, closed_time=720, description="---"),
#         Canteen(canteen_id=6, name="THM", description="---"),
#         Canteen(canteen_id=7, name="тестовая столовая_1",description="---"),
#
#
#     ]

