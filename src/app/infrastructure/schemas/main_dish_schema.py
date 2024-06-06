from pydantic import BaseModel


class MainDishBaseSchema(BaseModel):
    canteen_id: int
    name: str
    type: str
    price: str
    properties: str | None


class MainDishSchemaCreate(MainDishBaseSchema):
    pass


class MainDishSchema(MainDishBaseSchema):
    main_dish_id: int

