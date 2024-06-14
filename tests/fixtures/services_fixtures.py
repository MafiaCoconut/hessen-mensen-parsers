from src.application.services.canteen_service import CanteenService
from src.application.services.translation_service import TranslationService
from src.application.services.scheduler_service import SchedulerService
from src.application.services.set_all_schedulers_service import SetAllSchedulersJobsUseCase


import pytest

@pytest.fixture
def canteen_service(canteens_repository, main_dishes_repository, side_dishes_repository, canteens_provider, translation_service):
    canteen_service = CanteenService(
        canteens_repository=canteens_repository,
        main_dishes_repository=main_dishes_repository,
        side_dishes_repository=side_dishes_repository,
        canteens_provider=canteens_provider,
        translation_service=translation_service,
    )
    return canteen_service


# @pytest.fixture
# def scheduler_service(scheduler_interface):
#     return SchedulerService(scheduler_interface)


