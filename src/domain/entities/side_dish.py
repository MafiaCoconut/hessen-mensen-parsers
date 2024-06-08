from dataclasses import dataclass, field
from datetime import datetime

from src.infrastructure.db.base import Base
from sqlalchemy import Column, Integer, String, DATETIME

@dataclass
class SideDish(Base):

    side_dish_id: int | None
    canteen_id: int | None
    name: str
    type: str = field(default=None)
    price: str = field(default=None)
    properties: str = field(default=None)
    created_at: datetime = field(default=None)
    updated_at: datetime = field(default=None)
