from application.repositories.canteens_repository import CanteensRepository


class GetCanteenUseCase:
    def __init__(self, canteens_repository: CanteensRepository):
        self.canteens_repository = canteens_repository

    def get(self, canteen_id: int):
        canteen = self.canteens_repository.get(canteen_id=canteen_id)
        if canteen is None:
            raise ValueError(f"Canteen with ID {canteen_id} does not exist.")

        text = "ID:{}\nНазвание: {}\n".format(
            canteen.canteen_id,
            canteen.name,
        )
        return text
