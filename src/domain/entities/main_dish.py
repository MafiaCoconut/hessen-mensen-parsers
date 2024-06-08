from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class MainDish:
    main_dish_id: int | None
    canteen_id: int | None
    name: str | None
    type: str = field(default=None)
    price: str = field(default=None)
    properties: str = field(default=None)
    created_at: datetime = field(default=None)
    updated_at: datetime = field(default=None)


