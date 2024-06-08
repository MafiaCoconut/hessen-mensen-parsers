from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text, ForeignKey
from typing import Annotated
from infrastructure.db.base import Base
from infrastructure.db.models.orm_template_columns import intpk, created_at, updated_at


class MainDishesOrm(Base):
    __tablename__ = 'main_dishes'

    main_dish_id: Mapped[intpk]

    name: Mapped[str]
    type: Mapped[str]
    price: Mapped[str]
    properties: Mapped[str]
    canteen_id: Mapped[int] = mapped_column(ForeignKey("canteens.canteen_id", ondelete="CASCADE"))

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
