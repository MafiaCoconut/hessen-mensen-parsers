import pytest
from contextlib import nullcontext as does_not_raise

from application.services.canteen_service import CanteenService
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish


@pytest.mark.usefixtures("canteen_service")
class TestSaveMenuUseCase:
    @pytest.mark.parametrize(
        "canteens_menu",
        [
            "normal",
            "without_side_dishes",
            "without_main_dishes",
        ],
        indirect=True
    )
    # def test_save(self, main_dishes: list[MainDish], side_dishes: list[SideDish], expectation, canteen_service: CanteenService):
    def test_save(self, canteens_menu, canteen_service: CanteenService, set_test_canteens):
        canteen_id, main_dishes, side_dishes, expectation = canteens_menu
        with expectation:

            canteen_service.delete_main_dishes(canteen_id=canteen_id)

            canteen_service.delete_side_dishes(canteen_id=canteen_id)

            canteen_service.save_menu(
                main_dishes=main_dishes,
                side_dishes=side_dishes
            )

            main_dishes_obj: list = canteen_service.get_main_dishes_obj(canteen_id=canteen_id)
            side_dishes_obj: list = canteen_service.get_side_dishes_obj(canteen_id=canteen_id)

            for i, main_dish_obj in enumerate(main_dishes_obj):
                print("main_dishes: ", main_dishes[i])
                print("main_dish_obj: ", main_dish_obj)
                assert main_dishes[i] == main_dish_obj

            for i, side_dish_obj in enumerate(side_dishes_obj):
                print("main_dishes: ", side_dishes[i])
                print("main_dish_obj: ", side_dish_obj)
                assert side_dishes[i] == side_dish_obj





