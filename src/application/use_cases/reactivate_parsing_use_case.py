from typing import Callable

from application.interfaces.scheduler_interface import SchedulerInterface
from application.repositories.canteens_repository import CanteensRepository
from application.use_cases.set_jobs_by_canteen_use_case import SetJobsByCanteenUseCase


class ReactivateParsingUseCase:
    def __init__(self,
                 canteens_repository: CanteensRepository,
                 scheduler_interface: SchedulerInterface,
                 set_jobs_use_case: SetJobsByCanteenUseCase,
                 ):
        self.canteens_repository = canteens_repository
        self.scheduler_interface = scheduler_interface
        self.set_jobs_use_case = set_jobs_use_case

    async def execute(self, canteen_id: int, func: Callable):
        await self.canteens_repository.update_status(canteen_id=canteen_id, new_status="active")
        canteen = await self.canteens_repository.get(canteen_id=canteen_id)
        await self.scheduler_interface.get_all()
        await self.set_jobs_use_case.execute(canteen=canteen, func=func)

