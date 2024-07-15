from application.services.canteen_service import CanteenService
from application.services.translation_service import TranslationService
from application.services.scheduler_service import SchedulerService
from application.services.set_all_schedulers_service import SetAllSchedulersJobsUseCase

import pytest


@pytest.fixture
def canteen_service(
        canteens_repository, main_dishes_repository, side_dishes_repository,
        canteens_provider, translation_service, dishes_validator
):
    canteen_service = CanteenService(
        canteens_repository=canteens_repository,
        main_dishes_repository=main_dishes_repository,
        side_dishes_repository=side_dishes_repository,
        canteens_provider=canteens_provider,
        translation_service=translation_service,
        dishes_validator=dishes_validator
    )
    return canteen_service

# @pytest.fixture
# def scheduler_service(scheduler_interface):
#     return SchedulerService(scheduler_interface)


    # def main_dish(main_dish: MainDish):
    #     if main_dish.name is None:
    #         raise ValueError("name")
    #     if main_dish.type is None:
    #         raise ValueError("type")
    #     if main_dish.canteen_id is None:
    #         raise ValueError("canteen_id")
    #     if main_dish.price is None:
    #         raise ValueError("price")
    #     if main_dish.properties is None:
    #         raise ValueError("properties")