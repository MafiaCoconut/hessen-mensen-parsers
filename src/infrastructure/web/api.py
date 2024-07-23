from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from infrastructure.config.canteen_service_config import canteens_service
from infrastructure.interfaces_impl.errors import ParserErrorCodes

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@router.get("/canteens/{canteen_id}")
async def read_canteens(canteen_id: str):
    print("/canteens/{canteen_id}")
    return {"text": await canteens_service.get_canteen_text(canteen_id=int(canteen_id))}


@router.get("/canteens_menu/{canteen_id}")
async def read_canteens_menu(canteen_id: str, locale: str):
    print("read_canteens_menu")
    return await canteens_service.get_menu(canteen_id=int(canteen_id), locale=locale)


@router.post('/parser/all')
async def start_all_canteens_parser():
    print("start_all_canteens_parser")
    return await canteens_service.parse_all_canteens()


@router.post('/parser/{canteen_id}')
async def start_canteens_parser(canteen_id: str):
    print("start_canteens_parser")
    result = await canteens_service.parse_canteen(canteen_id=int(canteen_id))

    if result.get('error') == ParserErrorCodes.NO_DATA_ON_WEBSITE:
        return {"error": ParserErrorCodes.NO_DATA_ON_WEBSITE.name}
    else:
        return result


# @router.get('/start')
# def start_canteens_parser():
#     return {"Hello world"}
