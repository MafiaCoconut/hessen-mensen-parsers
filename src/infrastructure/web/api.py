from fastapi import Depends
from sqlalchemy.orm import Session

from application.services.canteen_service import CanteenService
from infrastructure.config.repositories_config import canteens_repository
from infrastructure.web.fast_api_config import app
from infrastructure.db.base import get_db

# post - добавить
# put - обновить
# get - получить
# delete - удалить


@app.get('/canteens/{canteen_id}')
def read_canteens_menu(canteen_id: str, db: Session = Depends(get_db)):

    canteen_service = CanteenService(canteens_repository)
    return {canteen_service.get()}


@app.post('/start-parser/{canteen_id}')
def start_canteens_parser(canteen_id: str, db: Session = Depends(get_db)):
    pass
