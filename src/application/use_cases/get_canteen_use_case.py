from application.repositories.canteens_repository import CanteensRepository


class GetCanteenUseCase:
    def __init__(self, canteens_repository: CanteensRepository):
        self.canteens_repository = canteens_repository

    def execute(self):
        canteen = self.canteens_repository.get()
        # TODO переделать на fluent
        text = "ID:{}\nНазвание: {}\nВремя открытия: {}\nВремя закрытия: {}".format(
            canteen.canteen_id,
            canteen.name,
            canteen.opening_time,
            canteen.closing_time
        )
        return text
