import pytest

from application.validators.dishes_validator import DishesValidator


@pytest.fixture
def dishes_validator():
    return DishesValidator()


