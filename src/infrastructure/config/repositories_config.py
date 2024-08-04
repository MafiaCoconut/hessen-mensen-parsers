from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.base import async_engine
from infrastructure.repositories_impl.canteens_repository_impl import CanteensRepositoryImpl
from infrastructure.repositories_impl.main_dishes_repository_impl import MainDishesRepositoryImpl
from infrastructure.repositories_impl.side_dishes_repository_impl import SideDishesRepositoryImpl


def get_canteens_repository() -> CanteensRepositoryImpl:
    session = AsyncSession(bind=async_engine, expire_on_commit=False)
    return CanteensRepositoryImpl(session=session)


def get_main_dishes_repository() -> MainDishesRepositoryImpl:
    session = AsyncSession(bind=async_engine, expire_on_commit=False)
    return MainDishesRepositoryImpl(session=session)


def get_side_dishes_repository() -> SideDishesRepositoryImpl:
    session = AsyncSession(bind=async_engine, expire_on_commit=False)
    return SideDishesRepositoryImpl(session=session)

