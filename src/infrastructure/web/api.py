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
    return {"text": await canteens_service.get_canteen_text(canteen_id=int(canteen_id))}


@router.get("/canteens_menu/{canteen_id}")
async def read_canteens_menu(canteen_id: str):
    """
    Функция возвращает информацию о текущих блюдах столовой
    :param canteen_id: Id столовой в базе данных
    :return: {'main_dishes': list[MainDish], 'side_dishes': side_dishes[SideDishes], 'canteen_name': str}
    """
    return await canteens_service.get_canteens_dishes(canteen_id=int(canteen_id))


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


