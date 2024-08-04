from application.services.canteen_service import CanteenService
from infrastructure.config.providers_config import canteens_provider
from infrastructure.config.repositories_config import get_side_dishes_repository, get_main_dishes_repository, \
    get_canteens_repository
from infrastructure.config.translation_service_config import translation_service
from infrastructure.config.validators_config import dishes_validator

canteens_service = CanteenService(
    canteens_repository=get_canteens_repository(),
    main_dishes_repository=get_main_dishes_repository(),
    side_dishes_repository=get_side_dishes_repository(),
    canteens_provider=canteens_provider,
    translation_service=translation_service,
    dishes_validator=dishes_validator,

)
