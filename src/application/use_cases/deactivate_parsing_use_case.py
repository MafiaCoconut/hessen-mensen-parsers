from application.interfaces.scheduler_interface import SchedulerInterface
from application.repositories.canteens_repository import CanteensRepository


class DeactivateParsingUseCase:
    def __init__(self,
                 canteens_repository: CanteensRepository,
                 scheduler_interface: SchedulerInterface,
                 ):
        self.canteens_repository = canteens_repository
        self.scheduler_interface = scheduler_interface

    async def execute(self, canteen_id: int):
        await self.canteens_repository.update_status(canteen_id=canteen_id, new_status="deactivated")
        await self.scheduler_interface.get_all()
        # await self.scheduler_interface.remove(job_id="fgfjkl;")
    """
    1. Изменить параметр в бд
    2. Убрать из scheduler
    """

