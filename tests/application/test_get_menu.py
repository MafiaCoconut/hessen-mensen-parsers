import pytest

from application.use_cases.errors import MenuErrorCodes


@pytest.mark.usefixtures("canteen_service", "set_real_canteens")
class TestCanteensMenu:
    @staticmethod
    @pytest.mark.parametrize(
        "certain_canteens_menu",
        [
            # "marburg_erlenring",
            # "marburg_lahnberge",
            # "marburg_bistro",
            # "marburg_cafeteria",
            # "giessen_thm"
        ],
        indirect=True
    )
    def test_get_menu_marburg_erlenring(canteen_service, certain_canteens_menu):
        languages = ['ru', 'en', 'de', 'uk', 'ar']
        canteen_id, main_dishes, side_dishes, _ = certain_canteens_menu
        print(canteen_id)
        canteen_service.save_menu(main_dishes=main_dishes, side_dishes=side_dishes)

        for language in languages:
            menu = canteen_service.get_menu(canteen_id=canteen_id, locale=language)
            # assert menu['error']['type'] == "" and menu['error']['text'] == ""
            assert isinstance(menu['menu'], str)


    @staticmethod
    @pytest.mark.parametrize(
        "certain_canteens_menu",
        [
            # "marburg_erlenring",
            # "marburg_lahnberge",
            # "marburg_bistro",
            # "marburg_cafeteria",
            # "giessen_thm"
        ],
        indirect=True
    )
    def test_get_menu_after_closing(canteen_service, certain_canteens_menu):
        languages = ['ru', 'en', 'de', 'uk', 'ar']
        canteen_id, main_dishes, side_dishes, _ = certain_canteens_menu
        print(canteen_id)
        canteen_service.save_menu(main_dishes=main_dishes, side_dishes=side_dishes)

        for language in languages:
            menu = canteen_service.get_menu(canteen_id=canteen_id, locale=language, test_time=9999, test_day=3)
            print(menu)
            assert menu['error']['type'] == MenuErrorCodes.CANTEEN_IS_CLOSED
            assert isinstance(menu['menu'], str)

    @staticmethod
    @pytest.mark.parametrize(
        "certain_canteens_menu",
        [
            "marburg_erlenring",
            "marburg_lahnberge",
            "marburg_bistro",
            "marburg_cafeteria",
            "giessen_thm"
        ],
        indirect=True
    )
    def test_get_menu_in_open_time(canteen_service, certain_canteens_menu):
        languages = ['ru', 'en', 'de', 'uk', 'ar']
        canteen_id, main_dishes, side_dishes, _ = certain_canteens_menu
        canteen_service.save_menu(main_dishes=main_dishes, side_dishes=side_dishes)

        canteen = canteen_service.get_canteen_obj(canteen_id)
        for language in languages:
            menu = canteen_service.get_menu(canteen_id=canteen_id, locale=language,
                                            test_time=canteen.closed_time - 30, test_day=3)
            assert menu['error']['type'] == ""
            assert isinstance(menu['menu'], str)



