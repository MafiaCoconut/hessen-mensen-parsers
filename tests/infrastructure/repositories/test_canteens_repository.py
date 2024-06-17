import pytest
from domain.entities.canteen import Canteen


@pytest.fixture
def canteens():
    canteens = [
        Canteen(name="Тестовая столовая 1", description="Qwerty", opened_time=123, closed_time=345),
        # Canteen(name="Тестовая столовая 2", description="Ytrewq", opened_time=456, closed_time=857),
        # Canteen(name="Тестовая столовая 3", description="asdfgh", opened_time=987, closed_time=258),
    ]
    return canteens


# class TestCanteensRepository:
#     def test_get_all(self):
#         pass
#
#     def test_get(self):
#         pass
#
#     def test_save(self, canteens, canteens_repository):
#         for canteen in canteens:
#             canteens_repository.save(canteen)
#
#         new_data = canteens_repository.get_all()
#         print(new_data)
#         assert len(new_data) == 1
