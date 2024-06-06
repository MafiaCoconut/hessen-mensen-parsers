from fastapi import Depends

from infrastructure.repositories_impl.canteens_repository_impl import CanteensRepositoryImpl
from infrastructure.db.base import get_db

# db_connection = Depends(get_db)
# canteens_repository = CanteensRepositoryImpl(db_connection=db_connection)
# main_dishes_repository = MainDishesRepositoryImpl()
# side_dishes_repository = SideDishesRepositoryImpl()
