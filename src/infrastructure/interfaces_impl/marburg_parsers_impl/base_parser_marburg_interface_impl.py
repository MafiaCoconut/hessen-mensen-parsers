from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish
from infrastructure.interfaces_impl.base_parser_interface_impl import BaseParser


class BaseMarburgParser(BaseParser):
    def parse(self):
        raise NotImplementedError("This method should be overridden in a subclass")

    def rafactor_main_dish(self, dish: list, canteen_id: int):
        main_dish = MainDish(canteen_id=canteen_id)

        main_dish.name = self.format_title(dish[0])
        main_dish.type = dish[1]
        main_dish.price = dish[-1]

        properties = main_dish.type[main_dish.type.rfind(' ') + 1:]
        item_properties_in_type = self.is_vegan_or_is_sweet(properties)

        item_properties_in_separate_cell = dish[-2]
        if item_properties_in_separate_cell != main_dish.type:
            main_dish.properties = item_properties_in_separate_cell

        else:
            main_dish.properties = item_properties_in_type

        main_dish.type = main_dish.type[
                         :main_dish.type.rfind(' ')] if item_properties_in_type != 'None' else main_dish.type
        return main_dish

    def refactor_side_dish(self, dish: list, canteen_id: int):
        side_dish = SideDish(canteen_id=canteen_id)

        side_dish.name = self.format_title(dish[0])
        if len(dish) == 2:
            side_dish.properties = dish[1]
        else:
            side_dish.properties = self.is_vegan_or_is_sweet(dish[0])
        side_dish.type = "-"
        side_dish.price = "-"
        return side_dish
