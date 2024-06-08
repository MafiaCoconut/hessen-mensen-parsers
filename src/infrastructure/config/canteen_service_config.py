from application.services.canteen_service import CanteenService
from infrastructure.config.providers_config import canteens_provider
from infrastructure.config.repositories_config import canteens_repository, main_dishes_repository, side_dishes_repository

canteens_service = CanteenService(
    canteens_repository=canteens_repository,
    main_dishes_repository=main_dishes_repository,
    side_dishes_repository=side_dishes_repository,
    canteens_provider=canteens_provider
)
