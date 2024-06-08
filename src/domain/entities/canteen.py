from datetime import datetime

from infrastructure.db.base import Base
from sqlalchemy import Column, Integer, String, DATETIME, Table, MetaData

# metadata_obj = MetaData()
#
# canteens_table = Table(
#     "canteens",
#     metadata_obj,
#     Column('canteen_id', Integer, primary_key=True),
#     Column('name', String),
#
# )


class Canteen:
    canteen_id: int
    name: str
    created_at: datetime


# class Canteen(Base):
#     __tablename__ = 'canteens'
#
#     canteen_id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     opening_time = Column(DATETIME)
#     closing_time = Column(DATETIME)
#     created_at = Column(DATETIME)
