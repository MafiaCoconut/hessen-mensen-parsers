from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from application.services.canteen_service import CanteenService
from domain.entities.canteen import Canteen
from infrastructure.config.repositories_config import canteens_repository


router = APIRouter()

@router.get("/canteens/{canteen_id}")
def read_canteens_menu(canteen_id: str):

    canteen_service = CanteenService(canteens_repository)
    return {canteen_service.get(canteen_id=canteen_id)}


@router.post('/start-parser/{canteen_id}')
def start_canteens_parser(canteen_id: str):
    pass

@router.get('/start')
def start_canteens_parser():
    return {"Hello world"}
