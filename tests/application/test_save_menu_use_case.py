import pytest
from contextlib import nullcontext as does_not_raise

from application.services.canteen_service import CanteenService
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish

@pytest.mark.usefixtures("canteen_service")
class TestSaveMenuUseCase:
    @pytest.mark.parametrize(
        "main_dishes, side_dishes, expectation",
        [
            pytest.lazy_fixture("canteens_menu_normal"),
            pytest.lazy_fixture("canteens_menu_without_side_dishes"),
            pytest.lazy_fixture("canteens_menu_without_main_dishes"),
            pytest.lazy_fixture("canteens_menu_with_different_canteens_id"),
        ]
    )
    def test_save(self, main_dishes: list[MainDish], side_dishes: list[SideDish], expectation, canteen_service: CanteenService):
        with expectation:

            canteen_service.delete_main_dishes(canteen_id=main_dishes[0].canteen_id)
            canteen_service.delete_side_dishes(canteen_id=main_dishes[0].canteen_id)

            canteen_service.save_canteens_menu_use_case(
                main_dishes=main_dishes,
                side_dishes=side_dishes
            )

            main_dishes_obj: list = canteen_service.get_main_dishes_obj()
            side_dishes_obj: list = canteen_service.get_side_dishes_obj()

            for i, main_dish_obj in enumerate(main_dishes_obj):
                assert main_dishes[i] == main_dish_obj

            for i, side_dish_obj in enumerate(side_dishes_obj):
                assert side_dishes[i] == side_dish_obj




