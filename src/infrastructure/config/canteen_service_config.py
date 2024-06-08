from application.services.canteen_service import CanteenService
from infrastructure.config.repositories_config import canteens_repository

canteens_service = CanteenService(canteens_repository=canteens_repository)