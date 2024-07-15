from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish


class DishesValidator:
    @staticmethod
    def main_dish(main_dish: MainDish):
        if main_dish.name is None:
            raise ValueError("name")
        if main_dish.type is None:
            raise ValueError("type")
        if main_dish.canteen_id is None:
            raise ValueError("canteen_id")
        if main_dish.price is None:
            raise ValueError("price")
        if main_dish.properties is None:
            raise ValueError("properties")

    @staticmethod
    def side_dish(side_dishes: SideDish):
        if side_dishes.name is None:
            raise ValueError("name")
        if side_dishes.type is None:
            raise ValueError("type")
        if side_dishes.canteen_id is None:
            raise ValueError("canteen_id")
        if side_dishes.price is None:
            raise ValueError("price")
        if side_dishes.properties is None:
            raise ValueError("properties")

