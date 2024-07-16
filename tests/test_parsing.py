import pytest

@pytest.mark.usefixtures("canteen_service", "set_real_canteens")
class TestParseCanteens:
    @staticmethod
    def test_parse_marburg_erlenring(canteen_service):
        canteen_id = 1
        canteen_service.parse_canteen(canteen_id)
        main_dishes = canteen_service.get_main_dishes_obj(canteen_id=canteen_id)
        side_dishes = canteen_service.get_side_dishes_obj(canteen_id=canteen_id)

        print(main_dishes)
        print(side_dishes)
        assert main_dishes is not None
        assert side_dishes is not None

    @staticmethod
    def test_parse_marburg_lahnberge(canteen_service):
        canteen_id = 2
        canteen_service.parse_canteen(canteen_id)
        main_dishes = canteen_service.get_main_dishes_obj(canteen_id=canteen_id)
        side_dishes = canteen_service.get_side_dishes_obj(canteen_id=canteen_id)

        print(main_dishes)
        print(side_dishes)
        assert main_dishes is not None
        assert side_dishes is not None

    @staticmethod
    def test_parse_marburg_cafeteria(canteen_service):
        canteen_id = 4
        canteen_service.parse_canteen(canteen_id)
        main_dishes = canteen_service.get_main_dishes_obj(canteen_id=canteen_id)
        side_dishes = canteen_service.get_side_dishes_obj(canteen_id=canteen_id)

        print(main_dishes)
        print(side_dishes)
        assert main_dishes is not None
        assert side_dishes is not None

    @staticmethod
    def test_parse_marburg_bistro(canteen_service):
        canteen_id = 3
        canteen_service.parse_canteen(canteen_id)
        main_dishes = canteen_service.get_main_dishes_obj(canteen_id=canteen_id)
        side_dishes = canteen_service.get_side_dishes_obj(canteen_id=canteen_id)

        print(main_dishes)
        print(side_dishes)
        assert main_dishes is not None
        assert side_dishes is not None

    @staticmethod
    def test_parse_giessen_thm(canteen_service):
        canteen_id = 6
        canteen_service.parse_canteen(canteen_id)
        main_dishes = canteen_service.get_main_dishes_obj(canteen_id=canteen_id)
        side_dishes = canteen_service.get_side_dishes_obj(canteen_id=canteen_id)

        print(main_dishes)
        print(side_dishes)
        assert main_dishes is not None
        assert side_dishes is not None




