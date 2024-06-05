from dataclasses import dataclass
from typing import Optional


@dataclass
class MainDish:
    id: Optional[int]
    name: str
    type: str
    price: str
    properties: str

