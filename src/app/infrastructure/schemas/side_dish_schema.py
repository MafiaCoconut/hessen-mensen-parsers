from pydantic import BaseModel


class SideDishBaseSchema(BaseModel):
    canteen_id: int
    name: str
    type: str | None
    price: str
    properties: str | None


class SideDishSchemaCreate(SideDishBaseSchema):
    pass


class SideDishSchema(SideDishBaseSchema):
    main_dish_id: int

