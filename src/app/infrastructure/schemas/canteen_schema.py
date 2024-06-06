from pydantic import BaseModel


class CanteenBase(BaseModel):
    name: str


class Canteen(CanteenBase):
    canteen_id: int
