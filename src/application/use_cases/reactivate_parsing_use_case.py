from typing import Callable

from application.interfaces.scheduler_interface import SchedulerInterface
from application.providers.repositories_provider import RepositoriesProvider
from application.repositories.canteens_repository import CanteensRepository
from application.use_cases.set_jobs_by_canteen_use_case import SetJobsByCanteenUseCase
from infrastructure.config.logs_config import log_decorator


class ReactivateParsingUseCase:
    def __init__(self,
                 repositories_provider: RepositoriesProvider,
                 scheduler_interface: SchedulerInterface,
                 set_jobs_use_case: SetJobsByCanteenUseCase,
                 ):
        self.repositories_provider = repositories_provider
        self.scheduler_interface = scheduler_interface
        self.set_jobs_use_case = set_jobs_use_case

    @log_decorator(print_args=False)
    async def execute(self, canteen_id: int, func: Callable):
        canteens_repository = self.repositories_provider.get_canteens_repository()

        await canteens_repository.update_status(canteen_id=canteen_id, new_status="active")
        canteen = await canteens_repository.get(canteen_id=canteen_id)
        await self.scheduler_interface.get_all()
        await self.set_jobs_use_case.execute(canteen=canteen, func=func)

