from sqlalchemy.orm import Mapped, mapped_column
from infrastructure.db.base import Base
from infrastructure.db.models.orm_template_columns import intpk, created_at


class CanteensOrm(Base):
    __tablename__ = 'canteens'

    canteen_id: Mapped[intpk]
    name: Mapped[str] = mapped_column()
    created_at: Mapped[created_at]




