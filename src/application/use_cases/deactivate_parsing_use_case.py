from application.interfaces.scheduler_interface import SchedulerInterface
from application.repositories.canteens_repository import CanteensRepository
from application.use_cases.delete_jobs_by_canteen_use_case import DeleteJobsByCanteenUseCase


class DeactivateParsingUseCase:
    def __init__(self,
                 canteens_repository: CanteensRepository,
                 scheduler_interface: SchedulerInterface,
                 delete_jobs_use_case: DeleteJobsByCanteenUseCase,
                 ):
        self.canteens_repository = canteens_repository
        self.scheduler_interface = scheduler_interface
        self.delete_jobs_use_case = delete_jobs_use_case

    async def execute(self, canteen_id: int):

        await self.canteens_repository.update_status(canteen_id=canteen_id, new_status="deactivated")
        canteen = await self.canteens_repository.get(canteen_id=canteen_id)
        await self.scheduler_interface.get_all()
        await self.delete_jobs_use_case.execute(canteen=canteen)
        # await self.scheduler_interface.remove(job_id="fgfjkl;")
    """
    1. Изменить параметр в бд
    2. Убрать из scheduler
    """

