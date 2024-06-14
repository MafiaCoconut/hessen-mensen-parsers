from src.application.services.canteen_service import CanteenService
import pytest
from contextlib import nullcontext as does_not_raise


@pytest.mark.usefixtures("canteen_service")
class TestCanteenService:

    @pytest.mark.parametrize(
        "canteen_id, locale, expectation",
        [
            (1, 'ru', does_not_raise()),
            (2, 'en', does_not_raise()),
            (5, 'ru', pytest.raises(TypeError))
        ])
    def test_get_menu(self, canteen_id, locale, expectation, canteen_service):
        with expectation:
            print(canteen_service.get_canteen(canteen_id))
            assert isinstance(canteen_service.get_canteen(canteen_id), str)

    # def test_get_canteen(self):
    #     pass
    #
    # def test_parse_canteen(self):
    #     pass
    #
    # def test_parse_all_canteens(self):
    #     pass