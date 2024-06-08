from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class SideDish:

    side_dish_id: int = field(default=None)
    canteen_id: int = field(default=None)
    name: str = field(default=None)
    type: str = field(default=None)
    price: str = field(default=None)
    properties: str = field(default=None)
    created_at: datetime = field(default=None)
    updated_at: datetime = field(default=None)
