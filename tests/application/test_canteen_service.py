from domain.entities.canteen import Canteen
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
