from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from infrastructure.config.canteen_service_config import canteens_service
from infrastructure.interfaces_impl.errors import ParserErrorCodes

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Hello, World!"}


@router.get("/canteens/{canteen_id}")
def read_canteens(canteen_id: str):
    print("/canteens/{canteen_id}")
    return {"text": canteens_service.get_canteen_text(canteen_id=int(canteen_id))}


@router.get("/canteens_menu/{canteen_id}")
def read_canteens_menu(canteen_id: str, locale: str):
    print("read_canteens_menu")
    return canteens_service.get_menu(canteen_id=int(canteen_id), locale=locale)


@router.get('/parser/all')
def start_all_canteens_parser():
    print("start_all_canteens_parser")
    return canteens_service.parse_all_canteens()


@router.get('/parser/{canteen_id}')
def start_canteens_parser(canteen_id: str):
    print("start_canteens_parser")
    result = canteens_service.parse_canteen(canteen_id=int(canteen_id))

    if result.get('error') == ParserErrorCodes.NO_DATA_ON_WEBSITE:
        return {"error": ParserErrorCodes.NO_DATA_ON_WEBSITE.name}
    else:
        return canteens_service.parse_canteen(canteen_id=int(canteen_id))


# @router.get('/start')
# def start_canteens_parser():
#     return {"Hello world"}
