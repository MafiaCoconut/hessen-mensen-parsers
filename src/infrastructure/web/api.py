from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from application.services.canteen_service import CanteenService
from domain.entities.canteen import Canteen
from infrastructure.db.base import get_db
from infrastructure.repositories_impl.canteens_repository_impl import CanteensRepositoryImpl

router = APIRouter()

@router.get("/canteens/{canteen_id}")
def read_canteens_menu(canteen_id: int, db: Session = Depends(get_db)):
    canteens_repository = CanteensRepositoryImpl(db_connection=db)

    canteen_service = CanteenService(canteens_repository)
    return {canteen_service.get(canteen_id=canteen_id)}


@router.post('/start-parser/{canteen_id}')
def start_canteens_parser(canteen_id: str):
    pass

@router.get('/start')
def start_canteens_parser():
    return {"Hello world"}
