
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


@pytest.fixture()
def real_canteens():
    return [
        Canteen(canteen_id=1, name="Mensa Erlenring", opened_time=690, closed_time=855, description="---"),
        Canteen(canteen_id=2, name="Mensa Lahnberge", opened_time=690, closed_time=855, description="---"),
        Canteen(canteen_id=3, name="Bistro", opened_time=540, closed_time=1140, description="---"),
        Canteen(canteen_id=4, name="Cafeteria Lahnberge", opened_time=480, closed_time=1020, description="---"),
        Canteen(canteen_id=5, name="Mo's Dinner", opened_time=510, closed_time=720, description="---"),
        Canteen(canteen_id=6, name="THM", opened_time=0, closed_time=840, description="---"),
        Canteen(canteen_id=7, name="тестовая столовая_1",description="---"),


    ]



@pytest.fixture
def test_canteens():
    return [
        Canteen(name="Тестовая столовая 1", description="Qwerty", opened_time=123, closed_time=345),
        Canteen(name="Тестовая столовая 2", description="Ytrewq", opened_time=456, closed_time=857),
        Canteen(name="Тестовая столовая 3", description="asdfgh", opened_time=987, closed_time=258),
    ]


@pytest.fixture
def certain_canteens_menu(request):
    match request.param:
        case "marburg_erlenring":
            return test_data_marburg_erlenring()
        case "marburg_lahnberge":
            return test_data_marburg_lahnberge()
        case "marburg_bistro":
            return test_data_marburg_bistro()
        case "marburg_cafeteria":
            return test_data_marburg_cafeteria()
        case "giessen_thm":
            return test_data_giessen_thm()


def test_data_marburg_erlenring():
    return (
        1,
        [
            MainDish(canteen_id=1, name="Hackfleischbällchen Preiselbeersauce", type="Menü 1", price="4.45", properties="-"),
            MainDish(canteen_id=1, name="Paprika-Zucchinipfanne mit Bulgur und Soja-Hack, dazu Tomaten-Soja-Dip", type="Menü 2 vegetarisch", price="4.05", properties="vegan"),
            MainDish(canteen_id=1, name="Käsespätzle 'Schwäbische Art' mit gebräunten Zwiebeln Blattsalat", type="Tagesgericht", price="3.05", properties="-"),
        ],
        [
            SideDish(canteen_id=1, name="Kartoffelsuppe -vegan", type="-", price="-", properties="-"),
            SideDish(canteen_id=1, name="Reis Pommes frites Salzkartoffeln", type="-", price="-", properties="-"),
        ],
        does_not_raise()
        )


def test_data_marburg_lahnberge():
    return (
        2,
        [
            MainDish(canteen_id=2, name="Gebackenes Schweinekotelette mit Salzkartoffeln und Kraut dazu Salat", type="Aktion Lahnberge", price="4.65", properties="polen"),
            MainDish(canteen_id=2, name="Hackfleischbällchen Preiselbeersauce", type="Menü 1", price="4.45", properties="-"),
            MainDish(canteen_id=2, name="Paprika-Zucchinipfanne mit Bulgur und Soja-Hack, dazu Tomaten-Soja-Dip", type="Menü 2 vegetarisch", price="4.05", properties="vegan"),
            MainDish(canteen_id=2, name="Käsespätzle 'Schwäbische Art' mit gebräunten Zwiebeln Blattsalat", type="Tagesgericht", price="3.05", properties="-"),
        ],
        [
            SideDish(canteen_id=2, name="Kartoffelsuppe -vegan", type="-", price="-", properties="-"),
            SideDish(canteen_id=2, name="Reis Pommes frites Salzkartoffeln", type="-", price="-", properties="-"),
        ],
        does_not_raise()
        )


def test_data_marburg_bistro():
    return (
        3,
        [
            MainDish(canteen_id=3, name="Gebackenes Schweinekotelette mit Salzkartoffeln und Kraut dazu Salat", type="Bistro Aktionsgericht", price="4.65", properties="polen"),
            MainDish(canteen_id=3, name="Spaghetti mit Rindfleischbolognese, dazu Salat", type="Late Lunch", price="3.25", properties="-"),
            MainDish(canteen_id=3, name="Käsespätzle 'Schwäbische Art' mit gebräunten Zwiebeln Blattsalat", type="Late Lunch vegetarisch", price="0.00", properties="vegan"),
        ],
        [
            SideDish(canteen_id=3, name="Kartoffelsuppe -vegan", type="-", price="-", properties="-"),
            SideDish(canteen_id=3, name="Reis Pommes frites Salzkartoffeln", type="-", price="-", properties="-"),
        ],
        does_not_raise()
        )


def test_data_marburg_cafeteria():
    return (
        4,
        [
            MainDish(canteen_id=4, name="Kottbülar mit Preiselbeerrahm", type="Late Lunch", price="4.45", properties="-"),
            MainDish(canteen_id=4, name="Paprika-Zucchinipfanne mit Bulgur und Soja-Streifen, dazu Tomaten-Chili-Dip", type="Late Lunch vegetarisch", price="4.05", properties="vegan"),
        ],
        [],
        does_not_raise()
        )


def test_data_giessen_thm():
    return (
        6,
        [
            MainDish(canteen_id=6, name="Knusprige Chicken Drumsticks", type="Ausgabe 1", price="3.80", properties="-"),
            MainDish(canteen_id=6, name="Maultaschen mit Frischkäse- Spinatfüllung", type="Ausgabe 2", price="3.20", properties="-"),
            MainDish(canteen_id=6, name="Vegane Kürbis-Gemüsepfanne", type="Ausgabe 2", price="2.60", properties="-"),
            # MainDish(canteen_id=6, name="Pasta", type="Pastaria", price="2.4", properties="-"),
            MainDish(canteen_id=6, name="Karotten-Ingwercremesuppe", type="Suppen-/Eintopfstation", price="0.80", properties="-"),
        ],
        [
            SideDish(canteen_id=6, name="Frisches saisonales Gemüse", type="Alle Ausgaben", price="1.10", properties="-"),
            SideDish(canteen_id=6, name="Pommes frites Tüte",         type="Alle Ausgaben", price="1.20", properties="-"),
            SideDish(canteen_id=6, name="Gemischter Blattsalat",      type="Alle Ausgaben", price="0.70", properties="-"),
            SideDish(canteen_id=6, name="Karottensalat",              type="Alle Ausgaben", price="0.70", properties="-"),
            SideDish(canteen_id=6, name="Sahnepudding Nuss Nougat",   type="Alle Ausgaben", price="0.70", properties="-"),
        ],
        does_not_raise()
        )
