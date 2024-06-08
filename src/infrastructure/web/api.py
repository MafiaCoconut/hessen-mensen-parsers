from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from infrastructure.config.canteen_service_config import canteens_service

router = APIRouter()


@router.get("/canteens/{canteen_id}")
def read_canteens_menu(canteen_id: int):

    return {"text": canteens_service.get_canteen(canteen_id=canteen_id)}


@router.get("/canteens_menu/{canteen_id}")
def read_canteens_menu(canteen_id: int):

    return {"menu": canteens_service.get_menu(canteen_id=canteen_id)}


@router.get('/parser/all')
def start_canteens_parser():

    return canteens_service.parse_all_canteens()


@router.get('/parser/{canteen_id}')
def start_canteens_parser(canteen_id: int):

    return canteens_service.parse_canteen(canteen_id=int(canteen_id))


@router.get('/start')
def start_canteens_parser():
    return {"Hello world"}
