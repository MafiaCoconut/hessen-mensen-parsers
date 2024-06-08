from application.repositories.canteens_repository import CanteensRepository


class GetCanteenUseCase:
    def __init__(self, canteens_repository: CanteensRepository):
        self.canteens_repository = canteens_repository

    def get(self, canteen_id: int):
        canteen = self.canteens_repository.get(canteen_id=canteen_id)
        # TODO переделать на fluent
        text = "ID:{}\nНазвание: {}\n".format(
            canteen.canteen_id,
            canteen.name,
        )
        return text
