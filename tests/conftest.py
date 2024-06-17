import sys
import os
from pathlib import Path
import pytest
from icecream import ic

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

sys.path.append(str(Path(__file__).parent.parent))

from infrastructure.db.models.canteens_orm import CanteensOrm
from infrastructure.db.base import Base, sync_engine

# Импорт фикстур
from tests.fixtures.entities_fixtures import *
from tests.fixtures.databases_fixtures import *
from tests.fixtures.services_fixtures import *
from tests.fixtures.interfaces_fixtures import *
from tests.fixtures.repositories_fixtures import *

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Создание таблиц перед выполнением тестов и удаление после."""
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)

    yield






# @pytest.fixture(scope="session")
# def db_session(db_engine):
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
#
#     connection = db_engine.connect()
#     transaction = connection.begin()
#     session = SessionLocal(bind=connection)
#
#     yield session
#
#     session.close()
#     transaction.rollback()
#     connection.close()
