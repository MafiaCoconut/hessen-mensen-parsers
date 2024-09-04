from fastapi import Depends, APIRouter, Response, status, BackgroundTasks
from sqlalchemy.orm import Session

from application.services.canteen_service import CanteensService
from application.services.scheduler_service import SchedulerService
from infrastructure.config.logs_config import log_api_decorator
from infrastructure.config.services_config import get_canteens_service, get_scheduler_service
from infrastructure.interfaces_impl.errors import ParserErrorCodes
from application.exceptions.repositories_exceptions import CanteenWrongDataException, CanteenNotFoundException

router = APIRouter()


@router.get("/")
@log_api_decorator
async def read_root(response: Response, ):
    return {"message": "Hello, World!"}


@router.get("/canteen{canteen_id}/getObject")
@log_api_decorator
async def get_canteen_object(canteen_id: int, response: Response, canteens_service=Depends(get_canteens_service)):
    try:
        result = await canteens_service.get_canteen_obj(canteen_id=int(canteen_id))
        return {'canteen': result.model_dump()}
    except CanteenWrongDataException as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'error': e}
    except CanteenNotFoundException as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'error': e}


@router.get("/canteen{canteen_id}/getDishes")
@log_api_decorator
async def get_canteens_data(canteen_id: int, response: Response, canteens_service=Depends(get_canteens_service)):
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
@log_api_decorator
async def start_all_canteens_parser(
        response: Response, background_tasks: BackgroundTasks,
        canteens_service=Depends(get_canteens_service)
):
    """
    Функция после запроса по API запускает парсинг всех столовых

    :return: None
    """
    background_tasks.add_task(canteens_service.parse_all_canteens)

    return {"message": "Request received, processing in background"}


@router.post('/canteen{canteen_id}/startParser')
@log_api_decorator
async def start_canteens_parser(canteen_id: int, response: Response, canteens_service=Depends(get_canteens_service)):
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
@log_api_decorator
async def deactivate_parsing(canteen_id: int, response: Response, canteens_service=Depends(get_canteens_service)):
    """
    Функция деактивирует парсинг столовой

    :param canteen_id: ID столовой в базе данных
    """
    await canteens_service.deactivate_canteen(canteen_id)


@router.put('/canteen{canteen_id}/reactivate')
@log_api_decorator
async def reactivate_parsing(canteen_id: int, response: Response, canteens_service=Depends(get_canteens_service)):
    """
    Функция реактивирует парсинг столовой

    :param canteen_id: ID столовой в базе данных
    """
    await canteens_service.reactivate_canteen(canteen_id)


# TODO доделать
# @router.delete('/canteen{canteen_id}/deleteDishes')
# async def delete_dishes(canteen_id: int, response: Response, canteens_service: CanteensService = Depends(get_canteens_service)):
#     """
#     Функция очищает меню столовой
#     :param canteen_id: ID столовой в базе данных
#     """
#     await canteens_service.delele_menu(canteen_id=canteen_id)


@router.get("/jobs/getAll")
@log_api_decorator
async def get_all_jobs(response: Response, scheduler_service: SchedulerService = Depends(get_scheduler_service)):
    return await scheduler_service.get_all_jobs()
