from src.infrastructure.db.base import Base
from sqlalchemy import Column, Integer, String, DATETIME


class MainDish(Base):
    __tablename__ = 'main_dishes'

    main_dish_id = Column(Integer, primary_key=True, index=True)
    canteen_id = Column(Integer)
    name = Column(String)
    type = Column(String)
    price = Column(String)
    properties = Column(String)
    created_at = Column(DATETIME)
