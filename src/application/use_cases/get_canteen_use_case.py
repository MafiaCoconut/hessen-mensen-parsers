from application.repositories.canteens_repository import CanteensRepository
from domain.entities.canteen import Canteen


class GetCanteenUseCase:
    def __init__(self, canteens_repository: CanteensRepository):
        self.canteens_repository = canteens_repository

    def get_text(self, canteen_id: int) -> str:
        canteen = self.canteens_repository.get(canteen_id=canteen_id)
        if canteen is None:
            raise ValueError(f"Canteen with ID {canteen_id} does not exist.")

        text = "ID:{}\nНазвание: {}\n".format(
            canteen.canteen_id,
            canteen.name,
        )
        return text

    def get_object(self, canteen_id: int) -> Canteen:
        canteen = self.canteens_repository.get(canteen_id=canteen_id)
        if canteen is None:
            raise ValueError(f"Canteen with ID {canteen_id} does not exist.")

        return Canteen(canteen_id=canteen.canteen_id, name=canteen.name, description=canteen.description,
                       opened_time=canteen.opened_time, closed_time=canteen.closed_time, created_at=canteen.created_at)
