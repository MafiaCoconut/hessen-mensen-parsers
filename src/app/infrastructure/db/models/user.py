from src.app.infrastructure.db.base import Base
from sqlalchemy import Column, Integer, String, DATETIME


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    mailing_time = Column(DATETIME),
    language = Column(String)
    canteen_id = Column(Integer)
    created_at = Column(DATETIME)
