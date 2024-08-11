from application.services.canteen_service import CanteensService
from application.services.scheduler_service import SchedulerService
from infrastructure.config.providers_config import canteens_provider
from infrastructure.config.repositories_config import get_side_dishes_repository, get_main_dishes_repository, \
    get_canteens_repository
from infrastructure.config.scheduler_interfaces_config import get_scheduler_interface
from infrastructure.config.translation_service_config import translation_service
from infrastructure.config.validators_config import dishes_validator


def get_canteens_service() -> CanteensService:
    return CanteensService(
        canteens_repository=get_canteens_repository(),
        main_dishes_repository=get_main_dishes_repository(),
        side_dishes_repository=get_side_dishes_repository(),
        canteens_provider=canteens_provider,
        translation_service=translation_service,
        dishes_validator=dishes_validator,
        scheduler_interface=get_scheduler_interface()
    )


def get_scheduler_service() -> SchedulerService:
    return SchedulerService(
        scheduler_interface=get_scheduler_interface(),
        canteens_service=get_canteens_service()
    )

