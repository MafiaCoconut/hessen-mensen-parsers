# from src.application.services.canteen_service import CanteenService
# import pytest
# from contextlib import nullcontext as does_not_raise
#
#
# @pytest.mark.usefixtures("canteen_service")
# class TestCanteenService:
#
#     @pytest.mark.parametrize(
#         "canteen_id, locale, expectation",
#         [
#             (1, 'ru', does_not_raise()),
#             # (2, 'en', does_not_raise()),
#             # (10, 'ru', pytest.raises(ValueError))
#         ])
#     def test_get_canteen(self, canteen_id: int, locale: str, expectation, canteen_service):
#         with expectation:
#             assert isinstance(canteen_service.get_canteen(canteen_id), str)
#
#     @pytest.mark.parametrize(
#         "canteen_id, locale, expectation",
#         [
#
#         ]
#     )
#     def test_get_menu(self, canteen_id: int,  locale: str, expectation, canteen_service):
#         with expectation:
#             assert isinstance(canteen_service.get_menu(canteen_id=canteen_id, locale=locale), str)
#     #
#     # def test_parse_canteen(self):
#     #     pass
#     #
#     # def test_parse_all_canteens(self):
#     #     pass