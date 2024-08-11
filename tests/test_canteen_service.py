from domain.entities.canteen import Canteen
from src.application.services.canteen_service import CanteensService
import pytest
from contextlib import nullcontext as does_not_raise


@pytest.mark.usefixtures("canteen_service")
class TestCanteenService:

    @pytest.mark.parametrize(
        "canteen_id, locale, expectation",
        [
            (1, 'ru', does_not_raise()),
            (2, 'en', does_not_raise()),
            (10, 'ru', pytest.raises(ValueError))
        ])
    def test_get_canteen_text(self, canteen_id: int, locale: str, expectation, canteen_service, set_test_canteens):
        with expectation:
            assert isinstance(canteen_service.get_canteen_text(canteen_id), str)

    @pytest.mark.parametrize(
        "canteen_id, locale, expectation",
        [
            (1, 'ru', does_not_raise()),
            (2, 'en', does_not_raise()),
            (10, 'ru', pytest.raises(ValueError))
        ])
    def test_get_canteen_obj(self, canteen_id: int, locale: str, expectation, canteen_service, set_test_canteens):
        with expectation:
            assert isinstance(canteen_service.get_canteen_obj(canteen_id), Canteen)

    # @pytest.mark.parametrize(
    #     ""
    # )
    # def test_get_main_dishes_obj(self, canteen_id: int, expectation, canteen_service,
    #                              test_main_dishes, test_side_dishes):
    #     canteen_service.save_main_dishes(test_main_dishes)
    #     canteen_service.save_side_dishes(test_side_dishes)
    #
    #     main_dishes_obj: list = canteen_service.get_main_dishes_obj(canteen_id=canteen_id)
    #     side_dishes_obj: list = canteen_service.get_side_dishes_obj(canteen_id=canteen_id)
    #
    #     for i, main_dish_obj in enumerate(main_dishes_obj):
    #         assert True

