from src.app.infrastructure.db.base import Base
from sqlalchemy import Column, Integer, String, DATETIME


class Canteen(Base):
    __tablename__ = 'canteens'

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DATETIME)