from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Canteen:
    canteen_id: int
    name: str
    created_at: Optional[datetime] = field(default=None)
