from src.infrastructure.db.base import Base
from sqlalchemy import Column, Integer, String, DATETIME


class Canteen(Base):
    __tablename__ = 'canteens'

    canteen_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    opening_time = Column(DATETIME)
    closing_time = Column(DATETIME)
    created_at = Column(DATETIME)
