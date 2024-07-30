from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from infrastructure.config.canteen_service_config import canteens_service
from infrastructure.interfaces_impl.errors import ParserErrorCodes

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@router.get("/canteen{canteen_id}")
async def read_canteens(canteen_id: int):
    return {"text": await canteens_service.get_canteen_text(canteen_id=int(canteen_id))}


@router.get("/canteen{canteen_id}/getDishes")
async def get_canteens_data(canteen_id: int):
    """
    Функция возвращает по API информацию о запрашиваемой столовой и её текущих блюдах

    :param canteen_id: Id столовой в базе данных
    :return: {
        'main_dishes': list[MainDish],
        'side_dishes': side_dishes[SideDishes],
        'canteen': Canteen
    }
    """
    return await canteens_service.get_canteens_data(canteen_id=int(canteen_id))


@router.post('/canteen/startAllParsers')
async def start_all_canteens_parser():
    """
    Функция после запроса по API запускает парсинг всех столовых

    :return: None
    """
    return await canteens_service.parse_all_canteens()


@router.post('/canteen{canteen_id}/startParser')
async def start_canteens_parser(canteen_id: int):
    """
    Функция запускает парсер конкретной столовой по её ID в базе данных
    :param canteen_id: ID столовой в базе данных
    :return: {'main_dishes': list, 'side_dishes': list} | {'error': NO_DATA_ON_WEBSITE}
    """
    result = await canteens_service.parse_canteen(canteen_id=int(canteen_id))

    if result.get('error') == ParserErrorCodes.NO_DATA_ON_WEBSITE:
        return {"error": ParserErrorCodes.NO_DATA_ON_WEBSITE.name}
    else:
        return result


@router.put('/canteen{canteen_id}/deactivate')
async def deactivate_parsing(canteen_id: int):
    """
    Функция деактивирует парсинг столовой

    :param canteen_id: ID столовой в базе данных
    """
    pass


@router.put('/canteen{canteen_id}/reactivate')
async def reactivate_parsing(canteen_id: int):
    """
    Функция реактивирует парсинг столовой

    :param canteen_id: ID столовой в базе данных
    """
    pass


@router.delete('/canteen{canteen_id}/deleteDishes')
async def delete_dishes(canteen_id: int):
    """
    Функция очищает меню столовой
    :param canteen_id: ID столовой в базе данных
    """
    await canteens_service.delele_menu(canteen_id=canteen_id)


