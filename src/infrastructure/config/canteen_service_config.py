from application.services.canteen_service import CanteenService
from infrastructure.config.providers_config import canteens_provider
from infrastructure.config.repositories_config import canteens_repository, main_dishes_repository, side_dishes_repository
from infrastructure.config.translation_service_config import translation_service

canteens_service = CanteenService(
    canteens_repository=canteens_repository,
    main_dishes_repository=main_dishes_repository,
    side_dishes_repository=side_dishes_repository,
    canteens_provider=canteens_provider,
    translation_service=translation_service

)
