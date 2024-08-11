from abc import abstractmethod, ABC
from typing import List
from sqlalchemy.orm import Session

from domain.entities.canteen import Canteen


class CanteensRepository(ABC):

    @abstractmethod
    async def get_all(self) -> List[Canteen]:
        pass

    @abstractmethod
    async def get(self, canteen_id: int) -> Canteen:
        pass

    @abstractmethod
    async def save(self, canteen: Canteen) -> None:
        pass

    @abstractmethod
    async def delete_all(self) -> None:
        pass

    @abstractmethod
    async def delete(self, canteen_id: int) -> None:
        pass

    @abstractmethod
    async def update_status(self, canteen_id: int, new_status: str) -> None:
        pass




