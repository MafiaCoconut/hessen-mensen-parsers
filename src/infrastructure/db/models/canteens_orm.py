from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import TEXT, INTEGER
from infrastructure.db.base import Base
from infrastructure.db.models.orm_template_columns import intpk, created_at


class CanteensOrm(Base):
    __tablename__ = 'canteens'
    __table_args__ = {'extend_existing': True}

    canteen_id: Mapped[intpk]
    name: Mapped[str] = mapped_column(TEXT, nullable=True)
    description: Mapped[str] = mapped_column(TEXT, nullable=True)
    opened_time: Mapped[int] = mapped_column(INTEGER, nullable=True)
    closed_time: Mapped[int] = mapped_column(INTEGER, nullable=True)
    created_at: Mapped[created_at]



