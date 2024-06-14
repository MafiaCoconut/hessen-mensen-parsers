import sys
import os
from pathlib import Path

print('----------')
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

sys.path.append(str(Path(__file__).parent.parent))

from tests.fixtures.databases_fixtures import *
from tests.fixtures.repositories_fixtures import *
# from tests.fixtures.entities_fixtures import *

from tests.fixtures.services_fixtures import *
from tests.fixtures.interfaces_fixtures import *


# TEST_DATABASE_URL = "jdbc:postgresql://localhost:5432/test_database"


from src.infrastructure.db.base import Base, sync_engine, db_settings
# from src.infrastructure.db.models.canteens_orm import CanteensOrm
# from src.infrastructure.db.models.main_dishes_orm import MainDishesOrm
# from src.infrastructure.db.models.side_dishes_orm import SideDishesOrm

@pytest.fixture(scope="session", autouse=True)
def db_engine():
    Base.metadata.create_all(sync_engine)
    print(db_settings.DB_NAME, db_settings.MODE)
    print('данные дропнулись')
    assert db_settings.MODE == "TEST"

    # yield sync_engine
    # Base.metadata.drop_all(bind=engine)


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
